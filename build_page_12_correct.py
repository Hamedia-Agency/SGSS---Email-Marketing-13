import os

project_root = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12"

page_content = """\
import Image from "next/image";
import styles from "./page.module.css";
import { Navbar } from "@/components/Navbar";
import { Footer } from "@/components/Footer";
import BackToTop from "@/components/BackToTop";
import { PreFooterCTA } from "@/components/PreFooterCTA";

import PillarsCarousel from "@/components/PillarsCarousel";
import FloatingShapes from "@/components/FloatingShapes";
import { FAQAccordion } from "@/components/FAQAccordion";
import { CoverageSection } from "@/components/CoverageSection";

export default function HomePage() {
  return (
    <main className={styles.main}>
      <Navbar />

      {/* ===== SECTION 1: HERO ===== */}
      <section className={styles.hero} id="hero">
        <div className={styles.heroBg}>
          <Image
            src="https://cms.secureguardservices.com/wp-content/uploads/2026/08/em8-1-1.webp"
            alt="Hybrid Security"
            fill
            className={styles.heroBgImg}
            priority
            quality={90}
          />
          <div className={styles.heroOverlay} />
        </div>
        <div className={`container ${styles.heroWrapper}`}>
          <div className={styles.heroContent}>
            <div className={styles.heroBadge} id="hero-badge">
              <span className={styles.heroBadgeDot} />
              Connected Threat Response
            </div>
            <h1 className={styles.heroTitle} id="hero-title">
              Hybrid <span className={styles.heroTitleAccent}>Security</span>
            </h1>
            <p className={styles.heroSubtitle}>
              Secure Guard unifies video surveillance, 24/7 central dispatch, and field guard teams into one connected response network. Integrating with existing cameras or standalone mobile towers, our model manages the entire incident lifecycle, from threat detection and verification to live voice deterrence, field dispatch, and SecureTrack tracking.
            </p>
            <div className={styles.heroCtas}>
              <a 
                href="#prefooter-cta" 
                className={styles.btnPrimary} 
                id="hero-cta-primary"
              >
                See How Hybrid Security Works
              </a>
            </div>
          </div>
        </div>
        <div className={styles.heroScroll} aria-hidden="true">
          <span className={styles.heroScrollDot} />
        </div>
      </section>

      {/* ===== SECTION 2: Camera Alert Is Only the Beginning ===== */}
      <section className={styles.section} id="vulnerability">
        <div className="container">
          <div className={styles.addonGrid}>
            <div className={styles.addonImageCol}>
              <Image 
                src="https://cms.secureguardservices.com/wp-content/uploads/2026/08/em8-2.webp" 
                alt="Connected Security Network" 
                width={500} 
                height={400} 
                className={styles.addonImage} 
                style={{ borderRadius: "12px", objectFit: "cover" }}
              />
            </div>
            <div className={styles.addonContent}>
              <div className={styles.sectionHeader} style={{ margin: "0", textAlign: "left" }}>
                <span className={styles.sectionTag}>Complete Incident Control</span>
                <h2 className={styles.sectionTitle} style={{ marginBottom: "16px" }}>
                  Camera Alert Is Only the Beginning
                </h2>
              </div>
              <p className={styles.bodyText}>
                Secure Guard’s hybrid security model bridges the gap between technology and physical security by managing the complete incident sequence for you.
              </p>
              <p className={styles.bodyText}>
                Instead of leaving property managers to determine next steps after an alert, our connected system automatically flags off-hours activity in high-vulnerability zones, verifies live footage in seconds to eliminate false alarms, and immediately executes your custom response protocols—whether that means issuing live voice warnings, dispatching mobile field patrols, or coordinating directly with local law enforcement.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ===== SECTION 3: How Hybrid Security Works (Unified Grid) ===== */}
      <section className={styles.section} id="setup" style={{ background: "var(--color-bg-alt, #f7f9fc)" }}>
        <div className="container">
          <div className={styles.setupUnifiedContainer}>
            {/* Left Pane */}
            <div className={styles.setupLeftPane}>
              <span className={styles.setupLeftTag}>Unified Incident Response</span>
              <h2 className={styles.setupLeftTitle}>
                How Hybrid Security Works
              </h2>
              <p className={styles.setupLeftDesc}>
                Hybrid security combines technology and physical security so each layer supports the others. This automated detection layer provides uninterrupted property oversight across expansive or complex commercial sites without relying solely on physical guard patrols.
              </p>
            </div>
            
            {/* Right Pane (Grid) */}
            <div className={styles.setupRightGrid} style={{ gridTemplateColumns: "1fr", gap: "20px" }}>
              
              <div className={`${styles.setupGridItem} ${styles.setupItem1}`}>
                <div className={styles.setupItemHeader}>
                  <span className={styles.setupItemIcon}>01</span>
                  <h3 className={styles.setupItemTitle}>Real-Time Detection</h3>
                </div>
                <p className={styles.setupItemDesc}>
                  High-definition fixed cameras, thermal sensors, and mobile surveillance towers continuously monitor perimeters, access points, and high-vulnerability assets to trigger instant system alerts upon unauthorized movement.
                </p>
              </div>

              <div className={`${styles.setupGridItem} ${styles.setupItem2}`}>
                <div className={styles.setupItemHeader}>
                  <span className={styles.setupItemIcon}>02</span>
                  <h3 className={styles.setupItemTitle}>Human Verification</h3>
                </div>
                <p className={styles.setupItemDesc}>
                  Secure Guard’s 24/7 central monitoring specialists instantly evaluate live video feeds upon alert activation to distinguish genuine operational threats from harmless environmental movement.
                </p>
              </div>

              <div className={`${styles.setupGridItem} ${styles.setupItem3}`}>
                <div className={styles.setupItemHeader}>
                  <span className={styles.setupItemIcon}>03</span>
                  <h3 className={styles.setupItemTitle}>Remote Intervention</h3>
                </div>
                <p className={styles.setupItemDesc}>
                  When suspicious activity is verified, monitoring personnel utilize high-decibel two-way speakers to broadcast live, localized voice-down warnings directly to unauthorized individuals on site.
                </p>
              </div>

              <div className={`${styles.setupGridItem} ${styles.setupItem4}`}>
                <div className={styles.setupItemHeader}>
                  <span className={styles.setupItemIcon}>04</span>
                  <h3 className={styles.setupItemTitle}>Coordinated Field Dispatch</h3>
                </div>
                <p className={styles.setupItemDesc}>
                  When physical on-site intervention is required, central dispatch immediately deploys resources according to your customized property security plan, alerting standing guards or mobile units.
                </p>
              </div>

              <div className={`${styles.setupGridItem} ${styles.setupItem1}`} style={{ background: "rgba(255,255,255,0.03)" }}>
                <div className={styles.setupItemHeader}>
                  <span className={styles.setupItemIcon}>05</span>
                  <h3 className={styles.setupItemTitle}>Digital Reporting</h3>
                </div>
                <p className={styles.setupItemDesc}>
                  Every system alert, verification, intervention, and dispatch action is automatically logged with verified metadata inside the SecureTrack platform, delivering audit-ready transparency.
                </p>
              </div>

            </div>
          </div>
        </div>
      </section>

      {/* ===== SECTION 4: The Secure Guard Hybrid Security Model (Carousel) ===== */}
      <section className={styles.featuresSection} id="applications">
        <div className="container">
          <div className={styles.sectionHeader} style={{ maxWidth: "100%" }}>
            <span className={styles.sectionTag} style={{ color: "#b89000", background: "rgba(254, 207, 49, 0.13)", borderColor: "rgba(254, 207, 49, 0.35)" }}>Secure Guard Framework</span>
            <h2 className={styles.sectionTitle} style={{ color: "var(--color-white)" }}>
              The Secure Guard Hybrid Security Model
            </h2>
            <p className={styles.bodyTextCenteredLight} style={{ color: "rgba(255, 255, 255, 0.85)", maxWidth: "100%", textAlign: "center" }}>
              Secure Guard can connect mobile surveillance technology with live monitoring, dispatch, security officers, and mobile patrol services. This allows technology to extend the reach of physical security while giving physical security teams better information about what is happening at the property.
            </p>
          </div>

          <PillarsCarousel />
        </div>
      </section>

      {/* ===== SECTION 5: Existing Camera Integration (Escalation box) ===== */}
      <section className={styles.contactSection} id="integration">
        <div className={`container ${styles.contactContainer}`}>
          <div className={styles.contactContentPanel}>
            <div className={styles.sectionHeader} style={{ margin: "0 0 24px 0", textAlign: "left" }}>
              <span className={styles.sectionTag} style={{ color: "#b89000", background: "rgba(254, 207, 49, 0.13)", borderColor: "rgba(254, 207, 49, 0.35)" }}>Cost-Effective Oversight</span>
              <h2 className={styles.sectionTitle} style={{ marginBottom: "16px", color: "var(--color-white)" }}>
                Existing Camera Integration
              </h2>
            </div>
            <p className={styles.bodyText} style={{ color: "rgba(255, 255, 255, 0.9)" }}>
              Secure Guard evaluates and integrates your existing security infrastructure into our hybrid monitoring network, eliminating the operational expense of complete hardware replacement.
            </p>
            <p className={styles.bodyText} style={{ color: "rgba(255, 255, 255, 0.9)", marginBottom: 0 }}>
              Compatible camera setups are connected directly into our 24/7 active monitoring, central dispatch, field response, and digital reporting ecosystem, instantly adding live human oversight and intervention to passive feeds.
            </p>
          </div>
        </div>
      </section>

      {/* ===== SECTION 6: Visibility Across the Entire Security Operation (Standard) ===== */}
      <section className={styles.standardSection} id="visibility">
        <div className={styles.standardPatternLeft}>
          <FloatingShapes shapeCount={18} />
        </div>
        <div className={styles.standardPatternRight}>
          <FloatingShapes shapeCount={18} />
        </div>
        <div className="container">
          <div className={styles.standardHeader} style={{ marginBottom: 0, maxWidth: "100%" }}>
            <span className={styles.sectionTag}>Total Transparency</span>
            <h2 className={styles.sectionTitle}>Visibility Across the Entire Security Operation</h2>
            <p className={styles.standardSubtitle} style={{ maxWidth: "100%", textAlign: "center" }}>
              Secure Guard provides complete operational visibility across all your properties without requiring you to be physically on site. By unifying live monitoring, field guard activity, and central dispatch into the SecureTrack platform, property managers gain real-time operational oversight and audit-ready incident tracking—delivering total portfolio transparency from anywhere.
            </p>
          </div>
        </div>
      </section>

      {/* ===== SECTION 7: Serving Southern and Northern California (Marquee) ===== */}
      <CoverageSection />

      {/* ===== SECTION 8: FAQ ===== */}
      <section className={styles.faqSection} id="faq">
        <div className="container">
          <div className={styles.sectionHeader}>
            <span className={styles.sectionTag}>FAQ</span>
            <h2 className={styles.sectionTitle}>
              Frequently Asked Questions
            </h2>
          </div>
          <FAQAccordion />
        </div>
      </section>

      {/* ===== PRE-FOOTER CTA ===== */}
      <PreFooterCTA />

      <Footer />
      <BackToTop />
    </main>
  );
}
"""
with open(os.path.join(project_root, "src", "app", "page.tsx"), "w", encoding="utf-8") as f:
    f.write(page_content)
