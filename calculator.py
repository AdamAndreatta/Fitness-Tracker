import zmq
import json

context = zmq.Context()
rep_socket = context.socket(zmq.REP)
rep_socket.bind('tcp://*:5555')

message = rep_socket.recv_string()

if message == "add":
    calories = 0

    f = open('Tracker.json')
    items = json.load(f)
    f.close()

    for item in items:
        calories += items[item][0]

    total = str(calories)
    rep_socket.send_string(total)


