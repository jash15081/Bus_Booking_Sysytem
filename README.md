# 🚌 Bus Ticket Booking System - Django Project

A full-stack web application for booking bus tickets online, built using **Django**. It features custom route-finding algorithms, seat selection, OTP-based authentication, e-ticket emailing, price calculation by distance, cancellation management, and a dedicated conductor dashboard.

---

## ✨ Features

* **🔐 Authentication with OTP Verification** (Email-based)
* **📍 Custom Route Finder** using DFS Algorithm
* **📏 Auto Fare Calculation** Based on Distance (per-km rate)
* **🪑 Interactive Seat Selection UI**
* **👩 Women-Only Seat Booking Option**
* **🎟️ E-Ticket Generation & Email Confirmation**
* **❌ Ticket Cancellation with Email Notification**
* **🧑‍✈️ Conductor Dashboard** to Manage Reservations
* **📦 Built on Django with SQLite** (via Django ORM)

---

## 🧠 Route Finding (Graph Algorithm)

The system uses a **custom graph-based algorithm** to compute the optimal path between source and destination cities. Each city is a node, and each direct route is an edge weighted by distance (in kilometers). The backend processes all valid routes dynamically.

> **Example:**
>
> * **Nodes**: Ahmedabad, Vadodara, Surat
> * **Edges with distances**: (Ahmedabad → Vadodara: 100 km), (Vadodara → Surat: 150 km)
> * **Input**: Ahmedabad → Surat
> * **Output Route**: Ahmedabad → Vadodara → Surat
> * **Total Distance**: 250 km
> * **Auto Fare**: 250 km $\times$ ₹X per km

---

## 💰 Dynamic Fare Calculation

Ticket prices are automatically calculated using the formula:

**Total Fare = Total Distance (km) $\times$ Rate Per Kilometer (₹)**

* **Distance** is computed using the graph path.
* **Per-kilometer rate** is configurable.
* The **final fare** is displayed before booking.
* This ensures fairness, transparency, and automation.

---

## 🛠️ Tech Stack

| Layer             | Technology               |
| :---------------- | :----------------------- |
| **Backend** | Django (Python)          |
| **Database** | SQLite + Django ORM      |
| **Frontend** | HTML, CSS, JavaScript    |
| **Auth** | OTP via Email            |
| **Email Service** | Django Email Backend     |

---

## 🔧 Installation

1.  **Clone the Repo**

    ```bash
    git clone https://github.com/jash15081/Bus_Booking_Sysytem.git
    cd Bus_Booking_Sysytem/SP_project
    ```

2.  **Create & Activate Virtual Environment**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations**

    ```bash
    python manage.py migrate
    ```

5.  **Start Server**

    ```bash
    python manage.py runserver
    ```

---

## 🧪 Usage

* **Register/Login** with OTP via email.
* **Select source and destination** cities.
* The system finds the **optimal route and calculates the fare**.
* **View available buses** → choose one → select your seat(s).
* **Book ticket** → e-ticket emailed instantly.
* **View & manage bookings** in the user dashboard.
* **Cancel ticket** if needed — confirmation sent via email.
* **Conductors can view reservations** via their dashboard.

---

## 🧑‍💻 Conductor Dashboard

* View list of buses assigned
* Monitor reservations by date, seat number, and user
* Seat layout visualization for clarity

---

## ✅ Future Improvements
* Add Razorpay or Stripe for online payments
* Admin panel to manage buses, cities, fares, and conductors
* SMS ticket & OTP support
* Mobile-first PWA optimization
