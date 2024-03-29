import socket
import random
import json

import rlcompleter
import readline

readline.parse_and_bind('tab: complete')

class RcpDocumentInfo:
	def __init__(self):
		self.name = ""
		self.lastUpdateTime = ""

class RcpConnection:
	def __init__(self):
		self.mainSocket = None
		self.typeTable = {}
		self.objects = {}
		self.documentList = []
		self.documentIDTable = {}
		self.userList = []
		self.userIDTable = {}
		self.remain = b""
#will be deprecated
		self.objectsArray = []
		self.outputDebug = True 
		
	def connectToLocal(self):
		host = 'localhost'
		port = 4000
		self.mainSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.mainSocket.connect((host,port))

		cmd = {
			'command':'open',
			'protocol':'alpha1',
			'client':"PyLL"
		}
		self.sendCommand(cmd)

	def connectToTunaCat(self):
		host = "www.tuna-cat.com"
		port = 4000
		self.mainSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.mainSocket.connect((host,port))

		cmd = {
			'command':'open',
			'protocol':'alpha1',
			'client':"PyLL"
		}
		self.sendCommand(cmd)
	
	def close(self):
		self.mainSocket.close()


#class must implement "executeCommand" method
	def bindClassToType(self,classObject,typeName):
		self.typeTable[typeName]=classObject

	def generateObjectID(self):
		while True:
			newID = random.uniform(0,4096*4096-1)	
			if newID in objects:
				return newID

	def executeCommand(self,command):
		if not "command" in command:
			return
		if command["command"]=="createUser":
			userID = command["userID"]
			if userID == 0:
				self.didFailRegist()
			else:
				self.didSucceedRegist()
		if command["command"] == "document":
			dinfo = RcpDocumentInfo()
			dinfo.name = command["name"]
			dinfo.lastUpdateTime = command["lastUpdateTime"]
			self.documentIDTable[command["documentID"]] = dinfo
			self.didUpdateContents()
			

#input: command dictionaly
	def sendCommand(self,command):
		commandString = json.dumps(command)
		if self.outputDebug:
			print("->"+commandString);
		commandString += "\0"
		self.mainSocket.send(bytes(commandString,'utf8'))

	def receiveCommand(self):
		new = self.remain + self.mainSocket.recv(1024*16)
		if new == b"":
			if self.outputDebug:
				print("connection closed")
			self.didLostConnection()
		new = self.remain + new 

		byte_segments = new.split(bytes(b"\0"));
		for segment in byte_segments[:-1]:
			try:
				segment = str(segment, 'utf8')
				if self.outputDebug:
					print("<-"+segment)
				command = json.loads(segment)
				self.executeCommand(command)
			except:
				print("<-X")
		self.remain = byte_segments[-1]


#command sending
	def protocol(self):
		command = {}
		command["command"]="protocol"
		command["protocol"]="RCP-ALPHA"
		command["client"]="Python-RCP"
		self.sendCommand(command)

	def createUser(self,username,password):
		command = {}
		command["command"]="createUser"
		command["username"]=username
		command["password"]=password
		self.sendCommand(command)

	def loginUser(self,username,password):
		command = {}
		command["command"]="loginUser"
		command["username"]=username
		command["password"]=password
		self.sendCommand(command)

	def setPermission(self,username,mode):
		command = {}
		command["command"]="setPermission"
		command["username"]=username
		command["mode"]=mode
		self.sendCommand(command)

	def unsetPermission(self,username):
		command = {}
		command["command"]="unsetPermission"
		command["username"]=username
		self.sendCommand(command)

	def addType(self,name):
		command = {}
		command["command"]="addType"
		command["name"]=name
		self.sendCommand(command)
	
	def appendValue(self,value):
		command = {}
		command["command"]="appendValue"
		command["value"]=value
		self.sendCommand(command)

	def setValue(self,key,value):
		command = {}
		command["command"]="setValue"
		command["path"]=key
		command["value"]=value
		self.sendCommand(command)

	def addContext(self,name):
		command = {}
		command["command"]="addContext"
		command["name"]=name
		self.sendCommand(command)

	def loginContext(self,name):
		command = {}
		command["command"]="loginContext"
		command["name"]=name
		self.sendCommand(command)

	def logoutContext(self):
		command = {}
		command["command"]="logoutContext"
		self.sendCommand(command)

	def resetContext(self):
		command = {}
		command["command"]="resetContext"
		self.sendCommand(command)
#events (these are never called except "didUpdateContents" because did not implemented...)
	def didConnectToServer(send):
		pass
	def didLostConnection(send):
		pass

#implemented
	def didSucceedRegist(self):
		pass
#implemented
	def didFailRegist(self):
		pass

	def didSucceedLogin(send):
		pass
	def didFailLogin(send):
		pass

	def didReceiveUserList(send):
		pass
	def didExecuteCommand(send):
		pass

	def willUpdateContents(send):
		pass
#implemented
	def didUpdateContents(self):
		pass
	def willAddObject(send):
		pass
	def willRemoveObject(send):
		pass
	def willRemoveAllObjects(send):
		pass
