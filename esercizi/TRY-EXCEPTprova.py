sium='bruh'

try:
    sium=float(sium)
except Exception as e:
    print('Sei un fetuso...')
    print('Quando la tua variabile è "{}", come faccio a cambiargli il tipo?'.format(sium))
    print('per la precisione, il tuo errore è "{}"'.format(e))
    print('...ma ti darò una mano, lo imposto a 0.0')
    sium=0.0

print(sium)