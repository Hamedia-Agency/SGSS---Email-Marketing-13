import os

project_root = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-10"

# 1. Write ApplicationsCarousel.tsx
apps_carousel_content = """\
"use client";

import { useCallback } from 'react';
import useEmblaCarousel from 'embla-carousel-react';
import { ChevronLeft, ChevronRight } from 'lucide-react';
import Image from 'next/image';
import styles from './SupervisionCarousel.module.css';

const items = [
  {
    title: "Construction Sites",
    desc: "Unattended building sites present high-value targets for material theft, tool loss, and equipment vandalism. Active video monitoring provides continuous oversight across perimeter fencing, staging areas, and equipment yards, allowing remote operators to verify live intrusions immediately and initiate response protocols before assets are stolen or damaged.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/qp.webp"
  },
  {
    title: "Commercial & Retail Centers",
    desc: "Loading docks, service corridors, rear entrances, and secondary parking areas become prime targets once business hours end. Remote operators monitor these vulnerable access points during off-hours, detecting loitering, unauthorized entry, or property damage early and coordinating with mobile patrols or emergency services to resolve threats quickly.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/plbs.webp"
  },
  {
    title: "Parking Structures & Garages",
    desc: "Multi-level parking facilities contain extensive blind spots across stairwells, driving lanes, and vehicle access gates that physical patrols cannot monitor continuously. Active video surveillance fills these coverage gaps by maintaining visual oversight across key transit areas, allowing monitoring personnel to evaluate live activity in real time and dispatch on-ground enforcement when necessary.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/rmlth.webp"
  },
  {
    title: "Industrial Facilities & Storage Yards",
    desc: "Large facility layouts and outdoor yards holding machinery, raw materials, and fleet vehicles present perimeter defense challenges that physical guards alone cannot cover efficiently. Combining remote live monitoring with targeted mobile patrol response creates a cost-effective, multi-layered security barrier across large outdoor assets.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/pioc.webp"
  }
];

export default function ApplicationsCarousel() {
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
with open(os.path.join(project_root, "src", "components", "ApplicationsCarousel.tsx"), "w", encoding="utf-8") as f:
    f.write(apps_carousel_content)


# 2. Write FAQAccordion.tsx
faq_content = """\
"use client";

import { useState } from "react";
import styles from "./FAQAccordion.module.css";
import { ChevronDown, ChevronUp } from "lucide-react";

const faqData = [
  {
    question: "Do I need to replace my existing security cameras?",
    answer: "In most cases, no. Secure Guard evaluates your current cameras, recording equipment, and network infrastructure to layer live monitoring directly onto your existing hardware—eliminating unnecessary replacement costs."
  },
  {
    question: "Are operators watching my camera feeds continuously 24/7?",
    answer: "Monitoring coverage is configured based on your property’s specific schedule and risk profile. Active monitoring typically activates during high-vulnerability off-hours, routing live feeds to operators the moment motion or unusual activity is detected."
  },
  {
    question: "What happens when suspicious motion is detected after hours?",
    answer: "When an automated sensor trips, an operator inspects the live feed within seconds to assess the situation. If a genuine threat is confirmed, operators execute your pre-established response protocol—initiating live voice-down warnings, notifying property managers, dispatching mobile field patrols, or contacting law enforcement for priority response."
  },
  {
    question: "How does live visual verification prevent false alarm fines?",
    answer: "By inspecting the live feed before taking action, operators filter out environmental triggers like stray animals, wind-blown debris, passing headlights, or weather conditions. Emergency services are only contacted for verified threats, saving your property from costly municipal false alarm penalties."
  },
  {
    question: "Can video monitoring work alongside physical security guards and mobile patrols?",
    answer: "Yes. Video monitoring and physical security complement each other. Cameras provide broad visual coverage across wide areas, while on-site officers and mobile patrols deliver physical presence and immediate on-ground intervention."
  },
  {
    question: "Does video monitoring integrate with SecureTrack reporting?",
    answer: "Yes. Active video monitoring works directly alongside SecureTrack to give you full operational transparency through digital daily activity logs, time-stamped incident documentation with photo evidence, and guard checkpoint tracking."
  },
  {
    question: "What types of properties benefit most from active video monitoring?",
    answer: "It is ideal for commercial properties with after-hours vulnerabilities or expansive footprints, including construction sites, retail centers, multi-level parking structures, industrial facilities, and outdoor storage yards."
  }
];

export default function FAQAccordion() {
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  const toggleAccordion = (index: number) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  return (
    <div className={styles.faqWrapper}>
      {faqData.map((faq, index) => {
        const isOpen = openIndex === index;
        return (
          <div 
            key={index} 
            className={`${styles.faqItem} ${isOpen ? styles.faqItemOpen : ""}`}
          >
            <button
              className={styles.faqQuestion}
              onClick={() => toggleAccordion(index)}
              aria-expanded={isOpen}
            >
              <span>{faq.question}</span>
              {isOpen ? (
                <ChevronUp className={styles.faqIcon} size={20} />
              ) : (
                <ChevronDown className={styles.faqIcon} size={20} />
              )}
            </button>
            
            <div className={`${styles.faqAnswer} ${isOpen ? styles.faqAnswerOpen : ""}`}>
              <div className={styles.faqAnswerInner}>
                <p>{faq.answer}</p>
              </div>
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


# 3. Write page.tsx
page_content = """\
import Image from "next/image";
import styles from "./page.module.css";
import { Navbar } from "@/components/Navbar";
import { Footer } from "@/components/Footer";
import BackToTop from "@/components/BackToTop";
import { PreFooterCTA } from "@/components/PreFooterCTA";
import ApplicationsCarousel from "@/components/ApplicationsCarousel";
import ParticleMesh from "@/components/ParticleMesh";
import FAQAccordion from "@/components/FAQAccordion";

export default function HomePage() {
  return (
    <main className={styles.main}>
      <Navbar />

      {/* ===== SECTION 1: HERO ===== */}
      <section className={styles.hero} id="hero">
        <div className={styles.heroBg}>
          <Image
            src="https://cms.secureguardservices.com/wp-content/uploads/2026/08/em8-1-1.webp"
            alt="Active Video Monitoring"
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
              Comprehensive Protection
            </div>
            <h1 className={styles.heroTitle} id="hero-title">
              Active Video <span className={styles.heroTitleAccent}>Monitoring</span>
            </h1>
            <p className={styles.heroSubtitle}>
              Secure Guard connects existing security camera infrastructure to live video monitoring operations. When automated systems detect after-hours motion, trained operators inspect the live feed, verify site conditions, and initiate immediate on-site response protocols.
            </p>
            <div className={styles.heroCtas}>
              <a 
                href="#prefooter-cta" 
                className={styles.btnPrimary} 
                id="hero-cta-primary"
              >
                Explore Video Monitoring for Your Property
              </a>
            </div>
          </div>
        </div>
        <div className={styles.heroScroll} aria-hidden="true">
          <span className={styles.heroScrollDot} />
        </div>
      </section>

      {/* ===== SECTION 2: Passive Recording to Live Response ===== */}
      <section className={styles.section} id="vulnerability">
        <div className="container">
          <div className={styles.addonGrid}>
            <div className={styles.addonImageCol}>
              <Image 
                src="https://cms.secureguardservices.com/wp-content/uploads/2026/08/em8-2.webp" 
                alt="Live Threat Detection" 
                width={500} 
                height={400} 
                className={styles.addonImage} 
                style={{ borderRadius: "12px", objectFit: "cover" }}
              />
            </div>
            <div className={styles.addonContent}>
              <div className={styles.sectionHeader} style={{ margin: "0", textAlign: "left" }}>
                <span className={styles.sectionTag}>Live Threat Response</span>
                <h2 className={styles.sectionTitle} style={{ marginBottom: "16px" }}>
                  Passive Recording to Live Response
                </h2>
              </div>
              <p className={styles.bodyText}>
                Secure Guard integrates active video monitoring into existing camera setups, converting standalone recording systems into a live threat detection and response network.
              </p>
              <p className={styles.bodyText}>
                The moment suspicious motion is detected, trained monitoring personnel immediately evaluate the live feed to distinguish routine site activity from genuine security threats.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ===== SECTION 3: How Active Video Monitoring Works ===== */}
      <section className={styles.section} id="setup" style={{ background: "var(--color-bg-alt, #f7f9fc)" }}>
        <div className="container">
          <div className={styles.setupUnifiedContainer}>
            {/* Left Pane */}
            <div className={styles.setupLeftPane}>
              <span className={styles.setupLeftTag}>Active Operational Response</span>
              <h2 className={styles.setupLeftTitle}>
                How Active Video Monitoring Works
              </h2>
              <p className={styles.setupLeftDesc}>
                Active video monitoring transforms automated camera alerts into an immediate, verified human response. Instead of storing footage of an ongoing incident or triggering false alarms, live feeds are instantly routed to trained operators who evaluate the threat and execute your property's specific escalation procedures. This closed-loop process moves your security from passive detection to active operational response across four key steps:
              </p>
            </div>
            
            {/* Right Pane (Grid) */}
            <div className={styles.setupRightGrid}>
              <div className={`${styles.setupGridItem} ${styles.setupItem1}`}>
                <div className={styles.setupItemHeader}>
                  <span className={styles.setupItemIcon}>01</span>
                  <h3 className={styles.setupItemTitle}>Activity Detection</h3>
                </div>
                <p className={styles.setupItemDesc}>
                  Targeted camera zones flag motion during high-vulnerability hours. Critical access points instantly trigger alerts, capturing potential risks early without manual screen monitoring.
                </p>
              </div>

              <div className={`${styles.setupGridItem} ${styles.setupItem2}`}>
                <div className={styles.setupItemHeader}>
                  <span className={styles.setupItemIcon}>02</span>
                  <h3 className={styles.setupItemTitle}>Live Feed Review</h3>
                </div>
                <p className={styles.setupItemDesc}>
                  Operators perform an immediate live video inspection to determine the true nature of the alert, filtering out harmless environmental triggers and focusing on genuine threats.
                </p>
              </div>

              <div className={`${styles.setupGridItem} ${styles.setupItem3}`}>
                <div className={styles.setupItemHeader}>
                  <span className={styles.setupItemIcon}>03</span>
                  <h3 className={styles.setupItemTitle}>Suspicious Activity Verification</h3>
                </div>
                <p className={styles.setupItemDesc}>
                  The monitoring team conducts a visual assessment of location, individuals, and actions, creating a verified intelligence profile before initiating any escalation.
                </p>
              </div>

              <div className={`${styles.setupGridItem} ${styles.setupItem4}`}>
                <div className={styles.setupItemHeader}>
                  <span className={styles.setupItemIcon}>04</span>
                  <h3 className={styles.setupItemTitle}>Response Protocol</h3>
                </div>
                <p className={styles.setupItemDesc}>
                  Operators execute your designated response, which can include two-way voice-down warnings, notifying managers, dispatching field supervisors, or contacting law enforcement.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ===== SECTION 4: Industry Applications (Carousel) ===== */}
      <section className={styles.featuresSection} id="applications">
        <div className="container">
          <div className={styles.sectionHeader}>
            <span className={styles.sectionTag} style={{ color: "#b89000", background: "rgba(254, 207, 49, 0.13)", borderColor: "rgba(254, 207, 49, 0.35)" }}>Customized Coverage</span>
            <h2 className={styles.sectionTitle} style={{ color: "var(--color-white)" }}>
              Industry Applications
            </h2>
            <p className={styles.bodyTextCenteredLight} style={{ color: "rgba(255, 255, 255, 0.85)" }}>
              Secure Guard customizes active video monitoring to align with the specific operational layouts, high-value assets, and risk profiles of diverse commercial environments, delivering real-time threat response where traditional security falls short.
            </p>
          </div>

          <ApplicationsCarousel />
        </div>
      </section>

      {/* ===== SECTION 5: Why Live Verification Matters (Escalation box) ===== */}
      <section className={styles.contactSection} id="verification">
        <div className={`container ${styles.contactContainer}`}>
          <div className={styles.contactContentPanel}>
            <div className={styles.sectionHeader} style={{ margin: "0 0 24px 0", textAlign: "left" }}>
              <span className={styles.sectionTag} style={{ color: "#b89000", background: "rgba(254, 207, 49, 0.13)", borderColor: "rgba(254, 207, 49, 0.35)" }}>Verified Proof</span>
              <h2 className={styles.sectionTitle} style={{ marginBottom: "16px", color: "var(--color-white)" }}>
                Why Live Verification Matters
              </h2>
            </div>
            <p className={styles.bodyText} style={{ color: "rgba(255, 255, 255, 0.9)" }}>
              Unverified alerts lead to alarm fatigue, wasted operational costs, and delayed emergency response. Live human verification ensures your team only acts on genuine threats, keeping property managers focused on real issues rather than constant false notifications.
            </p>
            <p className={styles.bodyText} style={{ color: "rgba(255, 255, 255, 0.9)", marginBottom: 0 }}>
              More importantly, verification connects video technology directly to physical security on the ground. While cameras provide broad visual coverage from a distance, mobile patrols and on-site guards deliver the physical presence needed to resolve issues. Pairing live remote oversight with field response creates a complete defense—closing blind spots across your facility without unnecessarily inflating post-hour costs.
            </p>
          </div>
        </div>
      </section>

      {/* ===== SECTION 6: Integration & Coverage (Text section) ===== */}
      <section className={styles.section} id="integration">
        <div className="container">
          <div className={styles.sectionHeader}>
            <span className={styles.sectionTag}>Seamless Hardware Use</span>
            <h2 className={styles.sectionTitle}>
              Existing Camera Integration
            </h2>
            <p className={styles.bodyTextCenteredLight} style={{ color: "var(--color-text)", maxWidth: "800px" }}>
              Upgrading to active video oversight does not require replacing your current surveillance hardware. Secure Guard evaluates your existing setup, analyzing camera technology, visual coverage, network bandwidth, and vulnerable blind spots. Where compatible, your existing camera feeds are integrated directly into our 24/7 monitoring platform, layering live human judgment and swift response protocols over your existing infrastructure without forcing unnecessary capital expenditures.
            </p>
          </div>
          
          <div className={styles.sectionHeader} style={{ marginTop: '80px' }}>
            <span className={styles.sectionTag}>Strategic Focus</span>
            <h2 className={styles.sectionTitle}>
              Targeted Security Coverage
            </h2>
            <p className={styles.bodyTextCenteredLight} style={{ color: "var(--color-text)", maxWidth: "800px" }}>
              Secure Guard strategically prioritizes high-vulnerability locations—such as perimeter gates, equipment yards, loading docks, parking structures, and storage enclosures—where unauthorized access poses the greatest risk. By focusing active monitoring resources on these critical zones rather than low-risk areas, we deliver maximum security impact and threat prevention right where your property is most exposed.
            </p>
          </div>
        </div>
      </section>

      {/* ===== SECTION 7: Our Security Standard ===== */}
      <section className={styles.standardSection} id="standard">
        <div className={styles.standardPatternLeft}>
          <ParticleMesh particleCount={22} />
        </div>
        <div className={styles.standardPatternRight}>
          <ParticleMesh particleCount={22} />
        </div>
        <div className="container">
          <div className={styles.standardHeader} style={{ marginBottom: 0 }}>
            <span className={styles.sectionTag}>Connected Security</span>
            <h2 className={styles.sectionTitle}>The Secure Guard Difference</h2>
            <p className={styles.standardSubtitle}>
              Cameras and automated alerts can flag activity, but they cannot assess intent or evaluate real-world risk. Secure Guard bridges this gap by pairing video technology with trained human judgment and integrated field operations. By combining remote live monitoring with dispatch support, mobile patrols, on-site officers, and detailed reporting, we deliver a fully connected security model.
            </p>
          </div>
        </div>
      </section>

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

print("SUCCESS")
