import { useState } from "react";
import { apiRequest } from "../api/client";
import { getToken } from "../core/auth";

export default function StartAudit() {
  const [controlId, setControlId] = useState("");

  async function start() {
    const res = await apiRequest(
      "/audit/start",
      "POST",
      { control_id: Number(controlId) },
      getToken()!
    );
    window.location.href = `/audit/${res.id}`;
  }

  return (
    <div>
      <h2>Start Audit</h2>
      <input
        placeholder="ECC Control ID"
        onChange={(e) => setControlId(e.target.value)}
      />
      <button onClick={start}>Start</button>
    </div>
  );
}
