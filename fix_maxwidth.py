import os

page_path = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12\src\app\page.tsx"
with open(page_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the specific sectionHeader style
old_str = "className={styles.sectionHeader} style={{ marginBottom: '48px', display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', width: '100%' }}"
new_str = "className={styles.sectionHeader} style={{ marginBottom: '48px', display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', width: '100%', maxWidth: '100%' }}"

content = content.replace(old_str, new_str)

with open(page_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
