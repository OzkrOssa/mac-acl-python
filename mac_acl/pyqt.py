import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from ubuquiti import UbiquitiACL

# Crea la ventana principal
ventana = QWidget()
ventana.setWindowTitle("Registro de direcciones MAC")

# Crea una etiqueta para el host
host_etiqueta = QLabel(ventana)
host_etiqueta.setText("Host:")
host_etiqueta.move(10, 10)

# Crea una caja de texto para el host
host_caja = QLineEdit(ventana)
host_caja.move(100, 10)

# Crea una etiqueta para la dirección MAC
mac_etiqueta = QLabel(ventana)
mac_etiqueta.setText("Dirección MAC:")
mac_etiqueta.move(10, 40)

# Crea una caja de texto para la dirección MAC
mac_caja = QLineEdit(ventana)
mac_caja.move(100, 40)

# Crea una etiqueta para el comentario
comentario_etiqueta = QLabel(ventana)
comentario_etiqueta.setText("Comentario:")
comentario_etiqueta.move(10, 70)

# Crea una caja de texto para el comentario
comentario_caja = QLineEdit(ventana)
comentario_caja.move(100, 70)

# Crea una función que se ejecuta cuando se presiona el botón "Registrar"
def registrar():
    ubnt = UbiquitiACL(host_caja.text())
    resultado = ubnt.add_mac(mac_caja.text(), comentario_caja.text())
    if "error" in resultado:
        QMessageBox.critical(ventana, "Error", resultado["error"])
    else:
        QMessageBox.information(ventana, "Registro exitoso", resultado["message"])

# Crea un botón "Registrar"
registrar_boton = QPushButton(ventana)
registrar_boton.setText("Registrar")
registrar_boton.move(10, 110)
registrar_boton.clicked.connect(registrar)

# Muestra la ventana
ventana.show()

# Inicia la aplicación
app = QApplication(sys.argv)
sys.exit(app.exec_())
