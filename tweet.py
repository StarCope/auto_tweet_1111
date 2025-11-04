import tweepy
import os
from datetime import datetime

# Autenticación con las variables de entorno del workflow
client = tweepy.Client(
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_SECRET")
)

# Generar el mensaje
fecha = datetime.now().strftime("%d/%m/%Y")
tweet = f"Son las 11:11 — pide tu deseo ✨ ({fecha})"

# Enviar el tweet
try:
    response = client.create_tweet(text=tweet)
    print(f"Tweet publicado correctamente: {response.data}")
except Exception as e:
    print(f"Error al publicar el tweet: {e}")
