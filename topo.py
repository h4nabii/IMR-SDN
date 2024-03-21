#!/usr/bin/python
from functools import partial

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost, RemoteController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI


class SingleSwitchTopo(Topo):
    def build(self, n=2):
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        self.addLink(switch1, switch2, delay="20ms")
        new_host = self.addHost('h%s' % (n + 1))
        self.addLink(switch2, new_host, delay="10ms")
        for h in range(n):
            host = self.addHost('h%s' % (h + 1),
                                cpu=.5 / n)
            self.addLink(host, switch1, bw=10, delay='10ms', loss=2,
                         max_queue_size=1000, use_htb=True)


def perfTest():
    """Create network and run simple performance test"""
    topo = SingleSwitchTopo(n=4)
    print("Dumping host connections")
    net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink,
                  controller=partial(RemoteController, ip='127.0.0.1', port=6653))
    net.start()
    dumpNodeConnections(net.hosts)
    print("Testing network connectivity")
    net.pingAll()
    print("Testing bandwidth between h1 and h4")
    h1, h4 = net.get('h1', 'h4')
    net.iperf((h1, h4))
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    perfTest()
