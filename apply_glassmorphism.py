import os
import re

project_root = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12"

# 1. Update CSS
css_path = os.path.join(project_root, "src", "app", "page.module.css")
with open(css_path, "a", encoding="utf-8") as f:
    f.write("""
/* ==== GLASS CARDS ==== */
.featureCardGlass {
  background: rgba(255, 255, 255, 0.03);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 30px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  transition: all 0.3s ease;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
}
.featureCardGlass:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.3);
  border-color: rgba(254, 207, 49, 0.3);
  background: rgba(255, 255, 255, 0.06);
}
.featureCardGlass .featureTitle {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--color-white);
  margin-bottom: 12px;
}
.featureCardGlass .featureDesc {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.6;
}
""")

# 2. Update page.tsx
page_path = os.path.join(project_root, "src", "app", "page.tsx")
with open(page_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the specific section 3
old_section_pattern = re.compile(r"\{\/\* ===== SECTION 3: How Hybrid Security Works \(Project 7 Style\) ===== \*\/\}.*?<\/section>", re.DOTALL)

new_section = """{/* ===== SECTION 3: How Hybrid Security Works (Glass & Navy) ===== */}
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
            <span className={`${styles.sectionTag} ${styles.sectionTagDark}`}>Unified Incident Response</span>
            <h2 className={`${styles.sectionTitle} ${styles.sectionTitleDark}`}>
              How Hybrid Security Works
            </h2>
            <p className={`${styles.bodyText} ${styles.bodyTextDark}`} style={{ textAlign: 'center', maxWidth: '100%', width: '100%', margin: '0 auto' }}>
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

content = old_section_pattern.sub(new_section, content)

with open(page_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
