import pytest
import main
from main import redator
file1 = ['The Burbank-based media giant stated that staffers whose jobs aren’t necessary at this time will be furloughed as of April 19']
def test1(file1):
    test1,cnt1 = red_dates(file1)
    assert cnt1 == 1
