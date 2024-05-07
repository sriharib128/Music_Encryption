import json
import random
from encryption import encrypt,best_look_up_table,generate_look_up_tables
from music_generation import generate_frequency_list, generate_audio_sequence
from decryption import decrypt_ciphertext, get_frequency_list, decrypt_swara

with open("swara_freq.json", "r") as f:
    swara_freq = json.load(f)

with open("arohana_swara.json", "r") as f:
    arohana_swara = json.load(f)

with open("swara_freq.json", "r") as f:
    swara_freq = json.load(f)

raga = "ganamurthi"
amsa_swara = "Pa"

text = arohana_swara[raga].split()
temp = swara_freq.copy()
for key in temp.keys():
    if key not in text:
        swara_freq.pop(key, None)

plaintext = "I LOVE MUSIC"
print(plaintext)

look_up_tables = generate_look_up_tables()
alphabet_swara = best_look_up_table(look_up_tables, plaintext, arohana_swara, raga, swara_freq)

print("Best Look Up Table:", alphabet_swara)

ciphertext = encrypt(plaintext, alphabet_swara,amsa_swara)
print("Ciphertext:", ciphertext)
print("="*100)
# working fine till above
print("Encryption is done into audio file with following frequencies 0.25s each")
freq_list = generate_frequency_list(ciphertext, arohana_swara[raga], swara_freq)
print(freq_list)
audio_file = f"audio_{raga}.wav"
sampling_rate = 4000
duration = 0.25
generate_audio_sequence(freq_list, duration=duration, sampling_rate=sampling_rate, output_file=audio_file)

window_size = int(duration * sampling_rate)
overlap = 0
swara_list = get_frequency_list(audio_file, window_size, overlap, swara_freq)
print("="*100)
decrypted_cypher = decrypt_swara(swara_list,amsa_swara)
print("Deciphertext:",decrypted_cypher)

# works fine from below
decrypted_text = decrypt_ciphertext(decrypted_cypher, alphabet_swara,amsa_swara)
print('Decrypted Text:', decrypted_text)
