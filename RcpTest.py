from RcpConnection import *

c = RcpConnection()
c.connectToDefaultServer()

c.setValue(100,"test");
#c.appendValue("test");

c.receiveCommand()
c.receiveCommand()
c.receiveCommand()
c.receiveCommand()
"""
con = {
	'command':'createUser',
	'username':'cz',
	'password':'const'
}
#c.sendCommand(con)

con = {
	'command':'loginUser',
	'username':'cz',
	'password':'const'
}
c.sendCommand(con)

con = {
	'command':'addContext',
	'name':'cz',
}
c.sendCommand(con)

con = {
	'command':'loginContext',
	'name':'cz',
}
c.sendCommand(con)

con = {
	'command':'sendValue',
	'type':'uint32',
	'value':100.1234}
c.sendCommand(con)

c.receiveCommand()
c.receiveCommand()
con = {
	'command':'kill'
}
c.sendCommand(con)
con = {
	'command':'createUser',
	'username':'okd',
	'password':'okd'
}
c.sendCommand(con)
con = {
	'command':'loginUser',
	'username':'black',
	'password':'bbbox'
	}
c.sendCommand(con)
con = {'command':'loginContext'}
c.sendCommand(con)
con = {'command':'addType',
		'name':'theNewType'}
#c.sendCommand(con)
con = {
	'command':'sendValue',
	'type':'uint32',
	'value':100.1234}
#c.sendCommand(con)
con = {
	'command':'sendValue',
	'type':'string',
	'value':'message'}
#c.sendCommand(con)
con = {
	'command':'appendValue',
	'value':{
		'a':'b',
		'c':'d'},
	'path':102,
	'type':'theNewType'
}
#c.sendCommand(con)
con = {
	'command':'addPermission',
	'username':'black'}
c.sendCommand(con)
con = {
	'command':'removePermission'}
c.sendCommand(con)
con = {'command':'dump'}
c.sendCommand(con)
c.receiveCommand()
c.receiveCommand()
c.receiveCommand()
c.receiveCommand()
"""
