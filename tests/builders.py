"""Builder functions for test models."""

from datetime import date

from healthinsight.models.user import User
from healthinsight.models.daily_record import DailyRecord
from healthinsight.models.medication import Medication
from healthinsight.models.activity import Activity
from healthinsight.models.measurement import Measurement
from healthinsight.models.symptom import Symptom
from healthinsight.models.lab_result import LabResult


def make_user(**kwargs):
    """Create a User instance with default values."""
    data = {
        "full_name": "John Doe",
        "date_of_birth": date(1990, 1, 1),
        "gender": "male",
        "height": 180,
        "initial_weight": 75.0,
        "target_weight": 70.0,
    }
    data.update(kwargs)
    return User(**data)


def make_daily_record(**kwargs):
    """Return a valid DailyRecord instance."""
    data = {
        "user_id": 1,
        "date": date(2024, 1, 1),
        "weight": 75.5,
        "systolic_bp": 120,
        "diastolic_bp": 80,
        "heart_rate": 70,
        "blood_glucose": 95,
        "water_intake": 2.5,
        "sleep_hours": 8,
        "sleep_quality": "Good",
        "appetite_score": 4,
        "energy_score": 5,
        "notes": "Feeling well",
    }
    data.update(kwargs)
    return DailyRecord(**data)


def make_medication(**kwargs):
    """Create a Medication instance with default values."""
    data = {
        "user_id": 1,
        "name": "Metformin",
        "dosage": 500.0,
        "unit": "mg",
        "frequency": "Twice daily",
        "start_date": date(2024, 1, 1),
        "end_date": date(2024, 12, 31),
        "notes": "Take after meals",
    }
    data.update(kwargs)
    return Medication(**data)


def make_activity(**kwargs):
    """Create an Activity instance with default values."""
    data = {
        "user_id": 1,
        "date": date(2024, 1, 1),
        "activity_type": "Walking",
        "duration": 45,
        "intensity": "Medium",
        "distance": 3.5,
        "calories": 220,
        "notes": "Morning walk",
    }
    data.update(kwargs)
    return Activity(**data)


def make_measurement(**kwargs):
    """Create a Measurement instance with default values."""
    data = {
        "user_id": 1,
        "date": date(2024, 1, 1),
        "waist": 90.5,
        "hip": 100.0,
        "whr": 0.91,
    }
    data.update(kwargs)
    return Measurement(**data)


def make_symptom(**kwargs):
    """Return a valid Symptom instance."""
    data = {
        "user_id": 1,
        "date": date(2024, 1, 1),
        "name": "Headache",
        "severity": 3,
        "notes": "Mild headache after lunch",
    }
    data.update(kwargs)
    return Symptom(**data)


def make_lab_result(**kwargs):
    """Return a valid LabResult instance."""
    data = {
        "user_id": 1,
        "date": date(2024, 1, 1),
        "test_name": "Fasting Blood Sugar",
        "value": 95.0,
        "unit": "mg/dL",
        "notes": "Normal",
    }
    data.update(kwargs)
    return LabResult(**data)
