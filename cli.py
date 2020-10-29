#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from fator_previdenciario import calcula_idade_aposentadoria

sexo = input("Informe o sexo [M/F]: ")
idade_inicio = int(input("Digite a idade que você começou a trabalhar: "))

idade_aposentadoria = calcula_idade_aposentadoria(idade_inicio, sexo)

print(f"Você terá a possibilidade de se aposentar com {idade_aposentadoria} anos de idade")

