#--GEO1001.2020--hw01
#--Michiel de Jong
#--4376978

import pandas as pd
import csv
import xlrd
from read_data import read_data


A,B,C,D,E = read_data()
print(A.mean())
print(B.mean())
print(C.mean())
print(D.mean())
print(E.mean())
