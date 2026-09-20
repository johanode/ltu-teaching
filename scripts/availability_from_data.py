from pathlib import Path

import numpy as np
import pandas as pd


# -----------------------------------------------------------------------------
# Load and prepare data
# -----------------------------------------------------------------------------

# Read corrective (AU) and preventive (FU) maintenance data
p = Path("../data/maintenance_events.csv")
df = pd.read_csv(p)

# Convert date and time columns to pandas datetime
datetime_columns = [
    "Reported date",
    "Forwarded date",
    "Work started",
    "Work completed",
]

for column in datetime_columns:
    df[column] = pd.to_datetime(df[column])

# Ensure event IDs are integers and sort the events
df["EventID"] = df["EventID"].astype(int)

df = (
    df.sort_values("EventID")
    .reset_index(drop=True)
)

# Verify that event IDs follow chronological order
if not df["Reported date"].is_monotonic_increasing:
    raise ValueError(
        "Event ID does not follow chronological order."
    )
    
    
# Date and time when the system was put into operation
operation_start_time  = pd.to_datetime("2023-11-01 08:00")


# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------

def time_between_failures(
    row,
    events,
    start_time=None,
    exclude_pm=True,
):
    """Calculate the time from the previous repair to the next failure."""

    failure_id = row["EventID"]
    failure_time = row["Reported date"]

    # Select corrective maintenance events that occurred before this failure
    previous_failures = events.loc[
        events["Type"].eq("CM")
        & events["EventID"].lt(failure_id)
    ]

    # Use the operation start for the first failure.
    # For later failures, use the completion time of the previous repair.
    if previous_failures.empty:
        if start_time is None:
            return pd.NaT
        previous_time = start_time
    else:
        previous_time = previous_failures.loc[
            previous_failures["EventID"].idxmax(),
            "Work completed",
        ]

    # Calendar time from the previous repair to the current failure
    elapsed_time = failure_time - previous_time

    # Keep preventive maintenance in the interval when calendar time is used
    if not exclude_pm:
        return elapsed_time

    # Select preventive maintenance that overlaps the failure interval
    pm_mask = (
        events["Type"].eq("PM")
        & events["Work started"].lt(failure_time)
        & events["Work completed"].gt(previous_time)
    )

    pm_events = events.loc[
        pm_mask,
        ["Work started", "Work completed"],
    ]

    # Limit each preventive maintenance interval to the part that overlaps
    # the interval between the previous repair and the current failure
    overlap_start = pm_events["Work started"].clip(
        lower=previous_time
    )
    overlap_end = pm_events["Work completed"].clip(
        upper=failure_time
    )

    # Calculate the total overlapping preventive maintenance time
    pm_duration = (
        overlap_end - overlap_start
    ).clip(lower=pd.Timedelta(0)).sum()

    # Available required time excludes preventive maintenance stops
    return elapsed_time - pm_duration


def time_between_maintenance(row, events, start_time=None):
    """Calculate the time from the previous maintenance event to the next."""

    event_id = row["EventID"]
    event_time = row["Reported date"]

    # Select earlier corrective and preventive maintenance events
    previous_events = events.loc[
        events["Type"].isin(["CM", "PM"])
        & events["EventID"].lt(event_id)
    ]

    # Use the operation start for the first maintenance event.
    # For later events, use the completion time of the previous event.
    if previous_events.empty:
        if start_time is None:
            return pd.NaT
        previous_time = start_time
    else:
        previous_time = previous_events.loc[
            previous_events["EventID"].idxmax(),
            "Work completed",
        ]

    return event_time - previous_time


def dt_to_hours(data, decimals=None):
    """Convert timedelta values to hours."""

    hours = data / pd.Timedelta(hours=1)

    if decimals is None:
        return hours

    return np.round(hours, decimals=decimals)


# %% a) Availability based on planned production time
#
# Preventive maintenance is not part of the required production time.
# Therefore, preventive maintenance stops are excluded from the time
# between corrective failures.

# Select corrective maintenance events
mask_cm = df["Type"].eq("CM")

# Calculate available required time between corrective failures
tbf = df.loc[mask_cm].apply(
    time_between_failures,
    axis=1,
    events=df,
    start_time=operation_start_time ,
    exclude_pm=True,
)

# Active repair time for corrective maintenance
repair_time = (
    df.loc[mask_cm, "Work completed"]
    - df.loc[mask_cm, "Work started"]
)

# Total corrective downtime from failure report to completed repair
downtime = (
    df.loc[mask_cm, "Work completed"]
    - df.loc[mask_cm, "Reported date"]
)

# Inherent availability:
# MTBF = mean time between failures
# MRT  = mean active repair time
MTBF = dt_to_hours(tbf.mean())
MRT = dt_to_hours(repair_time.mean())
Ai = MTBF / (MTBF + MRT)


# Operational availability based on required production time:
# MDT includes the complete corrective downtime.
# Preventive maintenance is outside the required production time.
MTBM = MTBF
MDT = dt_to_hours(downtime.mean())
Ao = MTBM / (MTBM + MDT)

# Print results
print("a) Availability based on planned production time")
print(f" - MTBF={MTBF:.2f} hours, MRT={MRT:.2f} hours")
print(f" - Ai={Ai:.1%}")
print(f" - MTBM={MTBM:.2f} hours, MDT={MDT:.2f} hours")
print(f" - Ao={Ao:.1%}")


# %% b) Availability based on total calendar time
#
# Both corrective and preventive maintenance are included.
# Time between failures is measured as calendar time, regardless of
# preventive maintenance occurring between the failures.

# Select all corrective and preventive maintenance events
mask_maintenance = df["Type"].isin(["CM", "PM"])

# Calculate calendar time between all maintenance events
tbm = df.loc[mask_maintenance].apply(
    time_between_maintenance,
    axis=1,
    events=df,
    start_time=operation_start_time ,
)

# Calculate calendar time between corrective failures.
# Preventive maintenance is retained in the interval.
tbf = df.loc[mask_cm].apply(
    time_between_failures,
    axis=1,
    events=df,
    start_time=operation_start_time ,
    exclude_pm=False,
)

# Inherent availability based on calendar time between failures
MTBF = dt_to_hours(tbf.mean())

repair_time = (
    df.loc[mask_cm, "Work completed"]
    - df.loc[mask_cm, "Work started"]
)

MRT = dt_to_hours(repair_time.mean())
Ai = MTBF / (MTBF + MRT)

# Achieved availability:
# MTBM = mean calendar time between maintenance events
# MAMT = mean active maintenance time for both AU and FU
MTBM = dt_to_hours(tbm.mean())

active_time = (
    df.loc[mask_maintenance, "Work completed"]
    - df.loc[mask_maintenance, "Work started"]
)

MAMT = dt_to_hours(active_time.mean())
Aa = MTBM / (MTBM + MAMT)

# Operational availability:
# MDT includes the complete downtime for both AU and FU, measured from
# the reported time until the maintenance work is completed.
downtime = (
    df.loc[mask_maintenance, "Work completed"]
    - df.loc[mask_maintenance, "Reported date"]
)

MDT = dt_to_hours(downtime.mean())
Ao = MTBM / (MTBM + MDT)


# Print results
print("b) Availability based on total calendar time")
print(f" - MTBF={MTBF:.2f} hours, MRT={MRT:.2f} hours")
print(f" - Ai={Ai:.1%}")
print(f" - MTBM={MTBM:.2f} hours, MAMT={MAMT:.2f} hours")
print(f" - Aa={Aa:.1%}")
print(f" - MTBM={MTBM:.2f} hours, MDT={MDT:.2f} hours")
print(f" - Ao={Ao:.1%}")