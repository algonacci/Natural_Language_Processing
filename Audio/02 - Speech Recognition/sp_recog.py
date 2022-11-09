import speech_recognition as sr
import tkinter as tk

print("Mulai Mendengarkan")
# print(sr.Microphone.list_microphone_names())

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        speech = r.listen(source)
        try:
            q = r.recognize_google(speech, language="id")
            print(q)
            return q
        except sr.UnknownValueError:
            print("=== Belum ada suara lagi ===")
            return "(DARI SISTEM) Menunggu suara masuk."
        except sr.RequestError:
            print("=== Maaf ada Request Error ===")
            return "(DARI SISTEM) Ada Error!"

def continuation():
    start = True
    try:
        while start:
            q = speech_to_text()
            if q:
                win = tk.Tk()
                win.title("Speech Recognition")
                tk.Label(win,
                        text=q,
                        font=("Times New Roman", 20),
                        background="white").grid(column=0, row=0)
                win.after(3000, lambda: win.destroy())
                win.mainloop()
                continue

            elif q == "udahan":
                break
    except KeyboardInterrupt:
        print("Dadah, sampai jumpa lagi!")
        pass

if __name__ == "__main__":
    continuation()