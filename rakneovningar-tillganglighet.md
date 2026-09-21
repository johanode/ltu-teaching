# Räkneövningar i tillgänglighet
Övningarna behandlar konstruktiv, material- och operativ tillgänglighet.

## Uppgifter

1. [Konstruktiv tillgänglighet för en pump](#uppgift-1-konstruktiv-tillgänglighet-för-en-pump)
2. [Konstruktiv tillgänglighet baserad på drifttid](#uppgift-2-konstruktiv-tillgänglighet-baserad-på-drifttid)
3. [Tre mått på tillgänglighet för ett borraggregat](#uppgift-3-tre-mått-på-tillgänglighet-för-ett-borraggregat)
4. [Tillgänglighet för en asfalteringsmaskin](#uppgift-4-tillgänglighet-för-en-asfalteringsmaskin)
5. [Konstruktiv och operativ tillgänglighet](#uppgift-5-konstruktiv-och-operativ-tillgänglighet)
6. [Tillgänglighet från en arbetsorderdata](#uppgift-6-tillgänglighet-från-en-arbetsorderdata)
    - [A: Planerad produktionstid](#a-planerad-produktionstid)
    - [B: Kalendertid](#b-kalendertid)



Följande beteckningar används:

- **AU**: avhjälpande underhåll
- **FU**: förebyggande underhåll
- **UT**: tillgänglig tid (*uptime*)
- **DT**: otillgänglig tid (*downtime*)
- **MTBF**: medeltid mellan fel
- **MRT**: medelreparationstid
- **MTBM**: medeltid mellan underhåll
- **MAMT**: medeltid för aktivt underhåll
- **MDT**: genomsnittlig otillgänglig tid per underhållsåtgärd

### Lösningsförslag
[Lösningsförslag räkneövningar tillgänglighet](losningsforslag-rakneovningar-tillganglighet.md)


## Uppgift 1: Konstruktiv tillgänglighet för en pump

Beräkna pumpens konstruktiva tillgänglighet $A_k$.

|  |  |
|---|---:|
| Medeltid mellan fel, MTBF | 20 h |
| Sammanlagd reparationstid | 200 h |
| Antal fel | 100 |


## Uppgift 2: Konstruktiv tillgänglighet baserad på drifttid

Ett system har följande data från en observationsperiod:

|  |  |
|---|---:|
| Drifttid, OT | 2 600 h |
| Sammanlagd tid för förebyggande underhåll | 400 h |
| Sammanlagd reparationstid | 300 h |
| Antal fel | 11 |

Beräkna systemets konstruktiva tillgänglighet $A_k$ baserat på drifttid.


## Uppgift 3: Tre mått på tillgänglighet för ett borraggregat

Ett borraggregat har följande data från en observationsperiod:

|  |  |
|---|---:|
| Tillgänglig tid, UT | 1 600 h |
| Sammanlagd förebyggande underhållstid (inklusive väntetid) | 400 h |
| Sammanlagd reparationstid | 100 h |
| Sammanlagd väntetid för AU | 50 h |
| Sammanlagd väntetid för FU | 20 h |
| Antal fel | 200 |
| Antal förebyggande underhållsåtgärder | 40 |


Beräkna följande mått baserat på kalendertid:

- Konstruktiv tillgänglighet $A_k$
- Materialtillgänglighet $A_m$
- Operativ tillgänglighet $A_o$


## Uppgift 4: Tillgänglighet för en asfalteringsmaskin

En asfalteringsmaskin har följande data från en observationsperiod:

|  |  |
|---|---:|
| Tillgänglig tid, UT | 7 952 h |
| Antal fel | 50 |
| Sammanlagd reparationstid | 400 h |
| Sammanlagd väntetid för AU | 100 h |
| Antal förebyggande underhållsåtgärder | 12 |
| Tid per förebyggande underhållsåtgärd | 4 h |
| Väntetid för FU | 0 h |


Beräkna följande mått baserat på kalendertid:

- Konstruktiv tillgänglighet $A_k$
- Materialtillgänglighet $A_m$
- Operativ tillgänglighet $A_o$


## Uppgift 5: Konstruktiv och operativ tillgänglighet

Ett system har följande data från en observationsperiod:

|  |  |
|---|---:|
| Drifttid, OT | 3 000 h |
| Sammanlagd reparationstid | 80 h |
| Sammanlagd väntetid för AU | 40 h |
| Antal fel | 10 |
| Antal förebyggande underhållsåtgärder | 10 |
| Sammanlagd förebyggande underhållstid | 30 h |


De angivna underhållsaktivteterna inträffar under krävd tid. Antag 0 h väntetid för FU. Beräkna följande mått:

- Konstruktiv tillgänglighet $A_k$
- Operativ tillgänglighet $A_o$


## Uppgift 6: Tillgänglighet från arbetsorderdata

En anläggning med kontinuerlig produktion togs i drift den 1 januari 2026 kl. 08.00. Tabellen visar samtliga underhållshändelser under observationsperioden.

| Händelse-ID | Typ | Anmält datum | Arbetet påbörjat | Arbetet slutfört |
|---:|:---:|:---|:---|:---|
| 1 | AU | 2026-01-03 08.00 | 2026-01-03 10.00 | 2026-01-03 12.00 |
| 2 | FU | 2026-01-05 08.00 | 2026-01-05 08.00 | 2026-01-05 12.00 |
| 3 | AU | 2026-01-07 12.00 | 2026-01-07 14.00 | 2026-01-07 18.00 |
| 4 | FU | 2026-01-09 08.00 | 2026-01-09 08.00 | 2026-01-09 10.00 |
| 5 | AU | 2026-01-11 10.00 | 2026-01-11 12.00 | 2026-01-11 16.00 |

### A: Planerad produktionstid

Den planerade produktionstiden är krävd tid. FU genomförs utanför krävd tid.

- Beräkna tid mellan fel (*time between failures, TBF*).

- Beräkna reparationstid och otillgänglig tid för varje AU.

- Beräkna MTBF, MRT och MDT för AU.

- Beräkna $A_k$ och $A_o$.


### B: Kalendertid

Vid den kalenderbaserade beräkningen ingår både AU och FU.

- Beräkna tid mellan fel (*time between failures, TBF*).

- Beräkna tid mellan underhållsåtgärder (*time between maintenance, TBM*).

- Beräkna reparationstid, aktiv underhållstid och otillgänglig tid för händelserna.

- Beräkna MTBF, MRT, MTBM, MAMT och MDT.

- Beräkna $A_k$, $A_m$ och $A_o$.
