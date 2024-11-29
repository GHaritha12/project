import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
from gtts import gTTS
import os
engine = pyttsx3.init()
def offline_tts():
    text = text_input.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("Warning", "No text entered!")
def save_offline_audio():
    text = text_input.get("1.0", tk.END).strip()
    if text:
        save_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                 filetypes=[("Audio Files", "*.mp3")])
        if save_path:
            engine.save_to_file(text, save_path)
            engine.runAndWait()
            messagebox.showinfo("Success", "Audio file saved successfully!")
    else:
        messagebox.showwarning("Warning", "No text entered!")
def online_tts():
    text = text_input.get("1.0", tk.END).strip()
    if text:
        try:
            tts = gTTS(text=text, lang='en')
            tts.save("temp_audio.mp3")
            os.system("start temp_audio.mp3" if os.name == "nt" else "open temp_audio.mp3")
        except Exception as e:
            messagebox.showerror("Error", f"Error with gTTS: {e}")
    else:
        messagebox.showwarning("Warning", "No text entered!")
def save_online_audio():
    text = text_input.get("1.0", tk.END).strip()
    if text:
        save_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                 filetypes=[("Audio Files", "*.mp3")])
        if save_path:
            try:
                tts = gTTS(text=text, lang='en')
                tts.save(save_path)
                messagebox.showinfo("Success", "Audio file saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error with gTTS: {e}")
    else:
        messagebox.showwarning("Warning", "No text entered!")
root = tk.Tk()
root.title("Text-to-Speech Application")
text_label = tk.Label(root, text="Enter Text Below:", font=("Arial", 14))
text_label.pack(pady=10)
text_input = tk.Text(root, wrap="word", width=50, height=10, font=("Arial", 12))
text_input.pack(pady=10)
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

offline_button = tk.Button(button_frame, text="Speak (Offline)", command=offline_tts, width=15)
offline_button.grid(row=0, column=0, padx=5, pady=5)

save_offline_button = tk.Button(button_frame, text="Save (Offline)", command=save_offline_audio, width=15)
save_offline_button.grid(row=0, column=1, padx=5, pady=5)

online_button = tk.Button(button_frame, text="Speak (Online)", command=online_tts, width=15)
online_button.grid(row=1, column=0, padx=5, pady=5)

save_online_button = tk.Button(button_frame, text="Save (Online)", command=save_online_audio, width=15)
save_online_button.grid(row=1, column=1, padx=5, pady=5)

exit_button = tk.Button(root, text="Exit", command=root.quit, width=15, bg="red", fg="white")
exit_button.pack(pady=10)
root.mainloop()