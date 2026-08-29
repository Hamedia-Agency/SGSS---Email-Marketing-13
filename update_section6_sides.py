import os
import re

page_path = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12\src\app\page.tsx"
with open(page_path, "r", encoding="utf-8") as f:
    content = f.read()

new_section = """{/* ===== SECTION 6: Visibility Across the Entire Security Operation (Standard) ===== */}
      <section className={styles.section} id="visibility" style={{ position: "relative", overflow: "hidden" }}>
        <div className={styles.standardPatternLeft}>
          <ParticleMesh particleCount={25} theme="light" />
        </div>
        <div className={styles.standardPatternRight}>
          <ParticleMesh particleCount={25} theme="light" />
        </div>
        
        <div className="container" style={{ position: "relative", zIndex: 1 }}>
          <div className={styles.sectionHeader} style={{ marginBottom: 0, maxWidth: "100%" }}>
            <span className={styles.sectionTag}>Total Transparency</span>
            <h2 className={styles.sectionTitle}>Visibility Across the Entire Security Operation</h2>
            <p className={styles.bodyTextCentered} style={{ maxWidth: "100%", textAlign: "center" }}>
              Secure Guard provides complete operational visibility across all your properties without requiring you to be physically on site. By unifying live monitoring, field guard activity, and central dispatch into the SecureTrack platform, property managers gain real-time operational oversight and audit-ready incident tracking—delivering total portfolio transparency from anywhere.
            </p>
          </div>
        </div>
      </section>"""

pattern = re.compile(r"\{\/\* ===== SECTION 6: Visibility Across the Entire Security Operation \(Standard\) ===== \*\/\}.*?<\/section>", re.DOTALL)
content = pattern.sub(new_section, content)

with open(page_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
