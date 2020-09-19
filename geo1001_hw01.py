#--GEO1001.2020--hw01
#--Michiel de Jong
#--4376978

import pandas as pd
import csv
import xlrd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from read_data import read_data
import seaborn as sns 
import math


A,B,C,D,E = read_data()



#######################################
#LESSON A1
#######################################
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
    #plt.show()
    plt.savefig(('plot_temps_hist_5'))

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
    #plt.show()
    plt.savefig(('plot_temps_hist_50'))

def frequency_polygon():
    temp_A = A.Temperature
    temp_B = B.Temperature
    temp_C = C.Temperature
    temp_D = D.Temperature
    temp_E = E.Temperature
    fig = plt.figure(figsize=(17,6))
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
    #plt.show()
    plt.savefig(('frequency_polygon'))

def boxplot_windspeed():
    WS_A = A.Wind_Speed
    WS_B = B.Wind_Speed
    WS_C = C.Wind_Speed
    WS_D = D.Wind_Speed
    WS_E = E.Wind_Speed

    fig = plt.figure(figsize=(17,6))
    ax1 = fig.add_subplot(151)
    ax2 = fig.add_subplot(152)
    ax3 = fig.add_subplot(153)
    ax4 = fig.add_subplot(154)
    ax5 = fig.add_subplot(155)
    ax1.boxplot(WS_A, showmeans=True)
    ax1.set_ylabel('Wind Speed [m/s]', fontsize=14)
    ax1.tick_params(labelsize=14)
    ax1.set_xlabel('Sensor A', fontsize=14)
    ax2.boxplot(WS_B, showmeans=True)
    ax2.set_ylabel('Wind Speed [m/s]', fontsize=14)
    ax2.tick_params(labelsize=14)
    ax2.set_xlabel('Sensor B', fontsize=14)
    ax3.boxplot(WS_C, showmeans=True)
    ax3.set_ylabel('Wind Speed [m/s]', fontsize=14)
    ax3.tick_params(labelsize=14)
    ax3.set_xlabel('Sensor C', fontsize=14)
    ax4.boxplot(WS_D, showmeans=True)
    ax4.set_ylabel('Wind Speed [m/s]', fontsize=14)
    ax4.tick_params(labelsize=14)
    ax4.set_xlabel('Sensor D', fontsize=14)
    ax5.boxplot(WS_E, showmeans=True)
    ax5.set_ylabel('Wind Speed [m/s]', fontsize=14)
    ax5.tick_params(labelsize=14)
    ax5.set_xlabel('Sensor E', fontsize=14)
    #plt.show()
    plt.savefig(('boxplot_windspeed'))

def boxplot_winddirection():
    WD_A = A.Direction_True
    WD_B = B.Direction_True
    WD_C = C.Direction_True
    WD_D = D.Direction_True
    WD_E = E.Direction_True

    fig = plt.figure(figsize=(17,6))
    ax1 = fig.add_subplot(151)
    ax2 = fig.add_subplot(152)
    ax3 = fig.add_subplot(153)
    ax4 = fig.add_subplot(154)
    ax5 = fig.add_subplot(155)
    ax1.boxplot(WD_A, showmeans=True)
    ax1.set_ylabel('Wind Direction [°]', fontsize=14)
    ax1.tick_params(labelsize=14)
    ax1.set_xlabel('Sensor A', fontsize=14)
    ax2.boxplot(WD_B, showmeans=True)
    ax2.set_ylabel('Wind Direction [°]', fontsize=14)
    ax2.tick_params(labelsize=14)
    ax2.set_xlabel('Sensor B', fontsize=14)
    ax3.boxplot(WD_C, showmeans=True)
    ax3.set_ylabel('Wind Direction [°]', fontsize=14)
    ax3.tick_params(labelsize=14)
    ax3.set_xlabel('Sensor C', fontsize=14)
    ax4.boxplot(WD_D, showmeans=True)
    ax4.set_ylabel('Wind Direction [°]', fontsize=14)
    ax4.tick_params(labelsize=14)
    ax4.set_xlabel('Sensor D', fontsize=14)
    ax5.boxplot(WD_E, showmeans=True)
    ax5.set_ylabel('Wind Direction [°]', fontsize=14)
    ax5.tick_params(labelsize=14)
    ax5.set_xlabel('Sensor E', fontsize=14)
    #plt.show()
    plt.savefig(('boxplot_winddirection'))

def boxplot_temperature():
    temp_A = A.Temperature
    temp_B = B.Temperature
    temp_C = C.Temperature
    temp_D = D.Temperature
    temp_E = E.Temperature

    fig = plt.figure(figsize=(17,6))
    ax1 = fig.add_subplot(151)
    ax2 = fig.add_subplot(152)
    ax3 = fig.add_subplot(153)
    ax4 = fig.add_subplot(154)
    ax5 = fig.add_subplot(155)
    ax1.boxplot(temp_A, showmeans=True)
    ax1.set_ylabel('Temperature [°C]', fontsize=14)
    ax1.tick_params(labelsize=14)
    ax1.set_xlabel('Sensor A', fontsize=14)
    ax2.boxplot(temp_B, showmeans=True)
    ax2.set_ylabel('Temperature [°C]', fontsize=14)
    ax2.tick_params(labelsize=14)
    ax2.set_xlabel('Sensor B', fontsize=14)
    ax3.boxplot(temp_C, showmeans=True)
    ax3.set_ylabel('Temperature [°C]', fontsize=14)
    ax3.tick_params(labelsize=14)
    ax3.set_xlabel('Sensor C', fontsize=14)
    ax4.boxplot(temp_D, showmeans=True)
    ax4.set_ylabel('Temperature [°C]', fontsize=14)
    ax4.tick_params(labelsize=14)
    ax4.set_xlabel('Sensor D', fontsize=14)
    ax5.boxplot(temp_E, showmeans=True)
    ax5.set_ylabel('Temperature [°C]', fontsize=14)
    ax5.tick_params(labelsize=14)
    ax5.set_xlabel('Sensor E', fontsize=14)
    #plt.show()
    plt.savefig(('boxplot_temperature'))

boxplot_windspeed()
boxplot_winddirection()
boxplot_temperature()
frequency_polygon()
plot_temps_hist_5()
plot_temps_hist_50()

#######################################
#LESSON A2
#######################################

def plot_PMF_T():
    temp_A = A.Temperature
    temp_B = B.Temperature
    temp_C = C.Temperature
    temp_D = D.Temperature
    temp_E = E.Temperature    

    def pmf(sample):
        c = sample.value_counts()
        p = c/len(sample)
        return p
    
    dfA = pmf(temp_A)
    cA = dfA.sort_index()
    dfB = pmf(temp_B)
    cB = dfB.sort_index()
    dfC = pmf(temp_C)
    cC = dfC.sort_index()
    dfD = pmf(temp_D)
    cD = dfD.sort_index()
    dfE = pmf(temp_E)
    cE = dfE.sort_index()

    fig = plt.figure(figsize=(17,6))
    ax1 = fig.add_subplot(151)
    ax2 = fig.add_subplot(152)
    ax3 = fig.add_subplot(153)
    ax4 = fig.add_subplot(154)
    ax5 = fig.add_subplot(155)
    ax1.bar(dfA.index,dfA.values)
    ax1.tick_params(labelsize=8)
    ax1.title.set_text('PMF of Sensor A')
    ax2.bar(dfB.index,dfB.values)
    ax2.tick_params(labelsize=8)
    ax2.title.set_text('PMF of Sensor B')
    ax3.bar(dfC.index,dfC.values)
    ax3.tick_params(labelsize=8)
    ax3.title.set_text('PMF of Sensor C')
    ax4.bar(dfD.index,dfD.values)
    ax4.tick_params(labelsize=8)
    ax4.title.set_text('PMF of Sensor D')
    ax5.bar(dfE.index,dfE.values)
    ax5.tick_params(labelsize=8)
    ax5.title.set_text('PMF of Sensor E')
    plt.tight_layout()
    #plt.show()
    plt.savefig(('plot_PMF_T'))

def plot_PDF_T():
    temp_A = A.Temperature
    temp_B = B.Temperature
    temp_C = C.Temperature
    temp_D = D.Temperature
    temp_E = E.Temperature 

    fig = plt.figure(figsize=(17,6))
    ax1 = fig.add_subplot(151)
    ax1.title.set_text('PDF of Sensor A')
    a1=ax1.hist(x=temp_A.astype(float),bins=50, density=True, color='g',alpha=0.7, rwidth=0.85)
    sns.distplot(temp_A.astype(float), color='royalblue',ax=ax1)
    ax2 = fig.add_subplot(152)
    ax2.title.set_text('PDF of Sensor B')
    a2=ax2.hist(x=temp_B.astype(float),bins=50, density=True, color='g',alpha=0.7, rwidth=0.85)
    sns.distplot(temp_B.astype(float), color='royalblue',ax=ax2)
    ax3 = fig.add_subplot(153)
    ax3.title.set_text('PDF of Sensor C')
    a3=ax3.hist(x=temp_C.astype(float),bins=50, density=True, color='g',alpha=0.7, rwidth=0.85)
    sns.distplot(temp_C.astype(float), color='royalblue',ax=ax3)
    ax4 = fig.add_subplot(154)
    ax4.title.set_text('PDF of Sensor D')
    a4=ax4.hist(x=temp_D.astype(float),bins=50, density=True, color='g',alpha=0.7, rwidth=0.85)
    sns.distplot(temp_D.astype(float), color='royalblue',ax=ax4)
    ax5 = fig.add_subplot(155)
    ax5.title.set_text('PDF of Sensor E')
    a5=ax5.hist(x=temp_E.astype(float),bins=50, density=True, color='g',alpha=0.7, rwidth=0.85)
    sns.distplot(temp_E.astype(float), color='royalblue',ax=ax5)
    plt.tight_layout()
    #plt.show()
    plt.savefig(('plot_PDF_T'))

def plot_CDF_T():
    temp_A = A.Temperature
    temp_B = B.Temperature
    temp_C = C.Temperature
    temp_D = D.Temperature
    temp_E = E.Temperature  
    bins = int((len(temp_A)) ** (1./3))*2
    fig = plt.figure(figsize=(17,6))
    ax1 = fig.add_subplot(151)
    ax1.title.set_text('CDF of Sensor A')
    a1=ax1.hist(x=temp_A.astype(float),bins=bins,density=True, cumulative=True, color='royalblue',alpha=0.7, rwidth=0.85)
    ax1.plot(a1[1][1:]-(a1[1][1:]-a1[1][:-1])/2,a1[0], color='k')
    ax1.set_xlabel('Temperature [C°]')
    ax2 = fig.add_subplot(152)
    ax2.title.set_text('CDF of Sensor B')
    a2=ax2.hist(x=temp_B.astype(float),bins=bins,density=True, cumulative=True, color='royalblue',alpha=0.7, rwidth=0.85)
    ax2.plot(a2[1][1:]-(a2[1][1:]-a2[1][:-1])/2,a2[0], color='k')
    ax2.set_xlabel('Temperature [C°]')
    ax3 = fig.add_subplot(153)
    ax3.title.set_text('CDF of Sensor C')
    a3=ax3.hist(x=temp_C.astype(float),bins=bins,density=True, cumulative=True, color='royalblue',alpha=0.7, rwidth=0.85)
    ax3.plot(a3[1][1:]-(a3[1][1:]-a3[1][:-1])/2,a3[0], color='k')
    ax3.set_xlabel('Temperature [C°]')
    ax4 = fig.add_subplot(154)
    ax4.title.set_text('CDF of Sensor D')
    a4=ax4.hist(x=temp_D.astype(float),bins=bins,density=True, cumulative=True, color='royalblue',alpha=0.7, rwidth=0.85)
    ax4.plot(a4[1][1:]-(a4[1][1:]-a4[1][:-1])/2,a4[0], color='k')
    ax4.set_xlabel('Temperature [C°]')
    ax5 = fig.add_subplot(155)
    ax5.title.set_text('CDF of Sensor E')
    a5=ax5.hist(x=temp_E.astype(float),bins=bins,density=True, cumulative=True, color='royalblue',alpha=0.7, rwidth=0.85)
    ax5.plot(a5[1][1:]-(a5[1][1:]-a5[1][:-1])/2,a5[0], color='k')
    ax5.set_xlabel('Temperature [C°]')
    plt.tight_layout()
    #plt.show()
    plt.savefig(('plot_CDF_T'))

def plot_CDF_WS():
    WS_A = A.Wind_Speed
    WS_B = B.Wind_Speed
    WS_C = C.Wind_Speed
    WS_D = D.Wind_Speed
    WS_E = E.Wind_Speed  
    bins = int((len(WS_A)) ** (1./3))*2
    fig = plt.figure(figsize=(17,6))
    ax1 = fig.add_subplot(151)
    ax1.title.set_text('CDF of Sensor A')
    a1=ax1.hist(x=WS_A.astype(float),bins=bins,density=True, cumulative=True, color='royalblue',alpha=0.7, rwidth=0.85)
    ax1.plot(a1[1][1:]-(a1[1][1:]-a1[1][:-1])/2,a1[0], color='k')
    ax1.set_xlabel('Wind Speed [m/s]')
    ax2 = fig.add_subplot(152)
    ax2.title.set_text('CDF of Sensor B')
    a2=ax2.hist(x=WS_B.astype(float),bins=bins,density=True, cumulative=True, color='royalblue',alpha=0.7, rwidth=0.85)
    ax2.plot(a2[1][1:]-(a2[1][1:]-a2[1][:-1])/2,a2[0], color='k')
    ax2.set_xlabel('Wind Speed [m/s]')
    ax3 = fig.add_subplot(153)
    ax3.title.set_text('CDF of Sensor C')
    a3=ax3.hist(x=WS_C.astype(float),bins=bins,density=True, cumulative=True, color='royalblue',alpha=0.7, rwidth=0.85)
    ax3.plot(a3[1][1:]-(a3[1][1:]-a3[1][:-1])/2,a3[0], color='k')
    ax3.set_xlabel('Wind Speed [m/s]')
    ax4 = fig.add_subplot(154)
    ax4.title.set_text('CDF of Sensor D')
    a4=ax4.hist(x=WS_D.astype(float),bins=bins,density=True, cumulative=True, color='royalblue',alpha=0.7, rwidth=0.85)
    ax4.plot(a4[1][1:]-(a4[1][1:]-a4[1][:-1])/2,a4[0], color='k')
    ax4.set_xlabel('Wind Speed [m/s]')
    ax5 = fig.add_subplot(155)
    ax5.title.set_text('CDF of Sensor E')
    a5=ax5.hist(x=WS_E.astype(float),bins=bins,density=True, cumulative=True, color='royalblue',alpha=0.7, rwidth=0.85)
    ax5.plot(a5[1][1:]-(a5[1][1:]-a5[1][:-1])/2,a5[0], color='k')
    ax5.set_xlabel('Wind Speed [m/s]')
    plt.tight_layout()
    #plt.show()
    plt.savefig(('plot_CDF_WS'))

def plot_PDF_WS():
    WS_A = A.Wind_Speed
    WS_B = B.Wind_Speed
    WS_C = C.Wind_Speed
    WS_D = D.Wind_Speed
    WS_E = E.Wind_Speed 

    fig = plt.figure(figsize=(17,6))
    ax1 = fig.add_subplot(151)
    ax1.title.set_text('PDF of Sensor A')
    a1=ax1.hist(x=WS_A.astype(float),bins=50, density=True, color='g',alpha=0.7, rwidth=0.85)
    sns.distplot(WS_A.astype(float), color='royalblue',ax=ax1)
    ax2 = fig.add_subplot(152)
    ax2.title.set_text('PDF of Sensor B')
    a2=ax2.hist(x=WS_B.astype(float),bins=50, density=True, color='g',alpha=0.7, rwidth=0.85)
    sns.distplot(WS_B.astype(float), color='royalblue',ax=ax2)
    ax3 = fig.add_subplot(153)
    ax3.title.set_text('PDF of Sensor C')
    a3=ax3.hist(x=WS_C.astype(float),bins=50, density=True, color='g',alpha=0.7, rwidth=0.85)
    sns.distplot(WS_C.astype(float), color='royalblue',ax=ax3)
    ax4 = fig.add_subplot(154)
    ax4.title.set_text('PDF of Sensor D')
    a4=ax4.hist(x=WS_D.astype(float),bins=50, density=True, color='g',alpha=0.7, rwidth=0.85)
    sns.distplot(WS_D.astype(float), color='royalblue',ax=ax4)
    ax5 = fig.add_subplot(155)
    ax5.title.set_text('PDF of Sensor E')
    a5=ax5.hist(x=WS_E.astype(float),bins=50, density=True, color='g',alpha=0.7, rwidth=0.85)
    sns.distplot(WS_E.astype(float), color='royalblue',ax=ax5)
    plt.tight_layout()
    #plt.show()
    plt.savefig(('plot_PDF_WS'))

def plot_KDE_WS():
    WS_A = A.Wind_Speed
    WS_B = B.Wind_Speed
    WS_C = C.Wind_Speed
    WS_D = D.Wind_Speed
    WS_E = E.Wind_Speed 
    fig = plt.figure(figsize=(17,6))
    ax1 = fig.add_subplot(151) 
    ax1 = WS_A.plot.kde()
    ax1.title.set_text('KDE of Sensor A')
    ax1.set_xlabel('Wind Speed [m/s]')
    ax2 = fig.add_subplot(152) 
    ax2 = WS_B.plot.kde()
    ax2.title.set_text('KDE of Sensor B')
    ax2.set_xlabel('Wind Speed [m/s]')
    ax3 = fig.add_subplot(153) 
    ax3 = WS_C.plot.kde()
    ax3.title.set_text('KDE of Sensor C')
    ax3.set_xlabel('Wind Speed [m/s]')
    ax4 = fig.add_subplot(154) 
    ax4 = WS_D.plot.kde()
    ax4.title.set_text('KDE of Sensor D')
    ax4.set_xlabel('Wind Speed [m/s]')
    ax5 = fig.add_subplot(155) 
    ax5 = WS_E.plot.kde()
    ax5.title.set_text('KDE of Sensor E')
    ax5.set_xlabel('Wind Speed [m/s]')
    plt.tight_layout()
    #plt.show()
    plt.savefig(('plot_KDE_WS'))



plot_PMF_T()
plot_PDF_T()
plot_CDF_T()
plot_PDF_WS()
plot_KDE_WS()

#######################################
#LESSON A3
#######################################

def correlations_T():
    keys = ['A','B','C','D','E']
    Temperature = pd.concat([A.Temperature,B.Temperature,C.Temperature,D.Temperature,E.Temperature],axis=1,keys=keys).dropna()
    pearson_list = []
    spearman_list = []
    
    while len(keys) > 1:
        sensor1 = keys[0]
        for sensor2 in keys:
            if sensor1 != sensor2:
                pearson = stats.pearsonr(Temperature[sensor1],Temperature[sensor2])
                key = str(sensor1) + ' x ' + str(sensor2)
                pearson_list.append(pearson)
                #pearson_list.append(key)
                spearman = stats.spearmanr(Temperature[sensor1],Temperature[sensor2])
                key = str(sensor1) + ' x ' + str(sensor2)
                spearman_list.append(pearson)

        keys.remove(sensor1)
        
    return pearson_list, spearman_list

def correlations_WBGT():
    keys = ['A','B','C','D','E']
    WBGT = pd.concat([A.WBGT,B.WBGT,C.WBGT,D.WBGT,E.WBGT],axis=1,keys=keys).dropna()
    pearson_list = []
    spearman_list = []
    
    while len(keys) > 1:
        sensor1 = keys[0]
        for sensor2 in keys:
            if sensor1 != sensor2:
                pearson = stats.pearsonr(WBGT[sensor1],WBGT[sensor2])
                key = str(sensor1) + ' x ' + str(sensor2)
                pearson_list.append(pearson)
                #pearson_list.append(key)
                spearman = stats.spearmanr(WBGT[sensor1],WBGT[sensor2])
                key = str(sensor1) + ' x ' + str(sensor2)
                spearman_list.append(pearson)

        keys.remove(sensor1)
    return pearson_list, spearman_list

def correlations_CWS():
    keys = ['A','B','C','D','E']
    Crosswind_Speed = pd.concat([A.Crosswind_Speed,B.Crosswind_Speed,C.Crosswind_Speed,D.Crosswind_Speed,E.Crosswind_Speed],axis=1,keys=keys).dropna()
    pearson_list = []
    spearman_list = []
    key_list = []
    
    while len(keys) > 1:
        sensor1 = keys[0]
        for sensor2 in keys:
            if sensor1 != sensor2:
                pearson = stats.pearsonr(Crosswind_Speed[sensor1],Crosswind_Speed[sensor2])
                key = str(sensor1) + ' - ' + str(sensor2)
                pearson_list.append(pearson)
                #pearson_list.append(key)
                spearman = stats.spearmanr(Crosswind_Speed[sensor1],Crosswind_Speed[sensor2])
                key = str(sensor1) + ' - ' + str(sensor2)
                spearman_list.append(pearson)
                key_list.append(key)

        keys.remove(sensor1)
    return pearson_list, spearman_list, key_list

                
def plot_correlations():
    temp_pearson, temp_spearman = correlations_T()
    temp_pearson = np.array(temp_pearson)
    temp_pearson = np.delete(temp_pearson,1,1)
    temp_spearman = np.array(temp_spearman)
    temp_spearman = np.delete(temp_spearman,1,1)
    wbgt_pearson, wbgt_spearman = correlations_WBGT()
    wbgt_pearson = np.array(wbgt_pearson)
    wbgt_pearson = np.delete(wbgt_pearson,1,1)
    wbgt_spearman = np.array(wbgt_spearman)
    wbgt_spearman = np.delete(wbgt_spearman,1,1)
    cws_pearson, cws_spearman, key_list = correlations_CWS()
    cws_pearson = np.array(cws_pearson)
    cws_pearson = np.delete(cws_pearson,1,1)
    cws_spearman = np.array(cws_spearman)
    cws_spearman = np.delete(cws_spearman,1,1)
    

    fig = plt.figure(figsize=(17,6))
    ax1 = fig.add_subplot(121)
    ax1.scatter(key_list,temp_pearson, c='paleturquoise',label='Temperature')
    ax1.scatter(key_list,wbgt_pearson, c='tomato',label='Wet Bulb Globe')
    ax1.scatter(key_list,cws_pearson, c='teal',label='Crosswind Speed')
    ax1.title.set_text('Pearson Correlation')
    ax1.set_ylabel('Correlation Coefficient',fontsize=14)
    plt.legend(loc='center right')
    ax2 = fig.add_subplot(122)
    ax2.scatter(key_list,temp_spearman, c='paleturquoise',label='Temperature')
    ax2.scatter(key_list,wbgt_spearman, c='tomato',label='Wet Bulb Globe')
    ax2.scatter(key_list,cws_spearman, c='teal',label='Crosswind Speed')
    ax2.title.set_text('Spearman Correlation')
    ax2.set_ylabel('Correlation Coefficient',fontsize=14)
    plt.legend(loc='center right')

    plt.tight_layout()
    #plt.show()
    plt.savefig(('plot_correlations'))
    


#######################################
#LESSON A4
#######################################

def confidence_interval_T():
    plot_CDF_T()
    keys = ['A','B','C','D','E']
    lower_values = []
    upper_values = []
    Temperature = pd.concat([A.Temperature,B.Temperature,C.Temperature,D.Temperature,E.Temperature],axis=1,keys=keys).dropna()
    sample_length = len(Temperature)
    sample_mean = Temperature.mean()
    sample_std = Temperature.std()
    lower, upper = stats.t.interval(0.95, sample_length-1,loc=sample_mean, scale=sample_std)
    lower_values.append(lower)
    upper_values.append(upper)
    confidence_table = pd.DataFrame({'Lower': lower,'Upper': upper}, index=keys).to_csv("confidence_interval_temperature.csv")
    print(((confidence_table)))

def confidence_interval_WS():
    plot_CDF_WS()
    keys = ['A','B','C','D','E']
    lower_values = []
    upper_values = []
    Temperature = pd.concat([A.Wind_Speed,B.Wind_Speed,C.Wind_Speed,D.Wind_Speed,E.Wind_Speed],axis=1,keys=keys).dropna()
    sample_length = len(Temperature)
    sample_mean = Temperature.mean()
    sample_std = Temperature.std()
    lower, upper = stats.t.interval(0.95, sample_length-1,loc=sample_mean, scale=sample_std)
    lower_values.append(lower)
    upper_values.append(upper)
    confidence_table = pd.DataFrame({'Lower': lower,'Upper': upper}, index=keys).to_csv("confidence_interval_winspeed.csv")
    print(((confidence_table)))

def t_test_ED():
    temp_D = D.Temperature
    temp_E = E.Temperature
    WS_D = D.Wind_Speed
    WS_E = E.Wind_Speed
    print("Comparing samples from sensors E and D")
    t_temp, p_temp = stats.ttest_ind(temp_D,temp_E)
    print("Temperature t-value: " + str(t_temp))
    print("Temperature p-value: " + str(p_temp))
    t_ws, p_ws = stats.ttest_ind(WS_D,WS_E)
    print("Wind Speed t-value: " + str(t_ws))
    print("Wind Speed p-value: " + str(p_ws))

def t_test_DC():
    temp_D = D.Temperature
    temp_C = C.Temperature
    WS_D = D.Wind_Speed
    WS_C = C.Wind_Speed
    print("Comparing samples from sensors D and C")
    t_temp, p_temp = stats.ttest_ind(temp_D,temp_C)
    print("Temperature t-value: " + str(t_temp))
    print("Temperature p-value: " + str(p_temp))
    t_ws, p_ws = stats.ttest_ind(WS_D,WS_C)
    print("Wind Speed t-value: " + str(t_ws))
    print("Wind Speed p-value: " + str(p_ws))

def t_test_CB():
    temp_C = C.Temperature
    temp_B = B.Temperature
    WS_C = C.Wind_Speed
    WS_B = B.Wind_Speed
    print("Comparing samples from sensors C and B")
    t_temp, p_temp = stats.ttest_ind(temp_C,temp_B)
    print("Temperature t-value: " + str(t_temp))
    print("Temperature p-value: " + str(p_temp))
    t_ws, p_ws = stats.ttest_ind(WS_C,WS_B)
    print("Wind Speed t-value: " + str(t_ws))
    print("Wind Speed p-value: " + str(p_ws))

def t_test_BA():
    temp_B = B.Temperature
    temp_A = A.Temperature
    WS_B = B.Wind_Speed
    WS_A = A.Wind_Speed
    print("Comparing samples from sensors B and A")
    t_temp, p_temp = stats.ttest_ind(temp_B,temp_A)
    print("Temperature t-value: " + str(t_temp))
    print("Temperature p-value: " + str(p_temp))
    t_ws, p_ws = stats.ttest_ind(WS_B,WS_A)
    print("Wind Speed t-value: " + str(t_ws))
    print("Wind Speed p-value: " + str(p_ws))



confidence_interval_T()
confidence_interval_WS()
t_test_ED()
t_test_DC()
t_test_CB()
t_test_BA()