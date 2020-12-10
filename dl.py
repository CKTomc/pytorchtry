from torch.utils.data import Dataset, DataLoader
import pandas
from torchvision import transforms
from matplotlib.pyplot import imshow
import matplotlib.pylab as plt
import pandas as pd
from PIL import Image

traindataname='https://cocl.us/DL0320EN_TRAIN_CSV'
train_data_name = pd.read_csv(traindataname)
train_data_name.head()

#get the file name stored in the first row (names are stored in the 3rd column)
print('File name:', train_data_name.iloc[0, 2])
#get the file class stored in the first row (classes are stored in the 4th column)
print('File name:', train_data_name.iloc[0, 3])
#number of records
print('Rows:',train_data_name.shape[0])

validationdataname='https://cocl.us/DL0320EN_VALID_CSV'
validation_data_name=pd.read_csv(validationdataname)

"""train_data_dir=<dir>
#load an image
train_image=train_data_dir+train_data_name.iloc[25,3]
img=Image.open(train_image)
plt.imshow(image)
plt.show()"""


class Dataset(dataset):

    def __init__(self, csv_file, data_dir, transform=None):
        self.data_dir=data_dir        
        self.transform=transform
        self.data_name=pd.read_csv(csv_file)
        self.len=self.data_name.shape[0] 
    
    # number of records
    def __len__(self):
        return self.len
    
    #get an image using data dir and data_name
    def __getitem__(self, numrecord):
        img_name=self.data_dir+self.data_name.iloc[idx, 2]
        img=Image.open(img_name)
        cls=self.data_name.iloc[numrecord,3] 
        # apply transform method if there is any
        if self.transform:
            img = self.transform(img)

        return img,cls
