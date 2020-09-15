#--GEO1001.2020--hw01
#--Michiel de Jong
#--4376978

import pandas as pd
import csv
import xlrd
import matplotlib.pyplot as plt
import numpy as np
from read_data import read_data


A,B,C,D,E = read_data()

def plot_temps_hist_5():
    temp_A = A.Temperature
    temp_B = B.Temperature
    temp_C = C.Temperature
    temp_D = D.Temperature
    temp_E = E.Temperature

    fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1, 5)
    fig.suptitle('Temperature histograms with 5 bins')
    ax1.hist(x=temp_A, bins=5, color='gold', label='Sensor A' )
    ax2.hist(x=temp_B, bins=5, color='greenyellow', label='Sensor B' )
    ax3.hist(x=temp_C, bins=5, color='aqua', label='Sensor C' )
    ax4.hist(x=temp_D, bins=5, color='royalblue', label='Sensor D' )
    ax5.hist(x=temp_E, bins=5, color='hotpink',label='Sensor E' )
    plt.show()

def plot_temps_hist_50():
    temp_A = A.Temperature
    temp_B = B.Temperature
    temp_C = C.Temperature
    temp_D = D.Temperature
    temp_E = E.Temperature

    fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1, 5)
    fig.suptitle('Temperature histograms with 50 bins')
    ax1.hist(x=temp_A, bins=50, color='gold', label='Sensor A' )
    ax2.hist(x=temp_B, bins=50, color='greenyellow', label='Sensor B' )
    ax3.hist(x=temp_C, bins=50, color='aqua', label='Sensor C' )
    ax4.hist(x=temp_D, bins=50, color='royalblue', label='Sensor D' )
    ax5.hist(x=temp_E, bins=50, color='hotpink',label='Sensor E' )
    plt.show()




plot_temps_hist_5()
plot_temps_hist_50()