import { useEffect, useState } from "react";
import { apiRequest } from "../api/client";
import { getToken } from "../core/auth";

export default function Result({ auditId }: { auditId: number }) {
  const [score, setScore] = useState<any>(null);

  useEffect(() => {
    apiRequest(
      `/audit/score/${auditId}`,
      "POST",
      null,
      getToken()!
    ).then(setScore);
  }, [auditId]);

  if (!score) return <div>Calculating...</div>;

  return (
    <div>
      <h2>Result</h2>
      <p>Score: {score.score_percentage}%</p>
      <p>Gaps: {score.gaps_count}</p>
    </div>
  );
}
