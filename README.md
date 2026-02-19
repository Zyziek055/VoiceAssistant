# Local Pi Assistant – Offline Raspberry Pi Voice Assistant

This is a privacy focused voice assistant running locally on my Raspberry Pi 5. I used OpenAI WhisperAI for speech-to-text and Ollama LLM for responses, which are displayed on 16x2 LCD screen.


## Built With
- Ollama running a lightweight LLM (Qwen2.5 1.5B)
- OpenAI Whisper (tiny model) for speech-to-text
- Raspberry Pi 5
- 16x2 LCD display
- The cheapest USB microphone from amazon.

## Features
- 100% offline – no cloud or API keys required
- Optimized for Raspberry Pi 5 performance
- Conversation memory (remembers last 10 messages)
- LCD shows responses and system states like “Listening…”, “Processing…” and “Thinking…”
