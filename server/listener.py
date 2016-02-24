#/usr/bin/python2
from time import sleep
import BaseHTTPServer
import SocketServer

from pygame import mixer

# Set up audio output
mixer.init()

alarm_wav_path = 'maemo_amsn_ring.wav'

alarm = mixer.Sound(alarm_wav_path)
#pygame.mixer Sound, representing the moisture detected alert sound 

def alert():
    """
    Sound the audible alarm!
    """
    number_of_rings = 2
    delay_sec = 3
    for ring_count in range(number_of_rings):
        alarm.play()
        sleep( delay_sec)

class MoistureHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET( self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("FOO!")
        alert()

def listen():
    """
    Launch HTTP server
    """
    port = 8000
    handler = MoistureHandler
    httpd = SocketServer.TCPServer(("", port), handler)
    print "serving at port", port
    httpd.serve_forever()

if __name__ == "__main__":
    listen()
