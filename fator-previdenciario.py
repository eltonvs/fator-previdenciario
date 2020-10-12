#!/usr/bin/env python
# -*- coding: UTF-8 -*-

sexo = input("Informe o sexo [M/F]: ")
idade = int(input("Digite a idade que você começou a trabalhar: "))
#Soma = idade que iniciou a contribuir + tempo de contribuição inicial (0)
soma = idade

#Define o a soma final (idade + tempo de contribuição) de acordo com o sexo informado
tempo = 95 if (sexo.upper() == "M") else 85 

while soma <= tempo:
    #Adiciona mais um ano à idade
    idade += 1
    #Adiciona 2 à soma (1 da idade e 1 do tempo de contribuição)
    soma += 2

#Mostra o texto na tela
print(f"Você terá a possibilidade de se aposentar com {idade} anos de idade")
