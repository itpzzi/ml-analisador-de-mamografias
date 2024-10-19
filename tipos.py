from enum import Enum


class FonteDados(Enum):
    MAMOGRAFIA = "mammographic_masses.data.txt"


class NomeColunas(Enum):
    BI_RADS = "BI-RADS"
    IDADE = "idade"
    FORMA = "forma"
    MARGEM = "margem"
    DENSIDADE = "densidade"
    GRAVIDADE = "gravidade"
