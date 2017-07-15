class SizedClass:
    def __len__(self): return 0
from collections import abc
print(isinstance(SizedClass(), abc.Sized)) # True