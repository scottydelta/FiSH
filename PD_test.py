#!/usr/bin/env python2

from LPDoL.multicast import Inducter
from LPDoL.handler import MessageHandler
from LPDoL.common import Peer
from uuid import uuid1
from twisted.internet import reactor
class PeerContainer(list):
	def __init__(self, onAdd, onDel):
		super(PeerContainer, self).__init__()
		self.aT=onAdd
		self.dT=onDel

	def add(self, peer_obj):
		flag=True
		for item in self:
			if item.addr == peer_obj.addr:
				self.remove(item)
				flag=False
		self.append(peer_obj)
		if flag:
			reactor.callInThread(self.aT, self)

	def discard(self, peer_obj):	
		for item in self:
			if item.addr == peer_obj.addr:
				self.remove(item)
				reactor.callInThread(self.dT, self)

def refAdd(peer_list):
	print peer_list

def refDel(peer_list):
	print peer_list

if __name__ == '__main__':
	p=Peer(uid=uuid1().hex, name='anon',addr='127.0.0.1')
	p_l=PeerContainer(refAdd, refDel)
	i=Inducter(('224.0.2.38',8999))
	reactor.listenMulticast(8999,i)
	h=MessageHandler(p, i.broadcast, p_l)
	i.addHandler(h.handle)
	reactor.run()
