
import { useEffect, useState } from "react";
import {
  AnimatePresence,
  motion,
  useReducedMotion,
} from "framer-motion";

export const FlipWords = ({
  words,
  interval = 2600,
  className = "",
}) => {
  const [index, setIndex] = useState(0);
  const reduce = useReducedMotion();

  useEffect(() => {
    if (reduce) return undefined;

    const id = setInterval(
      () => setIndex((i) => (i + 1) % words.length),
      interval
    );

    return () => clearInterval(id);
  }, [words.length, interval, reduce]);

  const word = words[index];

  return (
    <span
      className={`relative inline-block text-left align-baseline ${className}`}
      style={{ minWidth: "6.4ch" }}
    >
        <AnimatePresence mode="wait" initial={false}>
            <motion.span
            key={word}
            className="inline-block"
            initial={
                reduce
                ? false
                : { y: "55%", opacity: 0, filter: "blur(6px)" }
            }
            animate={{
                y: 0,
                opacity: 1,
                filter: "blur(0px)",
            }}
            exit={
                reduce
                ? { opacity: 0 }
                : { y: "-55%", opacity: 0, filter: "blur(6px)" }
            }
            transition={{
                duration: 0.45,
                ease: [0.22, 1, 0.36, 1],
            }}
            >
            {word}
            </motion.span>
        </AnimatePresence>
    </span>
  );
};
