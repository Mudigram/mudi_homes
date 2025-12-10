import { api } from "@/lib/api";

export async function getBlogs() {
  const res = await api.get("/blogs/");
  return res.data;
}
