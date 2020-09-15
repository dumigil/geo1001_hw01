import pandas as pd
import numpy as np
import scipy 
import math


def read_data():
    fields = ['Direction_True','Wind_Speed','Crosswind_Speed','Headwind_Speed','Temperature','Globe_Temperature','Wind_Chill','Relative_Humidity','Heat_Stress_Index','Dew_Point','Psychro_Wet_Bulb_Temperature','Station_Pressure','Barometric_Pressure','Altitude','Density_Altitude','NA_Wet_Bulb_Temperature','WBGT','TWL','Direction_Mag']
    A_data = pd.read_csv('HEAT - A_final.csv', skipinitialspace=True,skiprows= [0,1,2,4], usecols=fields)
    B_data = pd.read_csv('HEAT - B_final.csv', skipinitialspace=True,skiprows= [0,1,2,4], usecols=fields)
    C_data = pd.read_csv('HEAT - C_final.csv', skipinitialspace=True,skiprows= [0,1,2,4], usecols=fields)
    D_data = pd.read_csv('HEAT - D_final.csv', skipinitialspace=True,skiprows= [0,1,2,4], usecols=fields)
    E_data = pd.read_csv('HEAT - E_final.csv', skipinitialspace=True,skiprows= [0,1,2,4], usecols=fields)
    #print('Means for sensor A: ' + str(A_data.mean()) + str(A_data.std()) + str(A_data.var()))
    #print(B_data.mean(), B_data.std(), B_data.var())
    #print(C_data.mean(), C_data.std(), C_data.var())
    #print(D_data.mean(), D_data.std(), D_data.var())
    #print(E_data.mean(), E_data.std(), E_data.var())
    #a = np.array([[A_data.mean()],[A_data.std()],[A_data.var()]])
    #print(a)

    Adf = np.array([A_data])
    Bdf = np.array([B_data])
    Cdf = np.array([C_data])
    Ddf = np.array([D_data])
    Edf = np.array([E_data])




    return A_data,B_data,C_data,D_data,E_data   


#read_data()

