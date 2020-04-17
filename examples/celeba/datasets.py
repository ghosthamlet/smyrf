import torch
import torchvision.datasets as dsets
import torchvision
from torchvision import transforms
from PIL import Image
import os
from tqdm import tqdm
import torch.utils.data as data


class CelebAHQ(data.Dataset):
    def __init__(self, img_path, transform_img, mode):
        self.img_path = img_path
        self.transform_img = transform_img
        self.train_dataset = []
        self.test_dataset = []
        self.mode = mode
        self.preprocess()

        if mode == True:
            self.num_images = len(self.train_dataset)
        else:
            self.num_images = len(self.test_dataset)

    def preprocess(self):
        length = len([name for name in os.listdir(self.img_path) if os.path.isfile(os.path.join(self.img_path, name))])
        for i in tqdm(range(length)):
            img_path = os.path.join(self.img_path, str(i)+ '.jpg')
            print(img_path)
            if self.mode == True:
                self.train_dataset.append(img_path)
            else:
                self.test_dataset.append(img_path)
        print('Finished preprocessing the CelebA dataset...')


    def __getitem__(self, index):
        dataset = self.train_dataset if self.mode == True else self.test_dataset
        img_path = dataset[index]
        image = Image.open(img_path)
        return self.transform_img(image)


    def __len__(self):
        """Return the number of images."""
        return self.num_images



if __name__ == '__main__':
    transform = transforms.Compose([transforms.ToTensor(), lambda x: x.cuda()])
    dataset = CelebAHQ('CelebAMask-HQ/CelebA-HQ-img', transform, True)
    loader = torch.utils.data.DataLoader(dataset=dataset,
                                         batch_size=1,
                                         num_workers=6,
                                         shuffle=True,
                                         drop_last=True)