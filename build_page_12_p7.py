import os
import re

project_root = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12"

# 1. Append CSS
css_path = os.path.join(project_root, "src", "app", "page.module.css")
with open(css_path, "a", encoding="utf-8") as f:
    f.write("""
/* ==== PROJECT 7 5-CARD ROW ==== */
.featuresGrid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 20px;
  width: 100%;
}
@media (max-width: 1200px) {
  .featuresGrid { grid-template-columns: repeat(3, 1fr); }
}
@media (max-width: 768px) {
  .featuresGrid { grid-template-columns: 1fr; }
}

.featureCard {
  background: var(--color-white);
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 12px;
  padding: 30px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(0,0,0,0.02);
}
.featureCard:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0,0,0,0.08);
  border-color: rgba(254, 207, 49, 0.3);
}
.featureCardIcon {
  width: 56px;
  height: 56px;
  border-radius: 12px;
  background: rgba(254, 207, 49, 0.1);
  color: var(--color-gold);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}
.featureTitle {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--color-dark-blue);
  margin-bottom: 12px;
}
.featureDesc {
  font-size: 0.9rem;
  color: var(--color-text);
  line-height: 1.6;
}
""")

# 2. Rewrite page.tsx
page_path = os.path.join(project_root, "src", "app", "page.tsx")
with open(page_path, "r", encoding="utf-8") as f:
    content = f.read()

# Make sure lucide-react is imported
if 'ScanSearch' not in content:
    content = content.replace(
        'import { CoverageSection } from "@/components/CoverageSection";',
        'import { CoverageSection } from "@/components/CoverageSection";\\nimport { ScanSearch, Eye, Volume2, ShieldAlert, FileText } from "lucide-react";'
    )

new_section = """{/* ===== SECTION 3: How Hybrid Security Works (Project 7 Style) ===== */}
      <section className={styles.section} id="how-it-works" style={{ background: "var(--color-bg-alt, #f7f9fc)" }}>
        <div className="container">
          <div className={styles.splitGrid} style={{ marginBottom: '48px', alignItems: 'center' }}>
            <div className={styles.sectionHeaderLeft} style={{ marginBottom: 0 }}>
              <span className={styles.sectionTag}>Unified Incident Response</span>
              <h2 className={styles.sectionTitle}>
                How Hybrid Security Works
              </h2>
              <p className={styles.bodyText}>
                Hybrid security combines technology and physical security so each layer supports the others. This automated detection layer provides uninterrupted property oversight across expansive or complex commercial sites without relying solely on physical guard patrols.
              </p>
            </div>
            <div className={styles.splitImageWrapper} style={{ height: '100%', minHeight: '350px' }}>
              <Image 
                src="https://cms.secureguardservices.com/wp-content/uploads/2026/08/em8-2.webp" 
                alt="How Hybrid Security Works" 
                fill
                className={styles.splitImage}
                style={{ borderRadius: "12px", objectFit: "cover" }}
              />
            </div>
          </div>
          
          <div className={styles.featuresGrid}>
            <div className={styles.featureCard}>
              <div className={styles.featureCardIcon}>
                <ScanSearch size={28} />
              </div>
              <h3 className={styles.featureTitle}>Real-Time Detection</h3>
              <p className={styles.featureDesc}>High-definition fixed cameras, thermal sensors, and mobile surveillance towers continuously monitor perimeters and access points to trigger instant system alerts upon unauthorized movement.</p>
            </div>

            <div className={styles.featureCard}>
              <div className={styles.featureCardIcon}>
                <Eye size={28} />
              </div>
              <h3 className={styles.featureTitle}>Human Verification</h3>
              <p className={styles.featureDesc}>24/7 central monitoring specialists instantly evaluate live video feeds upon alert activation to distinguish genuine operational threats from harmless environmental movement.</p>
            </div>

            <div className={styles.featureCard}>
              <div className={styles.featureCardIcon}>
                <Volume2 size={28} />
              </div>
              <h3 className={styles.featureTitle}>Remote Intervention</h3>
              <p className={styles.featureDesc}>When suspicious activity is verified, monitoring personnel utilize high-decibel two-way speakers to broadcast live, localized voice-down warnings directly to unauthorized individuals.</p>
            </div>

            <div className={styles.featureCard}>
              <div className={styles.featureCardIcon}>
                <ShieldAlert size={28} />
              </div>
              <h3 className={styles.featureTitle}>Coordinated Field Dispatch</h3>
              <p className={styles.featureDesc}>When physical on-site intervention is required, central dispatch immediately deploys resources according to your customized property security plan.</p>
            </div>

            <div className={styles.featureCard}>
              <div className={styles.featureCardIcon}>
                <FileText size={28} />
              </div>
              <h3 className={styles.featureTitle}>Digital Reporting</h3>
              <p className={styles.featureDesc}>Every system alert, verification, intervention, and dispatch action is automatically logged with verified metadata inside the SecureTrack platform, delivering transparency.</p>
            </div>
          </div>
        </div>
      </section>"""

pattern = re.compile(r"\{\/\* ===== SECTION 3: How Hybrid Security Works \(Unified Grid\) ===== \*\/\}.*?<\/section>", re.DOTALL)
content = pattern.sub(new_section, content)

with open(page_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
