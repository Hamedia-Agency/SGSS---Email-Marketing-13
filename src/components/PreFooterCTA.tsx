"use client";

import React from "react";
import styles from "./PreFooterCTA.module.css";
import { LeadGenForm } from "./LeadGenForm";

export function PreFooterCTA() {
  return (
    <section id="free-assessment" className={styles.eyjiCtaSection}>
      <div className={styles.eyjiCtaInner}>
        <div className={styles.eyjiCtaPanel}>
          {/* Left content */}
          <div className={styles.eyjiCtaCopy}>
            <div className={styles.eyjiCtaKicker}>
              <div className={styles.eyjiCtaKickerText}>Free Security Assessment</div>
              <span className={styles.eyjiCtaKickerBullet}></span>
            </div>

            <h2 className={styles.eyjiCtaTitle}>
              Ready for a Security Plan Built Around Your Property?
            </h2>

            <p className={styles.eyjiCtaText}>
              Every site has its own layout, operating hours, access points, and risks—and your security coverage should reflect that. Fill out the quick form or reach out directly to explore how we can better protect your property with zero obligation.
            </p>

            {/* CONTACT INFO */}
            <div className={styles.eyjiCtaContacts}>
              <div className={styles.eyjiCtaContactItem}>
                <span className={styles.eyjiCtaContactIcon} aria-hidden="true">
                  <svg viewBox="0 0 24 24">
                    <path d="M7 4.5l2.5-1.5 2 3-1.6 1a10 10 0 0 0 4.6 4.6l1-1.6 3 2-1.5 2.5a2 2 0 0 1-2 1c-7 0-11-4-11-11a2 2 0 0 1 1-2z"></path>
                  </svg>
                </span>
                <span className={styles.eyjiCtaContactLabel}>Call</span>
                <span className={styles.eyjiCtaContactValue}>
                  <a href="tel:18889087818">888-908-7818</a>
                </span>
              </div>

              <div className={styles.eyjiCtaContactItem}>
                <span className={styles.eyjiCtaContactIcon} aria-hidden="true">
                  <svg viewBox="0 0 24 24">
                    <rect x="3.5" y="5.5" width="17" height="13" rx="1.5"></rect>
                    <path d="M4.5 7l7.5 5 7.5-5"></path>
                  </svg>
                </span>
                <span className={styles.eyjiCtaContactLabel}>Email</span>
                <span className={styles.eyjiCtaContactValue}>
                  <a href="mailto:info@secureguardservices.com">info@secureguardservices.com</a>
                </span>
              </div>

              <div className={styles.eyjiCtaContactItem}>
                <span className={styles.eyjiCtaContactIcon} aria-hidden="true">
                  <svg viewBox="0 0 24 24">
                    <path d="M12 21s-6-6.2-6-10.2A6 6 0 0 1 18 10.8C18 14.8 12 21 12 21z"></path>
                    <circle cx="12" cy="10" r="2.3"></circle>
                  </svg>
                </span>
                <span className={styles.eyjiCtaContactLabel}>Office</span>
                <span className={styles.eyjiCtaContactValue}>
                  18001 Sky Park Circle J, Irvine, CA 92614
                </span>
              </div>
            </div>

            <div className={styles.eyjiCtaBadge}>
              <span></span>
              <div>Serving clients across California since 2005</div>
            </div>
          </div>

          {/* Right form (Mandatory Component) */}
          <div className={styles.eyjiCtaFormWrap}>
            <LeadGenForm hideHeader={true} variant="dark" buttonText="Request a Security Consultation" />
          </div>
        </div>
      </div>
    </section>
  );
}

export default PreFooterCTA;
