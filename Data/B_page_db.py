class Database():
    def __init__(self):
        self.counter = 0
        self.current_user = None
        self.users = {"admin":"pass",
                      "Isak":"Elev",
                      "Odin":"Elev1",
                      "Lucian":"Hej-nej-new-now"}
        self.current_page = None
        self.naviList = [
            "test1",
            "test2",
            "test3",
            
        ]
       