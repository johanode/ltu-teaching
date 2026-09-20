from pathlib import Path

import numpy as np
import pandas as pd


# -----------------------------------------------------------------------------
# Läs in och förbered data
# -----------------------------------------------------------------------------

# Läs in data för avhjälpande (AU) och förebyggande (FU) underhåll
p = Path("../data/underhallsaktiviteter.csv")
df = pd.read_csv(p)

# Konvertera datumkolumner till pandas datetime-format
datetime_columns = [
    "Anmält datum",
    "Anmält vidare",
    "Arbetet påbörjat",
    "Arbetet slutfört",
]

for column in datetime_columns:
    df[column] = pd.to_datetime(df[column])

# Datum och tid då utrustningen togs i drift
t_put_in_operation = pd.to_datetime("2023-11-01 08:00")


# -----------------------------------------------------------------------------
# Hjälpfunktioner
# -----------------------------------------------------------------------------

def time_between_failures(
    row,
    events,
    start_time=None,
    exclude_pm=True,
):
    """Beräkna tiden från föregående reparation till nästa fel."""

    failure_id = row["HändelseID"]
    failure_time = row["Anmält datum"]

    # Välj avhjälpande underhåll som inträffade före det aktuella felet
    previous_failures = events.loc[
        events["Typ"].eq("AU")
        & events["HändelseID"].lt(failure_id)
    ]

    # För det första felet används tiden för driftsättning.
    # För senare fel används sluttiden för föregående reparation.
    if previous_failures.empty:
        if start_time is None:
            return pd.NaT
        previous_time = start_time
    else:
        previous_time = previous_failures.loc[
            previous_failures["HändelseID"].idxmax(),
            "Arbetet slutfört",
        ]

    # Kalendertid från föregående reparation till det aktuella felet
    elapsed_time = failure_time - previous_time

    # Behåll FU-tiden i intervallet när beräkningen baseras på kalendertid
    if not exclude_pm:
        return elapsed_time

    # Välj förebyggande underhåll som överlappar intervallet mellan felen
    pm_mask = (
        events["Typ"].eq("FU")
        & events["Arbetet påbörjat"].lt(failure_time)
        & events["Arbetet slutfört"].gt(previous_time)
    )

    pm_events = events.loc[
        pm_mask,
        ["Arbetet påbörjat", "Arbetet slutfört"],
    ]

    # Begränsa varje FU-intervall till den del som faktiskt överlappar
    # intervallet mellan föregående reparation och aktuellt fel
    overlap_start = pm_events["Arbetet påbörjat"].clip(
        lower=previous_time
    )
    overlap_end = pm_events["Arbetet slutfört"].clip(
        upper=failure_time
    )

    # Beräkna den sammanlagda överlappande tiden för förebyggande underhåll
    pm_duration = (
        overlap_end - overlap_start
    ).clip(lower=pd.Timedelta(0)).sum()

    # Tillgänglig krävd tid exkluderar stopp för förebyggande underhåll
    return elapsed_time - pm_duration


def time_between_maintenance(row, events, start_time=None):
    """Beräkna tiden från föregående underhåll till nästa underhåll."""

    event_id = row["HändelseID"]
    event_time = row["Anmält datum"]

    # Välj tidigare avhjälpande och förebyggande underhållshändelser
    previous_events = events.loc[
        events["Typ"].isin(["AU", "FU"])
        & events["HändelseID"].lt(event_id)
    ]

    # För den första underhållshändelsen används tiden för driftsättning.
    # För senare händelser används sluttiden för föregående underhåll.
    if previous_events.empty:
        if start_time is None:
            return pd.NaT
        previous_time = start_time
    else:
        previous_time = previous_events.loc[
            previous_events["HändelseID"].idxmax(),
            "Arbetet slutfört",
        ]

    return event_time - previous_time


def dt_to_hours(data, decimals=None):
    """Konvertera tidsdifferenser till timmar."""

    hours = data / pd.Timedelta(hours=1)

    if decimals is None:
        return hours

    return np.round(hours, decimals=decimals)


# %% a) Tillgänglighet baserad på planerad produktionstid
#
# Förebyggande underhåll ingår inte i den krävda produktionstiden.
# FU-stopp exkluderas därför från tiden mellan avhjälpande fel.

# Välj avhjälpande underhåll
mask_cm = df["Typ"].eq("AU")

# Beräkna tillgänglig krävd tid mellan avhjälpande fel
tbf = df.loc[mask_cm].apply(
    time_between_failures,
    axis=1,
    events=df,
    start_time=t_put_in_operation,
    exclude_pm=True,
)

# Aktiv reparationstid för avhjälpande underhåll
repair_time = (
    df.loc[mask_cm, "Arbetet slutfört"]
    - df.loc[mask_cm, "Arbetet påbörjat"]
)

# Total stopptid från felanmälan till slutförd reparation
downtime = (
    df.loc[mask_cm, "Arbetet slutfört"]
    - df.loc[mask_cm, "Anmält datum"]
)

# Inneboende tillgänglighet:
# MTBF = genomsnittlig tid mellan fel
# MRT  = genomsnittlig aktiv reparationstid
MTBF = dt_to_hours(tbf.mean())
MRT = dt_to_hours(repair_time.mean())
Ai = MTBF / (MTBF + MRT)

# Operativ tillgänglighet baserad på krävd produktionstid:
# MDT omfattar hela stopptiden för avhjälpande underhåll.
# Förebyggande underhåll ligger utanför den krävda produktionstiden.
MTBM = MTBF
MDT = dt_to_hours(downtime.mean())
Ao = MTBM / (MTBM + MDT)

# Print results
print("a) Tillgänglighet baserad på planerad produktionstid")
print(f" - MTBF={MTBF:.2f} timmar, MRT={MRT:.2f} timmar")
print(f" - Ai={Ai:.1%}")
print(f" - MTBM={MTBM:.2f} timmar, MDT={MDT:.2f} timmar")
print(f" - Ao={Ao:.1%}")


# %% b) Tillgänglighet baserad på total kalendertid
#
# Både avhjälpande och förebyggande underhåll ingår.
# Tiden mellan fel mäts som kalendertid, oavsett om förebyggande
# underhåll har genomförts mellan felen.

# Välj både avhjälpande och förebyggande underhåll
mask_maintenance = df["Typ"].isin(["AU", "FU"])

# Beräkna kalendertiden mellan samtliga underhållshändelser
tbm = df.loc[mask_maintenance].apply(
    time_between_maintenance,
    axis=1,
    events=df,
    start_time=t_put_in_operation,
)

# Beräkna kalendertiden mellan avhjälpande fel.
# Förebyggande underhåll behålls i tidsintervallet.
tbf = df.loc[mask_cm].apply(
    time_between_failures,
    axis=1,
    events=df,
    start_time=t_put_in_operation,
    exclude_pm=False,
)

# Konstruktiv tillgänglighet baserad på kalendertid mellan fel
MTBF = dt_to_hours(tbf.mean())

# Aktiv reparationstid för avhjälpande underhåll
repair_time = (
    df.loc[mask_cm, "Arbetet slutfört"]
    - df.loc[mask_cm, "Arbetet påbörjat"]
)

MRT = dt_to_hours(repair_time.mean())
Ai = MTBF / (MTBF + MRT)


# Materialtillgänglighet:
# MTBM = genomsnittlig kalendertid mellan underhållshändelser
# MAMT = genomsnittlig aktiv underhållstid för både AU och FU
MTBM = dt_to_hours(tbm.mean())

active_time = (
    df.loc[mask_maintenance, "Arbetet slutfört"]
    - df.loc[mask_maintenance, "Arbetet påbörjat"]
)

MAMT = dt_to_hours(active_time.mean())
Aa = MTBM / (MTBM + MAMT)


# Operativ tillgänglighet:
# MDT omfattar hela stopptiden för både AU och FU, mätt från
# anmälningstidpunkten tills underhållsarbetet är slutfört.
downtime = (
    df.loc[mask_maintenance, "Arbetet slutfört"]
    - df.loc[mask_maintenance, "Anmält datum"]
)

MDT = dt_to_hours(downtime.mean())
Ao = MTBM / (MTBM + MDT)


# Print results
print("b) Tillgänglighet baserad på total kalendertid")
print(f" - MTBF={MTBF:.2f} timmar, MRT={MRT:.2f} timmar")
print(f" - Ak={Ai:.1%}")
print(f" - MTBM={MTBM:.2f} timmar, MAMT={MAMT:.2f} timmar")
print(f" - Am={Aa:.1%}")
print(f" - MTBM={MTBM:.2f} timmar, MDT={MDT:.2f} timmar")
print(f" - Ao={Ao:.1%}")