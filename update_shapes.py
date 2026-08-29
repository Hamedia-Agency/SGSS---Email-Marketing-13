import os
import re

file_path = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12\src\components\FloatingShapes.tsx"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add theme prop
content = content.replace("export default function FloatingShapes({ shapeCount = 15 }) {", "export default function FloatingShapes({ shapeCount = 15, theme = 'dark' }: { shapeCount?: number, theme?: 'dark' | 'light' }) {")

# Update color logic
old_color_logic = 'color: isGold ? "254, 207, 49" : "255, 255, 255", // Gold or White'
new_color_logic = 'color: isGold ? "254, 207, 49" : (theme === "light" ? "10, 25, 47" : "255, 255, 255"), // Gold or (Navy Blue / White)'
content = content.replace(old_color_logic, new_color_logic)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
