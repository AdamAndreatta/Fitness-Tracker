import time
import json
import zmq

context = zmq.Context()
rep_socket = context.socket(zmq.REP)
rep_socket.bind('tcp://*:5555')

message1 = rep_socket.recv_string()
data = json.loads(message1)
vals = list(data.values())
keys = list(data.keys())

key = keys[0]
amount = vals[0]

if key == "kgs":
    amount = amount * .453592
    converted = str(amount)
    rep_socket.send_string(converted)

elif key == "lbs":
    amount = amount * 2.20462
    converted = str(amount)
    rep_socket.send_string(converted)
