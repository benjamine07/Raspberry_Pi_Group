from util import show_image
from flowermodel import FlowerModel

# a=FlowerModel()
a = FlowerModel()
a.pre_processing()
a.train_and_build(20)
a.predict("./data/daisy/5547758_eea9edfd54_n.jpg")