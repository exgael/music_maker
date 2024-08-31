import numpy as np
from scipy import signal
from instrument import Instrument

class Piano(Instrument):
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.pedal_pressed = False
        self.sustained_notes = {}
        self.reverb_buffer = np.zeros(int(2 * self.sample_rate))  # 2 seconds of reverb

    def generate_wave(self, frequency, duration, amplitude):
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)
        
        # Generate a rich piano tone with multiple harmonics
        harmonics = [1, 2, 3, 4, 5, 6, 7, 8]
        harmonic_weights = [1, 0.7, 0.5, 0.3, 0.2, 0.1, 0.05, 0.02]
        wave = np.zeros_like(t)
        for harmonic, weight in zip(harmonics, harmonic_weights):
            wave += weight * np.sin(2 * np.pi * frequency * harmonic * t)
        
        # Simulate the non-linear response of a piano hammer
        wave = np.tanh(wave * 2) * 0.5
        
        # Apply ADSR envelope
        attack_time, decay_time, sustain_level, release_time = 0.002, 0.1, 0.7, 0.3
        total_samples = len(wave)
        attack_samples = int(attack_time * self.sample_rate)
        decay_samples = int(decay_time * self.sample_rate)
        release_samples = int(release_time * self.sample_rate)
        sustain_samples = max(0, total_samples - attack_samples - decay_samples - release_samples)
        
        envelope = np.zeros(total_samples)
        
        # Attack
        envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
        
        # Decay
        decay_end = attack_samples + decay_samples
        envelope[attack_samples:decay_end] = np.linspace(1, sustain_level, decay_samples)
        
        # Sustain
        envelope[decay_end:decay_end + sustain_samples] = sustain_level
        
        # Release
        envelope[decay_end + sustain_samples:] = np.linspace(sustain_level, 0, total_samples - (decay_end + sustain_samples))
        
        # Apply envelope and amplitude
        wave = wave * envelope * amplitude
        
        # Apply pedal effect if pressed
        if self.pedal_pressed:
            wave = self.apply_pedal(wave)
        
        # Apply reverb
        wave = self.apply_reverb(wave)
        
        return wave

    def apply_pedal(self, wave):
        decay = 0.99 if self.pedal_pressed else 0.9
        self.sustained_notes = {note: self.sustained_notes[note] * decay for note in self.sustained_notes}
        sustained_wave = sum(self.sustained_notes.values())
        return wave + sustained_wave

    def apply_reverb(self, wave):
        reverb = np.convolve(wave, self.reverb_buffer)[:len(wave)]
        return 0.7 * wave + 0.3 * reverb

    def press_pedal(self):
        self.pedal_pressed = True

    def release_pedal(self):
        self.pedal_pressed = False

    def generate_phrase(self, frequencies, durations, amplitudes):
        waves = []
        for freq, duration, amplitude in zip(frequencies, durations, amplitudes):
            wave = self.generate_wave(freq, duration, amplitude)
            waves.append(wave)
            if self.pedal_pressed:
                self.sustained_notes[freq] = wave
        
        # Crossfade between notes
        crossfade_duration = 0.01  # 10ms crossfade
        crossfade_samples = int(crossfade_duration * self.sample_rate)
        
        full_wave = waves[0]
        for i in range(1, len(waves)):
            full_wave = self.crossfade(full_wave, waves[i], crossfade_samples)
        
        return full_wave

    def crossfade(self, wave1, wave2, crossfade_length):
        fade_out = np.linspace(1, 0, crossfade_length)**2
        fade_in = np.linspace(0, 1, crossfade_length)**2
        wave1[-crossfade_length:] *= fade_out
        wave2[:crossfade_length] *= fade_in
        return np.concatenate([wave1[:-crossfade_length], wave1[-crossfade_length:] + wave2[:crossfade_length], wave2[crossfade_length:]])