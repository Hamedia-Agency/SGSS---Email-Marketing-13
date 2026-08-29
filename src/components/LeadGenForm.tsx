"use client";

import React, { useState } from "react";
import Link from "next/link";
import styles from "./LeadGenForm.module.css";
import { Shield, CheckCircle, Send } from "lucide-react";

interface LeadGenFormProps {
  hideHeader?: boolean;
  className?: string;
  title?: string;
  subtitle?: string;
  buttonText?: string;
  variant?: "light" | "dark";
}

export function LeadGenForm({
  hideHeader = false,
  className = "",
  title = "Find Out Where Your Property May Be Exposed",
  subtitle = "Tell us a little about your property and current concerns. A member of our team will contact you with a customized security review.",
  buttonText = "Schedule Your Free Security Consultation",
  variant = "light",
}: LeadGenFormProps) {
  const [formData, setFormData] = useState({
    name: "",
    companyName: "",
    email: "",
    phone: "",
    propertyType: "",
    city: "",
    concern: "",
    agreed: false,
  });

  const [submitted, setSubmitted] = useState(false);

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
  ) => {
    const { name, value, type } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? (e.target as HTMLInputElement).checked : value,
    }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("SecureTrack Lead Form Submitted:", formData);
    setSubmitted(true);
  };

  if (submitted) {
    return (
      <div className={`${styles.successCard} ${className}`}>
        <div className={styles.successIconCircle}>
          <CheckCircle size={36} />
        </div>
        <h3 className={styles.successTitle}>Request Received!</h3>
        <p className={styles.successDesc}>
          Thank you, <strong>{formData.name}</strong>. Our security operations team has received your information for <strong>{formData.companyName || "your property"}</strong>. We will reach out shortly to schedule your live SecureTrack consultation.
        </p>
        <button
          onClick={() => setSubmitted(false)}
          className={styles.resetBtn}
        >
          Submit Another Request
        </button>
      </div>
    );
  }

  const isDark = variant === "dark";

  return (
    <div className={`${isDark ? styles.formCardDark : styles.formCard} ${className}`}>
      {!hideHeader && (
        <div className={styles.headerArea}>
          <div className={styles.badge}>
            <Shield size={14} className={styles.badgeIcon} />
            Risk Assessment
          </div>
          <h2 className={styles.title}>
            {title}
          </h2>
          <div className={styles.divider} />
          <p className={styles.subtitle}>
            {subtitle}
          </p>
        </div>
      )}

      <form onSubmit={handleSubmit} className={styles.form}>
        {/* Row 1: Name & Company */}
        <div className={styles.row2Col}>
          <div className={styles.fieldGroup}>
            <label className={isDark ? styles.labelDark : styles.label}>
              Full Name *
            </label>
            <input
              type="text"
              name="name"
              placeholder="e.g. John Doe"
              required
              value={formData.name}
              onChange={handleChange}
              className={isDark ? styles.inputDark : styles.input}
            />
          </div>
          <div className={styles.fieldGroup}>
            <label className={isDark ? styles.labelDark : styles.label}>
              Company / Property Name *
            </label>
            <input
              type="text"
              name="companyName"
              placeholder="e.g. Apex Commercial Plaza"
              required
              value={formData.companyName}
              onChange={handleChange}
              className={isDark ? styles.inputDark : styles.input}
            />
          </div>
        </div>

        {/* Row 2: Email & Phone */}
        <div className={styles.row2Col}>
          <div className={styles.fieldGroup}>
            <label className={isDark ? styles.labelDark : styles.label}>
              Business Email *
            </label>
            <input
              type="email"
              name="email"
              placeholder="name@company.com"
              required
              value={formData.email}
              onChange={handleChange}
              className={isDark ? styles.inputDark : styles.input}
            />
          </div>
          <div className={styles.fieldGroup}>
            <label className={isDark ? styles.labelDark : styles.label}>
              Phone Number *
            </label>
            <input
              type="tel"
              name="phone"
              placeholder="(555) 000-0000"
              required
              value={formData.phone}
              onChange={handleChange}
              className={isDark ? styles.inputDark : styles.input}
            />
          </div>
        </div>

        {/* Row 3: Property Type & City */}
        <div className={styles.row2Col}>
          <div className={styles.fieldGroup}>
            <label className={isDark ? styles.labelDark : styles.label}>
              Property Type
            </label>
            <select
              name="propertyType"
              value={formData.propertyType}
              onChange={handleChange}
              className={isDark ? styles.selectDark : styles.select}
            >
              <option value="">Select Property Type...</option>
              <option value="Commercial Office / Plaza">Commercial Office / Plaza</option>
              <option value="Construction Site">Construction Site</option>
              <option value="Retail & Shopping Center">Retail & Shopping Center</option>
              <option value="Industrial / Warehouse">Industrial / Warehouse</option>
              <option value="Residential HOA / Apartment">Residential HOA / Apartment</option>
              <option value="Other">Other Property</option>
            </select>
          </div>
          <div className={styles.fieldGroup}>
            <label className={isDark ? styles.labelDark : styles.label}>
              City / Location
            </label>
            <input
              type="text"
              name="city"
              placeholder="e.g. Los Angeles, Irvine, San Diego"
              value={formData.city}
              onChange={handleChange}
              className={isDark ? styles.inputDark : styles.input}
            />
          </div>
        </div>

        {/* Row 4: Concern */}
        <div className={styles.fieldGroup}>
          <label className={isDark ? styles.labelDark : styles.label}>
            Current Security Concern or Objectives
          </label>
          <textarea
            name="concern"
            placeholder="Tell us about your property's security challenges or questions regarding SecureTrack technology..."
            rows={3}
            value={formData.concern}
            onChange={handleChange}
            className={isDark ? styles.textareaDark : styles.textarea}
          ></textarea>
        </div>

        {/* Row 5: Terms */}
        <div className={styles.termsGroup}>
          <input
            type="checkbox"
            name="agreed"
            id="agreed"
            required
            checked={formData.agreed}
            onChange={handleChange}
            className={styles.checkbox}
          />
          <label htmlFor="agreed" className={isDark ? styles.termsTextDark : styles.termsText}>
            I agree to the <Link href="#privacy" className={isDark ? styles.privacyLinkDark : styles.privacyLink}>privacy terms</Link>. By submitting, I authorize SGSS to contact me regarding security services and field visibility solutions.
          </label>
        </div>

        {/* Row 6: Submit Button */}
        <button
          type="submit"
          className={styles.submitBtn}
        >
          <Send size={18} />
          {buttonText}
        </button>
      </form>
    </div>
  );
}

export default LeadGenForm;
