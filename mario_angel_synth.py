import numpy as np
from scipy import signal

class MarioAngelSynth:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

    def generate_wave(self, frequency, duration, amplitude):
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)
        
        # Base sine wave
        wave = amplitude * np.sin(2 * np.pi * frequency * t)
        
        # Add harmonics for richness
        wave += 0.3 * amplitude * np.sin(4 * np.pi * frequency * t)
        wave += 0.2 * amplitude * np.sin(6 * np.pi * frequency * t)
        
        # Add a bit of 'square' feel for that Mario flavor
        wave += 0.1 * amplitude * signal.square(2 * np.pi * frequency * t)
        
        # Soft attack and release
        attack_time, release_time = 0.05, 0.1
        attack_samples = int(attack_time * self.sample_rate)
        release_samples = int(release_time * self.sample_rate)
        
        attack = np.linspace(0, 1, attack_samples)**2
        release = np.linspace(1, 0, release_samples)**2
        
        wave[:attack_samples] *= attack
        wave[-release_samples:] *= release
        
        return wave

    def generate_chord(self, frequencies, duration, amplitude):
        chord = np.zeros(int(self.sample_rate * duration))
        for freq in frequencies:
            chord += self.generate_wave(freq, duration, amplitude / len(frequencies))
        return chord

    def generate_arpeggio(self, frequencies, duration, amplitude):
        arpeggio = np.zeros(int(self.sample_rate * duration))
        single_note_duration = duration / len(frequencies)
        for i, freq in enumerate(frequencies):
            start = int(i * single_note_duration * self.sample_rate)
            end = int((i + 1) * single_note_duration * self.sample_rate)
            arpeggio[start:end] += self.generate_wave(freq, single_note_duration, amplitude)
        return arpeggio