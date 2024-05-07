# Music Encryption and Decryption

This project demonstrates a music-based encryption and decryption system using swaras (musical notes) and ragas (melodic frameworks) from Indian classical music. The system encrypts plaintext into a sequence of swaras, generates an audio sequence based on the encrypted swaras, and then decrypts the audio sequence back into the original plaintext.

## Prerequisites

- Python 3.x
- NumPy
- SciPy
- Mido

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/music-encryption-decryption.git
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

2. Update the `main.py` script with the desired plaintext, raga, and other parameters.

3. Run the `main.py` script:
   ```
   python main.py
   ```

4. The script will perform the following steps:
   - Generate multiple look-up tables for encryption.
   - Select the best look-up table based on the scoring function.
   - Encrypt the plaintext using the selected look-up table.
   - Generate an audio sequence based on the encrypted swaras.
   - Decrypt the audio sequence back into the original plaintext.

5. The encrypted ciphertext, generated audio files (WAV and MIDI), and decrypted plaintext will be displayed in the console.

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
- Adjust the parameters in the `main.py` script, such as the plaintext, raga, sampling rate, and duration, to suit your needs.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The concept of using Indian classical music for encryption and decryption was inspired by various research papers and articles.
- The project utilizes the NumPy, SciPy, and Mido libraries for audio processing and MIDI generation.

## Contact

For any questions or inquiries, please contact [your-email@example.com](mailto:your-email@example.com).