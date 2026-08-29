import os
import re

page_path = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-11\src\app\page.tsx"
with open(page_path, "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r"\{\/\* ===== INDUSTRY APPLICATIONS \(CAROUSEL\) ===== \*\/\}.*?<\/section>", re.DOTALL)

new_block = """{/* ===== INDUSTRY APPLICATIONS (CAROUSEL) ===== */}
      <section className={`${styles.section} ${styles.sectionDark}`} id="applications">
        <div className="container">
          <div className={styles.sectionHeaderCentered}>
            <span className={`${styles.sectionTag} ${styles.sectionTagDark}`}>Deployment Scenarios</span>
            <h2 className={`${styles.sectionTitle} ${styles.sectionTitleDark}`}>
              Industry Applications
            </h2>
            <p className={`${styles.bodyTextCentered} ${styles.bodyTextDark}`}>
              Mobile surveillance towers provide critical security coverage for expansive, remote, or temporary outdoor spaces where traditional wired cameras cannot be installed.
            </p>
          </div>

          <ApplicationsCarousel />
        </div>
      </section>"""

content = pattern.sub(new_block, content)

with open(page_path, "w", encoding="utf-8") as f:
    f.write(content)
