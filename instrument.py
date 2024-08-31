from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def generate_wave(self, frequency, duration, amplitude):
        pass
