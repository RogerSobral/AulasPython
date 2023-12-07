# -*- coding: utf-8 -*-
import re

texto="""	Lorem ipsum rutrum amet a curae pharetra lorem mattis 
sed felis habitant varius ut, placerat adipiscing donec pulvinar 
phasellus commodo sobral per consequat ut laoreet placerat. fusce 
ut convallis urna integer diam sapien hac habitasse per tempor massa 
accumsan, vulputate arcu in maria aenean 22 placerat nec aenean commodo 
imperdiet pellentesque, potenti velit convallis quis accumsan commodo et 
condimentum eu amet curae. fusce tempor leo Sobral malesuada vitae
 quisque tempor, Maria dapibus nostra cubilia turpis pulvinar sagittis
  congue, ac mollis nullam sem sollicitudin eu. quisque conubia 
  condimentum habitasse cras bibendum orci aliquam elementum, 
  nunc per laoreet in inceptos elementum. 
"""
# Metacaracter
# |   -> Ou do teste lógico
# .   -> Qualquer caracter menos a quebra de linha
# [ ] -> Define um intervalo de valores, range ou caracteres especificos
# De acordo com o padrão passado ele retorna um ou mais elementos encontrados através de uma lista
lista=re.findall("[Ss]o..al|maria|aliquam|[0-9]",texto,flags=re.IGNORECASE)
print(lista)

