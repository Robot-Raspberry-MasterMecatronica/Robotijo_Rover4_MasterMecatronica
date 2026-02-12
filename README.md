# 🤖 Robotijo Rover4 - Master Mecatrónica

---

## 👥 Autores

**Equipo 4 - Master Mecatrónica**
- Luis Enrique Padilla Belmonte
- Iago Villasanin Vázquez 
- Antonio Oliva Arrojo

---

## 📝 Descripción del Proyecto

**Robotijo Rover4** es un robot rover autónomo e inteligente desarrollado como proyecto del Máster en Mecatrónica. El sistema está diseñado para funcionar sobre una **Raspberry Pi** e integra múltiples sensores y actuadores para realizar tareas de navegación autónoma y seguimiento de línea.

El programa principal (`mi_robot.py`) implementa un sistema de control en tiempo real con **4 modos de funcionamiento**:

**Modos Implementados:**
1. 🛤️ **Seguidor de línea** - Navegación autónoma usando 3 sensores infrarrojos
2. 🚗 **Evitar obstáculos** - Detección y esquiva con sensor ultrasónico
3. 🎮 **Control manual** - Manejo por teclado (W/A/S/D)
4. 🔬 **Test de sensores** - Diagnóstico en tiempo real

**Características del sistema:**
- 🔒 Sistema anti-colisión integrado en modo seguidor de línea
- ⚡ Control en tiempo real (100Hz en modo seguidor)
- 🎯 Velocidades configurables mediante código
- 🛑 Detención segura con Ctrl+C

Adicionalmente, incluye una interfaz gráfica opcional (`main.py`) para control remoto con streaming de video, LEDs y buzzer.

---

## 🚀 Inicio Rápido

Para comenzar a usar el robot inmediatamente:

```bash
cd ~/Robotijo_Rover4_MasterMecatronica
sudo python3 mi_robot.py
```

El programa mostrará un **menú interactivo** con 5 opciones:
1. Seguir línea
2. Evitar obstáculos  
3. Control manual
4. Test de sensores
5. Salir

Selecciona el modo que desees (1-5). Presiona `Ctrl+C` en cualquier momento para volver al menú.

---

## 🔧 Componentes Hardware

### Componentes usados en `mi_robot.py`:
- **Raspberry Pi** (CPU principal)
- **Motor DC** (4 motores para tracción)
- **Driver PCA9685** (control PWM de servos y motores)
- **Sensor Ultrasónico HC-SR04** (detección de distancia)
- **Sensores Infrarrojos** (seguimiento de línea, 3 sensores)

### Componentes adicionales disponibles (usados en `main.py`):
- **Cámara Raspberry Pi** (streaming de video)
- **LEDs RGB** (iluminación)
- **Buzzer** (señales acústicas)
- **Servo** (orientación del sensor ultrasónico)
- **ADC (Conversor Analógico-Digital)**
- **Fotoresistor** (detección de luz ambiente)

---

## 📋 Requisitos de Software

### Dependencias para `mi_robot.py` (Programa Principal)

```bash
python3 >= 3.7
RPi.GPIO
smbus
```

### Dependencias adicionales para `main.py` (Interfaz Gráfica)

```bash
PyQt5
opencv-python
numpy
```

### Instalación de Dependencias

```bash
# Actualizar sistema
sudo apt-get update
sudo apt-get upgrade

# Dependencias mínimas para mi_robot.py
sudo apt-get install python3-pip
pip3 install RPi.GPIO smbus

# Dependencias adicionales solo si usas main.py (GUI)
sudo apt-get install python3-pyqt5 python3-opencv
pip3 install opencv-python numpy
```

---

## 🚀 Cómo Usar el Robot

### **Modo Principal: Control Directo (Recomendado)**

Este es el modo principal de uso del robot. Ejecuta el robot en modo autónomo con seguimiento de línea y control directo.

```bash
cd ~/Robotijo_Rover4_MasterMecatronica
sudo python3 mi_robot.py
```

**Características:**
- ✅ 4 modos de funcionamiento integrados con menú interactivo
- ✅ **Modo 1:** Seguimiento de línea automático usando sensores infrarrojos
- ✅ **Modo 2:** Navegación con evitación de obstáculos (ultrasonido)
- ✅ **Modo 3:** Control manual por teclado (W/A/S/D/X/Q)
- ✅ **Modo 4:** Test de sensores en tiempo real
- ✅ Sistema anti-colisión en modo 1 (detiene el robot si detecta obstáculo < 20cm)
- ✅ Control de velocidad configurable
- ✅ Implementación optimizada para control en tiempo real (100Hz)

**Controles durante ejecución:**
- `Ctrl+C` - Detener el robot de forma segura y volver al menú

**Al ejecutar el programa:**
Se muestra un menú donde puedes seleccionar el modo de operación (1-5). El robot se puede detener en cualquier momento con `Ctrl+C` y volverá al menú principal.

---

### **Modo Alternativo: Control con Interfaz Gráfica (GUI)**

Modo opcional con servidor TCP e interfaz gráfica PyQt5 para control remoto del robot desde un cliente web.

```bash
cd ~/Robotijo_Rover4_MasterMecatronica
python3 main.py
```

**Características:**
- Servidor TCP en puerto 5000 (comandos) y 8000 (video)
- Interfaz gráfica para monitorización
- Streaming de video en tiempo real
- Control remoto desde navegador o aplicación cliente

**Uso:**
1. Ejecutar `main.py`
2. Presionar el botón "Start Server" en la interfaz
3. Conectar desde un cliente a la IP mostrada en la interfaz
4. Controlar el robot mediante la aplicación cliente

---

## 📁 Estructura del Proyecto

```
Robotijo_Rover4_MasterMecatronica/
│
├── mi_robot.py          # ⭐ PROGRAMA PRINCIPAL - Control directo y seguidor de línea
│
├── main.py              # Aplicación alternativa con GUI (PyQt5)
├── server.py            # Servidor TCP/IP
├── tcp_server.py        # Implementación del servidor TCP
├── server_ui.py         # Interfaz de usuario Qt
│
├── car.py               # Control general del vehículo
├── motor.py             # Driver de motores DC
├── servo.py             # Control de servomotores
├── camera.py            # Captura y streaming de video
├── ultrasonic.py        # Sensor ultrasónico HC-SR04
├── infrared.py          # Sensores infrarrojos
├── led.py               # Control de LEDs RGB
├── buzzer.py            # Control del buzzer
├── photoresistor.py     # Sensor de luz
├── adc.py               # Conversor analógico-digital
├── pca9685.py           # Driver PCA9685 (PWM)
│
├── command.py           # Procesamiento de comandos
├── message.py           # Parseo de mensajes
├── parameter.py         # Parámetros de configuración
├── Thread.py            # Utilidades de threading
├── test.py              # Scripts de prueba
│
└── params.json          # Archivo de configuración
```

---

## ⚙️ Configuración

### Archivo `params.json`

Contiene parámetros de configuración del robot:
- Velocidades de motores
- Umbrales de sensores
- Configuración de cámara
- Parámetros del servidor

### Personalización en `mi_robot.py`

Ajusta estos valores según tu robot:

```python
self.speed_forward = 600   # Velocidad hacia adelante
self.speed_turn = 800      # Velocidad de giro
self.speed_manual = 700    # Velocidad en modo manual
```

---

## 🔍 Solución de Problemas

### Error: "Permission denied" al acceder a GPIO
```bash
# Ejecutar con sudo
sudo python3 mi_robot.py
```

### El robot no se mueve
- Verificar conexiones de los motores
- Comprobar alimentación de la Raspberry Pi y motores
- Revisar driver PCA9685

### No se obtiene video
- Verificar que la cámara esté habilitada: `sudo raspi-config`
- Comprobar conexión de la cámara
- Verificar permisos de acceso a `/dev/video0`

### El servidor no inicia
- Verificar que los puertos 5000 y 8000 no estén en uso
- Comprobar conectividad de red (wlan0)

---

## 📜 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

---

**¡Disfruta corrigiendo nuestro codigo! 🤖🚀**
