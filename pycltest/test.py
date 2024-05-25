
TEST_OK  = "OK"
TEST_ERR = "ERR"

class Test:
    location: str
    name:     str

    def __init__(self, location: str, name: str):
        self.location = location
        self.name     = name
