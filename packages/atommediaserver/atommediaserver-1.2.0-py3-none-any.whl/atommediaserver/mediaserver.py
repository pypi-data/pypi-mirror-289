from ffmpeg import FFmpeg, Progress
import ctypes
import threading
import time
import cv2
import subprocess
import os
import numpy as np

def run_server():
    current_path = os.path.dirname(os.path.abspath(__file__))

    dll_path = os.path.join(current_path, 'atommedia.dll')
    dll = ctypes.CDLL(dll_path)

    result = dll.RunMediaServer("".encode('utf-8'))

def run():
    thread = threading.Thread(target=run_server)
    thread.start()

class RTSPStreamer:
    def __init__(self, width, height, output_postfix, quality):
        self.width = width
        self.height = height
        self.output_postfix = output_postfix
        self.running = True

        current_path = os.path.dirname(os.path.abspath(__file__))
        self.path_to_ffmpeg = os.path.join(current_path, 'decoder.exe')

        self.ffmpeg_command = [
            self.path_to_ffmpeg,
            '-y',
            '-f', 'rawvideo',
            '-fflags', 'nobuffer',
            '-flags', 'low_delay',
            '-probesize', '32',
            '-analyzeduration', '0',
            '-pix_fmt', 'bgra',
            '-s', f'{self.width}x{self.height}',
            '-i', 'pipe:0',
            '-c:v', 'mpeg4',
            '-qscale:v', f'{quality}',
            '-b:v', '20M',
            '-maxrate', '20M',
            '-bufsize', '40M',
            '-g', '1',
            '-f', 'rtsp',
            f'rtsp://localhost:8554/{self.output_postfix}'
        ]

        self.process = None

    def start(self):
        self.process = subprocess.Popen(self.ffmpeg_command, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        frame = np.zeros((
            self.width,
            self.height,
            4
        ), dtype=np.uint8)
        self.process.stdin.write(frame.tobytes())
        
        while self.running:
            pass

    def stop(self):
        self.running = False
        self.process.stdin.close()
        self.process.wait()

    def send_frame_to_ffmpeg(self, frame):
        self.process.stdin.write(frame.tobytes())
    