import os

project_root = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-11"

# 1. ProcessExplorer.tsx
process_explorer_content = """\
"use client";

import React, { useState } from "react";
import { 
  ScanSearch, 
  Eye, 
  Volume2, 
  ShieldAlert 
} from "lucide-react";
import styles from "./ProcessExplorer.module.css";

const processItems = [
  {
    title: "AI Analytics and Motion Tracking",
    shortTitle: "Detection",
    description: "AI analytics scan designated site boundaries 24/7 to track movement patterns. The system instantly detects unauthorized human or vehicle activity while automatically filtering out false triggers like weather, swaying trees, or small wildlife.",
    icon: ScanSearch,
    label: "Step 1"
  },
  {
    title: "Live Command Center Assessment",
    shortTitle: "Verification",
    description: "Triggered alerts immediately route live video feeds to a central command center. Trained operators review the footage within seconds to confirm whether the activity poses a genuine security threat or is simply authorized site movement.",
    icon: Eye,
    label: "Step 2"
  },
  {
    title: "Live Verbal Warnings and Strobes",
    shortTitle: "Deterrence",
    description: "Once a threat is confirmed, operators issue direct, live verbal warnings over high-decibel loudspeakers accompanied by flashing strobes. Communicating directly with the intruder in real time forces most trespassers to flee immediately.",
    icon: Volume2,
    label: "Step 3"
  },
  {
    title: "Dispatching Field Resources",
    shortTitle: "Response",
    description: "If the trespasser fails to comply, operators escalate the incident by dispatching local field resources and requesting priority law enforcement response for a verified crime in progress.",
    icon: ShieldAlert,
    label: "Step 4"
  }
];

export function ProcessExplorer() {
  const [activeTab, setActiveTab] = useState(0);
  const activeItem = processItems[activeTab];
  const IconComponent = activeItem.icon;

  return (
    <div className={styles.explorerContainer}>
      <div className={styles.tabList}>
        {processItems.map((item, index) => {
          const ItemIcon = item.icon;
          return (
            <button
              key={index}
              onClick={() => setActiveTab(index)}
              className={`${styles.tabButton} ${activeTab === index ? styles.activeTabButton : ""}`}
              aria-label={`Show details for ${item.title}`}
            >
              <span className={styles.tabIcon}>
                <ItemIcon size={20} />
              </span>
              <span className={styles.tabTitle}>{item.shortTitle}</span>
            </button>
          );
        })}
      </div>

      <div className={styles.displayCard} key={activeTab}>
        <div className={styles.cardHeader}>
          <span className={styles.cardTag}>{activeItem.label}</span>
          <h3 className={styles.cardTitle}>{activeItem.title}</h3>
          <p className={styles.cardDescription}>{activeItem.description}</p>
        </div>

        <div className={styles.visualWrapper}>
          <div className={styles.glowOrb} />
          <div className={styles.illustrationCard}>
            <IconComponent size={64} className={styles.visualIcon} />
            <span className={styles.visualLabel}>{activeItem.shortTitle}</span>
          </div>
        </div>
      </div>
    </div>
  );
}
"""
with open(os.path.join(project_root, "src", "components", "ProcessExplorer.tsx"), "w", encoding="utf-8") as f:
    f.write(process_explorer_content)

# 2. IndustryApplications.tsx (Replacing CoverageSection)
industry_applications_content = """\
import React from "react";
import styles from "./CoverageSection.module.css";
import { Construction, Factory, Car, Building, Tent } from "lucide-react";

const locations = [
  { name: "Construction Sites", desc: "Protects unpowered job sites from day one against the theft of equipment and materials." },
  { name: "Industrial Yards", desc: "Delivers broad visual coverage across expansive yards storing high-value machinery." },
  { name: "Commercial Parking", desc: "Overcomes ground-level blind spots across parking lanes to prevent break-ins." },
  { name: "Vacant Properties", desc: "Establishes an immediate, off-grid security presence to deter trespassing." },
  { name: "Outdoor Venues", desc: "Provides short-term, rapid-deployment surveillance for high-traffic entryways." }
];

export const IndustryApplications = () => {
  return (
    <section 
      className={styles.coverageSection} 
      id="applications"
      style={{
        backgroundImage: 'url("https://cms.secureguardservices.com/wp-content/uploads/2026/08/em8-1-1.webp")'
      }}
    >
      <div className={styles.overlay} />
      
      <div className={`container ${styles.content}`}>
        <div className={styles.badge}>Deployment Scenarios</div>
        <h2 className={styles.title}>
          Industry <span className={styles.accent}>Applications</span>
        </h2>
        <p className={styles.description}>
          Mobile surveillance towers provide critical security coverage for expansive, remote, or temporary outdoor spaces where traditional wired cameras cannot be installed.
        </p>
      </div>

      <div className={styles.marqueeContainer}>
        <div className={styles.marqueeContent}>
          {locations.map((loc, idx) => (
            <div key={`loc-1-${idx}`} className={styles.marqueeItem} style={{ flexDirection: 'column', alignItems: 'flex-start', padding: '24px', maxWidth: '350px', whiteSpace: 'normal', height: '100%', minHeight: '140px' }}>
              <span style={{ fontWeight: 'bold', fontSize: '1.2rem', marginBottom: '8px', display: 'block', color: 'var(--color-gold)' }}>{loc.name}</span>
              <span style={{ fontSize: '0.9rem', lineHeight: '1.4', opacity: 0.9 }}>{loc.desc}</span>
            </div>
          ))}
        </div>
        <div className={styles.marqueeContent} aria-hidden="true">
          {locations.map((loc, idx) => (
            <div key={`loc-2-${idx}`} className={styles.marqueeItem} style={{ flexDirection: 'column', alignItems: 'flex-start', padding: '24px', maxWidth: '350px', whiteSpace: 'normal', height: '100%', minHeight: '140px' }}>
              <span style={{ fontWeight: 'bold', fontSize: '1.2rem', marginBottom: '8px', display: 'block', color: 'var(--color-gold)' }}>{loc.name}</span>
              <span style={{ fontSize: '0.9rem', lineHeight: '1.4', opacity: 0.9 }}>{loc.desc}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
"""
with open(os.path.join(project_root, "src", "components", "IndustryApplications.tsx"), "w", encoding="utf-8") as f:
    f.write(industry_applications_content)

# 3. FAQAccordion.tsx
faq_content = '''"use client";

import { useState } from "react";
import styles from "./FAQAccordion.module.css";
import { ChevronDown } from "lucide-react";

const faqData = [
  { question: "Do mobile surveillance towers require local electricity or Wi-Fi?", answer: "No. Towers operate 100% off-grid using onboard solar panels and cellular connectivity, making them completely independent of local power hookups and Wi-Fi networks." },
  { question: "How quickly can a tower be deployed, and can it be moved as site needs change?", answer: "Towers can be delivered and deployed rapidly once site conditions are evaluated. Because they are mobile units, they can easily be repositioned as project phases shift, construction progresses, or site layouts change." },
  { question: "Does the system operate in complete darkness?", answer: "Yes. Mobile towers are equipped with infrared night vision and high-intensity lighting to maintain visual clarity and detection capabilities overnight, on weekends, and during unlit site conditions." },
  { question: "Are operators watching my camera feeds continuously 24/7?", answer: "Monitoring is configured to your property’s schedule and risk profile. Active monitoring typically activates during off-hours, using AI analytics to alert central command operators the moment suspicious motion or boundary breaches occur." },
  { question: "What happens when suspicious activity is detected after hours?", answer: "Within seconds of an alert, a live operator inspects the feed to verify the threat. If an unauthorized trespasser is confirmed, the operator issues live verbal commands over high-decibel loudspeakers and activates strobes to warn them off. If compliance fails, operators dispatch mobile patrols or notify law enforcement for priority response." },
  { question: "How does live visual verification prevent false alarm fines?", answer: "Human operators review every alert before taking action, filtering out non-threats like animals, wind, or weather. Law enforcement is only contacted for verified crimes in progress, protecting your property from costly municipal false alarm penalties." },
  { question: "Can mobile surveillance towers replace security guards, or work alongside them?", answer: "Towers can function independently or complement physical security. While towers provide continuous wide-area visual coverage and automated deterrence, on-site guards and mobile patrol officers provide physical presence, access control, and immediate ground intervention." },
  { question: "Do I need to replace my existing security cameras?", answer: "In most cases, no. Secure Guard can layer live monitoring protocols directly onto your existing camera infrastructure and recording hardware, eliminating replacement costs." },
  { question: "How does SecureTrack reporting integrate with the surveillance tower program?", answer: "SecureTrack automatically logs every alert, live intervention, patrol sweep, and incident into a time-stamped digital record with photo evidence—giving property managers full operational visibility and insurance compliance off-site." },
  { question: "What types of properties benefit most from mobile surveillance towers?", answer: "Towers are ideal for expansive, remote, or temporary outdoor spaces, including construction sites, industrial equipment yards, commercial parking areas, vacant commercial properties, undeveloped land, and outdoor event venues." },
  { question: "Can Secure Guard monitor multiple towers across several locations?", answer: "Yes. Secure Guard centrally manages surveillance, central dispatch, mobile patrol, and SecureTrack reporting across multiple towers and multi-site footprints within a single security strategy." }
];

export function FAQAccordion() {
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  const toggleAccordion = (index: number) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  return (
    <div className={styles.accordionContainer}>
      {faqData.map((faq, index) => {
        const isOpen = openIndex === index;
        return (
          <div key={index} className={styles.accordionItem}>
            <button
              className={styles.accordionHeader}
              onClick={() => toggleAccordion(index)}
              aria-expanded={isOpen}
            >
              <h3 className={styles.accordionTitle}>{faq.question}</h3>
              <div className={`${styles.icon} ${isOpen ? styles.iconOpen : ""}`}>
                 <ChevronDown size={20} />
              </div>
            </button>
            <div className={`${styles.accordionContent} ${isOpen ? styles.accordionContentOpen : ""}`}>
              <p className={styles.accordionText}>{faq.answer}</p>
            </div>
          </div>
        );
      })}
    </div>
  );
}
'''
with open(os.path.join(project_root, "src", "components", "FAQAccordion.tsx"), "w", encoding="utf-8") as f:
    f.write(faq_content)

# 4. page.tsx
page_content = """\
import Image from "next/image";
import styles from "./page.module.css";
import { Navbar } from "@/components/Navbar";
import { Footer } from "@/components/Footer";
import BackToTop from "@/components/BackToTop";
import { PreFooterCTA } from "@/components/PreFooterCTA";

import { ProcessExplorer } from "@/components/ProcessExplorer";
import { IndustryApplications } from "@/components/IndustryApplications";
import { FAQAccordion } from "@/components/FAQAccordion";
import { 
  Camera, 
  Moon, 
  Sun, 
  Activity, 
  Mic, 
  ShieldCheck,
  Radio,
  CarFront
} from "lucide-react";

export default function HomePage() {
  return (
    <main className={styles.main}>
      <Navbar />

      {/* ===== HERO ===== */}
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

      {/* ===== WHY OUTDOOR PROPERTIES NEED MORE THAN CAMERAS ===== */}
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

      {/* ===== HOW MOBILE SURVEILLANCE TOWERS WORK ===== */}
      <section className={`${styles.section} ${styles.sectionAlt}`} id="how-it-works">
        <div className="container">
          <div className={styles.sectionHeaderCentered}>
            <span className={styles.sectionTag}>Connected Security Operations</span>
            <h2 className={styles.sectionTitle}>
              How Mobile Surveillance Towers Work
            </h2>
            <p className={styles.bodyTextCentered}>
              Towers function as fully integrated, connected security operations rather than passive recording devices.
            </p>
          </div>
          <ProcessExplorer />
        </div>
      </section>

      {/* ===== KEY FEATURES GRID ===== */}
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

      {/* ===== OPERATIONS AND REPORTING ===== */}
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

      {/* ===== INDUSTRY APPLICATIONS ===== */}
      <IndustryApplications />

      {/* ===== WHY CHOOSE SECURE GUARD ===== */}
      <section className={styles.section} id="why-secure-guard" style={{ background: "var(--color-bg-alt, #f7f9fc)" }}>
        <div className="container">
          <div className={styles.sectionHeaderCentered} style={{ maxWidth: '900px' }}>
            <span className={styles.sectionTag}>Multi-Layered Defense</span>
            <h2 className={styles.sectionTitle}>
              Why Choose Secure Guard for Mobile Surveillance?
            </h2>
            <p className={styles.bodyTextCentered}>
              Secure Guard goes beyond providing standalone hardware by fully integrating mobile surveillance towers into a complete, managed security framework. By pairing intelligent AI detection and live voice intervention with trained monitoring operators, central dispatch, mobile patrols, on-site guards, and SecureTrack digital reporting, Secure Guard creates a multi-layered defense around your property.
            </p>
          </div>
        </div>
      </section>

      {/* ===== FAQ ===== */}
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

print("SUCCESS")
