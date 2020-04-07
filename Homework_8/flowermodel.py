import torchvision.datasets as datasets
from torch import nn
from torchvision.transforms import transforms
from torch.utils.data import DataLoader
from torchvision.utils import make_grid
from PIL import Image
import torch
from torch.autograd import Variable

from flowernet import FlowerClassifierCNNModel
from util import show_transformed_image
from torch.optim import Adam
from torch.utils.data import random_split


class FlowerModel:
    def __init__(self, data_folder="./data", cudaready=False):
        self.cuda = cudaready
        self.cnn_model = FlowerClassifierCNNModel()

        if (self.cuda):
            self.cnn_model.cuda()

        self.optimizer = Adam(self.cnn_model.parameters())
        if (self.cuda):
            self.loss_fn = nn.CrossEntropyLoss().cuda()
        else:
            self.loss_fn = nn.CrossEntropyLoss()

        # load data
        self.transformations = transforms.Compose([
            transforms.RandomResizedCrop(64),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])

        total_dataset = datasets.ImageFolder(data_folder, transform=self.transformations)
        dataset_loader = DataLoader(dataset=total_dataset, batch_size=100)
        items = iter(dataset_loader)
        image, label = items.next()
        print(len(total_dataset))
        train_size = int(0.8 * len(total_dataset))
        test_size = len(total_dataset) - train_size
        train_dataset, test_dataset = random_split(total_dataset, [train_size, test_size])

        self.train_dataset_loader = DataLoader(dataset=train_dataset, batch_size=100)
        self.test_dataset_loader = DataLoader(dataset=test_dataset, batch_size=100)

    def train(self, epoches=20):
        for epoch in range(epoches):
            self.cnn_model.train()
            cnt=0
            for i, (images, labels) in enumerate(self.train_dataset_loader):
                if (self.cuda):
                    images, labels = Variable(images.cuda(non_blocking=True)), Variable(labels.cuda(non_blocking=True))
                else:
                    images, labels = Variable(images), Variable(labels)

                self.optimizer.zero_grad()
                outputs = self.cnn_model(images)

                if self.cuda:
                    outputs = self.cnn_model(images).cuda(non_blocking=True)
                else:
                    outputs = self.cnn_model(images)
                outputs = outputs.squeeze()
                loss = self.loss_fn(outputs, labels)
                loss.backward()
                self.optimizer.step()

                #print("iteration " + str(i) + ": " + str(loss))
                cnt=cnt+1
                if i % 5 == 4:  # print every 5 mini-batches
                    print('[%d, %5d] loss: %.6f' % (epoch + 1, i + 1, loss / (i + 1)))

            print(cnt)
        print(epoch)

    def saveModel(self, mfile='model.pth'):
        print('Saving Model ')
        torch.save(self.cnn_model.state_dict(), mfile)

    def loadModel(self, mfile='model.pth'):
        self.cnn_model.load_state_dict(torch.load(mfile, map_location=lambda storage, loc: storage))


    def predict(self, filename):
        test_image = Image.open(filename)
        test_image_tensor = self.transformations(test_image).float()

        if (self.cuda):
            test_image_tensor = Variable(test_image_tensor.cuda(non_blocking=True))
            output = self.cnn_model(test_image_tensor).cuda(non_blocking=True)
        else:
            test_image_tensor = test_image_tensor.unsqueeze_(0)
            output = self.cnn_model(test_image_tensor)

        output = self.cnn_model(test_image_tensor)
        class_index = output.data.numpy().argmax()

        return class_index