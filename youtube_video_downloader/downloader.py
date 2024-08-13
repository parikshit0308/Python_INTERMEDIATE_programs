from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
def download_video(url, path_save):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        high_res_stream = streams.get_highest_resolution()
        high_res_stream.download(output_path = path_save)
        print('Video downloaded successfully.')
    except Exception as e:
        print(f'Error downloading video: {str(e)}')

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"selected folder is: {folder}")

        return folder

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter a youtube URL to download: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Downloading video...")
        download_video(video_url, save_dir)
    else:
        print("Please select a folder to save the downloaded video.")