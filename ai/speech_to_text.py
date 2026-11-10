from faster_whisper import WhisperModel


def transcribe_audio(audio_file):

    print("Converting voice to text...")

    model = WhisperModel(
        "small",
        device="cpu",
        compute_type="int8"
    )

    segments, info = model.transcribe(
        audio_file,
        language="ar"
    )

    text = ""

    for segment in segments:
        text += segment.text

    print("Customer said:", text)

    return text