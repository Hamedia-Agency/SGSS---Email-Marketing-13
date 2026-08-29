import os
import re

page_path = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12\src\app\page.tsx"
with open(page_path, "r", encoding="utf-8") as f:
    content = f.read()

new_header = """<div className={styles.sectionHeader} style={{ marginBottom: '48px', display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', width: '100%' }}>
            <span className={styles.sectionTag}>Unified Incident Response</span>
            <h2 className={styles.sectionTitle}>
              How Hybrid Security Works
            </h2>
            <p className={styles.bodyText} style={{ textAlign: 'center', maxWidth: '100%', width: '100%', margin: '0 auto' }}>
              Hybrid security combines technology and physical security so each layer supports the others. This automated detection layer provides uninterrupted property oversight across expansive or complex commercial sites without relying solely on physical guard patrols.
            </p>
          </div>"""

# Find the old header block in section 3
pattern = re.compile(r"<div className=\{styles\.sectionHeaderCentered\}.*?<\/div>", re.DOTALL)
content = pattern.sub(new_header, content)

with open(page_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
