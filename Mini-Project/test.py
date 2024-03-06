import os
import librosa
import time

def count_channels(directory, output_file):
    files = [f for f in os.listdir(directory) if f.endswith('.mp3')]
    with open(output_file, 'w') as f:
        for file in files:
            file_path = os.path.join(directory, file)
            audio, _ = librosa.load(file_path, sr=None, mono=False)
            channels = "Mono" if len(audio.shape) == 1 else "Stereo"
            f.write(f"File: {file}, Channels: {channels}\n")

if __name__ == "__main__":
    directory = input("Enter the directory containing the MP3 files: ")
    count_channels(r"../Dataset/MP3/", "Mono_Stereo.txt")
