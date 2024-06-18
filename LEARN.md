
# WhatsApp Automation with Typebot API

## Overview

This project sets up an automation system for WhatsApp using Selenium and Typebot API. The automation allows you to handle chat interactions with users through WhatsApp, leveraging the Typebot API to manage conversations.

## Prerequisites

Ensure you have the following installed on your system:

- Docker

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/marco0antonio0/api-plugin-typebot
   cd api-plugin-typebot
   ```

2. **Create and Configure `.env` File**

   Create a `.env` file in the root directory of the project with the following content:

   ```env
   TYPEBOT_ID=<your typebot key>
   TOKEN=<your token access typebot flux>
   BASE_URL=<your URL chat typebot>
   ```

   Replace `<your typebot key>`, `<your token access typebot flux>`, and `<your URL chat typebot>` with your actual Typebot credentials and base URL.

3. **Build and Run Docker Container**

   Ensure you have Docker installed and running. Execute the following commands to build and run the Docker container:
    **build image**

   ```bash
   docker build -t whatsapp-automation .
   ```

     **run container with image**

   ```bash
    docker run -d -t --name whatsapp-automatio --shm-size 2g whatsapp-automation
   ```

4. **View Logs and Scan QR Code**

   After the container is created, you need to scan the QR code to log in to WhatsApp. To view the QR code, run:

   ```bash
   docker logs -f whatsapp-automation
   ```

   This command will display the logs of the running container, where you will find the QR code for logging into WhatsApp. Scan this QR code with your WhatsApp mobile app to complete the login process.

5. **Access the Automation**

   Once the Docker container is running and you have logged into WhatsApp, the automation script will start, connecting to WhatsApp and handling messages according to the logic defined in `main.py`.

## Project Structure

- `./main.py`: The main script to start the automation, handle incoming messages, and interact with the Typebot API.
- `./services/automation.py`: Contains the logic for WhatsApp automation using Selenium.
- `./services/TypebotAPI.py`: Handles interactions with the Typebot API, including starting chats and sending messages.
- `./services/others services`: qrcode generate for terminal,package request.
- `./Dockerfile`: The Docker configuration to set up the environment, install dependencies, and run the application.
- `./requirements.txt`: Lists the Python dependencies needed for the project.
- `./.env`: Contains environment variables for Typebot credentials and base URL.

## How to Use

1. **Configure Environment Variables**

   Ensure the `.env` file is correctly set up with your Typebot credentials and base URL.

2. **Start Docker Container**

   ```bash
   docker build -t whatsapp-automation .whatsapp-automation
   ```

3. **View Logs and Scan QR Code**

   ```bash
   docker logs -f whatsapp-automation
   ```

   Scan the QR code displayed in the logs with your WhatsApp mobile app to log in.

4. **Interact with the Bot**

   The bot will automatically start and connect to WhatsApp. It will listen for new messages and interact with users based on the logic defined in the scripts.

5. **Stop Docker Container**

   To stop the container, run:

   ```bash
   docker stop whatsapp-automation
   ```

   To remove the container, run:

   ```bash
   docker rm whatsapp-automation
   ```

## Contribution

Feel free to fork this repository, submit issues, and make pull requests to contribute to the project.

## License

This project is licensed under the MIT License.

---

This README provides a comprehensive guide to setting up and using the WhatsApp automation project with the Typebot API. By following these steps, you can efficiently manage chat interactions through WhatsApp.

## Acknowledgment

This repository was inspired by the following project:
<https://github.com/marco0antonio0/py-connector-whatsapp-unofficia>
