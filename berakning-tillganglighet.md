---
title: Tillgänglighet
author: Johan Odelius, Drift och underhållsteknik, Luleå tekniska universitet
toc: true
toc-title: Innehåll
toc-depth: 2
---

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

- <a id="funktionsodugligt-tillstånd"></a>**Funktionsodugligt tillstånd** (*down state*) är ett tillstånd då en enhet inte kan utföra krävd funktion på grund av förebyggande underhåll eller ett feltillstånd.

- <a id="tillgagnglig-tid"></a>**Tillgänglig tid** (*uptime*, UT) är tidsintervallet under vilket en enhet är i ett funktionsdugligt tillstånd.

- <a id="otillgagnglig-tid"></a>**Otillgänglig tid** (*downtime*, DT) är tidsintervallet under vilket en enhet är i ett funktionsodugligt tillstånd.

- <a id="drifttid"></a>**Drifttid** (*operating Time*, OT) är tidsintervallet under vilket en enhet är i drifttillstånd (ett tillstånd när en enhet utför det som krävs).

- <a id="kravd-tid"></a>**Krävd tid** (*required time*) är det tidsintervall under vilket en enhet måste vara i funktionsdugligt tillstånd. 

- <a id="beredskapstid"></a>**Beredskapstid** (*standby time*) är den tid då en enhet är i funktionsdugligt tillstånd men inte i drift under krävd tid. 

- <a id="outnyttjad-tid"></a>**Outnyttjad tid** (*idle time*) är den tid då en enhet är i funktionsdugligt tillstånd, men inte är i drift, under ej krävd tid

## Observerad och förväntad tillgänglighet
Tillgänglig och otillgänglig tid bestäms av de händelser och tidsintervall som observeras under en given observationsperiod. De händelser som påverkar tillgängligheten kan beskrivas med stokastiska processer. Exempelvis kan felhändesler modelleras med en homogen eller icke-homogen Poissonprocess (HPP respektive NHPP). De observerade tiderna till fel samt reparations- och väntetiderna är realisationer av stokastiska variabler med tillhörande sannolikhetsfördelningar. Tidsintervallet mellan förebyggande underhållsåtgärder betraktas däremot vanligen som deterministiskt och modelleras därför inte som en stokastisk variabel.

De observerade tiderna kan alltså användas för att beräkna tillgängligheten under den aktuella observationsperioden, enligt beskrivningen i föregående avsnitt. Genom att representera tiderna med deras väntevärden eller skattade medelvärden kan den förväntade tillgängligheten på lång sikt beskrivas. Detta behandlas vidare i nästa avsnitt [Tre mått på tillgänglighet](#tre-mått-på-tillgänglighet-ak-am-ao). En mer matematisk beskrivning av punkt-, intervall- och asymptotisk tillgänglighet finns på sidan [Tillgänglighet som funktion av tiden](tillganglighet-som-funktion-av-tiden.md).

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

MTBF (*Mean Time Between Failures*) är medeltiden mellan fel. En skattning av MTBF kan beräknas som det aritmetiska medelvärdet av de observerade tiderna mellan fel:

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

MTBF används för reparerbara enheter. För enheter som inte repareras används i stället MTTF (*Mean Time To Failure*), medeltid till fel.

Tid mellan fel för kalenderbaserad tillgänglighet inkluderar både tillgänglig tid $(UT)$ och förebyggande underhållstid $(T_{PM})$. Den kan därför också beräknas enligt

$$
\mathrm{MTBF} 
= 
\frac{\mathrm{UT}+\sum T_{PM}}{n_{\mathrm{Fail}}}
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


På motsvarande sätt approximeras MTBF även med utgångspunkt i bara tillgänglig tid som

$$
\mathrm{MTBF} 
\approx
\frac{\mathrm{UT}}{n_{Fail}}
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

## Beräkningsexempel 
Genomgång av två exempel för beräkning av tillgänglighet finns på sidan [Beräkningsexempel tillgänglighet](#exempel-berakning-tillganglighet.md).

## Övningsuppgifter

Övningsuppgifter finns på sidan [Räkneövningar i tillgänglighet](rakneovningar-tillganglighet.md).


