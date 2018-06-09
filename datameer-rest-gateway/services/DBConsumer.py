class DBConsumer:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def read_config(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

    def connect_db(self):               # Abstract method, defined by convention only
            raise NotImplementedError("Subclass must implement abstract method")

    def execute_query(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")