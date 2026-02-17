from assistant import Assistant
from lcd_display import LCDDisplay


def main():
    lcd = LCDDisplay()
    assistant = Assistant(lcd_display=lcd)
    assistant.run()

if __name__ == "__main__":
    main()