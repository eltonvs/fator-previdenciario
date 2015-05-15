#!/usr/bin/env python
# -*- coding: UTF-8 -*-

sexo = input("Informe o sexo [M/F]: ")
idade = int(input("Digite a idade que você começou a trabalhar: "))
soma = idade

if sexo.upper() == "M":
	tempo = 95
else:
	tempo = 85

while soma <= tempo:
	idade += 1
	soma += 2

print ("Você poderá se aposentar com %d anos de idade" %idade)
