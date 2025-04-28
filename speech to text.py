# NOTE: This is a VERY basic example using a common library.
# It DOES NOT include speaker diarization or robust session management.
# Real implementation would be much more complex.

import speech_recognition as sr
import time
import threading

# --- Configuration ---
RECORD_DURATION_SECONDS = 3600  # 1 hour limit
LANGUAGE = "en-US"

# --- Global Variables ---
recognizer = sr.Recognizer()
is_recording = False
full_transcript = ""


# --- Functions ---
def record_audio(stop_event):
    """Records audio from the microphone until stop_event is set."""
    global full_transcript
    global is_recording

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print(f"Recording for up to {RECORD_DURATION_SECONDS / 60} minutes... Speak now!")
        is_recording = True

        # Record in chunks to process potentially long audio
        # Note: A real app would handle this more robustly, maybe continuously
        try:
            # record() attempts to listen until silence is detected by default.
            # For continuous recording up to a limit, listen_in_background is better
            # but more complex to manage the full hour and diarization.
            # This simple example just records one long chunk.
            audio_data = recognizer.listen(source, timeout=RECORD_DURATION_SECONDS,
                                           phrase_time_limit=RECORD_DURATION_SECONDS)
            print("Recording finished or timed out.")

            print("Recognizing...")
            try:
                text = recognizer.recognize_google(audio_data, language=LANGUAGE)
                # *** SPEAKER DIARIZATION WOULD NEED TO HAPPEN HERE OR EARLIER ***
                # This basic example assigns everything to "Speaker ?"
                full_transcript += f"Speaker ?: {text}\n"
                print("Transcription Chunk: Speaker ?: ", text)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

        except sr.WaitTimeoutError:
            print("No speech detected within the timeout.")
        except Exception as e:
            print(f"An error occurred during recording: {e}")
        finally:
            is_recording = False
            stop_event.set()  # Signal the main thread to stop


def main():
    """Main function to start and manage recording."""
    global full_transcript

    stop_event = threading.Event()
    record_thread = threading.Thread(target=record_audio, args=(stop_event,))

    print("Starting recording thread...")
    record_thread.start()

    # Keep the main thread alive while recording, maybe add a manual stop option
    try:
        # Wait for the recording thread to finish (up to RECORD_DURATION_SECONDS + buffer)
        record_thread.join(timeout=RECORD_DURATION_SECONDS + 10)
        if record_thread.is_alive():
            print("Stopping recording manually (if needed)...")
            # In a real UI, a button press would set stop_event
            stop_event.set()
            record_thread.join()  # Wait for cleanup

    except KeyboardInterrupt:
        print("Interrupted! Stopping recording...")
        if is_recording:
            stop_event.set()
            record_thread.join()

    print("\n--- Full Transcript ---")
    print(full_transcript if full_transcript else "No transcript generated.")
    print("-----------------------")


if __name__ == "__main__":
    main()