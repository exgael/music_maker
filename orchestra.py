import numpy as np
import simpleaudio as sa
from music_player import MusicComposer

class Track:
    def __init__(self, instrument, name=""):
        self.composer = MusicComposer(instrument)
        self.name = name

    def add_note(self, note, duration=0.5, amplitude=0.5):
        self.composer.add_note(note, duration, amplitude)
        return self

    def add_chord(self, chord_name, duration=0.5, amplitude=0.5):
        self.composer.add_chord(chord_name, duration, amplitude)
        return self

    def add_phrase(self, notes, durations, amplitudes):
        self.composer.add_phrase(notes, durations, amplitudes)
        return self

class Orchestra:
    def __init__(self, sample_rate=44100):
        self.tracks = []
        self.sample_rate = sample_rate

    def create_track(self, instrument, name=""):
        track = Track(instrument, name)
        self.tracks.append(track)
        return track

    def generate_composition(self):
        max_length = 0
        track_waves = []

        for track in self.tracks:
            wave = track.composer.generate_composition()
            track_waves.append(wave)
            max_length = max(max_length, len(wave))

        # Pad shorter tracks with silence
        padded_waves = [np.pad(wave, (0, max_length - len(wave))) for wave in track_waves]

        # Mix all tracks
        mixed_wave = np.sum(padded_waves, axis=0)

        # Normalize the mixed wave
        mixed_wave = mixed_wave / np.max(np.abs(mixed_wave))

        return mixed_wave

    def play(self):
        mixed_wave = self.generate_composition()
        mixed_wave = (mixed_wave * 32767).astype(np.int16)
        play_obj = sa.play_buffer(mixed_wave, 1, 2, self.sample_rate)
        play_obj.wait_done()