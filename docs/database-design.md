# Database Design

## Overview

This document describes the initial database design for the HealthInsight project. The schema may evolve as new features are added during development.

---

## User

Stores the user's profile information.

### Fields

- id
- name
- age
- gender
- height
- initial_weight
- target_weight
- created_at

### Relationships

- One user can have many medications.
- One user can have many daily records.
- One user can have many activities.
- One user can have many body measurements.
- One user can have many symptoms.
- One user can have many laboratory results.
- One user can have many progress photos.

---

## Medication

Stores medications defined by the user.

### Fields

- id
- user_id
- name
- dosage
- unit
- frequency
- start_date
- end_date
- notes

### Relationships

- Belongs to one user.
- Has many medication logs.

---

## MedicationLog

Stores medication intake records.

### Fields

- id
- medication_id
- date
- taken
- notes

### Relationships

- Belongs to one medication.

---

## DailyRecord

Stores daily health records.

### Fields

- id
- user_id
- date
- weight
- systolic_pressure
- diastolic_pressure
- heart_rate
- blood_glucose
- water_intake
- appetite_score
- energy_score
- sleep_quality
- notes

### Relationships

- Belongs to one user.

---

## Activity

Stores physical activities.

### Fields

- id
- user_id
- date
- type
- duration
- intensity
- distance
- calories
- notes

### Relationships

- Belongs to one user.

---

## Measurement

Stores periodic body measurements.

### Fields

- id
- user_id
- date
- weight
- waist
- hip
- whr

### Relationships

- Belongs to one user.

---

## Symptom

Stores symptoms and side effects.

### Fields

- id
- user_id
- date
- name
- severity
- notes

### Relationships

- Belongs to one user.

---

## LabResult

Stores laboratory test results.

### Fields

- id
- user_id
- date
- test_name
- value
- unit
- notes

### Relationships

- Belongs to one user.

---

## Photo

Stores progress photos.

### Fields

- id
- user_id
- date
- file_path
- notes

### Relationships

- Belongs to one user.
