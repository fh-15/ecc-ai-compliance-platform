import Login from "./auth/Login";
import Register from "./auth/Register";
import Dashboard from "./dashboard/Dashboard";
import StartAudit from "./audit/StartAudit";
import Guard from "./core/guard";

export default function App() {
  const path = window.location.pathname;

  if (path === "/register") return <Register />;
  if (path === "/dashboard")
    return (
      <Guard>
        <Dashboard />
      </Guard>
    );
  if (path === "/audit/start")
    return (
      <Guard>
        <StartAudit />
      </Guard>
    );

  return <Login />;
}
