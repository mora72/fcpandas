from arquivos import *
from datetime import date

dfinvest = abrearquivodf('dfinvest')
dfmesano = abrearquivodf('dfmesano')

ano = dfmesano.iloc[0].ano
mes = dfmesano.iloc[0].mes

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
# print(dfinvest.columns)

invest = input('Nome do Investimento: ')
a = dfinvest[(dfinvest['nomeinvest'] == invest) & (dfinvest['mes'] == mes) & (dfinvest['ano'] == ano)]
print(a)
print(f'Valor Total do Investimento {invest} é {a["vlrtotfim"].sum():10,.2f}')
print(f'Quantidade do Investimento {invest} é {a["qtdefim"].sum():10,.0f}')
