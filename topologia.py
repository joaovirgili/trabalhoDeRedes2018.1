#!/usr/bin/python   
#coding=UTF-8                                                                         
                                                                                        
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.node import RemoteController

class MyTopo(Topo):
    def __init__(self,**opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)

        #Adiciona o switch 's1' a topologia.
        switch = self.addSwitch('s1')
        switch = self.addSwitch('s2')
        switch = self.addSwitch('s3')

        #Adiciona hosts h1 e h2 a topologia.
        for h in xrange(9):
            host = self.addHost('h%d' % (h + 1))

        #Adiciona Links.
        self.addLink('s1', 's2')
        self.addLink('s2', 's3')
        self.addLink('s1', 's3')
        
        self.addLink('h1','s1')
        self.addLink('h2','s1')
        self.addLink('h3','s1')
        self.addLink('h4','s2')
        self.addLink('h5','s2')
        self.addLink('h6','s2')
        self.addLink('h7','s3')
        self.addLink('h8','s3')
        self.addLink('h9','s3')

        self.addHost('h1', ip='10.10.1.101/24')
        self.addHost('h2', ip='10.10.1.102/24')
        self.addHost('h3', ip='10.10.1.103/24')

        self.addHost('h4', ip='10.10.2.101/24')
        self.addHost('h5', ip='10.10.2.102/24')
        self.addHost('h6', ip='10.10.2.103/24')
        
        self.addHost('h7', ip='10.10.3.101/24')
        self.addHost('h8', ip='10.10.3.102/24')
        self.addHost('h9', ip='10.10.3.103/24')


def main():
    topo = MyTopo()
    net = Mininet(topo = topo, controller = RemoteController) 
    net.start()

    s1 = net.get('s1') #Get switch s1 instance from net
    s2 = net.get('s2') #Get switch s1 instance from net
    s3 = net.get('s3') #Get switch s1 instance from net
    
    #---------- ARP ------------------------------------------------------------------#
    #Vocês precisarão dessa parte do codigo para não precisarem tratar o problema
    #de loops na rede no broadcast do protocolo ARP. basta copiar e colar, eestá feito
    #para configurar uma rede com 9 hosts (que é o cas do trabalho).
    #Basta descomentar as proximas 5 linhas no script da topologia de vocês.
    for i in xrange(9):
       h = net.get('h%d' % (i + 1))
       h.cmd("ip route add default dev %s-eth0" % ('h%d' % (i + 1)))
       for j in xrange(9):
           h_dst = net.get('h%d' % (j+1))
           h.setARP(h_dst.IP(), h_dst.MAC())
    # ---------------------------------------------------------------------------------#

    CLI(net)
    net.stop()

if __name__ == '__main__':
    main()