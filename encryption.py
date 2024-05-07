import random
import json
import os
from scoring import scoring
from music_generation import generate_frequency_list, generate_audio_sequence

def generate_look_up_tables():
    with open("two_three_four_five_comb.json", "r") as f:
        two_three_four_five_comb = json.load(f)
    all_possible_two_comb = two_three_four_five_comb[0]
    all_possible_three_comb = two_three_four_five_comb[1]

    random_two_list = [random.sample(range(15), 15) for _ in range(10)]
    random_three_list = [random.sample(range(11), 11) for _ in range(10)]

    look_up_tables = []
    two_list = ['A', 'C', 'D', 'E', 'F', 'H', 'I', 'L', 'M', 'N', 'O', 'R', 'S', 'T', 'U']
    three_list = ['B', 'G', 'J', 'K', 'P', 'Q', 'V', 'W', 'X', 'Y', 'Z']

    for i in range(10):
        look_up_table = {}
        for j in range(15):
            look_up_table[two_list[j]] = " ".join(all_possible_two_comb[random_two_list[i][j]])
        for j in range(11):
            look_up_table[three_list[j]] = " ".join(all_possible_three_comb[random_three_list[i][j]])
        look_up_tables.append(look_up_table)
    return look_up_tables

def best_look_up_table(look_up_tables, plaintext, arohana_swara, raga, swara_freq):
    max_score = 0
    best_look_up_table = None
    a = 0
    for look_up_table in look_up_tables:
        alphabet_swara = look_up_table
        ciphertext = encrypt(plaintext, alphabet_swara)
        freq_list = generate_frequency_list(ciphertext, arohana_swara[raga], swara_freq)
        audio_file = f"./midi_files/audio_sequence_{a}.wav"
        sampling_rate = 4000
        duration = 0.25
        os.makedirs("./midi_files", exist_ok=True)
        generate_audio_sequence(freq_list, duration=duration, sampling_rate=sampling_rate, output_file=audio_file, output_midi=f"./midi_files/audio_{raga}_{a}.mid")
        a += 1

    for i in range(a):
        audio_file = f"./midi_files/audio_{raga}_{i}.mid"
        print(audio_file)
        score = scoring(audio_file)
        if score > max_score:
            max_score = score
            best_look_up_table = look_up_tables[i]
    return best_look_up_table

def encrypt(plaintext, alphabet_swara,amsa_swara='Pa'):
    ciphertext = ''
    for char in plaintext:
        if char != ' ':
            ciphertext += alphabet_swara[char.upper()] + amsa_swara
        if char == ' ':
            ciphertext += f' {amsa_swara}'
    return ciphertext