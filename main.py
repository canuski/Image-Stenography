import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QFileDialog, QMessageBox, QLabel, QProgressBar
from PyQt5.QtCore import Qt, QTimer
from encode import encode_image
from decode import decode_image

def resource_path(relative_path):
    try:
        base_path =  sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class LoadingScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("Processing")
        self.setGeometry(300, 300, 200, 100)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  # Add margins to layout

        self.label = QLabel("Processing, please wait...")
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)  # Set to indeterminate mode

        layout.addWidget(self.label)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

        # Add a timer to animate the progress bar
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate_progress)
        self.timer.start(100)  # Milliseconds interval for animation

    def animate_progress(self):
        self.progress_bar.setValue(
            (self.progress_bar.value() + 1) % (self.progress_bar.maximum() + 1))


class EncodeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Encode Message')

        screen_geometry = QApplication.desktop().availableGeometry()
        width = int(screen_geometry.width() * 0.8)
        height = int(screen_geometry.height() * 0.8)
        x = int(screen_geometry.width() * 0.1)
        y = int(screen_geometry.height() * 0.1)
        self.setGeometry(x, y, width, height)

        self.message_label = QLabel("Enter message:")
        self.message_input = QLineEdit()
        self.file_path_button = QPushButton('Select Image')
        self.file_path_input = QLineEdit()
        self.encode_button = QPushButton('Encode')
        self.back_button = QPushButton('Back')

        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)  # Add margins to layout
        layout.setSpacing(20)  # Adjust spacing between widgets

        layout.addWidget(self.message_label)
        layout.addWidget(self.message_input)
        layout.addWidget(self.file_path_button)
        layout.addWidget(self.file_path_input)
        layout.addWidget(self.encode_button)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

        self.file_path_button.clicked.connect(self.select_image)
        self.encode_button.clicked.connect(self.encode_clicked)
        self.back_button.clicked.connect(self.close)

        # Apply external CSS
        with open(resource_path('E:/Projects/Image Stenography/style.css'), 'r') as f:
            self.setStyleSheet(f.read())

    def select_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)
        if file_path:
            self.file_path_input.setText(file_path)

    def encode_clicked(self):
        message = self.message_input.text()
        file_path = self.file_path_input.text()
        if message and file_path:
            loading_screen = LoadingScreen(self)
            loading_screen.show()
            encode_image(
                file_path, f'............{message}', 'encoded_image.png')
            loading_screen.close()
            QMessageBox.information(
                self, "Success", "Message encoded successfully.")
        else:
            QMessageBox.warning(
                self, "Warning", "Please enter a message and select an image.")

        self.close()


class DecodeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Decode Message')

        screen_geometry = QApplication.desktop().availableGeometry()
        width = int(screen_geometry.width() * 0.8)
        height = int(screen_geometry.height() * 0.8)
        x = int(screen_geometry.width() * 0.1)
        y = int(screen_geometry.height() * 0.1)
        self.setGeometry(x, y, width, height)

        self.file_path_label = QLabel("Select Image:")
        self.file_path_input = QLineEdit()
        self.file_path_button = QPushButton('Select Image')
        self.decode_button = QPushButton('Decode')
        self.back_button = QPushButton('Back')

        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)  # Add margins to layout
        layout.setSpacing(20)  # Adjust spacing between widgets

        layout.addWidget(self.file_path_label)
        layout.addWidget(self.file_path_input)
        layout.addWidget(self.file_path_button)
        layout.addWidget(self.decode_button)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

        self.file_path_button.clicked.connect(self.select_image)
        self.decode_button.clicked.connect(self.decode_clicked)
        self.back_button.clicked.connect(self.close)

        # Apply external CSS
        with open(resource_path('E:/Projects/Image Stenography/style.css'), 'r') as f:
            self.setStyleSheet(f.read())

    def select_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)
        if file_path:
            self.file_path_input.setText(file_path)

    def decode_clicked(self):
        file_path = self.file_path_input.text()
        if file_path:
            loading_screen = LoadingScreen(self)
            loading_screen.show()
            decoded_message = decode_image(file_path)
            loading_screen.close()
            if decoded_message:
                QMessageBox.information(
                    self, "Decoded Message", f"Decoded message: {decoded_message}")
            else:
                QMessageBox.warning(
                    self, "Warning", "No message found in the image.")
        else:
            QMessageBox.warning(self, "Warning", "Please select an image.")

        self.close()


class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        encode_button = QPushButton('Encode', self)
        decode_button = QPushButton('Decode', self)

        message_label = QLabel('Image Steganography App', self)  # Added message label

        layout = QVBoxLayout()
        layout.setContentsMargins(100, 100, 100, 100)  # Add margins to layout
        layout.setSpacing(50)  # Adjust spacing between widgets

        layout.addWidget(message_label)  # Add message label
        layout.addWidget(encode_button)
        layout.addWidget(decode_button)

        self.setLayout(layout)

        encode_button.clicked.connect(self.open_encode_window)
        decode_button.clicked.connect(self.open_decode_window)

        self.setWindowTitle('Home Screen')

        # Set main window size to 80% of screen size
        screen_geometry = QApplication.desktop().availableGeometry()
        width = int(screen_geometry.width() * 0.8)
        height = int(screen_geometry.height() * 0.8)
        x = int(screen_geometry.width() * 0.1)
        y = int(screen_geometry.height() * 0.1)
        self.setGeometry(x, y, width, height)

        # Apply external CSS
        with open(resource_path('E:/Projects/Image Stenography/style.css'), 'r') as f:
            self.setStyleSheet(f.read())

    def open_encode_window(self):
        self.encode_window = EncodeWindow()
        self.encode_window.show()

    def open_decode_window(self):
        self.decode_window = DecodeWindow()
        self.decode_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    home_screen = HomeScreen()
    home_screen.show()
    sys.exit(app.exec_())

