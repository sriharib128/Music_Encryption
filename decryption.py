from scipy.io import wavfile
import numpy as np

def get_key(alphabet_swara, value):
    for k, v in alphabet_swara.items():
        if v == value:
            return k
    return None

def reverse_map_full_swaras(full_swaras):
    for (i,swara) in enumerate(full_swaras):
        if(len(swara))==3:
            full_swaras[i]=swara[:2]
        elif(len(swara))==4:
            full_swaras[i]=swara[:3]
    return full_swaras

def decrypt_ciphertext(ciphertext, alphabet_swara,amsa_swara='Pa'):
    plaintext = ''
    for swara_seq in ciphertext.split(amsa_swara):
        if swara_seq == ' ':
            plaintext += " "
        else:
            if get_key(alphabet_swara, swara_seq):
                plaintext += get_key(alphabet_swara, swara_seq)
    return plaintext

def get_frequency_list(audio_file, window_size, overlap, swara_freq):
    sampling_rate, data = wavfile.read(audio_file)
    frequency_list = []
    step_size = int(window_size * (1 - overlap))

    for i in range(0, len(data), step_size):
        window = data[i:i+window_size]
        fft_result = np.fft.fft(window)
        frequencies = np.fft.fftfreq(len(window), 1 / sampling_rate)
        max_index = np.argmax(np.abs(fft_result))
        max_frequency = np.abs(frequencies[max_index])
        frequency_list.append(max_frequency)

    nearest_swara = []
    for freq in frequency_list:
        nearest = min(swara_freq.values(), key=lambda x: abs(x - freq))
        nearest_swara.append([key for key, value in swara_freq.items() if value == nearest][0])
    return reverse_map_full_swaras(nearest_swara)

def decrypt_swara(swara_list,amsa_swara='Pa'):
    plaintext = ''
    words = []
    word_list = []
    for i in range(len(swara_list)-1):
        if swara_list[i] == amsa_swara and swara_list[i-1] == amsa_swara:
            continue
        if swara_list[i] == amsa_swara and swara_list[i+1] == amsa_swara:
            words.append(word_list.copy())
            word_list.clear()
            continue
        word_list.append(swara_list[i])

    list_of_strings = []
    for word in words:
        swara_subseq = ''
        for i in range(len(word)):
            if word[i] == amsa_swara:
                swara_subseq = swara_subseq[:-1] + amsa_swara
                continue
            swara_subseq += word[i] + " "
        list_of_strings.append(swara_subseq)

    single_string = ''
    for string in list_of_strings:
        single_string += string[:-1] + f"{amsa_swara} {amsa_swara}"
    return single_string[:-5] + amsa_swara