class Card():
    def __init__(self, group, suites, color):
        self.group = group
        self.suites = suites
        self.color = color

    def print_card(self):
        print(f"{self.group} {self.suites} {self.color}")
    
      