import sys
import speech_recognition as sr
import whisper
import ollama
import ssl
from lcd_display import LCDDisplay

ssl._create_default_https_context = ssl._create_unverified_context

class Assistant:
    def __init__(self, lcd_display = None):
        self.lcd = lcd_display
        self.ollama_host = "http://localhost:11434"
        self.ollama_model = "qwen2.5:1.5b"
        self.whisper_model = "tiny"
        self.r = sr.Recognizer()
        self.conversation_history = []
        self.max_history_length = 10


        print(f"Initializing Whipser {self.whisper_model} model...")

        try:
            self.model = whisper.load_model(self.whisper_model)
            print("Whisper model loaded.")
        except Exception as e:
            print(f"Error occured while loading whisper: {e}")
            sys.exit(1)

        self.ollama_client = ollama.Client(host=self.ollama_host)

        print("Voice assistant initialized successfully.")

    def record_audio(self):
        with sr.Microphone() as source:
            print("Reducing noise...")
            self.lcd.write_status("Reducing noise...")

            self.r.adjust_for_ambient_noise(source, duration=1)

            print("Speak now!")
            self.lcd.write("Speak now!")

            audio = self.r.listen(source)
            self.lcd.write_status("Processing using whisper")

            print("Processing using whisper..")

            try:
                text = self.r.recognize_whisper(audio, model=self.whisper_model, language="english")
                print(f"\nRecognized text: {text}")

                return text
            except Exception as e:
                print(f"Error: {e}")

    def ask_ollama(self, prompt):
        if not prompt:
            return ""

        print("Thinking...")
        self.lcd.write_status("Thinking")

        system_prompt = {
            "role": "system",
            "content": (
                "Your name is Pi. "
                "You are a voice assistant. "
                "Respond in ONE short sentence. "
                "Maximum 15 words. "
                "Never exceed the word limit."
            )
        }

        self.conversation_history.append({
            "role": "user",
            "content": prompt
        })

        messages = [system_prompt] + self.conversation_history[-self.max_history_length:]


        try:
            response = self.ollama_client.chat(
                model = self.ollama_model,
                messages=messages
            )

            assistant_response = response['message']['content']

            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_response
            })

            print(f"Assisant response: {assistant_response}")
            self.lcd.scroll_text(assistant_response)

            return assistant_response

        except Exception as e:
            error_msg = "Sorry, I encountered an error. Please try again."
            print(f"Assistant response: {error_msg} + {e}\n")

            return error_msg

    def run(self):
        try:
            while True:
                command = input("Press ENTER to speak or type 'quit' to quit: ").strip().lower()

                if command == "quit":
                    print("bye bye")
                    self.lcd.write("Bye, bye!")

                    self.lcd.clear()
                    break
                elif command == "":
                    text = self.record_audio()

                    if text:
                        response = self.ask_ollama(text)
                else:
                    print("Uknown command.")

        except KeyboardInterrupt:
            print("bye bye ")
            self.write("Bye bye!")
            self.lcd.clear()
        except Exception as e:
            print("Error occured")








