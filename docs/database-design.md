# Database Design

## Overview

This document describes the initial database design for the HealthInsight project. The schema may evolve as new features are added during development.

---

## User

Stores the user's profile information.

### Fields

- id
- full_name
- date_of_birth
- gender
- height
- initial_weight
- target_weight
- created_at
- updated_at

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
- created_at
- updated_at

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
- created_at
- updated_at

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
- systolic_bp
- diastolic_bp
- heart_rate
- blood_glucose
- water_intake
- sleep_hours
- sleep_quality
- appetite_score
- energy_score
- notes
- created_at
- updated_at

### Relationships

- Belongs to one user.

---

## Activity

Stores physical activities.

### Fields

- id
- user_id
- date
- activity_type
- duration
- intensity
- distance
- calories
- notes
- created_at
- updated_at

### Relationships

- Belongs to one user.

---

## Measurement

Stores periodic body measurements.

### Fields

- id
- user_id
- date
- waist
- hip
- whr
- created_at
- updated_at

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
- created_at
- updated_at

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
- created_at
- updated_at

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
- created_at
- updated_at

### Relationships

- Belongs to one user.
