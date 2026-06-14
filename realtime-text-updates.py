
from RealtimeSTT import AudioToTextRecorder


def update(text):
    print("live:", text)


if __name__ == "__main__":
    recorder = AudioToTextRecorder(
        transcription_engine="sherpa_onnx_parakeet",
        model="test-model-cache/sherpa-onnx/sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8",
        device="cpu",
        transcription_engine_options={
            "num_threads": 4,
            "provider": "cpu",
            "model_dir": "test-model-cache/sherpa-onnx/sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8",
        },
        enable_realtime_transcription=True,
        on_realtime_transcription_update=update,
        # realtime_model_type="tiny.en",
    )

    while True:
        print("final:", recorder.text())