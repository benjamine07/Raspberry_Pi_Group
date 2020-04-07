from util import show_image
from flowermodel import FlowerModel

a = FlowerModel()
a.train(epoches=200)
a.predict("./data/daisy/5547758_eea9edfd54_n.jpg")
