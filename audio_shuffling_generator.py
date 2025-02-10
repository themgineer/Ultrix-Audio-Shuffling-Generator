"""
This creates a GUI that will easily generate names and port labels
for Audio Shuffling Sources for a Ross Video Ultrix.
"""

import os
import sys
import csv
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

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

    def select_source_file():
        # Specify file types
        filetype_list = (('csv files', '*.csv'),
                         ('text files', '*.txt'),
                         ('All files', '*.*'))

        # Create and open file selection dialog
        f = fd.askopenfile(filetypes=filetype_list)

        # Insert selected filename into source and output entry fields
        if f:
            filename = f.name
        else:
            filename = ""
        
        source_entry.delete(0, tk.END)
        output_entry.delete(0, tk.END)
        source_entry.insert(0, filename)
        output_entry.insert(0, get_folder(filename))

    def update_output(event=None):
        output_entry.delete(0, tk.END)
        output_entry.insert(0, get_folder(source_file.get()))

    def press_go():
        message = process_file(source_file.get(),
                               channels.get(),
                               grouping.get(),
                               output_file.get(),
                               leading_zero.get())
        status_message.set(message)

    icon_path = img_resource_path("icon/Ultrix_U.ico")

    # Create the main window
    root = tk.Tk()
    root.minsize(width=475, height=150)
    root.resizable(True, False)

    leading_zero = tk.BooleanVar(value=False)
    source_file = tk.StringVar(value="")
    output_file = tk.StringVar(value="")
    channels = tk.IntVar(value=16)
    grouping = tk.StringVar(value="Mono")
    status_message = tk.StringVar(value="")

    # Set window title
    root.title("Ultrix Audio Shuffling Generator")

    # Set window icon (path to .ico file)
    root.iconbitmap(icon_path)

    # Grid Config
    root.columnconfigure(0, weight=1)

    # Frames
    source_frame = ttk.Frame(root)
    source_frame.columnconfigure(1, weight=1)

    audio_frame = ttk.Frame(root)
    audio_frame.columnconfigure(2, weight=1)
    audio_frame.columnconfigure(5, weight=1)

    output_frame = ttk.Frame(root)
    output_frame.columnconfigure(1, weight=1)

    function_frame = ttk.Frame(root)
    function_frame.columnconfigure(1, weight=1)

    # Source List widgets
    source_lbl = ttk.Label(source_frame,
                           text = "Source List")
    source_entry = ttk.Entry(source_frame,
                             textvariable=source_file)
    source_entry.bind("<FocusOut>", update_output)
    source_browse = ttk.Button(source_frame,
                               text = "Browse",
                               command=select_source_file)

    # Audio widgets
    aud_ch_lbl = ttk.Label(audio_frame,
                           text="Audio Channels")
    aud_ch_combo = ttk.Combobox(audio_frame,
                                values=(2, 4, 8, 16),
                                width=3,
                                state="readonly",
                                textvariable=channels)

    aud_group_lbl = ttk.Label(audio_frame,
                              text="Audio Grouping")
    aud_group_combo = ttk.Combobox(audio_frame,
                                   values=("Mono", "Stereo", "Quad", "Octo"),
                                   width=7,
                                   state="readonly",
                                   textvariable=grouping)

    leading_zero_check = ttk.Checkbutton(audio_frame,
                                         offvalue=False,
                                         onvalue=True,
                                         variable=leading_zero,
                                         padding=0)
    leading_zero_lbl = ttk.Label(audio_frame,
                                 text="Leading Zeroes")

    aud_spacer1 = ttk.Label(audio_frame, text="")
    aud_spacer2 = ttk.Label(audio_frame, text="")

    # Separator
    separator = ttk.Separator(root, orient="horizontal")

    # Output File widgets
    output_lbl = ttk.Label(output_frame,
                           text = "Output File")
    output_entry = ttk.Entry(output_frame,
                             textvariable=output_file)
    output_entry.bind("<Return>", press_go)
    output_browse = ttk.Button(output_frame,
                               text = "Browse")

    # Function widgets
    go_button = ttk.Button(function_frame,
                           text = "Go",
                           command=press_go)
    status_lbl = ttk.Label(function_frame,
                           text="",
                           textvariable=status_message)
    status_lbl.bind("<ButtonRelease-1>", lambda event=None : status_message.set(""))
    exit_button = ttk.Button(function_frame,
                             text="Exit",
                             command=root.destroy)

    # Frame placing
    source_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
    audio_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
    separator.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
    output_frame.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
    function_frame.grid(row=4, column=0, sticky="ew", padx=10, pady=5)

    # Widget placing
    source_lbl.grid(row=0, column=0)
    source_entry.grid(row=0, column=1, sticky="ew", padx=5)
    source_browse.grid(row=0, column=2)

    aud_ch_lbl.grid(row=0, column=0)
    aud_ch_combo.grid(row=0, column=1, padx=5)

    aud_spacer1.grid(row=0, column=2, padx=10, sticky="ew")

    aud_group_lbl.grid(row=0, column=3)
    aud_group_combo.grid(row=0, column=4, padx=5)

    aud_spacer2.grid(row=0, column=5, padx=10, sticky="ew")

    leading_zero_check.grid(row=0, column=6)
    leading_zero_lbl.grid(row=0, column=7)

    output_lbl.grid(row=0, column=0)
    output_entry.grid(row=0, column=1, sticky="ew", padx=5)
    output_browse.grid(row=0, column=2)

    go_button.grid(row=0, column=0)
    status_lbl.grid(row=0, column=1)
    exit_button.grid(row=0, column=2)

    # Start the GUI event loop
    root.mainloop()

if __name__ == '__main__':
    main()
