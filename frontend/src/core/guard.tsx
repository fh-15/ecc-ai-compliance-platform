import { ReactNode } from "react";
import { getToken } from "./auth";

export default function Guard({ children }: { children: ReactNode }) {
  const token = getToken();
  if (!token) {
    window.location.href = "/";
    return null;
  }
  return <>{children}</>;
}
