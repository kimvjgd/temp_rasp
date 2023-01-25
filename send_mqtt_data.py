import config

id = "dongpakka"

hum = input("humidity : ")
ill = input("illu : ")
temper = input("temperature : ")

config.sendMqttData(id, hum, ill, temper)

