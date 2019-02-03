class Game:

    def __init__(self, name, category, device):
        self._name = name
        self._category = category
        self._device = device

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @property
    def device(self):
        return self._device