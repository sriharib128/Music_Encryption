# Music Encryption and Decryption

This project demonstrates a music-based encryption and decryption system using swaras (musical notes) and ragas (melodic frameworks) from Indian classical music. The system generates multiple look-up tables using different ragas, encrypts the plaintext into a sequence of swaras, generates multiple encrypted audio sequences, and then selects the best raga and look-up table based on a scoring function. The decryption process then uses the selected raga and look-up table to decrypt the audio sequence back into the original plaintext.

## Prerequisites

- Python 3.x
- NumPy
- SciPy
- Mido

## Installation

1. Clone the repository:
   ```
   https://github.com/sriharib128/Music_Encryption.git
   ```

2. Install the required dependencies:
   ```
   pip install numpy scipy mido
   ```

## Usage

1. Prepare the necessary JSON files:
   - `swara_freq.json`: Contains the mapping of swaras to their corresponding frequencies.
   - `arohan_swara.json`: Contains the arohan (ascending) sequence of swaras for different ragas.
   - `two_three_four_five_comb.json`: Contains the possible combinations of swaras for encryption.

2. Update the `main.py` script with the desired plaintext.

3. Run the `main.py` script:
   ```
   python main.py
   ```

4. The script will perform the following steps:
   - Generate multiple look-up tables using different ragas.
   - Encrypt the plaintext into multiple encrypted audio sequences.
   - Score the encrypted audio sequences based on a pleasantness metric.
   - Select the best raga and look-up table based on the scoring function.
   - Decrypt the selected encrypted audio sequence back into the original plaintext.

5. The selected raga name, look-up table, encrypted ciphertext, and decrypted plaintext will be displayed in the console.

## File Structure

- `encryption.py`: Contains functions related to encryption.
- `music_generation.py`: Contains functions for generating music and audio sequences.
- `decryption.py`: Contains functions for decryption and frequency analysis.
- `scoring.py`: Contains the scoring function.
- `main.py`: The main script that ties everything together and executes the program.

## Customization

- Modify the `swara_freq.json` file to change the mapping of swaras to frequencies.
- Update the `arohan_swara.json` file to include different ragas and their corresponding arohan sequences.
- Customize the `two_three_four_five_comb.json` file to change the possible combinations of swaras for encryption.
- Adjust the parameters in the `main.py` script, such as the plaintext, sampling rate, and duration, to suit your needs.

## Acknowledgements

- The concept of using Indian classical music for encryption and decryption was inspired by various research papers and articles.
- The project utilizes the NumPy, SciPy, and Mido libraries for audio processing and MIDI generation.