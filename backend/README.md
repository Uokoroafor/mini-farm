# Mini-Farm Backend

## Overview
The **Mini-Farm Backend** is built with **FastAPI** and uses **MongoDB** as the database. This backend provides a RESTful API to manage tasks in a **FARM stack** (**FastAPI, React, and MongoDB**) to-do application. It is containerised using Docker and can be orchestrated with Docker Compose and serves the final build using **Nginx** for production.

## Features
- **FastAPI** for high-performance backend services
- **MongoDB** as a NoSQL database
- **Docker & Docker Compose** for easy deployment
- **Swagger UI** for API documentation
- **Environment-based configuration**

---

## Setup and Installation

### 1. Clone the Repository
```sh
git clone https://github.com/Uokoroafor/mini-farm.git
cd mini-farm/backend
```

### 2. Create a Virtual Environment (Optional)
```sh
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
The backend dependencies are managed through [uv](https://docs.astral.sh/uv/getting-started/). To use, you must first[Install uv](https://docs.astral.sh/uv/getting-started/installation/) and then run the below command:
```sh
uv sync --frozen
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and configure the following variables
```sh
MONGODB_URI='mongodb://mongo:27017'
DATABASE_NAME=''
PORT=3001
HOST="0.0.0.0"
```

### 5. Run the Backend Server
```sh
uv run main.py
```

The API will be available at: **`http://localhost:3001`** by default 
Swagger UI: **`http://localhost:3001/docs`** by default

---
## Running with Docker

### 1. Build and Start the Backend Container
```sh
docker build -t mini-farm-backend .
docker run -p 3001:3001 --env-file .env mini-farm-backend
```

### 2. Using Docker Compose (Recommended)
To start both **MongoDB** and the backend:
```sh
docker-compose up --build
```
---

## License
This project is licensed under the **MIT License**.

---

## Contact
For questions create an issue in the repo.

Happy coding!

