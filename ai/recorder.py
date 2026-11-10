import sounddevice as sd
from scipy.io.wavfile import write


def record_audio(duration=5):
    sample_rate = 16000
    print(sd.query_devices())

    print("Speak now...")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()
    import numpy as np
    print("Max volume:", np.max(np.abs(audio)))


    write("customer_voice.wav", sample_rate, audio)

    print("Recording saved successfully!")

    return "customer_voice.wav"