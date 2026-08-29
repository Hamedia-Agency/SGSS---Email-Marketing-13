import React, { useCallback, useEffect, useState } from "react";
import useEmblaCarousel from "embla-carousel-react";
import Autoplay from "embla-carousel-autoplay";
import styles from "./CarouselSection.module.css";
import { ChevronLeft, ChevronRight } from "lucide-react";
import Image from "next/image";

interface CarouselItem {
  title: string;
  description: React.ReactNode;
  image?: string;
  tag?: string;
}

interface CarouselSectionProps {
  items: CarouselItem[];
  autoplay?: boolean;
}

export const CarouselSection: React.FC<CarouselSectionProps> = ({
  items,
  autoplay = true,
}) => {
  const [emblaRef, emblaApi] = useEmblaCarousel(
    { loop: true, align: "center", skipSnaps: false },
    autoplay ? [Autoplay({ delay: 5000, stopOnInteraction: true })] : []
  );

  const [prevBtnDisabled, setPrevBtnDisabled] = useState(true);
  const [nextBtnDisabled, setNextBtnDisabled] = useState(true);
  const [selectedIndex, setSelectedIndex] = useState(0);
  const [scrollSnaps, setScrollSnaps] = useState<number[]>([]);

  const scrollPrev = useCallback(
    () => emblaApi && emblaApi.scrollPrev(),
    [emblaApi]
  );
  const scrollNext = useCallback(
    () => emblaApi && emblaApi.scrollNext(),
    [emblaApi]
  );
  const scrollTo = useCallback(
    (index: number) => emblaApi && emblaApi.scrollTo(index),
    [emblaApi]
  );

  const onInit = useCallback((emblaApi: any) => {
    setScrollSnaps(emblaApi.scrollSnapList());
  }, []);

  const onSelect = useCallback((emblaApi: any) => {
    setSelectedIndex(emblaApi.selectedScrollSnap());
    setPrevBtnDisabled(!emblaApi.canScrollPrev());
    setNextBtnDisabled(!emblaApi.canScrollNext());
  }, []);

  useEffect(() => {
    if (!emblaApi) return;

    onInit(emblaApi);
    onSelect(emblaApi);
    emblaApi.on("reInit", onInit);
    emblaApi.on("reInit", onSelect);
    emblaApi.on("select", onSelect);
  }, [emblaApi, onInit, onSelect]);

  return (
    <div className={styles.carouselSection}>
      <button
        className={`${styles.arrowBtn} ${styles.arrowLeft}`}
        onClick={scrollPrev}
        disabled={prevBtnDisabled}
        aria-label="Previous slide"
      >
        <ChevronLeft size={28} />
      </button>

      <div className={styles.embla} ref={emblaRef}>
        <div className={styles.emblaContainer}>
          {items.map((item, index) => {
            const isActive = index === selectedIndex;
            return (
              <div
                className={`${styles.emblaSlide} ${
                  isActive ? styles.isActive : ""
                }`}
                key={index}
              >
                <div className={styles.card}>
                  {item.image && (
                    <div className={styles.cardImageWrapper}>
                      <Image
                        src={item.image}
                        alt={item.title}
                        fill
                        className={styles.cardImage}
                      />
                    </div>
                  )}
                  <div className={styles.cardContent}>
                    {item.tag && <span className={styles.cardTag}>{item.tag}</span>}
                    <h3 className={styles.cardTitle}>{item.title}</h3>
                    <div className={styles.cardText}>{item.description}</div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      <button
        className={`${styles.arrowBtn} ${styles.arrowRight}`}
        onClick={scrollNext}
        disabled={nextBtnDisabled}
        aria-label="Next slide"
      >
        <ChevronRight size={28} />
      </button>

      <div className={styles.dots}>
        {scrollSnaps.map((_, index) => (
          <button
            key={index}
            className={`${styles.dot} ${
              index === selectedIndex ? styles.dotActive : ""
            }`}
            onClick={() => scrollTo(index)}
            aria-label={`Go to slide ${index + 1}`}
          />
        ))}
      </div>
    </div>
  );
};
