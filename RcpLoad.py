from RcpConnection import *

c = RcpConnection()
c.connectToDefaultServer()
c.loginContext('pw')
cmd = {
	'command':'load'
}
c.sendCommand(cmd)

c.receiveCommand()
c.receiveCommand()
c.receiveCommand()
c.receiveCommand()
