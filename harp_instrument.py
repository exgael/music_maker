import numpy as np
from scipy import signal

class Harp:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.resonance_factor = 0.99
        self.decay_factor = 0.9997

    def generate_wave(self, frequency, duration, amplitude):
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)
        
        # Generate the main tone with overtones
        wave = amplitude * np.sin(2 * np.pi * frequency * t)
        wave += 0.5 * amplitude * np.sin(2 * np.pi * frequency * 2 * t)
        wave += 0.25 * amplitude * np.sin(2 * np.pi * frequency * 3 * t)
        wave += 0.125 * amplitude * np.sin(2 * np.pi * frequency * 4 * t)
        
        # Apply a soft attack
        attack_time = 0.01
        attack_samples = int(attack_time * self.sample_rate)
        attack_envelope = np.linspace(0, 1, attack_samples)**2
        wave[:attack_samples] *= attack_envelope
        
        # Apply resonance and decay
        for i in range(1, len(wave)):
            wave[i] += wave[i-1] * self.resonance_factor
            wave[i] *= self.decay_factor
        
        return wave

    def generate_phrase(self, frequencies, durations, amplitudes):
        waves = []
        for freq, dur, amp in zip(frequencies, durations, amplitudes):
            waves.append(self.generate_wave(freq, dur, amp))
        
        # Ensure smooth transition between notes
        crossfade_duration = 0.05  # 50ms crossfade
        crossfade_samples = int(crossfade_duration * self.sample_rate)
        
        full_wave = waves[0]
        for i in range(1, len(waves)):
            if len(full_wave) < crossfade_samples:
                full_wave = np.concatenate([full_wave, waves[i]])
            else:
                fade_out = np.linspace(1, 0, crossfade_samples)**2
                fade_in = np.linspace(0, 1, crossfade_samples)**2
                full_wave[-crossfade_samples:] *= fade_out
                waves[i][:crossfade_samples] *= fade_in
                full_wave = np.concatenate([full_wave[:-crossfade_samples], 
                                            full_wave[-crossfade_samples:] + waves[i][:crossfade_samples], 
                                            waves[i][crossfade_samples:]])
        
        return full_wave