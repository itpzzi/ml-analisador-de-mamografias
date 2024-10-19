from typing import List
import pandas as pd
from tipos import NomeColunas


class PreProcessadorDados:
    def __init__(self, padrao_faltante: str):
        self.padrao_faltante = padrao_faltante

    def substituir_faltantes_por_mediana(
        self, df: pd.DataFrame, colunas: List[str]
    ) -> pd.DataFrame:
        df = df.copy()
        df.replace(self.padrao_faltante, pd.NA, inplace=True)

        for coluna in colunas:
            df[coluna].fillna(df[coluna].median(), inplace=True)

        return df

    def converter_tipos_dados(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df[NomeColunas.IDADE.value] = pd.to_numeric(
            df[NomeColunas.IDADE.value], errors="coerce", downcast="integer"
        )

        colunas_categoricas = [
            NomeColunas.FORMA.value,
            NomeColunas.MARGEM.value,
            NomeColunas.DENSIDADE.value,
        ]

        for col in colunas_categoricas:
            df[col] = df[col].astype("category")

        return df
