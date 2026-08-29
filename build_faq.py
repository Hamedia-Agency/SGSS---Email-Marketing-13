import os

content = """"use client";

import { useState } from "react";
import styles from "./FAQAccordion.module.css";
import { ChevronDown } from "lucide-react";

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
    <div className={styles.accordionContainer}>
      {faqData.map((faq, index) => {
        const isOpen = openIndex === index;
        return (
          <div 
            key={index} 
            className={styles.accordionItem}
          >
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

with open(r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-10\src\components\FAQAccordion.tsx", "w", encoding="utf-8") as f:
    f.write(content)
