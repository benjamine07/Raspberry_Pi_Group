import torchvision.datasets as datasets
from torch import nn
from torchvision.transforms import transforms
from torch.utils.data import DataLoader
from torchvision.utils import make_grid
from PIL import Image

from flowernet import FlowerClassifierCNNModel
from util import show_transformed_image
from torch.optim import Adam
from torch.utils.data import random_split


class FlowerModel:
    def __init__(self, data_folder="./data"):
        self.cnn_model = FlowerClassifierCNNModel()
        self.optimizer = Adam(self.cnn_model.parameters())
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

        train_size = int(0.8 * len(total_dataset))
        test_size = len(total_dataset) - train_size
        train_dataset, test_dataset = random_split(total_dataset, [train_size, test_size])

        self.train_dataset_loader = DataLoader(dataset=train_dataset, batch_size=100)
        self.test_dataset_loader = DataLoader(dataset=test_dataset, batch_size=100)

    def train(self, epoches=20):
        for epoch in range(epoches):
            self.cnn_model.train()
            for i, (images, labels) in enumerate(self.train_dataset_loader):
                self.optimizer.zero_grad()
                outputs = self.cnn_model(images)
                loss = self.loss_fn(outputs, labels)
                print("iteration " + str(i) + ": " + str(loss))

                loss.backward()
                self.optimizer.step()

    def predict(self, filename):
        test_image = Image.open(filename)
        test_image_tensor = self.transformations(test_image).float()
        test_image_tensor = test_image_tensor.unsqueeze_(0)
        output = self.cnn_model(test_image_tensor)
        class_index = output.data.numpy().argmax()
