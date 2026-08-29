import os

page_path = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12\src\app\page.tsx"
with open(page_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    '<span className={styles.sectionTag}>Cost-Effective Oversight</span>',
    '<span className={styles.sectionTag} style={{ color: "var(--color-dark-blue)" }}>Cost-Effective Oversight</span>'
)

with open(page_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
