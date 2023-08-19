# README.md

# Telethon Bulk Messaging Script

A Python script for sending bulk messages to multiple recipients on Telegram using the Telethon library.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This script allows you to send bulk messages to multiple recipients on Telegram using the Telethon library. It's especially useful for broadcasting announcements or updates to a group of users. The script is designed to be easy to configure and use.

## Prerequisites

Before using the script, make sure you have the following:

- Python 3.6 or higher installed on your system.
- Telethon library (`pip install telethon`) for interacting with the Telegram API.
- Openpyxl library (`pip install openpyxl`) for working with Excel files.

## Installation

1. Clone this repository to your local machine or download the source code as a ZIP file.
2. Install the required Python libraries by running:



## Configuration

1. Open the `config.py` file and fill in the necessary information:
- `num_aks`: Number of Telegram accounts (clients) you want to use.
- `phone_<i>`: Phone number for each client.
- `api_id_<i>`: API ID for each client (get this from https://my.telegram.org/auth).
- `api_hash_<i>`: API Hash for each client (get this from https://my.telegram.org/auth).
- `data`: A list of tuples containing the messages and files to send for each client.

2. Place the Excel files containing recipient information in the same directory with the names `input_1.xlsx`, `input_2.xlsx`, and `input_3.xlsx`.

## Usage

1. Run the script by executing the following command in your terminal:
```bash
python3 main.py
