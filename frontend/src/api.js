// src/api.js
import axios from "axios";

const API_URL = process.env.REACT_APP_API_URL; // Ensure this matches your .env file

const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Register a new user
export const registerUser = async (userData) => {
  const response = await api.post("/api/register/", userData); // Updated endpoint
  return response.data;
};

// Login an existing user
export const loginUser = async (userData) => {
  const response = await api.post("/api/login/", userData); // Updated endpoint
  return response.data;
};

// Fetch all produce
export const getProduce = async () => {
  const response = await api.get("/api/produce/");
  return response.data;
};

// Fetch all forum posts
export const getForumPosts = async () => {
  const response = await api.get("/api/forum/");
  return response.data;
};

// Fetch all equipment
export const getEquipment = async () => {
  const response = await api.get("/api/equipment/");
  return response.data;
};