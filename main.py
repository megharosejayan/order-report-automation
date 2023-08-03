import xlrd
import pandas as pd

def get_daily_report():
  fileloc = '/content/Orders_0803.xlsx'
  df = pd.read_excel(fileloc)
  return df

def get_paid_report():
  fileloc= '/content/Orders_0803_paid.xlsx'
  df = pd.read_excel(fileloc)
  return df