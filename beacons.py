import requests
import json
import asyncio
import discord
import telebot
import paramiko
import socket
import struct
import os

from flask import Flask, request

class Beacon:
	def __init__(self,):
		# Discord beacon config
		self.discordClient = discord.Client()
		self.discordWebhook = 'webhook'
		self.discordChanID = channelID
		
		# Telegram Beacon Config
		self.telegramBot = telebot.Telebot("API KEY")
		self.telegramChatID = chatID
		
		# HTTP Beacon Config
		self.httpApp = flask(__name__)
		self.httpEndpoint = 'http://localhost:5000'
		
		# SSH Beacon Config
		self.sshHost = 'localhost'
		self.sshPort = 2022
		self.sshUser = 'username'
		self.sshPass = 'password'
		
	async def sendDiscordBeacon(self, data):
		await self.discordClient.wait_until_ready()
		await self.discordClient.get_channel(self.discordChanID).send(data)
	
	@self.telegram_bot.message_handler(commands=['start'])
	def startMessage(self, message):
		self.telegram_bot.reply_to(message, '[+] Telegram Beacon Connected'
		
	async def sendTeleBeacon(self, data):
		self.telegram_bot.send_message(self.telegramChatID, data)
		
	@self.http_app.route('/', methods=['POST'])
	def httpBeacon(self)
		data = request.json
		print("[+] HTTP Beacon Connected")
		print(data)
		return "OK", 200
		
	async def sendHTTPBeacon(self, data):
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		r = requests.post(self.httpEndpoint, data=json.dumps(data), headers=headers)
		print("[+] HTTP Beacon Sent")
		print(r.status_code)
		
	def sshBeacon(self, data):
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(self.sshHost, self.sshPort, self.sshUser, self.sshPass)
		print("[+] SSH Beacon Connected")
		stdin, stdout, stderr = client.exec_command('SSH> ' + data)
		print(stdout.read())
		client.close()
	
	async def sendSSHBeacon(self, data):
		loop = asyncio.get_event_loop()
		await loop.run_in_executor(None, self.sshBeacon, data)
		print("[+] SSH Beacon Sent")
		
	async def sendTCPBeacon(self, data, host, port):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host, port))
			s.send(data.encode())
			s.close()
			print("[+] TCP Beacon Sent")
		except:
			print("[-] TCP Beacon Failed")
			
	async def sendUDPBeacon(self, data, host, port):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.sendto(data.encode(), (host, port))
			s.close()
			print("[+] UDP Beacon Sent")
		except:
			print("[-] UDP Beacon Failed")
			
	async def sendICMP(self, data, host):
		try:
			with os.popen("ping -c 1 -W 1 " + host, 'r') as f:
				output = f.read()
				if "1 received" in output:
					print("[+] ICMP Beacon Sent")
				else:
					print("[-] ICMP Beacon Failed")
				
		except:
			print("[-] ICMP Beacon Error")
			
		
			
		
