from elastalert.ruletypes import RuleType
import re

class ArisanRule(RuleType):
	def match_regex(self, pattern, message):
		return bool(re.search(pattern, message))
	
	def process_line(self, line):
		line_split = line.split(":")
		key = line_split[0].strip()
		key = key.replace("/",r"\/")
		key = ".*"+key+".*"
		value = line_split[1].strip()
		return key, value

	def load_paths(self, name):
		f = open("modules/pattern/"+name,"r")
		lines = f.readlines()
		paths = {}
		for line in lines:
			key, value = self.process_line(line)
			paths[key] = value
		return paths
		
	def get_source(self, message, document):
		pattern = r"GET.*=|POST.*="
		if "web" in document['_index']:
			pattern = r"GET.*HTTP|POST.*HTTP"
			
		path = re.findall(r"GET.*=|POST.*=",message)[0]
		path = path.split(" ")[1]
		document['path'] = path
		
		name = document['_index'].split("-")[1]
		paths = self.load_paths(name)
		for pattern in paths:
			if self.match_regex(pattern, message):
				return paths[pattern]
		
		# if source pattern doesn't exists return path
		return path
            
	def add_data(self, data):
		for document in data:
			message = document['message']
			print("Message: "+message)
			error_pattern = r"HTTP[\/1-9\.\"]+\s20."

			if self.match_regex(error_pattern, message):
				document['target'] = self.get_source(message,document)
				document['error_code'] = re.findall(error_pattern,message)[0]
				self.add_match(document)

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