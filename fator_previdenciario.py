#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def calcula_idade_aposentadoria(idade_inicio, sexo):
    # Define o a soma final (idade + tempo de contribuição) de acordo com o sexo informado
    tempo = 95 if sexo.upper() == 'M' else 85
    #Soma = idade que iniciou a contribuir + tempo de contribuição inicial (0)
    soma = idade = idade_inicio
    while soma <= tempo:
        # Adiciona mais um ano à idade
        idade += 1
        # Adiciona 2 à soma (1 da idade e 1 do tempo de contribuição)
        soma += 2
    return idade
