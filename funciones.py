import asyncio
from tapo import ApiClient, Color

class Control:
    def __init__(self):
        self.username = "" # Colocar email de la cuenta Tapo
        self.password = "" # Colocar contraseña de la cuenta Tapo
        self.ip = "" # Colocar IP de las luces led (Entrar a la aplicacion Tapo del celular / Seleccionar la tira led L920 / Configuracion del dispositivo / Informacion del dispositivo)

        asyncio.run(self.conectar())

    async def conectar(self):
        client = ApiClient(self.username, self.password)
        try:
            self.device = await client.l900(self.ip)
            print("\033[92m> Conexión exitosa con el dispositivo.\033[0m")
        except Exception as e:
            print(f"\033[91m> Error al conectar: {e}\033[0m")

    async def obtener_estado_luz(self):
        try:
            device_info = await self.device.get_device_info_json()
            device_on = device_info.get("device_on")
            if device_on is not None:
                if device_on:
                    print("\033[92m> La luz está encendida.\033[0m")
                    return True
                else:
                    print("\033[92m> La luz está apagada.\033[0m")
                    return False
            else:
                print("\033[91m> No se pudo determinar el estado de la luz. Verifica la respuesta del dispositivo.\033[0m")
        except Exception as e:
            print(f"\033[91m> Error al obtener el estado de la luz: {e}\033[0m")

    async def encender_apagar_luz(self):
        try:
            estado = await self.obtener_estado_luz()
            if estado == True:
                await self.device.off()
                print("\033[92m> Luz apagada.\033[0m")
            elif estado == False:
                await self.device.on()
                print("\033[92m> Luz encendida.\033[0m")
            else:
                print("\033[93m> No se realizó ninguna acción.\033[0m")
        except Exception as e:
            print(f"\033[91m> Error al encender/apagar la luz: {e}\033[0m")

    async def obtener_estado_brillo(self):
        try:
            device_info = await self.device.get_device_info_json()
            brightness = device_info.get("brightness")
            if brightness is not None:
                print(f"\033[92m> El brillo está en {brightness}%.\033[0m")
                return brightness
            else:
                print("\033[93m> No se pudo conseguir el estado del brillo.\033[0m")
        except Exception as e:
            print(f"\033[91m> Error al obtener el estado del brillo: {e}\033[0m")

    async def cambiar_brillo_luz(self, valor: int):
        try:
            await self.device.on()
            await self.device.set_brightness(valor)
            print(f"\033[92m> Se cambió el brillo al %{valor}.\033[0m")
        except Exception as e:
            print(f"\033[91m> Error al cambiar el brillo de la luz: {e}\033[0m")

    async def cambiar_color_luz_google_home(self, nuevo_color: Color):
        try:
            await self.device.on()
            await self.device.set_color(nuevo_color)
            print(f"\033[92m> Se cambió el color de la luz a {nuevo_color}.\033[0m")
        except Exception as e:
            print(f"\033[91m> Error al cambiar el color de la luz: {e}\033[0m")

    async def obtener_estado_hue(self):
            try:
                device_info = await self.device.get_device_info_json()
                hue = device_info.get("hue")
                if hue is not None:
                    print(f"\033[92m> El hue está en {hue}%.\033[0m")
                    return hue
                else:
                    print("\033[93m> No se pudo conseguir el estado del hue.\033[0m")
            except Exception as e:
                print(f"\033[91m> Error al obtener el hue: {e}\033[0m")

    async def obtener_estado_saturacion(self):
            try:
                device_info = await self.device.get_device_info_json()
                saturation = device_info.get("saturation")
                if saturation is not None:
                    print(f"\033[92m> La saturación está en {saturation}%.\033[0m")
                    return saturation
                else:
                    print("\033[93m> No se pudo conseguir la saturación.\033[0m")
            except Exception as e:
                print(f"\033[91m> Error al obtener la saturación: {e}\033[0m")

    async def cambiar_color_luz(self, hue: int, saturation: int):
        try:
            await self.device.on()
            await self.device.set_hue_saturation(hue, saturation)
            print(f"\033[92m> Se cambió el color de la luz.\033[0m")
        except Exception as e:
            print(f"\033[91m> Error al cambiar el color de la luz: {e}\033[0m")


class Funciones(Control):
    def estado_luz(self,*args, **kwargs):
        estado = asyncio.run(self.obtener_estado_luz())
        return estado

    def power(self, *args, **kwargs):
        asyncio.run(self.encender_apagar_luz())

    def estado_brillo(self, *args, **kwargs):
        valor = asyncio.run(self.obtener_estado_brillo())
        return valor

    def brillo(self, valor, *args, **kwargs):
        valor = int(valor.control.value)
        asyncio.run(self.cambiar_brillo_luz(valor))

    def colores_google(self, color, *args, **kwargs):
        color = color.control.value
        colores = {
                'AliceBlue': Color.AliceBlue,
                'LightGoldenrod': Color.LightGoldenrod,
                'LemonChiffon': Color.LemonChiffon,
                'Gold': Color.Gold,
                'Peru': Color.Peru,
                'Chocolate': Color.Chocolate,
                'SandyBrown': Color.SandyBrown,
                'Coral': Color.Coral,
                'Pumpkin': Color.Pumpkin,
                'Tomato': Color.Tomato,
                'Vermilion': Color.Vermilion,
                'OrangeRed': Color.OrangeRed,
                'Pink': Color.Pink,
                'Crimson': Color.Crimson,
                'HotPink': Color.HotPink,
                'Smitten': Color.Smitten,
                'MediumPurple': Color.MediumPurple,
                'BlueViolet': Color.BlueViolet,
                'Indigo': Color.Indigo,
                'LightSkyBlue': Color.LightSkyBlue,
                'CornflowerBlue': Color.CornflowerBlue,
                'Ultramarine': Color.Ultramarine,
                'DeepSkyBlue': Color.DeepSkyBlue,
                'Azure': Color.Azure,
                'NavyBlue': Color.NavyBlue,
                'LightTurquoise': Color.LightTurquoise,
                'Aquamarine': Color.Aquamarine,
                'Turquoise': Color.Turquoise,
                'LightGreen': Color.LightGreen,
                'Lime': Color.Lime,
                'ForestGreen': Color.ForestGreen,
            }
        if color in colores:
            asyncio.run(self.cambiar_color_luz_google_home(colores[color]))

    def obetener_hue(self):
        valor = asyncio.run(self.obtener_estado_hue())
        return valor
    
    def obetener_saturacion(self):
        valor = asyncio.run(self.obtener_estado_saturacion())
        return valor

    def cambiar_hue(self, valor):
        hue = int(valor.control.value)
        saturacion = asyncio.run(self.obtener_estado_saturacion())
        asyncio.run(self.cambiar_color_luz(hue, saturacion))

    def cambiar_saturacion(self, valor):
        hue = asyncio.run(self.obtener_estado_hue())
        saturacion = int(valor.control.value)
        asyncio.run(self.cambiar_color_luz(hue, saturacion))