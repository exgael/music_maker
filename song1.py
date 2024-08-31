from harp_instrument import Harp
from music_player import MusicComposer
import numpy as np

# Create a Harp instance
harp = Harp()

# Create a MusicComposer instance with the harp
composer = MusicComposer(harp)

# Helper function to create arpeggios
def add_arpeggio(notes, base_duration, amplitude_range):
    durations = [base_duration] * len(notes)
    amplitudes = np.linspace(amplitude_range[0], amplitude_range[1], len(notes))
    composer.add_phrase(notes, durations, amplitudes)

# Introduction
add_arpeggio(['C4', 'E4', 'G4', 'C5', 'E5', 'G5', 'C6', 'G5', 'E5', 'C5', 'G4', 'E4'], 0.2, (0.5, 0.7))

# Verse 1
for _ in range(2):
    add_arpeggio(['F4', 'A4', 'C5', 'F5', 'A5', 'C6', 'A5', 'F5'], 0.25, (0.6, 0.8))
    add_arpeggio(['G4', 'B4', 'D5', 'G5', 'B5', 'D6', 'B5', 'G5'], 0.25, (0.6, 0.8))
    add_arpeggio(['E4', 'G4', 'B4', 'E5', 'G5', 'B5', 'G5', 'E5'], 0.25, (0.6, 0.8))
    add_arpeggio(['A4', 'C5', 'E5', 'A5', 'C6', 'E6', 'C6', 'A5'], 0.25, (0.6, 0.8))

# Bridge
add_arpeggio(['D4', 'F4', 'A4', 'D5', 'F5', 'A5', 'D6', 'A5', 'F5', 'D5', 'A4', 'F4'], 0.2, (0.7, 0.9))
add_arpeggio(['G4', 'B4', 'D5', 'G5', 'B5', 'D6', 'G6', 'D6', 'B5', 'G5', 'D5', 'B4'], 0.2, (0.7, 0.9))

# Chorus
for _ in range(2):
    add_arpeggio(['C4', 'E4', 'G4', 'C5', 'E5', 'G5', 'C6', 'G5'], 0.2, (0.8, 1.0))
    add_arpeggio(['F4', 'A4', 'C5', 'F5', 'A5', 'C6', 'F6', 'C6'], 0.2, (0.8, 1.0))
    add_arpeggio(['G4', 'B4', 'D5', 'G5', 'B5', 'D6', 'G6', 'D6'], 0.2, (0.8, 1.0))
    add_arpeggio(['A4', 'C5', 'E5', 'A5', 'C6', 'E6', 'A6', 'E6'], 0.2, (0.8, 1.0))

# Verse 2 (variation)
for _ in range(2):
    add_arpeggio(['D4', 'F4', 'A4', 'D5', 'F5', 'A5', 'F5', 'D5'], 0.25, (0.6, 0.8))
    add_arpeggio(['G4', 'B4', 'D5', 'G5', 'B5', 'D6', 'B5', 'G5'], 0.25, (0.6, 0.8))
    add_arpeggio(['E4', 'G4', 'B4', 'E5', 'G5', 'B5', 'G5', 'E5'], 0.25, (0.6, 0.8))
    add_arpeggio(['A4', 'C5', 'E5', 'A5', 'C6', 'E6', 'C6', 'A5'], 0.25, (0.6, 0.8))

# Bridge (variation)
add_arpeggio(['F4', 'A4', 'C5', 'F5', 'A5', 'C6', 'F6', 'C6', 'A5', 'F5', 'C5', 'A4'], 0.2, (0.7, 0.9))
add_arpeggio(['G4', 'B4', 'D5', 'G5', 'B5', 'D6', 'G6', 'D6', 'B5', 'G5', 'D5', 'B4'], 0.2, (0.7, 0.9))

# Chorus (repeated)
for _ in range(2):
    add_arpeggio(['C4', 'E4', 'G4', 'C5', 'E5', 'G5', 'C6', 'G5'], 0.2, (0.8, 1.0))
    add_arpeggio(['F4', 'A4', 'C5', 'F5', 'A5', 'C6', 'F6', 'C6'], 0.2, (0.8, 1.0))
    add_arpeggio(['G4', 'B4', 'D5', 'G5', 'B5', 'D6', 'G6', 'D6'], 0.2, (0.8, 1.0))
    add_arpeggio(['A4', 'C5', 'E5', 'A5', 'C6', 'E6', 'A6', 'E6'], 0.2, (0.8, 1.0))

# Outro
add_arpeggio(['C4', 'E4', 'G4', 'C5', 'E5', 'G5', 'C6', 'E6', 'G6', 'E6', 'C6', 'G5', 'E5', 'C5', 'G4', 'E4', 'C4'], 0.15, (0.9, 0.5))

# Play the composition
composer.play()