
import os
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

reference_data = pd.DataFrame({
    "age": [21, 22, 23, 24, 25, 26, 27, 28],
    "score": [60, 65, 70, 75, 80, 85, 90, 95],
})

current_data = pd.DataFrame({
    "age": [30, 31, 32, 33, 34, 35, 36, 37],
    "score": [20, 25, 30, 35, 40, 45, 50, 55],
})

report = Report([DataDriftPreset()])
result = report.run(
    reference_data=reference_data,
    current_data=current_data,
)

os.makedirs("reports", exist_ok=True)
result.save_html("reports/data_drift.html")

print("Evidently monitoring completed.")
print("Report: reports/data_drift.html")
