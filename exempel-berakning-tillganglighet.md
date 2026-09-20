# Beräkningsexempel

Följande exempel visar hur tillgänglighetsmåtten kan beräknas steg för steg.

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

där antal underhållsaktiviteter $n_{M}=n_{Fail}+n_{PM}$

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

Nedan är data för fel och förebyggande underhåll för en anläggning med kontinuerlig produktion. Anläggningen driftsattes 2023-11-01 kl 08:00.

[a)](#uppgift-a) Beräkna $A_k$, $A_o$ baserat på planerad produktionstid, där planerad produktionstid är total tid minus de förebyggande underhållsstoppen.

[b)](#uppgift-b) Beräkna $A_k$, $A_m$, $A_o$ baserat på kalendertid


| HändelseID | Typ   | Anmält datum $(t_{failure, i})$| Anmält vidare       | Arbetet påbörjat    | Arbetet slutfört $(t_{restore, i})$ |
|:-----|:------|:--------------------|:--------------------|:--------------------|:--------------------|
| 1    | AU    | 2024-01-15 03:12:00 | 2024-01-15 06:45:00 | 2024-01-15 07:20:00 | 2024-01-15 08:40:00 |
| 3    | AU    | 2024-04-22 17:54:00 | 2024-04-22 19:10:00 | 2024-04-22 20:00:00 | 2024-04-22 23:15:00 |
| 4    | AU    | 2024-07-31 09:27:00 | 2024-07-31 10:05:00 | 2024-07-31 11:20:00 | 2024-07-31 14:50:00 |
| 6    | AU    | 2024-10-10 13:56:00 | 2024-10-10 14:53:00 | 2024-10-10 20:46:00 | 2024-10-11 04:45:00 |
| 7    | AU    | 2024-11-18 22:41:00 | 2024-11-18 23:30:00 | 2024-11-19 01:10:00 | 2024-11-19 03:20:00 |
| 8    | AU    | 2024-12-04 06:11:00 | 2024-12-04 06:41:00 | 2024-12-04 15:25:00 | 2024-12-04 22:37:00 |
| 9    | AU    | 2025-02-24 14:08:00 | 2025-02-24 14:55:00 | 2025-02-24 16:10:00 | 2025-02-24 19:40:00 |
| 11   | AU    | 2025-05-12 01:59:00 | 2025-05-12 02:39:00 | 2025-05-14 01:28:00 | 2025-05-14 11:19:00 |
| 12   | AU    | 2025-06-03 05:33:00 | 2025-06-03 08:20:00 | 2025-06-03 09:00:00 | 2025-06-03 11:45:00 |
| 14   | AU    | 2025-09-11 18:26:00 | 2025-09-11 20:10:00 | 2025-09-11 21:00:00 | 2025-09-12 00:55:00 |
| 15   | AU    | 2025-10-25 16:53:00 | 2025-10-25 17:40:00 | 2025-10-27 06:31:00 | 2025-10-27 09:00:00 |
| 16   | AU    | 2025-12-20 07:51:00 | 2025-12-20 08:40:00 | 2025-12-20 10:15:00 | 2025-12-20 13:05:00 |
| 18   | AU    | 2026-03-29 12:17:00 | 2026-03-29 13:05:00 | 2026-03-29 15:00:00 | 2026-03-29 17:40:00 |
| 19   | AU    | 2026-04-14 07:21:00 | 2026-04-14 08:18:00 | 2026-04-15 04:14:00 | 2026-04-15 09:34:00 |
| 20   | AU    | 2026-04-21 15:20:00 | 2026-04-21 15:59:00 | 2026-04-23 11:47:00 | 2026-04-23 20:45:00 |
| 21   | AU    | 2026-07-07 01:44:00 | 2026-07-07 04:20:00 | 2026-07-07 05:10:00 | 2026-07-07 07:05:00 |


| HändelseID | Typ   | Anmält datum        | Anmält vidare       | Arbetet påbörjat $(t_{PM\ start, i})$ | Arbetet slutfört $(t_{PM\ end, i})$ |
|:-----|:------|:--------------------|:--------------------|:--------------------|:--------------------|
| 2    | FU    | 2024-03-01 08:00:00 | 2024-03-01 08:00:00 | 2024-03-01 08:00:00 | 2024-03-02 08:00:00 |
| 5    | FU    | 2024-09-01 08:00:00 | 2024-09-01 08:00:00 | 2024-09-01 08:00:00 | 2024-09-02 08:00:00 |
| 10   | FU    | 2025-03-01 08:00:00 | 2025-03-01 08:00:00 | 2025-03-01 08:00:00 | 2025-03-02 08:00:00 |
| 13   | FU    | 2025-09-01 08:00:00 | 2025-09-01 08:00:00 | 2025-09-01 08:00:00 | 2025-09-02 08:00:00 |
| 17   | FU    | 2026-03-01 08:00:00 | 2026-03-01 08:00:00 | 2026-03-01 08:00:00 | 2026-03-02 08:00:00 |
| 22   | FU    | 2026-09-01 08:00:00 | 2026-09-01 08:00:00 | 2026-09-01 08:00:00 | 2026-09-02 08:00:00 |


### Uppgift a

#### Steg 1: Tider
Beräkna tid mellan fel samt reparationstid och nedtid (otillgänglig tid)
- **Tid mellan fel** är den tillgängliga tiden från föregående återställning till nästa fel där förebyggande underhåll som infaller under intervallet exkluderas
$$
TBF_i
=
\left(
t_{failure,i}
-
t_{restore,i-1}
\right)
-
\sum_j 
\max\left(
0,\,
\min(t_{PM\,end,j},t_{failure,i})
-
\max(t_{PM\,start,j},t_{restore,i-1})
\right)
\qquad t_{restore,0} = \text{2023-11-01 08:00}
$$
- **Reparationstid** är tidsintervallet mellan *Arbetet slutfört* och *Arbetet påbörjat*
- **Väntetid** är tidsintervallet mellan *Arbetet påbörjat* och *Anmält datum* 
- **Nedtid** är tidsintervallet mellan *Arbetet slutfört* och *Anmält datum*.

| HändelseID |   Tid mellan fel (TBF) [dygn] |   Reparationstid [h] |   Väntetid [h] |   Nedtid [h] |
|:-----|------------------------------:|---------------------:|---------------:|-------------:|
| 1    |                          74.8 |                  1.3 |            4.1 |          5.5 |
| 3    |                          97.4 |                  3.2 |            2.1 |          5.4 |
| 4    |                          99.4 |                  3.5 |            1.9 |          5.4 |
| 6    |                          70   |                  8   |            6.8 |         14.8 |
| 7    |                          38.7 |                  2.2 |            2.5 |          4.6 |
| 8    |                          15.1 |                  7.2 |            9.2 |         16.4 |
| 9    |                          81.6 |                  3.5 |            2   |          5.5 |
| 11   |                          75.3 |                  9.8 |           47.5 |         57.3 |
| 12   |                          19.8 |                  2.8 |            3.4 |          6.2 |
| 14   |                          99.3 |                  3.9 |            2.6 |          6.5 |
| 15   |                          43.7 |                  2.5 |           37.6 |         40.1 |
| 16   |                          54   |                  2.8 |            2.4 |          5.2 |
| 18   |                          98   |                  2.7 |            2.7 |          5.4 |
| 19   |                          15.6 |                  5.3 |           20.9 |         26.2 |
| 20   |                           6.2 |                  9   |           44.4 |         53.4 |
| 21   |                          74.2 |                  1.9 |            3.4 |          5.4 |

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
\mathrm{TBF_i} = t_{failure, i}-t_{restore, i-1} \quad \left(t_{restore, 0}=\text{2023-11-01 08:00}\right)
$$ 

- **Tid mellan underhåll** är 
$$
\mathrm{TBM_i} = t_{m, i}-t_{m\ restore, i-1} \quad \left(t_{m\ restore, 0}=\text{2023-11-01 08:00}\right)
$$ 

- **Aktiv underhållstid** (samma som reparationstid för AU) är tidsintervallet mellan *Arbetet slutfört* och *Arbetet påbörjat*.
- **Väntetid** är tidsintervallet mellan *Arbetet påbörjat* och *Anmält datum* 
- **Nedtid** är tidsintervallet mellan *Arbetet slutfört* och *Anmält datum*.

| HändelseID | Tid mellan fel (TBF) [dygn]   |   Tid mellan underhåll (TBM) [dygn] |   Aktiv underhållstid [h] |   Väntetid [h] |   Nedtid [h] |
|:-----|:------------------------------|------------------------------------:|--------------------------:|---------------:|-------------:|
| 1    | 74.8                          |                                74.8 |                       1.3 |            4.1 |          5.5 |
| 2    | -                             |                                46   |                      24   |            0   |         24   |
| 3    | 98.4                          |                                51.4 |                       3.2 |            2.1 |          5.4 |
| 4    | 99.4                          |                                99.4 |                       3.5 |            1.9 |          5.4 |
| 5    | -                             |                                31.7 |                      24   |            0   |         24   |
| 6    | 71.0                          |                                38.2 |                       8   |            6.8 |         14.8 |
| 7    | 38.7                          |                                38.7 |                       2.2 |            2.5 |          4.6 |
| 8    | 15.1                          |                                15.1 |                       7.2 |            9.2 |         16.4 |
| 9    | 81.6                          |                                81.6 |                       3.5 |            2   |          5.5 |
| 10   | -                             |                                 4.5 |                      24   |            0   |         24   |
| 11   | 76.3                          |                                70.7 |                       9.8 |           47.5 |         57.3 |
| 12   | 19.8                          |                                19.8 |                       2.8 |            3.4 |          6.2 |
| 13   | -                             |                                89.8 |                      24   |            0   |         24   |
| 14   | 100.3                         |                                 9.4 |                       3.9 |            2.6 |          6.5 |
| 15   | 43.7                          |                                43.7 |                       2.5 |           37.6 |         40.1 |
| 16   | 54.0                          |                                54   |                       2.8 |            2.4 |          5.2 |
| 17   | -                             |                                70.8 |                      24   |            0   |         24   |
| 18   | 99.0                          |                                27.2 |                       2.7 |            2.7 |          5.4 |
| 19   | 15.6                          |                                15.6 |                       5.3 |           20.9 |         26.2 |
| 20   | 6.2                           |                                 6.2 |                       9   |           44.4 |         53.4 |
| 21   | 74.2                          |                                74.2 |                       1.9 |            3.4 |          5.4 |
| 22   | -                             |                                56   |                      24   |            0   |         24   |


#### Steg 2: Konstruktiv tillgänglighet (Ak)
$$
MTBF = \frac{1}{16} \sum_{i=1}^{16} TBF_i = 1451.98 h
$$

$$
MRT = \frac{1}{16} \sum_{i=1}^{16} T_{R,i} = 4.35 h
$$

$$
A_k = \frac{MTBF}{MTBF+MRT}=\frac{1451.98}{1451.98+4.35} = 0.997
$$

**Svar:** Konstruktiv tillgänglighet $A_k = 99.7\%$

#### Steg 3: Materialtillgänglighet (Am)
$$
MTBM = \frac{1}{22} \sum_{i=1}^{22} TBM_i = 1111.67 h
$$

$$
MAMT = \frac{1}{22} \sum_{i=1}^{22} T_{M,i} = 9.71 h
$$

$$
A_m = \frac{MTBM}{MTBM+MAMT}=\frac{1111.67}{1111.67+9.71} = 0.991
$$

**Svar:** Materialtillgänglighet $A_m = 99.1\%$

#### Steg 4: Operativ tillgänglighet (Ao)

$$
MTBM = \frac{1}{22} \sum_{i=1}^{22} TBM_i = 1111.67 h
$$


$$
MDT = \frac{1}{22} \sum_{i=1}^{22} T_{Down,i} = 18.51 h
$$

$$
A_o = \frac{MTBM}{MTBM+MDT}=\frac{1111.67}{1111.67+18.51} = 0.984
$$

**Svar:** Operativ tillgänglighet $A_o = 98.4\%$
