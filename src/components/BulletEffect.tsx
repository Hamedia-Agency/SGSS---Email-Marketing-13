"use client";

import React, { useState, useEffect } from "react";
import styles from "./BulletEffect.module.css";

interface Bullet {
  id: number;
  x: number;
  y: number;
}

export function BulletEffect() {
  const [bullets, setBullets] = useState<Bullet[]>([]);

  useEffect(() => {
    const handleClick = (e: MouseEvent) => {
      const newBullet = {
        id: Date.now(),
        x: e.clientX,
        y: e.clientY,
      };
      setBullets((prev) => [...prev, newBullet]);

      // Remove the bullet after animation completes (e.g., 2 seconds)
      setTimeout(() => {
        setBullets((prev) => prev.filter((b) => b.id !== newBullet.id));
      }, 2000);
    };

    window.addEventListener("click", handleClick);
    return () => window.removeEventListener("click", handleClick);
  }, []);

  return (
    <>
      {bullets.map((bullet) => (
        <div
          key={bullet.id}
          className={styles.bulletHole}
          style={{ left: bullet.x, top: bullet.y }}
        >
          <div className={styles.spark} />
          <div className={styles.debris} />
        </div>
      ))}
    </>
  );
}
