import os

project_root = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12"

# 1. PillarsCarousel.tsx
pillars_carousel_content = """\
"use client";

import { useCallback } from 'react';
import useEmblaCarousel from 'embla-carousel-react';
import { ChevronLeft, ChevronRight } from 'lucide-react';
import Image from 'next/image';
import styles from './SupervisionCarousel.module.css';

const items = [
  {
    title: "Video Monitoring",
    desc: "Live video monitoring provides continuous visibility into designated areas of the property. Instead of relying solely on recorded footage after an incident, suspicious activity can be reviewed while it is happening.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/qp.webp"
  },
  {
    title: "Mobile Surveillance Towers",
    desc: "For large, open, temporary, or difficult-to-wire properties, mobile surveillance towers can provide elevated camera coverage, night visibility, live audio intervention, and remote monitoring without requiring traditional infrastructure across the entire site.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/pioc.webp"
  },
  {
    title: "Central Dispatch",
    desc: "Dispatch serves as the operational connection between monitoring and field personnel. When a situation requires additional support, dispatch can communicate with officers, mobile patrol units, supervisors, property contacts, and other appropriate resources.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/plbs.webp"
  },
  {
    title: "Security Officers",
    desc: "Standing security officers provide a physical presence at the property and can respond to incidents within their assigned responsibilities. Depending on the assignment, officers may manage access, conduct patrols, monitor activity, assist with emergencies, and document incidents.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/rmlth.webp"
  },
  {
    title: "Mobile Patrol",
    desc: "Mobile patrol extends physical security coverage across larger properties or locations that may not require a full-time officer. Patrol personnel can perform scheduled or randomized checks, investigate concerns, respond to verified activity, and provide an additional physical layer of protection.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/esm.webp"
  },
  {
    title: "SecureTrack",
    desc: "SecureTrack connects security operations, reporting, patrol activity, supervision, and field information into a coordinated management system. This gives Secure Guard greater visibility into what is happening across the security operation and provides clients with documented information about activity and response.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/qp.webp"
  }
];

export default function PillarsCarousel() {
  const [emblaRef, emblaApi] = useEmblaCarousel({ loop: true, align: 'start' });

  const scrollPrev = useCallback(() => {
    if (emblaApi) emblaApi.scrollPrev();
  }, [emblaApi]);

  const scrollNext = useCallback(() => {
    if (emblaApi) emblaApi.scrollNext();
  }, [emblaApi]);

  return (
    <div className={styles.carouselContainer}>
      <button 
        onClick={scrollPrev} 
        className={`${styles.navButton} ${styles.navLeft}`}
        aria-label="Previous"
      >
        <ChevronLeft size={24} />
      </button>

      <div className={styles.embla} ref={emblaRef}>
        <div className={styles.embla__container}>
          {items.map((item, idx) => (
            <div key={idx} className={styles.embla__slide}>
              <div className={styles.featureCard}>
                <div className={styles.featureCardImageWrapper}>
                  <Image src={item.imgSrc} alt={item.title} fill className={styles.featureCardImage} />
                </div>
                <div className={styles.featureCardContent}>
                  <h3 className={styles.featureCardTitle}>{item.title}</h3>
                  <p className={styles.featureCardDesc}>{item.desc}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      <button 
        onClick={scrollNext} 
        className={`${styles.navButton} ${styles.navRight}`}
        aria-label="Next"
      >
        <ChevronRight size={24} />
      </button>
    </div>
  );
}
"""
with open(os.path.join(project_root, "src", "components", "PillarsCarousel.tsx"), "w", encoding="utf-8") as f:
    f.write(pillars_carousel_content)

# 2. ProcessExplorer.tsx (5 steps)
process_explorer_content = """\
"use client";

import React, { useState } from "react";
import { 
  ScanSearch, 
  Eye, 
  Volume2, 
  ShieldAlert,
  FileText 
} from "lucide-react";
import styles from "./ProcessExplorer.module.css";

const processItems = [
  {
    title: "Real-Time Detection",
    shortTitle: "Detection",
    description: "High-definition fixed cameras, thermal sensors, and mobile surveillance towers continuously monitor perimeters, access points, and high-vulnerability assets to trigger instant system alerts upon unauthorized movement. This automated detection layer provides uninterrupted property oversight across expansive or complex commercial sites.",
    icon: ScanSearch,
    label: "Step 1"
  },
  {
    title: "Human Verification",
    shortTitle: "Verification",
    description: "Secure Guard’s 24/7 central monitoring specialists instantly evaluate live video feeds upon alert activation to distinguish genuine operational threats from harmless environmental movement. This human verification step eliminates false-alarm dispatch fees, assesses site risk against established post orders, and determines the exact response protocol.",
    icon: Eye,
    label: "Step 2"
  },
  {
    title: "Remote Intervention",
    shortTitle: "Intervention",
    description: "When suspicious activity is verified, monitoring personnel utilize high-decibel two-way speakers to broadcast live, localized voice-down warnings directly to unauthorized individuals on site. Delivering real-time verbal confirmation that the facility is actively monitored establishes immediate deterrence, forcing trespassers to vacate before property damage occurs.",
    icon: Volume2,
    label: "Step 3"
  },
  {
    title: "Coordinated Field Dispatch",
    shortTitle: "Dispatch",
    description: "When physical on-site intervention is required, central dispatch immediately deploys resources according to your customized property security plan. Dispatch coordinates mobile patrol units, alerts standing security guards, notifies designated property management contacts, or engages local emergency services with verified situational intelligence.",
    icon: ShieldAlert,
    label: "Step 4"
  },
  {
    title: "Digital Reporting and Documentation",
    shortTitle: "Reporting",
    description: "Every system alert, video verification, live intervention, and field dispatch action is automatically logged with verified timestamp and location metadata inside the SecureTrack platform. This generates complete, audit-ready activity reports and incident documentation, providing property managers with total operational transparency.",
    icon: FileText,
    label: "Step 5"
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

# 3. FAQAccordion.tsx
faq_content = """\
"use client";

import { useState } from "react";
import styles from "./FAQAccordion.module.css";
import { ChevronDown } from "lucide-react";

const faqData = [
  { question: "What is hybrid security?", answer: "Hybrid security combines technology-based monitoring (fixed cameras, thermal sensors, and mobile surveillance towers) with physical security services (central dispatch, standing officers, and mobile patrols) into one synchronized response network tailored to your site." },
  { question: "What types of properties benefit most from hybrid security?", answer: "It is ideal for commercial properties with after-hours vulnerabilities, expansive footprints, or multi-access points—including construction sites, industrial yards, retail centers, multi-level parking structures, multi-family complexes, and vacant properties." },
  { question: "Do I need to replace my existing security cameras?", answer: "In most cases, no. Secure Guard evaluates your current cameras and network infrastructure to layer live monitoring directly onto compatible hardware, eliminating hardware replacement costs. Supplemental equipment, such as mobile surveillance towers, is introduced only where coverage gaps exist." },
  { question: "Are operators watching my camera feeds continuously 24/7?", answer: "Active monitoring is configured around your property's specific schedule and risk profile. It typically activates during high-vulnerability off-hours, routing live feeds to central specialists the moment motion sensors or video analytics trigger an alert." },
  { question: "What happens when suspicious motion is detected?", answer: "Central specialists inspect the live feed within seconds. If a threat is confirmed, operators execute your pre-established protocol—broadcasting live voice-down warnings directly to trespassers, notifying property managers, or dispatching mobile field patrols and law enforcement." },
  { question: "How does live visual verification prevent false alarm fines?", answer: "Operators inspect live footage before initiating an escalation, filtering out environmental triggers like stray animals, wind-blown debris, or passing headlights. Emergency services and field units are dispatched only for verified threats, eliminating costly municipal false-alarm penalties." },
  { question: "Does hybrid security replace physical security guards?", answer: "Not necessarily. Hybrid security can operate without on-site guards by relying on remote monitoring and mobile patrols, or it can complement standing officers by extending coverage into blind spots beyond a guard's physical line of sight." },
  { question: "What is the role of central dispatch?", answer: "Dispatch serves as the operational link between monitoring operators and physical security personnel. When an incident requires on-ground intervention, dispatch routes verified situational intelligence to mobile patrol units, standing guards, property contacts, or local emergency services." },
  { question: "How does SecureTrack support hybrid security?", answer: "SecureTrack consolidates operations, patrol activity, guard tracking, and incident documentation into a single digital dashboard. It automatically logs exact timestamps for initial threat detection, human verification, voice intervention, field dispatch, and final resolution—delivering audit-ready transparency across your portfolio." }
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
"""
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
import PillarsCarousel from "@/components/PillarsCarousel";
import { FAQAccordion } from "@/components/FAQAccordion";
import { CoverageSection } from "@/components/CoverageSection";

export default function HomePage() {
  return (
    <main className={styles.main}>
      <Navbar />

      {/* ===== 1. HERO (DARK) ===== */}
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
              Secure Guard unifies video surveillance, 24/7 central dispatch, and field guard teams into one connected response network. Integrating with existing cameras or standalone mobile towers, our model manages the entire incident lifecycle.
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

      {/* ===== 2. VULNERABILITY (LIGHT) ===== */}
      <section className={styles.section} id="vulnerability">
        <div className="container">
          <div className={styles.splitGrid} style={{ marginBottom: '0', alignItems: 'center' }}>
            <div className={styles.splitImageWrapper} style={{ height: '100%', minHeight: '400px' }}>
              <Image 
                src="https://cms.secureguardservices.com/wp-content/uploads/2026/08/em8-2.webp" 
                alt="Connected Security Network" 
                fill
                className={styles.splitImage}
              />
            </div>
            <div className={styles.sectionHeaderLeft} style={{ marginBottom: 0 }}>
              <span className={styles.sectionTag}>Complete Incident Control</span>
              <h2 className={styles.sectionTitle}>
                Camera Alert Is Only the Beginning
              </h2>
              <p className={styles.bodyText}>
                Secure Guard’s hybrid security model bridges the gap between technology and physical security by managing the complete incident sequence for you. 
              </p>
              <p className={styles.bodyText}>
                Instead of leaving property managers to determine next steps after an alert, our connected system automatically flags off-hours activity, verifies live footage in seconds, and immediately executes your custom response protocols.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ===== 3. HOW IT WORKS (DARK) ===== */}
      <section className={`${styles.section} ${styles.sectionDark}`} id="how-it-works">
        <div className="container">
          <div className={styles.sectionHeaderCentered}>
            <span className={`${styles.sectionTag} ${styles.sectionTagDark}`}>Unified Incident Response</span>
            <h2 className={`${styles.sectionTitle} ${styles.sectionTitleDark}`}>
              How Hybrid Security Works
            </h2>
            <p className={`${styles.bodyTextCentered} ${styles.bodyTextDark}`}>
              Hybrid security combines technology and physical security so each layer supports the others.
            </p>
          </div>
          <ProcessExplorer />
        </div>
      </section>

      {/* ===== 4. HYBRID SECURITY PILLARS (LIGHT) ===== */}
      <section className={styles.section} id="pillars">
        <div className="container">
          <div className={styles.sectionHeaderCentered} style={{ marginBottom: '40px' }}>
            <span className={styles.sectionTag}>Secure Guard Framework</span>
            <h2 className={styles.sectionTitle}>
              The Secure Guard Hybrid Security Model
            </h2>
            <p className={styles.bodyTextCentered}>
              Secure Guard can connect mobile surveillance technology with live monitoring, dispatch, security officers, and mobile patrol services, giving physical teams better on-site context.
            </p>
          </div>
          <PillarsCarousel />
        </div>
      </section>

      {/* ===== 5. INTEGRATION & VISIBILITY (DARK) ===== */}
      <section className={`${styles.section} ${styles.sectionDark}`} id="integration">
        <div className="container">
          <div className={styles.splitGrid} style={{ marginBottom: '40px', alignItems: 'flex-start' }}>
            <div className={styles.sectionHeaderLeft} style={{ marginBottom: 0 }}>
              <span className={`${styles.sectionTag} ${styles.sectionTagDark}`}>Cost-Effective Oversight</span>
              <h2 className={`${styles.sectionTitle} ${styles.sectionTitleDark}`}>
                Existing Camera Integration
              </h2>
              <p className={`${styles.bodyText} ${styles.bodyTextDark}`}>
                Secure Guard evaluates and integrates your existing security infrastructure into our hybrid monitoring network, eliminating the operational expense of complete hardware replacement.
              </p>
              <p className={`${styles.bodyText} ${styles.bodyTextDark}`}>
                Compatible camera setups are connected directly into our 24/7 active monitoring, central dispatch, field response, and digital reporting ecosystem, instantly adding live human oversight and intervention to passive feeds.
              </p>
            </div>
            
            <div className={styles.sectionHeaderLeft} style={{ marginBottom: 0, padding: '32px', background: 'rgba(255,255,255,0.03)', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.1)' }}>
              <span className={`${styles.sectionTag} ${styles.sectionTagDark}`}>Total Transparency</span>
              <h2 className={`${styles.sectionTitle} ${styles.sectionTitleDark}`} style={{ fontSize: '1.8rem', marginTop: '8px' }}>
                Visibility Across the Entire Security Operation
              </h2>
              <p className={`${styles.bodyText} ${styles.bodyTextDark}`}>
                Secure Guard provides complete operational visibility across all your properties without requiring you to be physically on site. 
              </p>
              <p className={`${styles.bodyText} ${styles.bodyTextDark}`} style={{ marginBottom: 0 }}>
                By unifying live monitoring, field guard activity, and central dispatch into the SecureTrack platform, property managers gain real-time operational oversight and audit-ready incident tracking.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ===== 6. COVERAGE MARQUEE (LIGHT) ===== */}
      <CoverageSection />

      {/* ===== 7. FAQ (LIGHT) ===== */}
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

# 5. Fix components style widgets white background
# Since we copied them from Project 10, let's copy the custom styled CSS for white widgets
import shutil
shutil.copy(
    r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-11\src\components\ProcessExplorer.module.css",
    os.path.join(project_root, "src", "components", "ProcessExplorer.module.css")
)
shutil.copy(
    r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-11\src\components\SupervisionCarousel.module.css",
    os.path.join(project_root, "src", "components", "SupervisionCarousel.module.css")
)

print("SUCCESS")
