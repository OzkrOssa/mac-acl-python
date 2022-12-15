import typer
from mikrotik import MikrotikACL
from ubuquiti import UbiquitiACL
from settings import AP_HOSTS

def main():
    # Solicita al usuario que ingrese un código
    codigo: str = typer.prompt("Codigo")
    # Solicita al usuario que ingrese una dirección MAC
    mac: str = typer.prompt("Mac")
    # Solicita al usuario que ingrese un comentario
    comment: str = typer.prompt("Comentario")

    # Pregunta al usuario si desea continuar
    confirm = typer.confirm("¿Desea continuar?")

    # Si el usuario no desea continuar, se aborta el programa
    if not confirm:
        raise typer.Abort()

    # Intenta agregar la dirección MAC al dispositivo especificado en el código
    try:
        # Si el dispositivo es un Mikrotik, se crea una instancia de MikrotikACL y se agrega la dirección MAC
        if AP_HOSTS[codigo]["device"] == "mikrotik":
            mk = MikrotikACL(AP_HOSTS[codigo]["ip"])
            return mk.add_mac(mac, comment)
        # Si el dispositivo es un Ubiquiti, se crea una instancia de UbiquitiACL y se agrega la dirección MAC
        elif AP_HOSTS[codigo]["device"] == "ubiquiti":
            ubnt = UbiquitiACL(AP_HOSTS[codigo]["ip"])
            return ubnt.add_mac(mac, comment)
    # Si ocurre algún error, se imprime el mensaje de error
    except Exception as e:
        return e


if __name__ == "__main__":
    typer.run(main)


