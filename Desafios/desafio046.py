# Faca um programa que mostre na tela ma contagem regressivapara o estouro de fogos de artificio, indo de 10 ate 0,
# cokm uma pausa de 1 segundo entre eles.
from time import sleep
print('''Os fogos se iniciarão em: ''')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('\033[1;31mBUM!!! BUM!!! BUM!!!')