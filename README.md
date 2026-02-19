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

## Installation
### 1. Install Ollama and pull the model
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen2.5:1.5b
```

### 2. Clone the repository
```bash
git clone https://github.com/Zyziek055/VoiceAssistant.git
cd VoiceAssistant
```

### 3. Install system dependencies
```bash
sudo apt install portaudio19-dev -y
```

### 4. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the assistant
```bash
python main.py
```


> **Note:** `rpi-lcd` is a Raspberry Pi specific library for controlling the 16x2 LCD display over I2C. Make sure I2C is enabled on your Pi (`sudo raspi-config` → Interface Options → I2C).

You may also need to install `portaudio` for microphone support:
```bash
sudo apt install portaudio19-dev -y
pip install pyaudio
```

### 5. Run the assistant
```bash
python main.py
```

Press **Enter** to start speaking, or type `quit` to exit.
