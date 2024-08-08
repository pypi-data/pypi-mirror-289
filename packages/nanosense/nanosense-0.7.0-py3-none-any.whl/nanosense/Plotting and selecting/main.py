import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QCheckBox, QListWidget, QLabel, QFileDialog, QLineEdit, QMessageBox, QListWidgetItem, QSplitter, QGroupBox, QFormLayout, QComboBox, QSpinBox,  QStyleFactory
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor
import os
import numpy as np
from neo.rawio import AxonRawIO
from scipy.ndimage import uniform_filter1d
import matplotlib
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import h5py
from scipy.signal import butter, bessel, cheby1, cheby2, ellip, firwin, lfilter, sosfilt, sosfilt_zi
from PySide6.QtWidgets import QProgressDialog
from PySide6.QtCore import Qt

matplotlib.use('Qt5Agg')

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        fig.tight_layout()
        super().__init__(fig)

def load_abf_file(file_path):
    # Create an instance of AxonRawIO
    raw_io = AxonRawIO(filename=file_path)

    # Parse the header information
    raw_io.parse_header()

    # Define the channel index you're interested in
    channel_index = 0

    # Read the signal size for the given block and segment without specifying channel_indexes
    signal_size = raw_io.get_signal_size(block_index=0, seg_index=0)

    # Now, read the analog signal data
    # Here, we specify channel_indexes when reading the chunk to ensure we only get data for the desired channel
    data = raw_io.get_analogsignal_chunk(block_index=0, seg_index=0, i_start=0, i_stop=signal_size, channel_indexes=[channel_index])

    # Convert the chunk to a physical quantity
    data = raw_io.rescale_signal_raw_to_float(data, dtype='float64', channel_indexes=[channel_index]).flatten()

    # Get the sampling rate for the specified channel
    sampling_rate = raw_io.get_signal_sampling_rate()

    # Convert the data to time
    time = np.arange(len(data)) / sampling_rate

    return data, sampling_rate, time

def load_hdf5_file(file_path):
    with h5py.File(file_path, 'r') as f:
        selected_data = f['selected_data'][()]
        sampling_rate = f.attrs['sampling_rate']
        time = np.arange(len(selected_data)) / sampling_rate
    return selected_data, sampling_rate, time

def calculate_rolling_stats(data, sampling_rate, avg_window_size_in_ms):
    avg_window_size_samples = int((avg_window_size_in_ms / 1000) * sampling_rate)
    rolling_avg = uniform_filter1d(data, size=avg_window_size_samples)
    return rolling_avg

class SegmentWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.start_label = QLabel("Start (s):")
        self.start_input = QLineEdit()
        self.end_label = QLabel("End (s):")
        self.end_input = QLineEdit()
        self.add_button = QPushButton("Add Segment")

        layout.addWidget(self.start_label)
        layout.addWidget(self.start_input)
        layout.addWidget(self.end_label)
        layout.addWidget(self.end_input)
        layout.addWidget(self.add_button)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SD ABF File Plotter and Selector App")
        self.setGeometry(100, 100, 1200, 800)

        self.data = None
        self.sampling_rate = None
        self.time = None
        self.selected_regions = None
        self.segment_widgets = []
        self.segments = []
        self.plots = []  # List to store multiple plots

        main_splitter = QSplitter(Qt.Orientation.Horizontal)

        left_widget = QWidget()
        left_layout = QVBoxLayout()
        left_widget.setLayout(left_layout)

        right_widget = QWidget()
        right_layout = QVBoxLayout()
        right_widget.setLayout(right_layout)

        main_splitter.addWidget(left_widget)
        main_splitter.addWidget(right_widget)
        main_splitter.setSizes([300, 900])

        self.setCentralWidget(main_splitter)

        nth_element_layout = QHBoxLayout()

        # Left Side
        self.app_name_label = QLabel("SD ABF File Plotter and Selector App")
        self.app_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.app_name_label.setStyleSheet("font-size: 22px; font-weight: bold;")
        self.email_label = QLabel("shankar.dutt@anu.edu.au")
        self.email_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.select_folder_btn = QPushButton("Select Folder")
        self.select_folder_btn.clicked.connect(self.select_folder)

        self.include_subfolders_chk = QCheckBox("Include Subfolders")

        self.files_list_widget = QListWidget()
        self.files_list_widget.setSelectionMode(QListWidget.SelectionMode.MultiSelection)

        self.folder_path_label = QLabel(" ")
        self.folder_path_label.setWordWrap(True)

        # Add the "Plot multiple files" checkbox
        self.plot_multiple_files_chk = QCheckBox("Plot multiple files")
        self.plot_multiple_files_chk.stateChanged.connect(self.toggle_plot_multiple_files)

        self.nth_element_label = QLabel("Plot nth element:")
        self.nth_element_spinbox = QSpinBox()
        self.nth_element_spinbox.setMinimum(1)
        self.nth_element_spinbox.setMaximum(1000)
        self.nth_element_spinbox.setValue(1)

        nth_element_layout.addWidget(self.nth_element_label)
        nth_element_layout.addWidget(self.nth_element_spinbox)

        self.low_pass_filter_chk = QCheckBox("Apply Low Pass Filter")
        self.low_pass_filter_chk.stateChanged.connect(self.toggle_low_pass_filter)

        self.filter_type_label = QLabel("Filter Type:")
        self.filter_type_dropdown = QComboBox()
        self.filter_type_dropdown.addItems(["Butterworth", "Bessel", "Chebyshev I", "Chebyshev II", "Elliptic", "FIR", "IIR"])
        self.filter_type_dropdown.setEnabled(False)

        self.cutoff_frequency_label = QLabel("Cutoff Frequency (kHz):")
        self.cutoff_frequency_spinbox = QSpinBox()
        self.cutoff_frequency_spinbox.setRange(1, 1000)
        self.cutoff_frequency_spinbox.setValue(10)
        self.cutoff_frequency_spinbox.setEnabled(False)

        self.plot_btn = QPushButton("Plot Selected File(s)")
        self.plot_btn.clicked.connect(self.plot_selected_files)

        left_layout.addWidget(self.app_name_label)
        left_layout.addWidget(self.email_label)
        left_layout.addWidget(self.select_folder_btn)
        left_layout.addWidget(self.include_subfolders_chk)
        left_layout.addWidget(self.files_list_widget)
        left_layout.addWidget(self.folder_path_label)
        left_layout.addWidget(self.plot_multiple_files_chk)  # Add the new checkbox
        left_layout.addLayout(nth_element_layout)
        left_layout.addWidget(self.low_pass_filter_chk)
        left_layout.addWidget(self.filter_type_label)
        left_layout.addWidget(self.filter_type_dropdown)
        left_layout.addWidget(self.cutoff_frequency_label)
        left_layout.addWidget(self.cutoff_frequency_spinbox)
        left_layout.addWidget(self.plot_btn)

        # Right Side
        self.right_splitter = QSplitter(Qt.Orientation.Vertical)
        right_layout.addWidget(self.right_splitter)

        self.top_right_widget = QWidget()
        self.top_right_layout = QVBoxLayout()
        self.top_right_widget.setLayout(self.top_right_layout)

        self.bottom_right_widget = QWidget()
        self.bottom_right_layout = QVBoxLayout()
        self.bottom_right_widget.setLayout(self.bottom_right_layout)

        self.right_splitter.addWidget(self.top_right_widget)
        self.right_splitter.addWidget(self.bottom_right_widget)

        # Top Right
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.top_right_layout.addWidget(self.canvas)

        self.mpl_toolbar = NavigationToolbar2QT(self.canvas, self)
        self.top_right_layout.addWidget(self.mpl_toolbar)

        # Bottom Right
        self.bottom_right_widget = QWidget()
        self.bottom_right_layout = QHBoxLayout()
        self.bottom_right_widget.setLayout(self.bottom_right_layout)
        self.right_splitter.addWidget(self.bottom_right_widget)

        self.calculate_avg_group = QGroupBox("Calculate and Plot Avg")
        self.calculate_avg_layout = QFormLayout()
        self.calculate_avg_group.setLayout(self.calculate_avg_layout)

        self.calculate_avg_chk = QCheckBox("Calculate and Plot Avg")
        self.calculate_avg_chk.stateChanged.connect(self.toggle_avg_window_size)

        self.avg_window_size_label = QLabel("Avg Window Size (ms):")
        self.avg_window_size_input = QLineEdit("10")
        #self.avg_window_size_input.setEnabled(False)
        self.avg_window_size_input.editingFinished.connect(self.update_plot)

        self.update_plot_btn = QPushButton("Update Plot")
        #self.update_plot_btn.setEnabled(False)
        self.update_plot_btn.clicked.connect(self.update_plot)

        self.calculate_avg_layout.addRow(self.calculate_avg_chk)
        self.calculate_avg_layout.addRow( self.avg_window_size_label, self.avg_window_size_input)
        self.calculate_avg_layout.addRow(self.update_plot_btn)

        self.threshold_group = QGroupBox("Select Regions within Threshold")
        self.threshold_layout = QFormLayout()
        self.threshold_group.setLayout(self.threshold_layout)

        self.threshold_chk = QCheckBox("Select Regions within Threshold")
        self.threshold_chk.stateChanged.connect(self.toggle_threshold_input)

        self.threshold_value_label = QLabel("Value for selecting regions(pA):")
        self.threshold_value_input = QSpinBox()
        self.threshold_value_input.setRange(0, 1000000)
        self.threshold_value_input.setValue(0)
        self.threshold_value_input.setEnabled(False)
        self.threshold_value_input.editingFinished.connect(self.update_plot)

        self.threshold_label = QLabel("Threshold (% of the value above):")
        self.threshold_input = QLineEdit("75")
        self.threshold_input.setEnabled(False)
        self.threshold_input.editingFinished.connect(self.update_plot)

        self.threshold_layout.addRow(self.threshold_chk)
        self.threshold_layout.addRow(self.threshold_value_label, self.threshold_value_input)
        self.threshold_layout.addRow( self.threshold_label, self.threshold_input)

        self.select_segments_group = QGroupBox("Select Segments")
        self.select_segments_layout = QVBoxLayout()
        self.select_segments_group.setLayout(self.select_segments_layout)

        self.select_segments_chk = QCheckBox("Select Segments")
        self.select_segments_chk.stateChanged.connect(self.toggle_select_segments)

        self.segment_dropdown = QComboBox()
        self.segment_dropdown.setEnabled(False)

        self.delete_segment_btn = QPushButton("Delete Segment")
        self.delete_segment_btn.setEnabled(False)
        self.delete_segment_btn.clicked.connect(self.delete_segment)

        self.select_segments_layout.addWidget(self.select_segments_chk)
        self.select_segments_layout.addWidget(self.segment_dropdown)
        self.select_segments_layout.addWidget(self.delete_segment_btn)

        self.bottom_right_layout.addWidget(self.calculate_avg_group)
        self.bottom_right_layout.addWidget(self.threshold_group)
        self.bottom_right_layout.addWidget(self.select_segments_group)

        bottom_button_layout = QHBoxLayout()
        self.bottom_right_layout.addLayout(bottom_button_layout)

        self.save_btn = QPushButton("Save Selected Data")
        self.save_btn.clicked.connect(self.save_selected_data)
        bottom_button_layout.addWidget(self.save_btn)

        self.raw_data = []
    
    def toggle_low_pass_filter(self, state):
        self.filter_type_dropdown.setEnabled(state == Qt.CheckState.Checked.value)
        self.cutoff_frequency_spinbox.setEnabled(state == Qt.CheckState.Checked.value)

    def toggle_plot_multiple_files(self, state):
        # Enable/disable multi-selection based on the checkbox state
        self.files_list_widget.setSelectionMode(
            QListWidget.SelectionMode.MultiSelection if state == Qt.CheckState.Checked.value
            else QListWidget.SelectionMode.SingleSelection
        )

    def select_folder(self):
        options = QFileDialog.Option.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(self, "Select Folder", "", options=options)
        if directory:
            self.folder_path_label.setText(f"Selected folder: {directory}")
            self.populate_file_list(directory, self.include_subfolders_chk.isChecked())

    def apply_low_pass_filter(self, data, cutoff_frequency, type, sampling_rate):
        if type == 'Butterworth':
            nyquist_rate = sampling_rate / 2.0
            cutoff = cutoff_frequency / nyquist_rate
            sos = butter(N=8, Wn=cutoff, btype='low', analog=False, output='sos')
            zi = sosfilt_zi(sos) * data[0]
            filtered_data, _ = sosfilt(sos, data, zi=zi)
            return filtered_data
        elif type == 'Bessel':
            nyquist_rate = sampling_rate / 2.0
            cutoff = cutoff_frequency / nyquist_rate
            sos = bessel(N=8, Wn=cutoff, btype='low', analog=False, output='sos')
            zi = sosfilt_zi(sos) * data[0]
            filtered_data, _ = sosfilt(sos, data, zi=zi)
            return filtered_data
        elif type == 'Chebyshev I':
            nyquist_rate = sampling_rate / 2.0
            cutoff = cutoff_frequency / nyquist_rate
            sos = cheby1(N=8, rp=0.1, Wn=cutoff, btype='low', analog=False, output='sos')
            zi = sosfilt_zi(sos) * data[0]
            filtered_data, _ = sosfilt(sos, data, zi=zi)
            return filtered_data
        elif type == 'Chebyshev II':
            nyquist_rate = sampling_rate / 2.0
            cutoff = cutoff_frequency / nyquist_rate
            sos = cheby2(N=8, rs=40, Wn=cutoff, btype='low', analog=False, output='sos')
            zi = sosfilt_zi(sos) * data[0]
            filtered_data, _ = sosfilt(sos, data, zi=zi)
            return filtered_data
        elif type == 'Elliptic':
            nyquist_rate = sampling_rate / 2.0
            cutoff = cutoff_frequency / nyquist_rate
            sos = ellip(N=8, rp=0.1, rs=40, Wn=cutoff, btype='low', analog=False, output='sos')
            zi = sosfilt_zi(sos) * data[0]
            filtered_data, _ = sosfilt(sos, data, zi=zi)
            return filtered_data
        elif type == 'FIR':
            nyquist_rate = sampling_rate / 2.0
            cutoff = cutoff_frequency / nyquist_rate
            taps = firwin(101, cutoff)
            filtered_data = lfilter(taps, 1, data)
            return filtered_data
        elif type == 'IIR':
            nyquist_rate = sampling_rate / 2.0
            cutoff = cutoff_frequency / nyquist_rate
            b, a = butter(N=8, Wn=cutoff, btype='low', analog=False)
            filtered_data = lfilter(b, a, data)
            return filtered_data

    def populate_file_list(self, directory, include_subfolders):
        self.files_list_widget.clear()
        file_list = []
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.abf') or file.endswith('.hdf5') or file.endswith('.h5'):
                    rel_path = os.path.relpath(os.path.join(root, file), start=directory)
                    full_path = os.path.join(root, file)
                    file_list.append((rel_path, full_path))
            
            if not include_subfolders:
                break
        
        # Sort the file list based on the relative path (which includes the file name)
        file_list.sort(key=lambda x: x[0].lower())
        
        # Add sorted items to the list widget
        for rel_path, full_path in file_list:
            item = QListWidgetItem(rel_path)
            item.setData(Qt.ItemDataRole.UserRole, full_path)
            self.files_list_widget.addItem(item)


    def plot_selected_files(self):
        selected_items = self.files_list_widget.selectedItems()
        if not selected_items:
            return

        self.plots = []
        self.figure.clear()

        total_steps = len(selected_items) * 2  # Loading + Plotting for each file
        progress = QProgressDialog("Processing files...", "Cancel", 0, total_steps, self)
        progress.setWindowModality(Qt.WindowModal)
        progress.setWindowTitle("Please Wait")
        progress.setMinimumDuration(0)

        loaded_data = []
        current_step = 0

        # Load all files
        for item in selected_items:
            if progress.wasCanceled():
                return
            file_path = item.data(Qt.ItemDataRole.UserRole)
            progress.setLabelText(f"Loading {os.path.basename(file_path)}...")
            try:
                data, sampling_rate, time = self.load_file(file_path)
                loaded_data.append((file_path, data, sampling_rate, time))
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))
            current_step += 1
            progress.setValue(current_step)
            QApplication.processEvents()

        # Plot loaded files
        if self.plot_multiple_files_chk.isChecked():
            num_plots = len(loaded_data)
            rows = int(np.ceil(np.sqrt(num_plots)))
            cols = int(np.ceil(num_plots / rows))

            for i, (file_path, data, sampling_rate, time) in enumerate(loaded_data):
                if progress.wasCanceled():
                    break
                progress.setLabelText(f"Plotting {os.path.basename(file_path)}...")
                ax = self.figure.add_subplot(rows, cols, i + 1)
                self.plot_data(ax, file_path, data, sampling_rate, time)
                self.plots.append(ax)
                current_step += 1
                progress.setValue(current_step)
                QApplication.processEvents()
        else:
            file_path, data, sampling_rate, time = loaded_data[0]
            progress.setLabelText(f"Plotting {os.path.basename(file_path)}...")
            ax = self.figure.add_subplot(111)
            self.plot_data(ax, file_path, data, sampling_rate, time)
            self.plots.append(ax)
            current_step += 1
            progress.setValue(current_step)

        progress.close()

        self.figure.tight_layout()
        self.canvas.draw()

    def plot_data(self, ax, file_path, data, sampling_rate, time):
        nth_element = self.nth_element_spinbox.value()
        ax.plot(time[::nth_element], data[::nth_element], linewidth=0.5)
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Current (nA)')
        ax.set_xlim([min(time), max(time)])
        ax.set_title(os.path.basename(file_path))

        # Store the data for later use
        ax.raw_data = data
        ax.sampling_rate = sampling_rate
        ax.time = time
        ax.data = data
        ax.full_file_path = file_path  # Store the full file path

    def load_file(self, file_path):
        try:
            if file_path.endswith('.abf'):
                raw_data, sampling_rate, time = load_abf_file(file_path)
            elif file_path.endswith('.hdf5') or file_path.endswith('.h5'):
                raw_data, sampling_rate, time = load_hdf5_file(file_path)
            else:
                raise ValueError(f"Unsupported file format: {file_path}")

            data = raw_data.copy()

            if self.low_pass_filter_chk.isChecked():
                filter_type = self.filter_type_dropdown.currentText()
                cutoff_frequency = self.cutoff_frequency_spinbox.value() * 1000  # Convert kHz to Hz
                
                if sampling_rate <= cutoff_frequency * 2:
                    raise ValueError(f"The selected cutoff frequency is too high for the sampling rate of {file_path}.")
            
                data = self.apply_low_pass_filter(data, cutoff_frequency, filter_type, sampling_rate)

            return data, sampling_rate, time
        except Exception as e:
            raise Exception(f"Error loading {os.path.basename(file_path)}: {str(e)}")

    def plot_file(self, file_path, ax):
        try:
            if file_path.endswith('.abf'):
                raw_data, sampling_rate, time = load_abf_file(file_path)
            elif file_path.endswith('.hdf5') or file_path.endswith('.h5'):
                raw_data, sampling_rate, time = load_hdf5_file(file_path)
            else:
                raise ValueError(f"Unsupported file format: {file_path}")

            data = raw_data.copy()

            if self.low_pass_filter_chk.isChecked():
                filter_type = self.filter_type_dropdown.currentText()
                cutoff_frequency = self.cutoff_frequency_spinbox.value() * 1000  # Convert kHz to Hz
                
                if sampling_rate <= cutoff_frequency * 2:
                    raise ValueError(f"The selected cutoff frequency is too high for the sampling rate of {file_path}.")
            
                data = self.apply_low_pass_filter(data, cutoff_frequency, filter_type, sampling_rate)
            
            nth_element = self.nth_element_spinbox.value()
            ax.plot(time[::nth_element], data[::nth_element], linewidth=0.5)
            ax.set_xlabel('Time (s)')
            ax.set_ylabel('Current (nA)')
            ax.set_xlim([min(time), max(time)])
            ax.set_title(os.path.basename(file_path))

            # Store the data for later use
            ax.raw_data = raw_data
            ax.sampling_rate = sampling_rate
            ax.time = time
            ax.data = data

        except Exception as e:
            ax.set_title(f"Failed to load: {os.path.basename(file_path)}")
            ax.text(0.5, 0.5, f"Error: {str(e)}", ha='center', va='center', transform=ax.transAxes, wrap=True)
            ax.axis('off')

    def update_plot(self):
        for ax in self.plots:
            ax.clear()
            file_path = ax.get_title()
            
            if not hasattr(ax, 'data'):
                # If data wasn't loaded successfully, skip this plot
                ax.set_title(f"Failed to load: {os.path.basename(file_path)}")
                continue

            ax.plot(ax.time[::self.nth_element_spinbox.value()], ax.data[::self.nth_element_spinbox.value()], linewidth=0.5)
            ax.set_xlabel('Time (s)')
            ax.set_ylabel('Current (nA)')
            ax.set_xlim([min(ax.time), max(ax.time)])
            ax.set_title(os.path.basename(file_path))

            show_rolling_avg = self.calculate_avg_chk.isChecked()
            if show_rolling_avg:
                avg_window_size_in_ms = float(self.avg_window_size_input.text())
                rolling_avg = calculate_rolling_stats(ax.data, ax.sampling_rate, avg_window_size_in_ms)
                ax.plot(ax.time, rolling_avg, linewidth=2)

            show_threshold = self.threshold_chk.isChecked()
            if show_threshold:
                threshold_percentage = float(self.threshold_input.text()) / 100
                if self.threshold_value_input.value() == 0:
                    self.threshold_value_input.setValue(int(np.mean(ax.data)*1000))
                threshold_value = self.threshold_value_input.value()/1000
                avg_window_size_in_ms = float(self.avg_window_size_input.text())
                rolling_avg = calculate_rolling_stats(ax.data, ax.sampling_rate, avg_window_size_in_ms)
                threshold_lower = threshold_value - (threshold_value*(1-threshold_percentage))
                threshold_upper = threshold_value + (threshold_value*(1-threshold_percentage))
                
                selected_regions = np.where((rolling_avg >= threshold_lower) & (rolling_avg <= threshold_upper))[0]
                
                for region_start, region_end in self.find_contiguous_regions(selected_regions):
                    start_time = ax.time[region_start]
                    end_time = ax.time[region_end]
                    ax.axvline(x=start_time, color='r', linestyle='-', linewidth=0.5)
                    ax.axvline(x=end_time, color='r', linestyle='-', linewidth=0.5)
                    ax.axvspan(start_time, end_time, alpha=0.3, color='red')

            show_segments = self.select_segments_chk.isChecked()
            if show_segments:
                for start_time, end_time in self.segments:
                    ax.axvline(x=start_time, color='g', linestyle='-', linewidth=0.5)
                    ax.axvline(x=end_time, color='g', linestyle='-', linewidth=0.5)
                    ax.axvspan(start_time, end_time, alpha=0.3, color='green')

        self.canvas.draw()


    def find_contiguous_regions(self, data):
        contiguous_regions = []
        data = np.sort(data)  # Sort the input data
        start_index = data[0]
        prev_index = start_index
        for i in range(1, len(data)):
            if data[i] > prev_index + 1:
                contiguous_regions.append((start_index, prev_index))
                start_index = data[i]
            prev_index = data[i]
        contiguous_regions.append((start_index, data[-1]))
        return contiguous_regions

    def toggle_avg_window_size(self, state):
        self.avg_window_size_input.setEnabled(state == Qt.CheckState.Checked.value)
        self.update_plot_btn.setEnabled(state == Qt.CheckState.Checked.value)
        self.update_plot()

    def toggle_threshold_input(self, state):
        self.threshold_input.setEnabled(state == Qt.CheckState.Checked.value)
        self.threshold_value_input.setEnabled(state == Qt.CheckState.Checked.value)
        self.select_segments_chk.setChecked(False)
        self.update_plot()

    def toggle_select_segments(self, state):
        if state == Qt.CheckState.Checked.value:
            segment_widget = SegmentWidget()
            segment_widget.add_button.clicked.connect(lambda: self.add_segment(segment_widget))
            self.segment_widgets.append(segment_widget)
            self.select_segments_layout.insertWidget(self.select_segments_layout.count() - 2, segment_widget)
            segment_widget.show()
            self.segment_dropdown.setEnabled(True)
            self.delete_segment_btn.setEnabled(True)
        else:
            while self.segment_widgets:
                segment_widget = self.segment_widgets.pop()
                self.select_segments_layout.removeWidget(segment_widget)
                segment_widget.deleteLater()
            self.segments.clear()
            self.segment_dropdown.clear()
            self.segment_dropdown.setEnabled(False)
            self.delete_segment_btn.setEnabled(False)

        self.threshold_chk.setChecked(False)
        self.update_plot()

    def add_segment(self, segment_widget):
        start_time = float(segment_widget.start_input.text())
        end_time = float(segment_widget.end_input.text())
        self.segments.append((start_time, end_time))
        segment_label = f"Segment: {start_time} - {end_time}"
        self.segment_dropdown.addItem(segment_label)
        index = self.segment_dropdown.count() - 1
        self.segment_dropdown.setItemData(index, segment_widget)

        # Add the segment to all plots
        for ax in self.figure.axes:
            ax.axvline(x=start_time, color='g', linestyle='-', linewidth=0.5)
            ax.axvline(x=end_time, color='g', linestyle='-', linewidth=0.5)
            ax.axvspan(start_time, end_time, alpha=0.3, color='green')

        self.canvas.draw()

    def delete_segment(self):
        if self.segment_dropdown.count() > 0:
            index = self.segment_dropdown.currentIndex()
            segment_to_remove = self.segments.pop(index)
            segment_label = self.segment_dropdown.itemText(index)
            self.segment_dropdown.removeItem(index)
            
            # Remove the segment from all plots
            for ax in self.figure.axes:
                # Remove green lines (segment boundaries)
                lines_to_remove = [line for line in ax.lines 
                                if line.get_color() == 'g' and 
                                (line.get_xdata()[0] == segment_to_remove[0] or 
                                    line.get_xdata()[0] == segment_to_remove[1])]
                for line in lines_to_remove:
                    ax.lines.remove(line)
                
                # Remove green spans (segment areas)
                spans_to_remove = [span for span in ax.patches 
                                if span.get_facecolor() == (0.0, 0.5019607843137255, 0.0, 0.3) and
                                span.get_x() == segment_to_remove[0] and 
                                span.get_x() + span.get_width() == segment_to_remove[1]]
                for span in spans_to_remove:
                    ax.patches.remove(span)
            
            # Redraw the remaining segments
            for start_time, end_time in self.segments:
                for ax in self.figure.axes:
                    ax.axvline(x=start_time, color='g', linestyle='-', linewidth=0.5)
                    ax.axvline(x=end_time, color='g', linestyle='-', linewidth=0.5)
                    ax.axvspan(start_time, end_time, alpha=0.3, color='green')
            
            self.canvas.draw()

            # Remove the segment widget if it exists
            for i in range(self.select_segments_layout.count()):
                widget = self.select_segments_layout.itemAt(i).widget()
                if isinstance(widget, SegmentWidget) and widget.start_input.text() == str(segment_to_remove[0]) and widget.end_input.text() == str(segment_to_remove[1]):
                    self.select_segments_layout.removeWidget(widget)
                    widget.deleteLater()
                    break

    def save_selected_data(self):
        if not self.plots:
            QMessageBox.warning(self, "Warning", "No data to save.")
            return

        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.Directory)
        directory = file_dialog.getExistingDirectory(self, "Select Directory to Save Files")

        if directory:
            for ax in self.plots:
                try:
                    full_file_path = ax.full_file_path  # Use the full file path we stored
                    file_name = os.path.basename(full_file_path)  # Get just the file name
                    raw_data = ax.raw_data
                    sampling_rate = ax.sampling_rate
                    time = ax.time

                    selected_data = raw_data

                    if self.threshold_chk.isChecked():
                        selected_regions = self.find_selected_regions(raw_data, sampling_rate, time)
                        selected_data = np.concatenate([raw_data[start:end+1] for start, end in selected_regions])
                    elif self.select_segments_chk.isChecked():
                        selected_data = np.concatenate([raw_data[np.searchsorted(time, start):np.searchsorted(time, end)+1] for start, end in self.segments])

                    # Create the new file name
                    base_name, ext = os.path.splitext(file_name)
                    output_filename = f"{base_name}_selected_data.h5"
                    output_path = os.path.join(directory, output_filename)

                    with h5py.File(output_path, 'w') as f:
                        f.create_dataset('selected_data', data=selected_data)
                        f.attrs['sampling_rate'] = sampling_rate


                    #QMessageBox.information(self, "Success", f"Data saved successfully as {output_filename}")

                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Failed to save data for {file_name}: {str(e)}")

            QMessageBox.information(self, "Success", f"All data saved successfully to {directory}.")

            
    def find_selected_regions(self, data, sampling_rate, time):
        avg_window_size_in_ms = float(self.avg_window_size_input.text())
        rolling_avg = calculate_rolling_stats(data, sampling_rate, avg_window_size_in_ms)
        threshold_value = self.threshold_value_input.value() / 1000
        threshold_percentage = float(self.threshold_input.text()) / 100
        threshold_lower = threshold_value - (threshold_value * (1 - threshold_percentage))
        threshold_upper = threshold_value + (threshold_value * (1 - threshold_percentage))
        selected_regions = np.where((rolling_avg >= threshold_lower) & (rolling_avg <= threshold_upper))[0]
        return self.find_contiguous_regions(selected_regions)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))  # Use Fusion or other available styles
    # Customize the palette for a darker, more modern look
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
    app.setPalette(palette)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())