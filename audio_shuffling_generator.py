"""
This creates a GUI that will easily generate names and port labels
for Audio Shuffling Sources for a Ross Video Ultrix.
"""

import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from openpyxl import load_workbook

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.

    myappid = "themgineer.audio_shuffling_generator.0.0.6"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

class OutputEmpty(Exception):
    """Creates custom OutputEmpty Exception"""


class InputEmpty(Exception):
    """Creates custom InputEmpty Exception"""


class InvalidGroup(Exception):
    """Creates custom InvalidGroup Exception"""


class UnknownError(Exception):
    """Catches any other weird errors"""

def process_file(source_file, end_id, channels, grouping, output_file, leading_zero):
    """Processes source file and settings"""
    
    # Initialize lists
    output = []
    names = []
    ports = []

    # Set up audio channel grouping
    group_dict = {"Mono": 1, "Stereo": 2, "Quad": 4, "Octo": 8}

    try:
        if grouping in group_dict:
            group_step = group_dict[grouping]
        else:
            raise InvalidGroup()

        if group_step > channels:
            group_step = channels
        
        if source_file == "" or source_file is None:
            raise InputEmpty()
        elif output_file == "" or output_file is None:
            raise OutputEmpty()
        
        wb = load_workbook(source_file)
        ws = wb["sources"]

        for row in ws.iter_rows(min_row=2, max_row=end_id + 2, min_col=2, max_col=5, values_only = True):
            names.append(row[0])
            ports.append(row[3][:-8])
        
        print(names)
        print(ports)
    
    except InvalidGroup:
        return "Invalid Audio Group Selection"
    except InputEmpty:
        return "Source list needs a name."
    except OutputEmpty:
        return "Output file needs a name."
    except FileNotFoundError:
        return "Input file cannot be found."
    except UnknownError:
        return "Unknown error occurred."

def get_folder(path):
    """Function that pulls the folder path from input file"""

    if path == "":
        out_path = ""
    else:
        path_list = path.split("/")
        path_list[-1] = f"{path_list[-1].split('.')[0]}_shuffled.xlsx"
        out_path = "/".join(path_list)

    return out_path

def main():
    """Main function"""

    def select_source_file():
        # Specify file types
        filetype_list = (('Excel files', '*.xlsx'),
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
                               end_id.get(),
                               channels.get(),
                               grouping.get(),
                               output_file.get(),
                               leading_zero.get())
        status_message.set(message)

    # Create the main window
    root = tk.Tk()
    root.minsize(width=550, height=150)
    root.resizable(True, False)

    leading_zero = tk.BooleanVar(value=False)
    source_file = tk.StringVar(value="")
    output_file = tk.StringVar(value="")
    channels = tk.IntVar(value=16)
    grouping = tk.StringVar(value="Mono")
    status_message = tk.StringVar(value="")
    end_id = tk.IntVar(value=0)

    # Set window title
    root.title("Ultrix Audio Shuffling Generator")

    # Set window icon (path to .ico file)
    root.iconbitmap(os.path.join(basedir, "icon/Ultrix_U.ico"))

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
    src_spacer = ttk.Label(source_frame, text="")
    end_id_lbl = ttk.Label(source_frame, 
                           text = "End ID")
    end_id_entry = ttk.Entry(source_frame, 
                             textvariable=end_id, 
                             width=5)

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
                                         text="Leading Zeroes",
                                         offvalue=False,
                                         onvalue=True,
                                         variable=leading_zero)
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
    src_spacer.grid(row=0, column=3, padx=10, sticky="ew")
    end_id_lbl.grid(row=0, column=4)
    end_id_entry.grid(row=0, column=5, padx=5)

    aud_ch_lbl.grid(row=0, column=0)
    aud_ch_combo.grid(row=0, column=1, padx=5)

    aud_spacer1.grid(row=0, column=2, padx=10, sticky="ew")

    aud_group_lbl.grid(row=0, column=3)
    aud_group_combo.grid(row=0, column=4, padx=5)

    aud_spacer2.grid(row=0, column=5, padx=10, sticky="ew")

    leading_zero_check.grid(row=0, column=6)

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
