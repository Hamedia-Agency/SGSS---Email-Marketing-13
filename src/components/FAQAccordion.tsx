"use client";

import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import styles from './FAQAccordion.module.css';

const faqs = [
  {
    question: "What is a site vulnerability audit, and what does it evaluate?",
    answer: "A site vulnerability audit is a structured review of your property's physical environment, operating conditions, and active security measures. Secure Guard evaluates both physical and operational security—including secondary access points, parking lighting, loading docks, patrol route predictability, camera coverage, visitor traffic flow, and after-hours procedures—to ensure your setup addresses real-world risks."
  },
  {
    question: "Is there any cost or obligation tied to requesting a security assessment walkthrough?",
    answer: "No. We offer an initial site evaluation to review your property layout, identify visual blind spots, and discuss potential operational improvements without any financial commitment or obligation."
  },
  {
    question: "How long does a typical walkthrough take, and will it interrupt daily operations?",
    answer: "A walkthrough typically takes between 1 and 2 hours, depending on the size of your property. Our specialists conduct the review quietly in the background without causing disruptions to your employees, tenants, or daily business operations."
  },
  {
    question: "Do we need to replace our current security provider or camera system to get an assessment?",
    answer: "No. Our objective is to evaluate your site objectively. We focus on identifying security gaps and showing you how to make your existing setup, guard force, and camera positioning more effective, regardless of what equipment or provider you currently use."
  },
  {
    question: "Will the assessment automatically recommend hiring on-site security guards?",
    answer: "Not necessarily. The appropriate solution depends entirely on your site's specific vulnerabilities and operational goals. Recommendations may involve mobile patrols, camera repositioning, solar surveillance towers, remote video monitoring, or simple procedural updates rather than full-time standing officers."
  },
  {
    question: "Can Secure Guard assess large facilities or properties with multiple buildings?",
    answer: "Yes. We evaluate multi-building campuses, industrial parks, commercial plazas, and residential communities based on their unique layouts, access points, traffic flows, and localized risk factors."
  },
  {
    question: "Can the assessment identify vulnerabilities during off-hours and shift changes?",
    answer: "Yes. We analyze how security risks shift during evenings, overnight periods, weekends, holidays, and shift changes to ensure your coverage addresses periods when normal property activity decreases."
  },
  {
    question: "What do we receive after the security walkthrough is completed?",
    answer: "You will receive a clear, plain-language breakdown of your site's physical vulnerabilities and operational gaps, along with prioritized recommendations on how to resolve them efficiently."
  },
  {
    question: "Is this assessment a substitute for official engineering or regulatory risk audits?",
    answer: "No. A Secure Guard site vulnerability audit evaluates security operations and practical threat mitigation from a security-service perspective. It is not a substitute for specialized engineering, life-safety, regulatory, insurance, or law-enforcement compliance audits."
  }
];

export default function FAQAccordion() {
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  const toggleOpen = (index: number) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  return (
    <div className={styles.accordionContainer}>
      {faqs.map((faq, index) => {
        const isOpen = openIndex === index;
        return (
          <div 
            key={index} 
            className={`${styles.accordionItem} ${isOpen ? styles.open : ''}`}
          >
            <button 
              className={styles.accordionHeader} 
              onClick={() => toggleOpen(index)}
              aria-expanded={isOpen}
            >
              <h3 className={styles.accordionTitle}>{faq.question}</h3>
              <span className={styles.accordionIcon}>
                <ChevronDown size={20} />
              </span>
            </button>
            <div 
              className={styles.accordionContent}
              style={{ maxHeight: isOpen ? '500px' : '0' }}
            >
              <div className={styles.accordionContentInner}>
                <p>{faq.answer}</p>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
}