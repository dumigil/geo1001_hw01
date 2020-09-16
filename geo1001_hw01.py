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

def frequency_polygon():
    temp_A = A.Temperature
    temp_B = B.Temperature
    temp_C = C.Temperature
    temp_D = D.Temperature
    temp_E = E.Temperature
    fig = plt.figure(figsize=(16,8))
    plt.hist(temp_A, bins=10, alpha=0.5, label='Sensor A', rwidth=0.85)
    [freq_A, bins]=np.histogram(temp_A, bins = 10) 
    cdf_temp_A = (freq_A)  
    plt.plot(bins[:-1], cdf_temp_A)
    plt.hist(temp_B, bins=10, alpha=0.5, label='Sensor B', rwidth=0.85)
    [freq_B, bins]=np.histogram(temp_B, bins = 10) 
    cdf_temp_B = np.cumsum(freq_B)  
    plt.plot(bins[:-1], cdf_temp_B)
    plt.hist(temp_C, bins=10, alpha=0.5, label='Sensor C', rwidth=0.85)
    [freq_C, bins]=np.histogram(temp_C, bins = 10) 
    cdf_temp_C = np.cumsum(freq_C)  
    plt.plot(bins[:-1], cdf_temp_C)
    plt.hist(temp_D, bins=10, alpha=0.5, label='Sensor D', rwidth=0.85)
    [freq_D, bins]=np.histogram(temp_D, bins = 10) 
    cdf_temp_D = np.cumsum(freq_D)  
    plt.plot(bins[:-1], cdf_temp_D)
    plt.hist(temp_E, bins=10, alpha=0.5, label='Sensor E', rwidth=0.85)
    [freq_E, bins]=np.histogram(temp_E, bins = 10) 
    cdf_temp_E = np.cumsum(freq_E)  
    plt.plot(bins[:-1], cdf_temp_E)
    plt.show()


frequency_polygon()



#plot_temps_hist_5()
#plot_temps_hist_50()