class Program:

    def __init__(self, name, year):
        self._name = name
        self.year = year
        self._likes = 0

    @property
    def name(self,name):
        self._name = name.title()

    @property
    def likes(self):
        return self._likes

    def give_like(self):
        self._likes += 1

    # @classmethod
    # def info(cls):
    #   pass

    # @staticmethod
    # def info():
    #   pass