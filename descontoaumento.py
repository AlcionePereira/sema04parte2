preço = float(input().strip())
valor_percentual = float(input().strip())
preço_com_desconto = preço - (preço * valor_percentual / 100)
preço_com_aumento = preço + (preço * valor_percentual / 100)
print('%.2f' % preço_com_aumento)
print('%.2f' % preço_com_desconto)

