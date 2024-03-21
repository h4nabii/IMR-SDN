from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import Topo
from mininet.cli import CLI


class DataCenterTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        c1 = self.addSwitch('s1')
        c2 = self.addSwitch('s2')

        a1 = self.addSwitch('s3')
        a2 = self.addSwitch('s4')
        a3 = self.addSwitch('s5')
        a4 = self.addSwitch('s6')

        e1 = self.addSwitch('s7')
        e2 = self.addSwitch('s8')
        e3 = self.addSwitch('s9')
        e4 = self.addSwitch('s10')

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')

        # self.addLink(c1, a1)
        # self.addLink(c1, a2)
        # self.addLink(c1, a3)
        # self.addLink(c1, a4)

        # self.addLink(c2, a1)
        # self.addLink(c2, a2)
        # self.addLink(c2, a3)
        # self.addLink(c2, a4)

        # self.addLink(a1, e1)
        self.addLink(a1, e2)
        self.addLink(a2, e1)
        self.addLink(a2, e2)
        # self.addLink(a3, e3)
        self.addLink(a3, e4)
        self.addLink(a4, e3)
        self.addLink(a4, e4)

        self.addLink(e1, h1)
        self.addLink(e1, h2)
        self.addLink(e2, h3)
        self.addLink(e2, h4)
        self.addLink(e3, h5)
        self.addLink(e3, h6)
        self.addLink(e4, h7)
        self.addLink(e4, h8)


if __name__ == '__main__':
    topo = DataCenterTopo()
    net = Mininet(topo=topo, controller=RemoteController, autoSetMacs=True)
    net.start()
    CLI(net)
    net.stop()
