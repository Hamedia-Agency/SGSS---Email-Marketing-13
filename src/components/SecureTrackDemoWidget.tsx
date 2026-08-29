"use client";

import React, { useState } from "react";
import styles from "./SecureTrackDemoWidget.module.css";
import { ShieldCheck, MapPin, Camera, AlertTriangle, Clock, CheckCircle2, FileText, ChevronRight } from "lucide-react";

export function SecureTrackDemoWidget() {
  const [activeTab, setActiveTab] = useState<"patrols" | "photos" | "incidents">("patrols");

  const patrolLogs = [
    { time: "02:14 AM", point: "North Perimeter Gate #2", status: "Verified Scan", officer: "Officer M. Ramirez", coords: "34.0522 N, 118.2437 W", badge: "Verified GPS" },
    { time: "02:30 AM", point: "Executive Parking & Loading Bay", status: "Clear & Secured", officer: "Officer M. Ramirez", coords: "34.0528 N, 118.2441 W", badge: "Verified GPS" },
    { time: "02:55 AM", point: "Building A - Main Entrance Lockup", status: "Access Verified", officer: "Officer M. Ramirez", coords: "34.0531 N, 118.2435 W", badge: "Verified GPS" },
    { time: "03:15 AM", point: "HVAC & Mechanical Room Patrol", status: "Temp Check OK", officer: "Officer M. Ramirez", coords: "34.0524 N, 118.2429 W", badge: "Verified GPS" },
  ];

  const photoLogs = [
    { title: "West Wing Exit Gate Lock Inspection", timestamp: "02:12 AM", category: "Security Check", officer: "Officer M. Ramirez", desc: "Digital verification lock confirmed secure. No signs of forced entry or tampering." },
    { title: "Lighting Hazard Reported - East Lot", timestamp: "01:45 AM", category: "Maintenance Alert", officer: "Officer M. Ramirez", desc: "Bulb failure on Pole #4 logged in SecureTrack system. Maintenance notified instantly." },
  ];

  const incidentLogs = [
    { title: "Unauthorized Vehicle Inquiry", time: "01:15 AM", priority: "Low Priority - Resolved", detail: "Driver located near loading dock. Officer verified delivery permit and escorted offsite at 01:22 AM.", status: "Closed & Logged" },
    { title: "Shift Changeover & Post Order Compliance", time: "00:00 AM", priority: "Routine Compliance", detail: "Supervisor spot check confirmed 100% Post Order compliance and full gear readiness.", status: "Verified by Supervisor" },
  ];

  return (
    <div className={styles.widgetContainer}>
      {/* Widget Header Bar */}
      <div className={styles.widgetHeader}>
        <div className={styles.widgetTitleGroup}>
          <div className={styles.statusDot} />
          <div>
            <h3 className={styles.widgetTitle}>SecureTrack™ Live Activity Feed</h3>
            <p className={styles.widgetSubtitle}>Proprietary GPS Field Reporting & Evidence Log</p>
          </div>
        </div>
        <div className={styles.liveBadge}>
          <ShieldCheck size={16} />
          Live Platform Preview
        </div>
      </div>

      {/* Interactive Tabs */}
      <div className={styles.tabNav}>
        <button
          className={`${styles.tabBtn} ${activeTab === "patrols" ? styles.activeTab : ""}`}
          onClick={() => setActiveTab("patrols")}
        >
          <MapPin size={16} />
          GPS Verified Patrols
        </button>
        <button
          className={`${styles.tabBtn} ${activeTab === "photos" ? styles.activeTab : ""}`}
          onClick={() => setActiveTab("photos")}
        >
          <Camera size={16} />
          Visual Documentation
        </button>
        <button
          className={`${styles.tabBtn} ${activeTab === "incidents" ? styles.activeTab : ""}`}
          onClick={() => setActiveTab("incidents")}
        >
          <AlertTriangle size={16} />
          Real-Time Incident Logs
        </button>
      </div>

      {/* Tab Content Display */}
      <div className={styles.widgetBody}>
        {activeTab === "patrols" && (
          <div className="space-y-3">
            <p className={styles.tabDescription}>
              Every patrol checkpoint is timestamped and geotagged in real time. Officers scan RFID/GPS tags on your property to eliminate skipped routes.
            </p>
            <div className={styles.logList}>
              {patrolLogs.map((log, idx) => (
                <div key={idx} className={styles.logCard}>
                  <div className={styles.logIcon}>
                    <CheckCircle2 size={20} className="text-[#fecf31]" />
                  </div>
                  <div className={styles.logDetails}>
                    <div className={styles.logHeader}>
                      <span className={styles.logPoint}>{log.point}</span>
                      <span className={styles.logTime}><Clock size={12} className="inline mr-1" />{log.time}</span>
                    </div>
                    <div className={styles.logMeta}>
                      <span>{log.officer}</span>
                      <span className={styles.dotSeparator}>•</span>
                      <span>GPS: {log.coords}</span>
                    </div>
                  </div>
                  <div className={styles.logBadge}>{log.badge}</div>
                </div>
              ))}
            </div>
          </div>
        )}

        {activeTab === "photos" && (
          <div className="space-y-4">
            <p className={styles.tabDescription}>
              Guards snap live photos directly in the SecureTrack mobile application. You get visual proof of property conditions without ever setting foot on site.
            </p>
            <div className={styles.photoGrid}>
              {photoLogs.map((item, idx) => (
                <div key={idx} className={styles.photoCard}>
                  <div className={styles.photoHeader}>
                    <div className={styles.photoCategory}>{item.category}</div>
                    <span className={styles.logTime}>{item.timestamp}</span>
                  </div>
                  <h4 className={styles.photoTitle}>{item.title}</h4>
                  <p className={styles.photoDesc}>{item.desc}</p>
                  <div className={styles.photoFooter}>
                    <Camera size={14} className="inline mr-1 text-[#fecf31]" />
                    <span>Captured by {item.officer}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {activeTab === "incidents" && (
          <div className="space-y-4">
            <p className={styles.tabDescription}>
              Incidents and site anomalies are logged instantly and escalated to dispatch and management in real time.
            </p>
            <div className={styles.logList}>
              {incidentLogs.map((inc, idx) => (
                <div key={idx} className={styles.incidentCard}>
                  <div className={styles.incidentHeader}>
                    <div className={styles.incidentTitleGroup}>
                      <FileText size={18} className="text-[#fecf31]" />
                      <h4 className={styles.incidentTitle}>{inc.title}</h4>
                    </div>
                    <span className={styles.incidentPriority}>{inc.priority}</span>
                  </div>
                  <p className={styles.incidentDetail}>{inc.detail}</p>
                  <div className={styles.incidentFooter}>
                    <span>Logged at {inc.time}</span>
                    <span className={styles.statusVerified}>{inc.status}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Widget Footer CTA */}
      <div className={styles.widgetFooter}>
        <span>Want to see how SecureTrack works on your property?</span>
        <a href="#lead-form" className={styles.widgetCtaLink}>
          Schedule Demo <ChevronRight size={16} />
        </a>
      </div>
    </div>
  );
}

export default SecureTrackDemoWidget;
