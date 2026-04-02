import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from railfence.ui.railfence import Ui_MainWindow 

class RailFenceApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_en.clicked.connect(self.call_api_encrypt)
        self.ui.btn_de.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.ui.txt_cipher.setText(response.json()["encrypted_text"])
                QMessageBox.information(self, "Thông báo", "Mã hóa thành công!")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể kết nối API: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.ui.txt_plain.setText(response.json()["decrypted_text"])
                QMessageBox.information(self, "Thông báo", "Giải mã thành công!")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể kết nối API: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RailFenceApp()
    window.show()
    sys.exit(app.exec_())