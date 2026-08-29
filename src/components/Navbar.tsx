"use client";

import { useState } from "react";
import Link from "next/link";
import styles from "./Navbar.module.css";
import { Menu, X } from "lucide-react";

interface NavbarProps {
  onOpenConsultation?: () => void;
}

export function Navbar({ onOpenConsultation }: NavbarProps) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <nav className={styles.navbar} id="navbar">
      <div className={`container ${styles.navInner}`}>
        <Link href="/" className={styles.navLogo} id="nav-logo">
          <img
            src="https://assets.cdn.filesafe.space/ApWkZ2IFXdvkS2AT3Tqg/media/691d0ba7c2cf864910f19e13.png"
            alt="Secure Guard Security Services Logo"
            className={styles.logoImg}
          />
        </Link>

        {/* Desktop Nav Links */}
        <ul className={styles.navLinks}>
          <li>
            <a
              href="https://www.secureguardservices.com/contact"
              className={styles.navCta}
              id="nav-cta"
            >
              Schedule Free Consultation
            </a>
          </li>
        </ul>

        {/* Mobile Hamburger Button */}
        <button
          className={styles.mobileMenuToggle}
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          aria-label="Toggle Navigation Menu"
        >
          {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
        </button>
      </div>

      {/* Mobile Menu Dropdown */}
      {mobileMenuOpen && (
        <div className={styles.mobileDropdown}>
          <a
            href="https://www.secureguardservices.com/contact"
            className={styles.mobileCta}
          >
            Schedule Free Consultation
          </a>
        </div>
      )}
    </nav>
  );
}

export default Navbar;
