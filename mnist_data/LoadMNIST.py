import urllib.request
import os.path
import gzip
import numpy as np
import pdb
import sys

'''
*Reference URL*
https://endoyuta.com/2017/01/12/python-mnistを使う/
http://yann.lecun.com/exdb/mnist/
'''


__file__ = 'mnist_data/'#there are perseptron datas in this path.
url_base = 'http://yann.lecun.com/exdb/mnist/'
key_file = {
    'train_img':'train-images-idx3-ubyte.gz',#rename filename
    'train_label':'train-labels-idx1-ubyte.gz',
    'test_img':'t10k-images-idx3-ubyte.gz',
    'test_label':'t10k-labels-idx1-ubyte.gz'
}
dataset_dir = os.path.dirname(os.path.abspath(__file__))

def _download(filename):
    file_path = dataset_dir + '/' + filename
    if os.path.exists(file_path):
        return print('already exist')
    print('Downloading ' + filename + ' ...')
    urllib.request.urlretrieve(url_base + filename, file_path)
    print('Done')

def download_mnist():
    for v in key_file.values():
       _download(v)

#ALREADDY DOWNLOADED!!!
#download_mnist()
'''
def load_mnist(filename, dat_size = 784, offset = 16):#dat means 'this'
    file_path = dataset_dir + '/' + filename
    with gzip.open(file_path, 'rb') as f:
        data = np.frombuffer(f.read(), np.uint8, offset= offset)
    return data.reshape(-1, dat_size)
'''
def load_mnist(filename, datapath, dat_size = 784, offset = 16):#dat means 'this'
    sys.path.append('datapath')
    file_path = os.path.join(datapath, filename )
    #file_path = dataset_dir + '/' + filename
    with gzip.open(file_path, 'rb') as f:
        data = np.frombuffer(f.read(), np.uint8, offset= offset)
    return data.reshape(-1, dat_size)

'''
For image Download, set offset to be 16, dat_size = 784
For label Download, set offset to be 8, dat_size = 1
Img's dat_size is picture size 24*24 = 784
Label's data_size is list size (1)
Img's offset is 16 bits. because 8*2(=16) bits are required to express 2-dimention.
Label's offset is 8 bits. because 8 bits are required to express 1-dimention.
'''

'''
input  : filename
output : data (In the form array)
img size is (60000,784)
label size is (60000,1)
'''
#filename = 'train_img' , 'train_label' , 'test_img' , 'test_label'
def readMNIST(filename, datapath):
    data = None
    if filename == 'train_img':
        data = load_mnist(key_file['train_img'], datapath, dat_size = 784 )
    elif filename == 'train_label':
        data = load_mnist(key_file['train_label'], datapath, dat_size = 1, offset =8)
    elif filename == 'test_img':
        data == load_mnist(key_file['test_img'], datapath, dat_size = 784 )
    elif filename == 'test_label':
        data == load_mnist(key_file['test_label'], datapath, dat_size = 1, offset =8)
    else:
        raise NotImplementedError
    return data
