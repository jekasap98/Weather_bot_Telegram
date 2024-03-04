FROM python:3.9.18-slim-bullseye

RUN mkdir -p /app/weather-bot
WORKDIR /app/weather-bot
COPY bot.py open_weather_api.py requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "bot.py"]


