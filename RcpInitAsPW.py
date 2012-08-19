from RcpConnection import *

c = RcpConnection()
c.connectToDefaultServer()

c.addContext('pw')
c.loginContext('pw')

c.receiveCommand()
c.receiveCommand()
c.receiveCommand()
c.receiveCommand()
