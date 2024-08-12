import threading
import queue
import sounddevice as sd
import numpy as np
from TTS.api import TTS

class CoquiXTTSStreamer:
    def __init__(self, model_path, device_name="default"):
        self.tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False)
        #self.tts.to("cuda" if self.tts.is_cuda_available else "cpu")
        self.device_name = device_name
        self.audio_queue = queue.Queue()
        self.stop_event = threading.Event()

    def text_to_speech_worker(self, text):
        chunks = self.tts.tts_to_stream(text)
        for chunk in chunks:
            if self.stop_event.is_set():
                break
            self.audio_queue.put(chunk)
        self.audio_queue.put(None)  # Signal end of stream

    def audio_callback(self, outdata, frames, time, status):
        if status:
            print(status)
        
        chunk = self.audio_queue.get()
        if chunk is None:
            raise sd.CallbackStop()
        
        if len(chunk) < len(outdata):
            outdata[:len(chunk)] = chunk
            outdata[len(chunk):] = 0
        else:
            outdata[:] = chunk[:len(outdata)]

    def stream_text_to_audio(self, text):
        self.stop_event.clear()
        worker_thread = threading.Thread(target=self.text_to_speech_worker, args=(text,))
        worker_thread.start()

        with sd.OutputStream(device=self.device_name, samplerate=self.tts.synthesizer.output_sample_rate, 
                             channels=1, callback=self.audio_callback):
            while worker_thread.is_alive() or not self.audio_queue.empty():
                sd.sleep(100)

    def stop_streaming(self):
        self.stop_event.set()

# Example usage
if __name__ == "__main__":
    streamer = CoquiXTTSStreamer(model_path="/Users/maverick/Library/Application Support/tts/tts_models--multilingual--multi-dataset--xtts_v2")
    streamer.stream_text_to_audio("Hello, this is a test of the Coqui XTTS v2 streaming library.")