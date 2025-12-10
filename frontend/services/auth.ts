import { api } from "@/lib/api";

export async function login(email: string, password: string) {
  const form = new FormData();
  form.append("username", email);
  form.append("password", password);

  const res = await api.post("/users/login", form);
  localStorage.setItem("token", res.data.access_token);

  return res.data;
}

export async function register(data: any) {
  const res = await api.post("/users/register", data);
  return res.data;
}

export async function getProfile() {
  const res = await api.get("/users/me");
  return res.data;
}
