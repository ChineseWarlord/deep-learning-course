import os
import argparse
import subprocess
from multiprocessing import Pool

def convert_webm_to_mp3(file_tuple):
    webm_file, mp3_file = file_tuple
    subprocess.run(['ffmpeg', '-i', webm_file, '-vn', '-acodec', 'libmp3lame', mp3_file])

def convert_webm_files(webm_files, mp3_path, num_processes=8):
    # Create the output directory if it doesn't exist
    if not os.path.exists(mp3_path):
        os.makedirs(mp3_path)

    file_tuples = []

    # Create tuples of input and output file paths
    for webm_file in webm_files:
        mp3_file = os.path.join(mp3_path, os.path.splitext(os.path.basename(webm_file))[0] + '.mp3')
        file_tuples.append((webm_file, mp3_file))

    # Use multiprocessing to convert files simultaneously
    with Pool(num_processes) as pool:
        pool.map(convert_webm_to_mp3, file_tuples)

def main():
    parser = argparse.ArgumentParser(description='Convert .webm files to .mp3')
    parser.add_argument('--webm_path', type=str, help='Path to folder containing .webm files')
    parser.add_argument('--mp3_path', type=str, help='Path to output folder for .mp3 files')
    parser.add_argument('--num_processes', type=int, default=4, help='Number of processes for multiprocessing')
    args = parser.parse_args()

    if not args.webm_path or not args.mp3_path:
        parser.print_help()
        return

    webm_files = [os.path.join(args.webm_path, file) for file in os.listdir(args.webm_path) if file.endswith('.webm')]

    convert_webm_files(webm_files, args.mp3_path, args.num_processes)

if __name__ == "__main__":
    main()
