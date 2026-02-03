import { useState } from "react";
import { apiRequest } from "../api/client";
import { getToken } from "../core/auth";

export default function AnswerAudit({ auditId }: { auditId: number }) {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  async function submit() {
    await apiRequest(
      `/audit/answer/${auditId}`,
      "POST",
      { question, answer },
      getToken()!
    );
    setQuestion("");
    setAnswer("");
    alert("Answer submitted");
  }

  return (
    <div>
      <h2>Answer Audit</h2>
      <input
        placeholder="Question"
        onChange={(e) => setQuestion(e.target.value)}
      />
      <input
        placeholder="Answer (yes/no)"
        onChange={(e) => setAnswer(e.target.value)}
      />
      <button onClick={submit}>Submit</button>
    </div>
  );
}
