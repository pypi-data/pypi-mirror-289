from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from pydub import AudioSegment
import os

class MediaReader:
    def __init__(self, media_path):
        self.media_path = media_path

    def get_video_extensions(self):
        video_extensions = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv']
        return video_extensions

    def get_audio_extensions(self):
        audio_extensions = ['.mp3', '.wav', '.aac', '.wma', '.flac']
        return audio_extensions

    def read_video(self, start_time, end_time, output_path):
        if not os.path.isfile(self.media_path):
            print(f"File not found: {self.media_path}")
            return

        if not self.is_video_extension(self.media_path):
            print(f"Invalid video extension: {self.media_path}")
            return

        ffmpeg_extract_subclip(self.media_path, start_time, end_time, targetname=output_path)

    def read_audio(self, output_path):
        if not os.path.isfile(self.media_path):
            print(f"File not found: {self.media_path}")
            return

        if not self.is_audio_extension(self.media_path):
            print(f"Invalid audio extension: {self.media_path}")
            return

        sound = AudioSegment.from_file(self.media_path)
        sound.export(output_path, format="wav")

    def is_video_extension(self, file_path):
        _, ext = os.path.splitext(file_path)
        return ext.lower() in self.get_video_extensions()

    def is_audio_extension(self, file_path):
        _, ext = os.path.splitext(file_path)
        return ext.lower() in self.get_audio_extensions()