# coding: utf-8
try:
    import urllib.request
except ImportError:
    raise ImportError('You should use Python 3.x')
#import os.path
#import gzip
#import pickle
#import os
#import numpy as np
from PIL import Image

def load_img(file):
    im = Image.open(file)
    pix = im.load()
    x = im.size[0]
    y = im.size[1]
    print("x=",x,"y=",y)

    #one = pix.reshape(-1,1,10,10)
    print(pix[0,0])


if __name__ == '__main__':
    load_img('im1.png')

#def load_image(normalize=True, flatten=True, one_hot_label=False):
#
#    if not os.path.exists(save_file):
#        init_mnist()
#
#    with open(save_file, 'rb') as f:
#        dataset = pickle.load(f)
#
#    if normalize:
#        for key in ('train_img', 'test_img'):
#            dataset[key] = dataset[key].astype(np.float32)
#            dataset[key] = 255.0
#
#    if one_hot_label:
#        dataset['train_label'] = _change_one_hot_label(dataset['train_label'])
#        dataset['test_label'] = _change_one_hot_label(dataset['test_label'])
#
#    if not flatten:
#         for key in ('train_img', 'test_img'):
#            dataset[key] = dataset[key].reshape(-1, 1, 28, 28)
#
#    return (dataset['train_img'], dataset['train_label']), (dataset['test_img'], dataset['test_label'])