from abc import ABC, abstractmethod
from pathlib import Path
from typing import List
import pandas as pd
from configuracoes import ConfiguracaoDados


class CarregadorDados(ABC):
    @abstractmethod
    def carregar(self) -> pd.DataFrame:
        pass


class CarregadorCSV(CarregadorDados):
    def __init__(
        self, caminho_arquivo: Path, config: ConfiguracaoDados, nomes_colunas: List[str]
    ):
        self.caminho_arquivo = caminho_arquivo
        self.config = config
        self.nomes_colunas = nomes_colunas

    def carregar(self) -> pd.DataFrame:
        return pd.read_csv(
            self.caminho_arquivo,
            delimiter=self.config.delimitador,
            header=self.config.cabecalho,
            names=self.nomes_colunas,
        )
