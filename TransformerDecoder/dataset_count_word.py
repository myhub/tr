import warnings
import torch
import os
# import random
from random import SystemRandom
random = SystemRandom()
from torch.utils.data import Dataset
import sys
from pathlib import Path

class MyDataset(Dataset): 
    def __init__(self, ain_size=128, aout_size=8):

        self.digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.EOS = "^"
        self.BLANK = chr(2)

        self.alphabet = [
            self.BLANK,
            self.EOS, 
            ".",
            ": ",
            "? ",
            "\"",
            "+", "-", "*", "/", "=",
        ] + self.digits

        self.words = Path(__file__).parent.joinpath("vocab.txt").read_text().split("\n")
        assert "letters" in self.words
        self.alphabet += self.words

        self.ain_size = ain_size
        self.aout_size = aout_size
        self.char2idx = {}
        for i, c in enumerate(self.alphabet):
            self.char2idx[c] = i


    def __len__(self):
        return 1024 * 128
    
    def __getitem__(self, index):
        _ = index

        if random.random() < 0.1:
            ss = random.choices(self.words, k=random.randint(1, 9))
        else:
            ss = random.choices(self.words, k=random.randint(1, 99))
            
        num = sum([len(s) for s in ss])

        part1 = ["how", "many", "letters", "are", "there", "in", "the", "following", "string"]
        part2 = [": ", "\""]
        part3 = ["\"", "? "]
        aout = f"{num}{self.EOS}"
    
        len_aout = len(aout)
        aout += self.EOS * (self.aout_size - len_aout)
        ain = part1 + part2 + ss + part3 + list(aout)
    
        ain = [self.char2idx[_] for _ in ain]

        assert len(ain) < self.ain_size

        ain = [0]*(self.ain_size + 1 - len(ain)) + ain

        mask = torch.zeros(size=(self.ain_size,), dtype=torch.bool)
        mask[-self.aout_size:-(self.aout_size - len_aout)] = True
        
        return (torch.LongTensor(ain[:-1]), torch.LongTensor(ain[1:]), 
                mask)



if __name__ == '__main__':
    ds = MyDataset()

    for i in range(5):
        ain, aout, mask = ds[i]
        print(ain.shape, aout.shape, mask.shape)

        pre = "^"
        for idx in ain:
            c = ds.alphabet[idx]
            if c == ds.BLANK: 
                pre = "^"
                continue
            if c[0].isalpha() and pre[-1].isalpha():
                print(" ", end="")
            print(c, end="")
            pre = c
        print()

        aout = aout[mask.nonzero()]
        pre = "^"
        for idx in aout:
            c = ds.alphabet[idx]
            if c == ds.BLANK: 
                pre = "^"
                continue
            if c[0].isalpha() and pre[-1].isalpha():
                print(" ", end="")
            print(c, end="")
            pre = c
        print()
