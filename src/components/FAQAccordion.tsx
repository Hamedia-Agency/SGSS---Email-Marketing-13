"use client";

import React, { useState } from "react";
import { ChevronDown } from "lucide-react";
import styles from "./FAQAccordion.module.css";

interface FAQItem {
  question: string;
  answer: React.ReactNode;
}

interface FAQAccordionProps {
  items: FAQItem[];
}

export const FAQAccordion: React.FC<FAQAccordionProps> = ({ items }) => {
  const [openIndex, setOpenIndex] = useState<number | null>(null);

  const toggleItem = (index: number) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  return (
    <div className={styles.accordionContainer}>
      {items.map((item, index) => {
        const isOpen = openIndex === index;
        return (
          <div key={index} className={styles.accordionItem}>
            <button
              className={styles.accordionHeader}
              onClick={() => toggleItem(index)}
              aria-expanded={isOpen}
            >
              <span>{item.question}</span>
              <ChevronDown
                className={`${styles.icon} ${isOpen ? styles.iconOpen : ""}`}
                size={24}
              />
            </button>
            <div
              className={`${styles.accordionContent} ${
                isOpen ? styles.accordionContentOpen : ""
              }`}
            >
              <div className={styles.accordionContentInner}>
                <div className={styles.accordionText}>{item.answer}</div>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
};
