NOTE_FREQUENCIES = {
    # Octave 0
    'C0': 16.35, 'C#0': 17.32, 'Db0': 17.32, 'D0': 18.35, 'D#0': 19.45, 'Eb0': 19.45,
    'E0': 20.60, 'F0': 21.83, 'F#0': 23.12, 'Gb0': 23.12, 'G0': 24.50, 'G#0': 25.96,
    'Ab0': 25.96, 'A0': 27.50, 'A#0': 29.14, 'Bb0': 29.14, 'B0': 30.87,

    # Octave 1
    'C1': 32.70, 'C#1': 34.65, 'Db1': 34.65, 'D1': 36.71, 'D#1': 38.89, 'Eb1': 38.89,
    'E1': 41.20, 'F1': 43.65, 'F#1': 46.25, 'Gb1': 46.25, 'G1': 49.00, 'G#1': 51.91,
    'Ab1': 51.91, 'A1': 55.00, 'A#1': 58.27, 'Bb1': 58.27, 'B1': 61.74,

    # Octave 2
    'C2': 65.41, 'C#2': 69.30, 'Db2': 69.30, 'D2': 73.42, 'D#2': 77.78, 'Eb2': 77.78,
    'E2': 82.41, 'F2': 87.31, 'F#2': 92.50, 'Gb2': 92.50, 'G2': 98.00, 'G#2': 103.83,
    'Ab2': 103.83, 'A2': 110.00, 'A#2': 116.54, 'Bb2': 116.54, 'B2': 123.47,

    # Octave 3
    'C3': 130.81, 'C#3': 138.59, 'Db3': 138.59, 'D3': 146.83, 'D#3': 155.56, 'Eb3': 155.56,
    'E3': 164.81, 'F3': 174.61, 'F#3': 185.00, 'Gb3': 185.00, 'G3': 196.00, 'G#3': 207.65,
    'Ab3': 207.65, 'A3': 220.00, 'A#3': 233.08, 'Bb3': 233.08, 'B3': 246.94,

    # Octave 4 (existing in your original dictionary)
    'C4': 261.63, 'C#4': 277.18, 'Db4': 277.18, 'D4': 293.66, 'D#4': 311.13, 'Eb4': 311.13,
    'E4': 329.63, 'F4': 349.23, 'F#4': 369.99, 'Gb4': 369.99, 'G4': 392.00, 'G#4': 415.30,
    'Ab4': 415.30, 'A4': 440.00, 'A#4': 466.16, 'Bb4': 466.16, 'B4': 493.88,

    # Octave 5 (existing in your original dictionary)
    'C5': 523.25, 'C#5': 554.37, 'Db5': 554.37, 'D5': 587.33, 'D#5': 622.25, 'Eb5': 622.25,
    'E5': 659.25, 'F5': 698.46, 'F#5': 739.99, 'Gb5': 739.99, 'G5': 783.99, 'G#5': 830.61,
    'Ab5': 830.61, 'A5': 880.00, 'A#5': 932.33, 'Bb5': 932.33, 'B5': 987.77,

    # Octave 6 (existing in your original dictionary)
    'C6': 1046.50, 'C#6': 1108.73, 'Db6': 1108.73, 'D6': 1174.66, 'D#6': 1244.51, 'Eb6': 1244.51,
    'E6': 1318.51, 'F6': 1396.91, 'F#6': 1479.98, 'Gb6': 1479.98, 'G6': 1567.98, 'G#6': 1661.22,
    'Ab6': 1661.22, 'A6': 1760.00, 'A#6': 1864.66, 'Bb6': 1864.66, 'B6': 1975.53,

    # Octave 7
    'C7': 2093.00, 'C#7': 2217.46, 'Db7': 2217.46, 'D7': 2349.32, 'D#7': 2489.02, 'Eb7': 2489.02,
    'E7': 2637.02, 'F7': 2793.83, 'F#7': 2959.96, 'Gb7': 2959.96, 'G7': 3135.96, 'G#7': 3322.44,
    'Ab7': 3322.44, 'A7': 3520.00, 'A#7': 3729.31, 'Bb7': 3729.31, 'B7': 3951.07,

    # Octave 8
    'C8': 4186.01, 'C#8': 4434.92, 'Db8': 4434.92, 'D8': 4698.63, 'D#8': 4978.03, 'Eb8': 4978.03,
    'E8': 5274.04, 'F8': 5587.65, 'F#8': 5919.91, 'Gb8': 5919.91, 'G8': 6271.93, 'G#8': 6644.88,
    'Ab8': 6644.88, 'A8': 7040.00, 'A#8': 7458.62, 'Bb8': 7458.62, 'B8': 7902.13
}

CHORDS = {
    # C chords
    'C_major': ['C4', 'E4', 'G4'],
    'C_minor': ['C4', 'Eb4', 'G4'],
    'C_diminished': ['C4', 'Eb4', 'Gb4'],
    'C_augmented': ['C4', 'E4', 'G#4'],
    'C_sus2': ['C4', 'D4', 'G4'],
    'C_sus4': ['C4', 'F4', 'G4'],
    'C_major7': ['C4', 'E4', 'G4', 'B4'],
    'C_minor7': ['C4', 'Eb4', 'G4', 'Bb4'],
    'C_dominant7': ['C4', 'E4', 'G4', 'Bb4'],
    'C_diminished7': ['C4', 'Eb4', 'Gb4', 'A4'],
    'C_half_diminished7': ['C4', 'Eb4', 'Gb4', 'Bb4'],
    'C_major9': ['C4', 'E4', 'G4', 'B4', 'D5'],
    'C_minor9': ['C4', 'Eb4', 'G4', 'Bb4', 'D5'],
    'C_dominant9': ['C4', 'E4', 'G4', 'Bb4', 'D5'],
    'C_add9': ['C4', 'E4', 'G4', 'D5'],
    
    # C# / Db chords
    'C#_major': ['C#4', 'F4', 'G#4'],
    'Db_major': ['Db4', 'F4', 'Ab4'],
    'C#_minor': ['C#4', 'E4', 'G#4'],
    'Db_minor': ['Db4', 'E4', 'Ab4'],
    'C#_diminished': ['C#4', 'E4', 'G4'],
    'C#_augmented': ['C#4', 'F4', 'A4'],
    'C#_sus2': ['C#4', 'D#4', 'G#4'],
    'C#_sus4': ['C#4', 'F#4', 'G#4'],
    'C#_major7': ['C#4', 'F4', 'G#4', 'C5'],
    'C#_minor7': ['C#4', 'E4', 'G#4', 'B4'],
    'C#_dominant7': ['C#4', 'F4', 'G#4', 'B4'],
    
    # D chords
    'D_major': ['D4', 'F#4', 'A4'],
    'D_minor': ['D4', 'F4', 'A4'],
    'D_diminished': ['D4', 'F4', 'Ab4'],
    'D_augmented': ['D4', 'F#4', 'A#4'],
    'D_sus2': ['D4', 'E4', 'A4'],
    'D_sus4': ['D4', 'G4', 'A4'],
    'D_major7': ['D4', 'F#4', 'A4', 'C#5'],
    'D_minor7': ['D4', 'F4', 'A4', 'C5'],
    'D_dominant7': ['D4', 'F#4', 'A4', 'C5'],
    'D_diminished7': ['D4', 'F4', 'Ab4', 'B4'],
    'D_half_diminished7': ['D4', 'F4', 'Ab4', 'C5'],
    
    # D# / Eb chords
    'D#_major': ['D#4', 'G4', 'A#4'],
    'Eb_major': ['Eb4', 'G4', 'Bb4'],
    'D#_minor': ['D#4', 'F#4', 'A#4'],
    'Eb_minor': ['Eb4', 'Gb4', 'Bb4'],
    'D#_diminished': ['D#4', 'F#4', 'A4'],
    'D#_augmented': ['D#4', 'G4', 'B4'],
    'D#_sus2': ['D#4', 'F4', 'A#4'],
    'D#_sus4': ['D#4', 'G#4', 'A#4'],
    
    # E chords
    'E_major': ['E4', 'G#4', 'B4'],
    'E_minor': ['E4', 'G4', 'B4'],
    'E_diminished': ['E4', 'G4', 'Bb4'],
    'E_augmented': ['E4', 'G#4', 'C5'],
    'E_sus2': ['E4', 'F#4', 'B4'],
    'E_sus4': ['E4', 'A4', 'B4'],
    'E_major7': ['E4', 'G#4', 'B4', 'D#5'],
    'E_minor7': ['E4', 'G4', 'B4', 'D5'],
    'E_dominant7': ['E4', 'G#4', 'B4', 'D5'],
    
    # F chords
    'F_major': ['F4', 'A4', 'C5'],
    'F_minor': ['F4', 'Ab4', 'C5'],
    'F_diminished': ['F4', 'Ab4', 'B4'],
    'F_augmented': ['F4', 'A4', 'C#5'],
    'F_sus2': ['F4', 'G4', 'C5'],
    'F_sus4': ['F4', 'Bb4', 'C5'],
    'F_major7': ['F4', 'A4', 'C5', 'E5'],
    'F_minor7': ['F4', 'Ab4', 'C5', 'Eb5'],
    'F_dominant7': ['F4', 'A4', 'C5', 'Eb5'],
    
    # F# / Gb chords
    'F#_major': ['F#4', 'A#4', 'C#5'],
    'Gb_major': ['Gb4', 'Bb4', 'Db5'],
    'F#_minor': ['F#4', 'A4', 'C#5'],
    'Gb_minor': ['Gb4', 'A4', 'Db5'],
    'F#_diminished': ['F#4', 'A4', 'C5'],
    'F#_augmented': ['F#4', 'A#4', 'D5'],
    'F#_sus2': ['F#4', 'G#4', 'C#5'],
    'F#_sus4': ['F#4', 'B4', 'C#5'],
    
    # G chords
    'G_major': ['G4', 'B4', 'D5'],
    'G_minor': ['G4', 'Bb4', 'D5'],
    'G_diminished': ['G4', 'Bb4', 'Db5'],
    'G_augmented': ['G4', 'B4', 'D#5'],
    'G_sus2': ['G4', 'A4', 'D5'],
    'G_sus4': ['G4', 'C5', 'D5'],
    'G_major7': ['G4', 'B4', 'D5', 'F#5'],
    'G_minor7': ['G4', 'Bb4', 'D5', 'F5'],
    'G_dominant7': ['G4', 'B4', 'D5', 'F5'],
    'G_diminished7': ['G4', 'Bb4', 'Db5', 'E5'],
    'G_half_diminished7': ['G4', 'Bb4', 'Db5', 'F5'],
    
    # G# / Ab chords
    'G#_major': ['G#4', 'C5', 'D#5'],
    'Ab_major': ['Ab4', 'C5', 'Eb5'],
    'G#_minor': ['G#4', 'B4', 'D#5'],
    'Ab_minor': ['Ab4', 'B4', 'Eb5'],
    'G#_diminished': ['G#4', 'B4', 'D5'],
    'G#_augmented': ['G#4', 'C5', 'E5'],
    'G#_sus2': ['G#4', 'A#4', 'D#5'],
    'G#_sus4': ['G#4', 'C#5', 'D#5'],
    
    # A chords
    'A_major': ['A4', 'C#5', 'E5'],
    'A_minor': ['A4', 'C5', 'E5'],
    'A_diminished': ['A4', 'C5', 'Eb5'],
    'A_augmented': ['A4', 'C#5', 'F5'],
    'A_sus2': ['A4', 'B4', 'E5'],
    'A_sus4': ['A4', 'D5', 'E5'],
    'A_major7': ['A4', 'C#5', 'E5', 'G#5'],
    'A_minor7': ['A4', 'C5', 'E5', 'G5'],
    'A_dominant7': ['A4', 'C#5', 'E5', 'G5'],
    'A_diminished7': ['A4', 'C5', 'Eb5', 'Gb5'],
    'A_half_diminished7': ['A4', 'C5', 'Eb5', 'G5'],
    
    # A# / Bb chords
    'A#_major': ['A#4', 'D5', 'F5'],
    'Bb_major': ['Bb4', 'D5', 'F5'],
    'A#_minor': ['A#4', 'C#5', 'F5'],
    'Bb_minor': ['Bb4', 'Db5', 'F5'],
    'A#_diminished': ['A#4', 'C#5', 'E5'],
    'A#_augmented': ['A#4', 'D5', 'F#5'],
    'A#_sus2': ['A#4', 'C5', 'F5'],
    'A#_sus4': ['A#4', 'D#5', 'F5'],
    
    # B chords
    'B_major': ['B4', 'D#5', 'F#5'],
    'B_minor': ['B4', 'D5', 'F#5'],
    'B_diminished': ['B4', 'D5', 'F5'],
    'B_augmented': ['B4', 'D#5', 'G5'],
    'B_sus2': ['B4', 'C#5', 'F#5'],
    'B_sus4': ['B4', 'E5', 'F#5'],
    'B_major7': ['B4', 'D#5', 'F#5', 'A#5'],
    'B_minor7': ['B4', 'D5', 'F#5', 'A5'],
    'B_dominant7': ['B4', 'D#5', 'F#5', 'A5'],
    'B_diminished7': ['B4', 'D5', 'F5', 'Ab5'],
    'B_half_diminished7': ['B4', 'D5', 'F5', 'A5'],
    
    # Extended and altered chords (examples)
    'C_maj9': ['C4', 'E4', 'G4', 'B4', 'D5'],
    'D_min11': ['D4', 'F4', 'A4', 'C5', 'E5', 'G5'],
    'G_13': ['G4', 'B4', 'D5', 'F5', 'A5', 'C6', 'E6'],
    'Eb_7#9': ['Eb4', 'G4', 'Bb4', 'Db5', 'F#5'],
    'F#_7b9': ['F#4', 'A#4', 'C#5', 'E5', 'G5'],
    'A_add9': ['A4', 'C#5', 'E5', 'B5'],
    'Bb_6/9': ['Bb4', 'D5', 'F5', 'G5', 'C6'],
    
    # Polychords (examples)
    'C/E': ['E4', 'G4', 'C5'],
    'G/B': ['B4', 'D5', 'G5'],
    'Am/C': ['C4', 'E4', 'A4'],
    'F/G': ['G4', 'A4', 'C5', 'F5'],
    
    # Quartal and quintal chords (examples)
    'C_quartal': ['C4', 'F4', 'Bb4', 'Eb5'],
    'D_quintal': ['D4', 'A4', 'E5', 'B5'],
    
    # Cluster chords (examples)
    'C_cluster': ['C4', 'C#4', 'D4', 'D#4'],
    'F_cluster': ['F4', 'F#4', 'G4', 'G#4'],
}