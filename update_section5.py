import os
import re

page_path = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12\src\app\page.tsx"
with open(page_path, "r", encoding="utf-8") as f:
    content = f.read()

new_section = """{/* ===== SECTION 5: Existing Camera Integration (Escalation box) ===== */}
      <section className={styles.contactSection} id="integration">
        <div className={`container ${styles.contactContainer}`}>
          <div className={styles.contactContentPanel} style={{ backgroundColor: "#ffffff" }}>
            <div className={styles.sectionHeader} style={{ margin: "0 0 24px 0", textAlign: "left" }}>
              <span className={styles.sectionTag}>Cost-Effective Oversight</span>
              <h2 className={styles.sectionTitle} style={{ marginBottom: "16px", color: "var(--color-dark-blue)" }}>
                Existing Camera Integration
              </h2>
            </div>
            <p className={styles.bodyText} style={{ color: "var(--color-dark-blue)" }}>
              Secure Guard evaluates and integrates your existing security infrastructure into our hybrid monitoring network, eliminating the operational expense of complete hardware replacement.
            </p>
            <p className={styles.bodyText} style={{ color: "var(--color-dark-blue)", marginBottom: 0 }}>
              Compatible camera setups are connected directly into our 24/7 active monitoring, central dispatch, field response, and digital reporting ecosystem, instantly adding live human oversight and intervention to passive feeds.
            </p>
          </div>
        </div>
      </section>"""

pattern = re.compile(r"\{\/\* ===== SECTION 5: Existing Camera Integration \(Escalation box\) ===== \*\/\}.*?<\/section>", re.DOTALL)
content = pattern.sub(new_section, content)

with open(page_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
