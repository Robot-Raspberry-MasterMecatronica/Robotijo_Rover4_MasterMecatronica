#!/usr/bin/env python3
"""
Programa principal para controlar el robotijo
Autor: Equipo4
Fecha: 30 de enero de 2026
"""

from infrared import Infrared
from motor import Ordinary_Car
from ultrasonic import Ultrasonic
from servo import Servo
from buzzer import Buzzer
from led import Led
import time
import sys

class Robot:
    """Clase principal que controla el robot"""
    
    def __init__(self):
        """Inicializa todos los componentes del robot"""
        print("🤖 Inicializando robot...")
        
        # Inicializar sensores y actuadores
        self.motor = Ordinary_Car()
        self.infrared = Infrared()
        self.sonic = Ultrasonic()
        self.servo = Servo()
        self.buzzer = Buzzer()
        self.led = Led()
        
    # Configuración de ingeniería (Valores reducidos para control sutil)
        self.speed_forward = 600   # Antes 800
        self.speed_turn = 800      # Antes 1500
        self.speed_manual = 700    # Nueva variable para el modo manual
        
        print("✅ Robot inicializado correctamente\n")
    
    def seguir_linea(self):
        print("🛤️  Modo: SEGUIDOR DE LÍNEA (V3)")
        print("Presiona Ctrl+C para detener")
        
        try:
            while True:
                # 1. Lectura de sensores
                valor = self.infrared.read_all_infrared()
                distancia = self.sonic.get_distance()
                
                # 2. Seguridad anti-choque (Prioridad absoluta)
                if distancia > 0 and distancia < 20:
                    self.detener() # Usamos el nuevo método
                    print(f"🚨 OBSTÁCULO ({distancia:.1f}cm) - Esperando...", end='\r')
                    time.sleep(0.1)
                    continue

                # 3. Lógica de seguimiento (Motores NEGATIVOS para V3)
                
                # CASO A: Línea centrada -> Avanzar
                if valor == 2:
                    self.motor.set_motor_model(-500, -500, -500, -500) # Velocidad moderada
                    print(f"⬆️  RECTO (Valor: {valor})   ", end='\r')
                
                # CASO B: Desvío a la Izquierda -> Corregir girando izquierda
                elif valor == 4 or valor == 6:
                    self.motor.set_motor_model(700, 700, -700, -700)
                    print(f"⬅️  CORRIGIENDO IZQ       ", end='\r')

                # CASO C: Desvío a la Derecha -> Corregir girando derecha
                elif valor == 1 or valor == 3:
                    self.motor.set_motor_model(-700, -700, 700, 700)
                    print(f"➡️  CORRIGIENDO DER       ", end='\r')
                
                # CASO D: ¡PÉRDIDA DE LÍNEA! (0 = Blanco total) -> SEGURIDAD
                elif valor == 0:
                    self.detener()
                    print(f"❓ LÍNEA PERDIDA (Stop)   ", end='\r')
                
                # CASO E: Cruce (7 = Todo negro) -> Parar
                elif valor == 7:
                    self.detener()
                    print(f"⏹️  FINAL DE PISTA        ", end='\r')

                time.sleep(0.01) # Ciclo de control rápido (100Hz)
                
        except KeyboardInterrupt:
            print("\n\n⛔ Saliendo del modo seguidor de línea...")
            self.detener()
    
    def evitar_obstaculos(self):
        print("🚀 Modo: EVITAR OBSTÁCULOS ACTIVO")
        print("Presiona Ctrl+C para detener\n")
        try:
            while True:
                # Obtener distancia del sensor ultrasónico
                distancia = self.sonic.get_distance()
                
                if distancia > 0 and distancia < 30:  # Obstáculo a menos de 30cm
                    print(f"⚠️ Obstáculo detectado a {distancia:.1f} cm. Girando...")
                    
                    # 1. Parar un instante
                    self.motor.set_motor_model(0, 0, 0, 0)
                    time.sleep(0.2)
                    
                    # 2. Marcha atrás sutil (Positivos para ir hacia atrás en V3)
                    self.motor.set_motor_model(self.speed_manual, self.speed_manual, 
                                               self.speed_manual, self.speed_manual)
                    time.sleep(0.5)
                    
                    # 3. Giro para buscar camino (Ajusta los signos según tu prueba manual)
                    self.motor.set_motor_model(-self.speed_turn, -self.speed_turn, 
                                               self.speed_turn, self.speed_turn)
                    time.sleep(0.5)
                    
                else:
                    # CAMINO LIBRE: Adelante recto (Negativos para V3)
                    self.motor.set_motor_model(-self.speed_forward, -self.speed_forward, 
                                               -self.speed_forward, -self.speed_forward)
                
                time.sleep(0.1) # Ciclo de escaneo
        except KeyboardInterrupt:
            self.motor.set_motor_model(0, 0, 0, 0)
    
    def modo_manual(self):
        """Control manual del robot por teclado"""
        print("🎮 Modo: CONTROL MANUAL")
        print("Comandos:")
        print("  w - Adelante")
        print("  s - Atrás")
        print("  a - Izquierda")
        print("  d - Derecha")
        print("  x - Detener")
        print("  q - Salir\n")
        
        import tty
        import termios
        
        # Guardar configuración del terminal
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        
        try:
            tty.setcbreak(fd)
            
            while True:
                tecla = sys.stdin.read(1).lower()
               
                if tecla == 'w':
                    print("⬆️  ADELANTE")
                    self.motor.set_motor_model(-self.speed_manual, -self.speed_manual, -self.speed_manual, -self.speed_manual)
                    
                elif tecla == 's':
                    print("⬇️  ATRÁS")
                    self.motor.set_motor_model(self.speed_manual, self.speed_manual, self.speed_manual, self.speed_manual)
                    
                elif tecla == 'a':
                    print("⬅️  IZQUIERDA")
                    self.motor.set_motor_model(-self.speed_manual, -self.speed_manual, self.speed_manual, self.speed_manual)
                    
                elif tecla == 'd':
                    print("➡️  DERECHA")
                    self.motor.set_motor_model(self.speed_manual, self.speed_manual, -self.speed_manual, -self.speed_manual)
                
                elif tecla == 'x':
                    print("⏹️  DETENIDO")
                    self.motor.set_motor_model(0, 0, 0, 0)
                
                elif tecla == 'q':
                    print("\n👋 Saliendo del modo manual...")
                    break
                    
        finally:
            # Restaurar configuración del terminal
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            self.detener()
    
    def test_sensores(self):
        """Prueba todos los sensores del robot"""
        print("🔬 Modo: TEST DE SENSORES")
        print("Presiona Ctrl+C para detener\n")
        
        try:
            while True:
                # Leer sensores infrarrojos
                ir_valor = self.infrared.read_all_infrared()
                ir1 = self.infrared.read_one_infrared(1)
                ir2 = self.infrared.read_one_infrared(2)
                ir3 = self.infrared.read_one_infrared(3)
                
                # Leer sensor ultrasónico
                distancia = self.sonic.get_distance()
                
                # Mostrar valores
                print(f"IR: [{ir1}][{ir2}][{ir3}] = {ir_valor} | Distancia: {distancia:.1f} cm")
                
                time.sleep(0.5)
                
        except KeyboardInterrupt:
            print("\n\n⛔ Saliendo del test de sensores...")
    
    def detener(self):
        """Detiene todos los motores"""
        self.motor.set_motor_model(0, 0, 0, 0)
        print("🛑 Motores detenidos")
    
    def cerrar(self):
        """Libera todos los recursos"""
        print("\n🔌 Cerrando recursos...")
        self.detener()
        self.motor.close()
        self.infrared.close()
        self.sonic.close()
        print("✅ Recursos liberados correctamente")


def main():
    """Función principal del programa"""
    print("=" * 60)
    print("  🤖 ROBOT FREENOVE 4WD - PROGRAMA PRINCIPAL")
    print("=" * 60)
    print()
    
    # Crear instancia del robot
    robot = Robot()
    
    try:
        while True:
            print("\n📋 MENÚ PRINCIPAL:")
            print("  1. Seguir línea")
            print("  2. Evitar obstáculos")
            print("  3. Control manual")
            print("  4. Test de sensores")
            print("  5. Salir")
            print()
            
            opcion = input("Selecciona una opción (1-5): ")
            
            if opcion == '1':
                robot.seguir_linea()
                
            elif opcion == '2':
                robot.evitar_obstaculos()
                
            elif opcion == '3':
                robot.modo_manual()
                
            elif opcion == '4':
                robot.test_sensores()
                
            elif opcion == '5':
                print("\n👋 Saliendo del programa...")
                break
                
            else:
                print("\n❌ Opción no válida. Intenta de nuevo.")
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario")
    
    finally:
        robot.cerrar()
        print("\n🏁 Programa finalizado\n")


if __name__ == '__main__':
    main()
