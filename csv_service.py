import zmq
import json
import csv

context = zmq.Context()
rep_socket = context.socket(zmq.REP)
rep_socket.bind('tcp://*:5555')

message2 = rep_socket.recv_string()

if message2 == "convert":
    with open('Tracker.json') as json_file:
        jsondata = json.load(json_file)


    data_file = open('Trackeroutput.csv', 'w', newline='')
    csv_writer = csv.writer(data_file)

    calories = []
    for item in jsondata:
        calories.append(jsondata[item][0] * jsondata[item][1])

    count = 0
    for i in jsondata:
        if count == 0:
            header = jsondata.keys()
            csv_writer.writerow(header)
            csv_writer.writerow(calories)
            count += 1
    data_file.close()

    rep_socket.send_string("Your csv is completed.")
