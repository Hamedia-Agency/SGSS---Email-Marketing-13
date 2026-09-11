import Image from "next/image";
import styles from "./page.module.css";
import { Navbar } from "@/components/Navbar";
import { Footer } from "@/components/Footer";
import BackToTop from "@/components/BackToTop";
import { PreFooterCTA } from "@/components/PreFooterCTA";
import EvaluationCarousel from "@/components/EvaluationCarousel";
import ParticleMesh from "@/components/ParticleMesh";
import FloatingShapes from "@/components/FloatingShapes";
import FAQAccordion from "@/components/FAQAccordion";
import { CoverageSection } from "@/components/CoverageSection";

export default function HomePage() {
  return (
    <main className={styles.main}>
      <Navbar />

      {/* ===== SECTION 1: HERO ===== */}
      <section className={styles.hero} id="hero">
        <div className={styles.heroBg}>
          <Image
            src="https://cms.secureguardservices.com/wp-content/uploads/2026/08/em10-1.webp"
            alt="Site Vulnerability Audit"
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
              Proactive Threat Identification
            </div>
            <h1 className={styles.heroTitle} id="hero-title">
              Site Vulnerability <span className={styles.heroTitleAccent}>Audit</span>
            </h1>
            <p className={styles.heroSubtitle}>
              Secure Guard identifies hidden security risks, from unsecured secondary entrances and dark parking zones to unmonitored loading docks and predictable patrol routes, before an incident occurs. Secure Guard conducts comprehensive site vulnerability audits that evaluate how your property functions as an interconnected system rather than inspecting isolated equipment.
            </p>
            <div className={styles.heroCtas}>
              <a 
                href="#prefooter-cta" 
                className={styles.btnPrimary} 
                id="hero-cta-primary"
              >
                Request a Site Audit
              </a>
            </div>
          </div>
        </div>
        <div className={styles.heroScroll} aria-hidden="true">
          <span className={styles.heroScrollDot} />
        </div>
      </section>

      {/* ===== SECTION 2: What Secure Guard Evaluates (Carousel) ===== */}
      <section className={styles.featuresSection} id="evaluates">
        <div className="container">
          <div className={styles.sectionHeader} style={{ maxWidth: "100%" }}>
            <span className={styles.sectionTag} style={{ color: "#b89000", background: "rgba(254, 207, 49, 0.13)", borderColor: "rgba(254, 207, 49, 0.35)" }}>Comprehensive Review</span>
            <h2 className={styles.sectionTitle} style={{ color: "var(--color-white)" }}>
              What Secure Guard Evaluates
            </h2>
            <p className={styles.bodyTextCenteredLight} style={{ color: "rgba(255, 255, 255, 0.85)", maxWidth: "100%", textAlign: "center" }}>
              We analyze every potential vulnerability across your facility, ensuring physical safeguards and technological tools work together to build an impenetrable defense.
            </p>
          </div>

          <EvaluationCarousel />
        </div>
      </section>

      {/* ===== SECTION 3: Evaluating Property Movement ===== */}
      <section className={styles.section} id="movement">
        <div className="container">
          <div className={styles.addonGrid}>
            <div className={styles.addonImageCol}>
              <Image 
                src="https://cms.secureguardservices.com/wp-content/uploads/2026/08/em10-2.webp" 
                alt="Evaluating Property Movement" 
                width={500} 
                height={400} 
                className={styles.addonImage} 
                style={{ borderRadius: "12px", objectFit: "cover" }}
              />
            </div>
            <div className={styles.addonContent}>
              <div className={styles.sectionHeader} style={{ margin: "0", textAlign: "left" }}>
                <span className={styles.sectionTag}>Traffic & Operations</span>
                <h2 className={styles.sectionTitle} style={{ marginBottom: "16px" }}>
                  Evaluating Property Movement
                </h2>
              </div>
              <p className={styles.bodyText}>
                Secure Guard analyzes how employees, visitors, contractors, and delivery vehicles navigate your site to uncover where unauthorized activity could blend into daily operations. Shared entryways, busy service bays, and unmanaged visitor pathways often make foot and vehicle traffic difficult to regulate, creating subtle vulnerabilities during peak operational hours.
              </p>
              <p className={styles.bodyText}>
                By mapping these movement patterns against your site's physical layout, we pinpoint exactly where your property requires stronger access controls, refined visitor check-in workflows, targeted patrol coverage, or live video monitoring to maintain complete operational oversight.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ===== SECTION 4: Connecting Your Security System (Escalation Box) ===== */}
      <section className={styles.contactSection} id="connecting">
        <div className={`container ${styles.contactContainer}`}>
          <div className={styles.contactContentPanel}>
            <div className={styles.sectionHeader} style={{ margin: "0 0 24px 0", textAlign: "left" }}>
              <span className={styles.sectionTag} style={{ color: "#b89000", background: "rgba(254, 207, 49, 0.13)", borderColor: "rgba(254, 207, 49, 0.35)" }}>Information Flow</span>
              <h2 className={styles.sectionTitle} style={{ marginBottom: "16px", color: "var(--color-white)" }}>
                Connecting Your Security System
              </h2>
            </div>
            <p className={styles.bodyText} style={{ color: "rgba(255, 255, 255, 0.9)" }}>
              Secure Guard evaluates how information flows between your personnel and technology, analyzing how incidents are escalated, how patrol activity is logged, and how existing protocols respond under pressure.
            </p>
            <p className={styles.bodyText} style={{ color: "rgba(255, 255, 255, 0.9)", marginBottom: 0 }}>
              By unifying standalone security elements into a synchronized operational network, we eliminate communication gaps and ensure your guards, technology, and procedures work together seamlessly when an incident occurs.
            </p>
          </div>
        </div>
      </section>

      {/* ===== SECTION 5: How Services Work Together ===== */}
      <section className={styles.standardSection} id="services">
        <div className={styles.standardPatternLeft}>
          <FloatingShapes shapeCount={18} />
        </div>
        <div className={styles.standardPatternRight}>
          <FloatingShapes shapeCount={18} />
        </div>
        <div className="container">
          <div className={styles.standardHeader} style={{ marginBottom: 0, maxWidth: "100%" }}>
            <span className={styles.sectionTag}>Unified Defense</span>
            <h2 className={styles.sectionTitle}>How Services Work Together</h2>
            <p className={styles.standardSubtitle} style={{ maxWidth: "100%", textAlign: "center" }}>
              Secure Guard combines physical personnel, electronic surveillance, and centralized management into a unified defense network. Officers manage fixed access points, while mobile patrols perform randomized checks across outer perimeters and parking areas. Concurrently, live video monitoring and surveillance towers maintain constant visual coverage over expansive or low-light zones. Central dispatch links these layers by analyzing surveillance data and routing field personnel to specific areas, ensuring every service directly fills the operational gaps of the others.
            </p>
          </div>
        </div>
      </section>

      {/* ===== SECTION 6: SecureTrack (Split Pane) ===== */}
      <section className={styles.section} id="securetrack" style={{ background: "var(--color-bg-alt, #f7f9fc)" }}>
        <div className="container">
          <div className={styles.addonGrid} style={{ gridTemplateColumns: "1fr 1fr", direction: "rtl" }}>
            <div className={styles.addonImageCol} style={{ direction: "ltr" }}>
              <Image 
                src="https://cms.secureguardservices.com/wp-content/uploads/2026/08/em8-1-1.webp" 
                alt="SecureTrack Platform" 
                width={500} 
                height={400} 
                className={styles.addonImage} 
                style={{ borderRadius: "12px", objectFit: "cover" }}
              />
            </div>
            <div className={styles.addonContent} style={{ direction: "ltr" }}>
              <div className={styles.sectionHeader} style={{ margin: "0", textAlign: "left" }}>
                <span className={styles.sectionTag}>Digital Accountability</span>
                <h2 className={styles.sectionTitle} style={{ marginBottom: "16px" }}>
                  SecureTrack
                </h2>
              </div>
              <p className={styles.bodyText}>
                SecureTrack is the central management platform that connects field personnel, dispatch, supervision, and reporting to enforce audit-driven security protocols.
              </p>
              <p className={styles.bodyText}>
                Using GPS tracking and digital checkpoint verification, the platform ensures guards actively inspect the high-risk zones, unlit areas, and secondary access points identified during your assessment. Real-time logging and digital incident reporting allow dispatchers to track officer movement continuously, verify route compliance, and deliver clear proof of coverage directly to property managers.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ===== SECTION 7: Security Assessment Process (Grid) ===== */}
      <section className={styles.section} id="process" style={{ background: "var(--color-bg, #ffffff)" }}>
        <div className="container">
          <div className={styles.setupUnifiedContainer} style={{ gridTemplateColumns: "1fr" }}>
            <div className={styles.sectionHeader} style={{ margin: "0 auto 48px", textAlign: "center", maxWidth: "800px" }}>
              <span className={styles.sectionTag}>Structured Evaluation</span>
              <h2 className={styles.sectionTitle} style={{ marginBottom: "16px" }}>
                Security Assessment Process
              </h2>
            </div>
            
            <div className={styles.setupRightGrid} style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))", gap: "24px" }}>
              <div className={styles.setupGridItem} style={{ background: "var(--color-bg-section)" }}>
                <div className={styles.setupItemHeader}>
                  <span className={styles.setupItemIcon}>01</span>
                  <h3 className={styles.setupItemTitle}>Map Property Operations</h3>
                </div>
                <p className={styles.setupItemDesc}>
                  Reviewing your site type, operating schedules, traffic flows, occupancy levels, and historical security incidents to establish a complete operational baseline before evaluating specific risks.
                </p>
              </div>

              <div className={styles.setupGridItem} style={{ background: "var(--color-bg-section)" }}>
                <div className={styles.setupItemHeader}>
                  <span className={styles.setupItemIcon}>02</span>
                  <h3 className={styles.setupItemTitle}>Inspect the Physical Environment</h3>
                </div>
                <p className={styles.setupItemDesc}>
                  Evaluates your physical boundaries, entrances, perimeters, parking zones, loading bays, and storage areas to pinpoint physical blind spots, lighting gaps, and access vulnerabilities across the property.
                </p>
              </div>

              <div className={styles.setupGridItem} style={{ background: "var(--color-bg-section)" }}>
                <div className={styles.setupItemHeader}>
                  <span className={styles.setupItemIcon}>03</span>
                  <h3 className={styles.setupItemTitle}>Audit Existing Security Resources</h3>
                </div>
                <p className={styles.setupItemDesc}>
                  Analyze how your current setup, including on-site guards, patrol schedules, camera coverage, access protocols, and reporting workflows, is actively performing relative to your actual daily risks.
                </p>
              </div>

              <div className={styles.setupGridItem} style={{ background: "var(--color-bg-section)" }}>
                <div className={styles.setupItemHeader}>
                  <span className={styles.setupItemIcon}>04</span>
                  <h3 className={styles.setupItemTitle}>Pinpoint & Prioritize Vulnerabilities</h3>
                </div>
                <p className={styles.setupItemDesc}>
                  Categorize and rank identified security gaps based on location, likelihood, and operational impact, allowing you to address critical threats first rather than treating every observation as equally urgent.
                </p>
              </div>

              <div className={styles.setupGridItem} style={{ background: "var(--color-bg-section)" }}>
                <div className={styles.setupItemHeader}>
                  <span className={styles.setupItemIcon}>05</span>
                  <h3 className={styles.setupItemTitle}>Deliver Actionable Improvements</h3>
                </div>
                <p className={styles.setupItemDesc}>
                  Provide practical, targeted recommendations, ranging from minor patrol route tweaks and procedural updates to camera repositioning or hybrid technology integration, designed to strengthen your security program.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ===== SECTION 8: Vulnerability Assessment to Security Strategy (Escalation box) ===== */}
      <section className={styles.contactSection} id="strategy">
        <div className={`container ${styles.contactContainer}`}>
          <div className={styles.contactContentPanel}>
            <div className={styles.sectionHeader} style={{ margin: "0 0 24px 0", textAlign: "left" }}>
              <span className={styles.sectionTag} style={{ color: "#b89000", background: "rgba(254, 207, 49, 0.13)", borderColor: "rgba(254, 207, 49, 0.35)" }}>Actionable Intelligence</span>
              <h2 className={styles.sectionTitle} style={{ marginBottom: "16px", color: "var(--color-white)" }}>
                Vulnerability Assessment to Security Strategy
              </h2>
            </div>
            <p className={styles.bodyText} style={{ color: "rgba(255, 255, 255, 0.9)", marginBottom: 0 }}>
              A vulnerability audit provides the concrete baseline needed to build a tailored security strategy rather than forcing a standardized package onto your property. Based on your site's specific findings, we deploy the exact mix of protection required, whether that means standing officers for continuous visible deterrence, mobile patrols for flexible after-hours checks, or solar surveillance towers and remote video monitoring for expansive outdoor perimeters.
            </p>
          </div>
        </div>
      </section>

      {/* ===== SECTION 9: The Secure Guard Difference ===== */}
      <section className={styles.standardSection} id="difference">
        <div className={styles.standardPatternLeft}>
          <FloatingShapes shapeCount={18} />
        </div>
        <div className={styles.standardPatternRight}>
          <FloatingShapes shapeCount={18} />
        </div>
        <div className="container">
          <div className={styles.standardHeader} style={{ marginBottom: 0, maxWidth: "100%" }}>
            <span className={styles.sectionTag}>Integrated Approach</span>
            <h2 className={styles.sectionTitle}>The Secure Guard Difference</h2>
            <p className={styles.standardSubtitle} style={{ maxWidth: "100%", textAlign: "center" }}>
              Secure Guard treats property security as an integrated operational system rather than a collection of standalone services. By evaluating your physical layout, traffic flow, operating schedules, and existing security measures together, we deliver practical recommendations based on how your property actually functions.
            </p>
          </div>
        </div>
      </section>

      {/* ===== COVERAGE SECTION ===== */}
      <CoverageSection />

      {/* ===== SECTION 10: FAQ ===== */}
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