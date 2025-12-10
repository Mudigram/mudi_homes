import { getBlogs } from "@/services/blogs";

export default async function BlogsPage() {
  const res = await getBlogs();
const blogs = res.items; 

  return (
    <div className="max-w-4xl mx-auto mt-10">
      <h1 className="text-3xl font-bold mb-6">Blogs</h1>

      <div className="space-y-4">
        {blogs.map((b: any) => (
          <div key={b.id} className="p-4 border rounded">
            <h2 className="font-semibold text-xl">{b.title}</h2>
            <p>{b.description}</p>
            <a href={`/blogs/${b.slug}`} className="text-blue-600 underline">
              Read more →
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}
