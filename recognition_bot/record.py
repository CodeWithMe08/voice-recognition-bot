import speech_recognition as sr
import sounddevice as sd
# import numpy as np
import scipy.io.wavfile as wav


# Constants
FILENAME_FROM_MIC = "RECORDING.WAV"
VOICE_TEXT_FILENAME = "VOICE_AS_TEXT.txt"

# Initialize the recognizer
r = sr.Recognizer()

def recognize_from_file(filename, language='en-US'):
    # Open the file
    with sr.AudioFile(filename) as source:
        # Listen for the data (load audio to memory)
        audio_data = r.record(source)
        # Recognize (convert from speech to text)
        try:
            text = r.recognize_google(audio_data, language=language)
        except sr.UnknownValueError:
            text = ""
        return text

def recognize_from_microphone(file_to_write, duration=5, sample_rate=44100):
    # Record audio from microphone
    audio_recording = sd.rec(duration * sample_rate, samplerate=sample_rate, channels=1, dtype='int32')
    print("Recording Audio")
    sd.wait()
    print("Audio recording complete, playing audio")
    sd.play(audio_recording, sample_rate)
    sd.wait()
    print("Play Audio Complete")
    wav.write(file_to_write, sample_rate, audio_recording)

def save_text_to_file(text, filename):
    with open(filename, 'w') as f:
        f.write(text)


if __name__ == "__main__":
    # Record audio from microphone
    recognize_from_microphone(FILENAME_FROM_MIC)
    # Transcribe audio data from file
    text_from_voice = recognize_from_file(FILENAME_FROM_MIC)
    # Save transcribed text to file
    save_text_to_file(text_from_voice, VOICE_TEXT_FILENAME)

