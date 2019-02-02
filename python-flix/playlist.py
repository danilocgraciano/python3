#from collections.abc import MutableSequence

#class PlayList(MutableSequence):
class PlayList:

    def __init__(self,name,programs):
        self.name = name
        self._programs = programs

    #Duck Typing
    def __getitem__(self, item):
        return  self._programs[item]

    #Duck Typing
    def __len__(self):
        return len(self._programs)

    @property
    def programs(self):
        return self._programs