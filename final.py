#coding=UTF-8
# Copyright 2012 James McCauley
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Turns your complex OpenFlow switches into stupid hubs.
There are actually two hubs in here -- a reactive one and a proactive one.
"""

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr

log = core.getLogger()


# def _handle_ConnectionUp (event): # Essa função lida com os eventos de conexão de swithces, assim que os swithces se conectam na rede eles avisam ao controlador


def _handle_PacketIn (event):

  msg = of.ofp_flow_mod()
  # if (msg.match.dl_type == 0x800):
    
  #Definição dos eventos do switch 1
  if event.dpid == 1:
    print("Switch: " + str(event.dpid))
    # print("From Port: " + str(event.port))
    # print("From IP: " + str(event.srcip))
    # print("To IP: " + str(nw_dst))
      
    if event.parsed.find("ipv4").dstip == "10.10.1.101":
      print("print("To " + event.parsed.find(ipv4).dstip)1.101")
      msg.match.dl_type = 0x800    
      msg.match.nw_dst = event.parsed.find("ipv4").dstip
      msg.actions.append(of.ofp_action_output( port = 3 ))

    if event.parsed.find("ipv4").dstip == "10.10.1.102":
      print("To " + event.parsed.find(ipv4).dstip)
      msg.match.dl_type = 0x800    
      msg.match.nw_dst = event.parsed.find("ipv4").dstip
      msg.actions.append(of.ofp_action_output( port = 4 ))

    if event.parsed.find("ipv4").dstip == "10.10.1.103":
      print("To " + event.parsed.find(ipv4).dstip)
      msg.match.dl_type = 0x800    
      msg.match.nw_dst = event.parsed.find("ipv4").dstip
      msg.actions.append(of.ofp_action_output( port = 5 ))

    if event.parsed.find("ipv4").dstip == "10.10.2.101" or  event.parsed.find("ipv4").dstip == "10.10.2.102" or  event.parsed.find("ipv4").dstip == "10.10.2.103":
      print("To " + event.parsed.find(ipv4).dstip)
      msg.match.dl_type = 0x800 
      msg.match.nw_dst = event.parsed.find("ipv4").dstip
      msg.actions.append(of.ofp_action_output( port = 1))

    if event.parsed.find("ipv4").dstip == "10.10.3.101" or  event.parsed.find("ipv4").dstip == "10.10.3.102" or  event.parsed.find("ipv4").dstip == "10.10.3.103":
      print("To " + event.parsed.find(ipv4).dstip)
      msg.match.dl_type = 0x800 
      msg.match.nw_dst = event.parsed.find("ipv4").dstip
      msg.actions.append(of.ofp_action_output( port = 2))

  if event.dpid == 2:
    print("Switch: " + str(event.dpid))
      
    if event.parsed.find("ipv4").dstip == "10.10.2.101":
      print("To " + event.parsed.find(ipv4).dstip)
      msg.match.dl_type = 0x800    
      msg.match.nw_dst = event.parsed.find("ipv4").dstip
      msg.actions.append(of.ofp_action_output( port = 3 ))

    if event.parsed.find("ipv4").dstip == "10.10.2.102":
      print("To " + event.parsed.find(ipv4).dstip)
      msg.match.dl_type = 0x800    
      msg.match.nw_dst = event.parsed.find("ipv4").dstip
      msg.actions.append(of.ofp_action_output( port = 4 ))

    if event.parsed.find("ipv4").dstip == "10.10.2.103":
      print("To " + event.parsed.find(ipv4).dstip)
      msg.match.dl_type = 0x800    
      msg.match.nw_dst = event.parsed.find("ipv4").dstip
      msg.actions.append(of.ofp_action_output( port = 5 ))

    if event.parsed.find("ipv4").dstip == "10.10.1.101" or  event.parsed.find("ipv4").dstip == "10.10.1.102" or  event.parsed.find("ipv4").dstip == "10.10.1.103":
      print("To " + event.parsed.find(ipv4).dstip)
      msg.match.dl_type = 0x800 
      msg.match.nw_dst = event.parsed.find("ipv4").dstip
      msg.actions.append(of.ofp_action_output( port = 1))

    if event.parsed.find("ipv4").dstip == "10.10.3.101" or  event.parsed.find("ipv4").dstip == "10.10.3.102" or  event.parsed.find("ipv4").dstip == "10.10.3.103":
      print("To " + event.parsed.find(ipv4).dstip)
      msg.match.dl_type = 0x800 
      msg.match.nw_dst = event.parsed.find("ipv4").dstip
      msg.actions.append(of.ofp_action_output( port = 2))

  if event.dpid == 3:
    print("Switch: " + str(event.dpid))
      
    if event.parsed.find("ipv4").dstip == "10.10.3.101":
      print("To " + event.parsed.find(ipv4).dstip)
      msg.match.dl_type = 0x800    
      msg.match.nw_dst = event.parsed.find("ipv4").dstip
      msg.actions.append(of.ofp_action_output( port = 3 ))

    if event.parsed.find("ipv4").dstip == "10.10.3.102":
      print("To " + event.parsed.find(ipv4).dstip)
      msg.match.dl_type = 0x800    
      msg.match.nw_dst = event.parsed.find("ipv4").dstip
      msg.actions.append(of.ofp_action_output( port = 4 ))

    if event.parsed.find("ipv4").dstip == "10.10.3.103":
      print("To " + event.parsed.find(ipv4).dstip)
      msg.match.dl_type = 0x800    
      msg.match.nw_dst = event.parsed.find("ipv4").dstip
      msg.actions.append(of.ofp_action_output( port = 5 ))

    if event.parsed.find("ipv4").dstip == "10.10.2.101" or  event.parsed.find("ipv4").dstip == "10.10.2.102" or  event.parsed.find("ipv4").dstip == "10.10.2.103":
      print("To " + event.parsed.find(ipv4).dstip)
      msg.match.dl_type = 0x800 
      msg.match.nw_dst = event.parsed.find("ipv4").dstip
      msg.actions.append(of.ofp_action_output( port = 1))

    if event.parsed.find("ipv4").dstip == "10.10.1.101" or  event.parsed.find("ipv4").dstip == "10.10.1.102" or  event.parsed.find("ipv4").dstip == "10.10.1.103":
      print("To " + event.parsed.find(ipv4).dstip)
      msg.match.dl_type = 0x800 
      msg.match.nw_dst = event.parsed.find("ipv4").dstip
      msg.actions.append(of.ofp_action_output( port = 2))


    event.connection.send(msg)



      # if event.port == 3:
      #   msg.match.in_port = 3
      #   msg.actions.append(of.ofp_action_output(port = 4))
      #   print("To: 4")
      # elif event.port == 4:
      #   msg.match.in_port = 4
      #   msg.actions.append(of.ofp_action_output(port = 3))
      #   print("To: 3")
      # elif event.port == 5:
      #   msg.match.in_port = 5
      #   msg.actions.append(of.ofp_action_output(port = 2))
      #   print("To: 2")
      # elif event.port == 2:
      #   msg.match.in_port = 2
      #   msg.actions.append(of.ofp_action_output(port = 5))
      #   print("To: 5")

    #Definição dos eventos do switch 2
    # elif event.dpid == 3:
    #   print("Switch: " + str(event.dpid))
    #   print("From: " + str(event.port))
    #   if event.port == 2:
    #     msg.match.in_port = 2
    #     msg.actions.append(of.ofp_action_output(port = 4))
    #     print("To: 4")
    #   if event.port == 4:
    #     msg.match.in_port = 4
    #     msg.actions.append(of.ofp_action_output(port = 2))
    #     print("To: 2")

    #Definição dos eventos do switch 3
    # event.connection.send(msg)














  """
  Be a reactive hub by flooding every incoming packet
  """
  # msg = of.ofp_flow_mod() #Essa Função cria um pacote OpenFlow para setar uma regra em um switch.
  # if event.port == 1:
  #   msg.match.in_port = 1 # Aqui criamos uma regra que executará as devidas actions quando tiver um match com porta de entrada = 1.
  #   msg.actions.append(of.ofp_action_output(port = 2)) # Aqui criamos uma action para encaminhar para porta 2.
  #   #Desta forma estamos criando uma regra no switch que encaminhará todos os pacotes que chegaram pela porta 1 para porta 2.

  # elif event.port == 2:
  #   msg.match.in_port = 2 # Aqui criamos uma regra que executará as devidas actions quando tiver um match com porta de entrada = 2
  #   msg.actions.append(of.ofp_action_output(port = 1)) # Aqui criamos uma action para encaminhar para porta 1.
  #   #Desta forma estamos criando uma regra no switch que encaminhará todos os pacotes que chegaram pela porta 2 para porta 1.
  
  # event.connection.send(msg) # Aqui nós enviamos o pacote que seta a regra no switch para o switch que gerou o evento de packetIn.


  #Também podemos criar um evento de packetOut, que simplesmente encaminha um pacote pro switch, com uma ação pra ele tomar, sem instanciar uma regra no switch.
  #Abaixo temos um exemplo:
  
  # msg = of.ofp_packet_out() #cria o pacote de packetOut.
  # msg.data = event.ofp #coloca os mesmos dados do pacote original nesse pacote (do pacote que gerou o packet_in).
  # msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD)) # Cria a regra pra o switch fazer um FLOOD com esse pacote.



def launch (reactive = False):
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    # core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)