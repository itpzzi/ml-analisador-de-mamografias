from matplotlib import pyplot as plt
import pandas as pd
from tipos import NomeColunas


class AnalisadorDados:
    @staticmethod
    def plotar_distribuicao_idade_casos_malignos(df: pd.DataFrame) -> None:
        casos_malignos = df[df[NomeColunas.GRAVIDADE.value] == 1]
        idades = casos_malignos[NomeColunas.IDADE.value].astype(float)

        plt.figure(figsize=(10, 6))
        plt.boxplot(idades)
        plt.title("Distribuição de idades para casos de câncer maligno")
        plt.ylabel("Idade")
        plt.show()


class AnaliseMamografia:
    def __init__(self):
        self.analisador = AnalisadorDados()

    def analisar(self, df: pd.DataFrame) -> pd.DataFrame:
        self.analisador.plotar_distribuicao_idade_casos_malignos(df)

        return df
