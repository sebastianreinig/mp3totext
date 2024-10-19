from flask import Flask, render_template, request, redirect, url_for
from openai import OpenAI
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['TRANSCRIPT_FOLDER'] = 'transcripted'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['TRANSCRIPT_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    transcription_text = None

    if request.method == 'POST':
        # Überprüfung, ob das Formular vollständig ist
        if 'file' not in request.files or 'api_key' not in request.form:
            return 'Es wurde keine Datei oder kein API Key übermittelt', 400

        file = request.files['file']
        api_key = request.form['api_key']

        if file.filename == '' or api_key == '':
            return 'Es wurde keine Datei oder kein API Key übermittelt', 400

        if file and file.filename.endswith('.mp3'):
            # Datei speichern
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # OpenAI API aufrufen
            #openai.api_key = api_key
            client = OpenAI(api_key=api_key)


            try:
                # MP3-Datei öffnen und Transkription anfordern
                with open(file_path, "rb") as audio_file:
                    transcription = client.audio.transcriptions.create(
                        model="whisper-1",
                        file=audio_file,
                        response_format="text"
                    )

                transcription_text = transcription

                file_name = os.path.splitext(file.filename)[0]  # Dateiname ohne Erweiterung

                # Transkription in Datei speichern
                transcript_path = os.path.join(app.config['TRANSCRIPT_FOLDER'], f"{file_name}.txt")
                with open(transcript_path, 'w') as transcript_file:
                    transcript_file.write(transcription_text)


            except Exception as e:
                return f'Fehler bei der API-Anfrage: {e}', 500

    return render_template('upload.html', transcription=transcription_text)


#if __name__ == '__main__':
    #app.run()
