"""
Application for creating Audio Shuffling Sources for a Ross Video Ultrix.
"""

from openpyxl import load_workbook

def main():
    """ Main Function"""

    wb = load_workbook(filename="Sample Data/example_sources.xlsx", data_only=True)
    ws = wb['sources']

    video_ports = ws['E']

    audio_ports = []
    for cell in video_ports[1:]:
        for ch in range(1,17):
            audio_ports.append(cell.value[:-8] + ".audio.ch" + str(ch))

if __name__ == '__main__':
    main()
