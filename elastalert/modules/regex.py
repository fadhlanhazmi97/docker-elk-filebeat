from elastalert.ruletypes import RuleType
import re

class RegexRule(RuleType):
        def add_data(self, data):
                for document in data:
                        message = document['message']
                        if bool(re.search(".*arisan.*",message)):
                            document['target'] = "arisan" 
                        error_pattern = ".*HTTP.{5}50.*"
                        match = bool(re.search(error_pattern,message)) 
                        if match:
                                self.add_match(document)

        def get_match_str(self, match):
                return "there is an error at: "+ match['target']
