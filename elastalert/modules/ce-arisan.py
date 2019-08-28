from elastalert.ruletypes import RuleType
import re

class CEArisanRule(RuleType):
	def match_regex(self, pattern, message):
		return bool(re.search(pattern, message))
		
	def get_source(self, document):
		self.paths = {
            r".*\/products.*": "ce-products",
            r".*\/arisan.*": "ce-arisan",
            r".*\/agent\/platform.*": "mps",
            r".*\/location.*": "location",
            r".*\/logistic.*": "logistic",
            r".*\/order.*": "ce-ordering",
            r".*\/agent.*": "GK"
        }
		
		url_path = document['url_path']
		
		for pattern in self.paths:
			if self.match_regex(pattern, url_path):
				return self.paths[pattern]
		
		# if source pattern doesn't exists return path
		return url_path
            
	def add_data(self, data):
		for document in data:
			try:
				status = document['status']
				error_pattern = r"40*|50*|200"

				if self.match_regex(error_pattern, status):
					document['target'] = self.get_source(document)
					document['error_code'] = re.findall(error_pattern,status)[0]
					self.add_match(document)
			except:
				print("Log format unsupported")

	def get_match_str(self, match):
		match_str = "The source of the error is at: "+ match['target']+"\n"
		match_str += "API Path: "+ match['url_path']+"\n"
		match_str += "Error detected in: "+match['app']+"\n"
		match_str += "Error HTTP code: "+match['error_code'][-3:]
		return match_str