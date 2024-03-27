import warnings
import torch
import torch.nn as nn
import time
import os
import random
from random import SystemRandom
random = SystemRandom()
from torch.utils.data import Dataset
import sys

class MyDataset(Dataset): 
    def __init__(self, ain_size=48, aout_size=16):
        self.a_z = []
        self.digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(26):
            self.a_z += chr(i + ord('a'))

        self.BLANK = chr(2)
        self.alphabet = [self.BLANK] + self.digits + self.a_z + [' ', '+', '-', '*', '/', "="]

        self.ain_size = ain_size
        self.aout_size = aout_size
        self.char2idx = {}
        for i, c in enumerate(self.alphabet):
            self.char2idx[c] = i

    def __len__(self):
        return 1024 * 128
    
    def __getitem__(self, index):
        _ = index

        a1 = random.randint(0, 999)
        a2 = random.randint(0, 999)
       
        ain = f"{str(a1)} * {str(a2)} = "
        aout = f"{a1*a2}"
        
        ain = [self.char2idx[_] for _ in ain]
        aout = [self.char2idx[_] for _ in aout]
        len_aout = len(aout)
        ain = [0]*(self.ain_size - len(ain)) + ain
        aout = aout + [0]*(self.aout_size - len(aout))
        
        return torch.LongTensor(ain), torch.LongTensor(aout), len_aout

if __name__ == '__main__':
    my_dataset = MyDataset()

    ds = MyDataset()

    for i in range(5):
        ain, aout, _ = ds[i]
        print(ain.shape, aout.shape, _)

        for idx in ain:
            c = ds.alphabet[idx]
            if c == ds.BLANK: continue
            print(ds.alphabet[idx], end='')
        print()
        for idx in aout:
            c = ds.alphabet[idx]
            if c == ds.BLANK: continue
            print(ds.alphabet[idx], end='')
        print()
