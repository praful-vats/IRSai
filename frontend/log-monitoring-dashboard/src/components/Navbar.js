import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="p-4 bg-blue-500 text-white flex justify-between">
      <h1 className="text-xl font-bold">Log Monitoring</h1>
      <div>
        <Link to="/" className="px-2">Home</Link>
        <Link to="/logs" className="px-2">Logs</Link>
        <Link to="/incidents" className="px-2">Incidents</Link>
      </div>
    </nav>
  );
};

export default Navbar;
