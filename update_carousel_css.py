import os

css_path = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12\src\components\SupervisionCarousel.module.css"
with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("background: #ffffff;", "background: var(--color-dark-blue);")
content = content.replace("color: var(--color-dark-blue);\n  margin-bottom: 12px;", "color: var(--color-white);\n  margin-bottom: 12px;")
content = content.replace("color: var(--color-text);\n  opacity: 0.9;", "color: rgba(255, 255, 255, 0.85);")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
