import os
import re

page_path = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12\src\app\page.tsx"
with open(page_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the entire splitGrid section with a centered sectionHeader
old_header_pattern = re.compile(r"<div className=\{styles\.splitGrid\}.*?<\/div>\s*<\/div>\s*<\/div>", re.DOTALL)

new_header = """<div className={styles.sectionHeaderCentered} style={{ marginBottom: '40px' }}>
            <span className={styles.sectionTag}>Unified Incident Response</span>
            <h2 className={styles.sectionTitle}>
              How Hybrid Security Works
            </h2>
            <p className={styles.bodyTextCentered}>
              Hybrid security combines technology and physical security so each layer supports the others. This automated detection layer provides uninterrupted property oversight across expansive or complex commercial sites without relying solely on physical guard patrols.
            </p>
          </div>"""

content = old_header_pattern.sub(new_header, content)

with open(page_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
