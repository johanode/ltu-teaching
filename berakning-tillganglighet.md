# Tillgänglighet
*Johan Odelius*, Drift och underhållsteknik, Luleå tekniska universitet
## Introduktion

Tillgänglighet, *eng. availability* (A), beskriver förmågan hos en enhet att utföra det som krävs när det krävs. Att utföra det som krävs innebär att enheten befinner sig i ett tillstånd där den kan utföra sina krävda funktioner, ett så kallat funktionsdugligt tillstånd. 

Definitionen av tillgänglighet förutsätter att nödvändiga externa resurser tillhandahålls. Om vi avgränsar tillgänglighetsberäkningen till en enhet förutsätter vi alltså att de resurser som enheten behöver för att kunna utföra det som krävs tillhandahålls.

Tillgänglighet kan kvantifieras som andelen av krävd tid (*required time*) under vilken enheten kan utföra det som krävs. Detta benämns tillgänglighetsprestanda i svensk standard för underhåll (SS-EN 13306:2017)[^SS13306].

$$
A = \frac{\text{Tillgänglig tid}}
{\text{Tillgänglig tid} + \text{Otillgänglig tid}}
= \frac{\mathrm{Uptime}}{\mathrm{Uptime} + \mathrm{Downtime}}
$$

Det finns många olika varianter av tillgänglighetsprestanda. Anledningen är att det för olika typer av verksamheter inom olika sektorer kan vara relevant att ta fram olika nyckeltal för att följa upp och utveckla verksamheten och dess underhåll.

Tidsbaserad tillgänglighet definieras enligt SS-EN 13306 som den procentandel av tiden, under en given tidsperiod, då en enhet kan utföra det som krävs. Det finns också produktionsbaserad tillgänglighet, som definieras som förhållandet mellan faktisk produktion och krävd produktion. Produktionsbaserad tillgänglighet beskrivs inte vidare i denna guide. 

Tidsbaserad tillgänglighet beskrivs också i svenska standarden SS-EN 15341:2019 Nyckeltal för underhåll[^SS15341] under *Maintenance Key Performance Indicators* genom nyckeltalet *Time-based availability* (M10) 
$$
M10 = \frac{\text{Uptime during required time}}{\text{Required time}}
$$

I M10 ingår [beredskapstid](#definitioner) (*standby time*) i tillgänglig tid (*uptime*) men inte [outnyttjad tid](#definitioner) (*idle time*). 

Gemensamt för tidsbaserade tillgänglighetsmått är att man måste bestämma vilken tid som ska räknas som [krävd tid](#definitioner). I denna guide beskrivs två alternativ: total kalendertid och planerad drifttid.

[^SS13306]: *SS-EN 13306:2017 Underhåll – Underhållsterminologi*. Stockholm: Svenska institutet för standarder.
[^SS15341]: *SS-EN 15341:2019 Underhåll – Nyckeltal för underhåll*. Stockholm: Svenska institutet för standarder.

### Tillgänglighet baserad på total kalendertid

Tillgänglighet baserad på kalendertid avser den andel av den totala kalendertiden (24 timmar om dygnet, 365 dagar om året) då en enhet är funktionsduglig

$$
\mathrm{Uptime} + \mathrm{Downtime} = \mathrm{Total\ time} 
\Longrightarrow 
A = \frac{\mathrm{Uptime}}{\mathrm{Total\ time}}
$$

### Tillgänglighet baserad på planerad driftstid

Detta mått på tillgänglighet beskriver den andel av den planerade driften då enheten kan utföra det som krävs $(\text{Krävd tid}=\text{Planerad drift})$. Den tillgängliga tiden omfattar drifttid och beredskapstid. 

I SS-EN 15341 beskrivs även *Availability based on operating time* (M11), som endast utgår från drifttid (OT) och exkluderar beredskapstid, enligt
$$
M11 = \frac{OT}{\text{Required operating time}}
$$

Standarden för nyckeltal inom underhåll beskriver även ett tredje mått, *Availability based on time to restoration* (M12) enligt
$$
M12 = \frac{OT}{OT+TTR}
$$ 
där TTR (*time to restoration*) är tiden till återställning och omfattar reparationstid och väntetid. 

### Definitioner
- <a id="funktionsdugligt-tillstånd"></a>**Funktionsdugligt tillstånd** (*up state*) är ett tillstånd då en enhet kan utföra krävd funktion, antaget att de externa resurserna tillhandahålls.

- <a id="funktionsodugligt-tillstånd"></a>**Funktionspdugligt tillstånd** (*down state*) är ett tillstånd då en enhet inte kan utföra krävd funktion på grund av förebyggande underhåll eller ett feltillstånd.

- <a id="tillgagnglig-tid"></a>**Tillgägnglig tid** (*uptime*, UT) är tidsintervallet under vilket en enhet är i ett funktionsdugligt tillstånd.

- <a id="otillgagnglig-tid"></a>**Otillgägnglig tid** (*downtime*, DT) är tidsintervallet under vilket en enhet är i ett funktionsodugligt tillstånd.

- <a id="drifttid"></a>**Drifttid** (*operating Time*, OT) är tidsintervallet under vilket en enhet är i drifttillstånd (ett tillstånd när en enhet utför det som krävs).

- <a id="kravd-tid"></a>**Krävd tid** (*required time*) är det tidsintervall under vilket en enhet måste vara i funktionsdugligt tillstånd. 

- <a id="beredskapstid"></a>**Beredskapstid** (*standby time*) är den tid då en enhet är i funktionsdugligt tillstånd men inte i drift under krävd tid. 

- <a id="outnyttjad-tid"></a>**Outnyttjad tid** (*idle time*) är den tid då en enhet är i funktionsdugligt tillstånd, men inte är i drift, under ej krävd tid

## Från observerad till förväntad tillgänglighet
Tillgänglig och otillgänglig tid består av observerade tider som är realisationer av slumpmässiga tider under en given observationsperiod. Tider till fel, reparationstider och väntetider kan beskrivas som stokastiska variabler med tillhörande sannolikhetsfördelningar. När fel inträffar, hur lång tid reparationen tar och hur länge man måste vänta på de resurser som behövs för att genomföra underhållet genom olika stokastiska processer. Tidsintervallet mellan förebyggande underhållsåtgärder beskrivs vanligen inte som en stokastisk variabel.

Enligt föregående avsnitt kan tillgängligheten under en observerad period beräknas direkt från de observerade tiderna. Genom att representera tiderna med deras väntevärden eller skattade medelvärden kan den förväntade tillgängligheten på lång sikt beskrivas. Detta behandlas vidare i nästa avsnitt [Tre mått på tillgänglighet](#tre-mått-på-tillgänglighet-ak-am-ao). En mer matematisk beskrivning av punkt-, intervall- och asymptotisk tillgänglighet finns på sidan [Tillgänglighet som funktion av tiden](tillganglighet-som-funktion-av-tiden.md).

## Tre mått på tillgänglighet (Ak, Am, Ao)
Utöver att tillgänglighet kan beräknas baserat på kalendertid eller driftstid finns det ytterligare indelningar med syfte att beskriva och utvärdera olika orsaker till otillgänglig tid.

Denna guide kommer att gå igenom tre olika indikatorer (nyckeltal) för tillgänglighet:

- [Konstruktiv tillgänglighet](#konstruktiv-tillgänglighet-ak) ($A_k$) / *Inherent availability* ($A_i$)
- [Materialtillgänglighet](#materialtillgänglighet-am) ($A_m$) / *Achieved availability* ($A_a$)
- [Operativ tillgänglighet](#operativ-tillgänglighet-ao) ($A_o$) / *Operational availability* ($A_o$)

### Konstruktiv tillgänglighet (Ak)
Den konstruktiva tillgängligheten eller inre tillgängligheten baseras på den i konstruktionen inbyggda funktionssäkerheten och underhållsmässigheten. Se också inre funktionsäkerhet och inre underhållsmässighet i SS-EN 13306. Varken väntetider eller förebyggande underhåll ingår. 

Den konstruktiva tillgängligheten beräknas enligt
$$
A_k=
\frac{MTBF}
{MTBF+MRT}
$$

där [**MTBF**](#mtbf) är medeltiden mellan fel (*Mean Time Between Failures*) och [**MRT**](#mrt) är medelreparationstiden (*Mean Repair Time*). 


I ekvationen för konstruktiv tillgänglighet betecknas medelreparationstiden traditionellt ofta med **MTTR** (*Mean Time To Repair*). Enligt terminologin i svensk standard betecknas medelreparationstiden emellertid med **MRT** (*Mean Repair Time*), medan **MTTR** står för *Mean Time To Restore* och inkluderar väntetid.

### Materialtillgänglighet (Am)
Materialtillgänglighet, eller uppnådd tillgängligheten, inkluderar både avhjälpande och förebyggande underhåll men exkluderar fortfarande väntetider. Den beräknas enligt

$$
A_m=
\frac{MTBM}
{MTBM+MAMT}
$$

där [**MTBM**](#mtbm) (*Mean Time Between Maintenance*) är medeltiden mellan underhåll och [**MAMT**](#mamt) (*Mean Active Maintenance Time*) är medeltiden för aktivt underhåll, såväl förebyggande som avhjälpande (reparation).

### Operativ tillgänglighet (Ao)
Operativ tillgänglighet inkluderar både avhjälpande underhåll och förebyggande underhåll där väntetid även ingår.

Den operativa tillgängligheten beräknas enligt
$$
A_o
=
\frac{MTBM}
{MTBM+MDT}
$$

där [**MDT**](#mdt) (*Mean Downtime*) är medeltiden är den genomsnittliga otillgängliga tiden per underhållsåtgärd, inklusive väntetid. Den kan också beräknas som $MDT = MAMT + MWT$ där [**MWT**](#mwt) (*Mean Waiting Time*) är medelväntetiden. 

---

## Driftsäkerhetsparametrar

Tillgänglighetsmåtten i föregående avsnitt bygger på medeltider för bland annat tider mellan fel, reparationstider och väntetider. Parametrarna är väntevärden för slumpmässiga tider, men skattas i praktiken från observerade tider.

Nedan beskrivs hur parametrarna kan skattas från observerade data. En mer utförlig statistisk beskrivning finns på sidan [Statistisk beskrivning av driftsäkerhetsparametrar](driftsakerhetsparametrar.md).

### MTBF

**MTBF** (*Mean Time Between Failures*) är medeltiden mellan fel. En skattning av **MTBF** kan beräknas som det aritmetiska medelvärdet av de observerade tiderna mellan fel:

$$
\mathrm{MTBF}
=
\frac{1}{n_{\mathrm{Fail}}}
\sum_{i=1}^{n_{\mathrm{Fail}}} T_i
=
\frac{1}{n_{\mathrm{Fail}}}
\sum_{i=1}^{n_{\mathrm{Fail}}}
\left(
t_{\mathrm{Fail},i}
-
t_{\mathrm{Restored},i-1}
\right)
$$

där $t_{\mathrm{Restored},0}=t_0$ och $t_0$ är observationsperiodens starttid.

MTBF används för reparerbara enheter. För enheter som inte repareras används i stället **MTTF** (*Mean Time To Failure*), medeltid till fel.

Tid mellan fel för kalenderbaserad tillgänglighet inkluderar både tillgänglig tid och förebyggande underhållstid. Den kan därför också beräknas enligt

$$
\mathrm{MTBF} 
= 
\frac{\mathrm{Uptime}+\text{Preventive maintenance time}}{\text{Number of failures}}
$$


För många system och anläggningar är reparationstiden väldigt kort i förhållande till kalendertiden. En approximation är att beräkna medeltiden av feltiderna för den totala tiden mellan fel
$$
\mathrm{MTBF} 
\approx
\frac{1}{n_{Fail}}\sum_{i=1}^{n_{Fail}} \left(
t_{\mathrm{Fail},\,i}
-
t_{\mathrm{Fail},\,i-1}
\right)
= 
\frac{\text{Total time}}{n_{Fail}}
$$

**MTBF** approximeras även med utgångspunkt i bara tillgänglig tid som

$$
\mathrm{MTBF} 
\approx
\frac{\mathrm{Uptime}}{\text{Number of failures}}
$$

#### Drifttid

För tillgänglighet baserad på planerad drift beräknas normalt **MTBF** som medeltiden för drifttiden $(OT)$ mellan fel, dvs utan hänsyn till eventuellt förebyggande underhåll som genomförs under planerad drift, enligt 

$$
\mathrm{MTBF} 
= \frac{mathrm{OT}}{n_{Fail}}
$$

### MRT
Medelreparationstiden beräknas enligt
$$
\mathrm{MRT}
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


### MTBM
Medeltiden mellan underhåll beräknas som medelvärdet av den tillgängliga tiden mellan underhållsåtgärder 

$$
\mathrm{MTBM}
=
\frac{1}{n_M}\sum_{i=1}^{n_M} T_{U,i}
=
\frac{1}{n_M}\sum_{i=1}^{n_M}
\left(
t_{\mathrm{M\ start},\,i}
-
t_{\mathrm{M\ end},\,i-1}
\right)
= \frac{\mathrm{Uptime}}{n_M}
$$. 

där $M$ (*maintenance*) är en underhållsåtgärd och $n_M = n_{Fail}+ n_{PM}$ är antalet avhjälpande och förebyggande underhållsåtgärder.


För tillgänglighet baserad på krävd tid är, enligt tidigare, tillgänglig tid detsamma som drifttid plus beredskapstid men beräknas vanligen som 
$$
\mathrm{MTBM}
= \frac{\mathrm{OT}}{n_M}
$$. 

### MAMT
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

där $T_{AM,i}$ är den aktiva underhållstiden för åtgärd $i$, $T_{Rep,j}$ är reparationstiden för fel $j$ och $T_{APM,k}$ är den aktiva förebyggande underhållstiden för åtgärd $k$. 

### MDT
Den genomsnittliga otillgängliga tiden (nedtiden) per underhållsåtgärd beräknas enligt 
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
där $T_{\mathrm{CM},i}$ är den otillgängliga tiden för den avhjälpande underhållsåtgärden $i$, och $T_{\mathrm{PM},i}$ är motsvarande tid för den förebyggande underhållsåtgärden.

Vilket också kan beräknas som
$$
\mathrm{MDT}
=\frac{\sum_{i=1}^{n_{Fail}} T_{CM, i} + \sum_{i=1}^{n_{PM}} T_{PM, i}}
{n_{Fail} + n_{PM}}
$$
 
#### MWT
MDT kan också beräknas som 
$$
MDT = MAMT + MWT
$$ 

$MWT$ är medelväntetiden per underhållsåtgärd enligt

$$
\mathrm{MWT}
=
\frac{1}{n_M}\sum_{i=1}^{n_M} T_{Wait,i}
$$

där $T_{Wait,i}$ är den sammanlagda väntetiden under underhållsaktivitet $i$.

# Exempel beräkning

## Exempel 1

Ett system har följande data:

- Tillgänglig tid (UT) = 3600 h
- Antal fel = 30
- Summa reparationstid = 150 h
- Medelväntetid avhjälpande underhåll = 3 h
- Antal förebyggande underhåll = 15
- Summa förebyggande underhållstid = 60 h
- Medelväntetid förebyggande underhåll = 1 h

Beräkna den kalenderbaserad tillgängligheten:

a) $A_k$

b) $A_m$

c) $A_o$


---

### a) Beräkna Ak
$$
A_k=
\frac{MTBF}{MTBF+MRT}
$$

#### Steg 1: MTBF
$$
MTBF=
\frac{\text{UT}+\sum T_{PM}}{n_{Fail}}
=
\frac{3600+(45+15)}{30}
=
122\ h
$$

#### Steg 2: MRT

$$
MRT=
\frac{\sum T_{Rep}}{n_{Fail}}
=
\frac{150}{30}
=
5\ h
$$

#### Steg 3: Ak

$$
A_k=
\frac{MTBF}{MTBF+MRT}
=
\frac{122}{122+5}
=
0.961
$$

**Svar:** Den konstruktiva tillgängligheten $A_k=96.1\%$

### b) Beräkna Am
$$
A_m=
\frac{MTBM}{MTBM+MAMT}
$$

#### Steg 1: MTBM
$$
MTBM=
\frac{UT}{n_{M}}
=
\frac{3600}{30+15}
=
80\ h
$$

där antal underhållshändelser n_{M}=n_{Fail}+n_{PM}$

#### Steg 2: MAMT
$$
MAMT=
\frac{\sum T_{Rep} + \sum T_{APM}}{n_{M}}
=
\frac{150 + (60-15 \cdot 1)}{45}
=
4.33\ h
$$

där summan aktivt förebyggande underhållstid erhålls ur 
$$
\sum T_{APM} = \sum T_{PM} - n_{PM} \cdot MWT_{PM}
$$

#### Steg 3: Am

$$
A_m=
\frac{MTBM}{MTBM+MAMT}
=
\frac{80}{80+4.33}
=
0.949
$$

**Svar:** Material tillgängligheten är $A_m=94.9\%$

### c) Beräkna Ao

$$
A_o=
\frac{MTBM}{MTBM+MDT}
$$

#### Steg 1: MTBM
$$
MTBM=
\frac{UT}{n_{M}}
=
\frac{3600}{45}
=
80\ h
$$

#### Steg 2: MDT
$$
MDT=
\frac{\sum T_{CM} + \sum T_{PM}}{n_M}
=
\frac{(150+90) + (45+15)}{45}
=
6.667\ h
$$

#### Steg 3: Ao

$$
A_o=
\frac{MTBM}{MTBM+MDT}
=
\frac{80}{80+6.667}
=
0.923
$$

**Svar:** Den operativa tillgängligheten är $A_o=92.3\%$


## Exempel 2

Nedan är data för fel och förebyggande underhåll för ett anläggning med kontinuerlig produktion. Anläggningen driftsattes 2023-11-01 kl 08:00.

[a)](#uppgift-a) Beräkna $A_k$, $A_o$ baserat på planerad produktionstid, där planerad produktionstid är total tid minus de förebyggande underhållsstoppen.

[b)](#uppgift-b) Beräkna $A_k$, $A_m$, $A_o$ baserat på kalender tid


| ID   | Typ   | Anmält datum $(t_{failure, i})$| Anmält vidare       | Arbetet påbörjat    | Arbetet slutfört $(t_{restore, i})$ |
|:-----|:------|:--------------------|:--------------------|:--------------------|:--------------------|
| F01  | AU    | 2024-01-15 03:12:00 | 2024-01-15 06:45:00 | 2024-01-15 07:20:00 | 2024-01-15 08:40:00 |
| F02  | AU    | 2024-04-22 17:54:00 | 2024-04-22 19:10:00 | 2024-04-22 20:00:00 | 2024-04-22 23:15:00 |
| F03  | AU    | 2024-07-31 09:27:00 | 2024-07-31 10:05:00 | 2024-07-31 11:20:00 | 2024-07-31 14:50:00 |
| F04  | AU    | 2024-10-10 13:56:00 | 2024-10-10 14:53:00 | 2024-10-10 20:46:00 | 2024-10-11 04:45:00 |
| F05  | AU    | 2024-11-18 22:41:00 | 2024-11-18 23:30:00 | 2024-11-19 01:10:00 | 2024-11-19 03:20:00 |
| F06  | AU    | 2024-12-04 06:11:00 | 2024-12-04 06:41:00 | 2024-12-04 15:25:00 | 2024-12-04 22:37:00 |
| F07  | AU    | 2025-02-24 14:08:00 | 2025-02-24 14:55:00 | 2025-02-24 16:10:00 | 2025-02-24 19:40:00 |
| F08  | AU    | 2025-05-12 01:59:00 | 2025-05-12 02:39:00 | 2025-05-14 01:28:00 | 2025-05-14 11:19:00 |
| F09  | AU    | 2025-06-03 05:33:00 | 2025-06-03 08:20:00 | 2025-06-03 09:00:00 | 2025-06-03 11:45:00 |
| F10  | AU    | 2025-09-11 18:26:00 | 2025-09-11 20:10:00 | 2025-09-11 21:00:00 | 2025-09-12 00:55:00 |
| F11  | AU    | 2025-10-25 16:53:00 | 2025-10-25 17:40:00 | 2025-10-27 06:31:00 | 2025-10-27 09:00:00 |
| F12  | AU    | 2025-12-20 07:51:00 | 2025-12-20 08:40:00 | 2025-12-20 10:15:00 | 2025-12-20 13:05:00 |
| F13  | AU    | 2026-03-29 12:17:00 | 2026-03-29 13:05:00 | 2026-03-29 15:00:00 | 2026-03-29 17:40:00 |
| F14  | AU    | 2026-04-14 07:21:00 | 2026-04-14 08:18:00 | 2026-04-15 04:14:00 | 2026-04-15 09:34:00 |
| F15  | AU    | 2026-04-21 15:20:00 | 2026-04-21 15:59:00 | 2026-04-23 11:47:00 | 2026-04-23 20:45:00 |
| F16  | AU    | 2026-07-07 01:44:00 | 2026-07-07 04:20:00 | 2026-07-07 05:10:00 | 2026-07-07 07:05:00 |


| ID   | Typ   | Anmält datum        | Anmält vidare       | Arbetet påbörjat $(t_{PM\ start, i})$ | Arbetet slutfört $(t_{PM\ end, i})$ |
|:-----|:------|:--------------------|:--------------------|:--------------------|:--------------------|
| PM01 | FU    | 2024-03-01 08:00:00 | 2024-03-01 08:00:00 | 2024-03-01 08:00:00 | 2024-03-02 08:00:00 |
| PM02 | FU    | 2024-09-01 08:00:00 | 2024-09-01 08:00:00 | 2024-09-01 08:00:00 | 2024-09-02 08:00:00 |
| PM03 | FU    | 2025-03-01 08:00:00 | 2025-03-01 08:00:00 | 2025-03-01 08:00:00 | 2025-03-02 08:00:00 |
| PM04 | FU    | 2025-09-01 08:00:00 | 2025-09-01 08:00:00 | 2025-09-01 08:00:00 | 2025-09-02 08:00:00 |
| PM05 | FU    | 2026-03-01 08:00:00 | 2026-03-01 08:00:00 | 2026-03-01 08:00:00 | 2026-03-02 08:00:00 |
| PM06 | FU    | 2026-09-01 08:00:00 | 2026-09-01 08:00:00 | 2026-09-01 08:00:00 | 2026-09-02 08:00:00 |


### Uppgift a

#### Steg 1: Tider
Beräkna tid mellan fel samt reperationstid och nedtid (otillgänglig tid)
- **Tid mellan fel** är den tillgängliga tiden från föregående återställande till nästa fel där förebyggande underhåll som infaller under intervallet exkluderas
$$
TBF_{i}
=
\left(
t_{failure,i}
-
t_{restore,i-1}
\right)
-
\sum_j
\left(
t_{PM end,j}
-
t_{PM start,j}
\right)
$$
- **Reperationstid** är tidsintervallet mellan *Arbetet slutfört* och *Arbetet påbörjat*
- **Väntetid** är tidsintervallet mellan *Arbetet påbörjat* och *Anmält datum* 
- **Nedtid** är tidsintervallet mellan *Arbetet slutfört* och *Anmält datum*.

| ID   |   Tid mellan fel (TBF) [dygn] |   Reparationstid [h] |   Väntetid [h] |   Nedtid [h] |
|:-----|------------------------------:|---------------------:|---------------:|-------------:|
| F01  |                          74.8 |                  1.3 |            4.1 |          5.5 |
| F02  |                          97.4 |                  3.2 |            2.1 |          5.4 |
| F03  |                          99.4 |                  3.5 |            1.9 |          5.4 |
| F04  |                          70   |                  8   |            6.8 |         14.8 |
| F05  |                          38.7 |                  2.2 |            2.5 |          4.6 |
| F06  |                          15.1 |                  7.2 |            9.2 |         16.4 |
| F07  |                          81.6 |                  3.5 |            2   |          5.5 |
| F08  |                          75.3 |                  9.8 |           47.5 |         57.3 |
| F09  |                          19.8 |                  2.8 |            3.4 |          6.2 |
| F10  |                          99.3 |                  3.9 |            2.6 |          6.5 |
| F11  |                          43.7 |                  2.5 |           37.6 |         40.1 |
| F12  |                          54   |                  2.8 |            2.4 |          5.2 |
| F13  |                          98   |                  2.7 |            2.7 |          5.4 |
| F14  |                          15.6 |                  5.3 |           20.9 |         26.2 |
| F15  |                           6.2 |                  9   |           44.4 |         53.4 |
| F16  |                          74.2 |                  1.9 |            3.4 |          5.4 |

#### Steg 2: Konstruktiv tillgänglighet (Ak)
$$
MTBF = \frac{1}{16} \sum_{i=1}^{16} TBF_i = 1444.6 h
$$

$$
MRT = \frac{1}{16} \sum_{i=1}^{16} T_{R,i} = 4.35 h
$$

$$
A_k = \frac{MTBF}{MTBF+MRT}=\frac{1444.6}{1444.6+4.35} = 0.997
$$

**Svar:** Konstruktiv tillgänglighet $A_k = 99.7\%$

#### Steg 3: Operativ tillgänglighet (Ao)

$$
MTBM = MTBF \Longleftarrow \text{förebyggande underhåll genomförs under icke krävd tid}
$$


$$
MDT = \frac{1}{16} \sum_{i=1}^{16} T_{Down,i} = 16.46 h
$$

$$
A_o = \frac{MTBM}{MTBM+MDT}=\frac{1444.6}{1444.6+16.46} = 0.989
$$

**Svar:** Operativ tillgänglighet $A_o = 98.9\%$

### Uppgift b

#### Steg 1: Tider

Beräkna tid mellan fel, tid mellan underhåll, aktiv underhållstid (avhjälpande och förebyggande) samt nedtid
- **Tid mellan fel** är
$$
\mathrm{TBF} = t_{failure, i-1}-t_{restore, i} \quad \left(t_{failure, 0}=\text{2023-11-01 08:00}\right)
$$ 

- **Tid mellan underhåll** är 
$$
\mathrm{TBM} = t_{m\ restore, i}-t_{m, i-1} \quad \left(t_{m, 0}=\text{2023-11-01 08:00}\right)
$$ 

- **Aktiv underhållstid** (samma som rerationstid för AU) är tidsintervallet mellan *Arbetet slutfört* och *Arbetet påbörjat*.
- **Väntetid** är tidsintervallet mellan *Arbetet påbörjat* och *Anmält datum* 
- **Nedtid** är tidsintervallet mellan *Arbetet slutfört* och *Anmält datum*.

| ID   | Tid mellan fel (TBF) [dygn]   |   Tid mellan underhåll (TBM) [dygn] |   Aktiv underhållstid [h] |   Väntetid [h] |   Nedtid [h] |
|:-----|:------------------------------|------------------------------------:|--------------------------:|---------------:|-------------:|
| F01  | 74.8                          |                                74.8 |                       1.3 |            4.1 |          5.5 |
| PM01 | -                             |                                46   |                      24   |            0   |         24   |
| F02  | 98.4                          |                                51.4 |                       3.2 |            2.1 |          5.4 |
| F03  | 99.4                          |                                99.4 |                       3.5 |            1.9 |          5.4 |
| PM02 | -                             |                                31.7 |                      24   |            0   |         24   |
| F04  | 71.0                          |                                38.2 |                       8   |            6.8 |         14.8 |
| F05  | 38.7                          |                                38.7 |                       2.2 |            2.5 |          4.6 |
| F06  | 15.1                          |                                15.1 |                       7.2 |            9.2 |         16.4 |
| F07  | 81.6                          |                                81.6 |                       3.5 |            2   |          5.5 |
| PM03 | -                             |                                 4.5 |                      24   |            0   |         24   |
| F08  | 76.3                          |                                70.7 |                       9.8 |           47.5 |         57.3 |
| F09  | 19.8                          |                                19.8 |                       2.8 |            3.4 |          6.2 |
| PM04 | -                             |                                89.8 |                      24   |            0   |         24   |
| F10  | 100.3                         |                                 9.4 |                       3.9 |            2.6 |          6.5 |
| F11  | 43.7                          |                                43.7 |                       2.5 |           37.6 |         40.1 |
| F12  | 54.0                          |                                54   |                       2.8 |            2.4 |          5.2 |
| PM05 | -                             |                                70.8 |                      24   |            0   |         24   |
| F13  | 99.0                          |                                27.2 |                       2.7 |            2.7 |          5.4 |
| F14  | 15.6                          |                                15.6 |                       5.3 |           20.9 |         26.2 |
| F15  | 6.2                           |                                 6.2 |                       9   |           44.4 |         53.4 |
| F16  | 74.2                          |                                74.2 |                       1.9 |            3.4 |          5.4 |
| PM06 | -                             |                                56   |                      24   |            0   |         24   |



#### Steg 2: Konstruktiv tillgänglighet (Ak)
$$
MTBF = \frac{1}{16} \sum_{i=1}^{16} TBF_i = 1452.1 h
$$

$$
MRT = \frac{1}{16} \sum_{i=1}^{16} T_{R,i} = 4.35 h
$$

$$
A_k = \frac{MTBF}{MTBF+MRT}=\frac{1452.1}{1451.2+4.35} = 0.997
$$

**Svar:** Konstruktiv tillgänglighet $A_k = 99.7\%$

#### Steg 3: Materialtillgänglighet (Am)
$$
MTBM = \frac{1}{22} \sum_{i=1}^{22} TBM_i = 1111.4 h
$$

$$
MAMT = \frac{1}{22} \sum_{i=1}^{22} T_{M,i} = 9.71 h
$$

$$
A_m = \frac{MTBF}{MTBF+MRT}=\frac{1111.4}{1111.4+9.71} = 0.991
$$

**Svar:** Materialtillgänglighet $A_m = 99.1\%$

#### Steg 4: Operativ tillgänglighet (Ao)

$$
MTBM = \frac{1}{22} \sum_{i=1}^{22} TBM_i = 1111.4 h
$$


$$
MDT = \frac{1}{22} \sum_{i=1}^{22} T_{Down,i} = 18.51 h
$$

$$
A_o = \frac{MTBM}{MTBM+MDT}=\frac{1111.4}{1111.4+18.51} = 0.984
$$

**Svar:** Operativ tillgänglighet $A_o = 98.4\%$
