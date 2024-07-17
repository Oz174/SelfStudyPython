class QueryTemplate:
    def connect(self):
        pass
    def construct_query(self):
        pass
    def do_query(self):
        pass
    def parse_results(self):
        pass
    def output_results(self):
        pass
    def process_query(self):
        self.connect()
        self.construct_query()
        self.do_query()
        self.parse_results()
        self.output_results()
class NewUserQuery(QueryTemplate):
    def construct_query(self):
        self.query = "select * from Users where new='true'"