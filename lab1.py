from mininet.topo import Topo

class Lab1Topo( Topo ):
    def build( self ):
        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's1' )
        rightSwitch = self.addSwitch( 's2' )
        topSwitch = self.addSwitch( 's3' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )
        self.addLink( rightSwitch, topSwitch )
        self.addLink( leftSwitch, topSwitch )



topos = { 'lab1topo': ( lambda: Lab1Topo() ) }
