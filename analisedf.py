from arquivos import *
import matplotlib.pyplot as plt
# from selenium import webdriver


plt.close('all')
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

dftrans = abrearquivodf('dftrans')
dfcontas = abrearquivodf('dfcontas')
dfcontas = dfcontas.rename(columns={'nome': 'conta'})
dfcontasprevisto = abrearquivodf('dfcontasprevisto')
dfcontasprevisto = dfcontasprevisto.rename(columns={'nome': 'conta'})

contasmes = dftrans.groupby(['ano', 'mes', 'conta']).sum()['valor']
contasmes = contasmes.reset_index()
contasmes = pd.merge(contasmes, dfcontas, how='left', on='conta')
contasmes = contasmes[contasmes['tipo'] == 'D']
contasmes = contasmes.rename(columns={'valor': 'real'})
# contasmes = contasmes.drop(['tipo'], axis=1)

contasprevistomes = dfcontasprevisto.groupby(['ano', 'mes', 'conta']).sum()['valorprevisto']
contasprevistomes = contasprevistomes.reset_index()
contasprevistomes = contasprevistomes.rename(columns={'valorprevisto': 'previsto'})

contasmesfinal = pd.merge(contasmes, contasprevistomes, how='outer', on=['ano', 'mes', 'conta'])
contasmesfinal = contasmesfinal[contasmesfinal['tipo'] == 'D']
contasmesfinal = contasmesfinal.fillna(0)
contasmesfinal['delta'] = (contasmesfinal.real - contasmesfinal.previsto) * -1
contasmesfinal['realinv'] = contasmesfinal.real * -1
contasmesfinal = contasmesfinal.set_index(['ano', 'mes', 'conta'])

resumomes = contasmesfinal.loc[2020, 3].sort_values('conta')
htmlresumo = resumomes.style.to_excel('resumomes.xlsx', engine='openpyxl')
# htmlresumo = resumomes.style.render()
# with open('htmlresumo.html', 'w') as file:
#    file.write(htmlresumo)
# htmlresult = webdriver.Firefox()
# htmlresult.get('file:///C:/Users/carlo/PycharmProjects/fcpandas/htmlresumo.html')

paretomes = contasmesfinal[contasmesfinal['real'] != 0].loc[2020, 3]['realinv'].sort_values()
# plt.figure(figsize=(10, 5))
paretomes.plot.barh(x=paretomes.index, y=paretomes.values)
plt.subplots_adjust(left=0.16)
plt.ylabel('TIPO DE DESPESA')
plt.xlabel('VALOR DA DESPESA')
plt.title('PARETO DE DESDESAS - MARÇO 2020')
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.show()
plt.close()

deltames = contasmesfinal.loc[2020, 3]['delta'].sort_values()
plt.figure(figsize=(11, 5))
deltames.plot.barh(x=deltames.index, y=deltames.values)
plt.subplots_adjust(left=0.20)
plt.ylabel('TIPO DE DESPESA')
plt.xlabel('VALOR DA DIFERENÇA PARA O PREVISTO')
plt.title('DELTA ENTRE DESPESA PREVISTA E REALIZADA - MARÇO 2020')
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.show()
plt.close()

sdatas = pd.Series(pd.date_range('20200301', periods=31))
dia = sdatas.dt.day
mes = sdatas.dt.month
ano = sdatas.dt.year
dfdatas = pd.DataFrame({'ano': ano, 'mes': mes, 'dia': dia, 'data': sdatas})

despesasdia = pd.merge(dftrans, dfcontas, how='left', on='conta')
despesasdia = despesasdia[(despesasdia['tipo'] == 'D') & (despesasdia['meio'] != 'PR')]
despesasdia['valorinv'] = despesasdia.valor * -1
despesasdia = despesasdia.groupby(['ano', 'mes', 'dia']).sum()['valorinv']
despesasdia = despesasdia.reset_index()
despesasdia = pd.merge(despesasdia, dfdatas, how='right', on=['ano', 'mes', 'dia'])
despesasdia = despesasdia.fillna(0)
# plt.figure(figsize=(8, 3))
despesasdia.plot(x='data', y='valorinv')
plt.ylabel('VALOR TOTAL DAS DESPESAS')
plt.xlabel('DIAS')
plt.title('VALOR TOTAL DAS DESPESAS POR DIA - 2020')
plt.legend(('Valor Despesa Diária', 0))
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.show()
plt.close()

# gravaarquivoqdf('dftrans', dftrans)
