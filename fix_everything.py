import os
import re

page_path = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12\src\app\page.tsx"
with open(page_path, "r", encoding="utf-8") as f:
    content = f.read()

replacement = """      {/* ===== SECTION 2: Camera Alert Is Only the Beginning ===== */}
      <section className={styles.section} id="vulnerability">
        <div className="container">
          <div className={styles.addonGrid}>
            <div className={styles.addonImageCol}>
              <Image 
                src="https://cms.secureguardservices.com/wp-content/uploads/2026/08/em8-2.webp" 
                alt="Connected Security Network" 
                width={500} 
                height={400} 
                className={styles.addonImage} 
                style={{ borderRadius: "12px", objectFit: "cover" }}
              />
            </div>
            <div className={styles.addonContent}>
              <div className={styles.sectionHeader} style={{ margin: "0", textAlign: "left" }}>
                <span className={styles.sectionTag}>Complete Incident Control</span>
                <h2 className={styles.sectionTitle} style={{ marginBottom: "16px" }}>
                  Camera Alert Is Only the Beginning
                </h2>
              </div>
              <p className={styles.bodyText}>
                Secure Guard’s hybrid security model bridges the gap between technology and physical security by managing the complete incident sequence for you.
              </p>
              <p className={styles.bodyText}>
                Instead of leaving property managers to determine next steps after an alert, our connected system automatically flags off-hours activity in high-vulnerability zones, verifies live footage in seconds to eliminate false alarms, and immediately executes your custom response protocols—whether that means issuing live voice warnings, dispatching mobile field patrols, or coordinating directly with local law enforcement.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ===== SECTION 3: How Hybrid Security Works (Glass & Navy) ===== */}
      <section className={`${styles.section} ${styles.sectionDark}`} id="how-it-works" style={{ position: 'relative', overflow: 'hidden' }}>
        {/* Navy Blue Filtered Background Image */}
        <div style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', zIndex: 0 }}>
          <Image 
            src="https://cms.secureguardservices.com/wp-content/uploads/2026/08/em8-2.webp" 
            alt="Security Background" 
            fill 
            style={{ objectFit: 'cover' }} 
            quality={80}
          />
          <div style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', background: 'rgba(10, 25, 47, 0.88)' }} />
        </div>

        <div className="container" style={{ position: 'relative', zIndex: 1 }}>
          <div className={styles.sectionHeader} style={{ marginBottom: '48px', display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', width: '100%', maxWidth: '100%' }}>
            <span className={styles.sectionTag} style={{ color: "#b89000", background: "rgba(254, 207, 49, 0.13)", borderColor: "rgba(254, 207, 49, 0.35)" }}>Unified Incident Response</span>
            <h2 className={styles.sectionTitle} style={{ color: 'var(--color-white)' }}>
              How Hybrid Security Works
            </h2>
            <p className={styles.bodyTextCenteredLight} style={{ maxWidth: '100%', width: '100%', margin: '0 auto' }}>
              Hybrid security combines technology and physical security so each layer supports the others. This automated detection layer provides uninterrupted property oversight across expansive or complex commercial sites without relying solely on physical guard patrols.
            </p>
          </div>
          
          <div className={styles.featuresGrid}>
            <div className={styles.featureCardGlass}>
              <div className={styles.featureCardIcon}>
                <ScanSearch size={28} />
              </div>
              <h3 className={styles.featureTitle}>Real-Time Detection</h3>
              <p className={styles.featureDesc}>High-definition fixed cameras, thermal sensors, and mobile surveillance towers continuously monitor perimeters and access points to trigger instant system alerts upon unauthorized movement.</p>
            </div>

            <div className={styles.featureCardGlass}>
              <div className={styles.featureCardIcon}>
                <Eye size={28} />
              </div>
              <h3 className={styles.featureTitle}>Human Verification</h3>
              <p className={styles.featureDesc}>24/7 central monitoring specialists instantly evaluate live video feeds upon alert activation to distinguish genuine operational threats from harmless environmental movement.</p>
            </div>

            <div className={styles.featureCardGlass}>
              <div className={styles.featureCardIcon}>
                <Volume2 size={28} />
              </div>
              <h3 className={styles.featureTitle}>Remote Intervention</h3>
              <p className={styles.featureDesc}>When suspicious activity is verified, monitoring personnel utilize high-decibel two-way speakers to broadcast live, localized voice-down warnings directly to unauthorized individuals.</p>
            </div>

            <div className={styles.featureCardGlass}>
              <div className={styles.featureCardIcon}>
                <ShieldAlert size={28} />
              </div>
              <h3 className={styles.featureTitle}>Coordinated Field Dispatch</h3>
              <p className={styles.featureDesc}>When physical on-site intervention is required, central dispatch immediately deploys resources according to your customized property security plan.</p>
            </div>

            <div className={styles.featureCardGlass}>
              <div className={styles.featureCardIcon}>
                <FileText size={28} />
              </div>
              <h3 className={styles.featureTitle}>Digital Reporting</h3>
              <p className={styles.featureDesc}>Every system alert, verification, intervention, and dispatch action is automatically logged with verified metadata inside the SecureTrack platform, delivering transparency.</p>
            </div>
          </div>
        </div>
      </section>"""

pattern = re.compile(r"\{\/\* ===== SECTION 2: Camera Alert Is Only the Beginning ===== \*\/\}.*?<\/section>\s*\{\/\* ===== SECTION 4:", re.DOTALL)
content = pattern.sub(replacement + "\n\n      {/* ===== SECTION 4:", content)

with open(page_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
