import warnings
import torch
import time
import os
# import random
from random import SystemRandom
random = SystemRandom()
from torch.utils.data import Dataset
import sys


class MyDataset(Dataset): 
    def __init__(self, ain_size=48, aout_size=8):
        self.a_z = []
        self.digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(26):
            self.a_z += chr(i + ord('a'))

        self.BLANK = chr(2)
        self.EOS = "^"
        self.alphabet = [self.BLANK] + self.digits + self.a_z + [' ', '+', '-', '*', '/', "=", self.EOS]
        
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
        
        aout = f"{a1*a2}{self.EOS}"
        len_aout = len(aout)
        aout += self.EOS * (self.aout_size - len_aout)
        ain = f"{str(a1)} * {str(a2)} = {aout}"    
        ain = [self.char2idx[_] for _ in ain]
    
        ain = [0]*(self.ain_size + 1 - len(ain)) + ain
        mask = torch.zeros(size=(self.ain_size,), dtype=torch.bool)
        mask[-self.aout_size:-(self.aout_size - len_aout)] = True
        return (torch.LongTensor(ain[:-1]), torch.LongTensor(ain[1:]), 
                mask)




if __name__ == '__main__':
    ds = MyDataset()

    for i in range(5):
        ain, aout, mask = ds[i]
        aout = aout[mask.nonzero()]
        print(ain.shape, aout.shape, mask.shape)
        # print(mask)
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