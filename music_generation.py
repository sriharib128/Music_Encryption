import numpy as np
from scipy.io.wavfile import write
import mido

def map_shorthand_swaras(swaras, raga_seq,amsa_swara='Pa'):
    for i, swara in enumerate(swaras):
        index = raga_seq.find(swara)
        if swara not in ["Dha", "Sa","Pa"]:
            num = raga_seq[index+2:index+3]
            swaras[i] = swara + num
        elif swara == "Dha":
            num = raga_seq[index+3:index+4]
            swaras[i] = swara + num
    return swaras

def reverse_map_full_swaras(full_swaras):
    for i, swara in enumerate(full_swaras):
        if len(swara) == 3:
            full_swaras[i] = swara[:2]
        elif len(swara) == 4:
            full_swaras[i] = swara[:3]
    return full_swaras

def generate_frequency_list(swara_sequence, raga_seq, swara_freq,amsa_swara='Pa'):
    # print(swara_freq)
    swara_list = []
    for word in swara_sequence.split(f'{amsa_swara} {amsa_swara}'):
        for character in word.split(amsa_swara):
            if character != "":
                swara_list.extend(character.split())
                swara_list.extend(amsa_swara.split())
        swara_list.extend(amsa_swara.split())
    swara_list = map_shorthand_swaras(swara_list, raga_seq,amsa_swara)
    # print(swara_list)
    freq_list = [swara_freq[swara] for swara in swara_list]
    return freq_list

def generate_audio_sequence(frequency_list, duration=0.5, sampling_rate=44100, output_file="audio_sequence.wav", output_midi="audio_sequence.mid"):
    def generate_sine_wave(frequency, duration, sampling_rate):
        t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
        return np.sin(2 * np.pi * frequency * t)

    audio_sequence = np.array([])
    for freq in frequency_list:
        audio_sequence = np.concatenate((audio_sequence, generate_sine_wave(freq, duration, sampling_rate)))

    audio_sequence *= 32767 / np.max(np.abs(audio_sequence))
    audio_sequence = audio_sequence.astype(np.int16)

    write(output_file, sampling_rate, audio_sequence)

    midi_file = mido.MidiFile()
    track = mido.MidiTrack()
    midi_file.tracks.append(track)

    tempo = mido.bpm2tempo(120)
    track.append(mido.MetaMessage('set_tempo', tempo=tempo))
    track.append(mido.MetaMessage('time_signature', numerator=4, denominator=4))

    for freq in frequency_list:
        note = mido.Message('note_on', note=midi_note_number(freq), velocity=100, time=0)
        track.append(note)
        note = mido.Message('note_off', note=midi_note_number(freq), velocity=100, time=int(mido.second2tick(duration, midi_file.ticks_per_beat, tempo)))
        track.append(note)

    midi_file.save(output_midi)

def midi_note_number(frequency):
    return int(12 * np.log2(frequency / 440) + 69)