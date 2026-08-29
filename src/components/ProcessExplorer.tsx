"use client";

import React, { useState } from "react";
import { 
  Eye,
  Clock,
  AlertCircle,
  ShieldCheck,
  FileText,
  TrendingUp
} from "lucide-react";
import styles from "./ProcessExplorer.module.css";

const processItems = [
  {
    title: "Evaluate the Property",
    shortTitle: "Evaluate Property",
    description: "Secure Guard inspects your physical layout, entry points, parking areas, lighting, and blind spots to map out where protection is needed most.",
    icon: Eye,
    label: "Step 1"
  },
  {
    title: "Understand Daily Operations",
    shortTitle: "Daily Operations",
    description: "Review operating hours, worker shifts, delivery schedules, and visitor traffic to design security that fits smoothly into your daily routine.",
    icon: Clock,
    label: "Step 2"
  },
  {
    title: "Identify Vulnerabilities",
    shortTitle: "Identify Vulnerabilities",
    description: "Analyze past incidents and site concerns to pinpoint exact risks, focusing resources where trespassing, theft, or damage are most likely.",
    icon: AlertCircle,
    label: "Step 3"
  },
  {
    title: "Match Services to the Property",
    shortTitle: "Match Services",
    description: "Build a tailored security mix for your site—combining standing guards, mobile patrols, solar camera towers, and live monitoring linked by SecureTrack.",
    icon: ShieldCheck,
    label: "Step 4"
  },
  {
    title: "Build Site-Specific Procedures",
    shortTitle: "Site Procedures",
    description: "Document clear Post Orders for your property, establishing exact rules for patrol routes, visitor check-ins, emergencies, and escalations.",
    icon: FileText,
    label: "Step 5"
  },
  {
    title: "Continue Evaluating the Program",
    shortTitle: "Evaluate Program",
    description: "As your business grows, hours shift, or layout changes, Secure Guard continuously reviews and adjusts your coverage so your protection never falls behind.",
    icon: TrendingUp,
    label: "Step 6"
  }
];

export function ProcessExplorer() {
  const [activeTab, setActiveTab] = useState(0);
  const activeItem = processItems[activeTab];
  const IconComponent = activeItem.icon;

  return (
    <div className={styles.explorerContainer}>
      {/* Left Column: Navigation Tabs */}
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

      {/* Right Column: Display Card */}
      <div className={styles.displayCard} key={activeTab}>
        <div className={styles.cardHeader}>
          <span className={styles.cardTag}>{activeItem.label}</span>
          <h3 className={styles.cardTitle}>{activeItem.title}</h3>
          <p className={styles.cardDescription}>{activeItem.description}</p>
        </div>

        {/* Visual Mockup Side */}
        <div className={styles.visualWrapper}>
          <div className={styles.glowOrb} />
          <div className={styles.illustrationCard}>
            <IconComponent size={64} className={styles.visualIcon} />
            <span className={styles.visualLabel}>{activeItem.label}</span>
          </div>
        </div>
      </div>
    </div>
  );
}
