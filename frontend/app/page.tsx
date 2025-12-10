import NavBar from "@/components/layout/NavBar";
import { Search, MapPin, ArrowRight } from "lucide-react";
import Image from "next/image";
import { ListingCard } from "@/components/ui/ListingCard";

export default function Home() {
  return (
    <div className="min-h-screen bg-background font-sans text-foreground">
      <NavBar />

      {/* Hero Section */}
      <section className="relative flex min-h-[600px] flex-col items-center justify-center px-6 py-24 text-center">
        {/* Background Pattern/Image Placeholder */}
        <div className="absolute inset-0 -z-10 bg-[linear-gradient(to_bottom,rgba(255,255,255,0.9),rgba(255,255,255,0.5))]"></div>
        <div className="absolute inset-0 -z-20 bg-gray-100 opacity-50" style={{ backgroundImage: 'radial-gradient(#CBD5E1 1px, transparent 1px)', backgroundSize: '32px 32px' }}></div>

        <h1 className="max-w-4xl text-5xl font-extrabold tracking-tight sm:text-7xl text-primary">
          Find your place in the <span className="text-accent">world</span>.
        </h1>
        <p className="mt-6 max-w-2xl text-lg text-muted-foreground sm:text-xl">
          Discover modern homes, architectural masterpieces, and eco-friendly living spaces designed for your lifestyle.
        </p>

        {/* Search Bar */}
        <div className="mt-10 mx-auto flex w-full max-w-2xl flex-col gap-2 p-2 sm:flex-row sm:items-center sm:rounded-full sm:bg-white sm:shadow-lg sm:border sm:border-gray-200">
          <div className="flex flex-1 items-center px-4">
            <Search className="h-5 w-5 text-gray-400" />
            <input
              type="text"
              placeholder="City, Neighborhood, or Zip"
              className="w-full border-none bg-transparent p-4 text-base placeholder:text-gray-400 focus:outline-none focus:ring-0"
            />
          </div>
          <button className="h-full rounded-full bg-primary px-8 py-4 text-base font-semibold text-white transition-all hover:bg-primary/90 sm:py-3">
            Search
          </button>
        </div>
      </section>

      {/* Featured Listings Section */}
      <section className="mx-auto max-w-7xl px-6 py-24">
        <div className="mb-12 flex items-end justify-between">
          <div>
            <h2 className="text-3xl font-bold tracking-tight text-primary">Featured Listings</h2>
            <p className="mt-2 text-muted-foreground">Hand-picked properties for you.</p>
          </div>
          <a href="/search" className="hidden items-center text-sm font-semibold text-accent hover:underline sm:flex">
            View all listings <ArrowRight className="ml-1 h-4 w-4" />
          </a>
        </div>

        {/* Grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 */}
        <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
          {/* Card 1 */}
          <ListingCard
            title="Modern Loft in Downtown"
            city="San Francisco, CA"
            price="$1,250,000"
            beds={2}
            baths={2}
            sqft={1400}
            image="/placeholder-house-1.jpg" // We dont have real images yet
            tag="New Construction"
          />
          {/* Card 2 */}
          <ListingCard
            title="Eco-Friendly Villa"
            city="Austin, TX"
            price="$890,000"
            beds={4}
            baths={3}
            sqft={2800}
            image="/placeholder-house-2.jpg"
            tag="Eco-Modern"
          />
          {/* Card 3 */}
          <ListingCard
            title="Minimalist Studio"
            city="New York, NY"
            price="$750,000"
            beds={1}
            baths={1}
            sqft={850}
            image="/placeholder-house-3.jpg"
          />
        </div>
      </section>
    </div>
  );
}
