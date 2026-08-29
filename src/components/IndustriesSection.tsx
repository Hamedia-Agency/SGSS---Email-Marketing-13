'use client';

import React from 'react';
import Link from 'next/link';
import styles from './IndustriesSection.module.css';
import { 
  HardHat, 
  Warehouse, 
  Building2, 
  Store, 
  Home, 
  Truck, 
  Hospital, 
  GraduationCap, 
  Landmark,
  ArrowRight
} from 'lucide-react';

const industries = [
  { name: 'Construction & Job Sites', icon: HardHat, link: 'https://www.secureguardservices.com/industries/construction-security-services-california' },
  { name: 'Warehouses & Industrial Facilities', icon: Warehouse, link: 'https://www.secureguardservices.com/industries/storage-facility-security-services-california' },
  { name: 'Commercial Properties & Office Buildings', icon: Building2, link: 'https://www.secureguardservices.com/industries/high-rise-security-services-california' },
  { name: 'Retail Centers & Shopping Properties', icon: Store, link: 'https://www.secureguardservices.com/industries/shopping-center-security-services-california' },
  { name: 'Multi-Family & Residential Communities', icon: Home, link: 'https://www.secureguardservices.com/industries/homeowner-association-security-services-california' },
  { name: 'Industrial Yards & Outdoor Properties', icon: Truck, link: 'https://www.secureguardservices.com/industries/transportation-logistic-facility-security-services-california' },
  { name: 'Healthcare & Medical Facilities', icon: Hospital, link: 'https://www.secureguardservices.com/industries/healthcare-facility-security-services-california' },
  { name: 'Educational & Institutional Properties', icon: GraduationCap, link: 'https://www.secureguardservices.com/industries/educational-institute-security-services-california' },
  { name: 'Government & Public-Sector Properties', icon: Landmark, link: 'https://www.secureguardservices.com/industries/government-facility-security-services-california' }
];

export default function IndustriesSection() {
  return (
    <section className={styles.section} id="industries">
      <div className="container">
        <div className={styles.sectionHeaderCentered}>
          <span className={styles.sectionTag}>Industries We Serve</span>
          <h2 className={styles.sectionTitle}>
            Security Solutions Built Around Different Industries
          </h2>
        </div>
        
        <div className={styles.grid}>
          {industries.map((industry, index) => (
            <Link href={industry.link} key={index} className={styles.card}>
              <div className={styles.iconWrapper}>
                <industry.icon size={28} strokeWidth={1.5} />
              </div>
              <div className={styles.cardContent}>
                <h3 className={styles.cardTitle}>{industry.name}</h3>
              </div>
              <ArrowRight className={styles.arrowIcon} size={20} strokeWidth={2} />
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
}
