import paho.mqtt.client as mqtt
import uuid

clienteID = uuid.uuid4()
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,"Cliente-{}".format(clienteID))
client.username_pw_set("dispositivo", "abc123.")

bombilla_encendida = False
topic_luz = "/oficina/luz1"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado con exito al broker")
        # Es aquí donde nos suscribimos al topic para empezar a escuchar
        client.subscribe(topic_luz)
        print("Suscrito a: " + topic_luz)
    else:
        print("Error de conexion. Codigo: " + str(rc))

def on_message(client, userdata, msg):
    global bombilla_encendida
    
    # El contenido del mensaje llega en msg.payload (lo pasamos a texto)
    orden = msg.payload.decode("utf-8").strip()
    
    if orden == "On":
        if not bombilla_encendida:
            bombilla_encendida = True
            print("Encendendo bombilla")
        else:
            print("La bombilla ya esta encendida")
            
    elif orden == "Off":
        if bombilla_encendida:
            bombilla_encendida = False
            print("Apagando bombilla")
        else:
            print("La bombilla ya esta apagada")

client.on_connect = on_connect
client.on_message = on_message

client.connect("<IP_alojado_mosquitto_server", 1884)
print("Simulador de bombilla activo. Esperando mensajes...")
client.loop_forever()





