# mp3totext with Whisper

![Screenshot](https://github.com/user-attachments/assets/97d44670-dde0-4e4f-9846-bcd40e330e60)

## Overview

`mp3totext with Whisper` is a simple web-based tool that converts MP3 audio files to text using OpenAI's Whisper API. The application is built with Flask and Python, providing an easy-to-use interface to transcribe audio into text.

## Requirements

To run this project, you'll need the following dependencies:

- Flask
- OpenAI API
- Werkzeug

You can install these dependencies using:

```bash
pip install flask openai werkzeug
```

Alternatively, install all required dependencies using:
```bash
pip install -r requirements.txt
```

## Usage
To start the application, run the following command:

```bash
python app.py
```

Once the server is running, you can access the web application at http://127.0.0.1:5000.

## Features
Audio-to-Text Conversion: Upload MP3 files and get a transcription using Whisper.
Simple Web Interface: Easy-to-navigate interface built with Flask.

## How It Works
1. Upload an MP3 file.
2. The file is processed via Whisper to extract the text.
3. he transcription is displayed on the screen for easy copy and use.

## Credits
This project was coded using Python and OpenAI's ChatGPT for assistance.



