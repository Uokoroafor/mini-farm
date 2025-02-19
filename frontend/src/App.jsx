import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider } from "./contexts/AuthContext";
import { ToDoProvider } from "./contexts/ToDoContext";
import NavBar from "./components/NavBar";
import Login from "./components/auth/Login";
import Register from "./components/auth/Register"
import Dashboard from "./components/todo/Dashboard";
import UserProfile from "./components/user/UserProfile";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import "./styles/App.css";

function App() {
  return (
    <Router className="main-content">
      <AuthProvider>
        <ToDoProvider>
          <NavBar />
          <Routes>
            {/* Public Routes */}
            <Route path="/" element={<Navigate to="/login" />} />
            <Route path="/login" element={<Login />} />
            <Route path="/dashboard" element={<Dashboard />}/>
            <Route path="/register" element={<Register />}/>
            {/* Protected Routes */}
            
            <Route
              path="/profile"
              element={<ProtectedRoute><UserProfile /></ProtectedRoute>}
            />

            {/* Catch-All Route */}
            <Route path="*" element={<div>404 Page Not Found</div>} />
          </Routes>
        </ToDoProvider>
      </AuthProvider>
    </Router>
  );
}

export default App;
