from RealtimeSTT import AudioToTextRecorder
import wave
import os

wav_file_path:str = os.path.join('test-model-cache','sherpa-onnx','sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8','test_wavs','en.wav')
pcm_file = None


CHUNK_BYTES = 3200
from RealtimeSTT import AudioToTextRecorder


if __name__ == "__main__":
    recorder = AudioToTextRecorder(use_microphone=False)

    with open("audio_stream.pcm", "rb") as audio_file:
        while True:
            chunk = audio_file.read(CHUNK_BYTES)
            if not chunk:
                break
            recorder.feed_audio(chunk, original_sample_rate=16000)

    print(recorder.text())
    recorder.shutdown()

    print(recorder.text())
    recorder.shutdown()
        

