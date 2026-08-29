import os
import re

page_path = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12\src\app\page.tsx"
with open(page_path, "r", encoding="utf-8") as f:
    content = f.read()

old_header_pattern = re.compile(r"<div className=\{styles\.sectionHeader\}.*?<\/div>\s*<div className=\{styles\.featuresGrid\}>", re.DOTALL)

new_header = """<div className={styles.sectionHeader} style={{ marginBottom: '48px', display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', width: '100%', maxWidth: '100%' }}>
            <span className={styles.sectionTag} style={{ color: "#b89000", background: "rgba(254, 207, 49, 0.13)", borderColor: "rgba(254, 207, 49, 0.35)" }}>Unified Incident Response</span>
            <h2 className={styles.sectionTitle} style={{ color: 'var(--color-white)' }}>
              How Hybrid Security Works
            </h2>
            <p className={styles.bodyTextCenteredLight} style={{ maxWidth: '100%', width: '100%', margin: '0 auto' }}>
              Hybrid security combines technology and physical security so each layer supports the others. This automated detection layer provides uninterrupted property oversight across expansive or complex commercial sites without relying solely on physical guard patrols.
            </p>
          </div>
          
          <div className={styles.featuresGrid}>"""

content = old_header_pattern.sub(new_header, content)

with open(page_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
