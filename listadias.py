import pandas as pd


sdatas = pd.Series(pd.date_range('20200101', periods=69))
dia = sdatas.dt.day
mes = sdatas.dt.month
ano = sdatas.dt.year
dfdatas = pd.DataFrame({'ano': ano, 'mes': mes, 'dia': dia, 'data': sdatas})
print(dfdatas)
