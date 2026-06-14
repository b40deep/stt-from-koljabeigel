#main

from RealtimeSTT import AudioToTextRecorder


def process_text(text):
    print(text)


if __name__ == "__main__":
    # recorder = AudioToTextRecorder()
    recorder = AudioToTextRecorder(
    transcription_engine="sherpa_onnx_parakeet",
    model="test-model-cache/sherpa-onnx/sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8",
    device="cpu",
    transcription_engine_options={
        "num_threads": 4,
        "provider": "cpu",
    },
    )

    while True:
        recorder.text(process_text)