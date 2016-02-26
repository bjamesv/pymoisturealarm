"""
Python module, to program a WiPy embedded device as a networked moisture sensor
"""
from time import sleep

import usocket
from machine import Timer, ADC

listener_ip = "192.168.1.2"
listener_port = 8000
# Verify the WiPy has an interface which can connect to listener
listener_addr_info = usocket.getaddrinfo(listener_ip, listener_port)
listener_addr = listener_addr_info[0][4]
# tuple, representing a verified pair of listener IPv4 address & TCP port

#set up analog input - per: https://micropython.org/resources/docs/en/latest/wipy/wipy/quickref.html#adc-analog-to-digital-conversion
apin = ADC().channel(pin='GP2')

def alert():
    """
    Alert the remove server of a moisture event!
    """ 
    # Connect to the remote listener
    ipv4_socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
    ipv4_socket.connect(listener_addr)
    # Notify
    msg = "V:"+str(apin())
    bytes_type = 'ascii'
    msg_bytes = bytes('GET /{}'.format(msg), bytes_type)
    ipv4_socket.sendall(msg_bytes)
    ipv4_socket.close()

#alert implementation allocates objects, which wont work with irq callback
#instead, just alert via a 1sec delay Pythonic busy-loop
while True:
    alert()
    sleep(1) #no smaller time unit available
