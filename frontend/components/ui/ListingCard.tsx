import { MapPin } from "lucide-react";

interface ListingCardProps {
    title: string;
    city: string;
    price: string;
    beds: number;
    baths: number;
    sqft: number;
    image: string;
    tag?: string;
}

export function ListingCard({ title, city, price, beds, baths, sqft, image, tag }: ListingCardProps) {
    return (
        <div className="group relative overflow-hidden rounded-2xl border border-border bg-card shadow-sm transition-all hover:shadow-md">
            {/* Image Placeholder */}
            <div className="relative aspect-[4/3] w-full bg-gray-200 overflow-hidden">
                {/* In a real app, Next/Image goes here. For now, a colored block */}
                <div className="absolute inset-0 bg-gradient-to-t from-gray-900/50 to-transparent opacity-60" />
                {tag && (
                    <span className="absolute top-4 left-4 rounded-full bg-white/90 px-3 py-1 text-xs font-semibold uppercase tracking-wider text-primary backdrop-blur-sm">
                        {tag}
                    </span>
                )}
            </div>

            <div className="p-5">
                <div className="flex items-start justify-between">
                    <div>
                        <h3 className="text-lg font-semibold text-primary group-hover:text-accent transition-colors">{title}</h3>
                        <p className="flex items-center text-sm text-muted-foreground">
                            <MapPin className="mr-1 h-3 w-3" /> {city}
                        </p>
                    </div>
                    <p className="text-lg font-bold text-primary">{price}</p>
                </div>

                <div className="mt-4 flex items-center justify-between border-t border-border pt-4 text-sm text-muted-foreground">
                    <span>{beds} Beds</span>
                    <span>{baths} Baths</span>
                    <span>{sqft} sqft</span>
                </div>
            </div>
        </div>
    );
}
