from values import *

def handle_messsage(msg):
   #message will be in form: ID:VALUE
   id_val = msg.split(':')
   update_value(id_val[0], int(id_val[1]))
   
def update_value(id, value):
   #exec("%s = %d" % (id, value))
   if(id == "speed"):
      global speed
      speed = value

      
