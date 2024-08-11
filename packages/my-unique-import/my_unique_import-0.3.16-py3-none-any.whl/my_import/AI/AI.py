import datetime
import sys
import torch.optim.lr_scheduler as _lr_scheduler
import torch
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torchvision import datasets, transforms, models
from torch.utils.tensorboard import SummaryWriter
import os
import glob
from my_import.class_builder import ClassBuilder
import subprocess
import numpy as np

lr_scheduler = _lr_scheduler


def get_gpu():
    if torch.cuda.is_available():
        return torch.device('cuda')


class MyDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]


class MyDataLoader:

    def __init__(self, data_dir, batch=32, shuffle=True, transform=None, image_size=None):
        if image_size is None:
            image_size = 128
        if transform is None:
            transform = transforms.Compose([
                transforms.Resize((image_size, image_size)),
                transforms.ToTensor(),
                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
            ])
        self.transform = transform
        train_dataset = datasets.ImageFolder(root=f'{data_dir}/train', transform=transform)
        val_dataset = datasets.ImageFolder(root=f'{data_dir}/val', transform=transform)
        test_dataset = datasets.ImageFolder(root=f'{data_dir}/test', transform=transform)
        self.train_loader = DataLoader(train_dataset, batch_size=batch, shuffle=shuffle)
        self.val_loader = DataLoader(val_dataset, batch_size=batch, shuffle=False)
        self.test_loader = DataLoader(test_dataset, batch_size=batch, shuffle=False)
        self.classes = train_dataset.classes
        value = next(iter(train_dataset))
        self.size = value[0].size()
        self.batch_size = batch
        print(self.size)
        self.data_dir = data_dir

    def check(self):
        for images, labels in self.train_loader:
            print(f'Image batch dimensions: {images.size()}')
            print(f'Image label dimensions: {labels.size()}')
            break

    def get_batch_index(self, index):
        test_batches = list(self.test_loader)
        return test_batches[index][0]


class Trainer:

    def __init__(self, model: nn.Module, data_loader: MyDataLoader, criterion=None, optimizer=None, device=None,
                 auto_classifer=True, log_dir=None, is_model_graph=True, auto_save=True, writer=None,
                 verbose=0, evaluation_interval=10, mem_threshold=0.9, lr=0.01, scheduler=None,
                 patience=5, save_interval=10, **kwargs):
        self.params = ClassBuilder.get_params()

        if device is None:
            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        if isinstance(data_loader, str):
            data_loader = MyDataLoader(data_loader)
        if isinstance(model, str):
            model = torch.load(model)
        print('Using device: {device}'.format(device=device))
        if auto_classifer:
            num_ftrs = model.fc.in_features
            num_classes = len(data_loader.classes)
            model.fc = nn.Linear(num_ftrs, num_classes)
        self.device = device
        self.verbose = verbose
        self.model = model.to(device)
        self.data_loader = data_loader
        self.criterion = criterion if criterion is not None else Loss.CrossEntropyLoss()  # nn.CrossEntropyLoss()
        self.optimizer = optimizer if optimizer is not None else optim.SGD(model.parameters(), lr=lr)
        self.lr = lr
        self.save_interval = save_interval
        if callable(self.optimizer):
            self.optimizer = self.optimizer(self.model.parameters())
        if writer is None:
            writer = SummaryWriter(log_dir)
        self.log_dir = log_dir if log_dir is not None else writer.get_logdir()
        self.writer = writer
        self.auto_save = auto_save
        self.epoch = kwargs.get('epoch', 0)
        self.is_model_graph = is_model_graph
        self.evaluation_interval = evaluation_interval
        self.mem_threshold = mem_threshold
        self.scheduler = scheduler
        self.patience = patience
        self.best_loss = np.inf
        self.early_stop_counter = 0
        if is_model_graph:
            sample_data, _ = next(iter(data_loader.train_loader))
            self.add_model_graph(sample_data)

    def _early_stop(self, average_loss, epoch):
        if average_loss < self.best_loss:
            self.best_loss = average_loss
            self.early_stop_counter = 0
            self.save_model(path=f'models/best_model.pth', epoch=epoch)
        else:
            self.early_stop_counter += 1

        if self.early_stop_counter >= self.patience:
            print(f"Early stopping triggered at epoch {epoch + 1}")
            return -1
        return 0

    def add_model_graph(self, data_sample):
        self.writer.add_graph(self.model, data_sample.to(self.device))

    def train(self, num_epochs):
        if self.verbose == 2:
            self.show()
        device = self.device
        total_epochs = self.epoch + num_epochs
        outer_tqdm = tqdm(range(self.epoch, total_epochs), desc='Epochs', unit='epoch', position=0, leave=False)
        for epoch in outer_tqdm:
            self.model.train()
            running_loss = 0.0
            inner_tqdm = tqdm(self.data_loader.train_loader, desc=f'Epoch {epoch + 1}/{total_epochs}', unit='batch',
                              position=1, leave=False)
            for data, labels in inner_tqdm:
                # data, labels = self.data_processing(data, labels)
                # outputs = self._predict(data)
                # loss = self.criterion(outputs, labels)
                loss, _ = self.train_method(data, labels)

                self.backward(loss)

                loss_value = self.loss_value(loss)
                running_loss += loss_value
                inner_tqdm.set_postfix(loss=loss_value)

            mem_allocated = torch.cuda.memory_allocated(device)
            mem_reserved = torch.cuda.memory_reserved(device)
            if mem_allocated / mem_reserved > self.mem_threshold:
                tqdm.write("The memory allocation is close to the maximum, So Ending the training")
                return

            epoch_loss = running_loss / len(self.data_loader.train_loader)
            outer_tqdm.set_postfix(loss=epoch_loss)
            self.writer.add_scalar('Loss/Training', epoch_loss, epoch)
            self.writer.add_scalar('Learning Rate', self.get_lr(), epoch)
            self._auto_save(epoch)
            if self._evaluation(epoch) == -1:
                return

            self.scheduler_step()
        self.epoch += num_epochs

    def train_method(self, data, labels):
        data, labels = data.to(self.device), labels.to(self.device)
        outputs = self._predict(data)
        loss = self.criterion(outputs, labels)
        return loss, outputs

    def loss_value(self, loss):
        return loss.item()

    def backward(self, loss):
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

    @staticmethod
    def is_inverval(epoch, interval):
        return epoch % interval == 0 and epoch != 0

    def _evaluation(self, epoch):
        if Trainer.is_inverval(epoch, self.evaluation_interval):
            accuracy, avg_loss = self.evaluate()
            self.writer.add_scalar('Accuracy/Validation', accuracy, epoch)
            self.writer.add_scalar('Loss/Validation', avg_loss, epoch)
            early_stop = self._early_stop(average_loss=avg_loss, epoch=epoch)
            return early_stop
        return 0

    def scheduler_step(self):
        if self.scheduler is not None:
            self.scheduler.step()

    def _auto_save(self, epoch):
        if Trainer.is_inverval(epoch, self.save_interval):
            self.save_model(path='models/model_epoch_{:02d}.pth'.format(epoch), epoch=epoch)

    def evaluate(self, data_loader=None, phase='Validation'):
        if data_loader is None:
            data_loader = self.data_loader.val_loader
        self.model.eval()
        correct = 0
        total = 0
        running_loss = 0.0
        with torch.no_grad():
            for data, labels in tqdm(data_loader, desc='Evaluating', unit='batch'):
                loss, outputs = self.train_method(data, labels)
                running_loss += self.loss_value(loss)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        accuracy = 100 * correct / total
        avg_loss = running_loss / len(data_loader)
        tqdm.write(f'{phase} Accuracy: {accuracy}%')
        tqdm.write(f'{phase} Average loss: {avg_loss}')
        return accuracy, avg_loss

    def test(self):
        return self.evaluate(self.data_loader.test_loader, phase='Test')

    def _predict(self, *args, **kwargs):
        return self.model(*args, **kwargs)

    def adjust_tensor_size(self, x):
        x1, x2, x3 = self.data_loader.size[0], self.data_loader.size[1], self.data_loader.size[2]

        if x.dim() == 3 and x.size(0) == x1 and x.size(1) == x2 and x.size(2) == x3:
            x = x.unsqueeze(0)
        elif x.dim() != 4 or x.size(1) != x1 or x.size(2) != x2 or x.size(3) != x3:
            raise ValueError("输入张量的尺寸不匹配")

        return x

    def predict(self, data, transform=False, full=False):
        if transform and not isinstance(data, torch.Tensor):
            data = self.data_loader.transform(data)
        data = self.adjust_tensor_size(data)
        outputs = self._predict(data.to(self.device))
        if full:
            return F.normalize(outputs, p=1, dim=1)
        _, predicted = torch.max(outputs.data, 1)
        return predicted

    def close(self):
        self.writer.close()

    def save_model(self, path='models/model.pth', epoch=None):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if epoch is None:
            epoch = self.epoch
        torch.save({
            'epoch': epoch,
            'model_state_dict': self.model.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict(),
            'loss': self.criterion,
        }, path)
        print(f'Model saved at epoch {epoch}')

    def load_model(self, path=None):
        if path is None:
            model_files = glob.glob('models/*')

            def extract_epoch(filename):
                try:
                    # 提取文件名的最后一个部分并转换为整数
                    return int(filename.split('_')[-1].split('.')[0])
                except (IndexError, ValueError):
                    # 如果提取失败，则返回一个最小值，这样这些文件不会被选中
                    return -1

            # 过滤掉无效的文件名
            valid_files = [f for f in model_files if extract_epoch(f) != -1]

            if not valid_files:
                raise ValueError("No valid model files found.")
            max_epoch_file = max(valid_files, key=extract_epoch)
            path = max_epoch_file
        if not os.path.exists(path):
            raise FileNotFoundError(f"No checkpoint found at '{path}'")
        print(f'Loading model from path {path}')
        checkpoint = torch.load(path, weights_only=False)
        self.model.load_state_dict(checkpoint['model_state_dict'])
        self.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        epoch = checkpoint['epoch']
        loss = checkpoint['loss']
        self.model.to(self.device)
        print(f'Model loaded from epoch {epoch}')
        return epoch, loss

    def save(self, path):
        if '.pth' in path:
            return self._save_config(path)
        os.makedirs(path, exist_ok=True)
        # self.save_model(os.path.join(path, 'model_weights.pth'))
        return self._save_config(os.path.join(path, 'trainer.pth'))

    def _save_config(self, path):

        try:
            torch.save({'model': self.model, 'epoch': self.epoch,
                        'optimizer': self.optimizer, 'criterion': self.criterion,
                        'device': self.device, 'log_dir': self.log_dir, 'verbose': self.verbose,
                        'is_model_graph': self.is_model_graph, 'auto_classifer': False,
                        'auto_save': self.auto_save, 'data_loader': self.data_loader},
                       path)
            print('Saved model configuration successfully')
            return True
        except Exception as e:
            print(f'Error saving model configuration: {str(e)}')
            return False

    @staticmethod
    def load(path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"No checkpoint found at '{path}'")
        params = torch.load(os.path.join(path, 'trainer.pth'))
        return Trainer(**params)

    def show(self):
        print(self.log_dir)
        subprocess.Popen(['tensorboard', '--logdir', os.path.dirname(self.log_dir)])

        print(f"TensorBoard is running. Open http://localhost:6006/ in your browser.")

    def set_scheduler(self, scheduler, **kwargs):
        self.scheduler = scheduler(self.optimizer, **kwargs)

    def get_lr(self):
        if self.scheduler is None:
            return self.optimizer.param_groups[0]['lr']
        else:
            return self.scheduler.get_last_lr()[0]


class Models:

    @staticmethod
    def resnet18(pretrained=True):
        return models.resnet18(weights=pretrained)

    @staticmethod
    def alexnet(pretrained=True):
        return models.alexnet(weights=pretrained)

    @staticmethod
    def vgg16(pretrained=True):
        return models.vgg16(weights=pretrained)

    @staticmethod
    def densenet121(pretrained=True):
        return models.densenet121(weights=pretrained)

    @staticmethod
    def squeezenet1_0(pretrained=True):
        return models.squeezenet1_0(weights=pretrained)


class Optimizer:
    SGD = optim.SGD
    Adam = optim.Adam


class Loss:
    CrossEntropyLoss = nn.CrossEntropyLoss
    MSELoss = nn.MSELoss
    BCELoss = nn.BCELoss
    NLLLoss = nn.NLLLoss
    L1Loss = nn.L1Loss
    SmoothL1Loss = nn.SmoothL1Loss
    CTCLoss = nn.CTCLoss


class Function:
    normalize = F.normalize


class TrainAndTest:

    def __init__(self, train, test):
        self.__call__(train, test)

    def __call__(self, train, test):
        args = sys.argv[1] if len(sys.argv) > 1 else None
        if args is not None:
            if args == 'train':
                return train()
            elif args == 'test':
                return test()
        return None
