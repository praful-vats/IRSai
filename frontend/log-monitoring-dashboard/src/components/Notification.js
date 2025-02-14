import { useEffect, useState } from "react";

const Notification = () => {
    const [messages, setMessages] = useState([]);
    const wsUrl = "ws://localhost:8000/ws";

    useEffect(() => {
        let ws;
        let reconnectInterval = 3000; // 3 seconds

        const connectWebSocket = () => {
            ws = new WebSocket(wsUrl);

            ws.onopen = () => {
                console.log("Connected to WebSocket");
            };

            ws.onmessage = (event) => {
                const data = JSON.parse(event.data);
                setMessages((prevMessages) => [
                    ...prevMessages,
                    { message: data.message, channel: data.channel }
                ]);
            };

            ws.onerror = (error) => {
                console.error("WebSocket Error:", error);
            };

            ws.onclose = () => {
                console.log("WebSocket Disconnected. Reconnecting...");
                setTimeout(connectWebSocket, reconnectInterval);
            };
        };

        connectWebSocket();
        return () => ws?.close();
    }, []);

    return (
        <div style={{ padding: "20px", border: "1px solid black", width: "400px" }}>
            <h2>Real-Time Notifications</h2>
            <ul>
                {messages.map((msg, index) => (
                    <li key={index} style={{ color: getColor(msg.channel) }}>
                        [{msg.channel.toUpperCase()}] {msg.message}
                    </li>
                ))}
            </ul>
        </div>
    );
};

// Utility function to color-code alerts
const getColor = (channel) => {
    switch (channel) {
        case "slack":
            return "blue";
        case "email":
            return "green";
        case "pagerduty":
            return "red";
        default:
            return "black";
    }
};

export default Notification;
