"""Builder functions for test models."""

from datetime import date

from healthinsight.models.user import User
from healthinsight.models.daily_record import DailyRecord
from healthinsight.models.medication import Medication


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
