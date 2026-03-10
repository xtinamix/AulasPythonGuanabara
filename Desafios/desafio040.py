# Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de
# acordo com a media atingida:
# - Media abaixo de 5.0: REPROVADO
# - Media entre 5.0 e 6.9: RECUPERAÇÃO
# - Media 7.0 ou superior: APROVADO

n1 = float(input('Qual a primeira nota: '))
n2 = float(input('Qual a segunda nota: '))
media = (n1 + n2) /2
if media < 5:
    print('Sua média foi {:.2f}. Você foi \033[31mREPROVADO!\033[m'.format(media))
elif 5 <= media and media < 6.91:
    print('Sua média foi {:.2f}. Você está de \033[33mRECUPERAÇÃO\033[m.'.format(media))
else:
    print('PARABÉNS sua média foi {:.2f}! você foi \033[1;34mAPROVADO\033[m.'.format(media))