from math import sqrt

nums = list()

n = str(input('Insira um valor [s - Para Sair]: ')).lower()

while n != 's':
    if n.isdigit():
        nums.append(float(n))
        print('adicionado!')
    else:
        print('Insira um valor númerico!')

    n = str(input('Insira um valor [s - Para Sair]: ')).lower()

media = float(sum(nums)/len(nums))
desvio = [i - media for i in nums]
desvioq = list(map(lambda x : x ** 2, desvio))
variancia = sum(desvioq)/len(desvioq)
varianciav = sum(desvioq) / (len(desvioq) - 1)
desviop = sqrt(variancia)
desviopv = sqrt(varianciav)

print('=' * 60)
print('media:', media)
print('desvio:', desvio)
print('variancia', variancia)
print('desvio padrao', desviop)
print('variancia viciada:',varianciav)
print('desvio padrao viciado:', desviopv)
print('=' * 60)
