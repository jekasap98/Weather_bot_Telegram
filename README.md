# Weather Telegram Bot

This project is a Telegram bot designed to provide weather information for various cities. It leverages the OpenWeatherMap API to fetch weather data and interacts with users via Telegram messages.


## Setup

To run the bot locally or deploy it to your server, follow these steps:

1. Clone the repository:

    ```
    git clone https://github.com/jekasap98/Weather_bot_Telegram.git
    ```

2. Install Docker and Docker Compose.

3. Create a Telegram bot and obtain the API key. Follow the instructions [here](https://core.telegram.org/bots#how-do-i-create-a-bot).

4. Obtain the API key for OpenWeatherMap. You can get it [here](https://openweathermap.org/appid).

5. Add your Telegram and OpenWeatherMap API keys to the `.env` file in the project directory.

6. Start the Docker container:

    ```
    docker compose up -d
    ```

7. Start interacting with the bot on Telegram!

## Usage

Once the bot is up and running, you can interact with it using the following commands:

- `/start`: Start the bot and get instructions.
- `/weather`: Get weather information for a specific city.

## Deployment Pipeline

The project includes a deployment pipeline for automating the deployment process. It consists of the following stages:

1. **Build Docker Image**: Builds the Docker image for the bot.
2. **Push Docker Image**: Pushes the Docker image to a Docker registry.
3. **Deploy Dev**: Deploys the bot to the development environment.
   
The pipeline utilizes global variables `${DOCKER_IMAGE_NAME}`, `${TOKEN_TEL}`, and `${TOKEN_API}` for configuration and credentials.  

## Webhook Configuration

The bot uses a webhook to receive updates from Telegram. Ensure that your environment has port 8083 open for incoming requests.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

