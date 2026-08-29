import os

css_path = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12\src\app\page.module.css"
with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("background: rgba(8, 18, 38, 0.96) !important;", "background: #ffffff !important;")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
