"use client";

import { useCallback } from 'react';
import useEmblaCarousel from 'embla-carousel-react';
import { ChevronLeft, ChevronRight } from 'lucide-react';
import Image from 'next/image';
import styles from './EvaluationCarousel.module.css';

const items = [
  {
    title: "Access Points & Secondary Entrances",
    desc: "Secure Guard inspects all entry channels beyond the main entrance, including service doors, loading gates, emergency exits, and employee side entrances. We evaluate who uses each entrance, how credentials are verified during business hours, and how access controls tighten after hours to prevent overlooked doors from becoming easy entry points for trespassers.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/em10-1.webp"
  },
  {
    title: "Parking Areas & Blind Spots",
    desc: "We assess dark or isolated parking zones, structures, corners, and vehicle traffic routes to uncover visibility gaps. By evaluating lighting quality and camera lines-of-sight across employee and visitor parking, we ensure patrols and technology provide clear, uninterrupted oversight during peak and off-hour periods.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/em10-2.webp"
  },
  {
    title: "Loading Docks & High-Traffic Zones",
    desc: "Delivery docks, staging areas, and service bays experience constant movement from vendors, contractors, and staff, making unauthorized activity easy to disguise. Secure Guard reviews vendor check-in procedures, vehicle logging, and off-hour access protocols to eliminate operational blind spots and maintain complete accountability across high-activity zones.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/em8-1-1.webp"
  },
  {
    title: "Patrol Routes & Guard Coverage",
    desc: "Having an on-site guard does not guarantee full property protection if patrol paths are predictable or incomplete. We review guard routes against your physical layout to ensure officers actively cover high-risk perimeters, dark corners, and restricted zones rather than walking repetitive, predictable loops that leave areas vulnerable.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/qp.webp"
  },
  {
    title: "Camera Placement & Technology Integration",
    desc: "Rather than automatically recommending costly new equipment, Secure Guard reviews your existing camera system for blind spots, obstructed angles, and missing coverage. We identify opportunities to adjust camera positioning, improve live monitoring workflows, and connect video feeds with active patrol response to make your current technology far more effective.",
    imgSrc: "https://cms.secureguardservices.com/wp-content/uploads/2026/08/plbs.webp"
  }
];

export default function EvaluationCarousel() {
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
