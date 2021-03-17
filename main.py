from usuarios import acciones

print("""
Acciones disponibles:
    - Login
    - Registro
""")

hazEl = acciones.Acciones()
accion = input("¿Qué quieres hacer? -> ")

if accion == "login":
    hazEl.login()

elif accion == "registro":
    hazEl.registro()