"""
IEGA - Grupo de pesquisa em Inovação Engenharia e Gestão do Conhecimento
Programa simples para somar tempos de videos de you tube
by Joao Santanna - jsantanna@gmail.com - 7 abril de 2018

Uso:
Iforme os tempos usando os dois pontos ":" para separar minutos de segundos
ao final digite -1 para sair e apresentar o somatorio de temposself.

Exemplo :
Calcular o somatorio de 3 videos: um com 3minutos e 30 segundos,
outro com 5 minutos e 13 seguntos e o ultimo com 8minutos e 58 segundos

Programa Conta Tempo
Informe o tempo a ser somado:(-1 para sair)
>3:30
>5:13
>8:58
>-1
tempo total = 0 : 17 : 41
"""


print("Programa Conta Tempo")
tempo =0
hora = 0
minutos = 0
segundos = 0
print("Informe o tempo a ser somado:(-1 para sair)")
while True:
    tempo = input(">")
    if tempo != "-1":
        v = tempo.split(':')
        if len(v) == 1:# se só informar o minuto
            minutos = minutos + int(v[0])
            if minutos > 60:
                hora = hora + 1
                minutos = minutos - 60
        else:
            segundos = segundos + int(v[1])
            if segundos > 60:
                minutos = minutos + 1
                segundos = segundos - 60

            minutos = minutos + int(v[0])
            if minutos > 60:
                hora = hora + 1
                minutos = minutos - 60


    else:
        break

print("tempo total =", hora,":",minutos,":", segundos)
