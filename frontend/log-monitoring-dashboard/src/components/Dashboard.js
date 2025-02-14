import React from "react";
import LogList from "./LogList";
import IncidentList from "./IncidentList";

const Dashboard = () => {
  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold">Dashboard</h2>
      <div className="grid grid-cols-2 gap-4">
        <LogList />
        <IncidentList />
      </div>
    </div>
  );
};

export default Dashboard;
