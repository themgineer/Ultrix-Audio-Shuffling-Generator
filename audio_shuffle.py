import csv
import PySimpleGUI as gui


class OutputEmpty(Exception):
    pass


class InputEmpty(Exception):
    pass


# Function that runs if input file is detected as a list instead of a csv.
# It recurses through the sources list and appends the channel number to it.
def run_as_list(channels, sources, output, out_file):
    for i in sources:
        for j in range(1, channels + 1):
            output.append([i + " " + "CH" + f"{j:02d}"])

    return(write_list(get_filename(out_file), output))


# Function that runs if input file is detected as a csv instead of a list.
def run_as_dict(channels, sources, output, out_file):
    fields = ["Name", "Description", "Video"]
    for f in range(1, channels+1):
        fields.append("Audio " + str(f))

    for i in sources:
        for j in range(1, channels + 1):
            temp = [i + " " + "CH" + f"{j:02d}"]
            temp.extend(["", ""])
            for k in range(1, channels + 1):
                temp.append(sources[i] + ".audio.ch" + str(j))
            tempDict = dict(zip(fields, temp))
            output.append(tempDict)

    return(write_dict(get_filename(out_file), output, fields))


# Function designed to output the list to a file.
def write_list(filename, list):
    with open(filename, 'w', newline='') as out:
        writer = csv.writer(out)
        writer.writerows(list)
    return("Output successful!")


# Function designed to generate csv that matches Ultrix database layout.
def write_dict(out_file, out_dict, fields):
    with open(out_file, 'w', newline='') as out:
        writer = csv.DictWriter(out, fieldnames=fields)
        writer.writeheader()
        writer.writerows(out_dict)
    return("Output successful!")


# Function that checks if an output path or filename was provided.
# If not, uses default 'shuffled_audio.csv'.
def get_filename(out_file):
    if out_file.split(".")[-1] != "csv":
        out_file += ".csv"

    return out_file


def process_file(list, channels, out_file):
    # Initialize output list
    output = []

    # Main function that attempts to parse an input list or csv.
    # If it finds a path or filename, it uses it and attempts to process it.
    # If it doesn't find a path or filename,
    # it will attempt to use 'sources.txt', but will fail if it cannot find it.

    try:
        if list == "":
            raise InputEmpty()
        elif out_file == "":
            raise OutputEmpty()

        sources = {}
        with open(list, mode='r') as src:
            read = csv.reader(src)
            sources = {rows[0]: rows[1] for rows in read}
        dict_return = run_as_dict(channels, sources, output, out_file)
        return(dict_return)

    except InputEmpty:
        return("Source list needs a name.")
    except OutputEmpty:
        return("Output file needs a name.")
    except Exception:
        try:
            sources = []
            source_file = open(list, 'r')
            while True:
                line = source_file.readline()

                if not line:
                    break
                sources.append(line.strip())
            source_file.close()
            return(run_as_list(channels, sources, output, out_file))

        except Exception:
            return("Input file cannot be found.")


def main():

    # GUI Theme
    gui.theme('reddit')
    gui.theme_background_color("#D9D6D1")
    gui.theme_text_element_background_color("#D9D6D1")
    gui.theme_button_color((None, "#D42E12"))

    # GUI Layout
    layout = [[gui.Text('Source List'),
               gui.Input(key='source_file'),
               gui.FileBrowse()],
              [gui.Text('Audio Channels'),
               gui.Combo((2, 4, 8, 16),
                         key='channels',
                         default_value=16,
                         readonly=True)],
              [gui.HorizontalSeparator()],
              [gui.Text('Output File'),
               gui.Input(key='out_file'),
               gui.FileBrowse()],
              [gui.Text(text='',
                        key='out_message',
                        justification='center',
                        size=(50, 1))],
              [gui.Column([[gui.Button('Go')]],
                          expand_x=True,
                          element_justification='l'),
               gui.Column([[gui.Exit()]],
                          element_justification='r')]]

    # Create the GUI Window
    window = gui.Window('Ultrix Audio Shuffle', layout)

    # Read the content of the window
    while True:
        event, values = window.Read(timeout=5000)

        if event == 'Exit' or event == gui.WIN_CLOSED:
            break
        elif event == 'Go':
            message = process_file(values['source_file'],
                                   values['channels'],
                                   values['out_file'])
            window['out_message'].expand(expand_x=True,
                                         expand_y=False,
                                         expand_row=True)
            window['out_message'].update(message)
        else:
            window['out_message'].update('')
    window.close()


if __name__ == '__main__':
    main()
