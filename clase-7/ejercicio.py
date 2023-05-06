#  Escriba una clase MobilePhone que represente un telefono movil.
#  Atributos
#  manufacturer ( cadena de texto)
#  screen_size (flotante)
#  apps (lista de cadenas de texto)
#  status (false: apagado, True: encendido)
#  Metodos
#  _init_(self, manufacturer, screen_size, num:cores)
# power_on(self)
# power_off(self)
#  install_app(self, app)
# uninstall_app(self, app)

class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.status = False
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = ['Wasap', 'Instagram', 'Youtube']

    def power_on(self):
        print("Encendiendo")
        self.status = True

    def power_off(self):
        print("Apagando")
        self.status = False

    def install_app(self, app):
        print(f"Instalando app {app}")
        self.apps.append(app)

    def uninstall_app(self, app):
        print(f"Desinstalando app {app}")
        self.apps.remove(app)

iphone = MobilePhone('Apple Inc', 6.1, 6)

iphone.power_on()
print('Iphone Encendido', iphone.status)
iphone.install_app('TikTok')
print('Aplicaciones:', iphone.apps)
iphone.uninstall_app('TikTok')
iphone.power_off()
print('Iphone Apagado', iphone.status)
