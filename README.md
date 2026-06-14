# STT from [Kolja Beigel](https://github.com/KoljaB/RealtimeSTT)

## specific flavour / edits:
- I want it to run on CPU only - and as fast as possible.
- So I've set it up for `sherpa_onnx_parakeet` rather than its default `faster-whisper`.
- I tried to upload the model files too, but they're too big. I'll leave setup instructions instead. They'll end up in `test-model-cache`.
- I've used parakeet and all the recipes work. I've not tried moonshine so this repo isn't guaranteed to work for it.
- Next, I want to hook it up to a gradio UI for a quick webapp to view the transcription as it happens.

## how to setup:
- setup a virtual environment `python -m venv venv`
- activate it `source venv/bin/activate`
- install the requirements `pip install -r requirements.txt`
- install the models to the `test-model-cache` folder.
  - origino instructions are [here](https://github.com/KoljaB/RealtimeSTT/blob/master/docs/engines/sherpa-onnx.md)
  - my summary is here:
  - open Powershell (whilst the venv is running so that that Python is what we'll use) Try this if it's not running within the venv: ` (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& c:\Users\nombre\Desktop\repos\stt-from-koljabeigel\venv\Scripts\Activate.ps1)`
  - and run this 3-line command. Or one line at a time. It'll download and extract Parakeet so you can use it in the code:
  - ``` Powershell
    New-Item -ItemType Directory -Path test-model-cache\sherpa-onnx -Force
    curl.exe -L -o test-model-cache\sherpa-onnx\sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8.tar.bz2 https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8.tar.bz2
    python -c "import tarfile; tarfile.open(r'test-model-cache\sherpa-onnx\sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8.tar.bz2', 'r:bz2').extractall(r'test-model-cache\sherpa-onnx')"
    ```

