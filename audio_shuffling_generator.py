"""
This creates a GUI that will easily generate names and port labels
for Audio Shuffling Sources for an Ross Video Ultrix.
"""

import os
import sys
import csv
import PySimpleGUI as gui


class OutputEmpty(Exception):
    """Creates custom OutputEmpty Exception"""


class InputEmpty(Exception):
    """Creates custom InputEmpty Exception"""


class InvalidGroup(Exception):
    """Creates custom InvalidGroup Exception"""


class UnknownError(Exception):
    """Catches any other weird errors"""


def img_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Function that runs if input file is detected as a list instead of a csv.
# It recurses through the sources list and appends the channel number to it.
def run_as_list(channels, group_step, sources, output, out_file):
    """"Processes input file as a list of names."""

    if group_step == 1:
        for i in sources:
            for j in range(1, channels + 1):
                output.append([f"{i} CH{j}"])
    else:
        for i in sources:
            for j in range(1, channels + 1, group_step):
                output.append([f"{i} CH{j}-{j+(group_step - 1)}"])

    out_file = get_filename(out_file)

    return write_list(out_file, output)


def run_as_list_leading_zero(channels, group_step, sources, output, out_file):
    """"Processes input file as a list with leading zeroes"""

    if group_step == 1:
        for i in sources:
            for j in range(1, channels + 1):
                output.append([f"{i} CH{j:02d}"])
    else:
        for i in sources:
            for j in range(1, channels + 1, group_step):
                output.append([f"{i} CH{j:02d}-{j+(group_step - 1):02d}"])

    out_file = get_filename(out_file)

    return write_list(out_file, output)


# Function that runs if input file is detected as a csv instead of a list.
def run_as_dict(channels, group_step, sources, output, out_file):
    """Processes input file as a CSV"""

    fields = ["Name", "Description", "Video"]
    for f in range(1, channels+1):
        fields.append(f"Audio {f}")

    if group_step == 1:
        for i in sources:
            for j in range(1, channels + 1):
                temp = [f"{i} CH{j}"]
                temp.extend(["", ""])
                for _ in range(1, channels + 1):
                    temp.append(f"{sources[i]}.audio.ch{j}")
                temp_dict = dict(zip(fields, temp))
                output.append(temp_dict)
    else:
        for i in sources:
            for j in range(1, channels + 1, group_step):
                temp = [f"{i} CH{j}-{j + (group_step - 1)}"]
                temp.extend(["", ""])
                for _ in range(1, channels + 1, group_step):
                    for m in range(j, j + group_step):
                        temp.append(f"{sources[i]}.audio.ch{m}")
                temp_dict = dict(zip(fields, temp))
                output.append(temp_dict)

    out_file = get_filename(out_file)

    return write_dict(out_file, output, fields)


def run_as_dict_leading_zero(channels, group_step, sources, output, out_file):
    """Processes input file as CSV with leading zeroes"""

    fields = ["Name", "Description", "Video"]
    for f in range(1, channels+1):
        fields.append(f"Audio {f}")

    if group_step == 1:
        for i in sources:
            for j in range(1, channels + 1):
                temp = [f"{i} CH{j:02d}"]
                temp.extend(["", ""])
                for _ in range(1, channels + 1):
                    temp.append(f"{sources[i]}.audio.ch{j}")
                temp_dict = dict(zip(fields, temp))
                output.append(temp_dict)
    else:
        for i in sources:
            for j in range(1, channels + 1, group_step):
                temp = [f"{i} CH{j:02d}-{j + (group_step - 1):02d}"]
                temp.extend(["", ""])
                for _ in range(1, channels + 1, group_step):
                    for m in range(j, j + group_step):
                        temp.append(f"{sources[i]}.audio.ch{m}")
                temp_dict = dict(zip(fields, temp))
                output.append(temp_dict)

    out_file = get_filename(out_file)

    return write_dict(out_file, output, fields)


def write_list(filename, output_list):
    """Function designed to output the list to a file."""
    with open(filename, 'w', encoding='UTF-8', newline='') as out:
        writer = csv.writer(out)
        writer.writerows(output_list)
    return "Output successful!"


def write_dict(out_file, out_dict, fields):
    """Function designed to generate csv that matches Ultrix database layout."""
    with open(out_file, 'w', encoding='UTF-8', newline='') as out:
        writer = csv.DictWriter(out, fieldnames=fields)
        writer.writeheader()
        writer.writerows(out_dict)
    return "Output successful!"


def get_filename(out_file):
    """
    Function that checks if an output path or filename was provided.
    If not, uses default 'shuffled_audio.csv'.
    """

    if out_file.split(".")[-1] != "csv":
        out_file += ".csv"

    return out_file


def process_file(source_list, channels, grouping, out_file, leading_zero):
    """Function that processes in the input file"""
    # Initialize output list
    output = []
    group_dict = {"Mono": 1, "Stereo": 2, "Quad": 4, "Octo": 8}

    if grouping in group_dict:
        group_step = group_dict[grouping]
    else:
        raise InvalidGroup()

    if group_step > channels:
        group_step = channels

    # Main function that attempts to parse an input list or csv.
    # If it finds a path or filename, it uses it and attempts to process it.
    # If it doesn't find a path or filename,
    # it will attempt to use 'sources.txt', but will fail if it cannot find it.

    try:
        if source_list == "" or source_list is None:
            raise InputEmpty()
        elif out_file == "" or out_file is None:
            raise OutputEmpty()

        sources = {}
        with open(source_list, mode='r', encoding='UTF-8') as src:
            read = csv.reader(src)
            sources = {rows[0]: rows[1] for rows in read}

        if leading_zero:
            dict_return = run_as_dict_leading_zero(
                channels, group_step, sources, output, out_file)
        else:
            dict_return = run_as_dict(
                channels, group_step, sources, output, out_file)
        return dict_return

    except InvalidGroup:
        return "Invalid Audio Grouping Selection"
    except InputEmpty:
        return "Source list needs a name."
    except OutputEmpty:
        return "Output file needs a name."
    except IndexError:
        try:
            sources = []

            with open(source_list, mode='r', encoding='UTF-8') as src:
                for line in src:
                    if line[0] == '\n' or line[0] == '#':
                        continue
                    sources.append(line.strip())

            if leading_zero:
                return_list = run_as_list_leading_zero(channels,
                                                       group_step,
                                                       sources,
                                                       output,
                                                       out_file)
            else:
                return_list = run_as_list(channels,
                                          group_step,
                                          sources,
                                          output,
                                          out_file)

            return return_list

        except UnknownError:
            return "Unknown error occurred."

    except FileNotFoundError:
        return "Input file cannot be found."


def get_folder(path):
    """Function that pulls the folder path from input file"""
    if path == "":
        out_path = ""
    else:
        path_list = path.split("/")
        path_list[-1] = f"{path_list[-1].split('.')[0]}_shuffled.csv"
        out_path = "/".join(path_list)

    return out_path


def main():
    """Main function"""

    icon_path = img_resource_path("icon/Ultrix_U.ico")

    # GUI Theme
    gui.theme('reddit')
    gui.theme_background_color("#D9D6D1")
    gui.theme_text_element_background_color("#D9D6D1")
    gui.theme_input_background_color("#EFEFEF")
    gui.theme_button_color((None, "#D42E12"))

    # GUI Layout
    layout = [[gui.Text('Source List'),
               gui.Input(key='source_file',
                         enable_events=True,
                         focus=True),
               gui.FileBrowse()],
              [gui.Text('Audio Channels'),
               gui.Combo((2, 4, 8, 16),
                         key='channels',
                         default_value=16,
                         readonly=True),
               gui.Text('Audio Grouping',
                        pad=((15, 0), (0, 0))),
               gui.Combo(('Mono', 'Stereo', 'Quad', 'Octo'),
                         key='grouping',
                         default_value='Mono',
                         readonly=True),
               gui.Checkbox(text='Leading Zeroes',
                            key='leading_zero',
                            pad=((15, 0), (0, 0)),
                            background_color='#D9D6D1',
                            checkbox_color='#FFFFFF')],
              [gui.HorizontalSeparator()],
              [gui.Text('Output File'),
               gui.Input(key='out_file'),
               gui.FileBrowse()],
              [gui.Column([[gui.Button('Go')]],
                          element_justification='l'),
               gui.Text(text='',
                        key='out_message',
                        justification='center',
                        size=(30, 1),
                        expand_x=True,),
               gui.Column([[gui.Exit()]],
                          element_justification='r')]]

    # Create the GUI Window
    window = gui.Window('Ultrix Audio Shuffling Generator', layout,
                        icon=icon_path)

    # Read the content of the window
    while True:
        event, values = window.Read(timeout=5000)

        if event == 'Exit' or event == gui.WIN_CLOSED:
            break
        elif event == 'Go':
            message = process_file(values['source_file'],
                                   values['channels'],
                                   values['grouping'],
                                   values['out_file'],
                                   values['leading_zero'])
            window['out_message'].update(message)
        elif event == "source_file":
            window['out_file'].update(get_folder(values['source_file']))
        else:
            window['out_message'].update('')
    window.close()


if __name__ == '__main__':
    main()
