import os
import re

page_path = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12\src\app\page.tsx"
with open(page_path, "r", encoding="utf-8") as f:
    content = f.read()

new_section = """{/* ===== SECTION 3: How Hybrid Security Works (Project 7 Style) ===== */}
      <section className={styles.section} id="how-it-works" style={{ background: "var(--color-bg-alt, #f7f9fc)" }}>
        <div className="container">
          <div className={styles.sectionHeaderCentered} style={{ marginBottom: '40px' }}>
            <span className={styles.sectionTag}>Unified Incident Response</span>
            <h2 className={styles.sectionTitle}>
              How Hybrid Security Works
            </h2>
            <p className={styles.bodyTextCentered}>
              Hybrid security combines technology and physical security so each layer supports the others. This automated detection layer provides uninterrupted property oversight across expansive or complex commercial sites without relying solely on physical guard patrols.
            </p>
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

pattern = re.compile(r"\{\/\* ===== SECTION 3: How Hybrid Security Works \(Project 7 Style\) ===== \*\/\}.*?<\/section>", re.DOTALL)
content = pattern.sub(new_section, content)

with open(page_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
