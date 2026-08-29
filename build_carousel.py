import os
import re

project_root = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-11"

# 1. ApplicationsCarousel.tsx
carousel_content = """\
"use client";

import { useCallback } from 'react';
import useEmblaCarousel from 'embla-carousel-react';
import { ChevronLeft, ChevronRight } from 'lucide-react';
import Image from 'next/image';
import styles from './SupervisionCarousel.module.css';

const items = [
  {
    title: "Construction Sites",
    desc: "Protects unpowered job sites from day one against the theft of equipment, tools, and materials during overnight and weekend hours.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/qp.webp"
  },
  {
    title: "Industrial & Equipment Yards",
    desc: "Delivers broad visual coverage across expansive yards storing high-value machinery, vehicles, and inventory to catch unauthorized movement early.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/pioc.webp"
  },
  {
    title: "Commercial Parking Areas",
    desc: "Overcomes ground-level blind spots across parking lanes and access points, using live voice deterrence to prevent vehicle break-ins, loitering, and property damage.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/rmlth.webp"
  },
  {
    title: "Vacant Properties",
    desc: "Establishes an immediate, off-grid security presence on unmanaged land or commercial sites to deter trespassing, illegal dumping, and squatting.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/plbs.webp"
  },
  {
    title: "Temporary Events & Outdoor Venues",
    desc: "Provides short-term, rapid-deployment surveillance for high-traffic entryways, staging areas, and equipment zones without permanent installation.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/esm.webp"
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
    f.write(carousel_content)


# 2. Modify page.tsx
page_path = os.path.join(project_root, "src", "app", "page.tsx")
with open(page_path, "r", encoding="utf-8") as f:
    page_text = f.read()

# Replace import
page_text = page_text.replace(
    'import { IndustryApplications } from "@/components/IndustryApplications";',
    'import ApplicationsCarousel from "@/components/ApplicationsCarousel";'
)

# Replace the component usage block
old_block = "      {/* ===== INDUSTRY APPLICATIONS ===== */}\n      <IndustryApplications />"
new_block = """      {/* ===== INDUSTRY APPLICATIONS (CAROUSEL) ===== */}
      <section className={styles.featuresSection} id="applications">
        <div className="container">
          <div className={styles.sectionHeader}>
            <span className={styles.sectionTag} style={{ color: "#b89000", background: "rgba(254, 207, 49, 0.13)", borderColor: "rgba(254, 207, 49, 0.35)" }}>Deployment Scenarios</span>
            <h2 className={styles.sectionTitle} style={{ color: "var(--color-white)" }}>
              Industry Applications
            </h2>
            <p className={styles.bodyTextCenteredLight} style={{ color: "rgba(255, 255, 255, 0.85)" }}>
              Mobile surveillance towers provide critical security coverage for expansive, remote, or temporary outdoor spaces where traditional wired cameras cannot be installed.
            </p>
          </div>

          <ApplicationsCarousel />
        </div>
      </section>"""

page_text = page_text.replace(old_block, new_block)

with open(page_path, "w", encoding="utf-8") as f:
    f.write(page_text)

print("SUCCESS")
