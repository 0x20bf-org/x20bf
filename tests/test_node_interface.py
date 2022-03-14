#######################################################################################################################
# Author: Maurice Snoeren                                                                                             #
# Version: 0.1 beta (use at your own risk)                                                                            #
#                                                                                                                     #
# This example show how to derive a own Node class (MyOwnPeer2PeerNode) from p2pnet.Node to implement your own Node   #
# implementation. See the MyOwnPeer2PeerNode.py for all the details. In that class all your own application specific  #
# details are coded.                                                                                                  #
#######################################################################################################################

import sys
import time

sys.path.insert(0, "..")  # Import the files where the modules are located

# from node_interface import NodeInterface
# import NodeInterface

from x20bf import node_interface as node
# node = node_interface
# node = __import__("0x20bf", globals(), locals(), ['NodeInterface'], 0)
# node = __import__("0x20bf", globals(), locals(), ['node_interface'], 0)
# node = __import__("0x20bf", globals(), locals(), ['node_interface'], 0)

# node_1 = node.node_interface.NodeInterface("127.0.0.1", 8001)
node_1 = node.NodeInterface("127.0.0.1", 8001)
node_2 = node.NodeInterface("127.0.0.1", 8002)
node_3 = node.NodeInterface("127.0.0.1", 8003)

time.sleep(1)

node_1.start()
node_2.start()
node_3.start()

time.sleep(1)

node_1.connect_with_node("127.0.0.1", 8002)
node_2.connect_with_node("127.0.0.1", 8003)
node_3.connect_with_node("127.0.0.1", 8001)

time.sleep(2)

node_1.send_to_nodes({"name": "Maurice", "number": 11})

time.sleep(5)

node_1.stop()
node_2.stop()
node_3.stop()
print("end test")
