class Wizard:

    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __repr__(self):
        return repr((self.name, self.house))
