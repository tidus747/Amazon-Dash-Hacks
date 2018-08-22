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

from pydhcplib.dhcp_network import *
import telebot

# Parámetros de configuración del BOT
try:
    with open("apiKey.txt", "r") as file:
        chat_id = file.readline().strip()
        GROUP = file.readline().strip()
        TOKEN = file.readline().strip()
        if len(chat_id) == 0 and len(GROUP) == 0:
            print("No se han introducido los ID correctos. Revisa el fichero apiKey.txt")
            exit()
        if len(TOKEN) == 0:
			print("El TOKEN introducido no es correcto. Revisa el fichero apiKey.txt")
			exit()

except FileNotFoundError:
    open("apiKey.txt", "w").close()
    print("Por favor introduce el chat_id, el group_id y el token del BOT en el fichero api_key.txt")
    exit()

telegram_bot = telebot.TeleBot(TOKEN)

def send_message():
	global TOKEN, telegram_bot, GROUP, chat_id
	telegram_bot.send_message(chat_id,'Hola')

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
dashbuttons.register("68:54:fd:af:c8:74", send_message) # Declaramos el dash que vamos a utilizar con su dirección MAC asociada
server = Server(netopt, dashbuttons)

while True :
    server.GetNextDhcpPacket()
