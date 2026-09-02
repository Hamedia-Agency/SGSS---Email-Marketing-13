import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import BackToTop from "@/components/BackToTop";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Real-Time Security Reporting | Secure Guard Services",
  description:
    "Experience total transparency with SecureTrack. Get real-time digital reporting, GPS-verified patrols, and unmatched accountability for your property.",
  keywords: [
    "SecureTrack",
    "security guard services",
    "verified patrols",
    "real-time reporting",
    "visual documentation",
    "accountability logs",
    "Southern California security",
    "GPS guard activity",
  ],
  openGraph: {
    title: "Real-Time Security Reporting | Secure Guard Services",
    description:
      "Experience total transparency with SecureTrack. Get real-time digital reporting, GPS-verified patrols, and unmatched accountability for your property.",
    type: "website",
  },
};


export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" className={inter.variable}>
      <body>
        {children}
        <BackToTop />
      </body>
    </html>
  );
}
