import pyperclip
import tkinter as tk
from tkinter import messagebox
import keyboard
import sys
import os
import winreg

class ClipboardManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Clipboard Manager")
        self.root.geometry("400x500")
        self.root.attributes("-topmost", True) 

        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)

        self.clipboard_history = []
        self.last_copied_text = ""
        
        self.title_label = tk.Label(root, text="Clipboard History", font=("Arial", 14, "bold"), pady=10)
        self.title_label.pack()

        self.history_listbox = tk.Listbox(root, font=("Arial", 10), selectmode=tk.SINGLE)
        self.history_listbox.pack(expand=True, fill="both", padx=10, pady=5)

        self.history_listbox.bind("<Double-Button-1>", self.copy_selected_item)

        self.info_label = tk.Label(root, text="Kopyalamak istediğin metne çift tıkla.", fg="gray")
        self.info_label.pack(pady=5)
        
        self.quit_button = tk.Button(root, text="Uygulamayı Tamamen Kapat", command=self.quit_app, bg="#ffcccc")
        self.quit_button.pack(pady=5)

        self.monitor_clipboard()
        self.hide_window()
        
        self.add_to_startup()

    def add_to_startup(self):
        """Uygulamayı Windows başlangıcına ekler."""
        try:
            if getattr(sys, 'frozen', False):
                app_path = sys.executable
            else:
                app_path = os.path.abspath(__file__)

            key_val = r"Software\Microsoft\Windows\CurrentVersion\Run"
            app_name = "MyClipboardManager"

            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_val, 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, app_path)
            winreg.CloseKey(key)
        except Exception as e:
            print(f"Startup hatası: {e}")

    def monitor_clipboard(self):
        try:
            current_text = pyperclip.paste()
            if current_text and current_text != self.last_copied_text:
                self.last_copied_text = current_text
                self.clipboard_history.insert(0, current_text)
                if len(self.clipboard_history) > 20:
                    self.clipboard_history.pop() 
                self.update_listbox_display()
        except Exception as e:
            print(f"Hata: {e}")
        
        self.root.after(1000, self.monitor_clipboard)
    
    def update_listbox_display(self):
        self.history_listbox.delete(0, tk.END)
        for item in self.clipboard_history:
            display_text = item.replace("\n", " ")
            if len(display_text) > 50:
                display_text = display_text[:47] + "..."
            self.history_listbox.insert(tk.END, display_text)
        
    def copy_selected_item(self, event):
        selection_index = self.history_listbox.curselection()
        if selection_index:
            index = selection_index[0]
            full_text = self.clipboard_history[index]
            pyperclip.copy(full_text)
            self.last_copied_text = full_text
            self.hide_window() 

    def hide_window(self):
        self.root.withdraw()

    def show_window(self):
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()

    def change_window(self):
        if self.root.state() == 'normal':
            self.hide_window()
        else:
            self.show_window()

    def quit_app(self):
        self.root.destroy()
        sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ClipboardManager(root=root)
    
    keyboard.add_hotkey('ctrl+space', app.change_window)
    
    root.mainloop()