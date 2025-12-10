import axios from "axios";

export const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

// Attach token if available
api.interceptors.request.use((config) => {
  if (typeof window !== "undefined") {
    const token = localStorage.getItem("token");
    if (token) config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});
