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
    fig.suptitle('Frequency Polygons for 5 sensors')
    #Frequency polygon Sensor A
    [freq_A, bins]=np.histogram(temp_A, bins = 10) 
    cdf_temp_A = np.cumsum(freq_A)  
    plt.plot(bins[:-1], cdf_temp_A)
    #Frequency polygon Sensor B
    [freq_B, bins]=np.histogram(temp_B, bins = 10) 
    cdf_temp_B = np.cumsum(freq_B)  
    plt.plot(bins[:-1], cdf_temp_B)
    #Frequency polygon Sensor C
    [freq_C, bins]=np.histogram(temp_C, bins = 10) 
    cdf_temp_C = np.cumsum(freq_C)  
    plt.plot(bins[:-1], cdf_temp_C)
    #Frequency polygon Sensor D
    [freq_D, bins]=np.histogram(temp_D, bins = 10) 
    cdf_temp_D = np.cumsum(freq_D)  
    plt.plot(bins[:-1], cdf_temp_D)
    #Frequency polygon Sensor E
    [freq_E, bins]=np.histogram(temp_E, bins = 10) 
    cdf_temp_E = np.cumsum(freq_E)  
    plt.plot(bins[:-1], cdf_temp_E)
    plt.show()

def boxplot_windspeed():
    WS_A = A.Wind_Speed
    WS_B = B.Wind_Speed
    WS_C = C.Wind_Speed
    WS_D = D.Wind_Speed
    WS_E = E.Wind_Speed

    fig = plt.figure(figsize=(28,8))
    ax1 = fig.add_subplot(151)
    ax2 = fig.add_subplot(152)
    ax3 = fig.add_subplot(153)
    ax4 = fig.add_subplot(154)
    ax5 = fig.add_subplot(155)
    ax1.boxplot(WS_A, showmeans=True)
    ax1.set_ylabel('Wind Speed [m/s]', fontsize=14)
    ax1.tick_params(labelsize=14)
    ax2.boxplot(WS_B, showmeans=True)
    ax2.set_ylabel('Wind Speed [m/s]', fontsize=14)
    ax2.tick_params(labelsize=14)
    ax3.boxplot(WS_C, showmeans=True)
    ax3.set_ylabel('Wind Speed [m/s]', fontsize=14)
    ax3.tick_params(labelsize=14)
    ax4.boxplot(WS_D, showmeans=True)
    ax4.set_ylabel('Wind Speed [m/s]', fontsize=14)
    ax4.tick_params(labelsize=14)
    ax5.boxplot(WS_E, showmeans=True)
    ax5.set_ylabel('Wind Speed [m/s]', fontsize=14)
    ax5.tick_params(labelsize=14)
    plt.show()

def boxplot_winddirection():
    WD_A = A.Direction_True
    WD_B = B.Direction_True
    WD_C = C.Direction_True
    WD_D = D.Direction_True
    WD_E = E.Direction_True

    fig = plt.figure(figsize=(28,8))
    ax1 = fig.add_subplot(151)
    ax2 = fig.add_subplot(152)
    ax3 = fig.add_subplot(153)
    ax4 = fig.add_subplot(154)
    ax5 = fig.add_subplot(155)
    ax1.boxplot(WD_A, showmeans=True)
    ax1.set_ylabel('Wind Direction [°]', fontsize=14)
    ax1.tick_params(labelsize=14)
    ax2.boxplot(WD_B, showmeans=True)
    ax2.set_ylabel('Wind Direction [°]', fontsize=14)
    ax2.tick_params(labelsize=14)
    ax3.boxplot(WD_C, showmeans=True)
    ax3.set_ylabel('Wind Direction [°]', fontsize=14)
    ax3.tick_params(labelsize=14)
    ax4.boxplot(WD_D, showmeans=True)
    ax4.set_ylabel('Wind Direction [°]', fontsize=14)
    ax4.tick_params(labelsize=14)
    ax5.boxplot(WD_E, showmeans=True)
    ax5.set_ylabel('Wind Direction [°]', fontsize=14)
    ax5.tick_params(labelsize=14)
    plt.show()

def boxplot_temperature():
    temp_A = A.Temperature
    temp_B = B.Temperature
    temp_C = C.Temperature
    temp_D = D.Temperature
    temp_E = E.Temperature

    fig = plt.figure(figsize=(28,8))
    ax1 = fig.add_subplot(151)
    ax2 = fig.add_subplot(152)
    ax3 = fig.add_subplot(153)
    ax4 = fig.add_subplot(154)
    ax5 = fig.add_subplot(155)
    ax1.boxplot(temp_A, showmeans=True)
    ax1.set_ylabel('Temperature [°C]', fontsize=14)
    ax1.tick_params(labelsize=14)
    ax2.boxplot(temp_B, showmeans=True)
    ax2.set_ylabel('Temperature [°C]', fontsize=14)
    ax2.tick_params(labelsize=14)
    ax3.boxplot(temp_C, showmeans=True)
    ax3.set_ylabel('Temperature [°C]', fontsize=14)
    ax3.tick_params(labelsize=14)
    ax4.boxplot(temp_D, showmeans=True)
    ax4.set_ylabel('Temperature [°C]', fontsize=14)
    ax4.tick_params(labelsize=14)
    ax5.boxplot(temp_E, showmeans=True)
    ax5.set_ylabel('Temperature [°C]', fontsize=14)
    ax5.tick_params(labelsize=14)
    plt.show()

boxplot_windspeed()
boxplot_winddirection()
boxplot_temperature()



#frequency_polygon()
#plot_temps_hist_5()
#plot_temps_hist_50()