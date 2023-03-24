import time

def contagem(t):
    while t:
        min, seg = divmod(t, 60)
        cronometro = '{:02d}:{:02d}'.format(min, seg)
        print(cronometro, end='\r')
        time.sleep(1)
        t -= 1

    print('Contagem regressiva concluído!')

t = input('Coloque o número em segundos: ')

contagem(int(t))