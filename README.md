# MQTT Light Simulator 💡
Este proyecto es una práctica de comunicación IoT utilizando el protocolo MQTT. Consiste en un servidor (Broker) configurado en una máquina virtual y un simulador de bombilla inteligente desarrollado en Python que reacciona a comandos remotos.

## 🏗️ Arquitectura del Sistema
- Broker: Mosquitto MQTT ejecutándose en Ubuntu (VM).

- Cliente Suscriptor: Script de Python que simula una bombilla.

- Cliente Publicador: Terminal de la máquina anfitriona enviando comandos mediante mosquitto_pub.

## ⚙️ Configuración del Servidor (VM Debian)

El servidor Mosquitto está configurado con las siguientes medidas de seguridad y acceso:

1. Puerto: 1884 (Personalizado para evitar conflictos con el estándar 1883).

2. Seguridad: * Acceso anónimo deshabilitado (allow_anonymous false).

        Autenticación mediante archivo de contraseñas en /etc/mosquitto/usuarios.txt.

3. Listener: Configurado para escuchar en la IP específica de la máquina virtual.

## Simulador de Bombilla (Python)
El script simulador_bombilla.py utiliza la librería paho-mqtt (API v1) para gestionar la lógica de la "luz".

**Lógica de funcionamiento:**
- Se suscribe al topic: /oficina/luz1.

- Comando "On": Si la bombilla está apagada, se enciende e imprime Encendendo bombilla.

- Comando "Off": Si la bombilla está encendida, se apaga e imprime Apagando bombilla.

- Si recibe un comando y la bombilla ya está en ese estado, notifica que no hay cambios.

**Requisitos:**
- Python 3.x
- Entorno virtual (venv) con la librería paho-mqtt instalada.

## 🚀 Cómo ponerlo en marcha
1. Preparar el entorno Python

```bash
# Crear entorno virtual
python3 -m venv .venv
# Activar el entorno
source .venv/bin/activate
# Instalar dependencias
pip install paho-mqtt
```
2. Ejecutar el simulador
Desde la carpeta raíz del proyecto
```bash
# Crear entorno virtual
python3 src/simulador_bombilla.py
```
3. Enviar comandos (Mando a distancia)
Abre otra terminal y usa el cliente de consola para interactuar:

**Encender:**
```bash
mosquitto_pub -h <IP_VM> -p 1884 -u "dispositivo" -P "abc123." -t "/oficina/luz1" -m "On"
```
**Apagar:**
```bash
mosquitto_pub -h <IP_VM> -p 1884 -u "dispositivo" -P "abc123." -t "/oficina/luz1" -m "Off"-m "On"
```
## 🛠️ Tecnologías utilizadas
- **Ubuntu**: Sistema operativo del servidor.
- **Mosquitto**: Broker MQTT.
- **Python**: Lógica del cliente.
- **Paho-MQTT**: Librería de comunicación.
- **UUID**: Para la generación de identificadores de cliente únicos.

