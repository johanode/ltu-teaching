# Tillgänglighet
*Johan Odelius*, Drift och underhållsteknik, Luleå tekniska universitet
## Introduktion

Tillgänglighet, *eng. availability* (A), beskriver förmågan hos en enhet att utföra det som krävs när det krävs. Att utföra det som krävs innebär att enheten befinner sig i ett tillstånd där den kan utföra sina krävda funktioner, ett så kallat funktionsdugligt tillstånd. En enhet kan här vara en större anläggning, till exempel järnvägen mellan Luleå och Boden, ett större produktionsavsnitt eller ett delsystem i en maskin. 

Definitionen av tillgänglighet förutsätter att nödvändiga externa resurser tillhandahålls. Om vi avgränsar tillgänglighetsberäkningen till en enhet förutsätter vi alltså att de resurser som enheten behöver för att kunna utföra det som krävs tillhandahålls.

Tillgänglighet kan kvantifieras som andelen av tiden under vilken enheten kan utföra det som krävs (när det krävs). Detta benämns tillgänglighetsprestanda i svensk standard för underhåll (SS-EN 13306:2017)[^SS13306].

$$
A = \frac{\text{Tillgänglig tid}}
{\text{Tillgänglig tid} + \text{Otillgänglig tid}}
= \frac{\text{Uptime}}{\text{Uptime} + \text{Downtime}}
$$

Det finns många olika varianter av tillgänglighetsprestanda. Anledningen är att det för olika typer av verksamheter inom olika sektorer kan vara relevant att ta fram olika nyckeltal för att följa upp och utveckla verksamheten och dess underhåll.

Tidsbaserad tillgänglighet definieras enligt SS-EN 13306 som den procentandel av tiden, under en given tidsperiod, då en enhet kan utföra det som krävs. Det finns också produktionsbaserad tillgänglighet, som definieras som förhållandet mellan faktisk produktion och krävd produktion. Produktionsbaserad tillgänglighet beskrivs inte vidare i denna guide.

Den tidsbaserade tillgängligheten kan utgå från total kalendertid eller krävd tid.

[^SS13306]: *SS-EN 13306:2017 Underhåll – Underhållsterminologi*. Stockholm: Svenska institutet för standarder.

### Tillgänglighet baserad på kalendertid

Tillgänglighet baserad på kalendertid avser den andel av den totala kalendertiden (24 timmar om dygnet, 365 dagar om året) då en enhet är funktionsduglig

$$
\text{Tillgänglig tid} + \text{Otillgänglig tid} = \text{Total tid}
$$

Det är således endast en del av den tillgängliga tiden som enheten är i drift, vilket benämns nyttjandegrad. Förhållandet mellan krävd tid och kalendertid kallas beläggningsgrad (*loading*)[^TEEP]. 

[^TEEP]: Beräkningen av total effektiv utrustningsprestanda, *Total Effective Equipment Performance* (TEEP), och utrustningens totala effektivitet, *Overall Equipment Effectiveness* (OEE), där $\mathrm{TEEP} = \mathrm{Loading} \cdot \mathrm{OEE}$.

### Tillgänglighet baserad på krävd tid

Detta mått på tillgänglighet beskriver den andel av den krävda tiden eller den planerade produktionstiden då enheten utför det som krävs

 $$
 \text{Tillgänglig tid} + \text{Otillgänglig tid} = \text{Krävd tid}
 $$

Den tillgängliga tiden (*uptime*) utgörs i detta fall drifttid plus beredskapstid (*standby time*). Beredskapstid är den tid då en enhet är i funktionsdugligt tillstånd men inte i drift under krävd tid. I praktiken kan man ofta bortse från denna tid vid beräkning av tillgängligheten[^Perf].

[^Perf]: Beredskapstid är en typ av produktionsförlust (*six losses*) som ingår i beräkningen av anläggningseffektivitet för OEE.

Detta mått beskrivs också i svenska standarden Nyckeltal för underhåll[^KPI] under *Maintenance Key Performance Indicators* och benämns där *Time-based availability* (M10). I samma standarden beskrivs även *Availability based on operating time* (M11), som endast utgår från drifttid och exkluderar beredskapstid från beräkningen.

[^KPI]: *SS-EN 15341:2019 Underhåll – Nyckeltal för underhåll*. Stockholm: Svenska institutet för standarder.

## Tre mått på tillgänglighet (Ak, Am, Ao)
Utöver att tillgänglighet kan beräknas baserat på kalendertid eller krävd tid finns det ytterligare indelningar med syfte att beskriva och utvärdera olika orsaker till otillgänglig tid.

Denna guide kommer att gå igenom tre olika indikatorer (nyckeltal) för tillgänglighet:

- Konstruktiv tillgänglighet (Ak) / *Inherent availability* (Ai)
- Materialtillgänglighet (Am) / *Achieved availability* (Aa)
- Operativ tillgänglighet (Ao) / *Operational availability* (Ao)

### Konstruktiv tillgänglighet (Ak)
Den konstruktiva tillgängligheten eller inre tillgängligheten baseras på den i konstruktionen inbyggda funktionssäkerheten och underhållsmässigheten. Se också inre funktionsäkerhet och inre underhållsmässighet SS-EN 13306. Varken väntetider eller förebyggande underhåll ingår. 

Den konstruktiva tillgängligheten beräknas enligt
$$
A_k=
\frac{MTBF}
{MTBF+MTTR}
$$

där **MTBF** är medeltiden mellan fel (*Mean Time Between Failure*) och **MTTR** är medelreparationstiden (*Mean Time To Repair*). 

**MTBF** är den förväntade tiden mellan fel definieras enligt
$$
MTBF = \int_{0}^{\infty} t f(t) dt = \int_{0}^{\infty} R(t) dt
$$
där $f(t)$ är fördelningens täthetsfunktion och $R(t)$ är *reliability function* (tillförlitlighetsfunktion)^[MTBF].

En skattning av **MTBF** kan beräknas som det aritmetiska medelvärdet av tiderna mellan fel, där tiden mellan fel är tiden från återställandet av tidigare fel till nästa fel: 
$$
\mathrm{MTBF} 
=
\frac{1}{n_{Fail}}\sum_{i=1}^{n_{Fail}} T_i
=
\frac{1}{n_{Fail}}\sum_{i=1}^{n_{Fail}}
\left(
t_{\mathrm{Fail},\,i}
-
t_{\mathrm{Restored},\,i-1}
\right)
$$
där $t_{\mathrm{Restored},\,0}=0$

**MTBF** används för enheter som kan repareras, medan medeltid till fel (**MTTF**) betecknar den förväntade tiden till fel för en enhet som inte repareras. 

[^MTBF]: För en exponentialfördelning är $MTBF = 1/\lambda$ och för en Weibullfördelning $MTBF = \alpha \Gamma (1/\beta+1)$.

#### Kalenderbaserad tillgänglighet
Tid mellan fel för kalenderbaserad tillgänglighet inkluderar både tillgänglig tid och förebyggande underhållstid. Den kan därför också beräknas enligt

$$
\mathrm{MTBF} 
= 
\frac{\text{Tillgänglig tid}+\text{Förebyggande underhållstid}}{\text{Antal fel}}
$$


För de flesta system och anläggningar är reparationstiden väldigt kort i förhållande till kalendertiden. En approximation är att beräkna medeltiden av feltiderna för den totala tiden mellan fel
$$
\mathrm{MTBF} 
\approx
\frac{1}{n_{Fail}}\sum_{i=1}^{n_{Fail}} \left(
t_{\mathrm{Fail},\,i}
-
t_{\mathrm{Fail},\,i-1}
\right)
= 
\frac{\text{Total tid}}{n_{Fail}}
$$

**MTBF** approximeras även med utgångspunkt i bara tillgänglig tid som

$$
\mathrm{MTBF} 
\approx
\frac{\text{Tillgänglig tid}}{\text{Antal fel}}
$$

#### Tillgänglighet baserad på krävd tid

För tillgänglighet baserad på krävd tid beräknas normalt **MTBF** som medeltiden för drifttiden mellan fel, dvs utan hänsyn till eventuellt förebyggande underhåll som genomförs under planerad drift, enligt 

$$
\mathrm{MTBF} 
= \frac{\text{Drifttid}}{n_{Fail}}
$$

#### Medelreparationstid
Medelreparationstiden beräknas enligt[^MTTR]
$$
\mathrm{MTTR}
=
\frac{1}{n_{Fail}}\sum_{i=1}^{n_{Fail}} T_{Rep,i}
=
\frac{1}{n_{Fail}}\sum_{i=1}^{n_{Fail}}
\left(
t_{\mathrm{Repair\ end},\,i}
-
t_{\mathrm{Repair\ start},\,i}
\right)
$$

[^MTTR]: I ekvationen för konstruktiv tillgänglighet (Ak) betecknas av tradition medelreparationstiden som **MTTR**, men enligt korrekt terminologi ska det vara **MRT**: *Mean Repair Time* då **MTTR** betecknar *Mean Time To Restore* som inkluderar väntetid. 

### Materialtillgänglighet (Am)
Materialtillgänglighet, eller uppnådd tillgängligheten, inkluderar både avhjälpande och förebyggande underhåll men exkluderar fortfarande väntetider. Den beräknas enligt

$$
A_m=
\frac{MTBM}
{MTBM+MAMT}
$$

där **MTBM** (*Mean Time Between Maintenance*) är medeltiden mellan underhåll och **MAMT** (*Mean Active Maintenance Time*) är medeltiden för aktivt underhåll, såväl förebyggande som avhjälpande (reparation).

Medeltiden mellan underhåll beräknas som medelvärdet av den tillgängliga tiden mellan underhållsåtgärder 

$$
\mathrm{MTBM}
=
\frac{1}{n_M}\sum_{i=1}^{n_M} T_{Up,i}
=
\frac{1}{n_M}\sum_{i=1}^{n_M}
\left(
t_{\mathrm{M\ start},\,i}
-
t_{\mathrm{M\ end},\,i-1}
\right)
= \frac{\text{Tillgänglig tid}}{n_M}
$$. 

där $M$ (*maintenance*) är en underhållsåtgärd och $n_M = n_{Fail}+ n_{PM}$ är antal fel plus antal antalet förebyggande åtgärder.


För tillgänglighet baserad på krävd tid är, enligt tidigare, tillgänglig tid detsamma som drifttid plus beredskapstid men beräknas vanligen som 
$$
\mathrm{MTBM}
= \frac{\text{Drifttid}}{n_M}
$$. 

Den genomsnittliga aktiva underhållstiden per åtgärd beräknas som
$$
\mathrm{MAMT}
=
\frac{1}{n_M}\sum_{i=1}^{n_M} T_{AM,i}
=
\frac{1}{n_{Fail}+n_{PM}}
\left(
\displaystyle\sum_{j=1}^{n_{Fail}} T_{Rep,j}
+
\displaystyle\sum_{k=1}^{n_{PM}} T_{APM,k}
\right)
$$

där $T_{AM,i}$ är den aktiva underhållstiden för åtgärd $i$, $T_{Rep,j}$ är den reparationstiden för fel $j$ och $T_{APM,i}$ är den aktiva förebyggande underhållstiden för åtgärd $k$. 


### Operativ tillgänglighet (Ao)
Operativ tillgänglighet inkluderar all otillgänglig tid, det vill säga både avhjälpande underhåll och förebyggande underhåll där väntetiden även ingår.

Den operativa tillgängligheten beräknas enligt
$$
A_o
=
\frac{MTBM}
{MTBM+MDT}
=
\frac{Tillgänglig tid}
{Tillgänglig tid + Otillgänglig tid}
$$

där **MDT** är medeltiden för en underhållsåtgärd inklusive väntetid

$$
\mathrm{MDT}
=
\frac{1}{n_M}\sum_{i=1}^{n_M} T_{Down,i}
=
\frac{1}{n_M}\sum_{i=1}^{n_M}
\left(
t_{\mathrm{M\ end},\,i}
-
t_{\mathrm{M\ start},\,i}
\right)
$$

vilket också kan beräknas som
$$
\mathrm{MDT}
=\frac{\sum_{i=1}^{n_{Fail}} T_{CM, i} + \sum_{i=1}^{n_{PM}} T_{PM, i}}
{n_{Fail} + n_{PM}}
$$
 
eller $MDT=MAMT + MWT$ där $MWT$ är medelväntetiden enligt

$$
\mathrm{MWT}
=
\frac{1}{n_M}\sum_{i=1}^{n_M} T_{Wait,i}
$$

där $T_{Wait,i}$ är den sammanlagda väntetiden under underhållsaktivitet $i$.


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