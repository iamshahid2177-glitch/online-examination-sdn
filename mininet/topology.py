from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.topo import Topo


class ExamTopo(Topo):

    def build(self):

        s1 = self.addSwitch(
            's1',
            protocols='OpenFlow13'
        )

        h1 = self.addHost(
            'h1',
            ip='10.0.0.1/24'
        )

        h2 = self.addHost(
            'h2',
            ip='10.0.0.2/24'
        )

        h3 = self.addHost(
            'h3',
            ip='10.0.0.3/24'
        )

        h4 = self.addHost(
            'h4',
            ip='10.0.0.4/24'
        )

        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)
        self.addLink(h4, s1)


def run():

    topo = ExamTopo()

    net = Mininet(
        topo=topo,
        controller=None,
        switch=OVSSwitch,
        autoSetMacs=True
    )

    net.addController(
        'c0',
        controller=RemoteController,
        ip='127.0.0.1',
        port=6653
    )

    net.start()

    print("\n*** Exam SDN topology started")
    print("*** Hosts:")
    print("*** h1 = Student 1")
    print("*** h2 = Student 2")
    print("*** h3 = Student 3")
    print("*** h4 = Exam Server")
    print("*** s1 = SDN Switch\n")

    CLI(net)

    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
