"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost1 = self.addHost( 'h1' )
	leftHost2 = self.addHost( 'h2' )
        rightHost1 = self.addHost( 'h3' )
	rightHost2 = self.addHost( 'h4' )
        leftSwitch = self.addSwitch( 'h5' )
        rightSwitch = self.addSwitch( 'h6' )

        # Add links
        self.addLink( leftHost1, leftSwitch )
	self.addLink( leftHost2, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost1 )
	self.addLink( rightSwitch, rightHost2 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
