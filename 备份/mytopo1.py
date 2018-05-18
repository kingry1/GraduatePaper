
"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
import fileinput

def initTopo(filePath):
	#calculate the lineNumber of text
	length = 0
	for line in fileinput.input(filePath):
		length = length + 1
	res = range(length)
	i = 0;
	for line in fileinput.input(filePath):
		j = 0
		#remove the line-break
		line = line.replace("\r\n", "")
		temp = range(len(line))
		for char in line:
			#transform string into integer
			temp[j] = int(char)
			j = j+1
		res[i] = temp
		i = i+1
	print(res)
	return res

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        #initilize netTopo /home/zhl/mininet/custom/test.txt
        topo = initTopo('/home/zhl/mininet/custom/test.txt')
        length = len(topo)

        #arrayList of host
        switches = range(length)
        print(length)
        switchNumber = 0
        for num in range(length):
        	switches[switchNumber] = self.addSwitch('switch' + str(switchNumber + 1))
        	switchNumber = switchNumber + 1
        i = 0
        for horizontal in topo:
        	j = 0
        	for each in horizontal:
        		if each == 1:
        			self.addLink(switches[i],switches[j])
        		j = j + 1
        	i = i + 1

topos = { 'mytopo': ( lambda: MyTopo() ) }

