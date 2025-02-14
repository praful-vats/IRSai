import React, { useEffect, useState } from "react";
import io from "socket.io-client";

const socket = io("http://your-api-gateway-ip");

const IncidentList = () => {
  const [incidents, setIncidents] = useState([]);

  useEffect(() => {
    socket.on("newIncident", (incident) => {
      setIncidents((prev) => [incident, ...prev]);
    });

    return () => socket.off("newIncident");
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-2">Incidents</h2>
      <ul className="bg-red-100 p-4 rounded">
        {incidents.map((incident, index) => (
          <li key={index} className="border-b p-2">
            🚨 {incident.message} ({incident.level})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default IncidentList;
