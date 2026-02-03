import { useState } from "react";
import { apiRequest } from "../api/client";
import { saveToken } from "../core/auth";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function handleLogin() {
    const data = await apiRequest("/auth/login", "POST", {
      email,
      password
    });

    saveToken(data.access_token);
    window.location.href = "/dashboard";
  }

  return (
    <div>
      <h2>Login</h2>
      <input placeholder="Email" onChange={e => setEmail(e.target.value)} />
      <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}
