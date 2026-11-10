from ai.recorder import record_audio
from ai.speech_to_text import transcribe_audio
from ai.llm_service import understand_order


def main():

    print("==============================")
    print("       VOICE WAITER AI")
    print("==============================")

    # Step 1: Record customer voice
    audio_file = record_audio()

    # Step 2: Convert voice to text
    customer_text = transcribe_audio(audio_file)

    if not customer_text.strip():
        print("No speech detected!")
        return

    # Step 3: Understand customer order
    print("\nUnderstanding customer order...")

    response = understand_order(customer_text)

    print("\nLlama 3 Response:")
    print(response)


if __name__ == "__main__":
    main()