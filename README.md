для того чтобы запустить скрипт сначала установите зависимость

'pip install -r requirements.txt'


После, скомперируй текст командой в .exe
'pyinstaller --onefile EhoAiForCreatePictures_bot.py'

.exe файл будет в папке dist

перед запуском '.exe' , удостовертись что рядом лежит файл 'config_2.yaml'
в котором описаны настройк бота
пример конфига - файл'config.yaml'