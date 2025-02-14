import axios from "axios";

const API_BASE = "http://your-api-gateway-ip";

export const fetchLogs = async () => {
  const response = await axios.get(`${API_BASE}/logs`);
  return response.data;
};

export const fetchIncidents = async () => {
  const response = await axios.get(`${API_BASE}/incidents`);
  return response.data;
};

export const sendNotification = async (message, channel, recipient) => {
    try {
        const response = await fetch("http://localhost:8000/send-notification/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message, channel, recipient })
        });

        return await response.json();
    } catch (error) {
        console.error("Error sending notification:", error);
        return { status: "error", message: "Failed to send notification" };
    }
};

