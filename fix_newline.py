import os

page_path = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12\src\app\page.tsx"
with open(page_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('";\\nimport', '";\nimport')

with open(page_path, "w", encoding="utf-8") as f:
    f.write(content)
