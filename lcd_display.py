import threading
import time
from rpi_lcd import LCD


class LCDDisplay:

    def __init__(self, width=16, height=2):
        self.animating = False
        self.animation_thread = None
        self.lock = threading.Lock()

        self.lcd = LCD()
        self.width = width
        self.height = height
        self.clear()

    def clear(self):
        with self.lock:
            self.lcd.clear()

    def write(self, text, line=1):
        self.stop_animation()
        with self.lock:
            self.lcd.clear()
            self.lcd.text(text[:self.width], line)

    def write_status(self, status_text):
        self.stop_animation()
        self.animating = True

        if len(status_text) < 14:

            base_text = status_text[:self.width - 3]

            with self.lock:
                self.lcd.clear()
                self.lcd.text(base_text, 1)

            def animate():
                dots_list = ["", ".", "..", "..."]
                while self.animating:
                    for dots in dots_list:
                        if not self.animating:
                            break

                        with self.lock:
                            self.lcd.text(
                                (base_text + dots).ljust(self.width),
                                1
                            )

                        time.sleep(0.6)

        else:

            words = status_text.split()

            if len(words) >= 2:
                line1 = words[0][:self.width]
                line2_base = " ".join(words[1:])[:self.width - 3]
            else:
                mid = len(status_text) // 2
                line1 = status_text[:mid][:self.width]
                line2_base = status_text[mid:][:self.width - 3]

            with self.lock:
                self.lcd.clear()
                self.lcd.text(line1.ljust(self.width), 1)
                self.lcd.text(line2_base, 2)

            def animate():
                dots_list = ["", ".", "..", "..."]
                while self.animating:
                    for dots in dots_list:
                        if not self.animating:
                            break

                        with self.lock:
                            self.lcd.text(
                                (line2_base + dots).ljust(self.width),
                                2
                            )

                        time.sleep(0.6)

        self.animation_thread = threading.Thread(target=animate)
        self.animation_thread.daemon = True
        self.animation_thread.start()

    def stop_animation(self):
        self.animating = False
        if self.animation_thread is not None:
            self.animation_thread.join()
            self.animation_thread = None

    def scroll_text(self, text, line=2, delay=0.35):
        self.stop_animation()

        with self.lock:
            self.lcd.clear()
            self.lcd.text("Pi:", 1)

        if len(text) <= self.width:
            with self.lock:
                self.lcd.text(text, line)
            return

        text = "     " + text + "     "

        for i in range(len(text) - self.width + 1):
            with self.lock:
                self.lcd.text(text[i:i + self.width], line)
            time.sleep(delay)