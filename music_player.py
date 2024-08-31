import numpy as np
import simpleaudio as sa
from music_utils import NOTE_FREQUENCIES, CHORDS

class Note:
    def __init__(self, note, duration=0.5, amplitude=0.5):
        self.note = note
        self.frequency = NOTE_FREQUENCIES[note]
        self.duration = duration
        self.amplitude = amplitude

class Phrase:
    def __init__(self, notes):
        self.notes = notes

class MusicComposer:
    def __init__(self, instrument, sample_rate=44100):
        self.instrument = instrument
        self.sample_rate = sample_rate
        self.composition = []

    def add_note(self, note, duration=0.5, amplitude=0.5):
        self.composition.append(Note(note, duration, amplitude))
        return self

    def add_chord(self, chord_name, duration=0.5, amplitude=0.5):
        chord_notes = [Note(note, duration, amplitude) for note in CHORDS[chord_name]]
        self.composition.append(Phrase(chord_notes))
        return self

    def add_phrase(self, notes, durations, amplitudes):
        phrase_notes = [Note(note, duration, amplitude) 
                        for note, duration, amplitude in zip(notes, durations, amplitudes)]
        self.composition.append(Phrase(phrase_notes))
        return self

    def generate_composition(self):
        full_wave = np.array([])
        
        for item in self.composition:
            if isinstance(item, Note):
                wave = self.instrument.generate_wave(item.frequency, item.duration, item.amplitude)
            elif isinstance(item, Phrase):
                notes = [note.frequency for note in item.notes]
                durations = [note.duration for note in item.notes]
                amplitudes = [note.amplitude for note in item.notes]
                wave = self.instrument.generate_phrase(notes, durations, amplitudes)
            
            full_wave = np.concatenate([full_wave, wave])
        
        return full_wave

    def play(self):
        full_wave = self.generate_composition()
        full_wave = full_wave * (2**15 - 1) / np.max(np.abs(full_wave))
        full_wave = full_wave.astype(np.int16)
        play_obj = sa.play_buffer(full_wave, 1, 2, self.sample_rate)
        play_obj.wait_done()