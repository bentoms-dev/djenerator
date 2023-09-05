import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage
import random
import os

def generate_djent_pattern(file_name_base='DjentPattern', num_measures=4, tempo_bpm=160, note_range=(40, 52)):
    # Create a new MIDI file
    midi = MidiFile()

    # Create a new MIDI track
    track = MidiTrack()
    midi.tracks.append(track)

    # Set the tempo (in microseconds per beat)
    tempo = 60000000 // tempo_bpm
    track.append(MetaMessage('set_tempo', tempo=tempo))

    # Define a structured rhythm pattern for djent with shorter notes
    rhythm_pattern = [240, 120, 60, 120]  # Example: 16th note, 32nd note, 64th note, 32nd note (shorter notes)

    # Generate a djent-style MIDI pattern
    for _ in range(num_measures):
        for duration in rhythm_pattern:
            # Randomly choose between a palm-muted note (lower velocity) and an accented note (higher velocity)
            velocity = random.choice([random.randint(60, 90), random.randint(100, 127)])
            note = random.randint(note_range[0], note_range[1])  # Random note within the specified range

            # Note On (with velocity)
            track.append(Message('note_on', note=note, velocity=velocity, time=0))

            # Note Off (after the specified duration)
            track.append(Message('note_off', note=note, velocity=0, time=duration))

    # Find an available file name by incrementing the base name
    file_name = file_name_base
    counter = 1
    while os.path.exists(file_name + '.mid'):
        file_name = f'{file_name_base}_{counter}'
        counter += 1

    # Save the MIDI file
    midi.save(file_name + '.mid')
    return file_name

def main():
    generated_file_name = generate_djent_pattern()
    print(f"Djent MIDI pattern '{generated_file_name}.mid' created and saved successfully.")

if __name__ == "__main__":
    main()
