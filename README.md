# 🕚 Auto Tweet 11:11 ✨

Bot simple en Python que publica automáticamente un tweet todos los días a las **11:11 hora de Chile**.

## 🚀 ¿Cómo usar?

1. **Crea un repositorio nuevo en GitHub** y sube estos archivos.
2. **Configura los secretos de la API de Twitter:**
   - Ve a `Settings > Secrets and variables > Actions > New repository secret`
   - Agrega:
     - `TWITTER_API_KEY`
     - `TWITTER_API_SECRET`
     - `TWITTER_ACCESS_TOKEN`
     - `TWITTER_ACCESS_SECRET`
3. **Listo.**  
   GitHub Actions ejecutará automáticamente el script todos los días a las 11:11 🇨🇱 (14:11 UTC).

## 💡 Nota
Puedes cambiar el mensaje del tweet modificando el texto en `tweet.py`.

## 🧩 Tecnologías
- Python 3.10+
- Tweepy
- GitHub Actions (cron)
