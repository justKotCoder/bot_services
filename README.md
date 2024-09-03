# Telegram Service Management Bot

This project is a Telegram bot built using Python and the `aiogram` library. The bot is designed for managing user services, including registration, adding, editing, and deleting services, as well as administering services with approval or rejection functionalities.

## Features

- **User Registration**: Users can register by providing their name.
- **Add Services**: Registered users can add their services with a name, description, and price.
- **Edit Services**: Users can edit the name, description, and price of their services.
- **Delete Services**: Users can delete their services.
- **View Services**: Users can view a list of their services with statuses (approved, pending approval, rejected).
- **Administer Services**: The administrator can view services pending approval and decide to approve or reject them with a reason.

## Project Structure

- `bot.py`: The main file of the project containing the primary settings and command handlers.
- `handlers/`: Package with command and message handlers.
  - `start.py`: Handler for the `/start` command.
  - `registration.py`: Handler for user registration.
  - `services.py`: Handlers for adding, editing, and deleting services.
  - `admin.py`: Handler for administrative commands.
  - `callback.py`: Handler for callback queries from inline buttons.
- `states/`: Package containing state definitions for the Finite State Machine (FSM).
  - `states.py`: State definitions for registration and service management.
- `database/`: Package for database operations.
  - `db.py`: Script for initializing the database and performing basic operations.
- `utils/`: Utility functions.
  - `utils.py`: Common utility functions.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/justKotCoder/bot_services.git
   cd bot_services
