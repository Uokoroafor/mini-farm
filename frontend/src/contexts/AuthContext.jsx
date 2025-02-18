import React, { createContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api";

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    // Auto-login if token is present
    if (token) {
      const getUser = async () => {
        const user = await fetchUserProfile(token);
        setUser(user);
      };
      getUser();
    }
  }, [token]);

  const login = async (username, password) => {
    try {
      const formData = new URLSearchParams();
      formData.append("grant_type", "password");
      formData.append("username", username);
      formData.append("password", password);
      formData.append("scope", "");
      formData.append("client_id", "string");
      formData.append("client_secret", "string");

      const { data } = await api.post("/auth/login", formData, {
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
      });

      localStorage.setItem("token", data.access_token);
      console.log(data.access_token)
      setUser(data.user);
      navigate("/profile");
    } catch (error) {
      console.error("Login failed:", error.response?.data || error.message);
    }
  };

  const logout = () => {
    localStorage.removeItem("token");
    setUser(null);
    navigate("/");
  };

  const registerUser = async ({ username, email, password }) => {
    try {
      const response = await api.post(`/auth/register`, {
        username,
        email,
        hashed_password: password, // Convert password field to match API
      });
      console.log("User registered successfully:", response.data);
      navigate("/login");
      return response.data;
    } catch (error) {
      console.error("Registration error:", error);
      throw error;
    }
  };

  const fetchUserProfile = async (token) => {
    try {
      const response = await api.get(`/users/me/`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      console.log(response)
      return response.data;
    } catch (error) {
      console.error("Fetch user profile error:", error);
      throw error;
    }
  };

  return (
    <AuthContext.Provider
      value={{ user, login, logout, registerUser, fetchUserProfile }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export { AuthProvider, AuthContext };
