import values

def handle_messsage(msg):
   #message will be in form: ID:VALUE
   if ":" in msg:
    id_val = msg.split(':')
    update_value(id_val[0], float(id_val[1]))
   
def update_value(id, value):
    values.valuesDict[id] = value
