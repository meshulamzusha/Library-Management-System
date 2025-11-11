class Library:

    def __init__(self, data_file="data.json"):
        self.books = {}
        self.users = {}
        self.data_file = data_file
        self.load_data()
