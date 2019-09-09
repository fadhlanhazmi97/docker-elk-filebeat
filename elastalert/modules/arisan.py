from elastalert.ruletypes import RuleType
import re

class ArisanRule(RuleType):
	# Check if a regex pattern matches a string message
	def match_regex(self, pattern, message):
		return bool(re.search(pattern, message))
	
	# Function to convert the path into a regex
	def process_line(self, line):
		line_split = line.split(":")
		key = line_split[0].strip()
		key = key.replace("/",r"\/")
		key = ".*"+key+".*"
		value = line_split[1].strip()
		return key, value

	# Function to load file from path
	# The file location must be on modules/pattern
	# Relative to the root of the elastalert folder
	def load_paths(self, name):
		f = open("modules/pattern/"+name,"r")
		lines = f.readlines()
		paths = {}
		for line in lines:
			key, value = self.process_line(line)
			paths[key] = value

		# Return a dictionary of path as key
		# And source of error as value
		return paths

	# Function to get the source of the	error from the pattern
	def get_source(self, message, document):
		# Pattern of the path
		pattern = r"GET.*=|POST.*="
		
		# Getting the path from the log message
		path = re.findall(r"GET.*=|POST.*=",message)[0]
		path = path.split(" ")[1]
		document['path'] = path
		
		# Getting the name of the Middleware
		# i.e. viewlogic, viewmidware, trxlogic, trxmidware
		name = document['_index'].split("-")[1]

		# Load a dictionay contains the path as the key
		# And the source of error as value
		paths = self.load_paths(name)

		# Convert the path to source of error
		for pattern in paths:
			if self.match_regex(pattern, message):
				return paths[pattern]
		
		# if source pattern doesn't exists return path
		return path
            
	# Implemented function from the superclass (RuleType)
	# When the logs from elasticsearch is queried this function is called
	def add_data(self, data):
		# Data is list of the logs
		# Iterate through each logs
		for document in data:
			# The log is a dictionary that converted from JSON
			# If the log have a different structure it will throw an error
			# So it is why there is a try-except block here
			try:
				# Get the actual log from the dictionary
				# That is the "message"
				message = document['message']
				print("Message: "+message)

				# Define the error pattern from the log
				error_pattern = r"HTTP[\/1-9\.\"]+\s50."

				# Check if the log matches the error pattern
				if self.match_regex(error_pattern, message):
					# Add additional info the log to display on the alert
					document['target'] = self.get_source(message,document)
					document['error_code'] = re.findall(error_pattern,message)[0]

					# Add the log to the list of matches
					# So it will send an alert
					self.add_match(document)
			except:
				print("Log format unsupported, here is the log:\n\n"+str(document))

	# Implemented function from the superclass (RuleType)
	# When there is a match this function is called
	# Return a string to display in the alert body
	def get_match_str(self, match):
		try:
			match_str = "The possible source of the error is at: "+ match['target']+"\n"
			match_str += "API Path: "+ match['path']+"\n"
			match_str += "Error detected in: "+match['host']['name']+"\n"
			match_str += "Error HTTP code: "+match['error_code'][-3:]
			return match_str
		except:
			error_str = "Log format unsupported\n\n"
			error_str += "Here is the log:\n"
			error_str += str(match)
			return error_str