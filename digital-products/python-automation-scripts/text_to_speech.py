#!/usr/bin/env python3
"""Text to Speech - Convert text files to audio."""

import sys
import os
from pathlib import Path
from datetime import datetime

def text_to_speech(text_file, output_file=None, voice=None):
    text_path = Path(text_file)
    content = text_path.read_text(errors='ignore')
    
    if output_file is None:
        output_file = text_path.stem + '.mp3'
    output_path = Path(output_file)
    
    # Try gTTS (Google TTS) - free, no API key
    try:
        from gtts import gTTS
        tts = gTTS(text=content, lang='en', slow=False)
        tts.save(str(output_path))
        print(f"✓ Saved: {output_path}")
        return
    except ImportError:
        pass
    
    # Try pyttsx3 (offline TTS)
    try:
        import pyttsx3
        engine = pyttsx3.init()
        if voice:
            voices = engine.getProperty('voices')
            for v in voices:
                if voice.lower() in v.name.lower():
                    engine.setProperty('voice', v.id)
                    break
        engine.save_to_file(content, str(output_path))
        engine.runAndWait()
        print(f"✓ Saved: {output_path}")
        return
    except ImportError:
        pass
    
    print("Error: Install gTTS (pip install gtts) or pyttsx3")
    sys.exit(1)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Text to Speech')
    parser.add_argument('file', help='Text file to convert')
    parser.add_argument('--output', '-o', help='Output audio file')
    parser.add_argument('--voice', '-v', help='Voice name (pyttsx3 only)')
    args = parser.parse_args()
    text_to_speech(args.file, args.output, args.voice)