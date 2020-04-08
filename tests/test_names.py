import pytest 
import main
from main import redactor

file = ['Abdul Kalam, (born October 15, 1931, Rameswaram, India—died July 27, 2015, Shillong), Indian scientist and politician who played a leading role in the development of India’s missile programs']

def san_names(file):
    test,cnt = san_names(file)
    assert cnt == 1


