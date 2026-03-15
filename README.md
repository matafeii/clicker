# Auto Clicker для Windows

## Установка зависимостей

```bash
pip install pyautogui keyboard pyinstaller
```

## Запуск

```bash
python main.py
```

## Использование

1. Введите интервал кликов в миллисекундах (например, 500 для 2 кликов в секунду)
2. **F6** - Старт/Стоп автокликера
3. **F7** - Выход из программы
4. Также можно использовать кнопки Start/Stop

## Горячие клавиши

- **F6** - Запуск/Остановка автокликера
- **F7** - Выход из программы
- **Закрытие окна** - Безопасный выход

## Сборка в .exe (самое простое решение)

Выполните команду в терминале VS Code:

```bash
python -m PyInstaller --onefile --windowed --name AutoClicker main.py
```

**Или:**

```bash
py -m PyInstaller --onefile --windowed --name AutoClicker main.py
```

**Готовый .exe файл будет находиться в:**

```
dist/AutoClicker.exe
```

**Альтернативно используйте build.bat** (может потребовать добавления PyInstaller в PATH).

## Требования

- Windows 10/11
- Python 3.8+
- PyInstaller для сборки .exe
