from abc import ABC, abstractmethod


class Player(ABC):
    _nickname = ""

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def player_info(self):
        pass
