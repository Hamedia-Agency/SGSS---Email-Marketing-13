import os
import re

page_path = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12\src\app\page.tsx"
with open(page_path, "r", encoding="utf-8") as f:
    content = f.read()

new_section = """{/* ===== SECTION 4: The Secure Guard Hybrid Security Model (Carousel) ===== */}
      <section className={styles.section} id="applications">
        <div className="container">
          <div className={styles.sectionHeader} style={{ maxWidth: "100%" }}>
            <span className={styles.sectionTag}>Secure Guard Framework</span>
            <h2 className={styles.sectionTitle}>
              The Secure Guard Hybrid Security Model
            </h2>
            <p className={styles.bodyTextCentered} style={{ maxWidth: "100%", textAlign: "center" }}>
              Secure Guard can connect mobile surveillance technology with live monitoring, dispatch, security officers, and mobile patrol services. This allows technology to extend the reach of physical security while giving physical security teams better information about what is happening at the property.
            </p>
          </div>

          <PillarsCarousel />
        </div>
      </section>"""

pattern = re.compile(r"\{\/\* ===== SECTION 4: The Secure Guard Hybrid Security Model \(Carousel\) ===== \*\/\}.*?<\/section>", re.DOTALL)
content = pattern.sub(new_section, content)

with open(page_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
