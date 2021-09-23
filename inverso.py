numero = int(input().strip())
milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = (numero % 100) // 10
unidade = numero % 10
print(f'{unidade}{dezena}{centena}{milhar}')

