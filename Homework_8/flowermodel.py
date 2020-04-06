import torchvision.datasets as datasets
from torchvision.transforms import transforms
from torch.utils.data import DataLoader
from torchvision.utils import make_grid
from util import show_transformed_image
import torch.nn as nn

class FlowerModel:
    def __init__(self):
        self.cnn_model = FlowerClassifierCNNModel()
        pass
        # myModel = FlowerModel()
        # myModel.train()


    def train_and_build(self, n_epoches):
        for epoch in range(n_epoches):
            self.cnn_model.train()
        for i, (images, labels) in enumerate(train_dataset_loader):
            optimizer.zero_grad()
            outputs = cnn_model(images)
            loss = loss_fn(outputs, labels)
            loss.backward()
            optimizer.step()

    def predict(self, test_img):
        test_image = Image.open(test.img)
        test_image_tensor = transformations(test_image).float()
        test_image_tensor = test_image_tensor.unsqueeze_(0)
        output = cnn_model(test_image_tensor)
        class_index = output.data.numpy().argmax()


    def pre_processing(self, datadir='./data/'):
        transformations = transforms.Compose([
            transforms.RandomResizedCrop(64),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])

        total_dataset = datasets.ImageFolder(datadir, transform=transformations)
        dataset_loader = DataLoader(dataset=total_dataset, batch_size=100)
        items = iter(dataset_loader)
        image, label = items.next()
        show_transformed_image(make_grid(image))


class FlowerClassifierCNNModel(nn.Module):

    def __init__(self, num_classes=5):
        super(FlowerClassifierCNNModel, self).__init__()

        self.conv1 = nn.Conv2d(in_channels=3, out_channels=12, kernel_size=3, stride=1, padding=1)
        self.relu1 = nn.ReLU()

        self.maxpool1 = nn.MaxPool2d(kernel_size=2)

        self.conv2 = nn.Conv2d(in_channels=12, out_channels=24, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()

        self.lf = nn.Linear(in_features=32 * 32 * 24, out_features=num_classes)

    def forward(self, input):
        output = self.conv1(input)
        output = self.relu1(output)

        output = self.maxpool1(output)

        output = self.conv2(output)
        output = self.relu2(output)

        output = output.view(-1, 32 * 32 * 24)

        output = self.lf(output)

        return output