import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Dashboard from "./components/Dashboard";
import LogList from "./components/LogList";
import IncidentList from "./components/IncidentList";
import Notification from "./components/Notification";

function App() {
  return (
    <Router>
      <Navbar />
      <div style={{ display: "flex", justifyContent: "space-between" }}>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/logs" element={<LogList />} />
          <Route path="/incidents" element={<IncidentList />} />
        </Routes>
        <Notification />
      </div>
    </Router>
  );
}

export default App;
