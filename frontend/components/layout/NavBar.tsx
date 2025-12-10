"use client";

import { useState } from "react";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Menu, House, X } from "lucide-react";

export default function NavBar() {
    const [open, setOpen] = useState(false);

    return (
        <>
            <header className="fixed top-4 left-0 right-0 z-50 flex justify-center px-4">
                <nav className="flex h-14 w-full max-w-2xl items-center justify-between rounded-full border border-white/20 bg-white/60 px-6 shadow-sm backdrop-blur-xl transition-all dark:bg-black/60 dark:border-white/10">

                    {/* Left: Logo */}
                    <Link href="/" className="flex items-center gap-2 transition-opacity hover:opacity-80">
                        <div className="flex h-8 w-8 items-center justify-center rounded-full bg-primary text-white">
                            <span className="font-bold">M</span>
                        </div>
                        <span className="hidden text-lg font-bold tracking-tight text-primary sm:inline-block">M-Homes</span>
                    </Link>

                    {/* Center: Desktop Navigation */}
                    <div className="hidden items-center gap-8 md:flex">
                        <Link href="/buy" className="text-sm font-medium text-primary/80 transition-colors hover:text-accent">
                            Buy
                        </Link>
                        <Link href="/rent" className="text-sm font-medium text-primary/80 transition-colors hover:text-accent">
                            Rent
                        </Link>
                        <Link href="/blog" className="text-sm font-medium text-primary/80 transition-colors hover:text-accent">
                            Blog
                        </Link>
                        <Link href="/properties" className="text-sm font-medium text-primary/80 transition-colors hover:text-accent">
                            Properties
                        </Link>
                    </div>

                    {/* Right: Contact & Mobile Menu */}
                    <div className="flex items-center gap-4">
                        <Button className="hidden rounded-full bg-accent px-6 font-semibold text-white hover:bg-accent/90 md:flex">
                            Contact Us
                        </Button>

                        <button
                            className="rounded-full p-2 text-primary hover:bg-black/5 md:hidden"
                            onClick={() => setOpen(!open)}
                        >
                            {open ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
                        </button>
                    </div>
                </nav>
            </header>

            {/* Mobile Menu Overlay */}
            {open && (
                <div className="fixed inset-0 z-40 bg-background/80 backdrop-blur-sm md:hidden">
                    <div className="fixed inset-x-4 top-24 z-50 rounded-3xl border border-white/20 bg-white/90 p-6 shadow-lg backdrop-blur-md dark:bg-zinc-900/90 dark:border-zinc-800">
                        <div className="flex flex-col gap-6 text-center">
                            <Link href="/buy" onClick={() => setOpen(false)} className="text-lg font-medium text-primary">
                                Buy
                            </Link>
                            <Link href="/rent" onClick={() => setOpen(false)} className="text-lg font-medium text-primary">
                                Rent
                            </Link>
                            <Link href="/blog" onClick={() => setOpen(false)} className="text-lg font-medium text-primary">
                                Blog
                            </Link>
                            <Link href="/properties" onClick={() => setOpen(false)} className="text-lg font-medium text-primary">
                                Properties
                            </Link>
                            <div className="border-t border-gray-200 pt-6">
                                <Button className="w-full rounded-full bg-accent text-white hover:bg-accent/90">
                                    Contact Us
                                </Button>
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </>
    );
}
