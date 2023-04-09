#!/bin/python3

from flask import Flask, request, jsonify

app = Flask(__name__)
clients = {}
commands = {}

@app.route('/register', methods=['POST'])
def registerClient():
	clientID = str(uuid4())
	clients[clientID] = {'status': 'online'}
	return jsonify({'clientID': clientID})
	
@app.route('/command', methods=['POST'])
def postCommand():
	clientID = request.form.get('clientID')
	cmd = request.form.get('cmd')
	if not clientID or not cmd:
		return jsonify({"error": "Missing clientID or cmd"})
	commands[clientID] = cmd
	return jsonify({"status": "Command Queued"})
	
@app.route('/check_command/<clientID>', methods=['GET']
def check_command(clientID):
	if clientID not in clients:
		return jsonify({"error", "Unregistered Client"})
	
	cmd = commands.get(clientID, '')
	if cmd:
		del commands[clientID]
	return jsonify({"cmd": cmd})
	

@app.route('/', methods=['POST'])
def handleCommand():
	data = request.get_json(
	cmd = data.get('cmd', None)
	if cmd:
		# This processes the command and returns the results
		# For simplicity this just returns the recieved command
		# This is merely a debugging line, later implementations will include a more robust response.
		return jsonify({"result": f"Command Received: {cmd})
	return jsonify({"error": "Error: No Command Received"})
	
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=31337)
