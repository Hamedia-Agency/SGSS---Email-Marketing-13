import os
import re

project_root = r"C:\Users\Admin\Documents\GitHub\SGSS---Email-Marketing-12"

# 1. Update ParticleMesh.tsx
particle_path = os.path.join(project_root, "src", "components", "ParticleMesh.tsx")
with open(particle_path, "r", encoding="utf-8") as f:
    p_content = f.read()

# Add theme prop
p_content = p_content.replace("export default function ParticleMesh({ particleCount = 20 }) {", "export default function ParticleMesh({ particleCount = 20, theme = 'dark' }: { particleCount?: number, theme?: 'dark' | 'light' }) {")
# Change color logic
old_color_logic = 'color: isGold ? "254, 207, 49" : "255, 255, 255", // Gold or White'
new_color_logic = 'color: isGold ? "254, 207, 49" : (theme === "light" ? "10, 25, 47" : "255, 255, 255"), // Gold or (Navy Blue / White)'
p_content = p_content.replace(old_color_logic, new_color_logic)

with open(particle_path, "w", encoding="utf-8") as f:
    f.write(p_content)


# 2. Update page.tsx Section 6
page_path = os.path.join(project_root, "src", "app", "page.tsx")
with open(page_path, "r", encoding="utf-8") as f:
    content = f.read()

# Ensure ParticleMesh is imported
if "import ParticleMesh" not in content:
    content = content.replace('import FloatingShapes from "@/components/FloatingShapes";', 'import FloatingShapes from "@/components/FloatingShapes";\nimport ParticleMesh from "@/components/ParticleMesh";')

new_section = """{/* ===== SECTION 6: Visibility Across the Entire Security Operation (Standard) ===== */}
      <section className={styles.section} id="visibility" style={{ position: "relative", overflow: "hidden" }}>
        {/* Full-width interactive particle mesh background */}
        <div style={{ position: "absolute", top: 0, left: 0, width: "100%", height: "100%", zIndex: 0, opacity: 0.6 }}>
          <ParticleMesh particleCount={30} theme="light" />
        </div>
        
        <div className="container" style={{ position: "relative", zIndex: 1 }}>
          <div className={styles.sectionHeader} style={{ marginBottom: 0, maxWidth: "100%" }}>
            <span className={styles.sectionTag}>Total Transparency</span>
            <h2 className={styles.sectionTitle}>Visibility Across the Entire Security Operation</h2>
            <p className={styles.bodyTextCentered} style={{ maxWidth: "100%", textAlign: "center" }}>
              Secure Guard provides complete operational visibility across all your properties without requiring you to be physically on site. By unifying live monitoring, field guard activity, and central dispatch into the SecureTrack platform, property managers gain real-time operational oversight and audit-ready incident tracking—delivering total portfolio transparency from anywhere.
            </p>
          </div>
        </div>
      </section>"""

pattern = re.compile(r"\{\/\* ===== SECTION 6: Visibility Across the Entire Security Operation \(Standard\) ===== \*\/\}.*?<\/section>", re.DOTALL)
content = pattern.sub(new_section, content)

with open(page_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS")
