import random
import requests

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gene_emodji():
    emodji = ["😂", "😍", "😭", "😘", "🥰", "😊", "🤔", "🤣", "😊", "😅", "😢"]
    return random.choice(emodji)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


def get_weather_info_url():    
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
    querystring = {"lat":"-12.051170552447141","lon":"-77.03076856051939","units":"metric","lang":"es"}
    headers = {
	"x-rapidapi-key": "dd44b94613msh2c82005f6597c3fp17fafcjsnf6fe00f40a2c",
	"x-rapidapi-host": "weatherbit-v1-mashape.p.rapidapi.com"
}
    res = requests.get(url, headers=headers, params=querystring)
    data = res.json()
    
    #Regresar la información ordenada
    weather_data = data['data'][0]
    formatted_data = (
        f"Ciudad: {weather_data['city_name']}\n"
        f"Temperatura: {weather_data['temp']}°C\n"
        f"Descripción: {weather_data['weather']['description']}\n"
        f"Viento: {weather_data['wind_spd']} mph desde {weather_data['wind_cdir_full']}\n"
        f"Humedad: {weather_data['rh']}%\n"
        f"Presión: {weather_data['pres']} mb\n"
        f"Índice UV: {weather_data['uv']}\n"
        f"Visibilidad: {weather_data['vis']} millas\n"
        f"Hora de observación: {weather_data['ob_time']}\n"
    )
    return(formatted_data)

def get_memes_url():
    url = 'https://api.imgflip.com/get_memes'
    res = requests.get(url)
    data = res.json()

    if data['success']:
        memes = data['data']['memes']
        return memes
    
def get_random_meme():
    memes = get_memes_url()
    return random.choice(memes)

def info_list():
    info_list_commands = (
        "**$hello**: El bot dice hola\n"
        "**$bye**: El bot dice adiós\n"
        "**$password**: genera una contraseña de 10 caracteres\n"
        "**$meme**: El bot envia un meme específico\n"
        "**$meme_aleatorio**: El bot envia un meme aleatoria de un conjunto de 3\n"
        "**$gen_emodji**: Genera un emoji aleatorio\n"
        "**$duck**: Foto de patos\n"
        "**$dog**: Foto de perros\n"
        "**$weather**: Muestra información sobre el tiempo\n"
        "**$memeapi**: El bot envia una plantilla de meme aleatorio de una pagina\n"
    )
    return info_list_commands
