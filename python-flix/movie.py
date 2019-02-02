from program import Program


class Movie(Program):

    def __init__(self, name, year, runtime):
        super().__init__(name, year)
        self.runtime = runtime

    def __str__(self):
        return f'{self._name} - {self.year} - {self.runtime} min : {self.likes} likes'
