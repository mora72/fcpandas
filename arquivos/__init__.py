# Funções de Abertura e Gravação de Arquivos
import pickle
import pandas as pd


def abrearquivo(nomelista):
    listaarqs = {'listameiossaldo': '/Users/carlo/PycharmProjects/fc/basemeiossaldo.pck1',
                 'listameios': '/Users/carlo/PycharmProjects/fc/basemeios.pck1',
                 'listacontas': '/Users/carlo/PycharmProjects/fc/basecontas.pck1',
                 'listacontasprevisto': '/Users/carlo/PycharmProjects/fc/basecontasprevisto.pck1',
                 'listacontaprovisaosaldo': '/Users/carlo/PycharmProjects/fc/basecontaprovisaosaldo.pck1',
                 'listatrans': '/Users/carlo/PycharmProjects/fc/basetrans.pck1',
                 'listainvest': '/Users/carlo/PycharmProjects/fc/baseinvest.pck1',
                 'listaemprest': '/Users/carlo/PycharmProjects/fc/baseemprest.pck1',
                 'basemesano': '/Users/carlo/PycharmProjects/fc/basemesano.pck1'
                 }
    arq = Arquivolista(listaarqs[nomelista])
    return arq.ler()


class Arquivolista:
    def __init__(self, caminho):
        self.path = caminho

    def ler(self):
        try:
            file = open(self.path, 'rb')
            listaret = pickle.load(file)
            file.close()
        except FileNotFoundError:
            listaret = []
        return listaret

    def gravar(self, lista):
        file = open(self.path, 'wb')
        pickle.dump(lista, file)
        file.close()


def abrearquivodf(nomedf):
    listaarqsdf = {'dftrans': '/Users/carlo/PycharmProjects/fcpandas/dftrans.pck1',
                   'dfmeios': '/Users/carlo/PycharmProjects/fcpandas/dfmeios.pck1',
                   'dfcontasprevisto': '/Users/carlo/PycharmProjects/fcpandas/dfcontasprevisto.pck1',
                   'dfcontas': '/Users/carlo/PycharmProjects/fcpandas/dfcontas.pck1'
                   }
    arqdf = Arquivodf(listaarqsdf[nomedf])
    return arqdf.ler()


def gravaarquivoqdf(nomedf, df):
    listaarqsdf = {'dftrans': '/Users/carlo/PycharmProjects/fcpandas/dftrans.pck1',
                   'dfmeios': '/Users/carlo/PycharmProjects/fcpandas/dfmeios.pck1',
                   'dfcontasprevisto': '/Users/carlo/PycharmProjects/fcpandas/dfcontasprevisto.pck1',
                   'dfcontas': '/Users/carlo/PycharmProjects/fcpandas/dfcontas.pck1'
                   }
    arqdf = Arquivodf(listaarqsdf[nomedf])
    return arqdf.gravar(df)


class Arquivodf:
    def __init__(self, caminho):
        self.path = caminho

    def ler(self):
        try:
            file = open(self.path, 'rb')
            dfret = pickle.load(file)
            file.close()
        except FileNotFoundError:
            dfret = pd.DataFrame([])
        return dfret

    def gravar(self, df):
        file = open(self.path, 'wb')
        pickle.dump(df, file)
        file.close()
