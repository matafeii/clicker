import tkinter as tk
from tkinter import messagebox
import pyautogui
import keyboard
import threading
import time

class AutoClicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Clicker")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        
        # Переменные состояния
        self.clicking = False
        self.interval = tk.DoubleVar(value=1000)  # Интервал в миллисекундах по умолчанию
        self.click_thread = None
        
        self.setup_ui()
        self.setup_hotkeys()
        
    def setup_ui(self):
        """Настройка пользовательского интерфейса"""
        # Поле для ввода интервала
        tk.Label(self.root, text="Интервал кликов (мс):", font=("Arial", 10)).pack(pady=10)
        interval_frame = tk.Frame(self.root)
        interval_frame.pack(pady=5)
        self.interval_entry = tk.Entry(interval_frame, textvariable=self.interval, width=10, font=("Arial", 12))
        self.interval_entry.pack(side=tk.LEFT)
        tk.Label(interval_frame, text="мс", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
        # Кнопки
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        self.start_button = tk.Button(button_frame, text="Start", command=self.toggle_clicking,
                                     bg="green", fg="white", font=("Arial", 12), width=10)
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_clicking,
                                    bg="red", fg="white", font=("Arial", 12), width=10)
        self.stop_button.pack(side=tk.LEFT, padx=10)
        
        # Статус
        self.status_label = tk.Label(self.root, text="Status: Stopped", font=("Arial", 12, "bold"),
                                   fg="red")
        self.status_label.pack(pady=20)
    
    def setup_hotkeys(self):
        """Настройка горячих клавиш"""
        keyboard.add_hotkey('f6', self.toggle_clicking)
        keyboard.add_hotkey('f7', self.exit_program)
    
    def toggle_clicking(self):
        """Переключение состояния автокликера (старт/стоп)"""
        if not self.clicking:
            self.start_clicking()
        else:
            self.stop_clicking()
    
    def start_clicking(self):
        """Запуск автокликера"""
        try:
            interval_ms = self.interval.get()
            if interval_ms <= 0:
                messagebox.showerror("Ошибка", "Интервал должен быть больше 0!")
                return
            
            self.clicking = True
            self.update_ui_running()
            
            # Запуск кликов в отдельном потоке
            self.click_thread = threading.Thread(target=self.click_loop, args=(interval_ms / 1000,))
            self.click_thread.daemon = True
            self.click_thread.start()
            
        except tk.TclError:
            messagebox.showerror("Ошибка", "Введите корректный интервал!")
    
    def click_loop(self, interval_sec):
        """Основной цикл кликов"""
        while self.clicking:
            pyautogui.click()  # Левый клик мыши
            time.sleep(interval_sec)
    
    def stop_clicking(self):
        """Остановка автокликера"""
        self.clicking = False
        self.update_ui_stopped()
    
    def update_ui_running(self):
        """Обновление UI при запуске"""
        self.status_label.config(text="Status: Running", fg="green")
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
    
    def update_ui_stopped(self):
        """Обновление UI при остановке"""
        self.status_label.config(text="Status: Stopped", fg="red")
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
    
    def exit_program(self):
        """Выход из программы"""
        self.stop_clicking()
        self.root.quit()

def main():
    """Главная функция запуска приложения"""
    root = tk.Tk()
    app = AutoClicker(root)
    root.protocol("WM_DELETE_WINDOW", app.exit_program)  # Обработка закрытия окна
    root.mainloop()

if __name__ == "__main__":
    main()
