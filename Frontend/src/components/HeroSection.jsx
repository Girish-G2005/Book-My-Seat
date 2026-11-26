
import { motion, useReducedMotion } from "framer-motion";
import { useNavigate } from "react-router-dom";
import { ArrowRight, Armchair } from "lucide-react";
import { FlipWords } from "./FlipWords";
import { SeatMap } from "./SeatMap";
import { isAuthed } from "../lib/auth";

const container = {
  hidden: {},
  show: { transition: { staggerChildren: 0.12 } },
};

const item = {
  hidden: { opacity: 0, y: 24 },
  show: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.6,
      ease: [0.22, 1, 0.36, 1],
    },
  },
};

export const HeroSection = () => {
  const navigate = useNavigate();
  const reduce = useReducedMotion();

  return (
    <section className="relative overflow-hidden bg-[#F8FAFC] pt-28 lg:pt-36 pb-16 lg:pb-24">


        {/** Dotted background*/}
        <div
            aria-hidden="true"
            className="absolute inset-0"
            style={{
            backgroundImage: "radial-gradient(#CBD5E1 1px, transparent 1px)",
            backgroundSize: "28px 28px",
            opacity: 0.45,
            maskImage: "linear-gradient(to bottom, black 55%, transparent 95%)",
            WebkitMaskImage: "linear-gradient(to bottom, black 55%, transparent 95%)",
            }}
        />

            {/** Landing page heading and Preview animation */}
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid lg:grid-cols-2 gap-14 lg:gap-10 items-center">

            {/**Landing Text */}
            <motion.div
            variants={container}
            initial={reduce ? false : "hidden"}
            animate="show"
            className="max-w-xl px-5 lg:px-0"
            >
            <motion.p
                variants={item}
                className="inline-flex items-center gap-2 text-xs font-semibold uppercase tracking-normal text-[#2563EB] bg-[#EFF6FF] border border-[#BFDBFE] rounded-full px-3 py-1.5"
            >
                <Armchair className="w-3.5 h-3.5" />
                Smart seat booking
            </motion.p>

            <motion.h1
                variants={item}
                className="font-sans mt-6 text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight text-[#101828] leading-[1.08]"
            >
                Your Seat,
                <br />
                Your Time,
                <br />
                Your{" "}
                <FlipWords
                words={["Booking.", "Schedule.", "Moment.", "Seat."]}
                className="text-[#2563EB]"
                />
            </motion.h1>

            <motion.p
                variants={item}
                className="mt-6 text-base sm:text-lg text-[#64748B] leading-relaxed"
            >
                Find your seat, check availability, and book your place in seconds.
                A simple and seamless way to manage your seating experience.
            </motion.p>

            <motion.div
                variants={item}
                className="mt-8 flex flex-col sm:flex-row gap-3"
            >
                <button
                type="button"
                data-testid="hero-cta-primary"
                onClick={() => navigate(isAuthed() ? "/dashboard" : "/login")}
                className="inline-flex items-center justify-center gap-2 text-base font-semibold text-white bg-[#2563EB] hover:bg-[#1D4ED8] transition-all duration-200 hover:-translate-y-0.5 px-6 py-3.5 rounded-lg shadow-[0_8px_24px_-8px_rgba(37,99,235,0.5)]"
                >
                Book Your Seat
                <ArrowRight className="w-4 h-4" strokeWidth={2.5} />
                </button>

                <a
                href="#how-it-works"
                data-testid="hero-cta-secondary"
                className="inline-flex items-center justify-center gap-2 text-base font-semibold text-[#101828] bg-white border border-slate-200 hover:border-slate-300 hover:bg-slate-50 transition-all duration-200 px-6 py-3.5 rounded-lg"
                >
                See How It Works
                </a>
            </motion.div>

            </motion.div>


            {/**Preview animation */}
            <motion.div
            initial={reduce ? false : { opacity: 0, y: 36 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{
                duration: 0.7,
                delay: 0.25,
                ease: [0.22, 1, 0.36, 1],
            }}
            >
            <SeatMap />
            </motion.div>
        </div>
    </section>
  );
};
