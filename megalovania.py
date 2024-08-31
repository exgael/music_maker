from orchestra import Orchestra
from mario_angel_synth import MarioAngelSynth
from violin_instrument import Violin
from harp_instrument import Harp
from kalimba_instrument import Kalimba
from music_utils import NOTE_FREQUENCIES

# Create an orchestra
orchestra = Orchestra()

# Create tracks for each instrument
synth_track = orchestra.create_track(MarioAngelSynth(), "Synth")
violin_track = orchestra.create_track(Violin(), "Violin")
harp_track = orchestra.create_track(Harp(), "Harp")
kalimba_track = orchestra.create_track(Kalimba(), "Kalimba")

# Megalovania main melody
def add_main_melody(track):
    melody = ['D4', 'D4', 'D5', 'A4', 'G#4', 'G4', 'F4', 'D4', 'F4', 'G4']
    for _ in range(2):  # Repeat twice
        for note in melody:
            track.add_note(note, 0.15, 0.7)
    
    melody_2 = ['C4', 'C4', 'D5', 'A4', 'G#4', 'G4', 'F4', 'D4', 'F4', 'G4']
    for note in melody_2:
        track.add_note(note, 0.15, 0.7)
    
    melody_3 = ['B3', 'B3', 'D5', 'A4', 'G#4', 'G4', 'F4', 'D4', 'F4', 'G4']
    for note in melody_3:
        track.add_note(note, 0.15, 0.7)

# Add the main melody to the synth track
add_main_melody(synth_track)

# Add a harmony to the violin track
def add_harmony(track):
    harmony = ['A3', 'A3', 'A3', 'A3', 'G#3', 'G3', 'F3', 'F3', 'F3', 'G3']
    for _ in range(3):  # Repeat three times
        for note in harmony:
            track.add_note(note, 0.3, 0.5)
    
    harmony_2 = ['G3', 'G3', 'G3', 'G3', 'F#3', 'F3', 'E3', 'E3', 'E3', 'F#3']
    for note in harmony_2:
        track.add_note(note, 0.3, 0.5)

add_harmony(violin_track)

# Add arpeggios to the harp track
def add_arpeggios(track):
    arpeggios = [
        ['D4', 'A4', 'D5'], ['D4', 'A4', 'D5'],
        ['C4', 'G4', 'C5'], ['C4', 'G4', 'C5'],
        ['B3', 'F#4', 'B4'], ['B3', 'F#4', 'B4'],
        ['A#3', 'F4', 'A#4'], ['A#3', 'F4', 'A#4']
    ]
    for arpeggio in arpeggios:
        track.add_phrase(arpeggio, [0.1, 0.1, 0.1], [0.4, 0.4, 0.4])
        track.add_phrase(arpeggio, [0.1, 0.1, 0.1], [0.4, 0.4, 0.4])

add_arpeggios(harp_track)


# Add a rhythmic ostinato to the kalimba track
def add_ostinato(track):
    ostinato = ['D4', 'A3'] * 20
    for note in ostinato:
        track.add_note(note, 0.15, 0.3)

add_ostinato(kalimba_track)

# Play the composition
orchestra.play()