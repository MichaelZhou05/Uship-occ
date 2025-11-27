# Web Application Work Flow

# Ushipp Operations Command Center (OCC) - Workflow Summary

## Project Objective

To build a **Headless Logistics Engine** that sits downstream from the existing Wix marketing site. The system automates route optimization, driver dispatch, and customer communication, replacing manual spreadsheets with an "Amazon-like" delivery experience.

## The "Happy Path" Lifecycle

### Phase 1: Ingestion & Soft Booking (The Bridge)

1. **Trigger:** A student places an order on `universityshipping.com` (Wix).
2. **Action:** Wix triggers a Webhook to our API (`POST /webhooks/wix-order`).
3. **System Logic:**
    - Sanitizes address data.
    - Geocodes addresses to Latitude/Longitude.
    - Creates a User Profile and Order record in Postgres with status `UNCONFIRMED`.
4. **Customer Exp:** Student receives an automated email with a **Magic Link** to their Tracking Dashboard.

### Phase 2: Confirmation (T-Minus 2 Weeks)

1. **Trigger:** 14 days before the move-out date.
2. **Action:** System sends a "Finalize Details" email.
3. **Customer Exp:** Student clicks the link, confirms their exact Dorm/Gate Code, and locks in their box count.
4. **System Logic:** Order status updates to `CONFIRMED`. Only confirmed orders are eligible for routing.

### Phase 3: The Logistics Brain (The "Florida/Maine Run")

1. **Trigger:** Admin clicks "Generate Route" in the Dashboard.
2. **System Logic (Python OR-Tools):**
    - Fetches all `CONFIRMED` orders.
    - Applies Constraints: Truck Capacity (Volume) + Geographic Linearity (North-South efficiency).
    - **Output:** Generates a **Manifest** (Ordered list of stops) for Driver A and Driver B.
3. **Communication:** System texts students a specific ETA window (e.g., "Tuesday, 9 AM - 11 AM").

### Phase 4: Execution (Driver Loop)

1. **Trigger:** Moving Day. Driver opens the **Mobile App**.
2. **Flexibility:** Driver reviews the list. If traffic is bad, they drag-and-drop stops to reorder them. The system recalculates ETAs for downstream customers.
3. **The Approach:**
    - Driver moves toward Stop #1.
    - **Geo-Fence Trigger:** When GPS < 5 miles from destination, system auto-texts student: *"5 mins away!"*
4. **The Handover:**
    - **Pickup:** Driver scans items, takes photo of loaded truck. Status -> `IN_TRANSIT`.
    - **Drop-off:** Driver unloads, takes photo at door. Status -> `DELIVERED`.

### Phase 5: Visibility (The Tracker)

- **Customer View:** Throughout Phase 4, the student views their **Tracking Page**.
- **Real-Time:** They see a live map icon of the truck moving toward them (powered by Redis GPS updates).
- **Support:** If an issue arises, they reply to the SMS, creating a ticket in the Admin Console.