"""
Скрипт для озвучивания введенного текста
Используется синтезатор речи Яндекса. Для проигрывания потока нужен mplayer.
Можно заменить на свою программу. Для запуска: python yandex-speech-to-text.py
"""

import subprocess


url = 'http://tts.voicetech.yandex.net/generate?'

# текст для озвучивания
text = input("Введите текст для озвучивания: ")

# получаем звук по ссылке и проигрываем с помощью mplayer
subprocess.run(["mplayer", "-really-quiet", "-nolirc", 'http://tts.voicetech.yandex.net/tts?format=mp3&quality=hi&lang=ru_RU&text='+text])
