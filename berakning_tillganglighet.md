# Tillgänglighet

## Introduktion

Tillgänglighet, *eng. availability* (A), beskriver förmågan hos en enhet att utföra det som krävs när det krävs (SS-EN 13306:2017). Att utföra det som krävs innebär att enheten befinner sig i ett tillstånd där den kan utföra sina krävda funktioner, ett så kallat funktionsdugligt tillstånd. En enhet kan här vara en större anläggning, till exempel järnvägen mellan Luleå och Boden, ett produktionsavsnitt eller ett delsystem i en maskin. Definitionen av tillgänglighet förutsätter att nödvändiga externa resurser tillhandahålls. Om vi avgränsar tillgänglighetsberäkningen till en enhet förutsätter vi alltså att de resurser som enheten behöver för att kunna utföra det som krävs tillhandahållits.

Tillgänglighet kan kvantifieras och beskriver som andelen av tiden under vilken enheten kan utföra det som krävs (när det krävs). Detta benämns tillgänglighetsprestanda i underhållsstandarden (SS-EN 13306:2017).

$$
A = \frac{\text{Tillgänglig tid}}
{\text{Tillgänglig tid} + \text{Otillgänglig tid}}
= \frac{\text{Uptime}}{\text{Uptime} + \text{Downtime}}
$$

Det finns många olika varianter av tillgänglighetsprestanda. Anledningen är att det för olika typer av verksamheter inom olika sektorer kan vara relevant att ta fram olika nyckeltal för att följa upp och utveckla verksamheten och dess underhåll.

Tidsbaserad tillgänglighet definieras enligt underhållsstandarden SS-EN 13306:2017 som den procentandel av tiden, under en given tidsperiod, då en enhet kan utföra det som krävs. Det finns också produktionsbaserad tillgänglighet, som definieras som förhållandet mellan faktisk produktion och krävd produktion (SS-EN 13306:2017). Produktionsbaserad tillgänglighet beskrivs inte vidare i denna guide.

Den tidsbaserade tillgängligheten kan utgå från total kalendertid eller krävd tid.

### Tillgänglighet baserad på kalendertid

Tillgänglighet baserad på kalendertid avser den andel av den totala kalendertiden då en enhet är funktionsduglig, där
$\text{Tillgänglig tid} + \text{Otillgänglig tid} = \text{Total tid}$. Det är således endast en del av den tillgängliga tiden som enheten är i drift, vilket benämns nyttjandegrad.

Förhållandet mellan krävd tid och kalendertid kallas beläggningsgrad (*loading*). Se vidare till exempel beräkningen av total effektiv utrustningsprestanda, *Total Effective Equipment Performance* (TEEP), och utrustningens totala effektivitet, *Overall Equipment Effectiveness* (OEE), där $\mathrm{TEEP} = \mathrm{Loading} \cdot \mathrm{OEE}$.

Tillgänglighet baserad på kalendertid frångår egentligen grunddefinitionen att det handlar om en förmåga att utföra det som krävs **när det krävs**.

### Tillgänglighet baserad på krävd tid

Detta mått beskriver den andel av den krävda tiden, eller den planerade produktionstiden, då enheten utför det som krävs. Den tillgängliga tiden (*uptime*) är i detta fall drifttid plus beredskapstid (*standby time*). Otillgänglig tid är underhållstid, där 
$\text{Tillgänglig tid} + \text{Otillgänglig tid} = \text{Krävd tid}$.

Detta mått på tillgänglighet beskrivs också i SS-EN 15341:2019 under *Maintenance Key Performance Indicators* och benämns där *Time-based availability* (M10). I standarden beskrivs även *Availability based on operating time* (M11), som endast utgår från drifttid och exkluderar beredskapstid från beräkningen.

Beredskapstid är den tid då en enhet är i funktionsdugligt tillstånd men inte i drift under krävd tid. I praktiken kan man ofta bortse från denna tid vid beräkning av tillgängligheten. Beredskapstid är en typ av produktionsförlust som ingår i beräkningen av anläggningseffektivitet och därmed i beräkningen av OEE.

---

## Tre mått på tillgänglighet
Utöver att beräkning av tillgänglighet kan baseras på kalendertid eller krävd tid finns det ytterligare indelningar som utgår från att man vill beskrva olika orsakar till otillgänglig tid. Dessa är om det otillgänglig tid är reperationstid till följd av ett fel, aktiv förebyggande underhållstid eller väntetid. 

Denna guide kommer att gå igenom tre olika indikatorer (nyckeltal) för tillgänglighet:

- Konstruktiv tillgänglighet (Ak) / *Inherent availability* (Ai)
- Materialtillgänglighet (Am) / *Achieved availability* (Aa)
- Operativ tillgänglighet (Ao) / *Operational availability* (Ao)

### Konstruktiv tillgänglighet (Ak)
Den konstruktiva tillgängligheten eller inre tillgängligheten baseras på den i konstruktionen inbyggda funktionssäkerheten och underhållsmässigheten. Se också inre funktionsäkerhet och inre underhållsmässighet i SS-EN 13306:2017. Inga väntetider ingår och inte heller förebyggande underhåll. 

Den konstruktiva tillgängligheten beräknas enligt
$$
A_k=
\frac{MTBF}
{MTBF+MTTR}
$$

där MTBF är medeltiden mellan fel (*Mean Time Between Failure*) och MTTR är medelreperationstiden (*Mean Time To Repair*). Ekvationen skriver, av tradition, medelreperationstiden som MTTR, men enligt korrekt terminologi bör det egentligen vara MRT:*Mean Repair Time* då MTTR också betyder *Mean Time To Restore* som inkluderar väntetid. 

MTBF är den förväntade tiden mellan fel definiera enligt
$$
MTBF = \int_{0}^{\infty} R(t) dt
$$
där $R(t)$ är *Reliability function* (tillförlitlighetsfunktion). För en exponentialfördelning är $MTBF = 1/\lambda$ och för en weibull fördelning $MTBF = \alpha \Gamma (1/\beta+1)$.

En skattning av det förväntade värdet kan beräknas som det aritmetiska medelvärdet av tiderna mellan fel. Tid mellan fel är tiden från återställande av tidigiare fel till nästa fel. Denna tid inkluderar för kalenderbaserad tillgänglighet således även förebyggande underhållstid. För de flesta system och anläggningar är reperationstiden väldigt liten i förhållande till kalender tiden så en bra approxiamtion är att beräkna medeltiden för den totalal tiden mellan fel. 

För tillgänglighet baserad på krävd tid, beräknas normal MTBF som medeltiden för drifttiden mellan fel, dvs utan hänsyn till eventuellt förebyggande underhåll som genomförs under planerad drift. 

MTBF används enheter som kan repareras, medan medeltid till fel (MTTF) betecknar den förväntade tiden till fel för en enhet som inte repareras. 

### Materialtillgänglighet (Am)
Materialtillgänglighet eller uppnådd tillgängligheten inkluderar utöver avhjälpande underhåll även förebyggande underhåll men exkluderar fortfarande väntetider. Den beräknas enligt

Den konstruktiva tillgängligheten beräknas enligt
$$
A_a=
\frac{MTBM}
{MTBM+MAMT}
$$

där MTBM (*Mean Time Between Maintenance*) är medeltidem mellan underhåll och MAMT (*Mean Active Maintenance Time*) är mdedeltiden för aktivt underhåll, förebyggande som avhjälpande (reperation).

Därför gäller:

```math
A_k \ge A_m \ge A_o
```

---

# Illustration

Nedanstående figur visar principen.

```text
Tid ---------------------------------------------------------->

Tillgänglig tid

██████████████      ████████████████      ██████████████

Otillgänglig tid

              ████                  ██

               ↑                     ↑
            Reparation          Förebyggande
                                underhåll
```

Systemet växlar mellan tillgängligt och otillgängligt tillstånd.

När systemet fungerar samlas tillgänglig tid.

När systemet repareras eller underhålls samlas otillgänglig tid.

---

# Konstruktiv tillgänglighet (Ak)

Konstruktiv tillgänglighet beskriver hur tillgängligheten påverkas av:

- fel
- reparationstid

Förebyggande underhåll och väntetider ingår inte.

## MTBF

MTBF står för:

```text
Mean Time Between Failures
```

på svenska:

```text
Medeltid mellan fel
```

Beräknas som

```math
MTBF=
\frac{\text{Tillgänglig tid}}
{\text{Antal fel}}
```

eller, om drifttid används i uppgiften,

```math
MTBF=
\frac{\text{Drifttid}}
{\text{Antal fel}}
```

---

## MTTR

MTTR står för:

```text
Mean Time To Repair
```

på svenska:

```text
Medelreparationstid
```

Beräknas som

```math
MTTR=
\frac{\text{Total reparationstid}}
{\text{Antal fel}}
```

---

## Beräkning av Ak

När MTBF och MTTR är beräknade används

```math
A_k=
\frac{MTBF}
{MTBF+MTTR}
```

---

# Materialtillgänglighet (Am)

Materialtillgänglighet beskriver hur tillgängligheten påverkas av:

- fel
- reparationstid
- förebyggande underhåll

Väntetider ingår inte.

---

## MTBM

MTBM står för:

```text
Mean Time Between Maintenance
```

på svenska:

```text
Medeltid mellan underhåll
```

Här räknas både:

- avhjälpande underhåll
- förebyggande underhåll

MTBM beräknas som

```math
MTBM=
\frac{\text{Tillgänglig tid}}
{\text{Antal fel + antal förebyggande underhåll}}
```

---

## MAMT

MAMT står för:

```text
Mean Active Maintenance Time
```

på svenska:

```text
Genomsnittlig aktiv underhållstid
```

Den aktiva underhållstiden består av:

- avhjälpande underhåll
- förebyggande underhåll

MAMT beräknas som

```math
MAMT=
\frac{\text{Avhjälpande underhållstid}
+\text{Förebyggande underhållstid}}
{\text{Antal fel + antal förebyggande underhåll}}
```

---

## Beräkning av Am

När MTBM och MAMT är beräknade används

```math
A_m=
\frac{MTBM}
{MTBM+MAMT}
```

---

# Operativ tillgänglighet (Ao)

Operativ tillgänglighet beskriver den verkliga tillgängligheten.

Här beaktas:

- fel
- reparationstid
- förebyggande underhåll
- väntetider

---

## MDT

MDT står för:

```text
Mean Down Time
```

på svenska:

```text
Medelnertid
```

MDT beräknas som

```math
MDT=MAMT+MWT
```

---

## MWT

MWT står för:

```text
Mean Waiting Time
```

på svenska:

```text
Medelväntetid
```

Väntetider kan vara exempelvis:

- väntan på reparatör
- väntan på reservdelar
- administrativ väntetid

MWT beräknas som

```math
MWT=
\frac{\text{Total väntetid}}
{\text{Antal fel + antal förebyggande underhåll}}
```

---

## Beräkning av Ao

När MTBM och MDT är beräknade används

```math
A_o=
\frac{MTBM}
{MTBM+MDT}
```

---

## Alternativ metod

Operativ tillgänglighet kan ofta beräknas direkt från tillgänglig tid och nertid.

```math
A_o=
\frac{\text{Tillgänglig tid}}
{\text{Tillgänglig tid + nertid}}
```

där

```math
\text{Nertid}
=
\text{Underhållstid}
+
\text{Väntetid}
```

---

# Fullständigt exempel

Ett system har följande data:

- Tillgänglig tid = 3600 h
- Antal fel = 30
- Total reparationstid = 150 h
- Antal förebyggande underhåll = 15
- Förebyggande underhållstid = 45 h
- Total väntetid = 90 h

Beräkna:

- Ak
- Am
- Ao

---

## Steg 1: Beräkna MTBF

```math
MTBF=
\frac{3600}{30}
=
120\ h
```

---

## Steg 2: Beräkna MTTR

```math
MTTR=
\frac{150}{30}
=
5\ h
```

---

## Steg 3: Beräkna Ak

```math
A_k=
\frac{120}{120+5}
=
0.96
```

```math
A_k=96.0\%
```

---

## Steg 4: Beräkna MTBM

Antal underhållshändelser:

```math
30+15=45
```

```math
MTBM=
\frac{3600}{45}
=
80\ h
```

---

## Steg 5: Beräkna MAMT

Total aktiv underhållstid:

```math
150+45=195\ h
```

```math
MAMT=
\frac{195}{45}
=
4.33\ h
```

---

## Steg 6: Beräkna Am

```math
A_m=
\frac{80}{80+4.33}
=
0.949
```

```math
A_m=94.9\%
```

---

## Steg 7: Beräkna MWT

```math
MWT=
\frac{90}{45}
=
2.0\ h
```

---

## Steg 8: Beräkna MDT

```math
MDT=
4.33+2.0
=
6.33\ h
```

---

## Steg 9: Beräkna Ao

```math
A_o=
\frac{80}{80+6.33}
=
0.927
```

```math
A_o=92.7\%
```

---

# Sammanfattning

## Konstruktiv tillgänglighet

```math
A_k=
\frac{MTBF}{MTBF+MTTR}
```

```math
MTBF=
\frac{\text{Tillgänglig tid}}{\text{Antal fel}}
```

```math
MTTR=
\frac{\text{Total reparationstid}}{\text{Antal fel}}
```

---

## Materialtillgänglighet

```math
A_m=
\frac{MTBM}{MTBM+MAMT}
```

```math
MTBM=
\frac{\text{Tillgänglig tid}}
{\text{Antal fel + antal förebyggande underhåll}}
```

```math
MAMT=
\frac{\text{Avhjälpande underhållstid}
+\text{Förebyggande underhållstid}}
{\text{Antal fel + antal förebyggande underhåll}}
```

---

## Operativ tillgänglighet

```math
A_o=
\frac{MTBM}{MTBM+MDT}
```

```math
MDT=MAMT+MWT
```

```math
MWT=
\frac{\text{Total väntetid}}
{\text{Antal fel + antal förebyggande underhåll}}
```