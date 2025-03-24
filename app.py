from flask import Flask, render_template, jsonify, request
import speech_recognition as sr
import numpy as np
import parselmouth  # For pitch analysis
import pyttsx3

app = Flask(__name__)

# Initialize Text-to-Speech (TTS) Engine
engine = pyttsx3.init()

def get_pitch(audio_data):
    """Extract fundamental frequency (pitch) from recorded audio."""
    snd = parselmouth.Sound(audio_data)
    pitch = snd.to_pitch()
    pitch_values = pitch.selected_array['frequency']
    pitch_values = pitch_values[pitch_values > 0]  # Remove silence

    if len(pitch_values) > 0:
        avg_pitch = np.mean(pitch_values)
        return round(avg_pitch, 2)  # Return rounded Hz value
    return 0  # No valid pitch found

def adjust_pitch(pitch, gender):
    """Adjust pitch based on male (80-180 Hz) & female (165-255 Hz) range."""
    if pitch < 80:
        adjusted_pitch = 120  # Increase pitch to male range
    elif 80 <= pitch <= 180 and gender == "male":
        adjusted_pitch = pitch  # Keep same for male
    elif 165 <= pitch <= 255 and gender == "female":
        adjusted_pitch = pitch  # Keep same for female
    elif pitch > 255:
        adjusted_pitch = 200  # Decrease pitch
    else:
        adjusted_pitch = 160  # Default safe pitch

    return round(adjusted_pitch, 2)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_voice', methods=['POST'])
def process_voice():
    data = request.json
    gender = data.get("gender", "male")  # Default gender to male

    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

        # Save to a temporary file
        with open("temp_audio.wav", "wb") as f:
            f.write(audio.get_wav_data())

        # Analyze pitch
        input_pitch = get_pitch("temp_audio.wav")
        adjusted_pitch = adjust_pitch(input_pitch, gender)

        return jsonify({"input_pitch": input_pitch, "adjusted_pitch": adjusted_pitch, "gender": gender})

if __name__ == '__main__':
    app.run(debug=True)
