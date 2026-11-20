
export const SeatLogo = ({ size = 34 }) => (
  <span
    className="inline-flex items-center justify-center rounded-[10px] bg-[#2563EB] shrink-0"
    style={{ width: size, height: size }}
  >
    <svg
      viewBox="0 0 32 32"
      style={{
        width: size * 0.68,
        height: size * 0.68,
      }}
      fill="none"
      stroke="#FFFFFF"
      strokeWidth="2.6"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M9 7v8" />
      <path d="M9 15h11a3 3 0 0 1 3 3v2" />
      <path d="M9 20h14" />
      <path d="M11 20v5" />
      <path d="M21 20v5" />
    </svg>
  </span>
);
