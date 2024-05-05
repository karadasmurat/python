# be careful with imports - Wizard class is defined in a module with the same name: Wizard.py
class Wizard:

    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __repr__(self):
        return repr((self.name, self.house))
