from dataclasses import dataclass
from typing import Optional


@dataclass
class ConfiguracaoDados:
    delimitador: str = ","
    padrao_faltante: str = "?"
    cabecalho: Optional[int] = None
