import numpy as np
from scipy import signal
from instrument import Instrument

class Violin(Instrument):
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

    def generate_wave(self, frequency, duration, amplitude):
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)
        
        # Generate a richer violin tone with more harmonics
        harmonics = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        harmonic_weights = [1, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05]
        wave = np.zeros_like(t)
        for harmonic, weight in zip(harmonics, harmonic_weights):
            wave += weight * np.sin(2 * np.pi * frequency * harmonic * t)
        
        # Add subtle noise to simulate bow-string interaction
        bow_noise = np.random.normal(0, 0.01, len(t))
        wave += bow_noise
        
        # Apply a more realistic ADSR envelope
        attack_time, decay_time, sustain_level, release_time = 0.08, 0.1, 0.7, 0.3
        envelope = np.ones_like(t)
        attack_samples = int(attack_time * self.sample_rate)
        decay_samples = int(decay_time * self.sample_rate)
        release_samples = int(release_time * self.sample_rate)
        
        # Ensure we don't exceed the total number of samples
        total_samples = len(t)
        sustain_samples = total_samples - attack_samples - decay_samples - release_samples
        
        if sustain_samples < 0:
            # Adjust times if the note is too short
            total_time = duration
            attack_time = total_time * 0.1
            decay_time = total_time * 0.2
            release_time = total_time * 0.2
            sustain_time = total_time - attack_time - decay_time - release_time
            
            attack_samples = int(attack_time * self.sample_rate)
            decay_samples = int(decay_time * self.sample_rate)
            sustain_samples = int(sustain_time * self.sample_rate)
            release_samples = total_samples - attack_samples - decay_samples - sustain_samples
        
        envelope[:attack_samples] = np.linspace(0, 1, attack_samples)**2
        envelope[attack_samples:attack_samples+decay_samples] = np.linspace(1, sustain_level, decay_samples)
        envelope[attack_samples+decay_samples:-release_samples] = sustain_level
        envelope[-release_samples:] = np.linspace(sustain_level, 0, release_samples)**2
        
        # Add vibrato
        vibrato_frequency = 5.5
        vibrato_amplitude = 0.006
        vibrato = 1 + vibrato_amplitude * np.sin(2 * np.pi * vibrato_frequency * t)
        
        # Add subtle pitch drift
        pitch_drift = 1 + 0.001 * np.cumsum(np.random.normal(0, 0.0001, len(t)))
        
        # Combine all elements
        wave = wave * envelope * vibrato * pitch_drift * amplitude
        
        # Apply a resonant body filter to simulate the violin body
        b, a = signal.butter(2, [500 / (self.sample_rate / 2), 3000 / (self.sample_rate / 2)], btype='bandpass')
        wave = signal.lfilter(b, a, wave)
        
        return wave

    def generate_phrase(self, frequencies, durations, amplitudes):
        waves = [self.generate_wave(f, d, a) for f, d, a in zip(frequencies, durations, amplitudes)]
        return np.concatenate(waves)