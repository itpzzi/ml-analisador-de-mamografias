from pathlib import Path
from analisadores import AnaliseMamografia
from carregadores import CarregadorCSV
from configuracoes import ConfiguracaoDados
from normalizadores import NormalizadorMinMax, NormalizadorZScore
from preprocessadores import PreProcessadorDados
from tipos import FonteDados, NomeColunas


def principal():
    # Definições
    colunas_numericas = [
        NomeColunas.IDADE.value,
        NomeColunas.FORMA.value,
        NomeColunas.MARGEM.value,
        NomeColunas.DENSIDADE.value,
    ]
    config = ConfiguracaoDados()
    nomes_colunas = [col.value for col in NomeColunas]
    fonte_dados = FonteDados.MAMOGRAFIA.value

    # Carregar dados e configurações
    carregador = CarregadorCSV(fonte_dados, config, nomes_colunas)
    df = carregador.carregar()

    # Pré-processar
    preprocessador = PreProcessadorDados(config.padrao_faltante)
    df = preprocessador.substituir_faltantes_por_mediana(df, colunas_numericas)
    df = preprocessador.converter_tipos_dados(df)

    # Análise dos dados
    analise = AnaliseMamografia()
    df = analise.analisar(df)

    # Normalizações
    normalizador = NormalizadorZScore()
    # normalizador = NormalizadorMinMax()
    normalizador.ajustar(df[NomeColunas.IDADE.value])
    df[NomeColunas.IDADE.value] = normalizador.normalizar(df[NomeColunas.IDADE.value])

    print(df)


if __name__ == "__main__":
    principal()
