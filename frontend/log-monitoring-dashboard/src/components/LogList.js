import React, { useEffect, useState } from "react";
import { fetchLogs } from "../api";

const LogList = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetchLogs().then(setLogs);
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-2">Logs</h2>
      <ul className="bg-gray-100 p-4 rounded">
        {logs.map((log, index) => (
          <li key={index} className="border-b p-2">
            [{log.timestamp}] {log.service} - {log.message}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default LogList;
