class Game:

    def __init__(self, name, category, device, id=None):
        self._id = id
        self._name = name
        self._category = category
        self._device = device

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category

    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, device):
        self._device = device