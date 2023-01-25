import pyrebase

config = {
  "apiKey": "AIzaSyAhFVhA_2kt5POoeH4CbSrvAU1GtB_3gM0",
  "authDomain": "final-smart-farm.firebaseapp.com",
  "databaseURL": "https://final-smart-farm-default-rtdb.firebaseio.com",
  "projectId": "final-smart-farm",
  "storageBucket": "final-smart-farm.appspot.com",
  "messagingSenderId": "700173485436",
  "appId": "1:700173485436:web:71ebbba30f4b9811c250f9",
  "serviceAccount": "/home/dongpakka/workspace/opencv/ServiceAccount.json",
  "databaseURL" : "https://final-smart-farm-default-rtdb.firebaseio.com/",
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db=firebase.database()

############################## IMAGE ##############################
# send
def sendImage(file,name):
  # storage.child("server.jpg").put("local.jpg")
  storage.child(name).put(file)

# get
def getImage():
  storage.download("server.jpg", "local_new.jpg")



############################## MQTT DATA ##############################
# temp data
# id = "dongpakka"

# hum = input("humidity : ")
# ill = input("illu : ")
# temper = input("temperature : ")

# send
def sendMqttData(id, hum, ill, temper):
  data = {
    "humidity":hum,
    "illu":ill,
    "temperature":temper,
  }
  db.child(id).set(data)

# get



