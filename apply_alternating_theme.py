import os

project_root = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-11"

# 1. Update SupervisionCarousel.module.css (for LIGHT background)
carousel_css_path = os.path.join(project_root, "src", "components", "SupervisionCarousel.module.css")
carousel_css = """\
.carouselContainer {
  position: relative;
  width: 100%;
  margin-top: 48px;
  display: flex;
  align-items: center;
}
.embla {
  overflow: hidden;
  width: 100%;
  padding: 16px;
  margin: -16px;
}
.embla__container {
  display: flex;
  margin-left: -24px;
}
.embla__slide {
  flex: 0 0 calc(33.333% - 16px);
  min-width: 0;
  padding-left: 24px;
}
.featureCard {
  background: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  border-radius: var(--radius-lg, 12px);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  height: 100%;
}
.featureCard:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}
.featureCardImageWrapper {
  position: relative;
  width: 100%;
  height: 200px;
}
.featureCardImage {
  object-fit: cover;
}
.featureCardContent {
  padding: 32px;
  flex: 1;
}
.featureCardTitle {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--color-dark-blue);
  margin-bottom: 12px;
}
.featureCardDesc {
  font-size: 0.95rem;
  color: var(--color-text);
  opacity: 0.9;
  line-height: 1.6;
}
.navButton {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: var(--color-white, #fff);
  color: var(--color-dark-blue);
  border: 1px solid rgba(0, 0, 0, 0.1);
  width: 48px;
  height: 48px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 10;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: all 0.2s ease;
}
.navButton:hover {
  background: var(--color-gold, #fecf31);
  color: var(--color-dark-blue);
  border-color: var(--color-gold, #fecf31);
}
.navLeft { left: -24px; }
.navRight { right: -24px; }
@media (max-width: 992px) { .embla__slide { flex: 0 0 calc(50% - 12px); } }
@media (max-width: 768px) {
  .embla__slide { flex: 0 0 100%; }
  .navLeft { left: 8px; }
  .navRight { right: 8px; }
}
"""
with open(carousel_css_path, "w", encoding="utf-8") as f:
    f.write(carousel_css)

# 2. Update ProcessExplorer.module.css (for DARK background)
process_css_path = os.path.join(project_root, "src", "components", "ProcessExplorer.module.css")
with open(process_css_path, "r", encoding="utf-8") as f:
    process_css = f.read()

# Make text white instead of dark blue for dark background
process_css = process_css.replace("color: var(--color-dark-blue);", "color: var(--color-white);")
process_css = process_css.replace("color: var(--color-text);", "color: rgba(255,255,255,0.85);")
process_css = process_css.replace("background: var(--color-white);", "background: rgba(255,255,255,0.05);")
process_css = process_css.replace("background: #ffffff;", "background: rgba(255,255,255,0.05);")
process_css = process_css.replace("background: #fff;", "background: rgba(255,255,255,0.05);")
# Add a white border to tabButton if missing
process_css = process_css.replace(".tabButton {", ".tabButton {\n  border: 1px solid rgba(255,255,255,0.1);\n")

with open(process_css_path, "w", encoding="utf-8") as f:
    f.write(process_css)

# 3. Rewrite page.tsx sections to strictly alternate Dark/White
page_path = os.path.join(project_root, "src", "app", "page.tsx")
page_content = """\
import Image from "next/image";
import styles from "./page.module.css";
import { Navbar } from "@/components/Navbar";
import { Footer } from "@/components/Footer";
import BackToTop from "@/components/BackToTop";
import { PreFooterCTA } from "@/components/PreFooterCTA";

import { ProcessExplorer } from "@/components/ProcessExplorer";
import ApplicationsCarousel from "@/components/ApplicationsCarousel";
import { FAQAccordion } from "@/components/FAQAccordion";
import { 
  Camera, 
  Moon, 
  Sun, 
  Activity, 
  Mic
} from "lucide-react";

export default function HomePage() {
  return (
    <main className={styles.main}>
      <Navbar />

      {/* ===== 1. HERO (DARK) ===== */}
      <section className={styles.hero} id="hero">
        <div className={styles.heroBg}>
          <Image
            src="https://cms.secureguardservices.com/wp-content/uploads/2026/08/em8-1-1.webp"
            alt="Mobile Surveillance Towers"
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
              Autonomous 24/7 Security
            </div>
            <h1 className={styles.heroTitle} id="hero-title">
              Mobile Surveillance <span className={styles.heroTitleAccent}>Towers</span>
            </h1>
            <p className={styles.heroSubtitle}>
              Secure Guard’s solar-powered surveillance towers combine HD cameras, smart detection, and live voice intervention into an autonomous 24/7 security solution—stopping trespassers, theft, and vandalism before damage occurs.
            </p>
            <div className={styles.heroCtas}>
              <a 
                href="#prefooter-cta" 
                className={styles.btnPrimary} 
                id="hero-cta-primary"
              >
                Request a Tower Consultation
              </a>
            </div>
          </div>
        </div>
        <div className={styles.heroScroll} aria-hidden="true">
          <span className={styles.heroScrollDot} />
        </div>
      </section>

      {/* ===== 2. VULNERABILITY (LIGHT) ===== */}
      <section className={styles.section} id="vulnerability">
        <div className="container">
          <div className={styles.splitGrid} style={{ marginBottom: '0', alignItems: 'center' }}>
            <div className={styles.splitImageWrapper} style={{ height: '100%', minHeight: '400px' }}>
              <Image 
                src="https://cms.secureguardservices.com/wp-content/uploads/2026/08/em8-2.webp" 
                alt="Mobile Surveillance Tower on site" 
                fill
                className={styles.splitImage}
              />
            </div>
            <div className={styles.sectionHeaderLeft} style={{ marginBottom: 0 }}>
              <span className={styles.sectionTag}>Active Protection</span>
              <h2 className={styles.sectionTitle}>
                Why Outdoor Properties Need More Than Cameras
              </h2>
              <p className={styles.bodyText}>
                Mobile surveillance towers provide another layer of protection by combining elevated cameras, visible deterrence, live monitoring, and remote voice communication in one mobile security solution. 
              </p>
              <p className={styles.bodyText}>
                Unlike static cameras that only record crimes as they happen, the tower can be positioned where coverage is needed most, moved as property conditions change, and actively deter intruders in real time.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ===== 3. HOW IT WORKS (DARK) ===== */}
      <section className={`${styles.section} ${styles.sectionDark}`} id="how-it-works">
        <div className="container">
          <div className={styles.sectionHeaderCentered}>
            <span className={`${styles.sectionTag} ${styles.sectionTagDark}`}>Connected Security Operations</span>
            <h2 className={`${styles.sectionTitle} ${styles.sectionTitleDark}`}>
              How Mobile Surveillance Towers Work
            </h2>
            <p className={`${styles.bodyTextCentered} ${styles.bodyTextDark}`}>
              Towers function as fully integrated, connected security operations rather than passive recording devices.
            </p>
          </div>
          <ProcessExplorer />
        </div>
      </section>

      {/* ===== 4. FEATURES (LIGHT) ===== */}
      <section className={styles.section} id="features">
        <div className="container">
          <div className={styles.sectionHeaderCentered} style={{ marginBottom: '56px' }}>
            <span className={styles.sectionTag}>Advanced Capabilities</span>
            <h2 className={styles.sectionTitle}>
              Mobile Surveillance Towers Key Features
            </h2>
          </div>
          
          <div className={styles.featuresGrid}>
            <div className={styles.featureCard} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', padding: '30px 20px' }}>
              <div className={styles.featureCardIcon} style={{ width: '56px', height: '56px', marginBottom: '16px' }}>
                <Camera size={28} />
              </div>
              <h3 className={styles.featureTitle} style={{ marginBottom: '10px', fontSize: '1.15rem' }}>Elevated Camera Coverage</h3>
              <p className={styles.featureDesc} style={{ fontSize: '0.95rem' }}>Eliminates ground-level blind spots caused by parked vehicles, stacked materials, and fencing. Oversees expansive outdoor areas.</p>
            </div>
            
            <div className={styles.featureCard} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', padding: '30px 20px' }}>
              <div className={styles.featureCardIcon} style={{ width: '56px', height: '56px', marginBottom: '16px' }}>
                <Moon size={28} />
              </div>
              <h3 className={styles.featureTitle} style={{ marginBottom: '10px', fontSize: '1.15rem' }}>Day and Night Visibility</h3>
              <p className={styles.featureDesc} style={{ fontSize: '0.95rem' }}>Equipped with advanced infrared night-vision and high-intensity lighting to maintain crisp visual clarity in complete darkness.</p>
            </div>
            
            <div className={styles.featureCard} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', padding: '30px 20px' }}>
              <div className={styles.featureCardIcon} style={{ width: '56px', height: '56px', marginBottom: '16px' }}>
                <Sun size={28} />
              </div>
              <h3 className={styles.featureTitle} style={{ marginBottom: '10px', fontSize: '1.15rem' }}>Solar-Powered Independence</h3>
              <p className={styles.featureDesc} style={{ fontSize: '0.95rem' }}>Operates entirely off the grid. Onboard solar panels provide continuous power while cellular connectivity streams real-time data.</p>
            </div>
            
            <div className={styles.featureCard} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', padding: '30px 20px' }}>
              <div className={styles.featureCardIcon} style={{ width: '56px', height: '56px', marginBottom: '16px' }}>
                <Activity size={28} />
              </div>
              <h3 className={styles.featureTitle} style={{ marginBottom: '10px', fontSize: '1.15rem' }}>Intelligent Activity Detection</h3>
              <p className={styles.featureDesc} style={{ fontSize: '0.95rem' }}>Integrated video analytics filter out routine background noise, automatically flagging only the activity that meets specific threat criteria.</p>
            </div>
            
            <div className={styles.featureCard} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', padding: '30px 20px' }}>
              <div className={styles.featureCardIcon} style={{ width: '56px', height: '56px', marginBottom: '16px' }}>
                <Mic size={28} />
              </div>
              <h3 className={styles.featureTitle} style={{ marginBottom: '10px', fontSize: '1.15rem' }}>Live Voice Intervention</h3>
              <p className={styles.featureDesc} style={{ fontSize: '0.95rem' }}>Monitoring operators use integrated two-way audio to speak directly to the intruder, creating a strong psychological deterrent.</p>
            </div>
          </div>
        </div>
      </section>

      {/* ===== 5. OPERATIONS (DARK) ===== */}
      <section className={`${styles.section} ${styles.sectionDark}`} id="operations">
        <div className="container">
          <div className={styles.splitGrid} style={{ marginBottom: '40px', alignItems: 'flex-start' }}>
            <div className={styles.sectionHeaderLeft} style={{ marginBottom: 0 }}>
              <span className={`${styles.sectionTag} ${styles.sectionTagDark}`}>Full Integration</span>
              <h2 className={`${styles.sectionTitle} ${styles.sectionTitleDark}`}>
                Secure Guard’s Security Operations
              </h2>
              <div className={`${styles.bodyText} ${styles.bodyTextDark}`}>
                <h4 style={{ color: 'var(--color-gold)', marginBottom: '8px' }}>Unified Operational Structure</h4>
                <p style={{ marginBottom: '20px' }}>Secure Guard connects field hardware directly with live dispatchers, mobile patrol units, on-site officers, field supervisors, and the SecureTrack reporting platform.</p>
                
                <h4 style={{ color: 'var(--color-gold)', marginBottom: '8px' }}>Dispatch Coordination</h4>
                <p style={{ marginBottom: '20px' }}>Central dispatch serves as the operational hub, evaluating live updates, managing communications, and coordinating the precise response protocol.</p>
                
                <h4 style={{ color: 'var(--color-gold)', marginBottom: '8px' }}>Mobile Patrol & On-Site Personnel</h4>
                <p>For properties where visual monitoring needs a physical presence, mobile patrol officers and dedicated security guards provide immediate on-scene backup.</p>
              </div>
            </div>
            <div className={styles.sectionHeaderLeft} style={{ marginBottom: 0, padding: '32px', background: 'rgba(255,255,255,0.03)', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.1)' }}>
              <h2 className={`${styles.sectionTitle} ${styles.sectionTitleDark}`} style={{ fontSize: '1.8rem' }}>
                SecureTrack Reporting and Visibility
              </h2>
              <p className={`${styles.bodyText} ${styles.bodyTextDark}`}>
                SecureTrack transforms security data into actionable operational records by automatically capturing every surveillance alert, live intervention, patrol sweep, and incident with time-stamped, location-verified accuracy.
              </p>
              <p className={`${styles.bodyText} ${styles.bodyTextDark}`} style={{ marginBottom: 0 }}>
                By creating a detailed, indisputable timeline of when activity occurred, what response was taken, and how the situation was resolved, the platform gives property managers total operational visibility across remote or expansive sites, delivering complete transparency and insurance compliance off-site.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ===== 6. APPLICATIONS CAROUSEL (LIGHT) ===== */}
      <section className={styles.section} id="applications">
        <div className="container">
          <div className={styles.sectionHeaderCentered}>
            <span className={styles.sectionTag}>Deployment Scenarios</span>
            <h2 className={styles.sectionTitle}>
              Industry Applications
            </h2>
            <p className={styles.bodyTextCentered}>
              Mobile surveillance towers provide critical security coverage for expansive, remote, or temporary outdoor spaces where traditional wired cameras cannot be installed.
            </p>
          </div>

          <ApplicationsCarousel />
        </div>
      </section>

      {/* ===== 7. WHY CHOOSE SECURE GUARD (DARK) ===== */}
      <section className={`${styles.section} ${styles.sectionDark}`} id="why-secure-guard">
        <div className="container">
          <div className={styles.sectionHeaderCentered} style={{ maxWidth: '900px' }}>
            <span className={`${styles.sectionTag} ${styles.sectionTagDark}`}>Multi-Layered Defense</span>
            <h2 className={`${styles.sectionTitle} ${styles.sectionTitleDark}`}>
              Why Choose Secure Guard for Mobile Surveillance?
            </h2>
            <p className={`${styles.bodyTextCentered} ${styles.bodyTextDark}`}>
              Secure Guard goes beyond providing standalone hardware by fully integrating mobile surveillance towers into a complete, managed security framework. By pairing intelligent AI detection and live voice intervention with trained monitoring operators, central dispatch, mobile patrols, on-site guards, and SecureTrack digital reporting, Secure Guard creates a multi-layered defense around your property.
            </p>
          </div>
        </div>
      </section>

      {/* ===== 8. FAQ (LIGHT) ===== */}
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
with open(page_path, "w", encoding="utf-8") as f:
    f.write(page_content)
