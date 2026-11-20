
import { useEffect, useState } from "react";
import { Menu, X } from "lucide-react";
import { SeatLogo } from "./SeatLogo";

const LINKS = [
  { label: "How It Works", href: "#how-it-works" },
  { label: "Features", href: "#features" },
];

export const Navbar = () => {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 8);

    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });

    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <header
      className={`fixed inset-x-0 top-0 z-50 bg-white/90 backdrop-blur-md border-b border-slate-200 transition-shadow duration-300 ${
        scrolled ? "shadow-md" : ""
      }`}
    >
      <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">

        {/* Logo */}
        <a href="/" className="flex items-center gap-2.5">
          <SeatLogo />
          <span className="font-extrabold text-lg text-[#101828] tracking-tight">
            BookMySeat
          </span>
        </a>

        {/* Desktop navigation links */}
        <div className="hidden md:flex items-center gap-8">
          {LINKS.map((link) => (
            <a
              key={link.href}
              href={link.href}
              className="text-sm font-medium text-slate-600 hover:text-[#101828] transition-colors"
            >
              {link.label}
            </a>
          ))}
        </div>

        {/* Desktop buttons */}
        <div className="hidden md:flex items-center gap-2">
          <a
            href="/login"
            className="text-sm font-semibold text-[#101828] hover:text-[#2563EB] px-3 py-2"
          >
            Sign In
          </a>

          <a
            href="/signup"
            className="text-sm font-semibold text-white bg-[#2563EB] hover:bg-[#1D4ED8] px-4 py-2 rounded-lg"
          >
            Get Started
          </a>
        </div>

        {/* Mobile menu button */}
        <button
          type="button"
          aria-expanded={open}
          aria-label={open ? "Close menu" : "Open menu"}
          onClick={() => setOpen((prev) => !prev)}
          className="md:hidden w-10 h-10 flex items-center justify-center rounded-lg hover:bg-slate-100"
        >
          {open ? (
            <X className="w-5 h-5" />
          ) : (
            <Menu className="w-5 h-5" />
          )}
        </button>
      </nav>

      {/* Mobile menu */}
      {open && (
        <div className="md:hidden border-t border-slate-200 bg-white px-4 py-4 space-y-2">
          {LINKS.map((link) => (
            <a
              key={link.href}
              href={link.href}
              onClick={() => setOpen(false)}
              className="block px-3 py-2.5 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-100"
            >
              {link.label}
            </a>
          ))}

          <a href="/login" className="block px-3 py-2.5 text-center font-semibold">
            Sign In
          </a>

          <a
            href="/signup"
            className="block px-3 py-2.5 text-center font-semibold text-white bg-[#2563EB] rounded-lg"
          >
            Get Started
          </a>
        </div>
      )}
    </header>
  );
};
