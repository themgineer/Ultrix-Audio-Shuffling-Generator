"""
This creates a GUI that will easily generate names and port labels
for Audio Shuffling Sources for a Ross Video Ultrix.
"""

import os, sys
sys.path.insert(0, os.path.abspath("."))

from pathlib import Path

from PySide6 import QtCore, QtWidgets
from openpyxl import load_workbook, Workbook, worksheet

from UI.main_window_ui import Ui_mw_main

try:
    from ctypes import windll  # Only exists on Windows.

    MYAPPID = "themgineer.audio_shuffling_generator.0.0.6"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(MYAPPID)
except ImportError:
    pass

class OutputEmpty(Exception):
    """Creates custom OutputEmpty Exception"""

class InputEmpty(Exception):
    """Creates custom InputEmpty Exception"""

class UnknownError(Exception):
    """Catches any other weird errors"""


class MainWindow(QtWidgets.QMainWindow, Ui_mw_main):

    wb = Workbook()
    ws = worksheet

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_srcBrowse.setFocus()

        self.action_quit.triggered.connect(self.close)
        self.pb_quit.clicked.connect(self.close)

        self.le_sourceFile.textChanged.connect(self.autofill_output)
        self.le_sourceFile.textChanged.connect(lambda: self.load_sheet(self.le_sourceFile.text()))

        self.sb_index.valueChanged.connect(self.get_last_source_name)

        self.action_open.triggered.connect(self.open_source_dialog)
        self.pb_srcBrowse.clicked.connect(self.open_source_dialog)
        self.pb_outBrowse.clicked.connect(self.open_dest_dialog)

        self.action_shuffle.triggered.connect(self.process_file)
        self.pb_go.clicked.connect(self.process_file)


    @QtCore.Slot()
    def load_sheet(self, source_file):
        """ Slot attempts to load """
        self.wb = Workbook()
        self.ws = worksheet
        if source_file:
            try:
                self.wb = load_workbook(source_file)
                self.ws = self.wb["sources"]
            except Exception as e:
                if type(e).__name__ == 'InvalidFileException':
                    self.show_status("File not found.")


    @QtCore.Slot()
    def autofill_output(self):
        if self.le_sourceFile.text() == "":
            self.le_outputFile.setText("")
        else:
            path_list = self.le_sourceFile.text().split("/")
            path_list[-1] = f"{path_list[-1].split('.')[0]}_shuffled.xlsx"
            self.le_outputFile.setText("/".join(path_list))

    @QtCore.Slot()
    def open_source_dialog(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Select a File",
            None,
            "Excel Files (*.xlsx)"
        )
        if filename:
            path = Path(filename)
            self.le_sourceFile.setText(str(path))

    @QtCore.Slot()
    def open_dest_dialog(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Select a File",
            None,
            "Excel Files (*.xlsx)"
        )
        if filename:
            path = Path(filename)
            self.le_outputFile.setText(str(path))

    @QtCore.Slot()
    def get_last_source_name(self):
        try:
            if self.le_sourceFile.text():
                last_source = self.ws['B'][self.sb_index.value() + 1].value
                self.show_status(f"Last source: {last_source}")
        except TypeError:
            self.show_status("Invalid index")

    @QtCore.Slot()
    def process_file(self):
        source_file = self.le_sourceFile.text()
        output_file = self.le_outputFile.text()
        end_id = self.sb_index.value()
        channels = int(self.cb_channels.currentText())
        grouping = self.cb_grouping.currentText()
        leading_zero = self.ck_leadingZero.isChecked()

        # Initialize lists
        names = []
        ports = []

        group_dict = {"Mono": 1, "Stereo": 2, "Quad": 4, "Octo": 8}

        try:
            group_step = min(group_dict[grouping], channels)

            if source_file == "" or source_file is None:
                raise InputEmpty()

            if output_file == "" or output_file is None:
                raise OutputEmpty()
            
            if not Path(source_file).exists():
                raise FileNotFoundError()

            for row in self.ws.iter_rows(min_row=2,
                                    max_row=end_id + 2,
                                    min_col=2,
                                    max_col=5,
                                    values_only = True):
                names.append(row[0])
                ports.append(row[3][:-8])

            starting_index = self.ws['A'][-1].value + 1

            shuffled_names = self.process_names(names, channels, group_step, leading_zero)
            shuffled_ports = self.process_ports(ports, channels, group_step)

            new_rows = self.create_new_rows(shuffled_names, shuffled_ports, starting_index)

            for row in new_rows:
                self.ws.append(row)

            self.wb.save(output_file)

            message = "Output Successful!"

        except InputEmpty:
            message = "Input file not defined."
        except OutputEmpty:
            message = "Output file not defined."
        except FileNotFoundError:
            message = "Input file not found."
        except PermissionError:
            message = "Permission Denied: Excel file may still be open."
        except UnknownError:
            message = "Unknown error occurred."
        except AttributeError:
            message = "Unknown error with input file."
        
        self.show_status(message)

    def process_names(self, names, channels, group_step, leading_zero):
        """ Creates a list of names with channel numbers appended """

        output = []

        if leading_zero:
            if group_step == 1:
                for i in names:
                    for j in range(1, channels + 1):
                        output.append(f"{i} CH{j:02d}")
            else:
                for i in names:
                    for j in range(1, channels + 1, group_step):
                        output.append(f"{i} CH{j:02d}-{j+(group_step - 1):02d}")
        else:
            if group_step == 1:
                for i in names:
                    for j in range(1, channels + 1):
                        output.append(f"{i} CH{j}")
            else:
                for i in names:
                    for j in range(1, channels + 1, group_step):
                        output.append(f"{i} CH{j}-{j+(group_step - 1)}")

        return output
    
    def process_ports(self, ports, channels, group_step):
        """ Creates a list of lists with channel ports """

        output = []

        for port in ports:
            for ch_range in range(1, channels + 1, group_step):
                temp = []
                for _ in range(1, channels + 1, group_step):
                    for ch in range(ch_range, ch_range + group_step):
                        temp.append(f"{port}.audio.ch{ch}")
                output.append(temp)
        return output

    def create_new_rows(self, names, ports, index):
        """ Creates rows to add to Excel sheet """
        output = []

        for i, name in enumerate(names):
            temp = [index, name, "", "", ""]
            temp.extend(ports[i])
            output.append(temp)
            index += 1

        return output
    
    def show_status(self, message):
        self.statusbar.showMessage(message, timeout=10000)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
