import numpy as np
from scipy import signal

class Kalimba:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.resonance_factor = 0.99
        self.decay_factor = 0.9995

    def generate_wave(self, frequency, duration, amplitude):
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)
        
        # Generate the main tone
        wave = amplitude * np.sin(2 * np.pi * frequency * t)
        
        # Add overtones
        wave += 0.5 * amplitude * np.sin(2 * np.pi * frequency * 2 * t)
        wave += 0.25 * amplitude * np.sin(2 * np.pi * frequency * 3 * t)
        
        # Simulate the "pluck" of the kalimba tine
        pluck = np.random.rand(100) * 2 - 1
        pluck = np.pad(pluck, (0, len(wave) - len(pluck)), 'constant')
        wave += pluck * amplitude
        
        # Apply resonance and decay
        for i in range(1, len(wave)):
            wave[i] += wave[i-1] * self.resonance_factor
            wave[i] *= self.decay_factor
        
        return wave

    def generate_phrase(self, frequencies, durations, amplitudes):
        waves = [self.generate_wave(freq, dur, amp) for freq, dur, amp in zip(frequencies, durations, amplitudes)]
        return np.concatenate(waves)