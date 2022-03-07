def init():
    global valuesDict
    valuesDict = {
        "speed": 0,
        "hv_voltage": 0,
        "hv_charge_percent": 0,
        "hv_avg_temp": 0,
        "hv_max_temp": 0,
        "hv_min_temp": 0,
        'lv_voltage': 0,
        "lv_charge_percent": 0,
        "lv_avg_temp": 0,
        "lv_max_temp": 0,
        "lv_min_temp": 0,
        "engine_mode": 0
    }
    global canDict
    canDict = {
        "0x1":0 #speed
    }
    global DV_MISSIONS
    DV_MISSIONS = [
        "ACCELERETION",
        "SKIDPAD",
        "EBS TEST",
        "INSPECTION",
        "MANUAL DRIVING"
    ]

