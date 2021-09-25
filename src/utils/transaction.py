import os
import pandas as pd
from datetime import datetime
import numpy as np
import json


def Net_Worth(filename):
    df = pd.read_csv(filename)

    df = df.astype({"Amount": float}, errors='ignore')

    df['Date'] = pd.to_datetime(df['Date'], format='%y%m%d', errors='ignore')

    #Net Worth Over Time

    a = df['Amount']
    a = list(map(float, a))

    Net_Worth_Table = df.groupby('Date')['Amount'].sum().reset_index(name ='sum')
    Net_Worth_Table['cumulative sum'] = Net_Worth_Table['sum'].cumsum()

    return Net_Worth_Table

def Monthly_Expense(filename):

    df = pd.read_csv(filename)

    df = df.astype({"Amount": float}, errors='ignore')

    df['Date'] = pd.to_datetime(df['Date'], format='%y%m%d', errors='ignore')


    # Total monthly Expense Chart

    Total_Monthly_Expenses_Table = df.groupby('Date')['Amount'].sum().reset_index(name='sum')
    Total_Monthly_Expenses_Table = Total_Monthly_Expenses_Table.rename(columns={'Date': 'Date', 'sum': 'TOTAL EXPENSE'})

    return Total_Monthly_Expenses_Table

def Expense_Breakdown(filename):
    df = pd.read_csv(filename)

    df = df.astype({"Amount": float}, errors='ignore')

    df['Date'] = pd.to_datetime(df['Date'], format='%y%m%d', errors='ignore')

    #Expense Breakdown Chart


    Expenses_Breakdown_Table = df.groupby('Category')['Amount'].sum().reset_index(name ='sum')

    return Expenses_Breakdown_Table
