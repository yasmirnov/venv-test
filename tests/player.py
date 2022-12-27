class Player:
    def __int__(self, name, points):
        self.name = name
        self.points = 0

    def change_name(self, new_name):
        self.name = new_name

    def add_points(self, number):
        self.points += number

    def get_points(self):
        return self.points



