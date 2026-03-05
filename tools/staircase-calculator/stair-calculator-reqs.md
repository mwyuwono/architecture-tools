# Product Requirements Document (PRD): V1 Residential Stair Calculator

## 1. Project Overview
**Objective:** Build a simple, lightweight web application to calculate the horizontal footprint ("Total Run") of a residential straight staircase based on floor-to-floor height. 
**Target Use Case:** Early-stage architectural space planning for residential designs in MA, NY, VT, and CT.
**Scope:** Version 1 will focus exclusively on straight staircases, omitting complex layouts (L-shapes, U-shapes, winders) to ensure a rapid build and launch.

## 2. Building Code Standards
All calculations are baselined against the **International Residential Code (IRC) - Section R311.7**, which serves as the foundational standard for the target states.

### Core IRC Constraints Used for Math:
* **Maximum Riser Height:** 7.75 inches
* **Minimum Tread Depth:** 10 inches

### Additional IRC Context (For Reference/Future Versions):
* **Minimum Clear Width:** 36 inches
* **Minimum Headroom:** 6 feet, 8 inches (80 inches)

## 3. Functional Requirements

### 3.1. User Inputs
The system shall accept the following input from the user:
* **Floor-to-Floor Height:** A single numerical value entered in inches. *(Definition: The measurement from the surface of the finished lower floor to the surface of the finished upper floor).*
* **Constraints:** Must accept positive numbers. Minimum input should be capped at 40 inches, maximum at 200 inches for practical usability.

### 3.2. Processing Logic (The Math)
The system will perform the following calculations automatically upon input:
1. **Total Risers:** `Ceiling(Floor-to-Floor Height ÷ 7.75)`
   *(Must round up to the nearest whole number to ensure no riser exceeds the 7.75" maximum).*
2. **Exact Riser Height:** `Floor-to-Floor Height ÷ Total Risers`
3. **Total Treads:** `Total Risers - 1`
   *(The final step up is the upper floor itself).*
4. **Total Horizontal Run:** `Total Treads × 10`

### 3.3. System Outputs
The interface shall clearly display:
* Total number of risers (integer).
* Exact height of each riser (formatted to two decimal places, e.g., "7.50 inches").
* Total number of treads (integer).
* **Total Horizontal Run** (This is the primary user goal).

## 4. Non-Functional Requirements
* **Tech Stack:** Vanilla HTML, CSS, and JavaScript. No external databases, servers, or heavy frameworks required for V1.
* **Performance:** Calculations must update instantaneously as the user changes the input value (client-side execution).
* **User Interface:** Clean, high-contrast, and mobile-responsive. 
* **Visualization:** A 2D HTML5 Canvas drawing that visually represents the steps, updating proportionately as the input changes.

## 5. Future Considerations (Post-V1)
* Allow inputting "Ceiling Height" and "Floor Joist Thickness" separately.
* Add standard headroom clearance visualizers.
* Support for metric conversions (mm/cm).
* Support for L-shaped stairs with a landing.