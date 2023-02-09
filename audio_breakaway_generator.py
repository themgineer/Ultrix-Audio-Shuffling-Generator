import os
import csv
import PySimpleGUI as gui


class OutputEmpty(Exception):
    pass


class InputEmpty(Exception):
    pass


class InvalidGroup(Exception):
    pass


def icon_path(image):
    root = os.path.dirname(__file__)
    return os.path.join(root, image)


# Function that runs if input file is detected as a list instead of a csv.
# It recurses through the sources list and appends the channel number to it.
def run_as_list(channels, group_step, sources, output, out_file):

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

def run_as_list_LZ(channels, group_step, sources, output, out_file):

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
    fields = ["Name", "Description", "Video"]
    for f in range(1, channels+1):
        fields.append(f"Audio {f}")

    if group_step == 1:
        for i in sources:
            for j in range(1, channels + 1):
                temp = ([f"{i} CH{j}"])
                temp.extend(["", ""])
                for k in range(1, channels + 1):
                    temp.append(f"{sources[i]}.audio.ch{j}")
                tempDict = dict(zip(fields, temp))
                output.append(tempDict)
    else:
        for i in sources:
            for j in range(1, channels + 1, group_step):
                temp = [f"{i} CH{j}-{j + (group_step - 1)}"]
                temp.extend(["", ""])
                for k in range(1, channels + 1, group_step):
                    for m in range(j, j + group_step):
                        temp.append(f"{sources[i]}.audio.ch{m}")
                tempDict = dict(zip(fields, temp))
                output.append(tempDict)

    out_file = get_filename(out_file)

    return write_dict(out_file, output, fields)

def run_as_dict_LZ(channels, group_step, sources, output, out_file):
    fields = ["Name", "Description", "Video"]
    for f in range(1, channels+1):
        fields.append(f"Audio {f}")

    if group_step == 1:
        for i in sources:
            for j in range(1, channels + 1):
                temp = ([f"{i} CH{j:02d}"])
                temp.extend(["", ""])
                for k in range(1, channels + 1):
                    temp.append(f"{sources[i]}.audio.ch{j}")
                tempDict = dict(zip(fields, temp))
                output.append(tempDict)
    else:
        for i in sources:
            for j in range(1, channels + 1, group_step):
                temp = [f"{i} CH{j:02d}-{j + (group_step - 1):02d}"]
                temp.extend(["", ""])
                for k in range(1, channels + 1, group_step):
                    for m in range(j, j + group_step):
                        temp.append(f"{sources[i]}.audio.ch{m}")
                tempDict = dict(zip(fields, temp))
                output.append(tempDict)

    out_file = get_filename(out_file)

    return write_dict(out_file, output, fields)


# Function designed to output the list to a file.
def write_list(filename, list):
    with open(filename, 'w', newline='') as out:
        writer = csv.writer(out)
        writer.writerows(list)
    return "Output successful!"


# Function designed to generate csv that matches Ultrix database layout.
def write_dict(out_file, out_dict, fields):
    with open(out_file, 'w', newline='') as out:
        writer = csv.DictWriter(out, fieldnames=fields)
        writer.writeheader()
        writer.writerows(out_dict)
    return "Output successful!"


# Function that checks if an output path or filename was provided.
# If not, uses default 'shuffled_audio.csv'.
def get_filename(out_file):
    if out_file.split(".")[-1] != "csv":
        out_file += ".csv"

    return out_file


def process_file(list, channels, grouping, out_file, LZ):
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
        if list == "" or list is None:
            raise InputEmpty()
        elif out_file == "" or out_file is None:
            raise OutputEmpty()

        sources = {}
        with open(list, mode='r') as src:
            read = csv.reader(src)
            sources = {rows[0]: rows[1] for rows in read}
        
        if LZ:
            dict_return = run_as_dict_LZ(
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

            with open(list, mode='r') as src:
                for line in src:
                    if line[0] == '\n' or line[0] == '#':
                        continue
                    sources.append(line.strip())

            if LZ:
                return_list = run_as_list_LZ(channels,
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

        except Exception:
            return "Unknown error occurred."

    except FileNotFoundError:
        return "Input file cannot be found."


def get_folder(path):
    if path == "":
        out_path = ""
    else:
        path_list = path.split("/")
        path_list[-1] = f"{path_list[-1].split('.')[0]}_shuffled.csv"
        out_path = "/".join(path_list)

    return out_path


def main():

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
                            key='LZ',
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
                        icon=icon_path("icon/Ultrix_U.ico"))

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
                                   values['LZ'])
            window['out_message'].update(message)
        elif event == "source_file":
            window['out_file'].update(get_folder(values['source_file']))
        else:
            window['out_message'].update('')
    window.close()


if __name__ == '__main__':
    main()
