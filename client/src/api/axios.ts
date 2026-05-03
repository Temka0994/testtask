import axios from "axios";

export const serverInstance = axios.create({
    baseURL: process.env.REACT_APP_API_URL,
    timeout: 10000,
    headers: { "Content-Type": "application/json" }
});