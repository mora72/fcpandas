from arquivos import *
import matplotlib.pyplot as plt


pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)
plt.figure(figsize=(19, 9))

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
contasmes = contasmes.drop(['tipo'], axis=1)

contasprevistomes = dfcontasprevisto.groupby(['ano', 'mes', 'conta']).sum()['valorprevisto']
contasprevistomes = contasprevistomes.reset_index()
contasprevistomes = contasprevistomes.rename(columns={'valorprevisto': 'previsto'})

contasmesfinal = pd.merge(contasmes, contasprevistomes, how='outer', on=['ano', 'mes', 'conta'])
contasmesfinal = contasmesfinal.fillna(0)
contasmesfinal['delta'] = (contasmesfinal.real - contasmesfinal.previsto) * -1
contasmesfinal['realinv'] = contasmesfinal.real * -1
contasmesfinal = contasmesfinal.set_index(['ano', 'mes', 'conta'])

paretomes = contasmesfinal[contasmesfinal['real'] != 0].loc[2020, 3]['realinv'].sort_values()
paretomes.plot.barh(x=paretomes.index, y=paretomes.values)
plt.show()

deltames = contasmesfinal.loc[2020, 3]['delta'].sort_values()
deltames.plot.barh()
plt.show()

despesasdia = pd.merge(dftrans, dfcontas, how='left', on='conta')
despesasdia = despesasdia[(despesasdia['tipo'] == 'D') & (despesasdia['meio'] != 'PR')]
# despesasdia['mesdia'] = despesasdia.assign(mesdia=lambda despesasdia: (str(despesasdia.mes)))
despesasdia['valorinv'] = despesasdia.valor * -1
despesasdia = despesasdia.groupby(['mes', 'dia']).sum()['valorinv']
despesasdia.plot()
plt.show()

# linha abaixo = relatório que já tenho pronto no fc
resumomes = contasmesfinal.loc[2020, 3].sort_values('conta')
print(resumomes)
# print(resumomes.table())

# gravaarquivoqdf('dftrans', dftrans)
