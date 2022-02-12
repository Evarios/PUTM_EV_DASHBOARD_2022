import values

def handle_messsage(msg):
   #message will be in form: ID:VALUE
   if ":" in msg:
    id_val = msg.split(':')
    update_value(id_val[0], float(id_val[1]))
   
def update_value(id, value):
   #exec("%s = %d" % (id, value))
    if id == "speed":
        values.speed = int(value)
    #hv values
    elif id == "hv_voltage":
        values.hv_voltage = value
    elif id == "hv_charge_percent":
        values.hv_charge_percent = int(value)
    elif id == "hv_avg_temp":
        values.hv_avg_temp = value
    elif id == "hv_max_temp":
        values.hv_max_temp = value              
    elif id == "hv_min_temp":
        values.hv_min_temp = value
    #lv values
    elif id == "lv_voltage":
        values.lv_voltage = value
    elif id == "lv_charge_percent":
        values.lv_charge_percent = int(value)
    elif id == "lv_avg_temp":
        values.lv_avg_temp = value
    elif id == "lv_max_temp":
        values.lv_max_temp = value              
    elif id == "lv_min_temp":
        values.lv_min_temp = value
    #engine mode
    elif id == "engine_mode":
        values.engine_mode = int(value)   
