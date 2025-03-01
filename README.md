# Mini-Farm

Mini-Farm is a full-stack **FARM stack** (FastAPI, React, MongoDB) application designed to explore the integration of these technologies in a simple **to-do app**. This project serves as a learning playground for leveraging the FARM stack and can be used as a boilerplate for future projects.  

The app is containerised with **Docker Compose** for ease of deployment, and **NGINX** is used as a reverse proxy to manage frontend and backend services.  

---

## Features  

- **Task Management**: Add, edit, delete, and mark tasks as completed.  
- **User-Friendly Interface**: A clean and responsive React-based front end, powered by Vite for fast builds.  
- **Backend API**: A lightweight and efficient FastAPI backend for handling CRUD operations.  
- **Database Integration**: MongoDB for storing tasks and user data, ensuring scalability.
- **Authentication**: Basic authentication system (optional for MVP, to be expanded in future iterations).  
- **Containerisation**: Docker Compose simplifies deployment and configuration.  
- **Reverse Proxy**: NGINX handles request routing for seamless frontend and backend integration.  

---

## Tech Stack  

### Frontend  
- **React**: For building a modern and interactive user interface.  
<!-- - **Vite**: For a fast development server and build process.  
- **Tailwind CSS**: Provides clean and minimalistic design.   -->

### Backend  
- **FastAPI**: High-performance backend API framework.  
- **MongoDB**: NoSQL database for storing tasks and user data.  
- **uv**: Lightweight dependency and virtual environment manager.  

### Deployment  
- **Docker Compose**: Manages frontend, backend, and database containers.  
- **NGINX**: Acts as a reverse proxy to route frontend and backend traffic.  

---

## Prerequisites  

Ensure you have the following installed:  
- **Docker** (v20+ recommended)   
- **Node.js** (v16 or higher, for local frontend development)  
- **Python** (v3.12 or higher, for local backend development)  

---

## Getting Started  

### 1. Clone the Repository  
```bash
git clone https://github.com/Uokoroafor/mini-farm.git
cd mini-farm
```  

### 2. Set Up Environment Variables  
Create a `.env` file in the root directory with the following content:  
```env
SECRET_KEY=your_secret_key_here
MONGODB_URI='mongodb://mongo:27017'
DATABASE_NAME=''
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
PORT=3001
HOST="0.0.0.0"
```
This is also detailed in the `.env.sample` file

#### Generating a Secret Key
The backend of the application requires a secure secret key for authentication. To generate one:

1. Run the following command:
   ```bash
   make generate-secret
   ```
Copy the output and set it as the `SECRET_KEY` variable in the `.env` file

### 3. Run with Docker Compose  
1. Build and start the containers:  
   ```bash
   docker-compose up --build
   ```  
2. Access the application:  
   - Frontend: `http://localhost/5173`  
   - API: `http://localhost/3001`  

## Folder Structure  
```
mini-farm/  
├── backend/                  # FastAPI backend
│   ├── src/                  # Application source code
│   │   ├── auth/             # Authentication and authorization logic
│   │   ├── crud/             # CRUD operations for database interactions
│   │   ├── models/           # Database models (Pydantic & ORMs)
│   │   ├── routers/          # API route definitions
│   │   ├── schemas/          # Pydantic schemas for request/response validation
│   │   ├── tests/            # Backend test suite
│   │   ├── config.py         # Configuration settings (env variables, constants)
│   │   ├── database.py       # Database connection setup (MongoDB, SQLAlchemy, etc.)
│   │   ├── dependencies.py   # Dependency injection for FastAPI
│   │   ├── lifecycle.py      # Lifespan event handlers (startup/shutdown tasks)
│   │   ├── logger.py         # Logger setup (configured via `logging_config.yaml`)
│   │   ├── middleware.py     # Custom middleware (CORS, logging, security, etc.)
│   │   ├── main.py           # Entry point for FastAPI app
│   ├── Dockerfile            # Dockerfile for backend container
│   ├── logging_config.yaml   # Logging configuration file
│   ├── README.md             # Backend documentation
│   ├── uv.lock               # Dependency lockfile for `uv`
│   └── pyproject.toml        # Python dependencies and package configuration
├── frontend/                 # React frontend (Vite + React)
│   ├── src/                  # Frontend source code
│   │   ├── __tests__/        # Frontend unit and integration tests
│   │   ├── components/       # Reusable React components
│   │   ├── contexts/         # Context providers (Global state management)
│   │   ├── styles/           # CSS styles
│   │   ├── api.js            # API client to communicate with backend
│   │   ├── App.jsx           # Main App component
│   │   ├── main.jsx          # React entry point
│   ├── README.md             # Frontend documentation
│   ├── vite.config.js        # Vite configuration
│   └── package.json          # Frontend dependencies
├── nginx/                    # Nginx reverse proxy
│   └── nginx.conf            # Nginx configuration file
├── docker-compose.yaml       # Docker Compose file for managing services
├── Makefile                  # Makefile for build and deployment commands
└── README.md                 # Root documentation (project overview, setup)
```


<!-- ```  
mini-farm/  
├── backend/  
│   ├── src/  
│   │   ├── auth/           
│   │   ├── crud/       
│   │   ├── models/       
│   │   ├── routers/      
│   │   ├── schemas/        
│   │   ├── tests/        
│   │   ├── config.py      
│   │   ├── database.py       
│   │   ├── dependencies.py     
│   │   ├── lifecycle.py       
│   │   ├── logger.py      
│   │   ├── main.py      
│   │   └── middleware.py       
│   ├── Dockerfile           
│   ├── logging_config.yaml          
│   ├── README.md           
│   ├── uv.lock            
│   └── pyproject.toml      
├── frontend/  
│   ├── src/  
│   │   ├── __tests__/     
│   │   ├── components/     
│   │   ├── contexts/       
│   │   ├── styles        
│   │   ├── api.js       
│   │   ├── App.jsx          
│   │   ├── main.jsx         
│   │   ├── components/     
│   │   ├── pages/          
│   │   ├── App.jsx         
│   │   └── main.jsx        
│   ├── README.md            
│   ├── vite.config.js     
│   └── package.json       
├── nginx/  
│   └── nginx.conf         
├── docker-compose.yaml      
├── Makefile      
└── README.md               
```   -->
---

## Contribution Guidelines  

Contributions, issues, and feature requests are welcome! Feel free to open an issue or create a pull request.  

---

## License  

This project is licensed under the MIT License. See the `LICENSE` file for details.  

---  
