import os

page_content = """\"use client\";

import React, { useState } from \"react\";
import Image from \"next/image\";
import styles from \"./page.module.css\";
import { Navbar } from \"@/components/Navbar\";
import { Footer } from \"@/components/Footer\";
import BackToTop from \"@/components/BackToTop\";
import { PreFooterCTA } from \"@/components/PreFooterCTA\";
import { LeadGenForm } from \"@/components/LeadGenForm\";
import { LeadGenModal } from \"@/components/LeadGenModal\";
import { ProcessExplorer } from \"@/components/ProcessExplorer\";
import { CarouselSection } from \"@/components/CarouselSection\";
import { CoverageSection } from \"@/components/CoverageSection\";
import { FAQAccordion } from \"@/components/FAQAccordion\";
import { 
  ShieldCheck, 
  MapPin, 
  FileText, 
  Camera, 
  FileSpreadsheet, 
  CheckCircle, 
  Eye, 
  AlertCircle, 
  UserCheck, 
  Headphones, 
  TrendingUp, 
  ArrowRight,
  Shield,
  FileCheck,
  BellRing,
  Clock,
  BookOpen,
  Lock,
  Key,
  Users,
  Activity
} from \"lucide-react\";

export default function HomePage() {
  const [modalOpen, setModalOpen] = useState(false);
  const [modalTitle, setModalTitle] = useState(\"Schedule Your Free Security Consultation\");

  const handleOpenConsultation = (title?: string) => {
    if (title) setModalTitle(title);
    else setModalTitle(\"Schedule Your Free Security Consultation\");
    setModalOpen(true);
  };

  const faqs = [
    {
      question: \"How does Secure Guard determine the right security combination for my industry and property?\",
      answer: \"We evaluate your property layout, operating schedules, traffic flow, and historical security risks. Rather than applying a standard template, we select a tailored mix of guards, mobile patrols, and monitoring technology designed specifically around how your facility operates.\"
    },
    {
      question: \"Does every property require a full-time, on-site security officer?\",
      answer: \"No. Some properties require a continuous visible presence, while others are effectively protected through mobile patrols, solar surveillance towers, live remote video monitoring, or a hybrid strategy. We align our services with your actual operational risks rather than forcing full-time guard posts.\"
    },
    {
      question: \"Can multiple security services be combined, and do you work with existing camera systems?\",
      answer: \"Yes. We frequently integrate standing officers, mobile patrols, and live monitoring to create multi-layered coverage. We can also evaluate your existing camera infrastructure and incorporate those feeds into our SecureTrack operational network to avoid unnecessary hardware replacement costs.\"
    },
    {
      question: \"How do standing guards and remote video monitoring work together on site?\",
      answer: \"Remote video monitoring provides continuous visual oversight across large perimeters and outdoor blind spots, while standing guards and mobile patrol officers manage access gates, conduct physical door inspections, and deliver rapid face-to-face response when an alert is flagged.\"
    },
    {
      question: \"Can our security service plan scale as our operational needs change?\",
      answer: \"Yes. Our plans are fully flexible. You can increase guard hours during peak operational periods, scale back during slower seasons, adapt coverage as construction projects transition into occupied buildings, or deploy short-term temporary protection for short projects.\"
    },
    {
      question: \"Does Secure Guard support large properties, multi-building campuses, and expansive outdoor yards?\",
      answer: \"Yes. We protect large industrial facilities, commercial plazas, residential communities, and hard-to-wire equipment yards by combining mobile field patrols, solar-powered surveillance towers, and centralized dispatch coordination.\"
    },
    {
      question: \"What geographic regions does Secure Guard serve?\",
      answer: \"Secure Guard provides professional, industry-tailored security services to commercial, industrial, and residential properties throughout Southern and Northern California.\"
    },
    {
      question: \"Is an industry-specific security assessment available before committing?\",
      answer: \"Yes. Secure Guard offers initial site evaluations to review your current setup, pinpoint industry-specific vulnerabilities, and outline how your security coverage can be optimized with zero obligation.\"
    }
  ];

  return (
    <main className={styles.main}>
      {/* ===== NAVBAR ===== */}
      <Navbar onOpenConsultation={() => handleOpenConsultation()} />

      {/* ===== HERO SECTION ===== */}
      <section className={styles.hero}>
        <div className={styles.heroBg}>
          <Image
            src=\"https://cms.secureguardservices.com/wp-content/uploads/2026/08/diffguards.webp\"
            alt=\"Industry-Tailored Security Solutions\"
            fill
            className={styles.heroBgImg}
            priority
            quality={90}
          />
          <div className={styles.heroOverlay} />
        </div>
        <div className={`container ${styles.heroWrapper}`}>
          <div className={styles.heroContent}>
            <div className={styles.heroBadge}>
              Customized Coverage
            </div>
            <h1 className={styles.heroTitle}>
              <span className={styles.heroTitleAccent}>Industry-Tailored</span> <br /> Security Solutions
            </h1>
            <p className={styles.heroSubtitle}>
              Secure Guard replaces generic security with custom coverage built around your site’s exact layout, operating hours, and risks. From construction sites to retail centers, we combine live monitoring, mobile patrols, and standing guards into a response network tailored to how your property actually operates.
            </p>
            <a 
              href=\"#\"
              onClick={(e) => { e.preventDefault(); handleOpenConsultation(); }}
              className={styles.btnPrimary}
            >
              See How We Protect Your Industry
            </a>
          </div>
        </div>
        <div className={styles.heroScroll} aria-hidden=\"true\">
          <span className={styles.heroScrollDot} />
        </div>
      </section>

      {/* ===== SECTION 1: WHY CHOOSE SECURE GUARD? ===== */}
      <section className={styles.section} id=\"why-choose-us\">
        <div className=\"container\">
          <div className={styles.splitGrid}>
            <div className={styles.splitContent}>
              <span className={styles.sectionTag}>Why Choose Us</span>
              <h2 className={styles.sectionTitle}>
                Why Choose Secure Guard?
              </h2>
              <p className={styles.bodyText}>
                Secure Guard builds industry-specific security around your actual property layout rather than forcing a standard template. Every location receives clear, site-specific procedures that guide guards on patrol routes, access controls, emergency contacts, and escalation steps. Through SecureTrack, on-site guards, field supervisors, 24/7 dispatchers, and camera systems operate as one connected network across Southern and Northern California.
              </p>
              <p className={styles.bodyText}>
                Because business needs change over time, our coverage remains fully flexible. We evaluate and adjust your security setup as site conditions, operating hours, and property risks evolve, ensuring seamless protection for single locations or multi-property portfolios.
              </p>
            </div>
            <div className={styles.splitImageWrapper}>
              <Image 
                src=\"https://cms.secureguardservices.com/wp-content/uploads/2026/08/cliepor.png\" 
                alt=\"Industry-Specific Security\" 
                fill
                className={styles.splitImage}
              />
            </div>
          </div>

          {/* ===== SECTION 2: WHAT MAKES EVERY PROPERTY DIFFERENT? ===== */}
          <div style={{ marginTop: \"80px\" }}>
            <div className={styles.sectionHeaderCentered} style={{ marginBottom: \"40px\" }}>
              <h2 className={styles.sectionTitle}>What Makes Every Property Different?</h2>
            </div>
            <div className={styles.cardsGridFive}>
              <div className={styles.featureCard} style={{ display: \"flex\", flexDirection: \"column\", alignItems: \"center\", textAlign: \"center\", padding: \"30px 20px\" }}>
                <div className={styles.featureCardIcon} style={{ width: \"56px\", height: \"56px\", marginBottom: \"16px\" }}>
                  <Lock size={28} />
                </div>
                <h3 className={styles.featureTitle} style={{ marginBottom: \"10px\", fontSize: \"1.15rem\" }}>Access Points</h3>
                <p className={styles.featureDesc} style={{ fontSize: \"0.95rem\" }}>
                  Every property features distinct entry and exit dynamics. Secure Guard implements precise oversight—including credential verification, visitor screening, and gate management—ensuring restricted areas stay protected.
                </p>
              </div>

              <div className={styles.featureCard} style={{ display: \"flex\", flexDirection: \"column\", alignItems: \"center\", textAlign: \"center\", padding: \"30px 20px\" }}>
                <div className={styles.featureCardIcon} style={{ width: \"56px\", height: \"56px\", marginBottom: \"16px\" }}>
                  <Clock size={28} />
                </div>
                <h3 className={styles.featureTitle} style={{ marginBottom: \"10px\", fontSize: \"1.15rem\" }}>Operating Hours</h3>
                <p className={styles.featureDesc} style={{ fontSize: \"0.95rem\" }}>
                  Security risks shift dynamically. We structure deployments around a site's specific operational schedule, scaling guard presence and access controls to match high-traffic windows and vacant after-hours.
                </p>
              </div>

              <div className={styles.featureCard} style={{ display: \"flex\", flexDirection: \"column\", alignItems: \"center\", textAlign: \"center\", padding: \"30px 20px\" }}>
                <div className={styles.featureCardIcon} style={{ width: \"56px\", height: \"56px\", marginBottom: \"16px\" }}>
                  <Activity size={28} />
                </div>
                <h3 className={styles.featureTitle} style={{ marginBottom: \"10px\", fontSize: \"1.15rem\" }}>Activity Patterns</h3>
                <p className={styles.featureDesc} style={{ fontSize: \"0.95rem\" }}>
                  Vulnerabilities fluctuate alongside routine site operations. Secure Guard analyzes recurring rhythms to strategically position personnel, mobile patrols, and technology where activity and potential risks peak.
                </p>
              </div>

              <div className={styles.featureCard} style={{ display: \"flex\", flexDirection: \"column\", alignItems: \"center\", textAlign: \"center\", padding: \"30px 20px\" }}>
                <div className={styles.featureCardIcon} style={{ width: \"56px\", height: \"56px\", marginBottom: \"16px\" }}>
                  <ShieldCheck size={28} />
                </div>
                <h3 className={styles.featureTitle} style={{ marginBottom: \"10px\", fontSize: \"1.15rem\" }}>Response Requirements</h3>
                <p className={styles.featureDesc} style={{ fontSize: \"0.95rem\" }}>
                  Specific operational goals dictate whether a property requires passive deterrence, rapid field deployment, or active remote intervention. Secure Guard aligns response protocols directly with site needs.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ===== SECTION 3: CAROUSEL (Secure Guard Services) ===== */}
      <section className={`${styles.section} ${styles.carouselSectionWithBg}`} id=\"services\">
        <div className=\"container\">
          <div className={styles.sectionHeaderCentered} style={{ marginBottom: \"40px\" }}>
            <span className={styles.sectionTag}>Our Offerings</span>
            <h2 className={styles.sectionTitle}>
              Secure Guard Services
            </h2>
          </div>
          <CarouselSection 
            autoplay={true}
            items={[
              {
                title: \"Security Officers\",
                tag: \"PHYSICAL PRESENCE\",
                description: (
                  <p>
                    Provide a strong physical presence on your property to deter threats before they happen. Depending on your site’s specific needs, officers manage access points, conduct foot patrols, monitor daily activity, assist during emergencies, and document all on-site incidents in real time.
                  </p>
                ),
                image: \"https://cms.secureguardservices.com/wp-content/uploads/2026/08/diffguards.webp\"
              },
              {
                title: \"Mobile Patrol\",
                tag: \"RAPID RESPONSE\",
                description: (
                  <p>
                    Extends physical protection across larger properties or locations that don't require a full-time standing guard. Patrol personnel perform scheduled or randomized vehicle sweeps, check secured access points, investigate suspicious activity, and provide rapid, visible field response.
                  </p>
                ),
                image: \"https://cms.secureguardservices.com/wp-content/uploads/2026/08/increp.webp\"
              },
              {
                title: \"Video Monitoring\",
                tag: \"CONTINUOUS OVERSIGHT\",
                description: (
                  <p>
                    This gives you continuous, real-time visibility across designated areas of your property. Instead of relying on recorded footage after damage or theft has already occurred, suspicious activity is actively monitored and evaluated while it is happening.
                  </p>
                ),
                image: \"https://cms.secureguardservices.com/wp-content/uploads/2026/08/checkpoint.webp\"
              },
              {
                title: \"Mobile Surveillance Towers\",
                tag: \"OFF-GRID SECURITY\",
                description: (
                  <p>
                    Engineered for large, open, temporary, or off-grid sites, mobile surveillance towers deliver elevated camera coverage, thermal night vision, live voice-down audio intervention, and remote monitoring without requiring on-site wiring or infrastructure.
                  </p>
                ),
                image: \"https://cms.secureguardservices.com/wp-content/uploads/2026/08/clearpostord.webp\"
              },
              {
                title: \"Central Dispatch\",
                tag: \"OPERATIONAL BRIDGE\",
                description: (
                  <p>
                    This serves as the active operational bridge between live monitoring networks and field personnel. Whenever a situation requires immediate backup, dispatch coordinates seamlessly with on-site guards, mobile patrol units, field supervisors, property contacts, and local authorities.
                  </p>
                ),
                image: \"https://cms.secureguardservices.com/wp-content/uploads/2026/08/whysecgu.webp\"
              }
            ]} 
          />
        </div>
      </section>

      {/* ===== SECTION 4: PROCESS EXPLORER (How Secure Guard Builds Your Security Plan) ===== */}
      <section className={styles.section} id=\"build-plan\">
        <div className=\"container\">
          <div className={styles.sectionHeaderCentered} style={{ marginBottom: \"56px\" }}>
            <span className={styles.sectionTag}>The Process</span>
            <h2 className={styles.sectionTitle}>
              How Secure Guard Builds Your Security Plan
            </h2>
          </div>
          
          <ProcessExplorer />
        </div>
      </section>

      {/* ===== SECTION 5: SECURETRACK & COMBINATION OF SERVICES ===== */}
      <section className={styles.section} id=\"securetrack-ecosystem\">
        <div className=\"container\">
          <div className={styles.splitGrid} style={{ alignItems: \"center\" }}>
            <div className={styles.splitImageWrapper} style={{ height: \"100%\", minHeight: \"400px\" }}>
              <Image 
                src=\"https://cms.secureguardservices.com/wp-content/uploads/2026/08/cliepor.png\" 
                alt=\"SecureTrack Ecosystem\" 
                fill
                className={styles.splitImage}
              />
            </div>
            <div className={styles.splitContent}>
              <h2 className={styles.sectionTitle}>
                SecureTrack
              </h2>
              <p className={styles.bodyText}>
                Secure Guard’s all-in-one management platform that links on-site guards, supervisors, 24/7 dispatchers, camera technology, and digital reporting into a single connected system. Whether verifying patrol rounds on a construction site, tracking entry logs at a warehouse, or recording incident reports in a residential community, SecureTrack gives you total visibility into your security operations. Rather than replacing trained personnel, this technology empowers our officers, dispatchers, and field supervisors to work together seamlessly while giving you clear, real-time proof of protection.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section className={`${styles.section} ${styles.sectionDark}`} id=\"combination\">
        <div className=\"container\">
          <div className={styles.splitGrid} style={{ alignItems: \"center\" }}>
            <div className={styles.splitContent}>
              <h2 className={`${styles.sectionTitle} ${styles.sectionTitleDark}`}>
                Combination of Services
              </h2>
              <p className={`${styles.bodyText} ${styles.bodyTextDark}`}>
                Combining security services turns individual protective measures into a unified, multi-layered defense network tailored to your property's exact layout and risk profile. Because different zones of a property carry distinct vulnerabilities across operating hours, blending physical coverage, remote technology, and centralized coordination ensures that every operational gap is covered without paying for unnecessary redundancy. 
              </p>
              <p className={`${styles.bodyText} ${styles.bodyTextDark}`} style={{ marginTop: \"16px\" }}>
                Guided by your site vulnerability audit, you retain total control over the exact mix of services you deploy, knowing that every layer connects seamlessly to share real-time data, coordinate rapid response, and deliver complete operational transparency across your entire site.
              </p>
            </div>
            <div className={`${styles.splitImageWrapper} ${styles.orderFirstMobile}`} style={{ height: \"100%\", minHeight: \"400px\" }}>
              <Image 
                src=\"https://cms.secureguardservices.com/wp-content/uploads/2026/08/whysecgu.webp\" 
                alt=\"Unified Management Ecosystem\" 
                fill
                className={styles.splitImage}
              />
            </div>
          </div>
        </div>
      </section>

      {/* ===== SECTION 6: INDUSTRIES ===== */}
      <section className={styles.section} id=\"industries\">
        <div className=\"container\">
          <div className={styles.sectionHeaderCentered} style={{ marginBottom: \"56px\" }}>
            <span className={styles.sectionTag}>Industries We Serve</span>
            <h2 className={styles.sectionTitle}>
              Security Solutions Built Around Different Industries
            </h2>
          </div>
          <div style={{ display: \"flex\", flexWrap: \"wrap\", gap: \"12px\", justifyContent: \"center\" }}>
            {[
              \"Construction & Job Sites\",
              \"Warehouses & Industrial Facilities\",
              \"Commercial Properties & Office Buildings\",
              \"Retail Centers & Shopping Properties\",
              \"Multi-Family & Residential Communities\",
              \"Industrial Yards & Outdoor Properties\",
              \"Healthcare & Medical Facilities\",
              \"Educational & Institutional Properties\",
              \"Government & Public-Sector Properties\"
            ].map((industry, index) => (
              <span key={index} style={{ padding: \"12px 24px\", background: \"#f1f5f9\", color: \"#0f172a\", borderRadius: \"8px\", fontWeight: \"600\", fontSize: \"1rem\" }}>
                {industry}
              </span>
            ))}
          </div>
        </div>
      </section>

      {/* ===== SECTION 7: COVERAGE ===== */}
      <CoverageSection />

      {/* ===== SECTION 8: FAQ ACCORDION ===== */}
      <section className={`${styles.section} ${styles.faqSection}`} id=\"faq\">
        <div className=\"container\">
          <div className={styles.sectionHeaderCentered} style={{ marginBottom: \"56px\" }}>
            <span className={styles.sectionTag}>Questions & Answers</span>
            <h2 className={styles.sectionTitle}>
              Frequently Asked Questions (FAQ)
            </h2>
          </div>
          <FAQAccordion items={faqs} />
        </div>
      </section>

      {/* ===== PRE-FOOTER CTA ===== */}
      <PreFooterCTA />

      {/* ===== FOOTER ===== */}
      <Footer />

      {/* ===== LEAD GENERATION MODAL ===== */}
      <LeadGenModal
        isOpen={modalOpen}
        onClose={() => setModalOpen(false)}
        title={modalTitle}
      />

      {/* ===== BACK TO TOP ===== */}
      <BackToTop />
    </main>
  );
}
"""

process_content = """\"use client\";

import React, { useState } from \"react\";
import { 
  Eye,
  Clock,
  AlertCircle,
  ShieldCheck,
  FileText,
  TrendingUp
} from \"lucide-react\";
import styles from \"./ProcessExplorer.module.css\";

const processItems = [
  {
    title: \"Evaluate the Property\",
    shortTitle: \"Evaluate Property\",
    description: \"Secure Guard inspects your physical layout, entry points, parking areas, lighting, and blind spots to map out where protection is needed most.\",
    icon: Eye,
    label: \"Step 1\"
  },
  {
    title: \"Understand Daily Operations\",
    shortTitle: \"Daily Operations\",
    description: \"Review operating hours, worker shifts, delivery schedules, and visitor traffic to design security that fits smoothly into your daily routine.\",
    icon: Clock,
    label: \"Step 2\"
  },
  {
    title: \"Identify Vulnerabilities\",
    shortTitle: \"Identify Vulnerabilities\",
    description: \"Analyze past incidents and site concerns to pinpoint exact risks, focusing resources where trespassing, theft, or damage are most likely.\",
    icon: AlertCircle,
    label: \"Step 3\"
  },
  {
    title: \"Match Services to the Property\",
    shortTitle: \"Match Services\",
    description: \"Build a tailored security mix for your site—combining standing guards, mobile patrols, solar camera towers, and live monitoring linked by SecureTrack.\",
    icon: ShieldCheck,
    label: \"Step 4\"
  },
  {
    title: \"Build Site-Specific Procedures\",
    shortTitle: \"Site Procedures\",
    description: \"Document clear Post Orders for your property, establishing exact rules for patrol routes, visitor check-ins, emergencies, and escalations.\",
    icon: FileText,
    label: \"Step 5\"
  },
  {
    title: \"Continue Evaluating the Program\",
    shortTitle: \"Evaluate Program\",
    description: \"As your business grows, hours shift, or layout changes, Secure Guard continuously reviews and adjusts your coverage so your protection never falls behind.\",
    icon: TrendingUp,
    label: \"Step 6\"
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
              className={`${styles.tabButton} ${activeTab === index ? styles.activeTabButton : \"\"}`}
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
"""

with open(r"c:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-13\src\app\page.tsx", "w", encoding="utf-8") as f:
    f.write(page_content)

with open(r"c:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-13\src\components\ProcessExplorer.tsx", "w", encoding="utf-8") as f:
    f.write(process_content)

print("Files generated successfully!")
