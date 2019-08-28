from elastalert.ruletypes import RuleType
import re

class ArisanRule(RuleType):
	def match_regex(self, pattern, message):
		return bool(re.search(pattern, message))
		
	def get_source(self, message, document):
		self.paths = {
            r".*\/products.*": "ce-products",
            r".*\/arisan.*": "ce-arisan",
            r".*\/agent\/platform.*": "mps",
            r".*\/location.*": "location",
            r".*\/logistic.*": "logistic",
            r".*\/order.*": "ce-ordering",
            r".*\/agent.*": "GK"
        }

		pattern = r"GET.*=|POST.*="
		if "web" in document['_index']:
			pattern = r"GET.*HTTP|POST.*HTTP"
			
		path = re.findall(r"GET.*=|POST.*=",message)[0]
		document['path'] = path.split(" ")[1]
		
		for pattern in self.paths:
			if self.match_regex(pattern, message):
				return self.paths[pattern]
		
		# if source pattern doesn't exists return path
		return path
            
	def add_data(self, data):
		for document in data:
			message = document['message']
			error_pattern = r"HTTP[\/1-9\.\"]+\s50."

			if self.match_regex(error_pattern, message):
				document['target'] = self.get_source(message,document)
				document['error_code'] = re.findall(error_pattern,message)[0]
				self.add_match(document)

	def get_match_str(self, match):
		match_str = "The source of the error is at: "+ match['target']+"\n"
		match_str += "API Path: "+ match['path']+"\n"
		match_str += "Error detected in: "+match['host']['name']+"\n"
		match_str += "Error HTTP code: "+match['error_code'][-3:]
		return match_str