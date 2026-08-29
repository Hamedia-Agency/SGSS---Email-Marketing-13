import Link from "next/link";
import styles from "./Footer.module.css";

export function Footer() {
  return (
    <footer className={styles.footer} id="footer">
      <div className={`container ${styles.footerInner}`}>
        <div className={styles.footerBrand}>
          <img
            src="https://assets.cdn.filesafe.space/ApWkZ2IFXdvkS2AT3Tqg/media/6a0262de60a7a52fdc112210.png"
            alt="SGSS Logo"
            className={styles.logoImg}
            style={{ height: '76px' }}
          />
        </div>

        <p className={styles.footerCopy}>
          © {new Date().getFullYear()} Secure Guard Security Services. All rights reserved. SecureTrack is a proprietary technology platform of SGSS.
        </p>
      </div>
    </footer>
  );
}

export default Footer;
