from abc import ABC, abstractmethod

import pandas as pd


class NormalizadorNumericoBase(ABC):
    @abstractmethod
    def ajustar(self, dados: pd.Series) -> None:
        pass

    @abstractmethod
    def normalizar(self, dados: pd.Series) -> pd.Series:
        pass


class NormalizadorMinMax(NormalizadorNumericoBase):
    def __init__(self):
        self.minimo: float = 0
        self.maximo: float = 0

    def ajustar(self, dados: pd.Series) -> None:
        self.minimo = dados.min()
        self.maximo = dados.max()

    def normalizar(self, dados: pd.Series) -> pd.Series:
        return (dados - self.minimo) / (self.maximo - self.minimo)


class NormalizadorZScore(NormalizadorNumericoBase):
    def __init__(self):
        self.media: float = 0
        self.desvio_padrao: float = 0

    def ajustar(self, dados: pd.Series) -> None:
        self.media = dados.mean()
        self.desvio_padrao = dados.std()

    def normalizar(self, dados: pd.Series) -> pd.Series:
        return (dados - self.media) / self.desvio_padrao
