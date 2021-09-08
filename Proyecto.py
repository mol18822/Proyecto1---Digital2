# Universidad del Valle de Guatemala
# Electrónica Digital II
# Luis Pedro Molina
# Carné 18822
# Proyecto No. 1 - Cinta transportadora

# Adafruit IO
# https://io.adafruit.com/


from Adafruit_IO import Client, RequestError, Feed
from time import sleep
import serial
import time

# Enviar dato 
def enviar():
    time.sleep(0.01)
    puerto.write(cent)
    time.sleep(0.01)
    puerto.write(dece)
    time.sleep(0.01)
    puerto.write(unit)


    envio = 184     #dato que viene desde la pág
    nulo = 0        #valor nulo 
    nulo = str(nulo)#char nulo
    temporal1 = 0
    temporal2 = 0

ADAFRUIT_IO_USERNAME = "Luispedro00"
ADAFRUIT_IO_KEY      = "aio_imPQ55lzH1jbUDNTe3IiRV4FmxaG"
aio                  = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

puerto = serial.Serial("COM2",9600)
puerto.timeout = 3
time.sleep(1)

print('Port successfully opened... \n')

Servomotor_feed = aio.feeds('servomotor')
Send_feed = aio.feeds('send')

puerto.write(b'a')
print('Sending....')
centenas = puerto.readline(1).decode("ascii")
decenas = puerto.readline(1).decode("ascii")
unidades = puerto.readline(1).decode("ascii")
contador_b = int(centenas+decenas+unidades)
print('Retrieving data...')
aio.send_data(Sensor01_feed.key, contador_b)

Send_data = aio.receive(Send_feed.key)

bitcount = Send_data.value
cent = bitcount[0:1].encode('ascii', 'ignore')
dece = bitcount[1:2].encode('ascii', 'ignore')
unit = bitcount[2:3].encode('ascii', 'ignore')
enviar()    # Se mandan los datos
print(bitcount)

    
print('Operation successful...')


#from Adafruit_IO import Client, Feed

# Declaración de usuario y llave de Adafruit IO

#ADAFRUIT_IO_USERNAME = "Luispedro00"
#ADAFRUIT_IO_KEY      = "aio_imPQ55lzH1jbUDNTe3IiRV4FmxaG"
#aio                  = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Conexión de PORTD

#digital_feed = aio.feeds('fotoresistencia')      # Feed receptor de datos
#aio.send_data(digital_feed.key, 78)             # Dato enviado --> 15
#digital_data = aio.receive(digital_feed.key)    # Recepción de datos
#print(f'digital signal: {digital_data.value}')  #

# Conexión de PORTA

#digital_feed = aio.feeds('servomotor')      # Feed receptor de datos
#aio.send_data(digital_feed.key, 56)             # Dato enviado --> 18
#digital_data = aio.receive(digital_feed.key)    # Recepción de datos
#print(f'digital singal: {digital_data.value}')  #

#send_feed = aio.feeds('send')                   #
#send_data = aio.receive(send_feed.key)          #
#print(f'send signal: {send_data.value}')        #
