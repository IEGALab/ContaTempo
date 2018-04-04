
print("programa soma tempo")
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
