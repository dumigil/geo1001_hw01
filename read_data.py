import pandas as pd

def read_data():
    A_data = pd.read_csv('HEAT - A_final.csv', skiprows= [0,1,2,4])
    B_data = pd.read_csv('HEAT - B_final.csv', skiprows= [0,1,2,4])
    C_data = pd.read_csv('HEAT - C_final.csv', skiprows= [0,1,2,4])
    D_data = pd.read_csv('HEAT - D_final.csv', skiprows= [0,1,2,4])
    E_data = pd.read_csv('HEAT - E_final.csv', skiprows= [0,1,2,4])
    print(A_data.head(5))
    print(A_data['TWL'].dtypes)
    WS_A = A_data["Wind Speed"]
    print(WS_A)

read_data()


