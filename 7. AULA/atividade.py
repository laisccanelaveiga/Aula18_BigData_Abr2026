#Verificando informações de roubo de carro pelo ponto de vista das cidades

import pandas as pd
import numpy as np


try:
    print("Obtendo dados...")
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    #utf-8, iso-8859-1, latin1, cp1252
    df_ocorrecias = pd.read_csv(ENDERECO_DADOS, sep=";", encoding='iso-8859-1')
   
    #deliminitando variáveis
    df_roubo_veiculo = df_ocorrecias[['munic','roubo_veiculo']]
    
    #totalizando os roubos (agrupando por município)
    df_roubo_veiculo = df_roubo_veiculo.groupby('munic', as_index=False)['roubo_veiculo'].sum()
    
    #manter organizado dos maior pro menor
    df_roubo_veiculo = df_roubo_veiculo.sort_values(by='roubo_veiculo',ascending=False)
    
    # print(df_roubo_veiculo.head())
    
except Exception as e:
    print(f'Erro ao obter dados: {e}')


try:
    print("Calculando as Medidas")
    print("-"*30)
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])

    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
    distancia = abs((media_roubo_veiculo-mediana_roubo_veiculo)/mediana_roubo_veiculo)

    print(f'Medidas de Tendência Central')
    print("-"*30)
    print(f'Média: {media_roubo_veiculo:.0f}\nMediana: {mediana_roubo_veiculo:.0f}')
    print(f'Distância: {distancia:.0%}')
    #50% do estado teve roubos abaixo de 256 de 2003 até agora
    #o fato da media estar mto maior que a mediana é uma tendência que os extremos estão mto distantes

   


except Exception as e:
    print(f'Erro ao processar dados: {e}')