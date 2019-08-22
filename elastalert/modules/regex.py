from elastalert.ruletypes import RuleType
import re

class RegexRule(RuleType):
        def match_regex(self, pattern, message):
                return bool(re.search(pattern, message))

        def get_path(self, message):
                self.paths = {
                        ".*products.*": "ce-products",
                        ".*arisan.*": "ce-arisan",
                        ".*agent\/platform.*": "mps",
                        ".*location.*": "location",
                        ".*logistic.*": "logistic",
                        ".*order.*": "ce-ordering",
                        ".*agent.*": "GK"
                }

                for pattern in self.paths:
                        if self.match_regex(pattern, message):
                                return self.paths[pattern]
                
                
        def add_data(self, data):
                for document in data:
                        message = document['message']
                        error_pattern = ".*HTTP.{5}50.*"
                        if self.match_regex(error_pattern, message):
                                document['target'] = self.get_path(message)
                                self.add_match(document)

        def get_match_str(self, match):
                return "there is an error at: "+ match['target']