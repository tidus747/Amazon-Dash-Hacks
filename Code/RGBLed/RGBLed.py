#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Ivan Rodriguez - 2018
Original Code -> https://www.nathankowald.com/blog/2017/05/dash-button-with-raspberry-pi/
'''

#importamos los módulos necesarios para nuestro código
from pydhcplib.dhcp_network import *
import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT) ## Color Rojo
GPIO.setup(15, GPIO.OUT) ## Color Verde
GPIO.setup(18, GPIO.OUT) ## Color Azul

Colores = np.array([14,15,18]) # Es importante que el orden sea RGB

def Apagar_led(Leds):
    for i in range(len(Leds)):
        GPIO.output(Leds[i],False)
    return 0

def Encender_leds(Leds):
	for i in range(len(Leds)):
		GPIO.output(Leds[i],True)
		time.sleep(0.05)
		GPIO.output(Leds[i],False)
	for i in range(len(Leds)):
		GPIO.output(Leds[len(Leds)-i-1],True)
		time.sleep(0.05)
		GPIO.output(Leds[len(Leds)-i-1],False)

def Encender_mix_rgb(r,g,b, Colores):
    if (r > 0):
        GPIO.output(Colores[0],True)
    else:
        GPIO.output(Colores[0],False)
    if (g > 0):
        GPIO.output(Colores[1],True)
    else:
        GPIO.output(Colores[1],False)
    if (b > 0):
        GPIO.output(Colores[2],True)
    else:
        GPIO.output(Colores[2],False)
    return 0

def accion_led():
    global Colores
    # Código principal desde el que usamos todas las funciones
    Apagar_led(Colores)

    for j in range(10):
    	Encender_leds(Colores)

    # Encendemos el color Cyan
    Encender_mix_rgb(0,1,1, Colores)
    time.sleep(3)
    # Encendemos el color Amarillo
    Encender_mix_rgb(1,1,0, Colores)
    time.sleep(3)
    # Encendemos el color Magenta
    Encender_mix_rgb(1,0,1, Colores)
    time.sleep(3)
    # Encendemos el color Blanco
    Encender_mix_rgb(1,1,1, Colores)
    time.sleep(3)
    Apagar_led(Colores)

netopt = {'client_listen_port':"68", 'server_listen_port':"67", 'listen_address':"0.0.0.0"}

class Server(DhcpServer):
	def __init__(self, options, dashbuttons):
		DhcpServer.__init__(self, options["listen_address"],
								options["client_listen_port"],
								options["server_listen_port"])
		self.dashbuttons = dashbuttons

	def HandleDhcpRequest(self, packet):
		mac = self.hwaddr_to_str(packet.GetHardwareAddress())
		self.dashbuttons.press(mac)


	def hwaddr_to_str(self, hwaddr):
		result = []
		hexsym = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
		for iterator in range(6) :
			result += [str(hexsym[hwaddr[iterator]/16]+hexsym[hwaddr[iterator]%16])]
		return ':'.join(result)

class DashButtons():
	def __init__(self):
		self.buttons = {}

	def register(self, mac, function):
		self.buttons[mac] = function

	def press(self, mac):
		if mac in self.buttons:
			self.buttons[mac]()
			return True
		return False


# Comienzo del código principal
dashbuttons = DashButtons()
dashbuttons.register("68:54:fd:af:c8:74", accion_led) # Declaramos el dash que vamos a utilizar con su dirección MAC asociada
server = Server(netopt, dashbuttons)

while True :
    server.GetNextDhcpPacket()
