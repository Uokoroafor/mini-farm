# Mini-Farm

Mini-Farm is a full-stack **FARM stack** (FastAPI, React, MongoDB) application designed to explore the integration of these technologies in a simple yet robust **to-do app**. This project serves as a learning playground for leveraging the FARM stack and can be used as a boilerplate for future projects.  

The app is containerised with **Docker Compose** for ease of deployment, and **NGINX** is used as a reverse proxy to manage frontend and backend services.  

---

## Features  

- **Task Management**: Add, edit, delete, and mark tasks as completed.  
- **User-Friendly Interface**: A clean and responsive React-based front end, powered by Vite for fast builds.  
- **Backend API**: A lightweight and efficient FastAPI backend for handling CRUD operations.  
- **Database Integration**: MongoDB for storing tasks and user data, ensuring scalability.
- **Authentication**: Basic authentication system (optional for MVP, to be expanded in future iterations).  
- **Containerization**: Docker Compose simplifies deployment and configuration.  
- **Reverse Proxy**: NGINX handles request routing for seamless frontend and backend integration.  

---

## Tech Stack  

### Frontend  
- **React**: For building a modern and interactive user interface.  
- **Vite**: For a fast development server and build process.  
- **Tailwind CSS**: Provides clean and minimalistic design.  

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
- **Docker Compose** (v2.0+ recommended)  
- **Node.js** (v16 or higher, for local frontend development)  
- **Python** (v3.10 or higher, for local backend development)  

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
# Backend Environment
MONGO_URI=mongodb://mongodb:27017/farmiliar
SECRET_KEY=your_secret_key_here

# Frontend Environment
VITE_API_BASE_URL=http://localhost/api
```  

### 3. Run with Docker Compose  
1. Build and start the containers:  
   ```bash
   docker-compose up --build
   ```  
2. Access the application:  
   - Frontend: `http://localhost`  
   - API: `http://localhost/api`  

### 4. Run Locally (Optional)  

#### Backend  
1. Navigate to the backend folder:  
   ```bash
   cd backend
   ```  
2. Set up a virtual environment with **uv**:  
   ```bash
   uv venv create
   uv venv enter
   ```  
3. Install dependencies:  
   ```bash
   uv install
   ```  
4. Run the backend server:  
   ```bash
   uvicorn app.main:app --reload
   ```  
   The API will be available at `http://127.0.0.1:8000`.  

#### Frontend  
1. Navigate to the frontend folder:  
   ```bash
   cd frontend
   ```  
2. Install dependencies:  
   ```bash
   npm install
   ```  
3. Start the Vite development server:  
   ```bash
   npm run dev
   ```  
   The React app will run at `http://localhost:5173`.  

---

## Folder Structure  

```  
mini-farm/  
├── backend/  
│   ├── app/  
│   │   ├── main.py         # Entry point for FastAPI  
│   │   ├── models.py       # MongoDB data models  
│   │   ├── routes.py       # API endpoints  
│   │   ├── schemas.py      # Data validation schemas  
│   │   └── utils.py        # Utility functions  
│   ├── uv.lock             # uv dependency lock file  
│   └── pyproject.toml      # Python dependencies  
├── frontend/  
│   ├── src/  
│   │   ├── components/     # Reusable React components  
│   │   ├── pages/          # Page components  
│   │   ├── App.jsx         # Main app entry  
│   │   └── main.jsx        # React DOM rendering  
│   ├── vite.config.js      # Vite configuration  
│   └── package.json        # Frontend dependencies  
├── nginx/  
│   └── nginx.conf          # NGINX configuration  
├── docker-compose.yml      # Docker Compose file  
├── Dockerfile.backend      # Dockerfile for backend  
├── Dockerfile.frontend     # Dockerfile for frontend  
└── README.md               # Project documentation  
```  

---

## Future Enhancements  

- Add user authentication (JWT or OAuth).  
- Implement drag-and-drop task reordering.  
- Integrate due dates and reminders.  
- Add real-time features using WebSockets.  
- Extend Docker Compose to support scaling the backend and database.  

---

## Contribution Guidelines  

Contributions, issues, and feature requests are welcome! Feel free to open an issue or create a pull request.  

---

## License  

This project is licensed under the MIT License. See the `LICENSE` file for details.  

---  
