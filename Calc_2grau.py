import math

print ('Calcular equação de segundo grau')
print ('---------------------------------')

while True:
    try:
        a = int(input("Digite o valor de A: "))
        if (a > 0):
            break
        if (a < 0):
            break
    except ValueError:
            print('"A" não pode ser igual a zero ou um número não-inteiro. Tente novamente.')

b = int(input("Digite o valor de B: "))

c = int(input("Digite o valor de C: "))


print ('sua equação é:', a, 'x² +', b, 'x +', c, ' = 0')

# Calculando Delta (b²-4ac)

delta = int(b * b - (4 * a * c))
print ('o valor de delta é: ', delta)

if (delta < 0):
    print ('Para delta negativo, não existem raízes reais.')
    input('Press ENTER to exit')

raiz_delta = math.sqrt(delta)

#Determinando raízes
    
if (delta == 0):
    x1 = ((- b + raiz_delta) / (2*a))
    print ('Para delta = 0, existem duas raízes reais iguais.')
    print ('A raiz da equação é: ', x1)
    
else:
    x1 = ((- b + raiz_delta) / (2*a))
    x2 = ((- b - raiz_delta) / (2*a))
    print ('Para delta positivo, existem duas raízes reais distintas.')
    print ('As raízes da equação são: ', x1, 'e ', x2)
    
input('Press ENTER to exit')