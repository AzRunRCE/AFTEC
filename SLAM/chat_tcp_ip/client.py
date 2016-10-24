#/* ************************************************************************* */
#/*									                                          */
#/*                                            ______ _______ ______   _____  */
#/*  file.py                            /\    |  ____|__   __|  ____| / ____| */
#/*                                    /  \   | |__     | |  | |__   | |      */
#/*  By: quentin.martinez@aftec.org   / /\ \  |  __|    | |  |  __|  | |      */
#/*                          	     / ____ \ | |       | |  | |____ | |____  */
#/*  Created: 2015/28/09 11:44:22   /_/    \_\|_|       |_|  |______| \_____| */
#/*                                                                           */
#/* ************************************************************************* */
#!/usr/bin/env python3
import socket
from  threading import Thread
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

BUFFER = 1024
IP = '127.0.0.1'
PORT = 8888
class HandlerSignal():
    def __init__(self,b):
	    self.builder = b
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
    def onButtonPressed(self, button):
      en = self.builder.get_object("entry1")
      print(en.get_text())
class Handler:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("window.glade")
        builder.connect_signals(HandlerSignal(builder))
        window = builder.get_object("window1")
        window.show_all()

class listen(Thread):
	def __init__(self, s):
        	Thread.__init__(self)
        	self.socket = s
	def run(self):
		while(1):
			data =	self.socket.recv(BUFFER)
			print("SERVER:", data.decode())

if __name__ == "__main__":

   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    ThreadListen = listen(s)
    ThreadListen.start()
    Handler()
    Gtk.main()
    while(1):
	    MESSAGE = input("Message?")
	    s.send(MESSAGE.encode())
    s.close()



