Database Design

Overview

This document describes the initial database design for the HealthInsight project. The schema may evolve as new features are added during development.

---

User

Stores the user's profile information.

- id
- name
- age
- gender
- height
- initial_weight
- target_weight
- created_at

---

Medication

Stores medications defined by the user.

- id
- user_id
- name
- dosage
- unit
- frequency
- start_date
- end_date
- notes

---

MedicationLog

Stores medication intake records.

- id
- medication_id
- date
- taken
- notes

---

DailyRecord

Stores daily health records.

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

---

Activity

Stores physical activities.

- id
- user_id
- date
- type
- duration
- intensity
- distance
- calories
- notes

---

Measurement

Stores periodic body measurements.

- id
- user_id
- date
- weight
- waist
- hip
- whr

---

Symptom

Stores symptoms and side effects.

- id
- user_id
- date
- name
- severity
- notes

---

LabResult

Stores laboratory test results.

- id
- user_id
- date
- test_name
- value
- unit
- notes

---

Photo

Stores progress photos.

- id
- user_id
- date
- file_path
- notes