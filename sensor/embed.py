"""
Python module, to program a WiPy embedded device as a networked moisture sensor
"""
from machine import Timer

import usocket

listener_ip = "192.168.1.3"
listener_port = 8000
# Verify the WiPy has an interface which can connect to listener
listener_addr_info = usocket.getaddrinfo(listener_ip, listener_port)
listener_addr = listener_addr_info[0][4]
# tuple, representing a verified pair of listener IPv4 address & TCP port

def alert():
    """
    Alert the remove server of a moisture event!
    """ 
    # Connect to the remote listener
    ipv4_socket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
    ipv4_socket.connect(listener_addr)
    # Notify
    msg = "SomeMoistureWasFound!"
    bytes_type = 'ascii'
    msg_bytes = bytes('GET /{}'.format(msg), bytes_type)
    ipv4_socket.sendall(msg_bytes)
    ipv4_socket.close()

def alert_handler(timer):
    """
    demonstrate alert works via WiPy timers
    """
    global led
    alert() #FIXME: timer fails to call, due to inability to allocate objects (socket)?
    led.toggle()

tim = Timer(1, mode=Timer.PERIODIC, width=32)
tim_a = tim.channel(Timer.A | Timer.B, freq=2)
#FIXME: irq call below does trigger a blink, but does not seem to trigger an alert
tim_a.irq(handler=alert_handler) #, trigger=Timer.PERIODIC)

