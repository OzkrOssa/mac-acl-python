import tkinter as tk
from tkinter import ttk
from mac_acl.ubiquiti import UbiquitiACL
from mac_acl.mikrotik import MikrotikACL
from mac_acl.settings import AP_HOSTS

# Crea la ventana principal
ventana = tk.Tk()
ventana.title("Registro de direcciones MAC")

# Crea una etiqueta para el host
ttk.Label(ventana, text="Codigo:").grid(row=0, column=0)

# Crea una caja de texto para el host
code = tk.StringVar()
code_entry = ttk.Entry(ventana, textvariable=code)
code_entry.grid(row=0, column=1)

# Crea una etiqueta para la dirección MAC
ttk.Label(ventana, text="Dirección MAC:").grid(row=1, column=0)

# Crea una caja de texto para la dirección MAC
mac = tk.StringVar()
mac_entry = ttk.Entry(ventana, textvariable=mac)
mac_entry.grid(row=1, column=1)

# Crea una etiqueta para el comentario
ttk.Label(ventana, text="Comentario:").grid(row=2, column=0)

# Crea una caja de texto para el comentario
comentario = tk.StringVar()
comentario_entry = ttk.Entry(ventana, textvariable=comentario)
comentario_entry.grid(row=2, column=1)

# Crea una función que se ejecuta cuando se presiona el botón "Registrar"
def registrar():
    print("registrar")
    if AP_HOSTS[code.get()]['device'] == "mikrotik":
        try:
            mk = MikrotikACL(AP_HOSTS[code.get()]['ip'],plaintext_login=True)
        except Exception as e:
            mk = MikrotikACL(AP_HOSTS[code.get()]['ip'])
        resultado = mk.add_mac(mac.get(), comentario.get())
        if "error" in resultado:
            ttk.Label(ventana, text=code.get()+resultado["error"], foreground="red").grid(row=4, column=0, columnspan=2)
        else:
            ttk.Label(ventana, text=code.get()+resultado["message"], foreground="green").grid(row=4, column=0, columnspan=2)
    elif AP_HOSTS[code.get()]['device'] == "ubiquiti":
        ubnt = UbiquitiACL(AP_HOSTS[code.get()]['ip'])
        print(mac.get())
        resultado = ubnt.add_mac(mac.get(), comentario.get())
        if "error" in resultado:
            ttk.Label(ventana, text=code.get()+resultado["error"], foreground="red").grid(row=4, column=0, columnspan=2)
        else:
            ttk.Label(ventana, text=code.get()+resultado["message"], foreground="green").grid(row=4, column=0, columnspan=2)

# Crea un botón "Registrar"
registrar_boton = ttk.Button(ventana, text="Registrar", command=registrar)
registrar_boton.grid(row=3, column=0, columnspan=2)

# Inicia la interfaz gráfica
ventana.mainloop()
