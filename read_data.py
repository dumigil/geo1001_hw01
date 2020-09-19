import pandas as pd
import numpy as np
import scipy 
import math


def read_data():
    fields = ['FORMATTED_DATE_TIME','Direction_True','Wind_Speed','Crosswind_Speed','Headwind_Speed','Temperature','Globe_Temperature','Wind_Chill','Relative_Humidity','Heat_Stress_Index','Dew_Point','Psychro_Wet_Bulb_Temperature','Station_Pressure','Barometric_Pressure','Altitude','Density_Altitude','NA_Wet_Bulb_Temperature','WBGT','TWL','Direction_Mag']
    A_data = pd.read_csv('HEAT - A_final.csv', skipinitialspace=True,skiprows= [0,1,2,4], usecols=fields,index_col=False)
    B_data = pd.read_csv('HEAT - B_final.csv', skipinitialspace=True,skiprows= [0,1,2,4], usecols=fields,index_col=False)
    C_data = pd.read_csv('HEAT - C_final.csv', skipinitialspace=True,skiprows= [0,1,2,4], usecols=fields,index_col=False)
    D_data = pd.read_csv('HEAT - D_final.csv', skipinitialspace=True,skiprows= [0,1,2,4], usecols=fields,index_col=False)
    E_data = pd.read_csv('HEAT - E_final.csv', skipinitialspace=True,skiprows= [0,1,2,4], usecols=fields,index_col=False)
    #print('Means for sensor A: ' + str(A_data.mean()) + str(A_data.std()) + str(A_data.var()))
    #print(B_data.mean(), B_data.std(), B_data.var())
    #print(C_data.mean(), C_data.std(), C_data.var())
    #print(D_data.mean(), D_data.std(), D_data.var())
    #print(E_data.mean(), E_data.std(), E_data.var())
    #a = np.array([[A_data.mean()],[A_data.std()],[A_data.var()]])
    #print(a)

    Adf = A_data.fillna(0)
    Bdf = B_data.fillna(0)
    Cdf = C_data.fillna(0)
    Ddf = D_data.fillna(0)
    Edf = E_data.fillna(0)
    #print(Adf)



    return Adf,Bdf,Cdf,Ddf,Edf   


#read_data()

