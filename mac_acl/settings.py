from decouple import config

AP = {
    "user": config("AP_USER"),
    "password": config("AP_PASSWORD")
}

AP_HOSTS = {

    "02.01":{
        "device": "mikrotik",
        "ip": "192.168.7.2"
    },
    "02.02": {
        "device": "mikrotik",
        "ip": "192.168.7.3"
    },
    "02.03":{
        "device": "mikrotik",
        "ip": "192.168.7.4"
    },
    "02.04":{
        "device": "mikrotik",
        "ip": "192.168.7.7"
    },
    "02.05": {
        "device": "ubiquiti",
        "ip":"192.168.7.10"
    },

    #MORON

    "05.02": {
        "device": "ubiquiti",
        "ip": "10.10.3.74"
    },
    "05.03": {
        "device": "mikrotik",
        "ip": "10.10.3.90"
    },
    "05.05": {
        "device": "mikrotik",
        "ip":"10.10.3.4",
    },
    "05.06": {
        "device": "ubiquiti",
        "ip": "10.10.3.3"
    },
    "05.08":{
        "device": "ubiquiti",
        "ip": "192.168.88.44",
    },
    "05.09": {
        "device": "mikrotik",
        "ip": "10.10.3.2"
    },
    "05.10": {
        "device": "ubiquiti",
        "ip": "10.10.3.5"
    },

    #Tabuyo

    "12.01": {
        "device":"ubiquiti",
        "ip":"10.10.2.2"
    },
    "12.02": {
        "device":"mikrotik",
        "ip":"10.10.2.10"
    },
    "12.03": {
        "device":"ubiquiti",
        "ip":"10.10.2.5"
    },
    "12.06": {
        "device":"mikrotik",
        "ip":"10.10.2.26"
    },

    #Blandon
    

    "13.01": {
        "device": "ubiquiti",
        "ip": "10.10.11.2"
    },
    "13.02": {
        "device": "ubiquiti",
        "ip": "10.10.11.18"
    },
    "13.03": {
        "device": "ubiquiti",
        "ip": "10.10.11.34"
    },
    "13.04": {
        "device": "ubiquiti",
        "ip": "10.10.11.26"
    },

    #Iberia

    "11.01":{
        "device":"ubiquiti",
        "ip": "10.10.9.2"
    },
    "11.02":{
        "device":"ubiquiti",
        "ip": "10.10.9.10"
    },
    "11.03":{
        "device":"mikrotik",
        "ip": "10.10.9.18"
    },
    "11.04":{
        "device":"mikrotik",
        "ip": "10.10.9.26"
    },
    "11.05":{
        "device":"ubiquiti",
        "ip": "10.10.9.3"
    },

    #Guamal

    "14.01": {
        "device": "mikrotik",
        "ip": "10.10.7.18"
    },
    "14.02": {
        "device": "mikrotik",
        "ip": "10.10.7.10"
    },
    "14.03": {
        "device": "mikrotik",
        "ip": "10.10.7.2"
    },
    "14.04": {
        "device": "mikrotik",
        "ip": "10.10.7.3"
    },

    #Cabuyal

    "11.06": {
        "device": "mikrotik",
        "ip": "10.10.16.2"
    },
    "11.07": {
        "device": "mikrotik",
        "ip": "10.10.16.10"
    },
    "11.08": {
        "device": "mikrotik",
        "ip": "10.10.16.18"
    },

    #Roble

    "05.11": {
        "device": "ubiquiti",
        "ip": "10.10.3.7"
    },

    #Irra

    "15.01": {
        "device":"mikrotik",
        "ip": "10.10.15.2"
    },
    "15.02": {
        "device":"ubiquiti",
        "ip": "10.10.15.10"
    },
    "15.03": {
        "device":"ubiquiti",
        "ip": "10.10.15.18"
    },
    "15.04": {
        "device":"mikrotik",
        "ip": "10.10.15.26"
    },

    #Pulgarin

    "14.05":{
        "device": "mikrotik",
        "ip": "10.10.7.37"
    },
    "14.06  ":{
        "device": "mikrotik",
        "ip": "10.10.7.38"
    },

    #Honduras
    
    "05.04": {
        "device": "ubiquiti",
        "ip": "10.10.3.9"
    },

    #Bonafont

    "09.01": {
        "device": "ubiquiti",
        "ip": "10.10.8.18"
    },
    "09.02": {
        "device": "ubiquiti",
        "ip": "10.10.8.19"
    },
    "09.03": {
        "device": "mikrotik",
        "ip": "10.10.8.20"
    },

    #PV

    "03.01": {
        "device": "mikrotik",
        "ip": "10.10.17.2"
    },
    "03.02": {
        "device": "mikrotik",
        "ip": "10.10.17.10"
    },

    #La Sierra

    "04.01": {
        "device": "ubiquiti",
        "ip": ""
    },
    "04.01": {
        "device": "ubiquiti",
        "ip": ""
    },
    "04.01": {
        "device": "ubiquiti",
        "ip": ""
    },
    "04.01": {
        "device": "ubiquiti",
        "ip": ""
    },

    #Las Cruces

    "07.01": {
        "device": "ubiquiti",
        "ip": "192.168.9.2"
    },
    "07.03": {
        "device": "mikrotik",
        "ip": "192.168.9.4"
    }
}