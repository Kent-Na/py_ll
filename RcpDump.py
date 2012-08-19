from RcpConnection import *

c = RcpConnection()
c.connectToDefaultServer()
c.loginContext('pw')
cmd = {
	'command':'dump'
}
c.sendCommand(cmd)

c.receiveCommand()
c.receiveCommand()
c.receiveCommand()
c.receiveCommand()
