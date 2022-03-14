#will run on computer


import numpy as np
import csv
import sys
import time
import math
import datetime
import os
import paho.mqtt.client as mqtt
import time,logging


															#ALL PRINT STATMENTS ARE STILL IN THIS CODE

ans = ''
count = 0

def on_connect(client, userdata, flags, rc):
  print('connected')
  client.subscribe("ece180d/IMU2", qos=1)

def on_message(client, userdata, message):
	global ans
	message_string = str(message.payload.decode("utf-8"))  #changes input from bytes to string and cleans up for reading into array
	disallowed_characters = "'"
	for character in disallowed_characters:
		message_string = message_string.replace(character, "") #removes characters from the payload before converting to array
	disallowed_characters = '"'
	for character in disallowed_characters:
		message_string = message_string.replace(character, "")
	disallowed_characters = '['
	for character in disallowed_characters:
		message_string = message_string.replace(character, "")
	disallowed_characters = ']'
	for character in disallowed_characters:
		message_string = message_string.replace(character, "")
	disallowed_characters = '('
	for character in disallowed_characters:
		message_string = message_string.replace(character, "")
	disallowed_characters = ')'
	for character in disallowed_characters:
		message_string = message_string.replace(character, "")
	disallowed_characters = ' '
	for character in disallowed_characters:
		message_string = message_string.replace(character, "")
	ans = message_string

	print('returned ' + ans)
	global count
	count = 1


def main():

	global count
	count = 0

	client = mqtt.Client('firstclient')
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect_async('test.mosquitto.org')
	client.loop_start()

	print('running')

	client.publish('ece180d/IMU', 'begin', qos=1)

	while count != 1:
		pass

	client.loop_stop()
	client.disconnect()

	print(ans)
	return ans
	

main()



