from RealtimeSTT import AudioToTextRecorder
import wave
import os

wav_file_path:str = os.path.join('test-model-cache','sherpa-onnx','sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8','test_wavs','en.wav')
pcm_file = None


CHUNK_BYTES = 3200

if __name__ == "__main__":
    recorder = AudioToTextRecorder(use_microphone=False,)

    with open("audio_chunk.pcm", "rb") as audio_file:
        recorder.feed_audio(audio_file.read(), original_sample_rate=16000)

    print(recorder.text())
    recorder.shutdown()
        

