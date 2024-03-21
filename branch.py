from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import Topo
from mininet.cli import CLI


class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(s1, s2)


if __name__ == '__main__':
    topo = MyTopo()
    net = Mininet(topo=topo, controller=RemoteController, autoSetMacs=True)
    net.start()
    net.pingAll()
    CLI(net)
    net.stop()
