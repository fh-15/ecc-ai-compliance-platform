import { useEffect, useState } from "react";
import { apiRequest } from "../api/client";
import { getToken } from "../core/auth";

export default function Dashboard() {
  const [summary, setSummary] = useState<any>(null);

  useEffect(() => {
    apiRequest("/audit/dashboard/summary", "GET", null, getToken()!)
      .then(setSummary);
  }, []);

  if (!summary) return <div>Loading...</div>;

  return (
    <div>
      <h2>Dashboard</h2>
      <p>Total Audits: {summary.total_audits}</p>
      <p>Completed Audits: {summary.completed_audits}</p>
      <p>Average Score: {summary.average_score}%</p>
    </div>
  );
}
