Use the following `pyinstaller` command to build as a single Windows executable:

`pyinstaller --onefile --windowed --icon='Icons\\Ultrix_U.ico' --add-data='Icons;Icons' --name='Ultrix Audio Shuffling Generator' --upx-dir='..\\upx-5.0.1-win64' audio_shuffling_generator.py`
