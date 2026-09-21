# Lösningsförslag till räkneövningar i driftsäkerhet"

Tillhör [Räkneövningar i driftsäkerhet](rakneovningar-driftsakerhet.html).

## Sammanställning
   
| Uppgift | $A_k$ | $A_m$ | $A_o$ |
|---|---:|---:|---:|
| 1 | 90,9 % | – | – |
| 2 | 89,7 % | – | – |
| 3 | 95,2 % | 76,9 % | 74,4 % |
| 4 | 95,2 % | 94,7 % | 93,6 % |
| 5 | 97,4 % | – | 95,2 % |
| 6A | 95,8 % | – | 93,4 % |
| 6B | 95,9 % | 93,4 % | 91,1 % |

## Innehåll

1. [Konstruktiv tillgänglighet för en pump](#upg-1-konstruktiv-tillgänglighet-för-en-pump)
2. [Konstruktiv tillgänglighet baserad på drifttid](#upg-2-konstruktiv-tillgänglighet-baserad-på-drifttid)
3. [Tre mått på tillgänglighet för ett borraggregat](#upg-3-tre-mått-på-tillgänglighet-för-ett-borraggregat)
4. [Tillgänglighet för en asfalteringsmaskin](#upg-4-tillgänglighet-för-en-asfalteringsmaskin)
5. [Konstruktiv och operativ tillgänglighet](#upg-5-konstruktiv-och-operativ-tillgänglighet)
6. [Tillgänglighet från en arbetsorderdata](#upg-6-tillgänglighet-från-en-arbetsorderdata)
    - [A: Planerad produktionstid](#a-planerad-produktionstid)
    - [B: Kalendertid](#b-kalendertid)


## Upg 1: Konstruktiv tillgänglighet för en pump

Medelreparationstiden är

$$
MRT=\frac{RT}{n_{Fail}}=\frac{200}{100}=2\ \text{h}.
$$

Den konstruktiva tillgängligheten blir

$$
A_k
=\frac{MTBF}{MTBF+MRT}
=\frac{20}{20+2}
=0{,}909.
$$

**Svar:** $A_k=90{,}9\ \%$.

## Upg 2: Konstruktiv tillgänglighet baserad på drifttid

Medeltiden mellan fel baserat på drifttid är

$$
MTBF=\frac{OT}{n_{Fail}}=\frac{2600}{11}=236{,}36\ \text{h}.
$$

Medelreparationstiden är

$$
MRT=\frac{RT}{n_{Fail}}=\frac{300}{11}=27{,}27\ \text{h}.
$$

Den konstruktiva tillgängligheten blir

$$
A_k
=\frac{MTBF}{MTBF+MRT}
=\frac{236{,}36}{236{,}36+27{,}27}
=0{,}897.
$$

**Svar:** $A_k=89{,}7\ \%$.

Tiden för förebyggande underhåll behövs inte. Beräkningen är baserad på drifttid och konstruktiv tillgänglighet omfattar endast tiden mellan fel och reparationstiden.

## Upg 3: Tre mått på tillgänglighet för ett borraggregat

### Konstruktiv tillgänglighet
Det förebyggande underhållet (*preventive maintenance time*, PMT) genomförs under krävd tid och ingår därför i tiden mellan fel. 

$$
MTBF=\frac{UT+PMT}{n_{Fail}}=\frac{1600+400}{200}=10\ \text{h}
$$

$$
MRT=\frac{RT}{n_{Fail}}=\frac{100}{200}=0{,}5\ \text{h}
$$

$$
A_k
=\frac{MTBF}{MTBF+MRT}
=\frac{10}{10+0{,}5}
=0{,}952.
$$

**Svar:** $A_k=95{,}2\ \%$.

### Materialtillgänglighet

Antalet underhållsåtgärder är

$$
n_M=200+40=240.
$$

Den aktiva förebyggande underhållstiden (APMT) är

$$
APMT=400-20=380\ \text{h}.
$$

Det ger följande beräkning av materialtillgängligheten
$$
MTBM=\frac{UT}{n_M}=\frac{1600}{240}=6{,}67\ \text{h}
$$

$$
MAMT=\frac{RT+APMT}{n_M}=\frac{100+380}{240}=2{,}00\ \text{h}
$$

$$
A_m
=\frac{MTBM}{MTBM+MAMT}
=\frac{6{,}67}{6{,}67+2{,}00}
=0{,}769.
$$

**Svar:** $A_m=76{,}9\ \%$.

### Operativ tillgänglighet

Den sammanlagda otillgängliga tiden (DT) är

$$
DT=100+50+400=550\ \text{h}.
$$

Vilket ger följande beräkning av den operativa tillgängligheten
$$
MDT=\frac{DT}{n_M}=\frac{550}{240}=2{,}29\ \text{h}
$$

$$
A_o
=\frac{MTBM}{MTBM+MDT}
=\frac{6{,}67}{6{,}67+2{,}29}
=0{,}744.
$$

**Svar:** $A_o=74{,}4\ \%$.

## Upg 4: Tillgänglighet för en asfalteringsmaskin

### Konstruktiv tillgänglighet
Eftersom det förebyggande underhållet genomförs under krävd tid ingår det i beräkningen av tid mellan fel. Den sammanlagda tiden för förebyggande underhåll (PMT) är

$$
PMT = 12\cdot4=48\ \text{h}.
$$

Det ger följande beräkning av konstruktiv tillgänglighet
$$
MTBF=\frac{UT+PMT}{n_{Fail}}=\frac{7\,952+48}{50}=160\ \text{h}
$$

$$
MRT=8\ \text{h}
$$

$$
A_k
=\frac{MTBF}{MTBF+MRT}
=\frac{160}{160+8}
=0{,}952.
$$

**Svar:** $A_k=95{,}2\ \%$.


### Materialtillgänglighet

Antalet underhållsåtgärder är $n_M=50+12=62$ och medeltiden mellan underhåll blir
$$
MTBM=\frac{UT}{n_M}=\frac{7\,952}{62}=128{,}26\ \text{h}
$$

Total reparationstid är

$$
RT = MRT \cdot n_{Fail} = 8 \cdot 50 = 400 \text{h}
$$

och aktiv förebyggande underhållstid är

$$
APMT = MAPMT \cdot n_{PM} = (4-0) \cdot 12 = 48 \text{h}
$$

Det ger följande beräkning av materialtillgängligheten

$$
MAMT=\frac{RT+APMT}{n_M}=\frac{400+48}{62}=7{,}23\ \text{h}
$$

$$
A_m
=\frac{MTBM}{MTBM+MAMT}
=\frac{128{,}26}{128{,}26+7{,}23}
=0{,}947.
$$

**Svar:** $A_m=94{,}7\ \%$.

### Operativ tillgänglighet

Den sammanlagda avhjälpande underhållstiden (CMT) är

$$
CMT = (MRT + MWT_{CM}) \cdot n_{Fail} = 500\ \text{h}.
$$

Den sammanlagda otillgängliga tiden (DT) blir då

$$
DT = CMT + PMT = 500 + 48 = 548\ \text{h}.
$$

Beräkningen av operativ tillgänglighet blir

$$
MDT=\frac{DT}{n_M}=\frac{548}{62}=8{,}84\ \text{h}
$$

$$
A_o
=\frac{MTBM}{MTBM+MDT}
=\frac{128{,}26}{128{,}26+8{,}84}
=0{,}936.
$$

**Svar:** $A_o=93{,}6\ \%$.

## Upg 5: Konstruktiv och operativ tillgänglighet

Beräkningarna ska baseras på drifttid (OT). 

### Konstruktiv tillgänglighet

$$
MTBF=\frac{OT}{n_{Fail}}=\frac{3000}{10}=300\ \text{h}
$$

$$
MRT=\frac{RT}{n_{Fail}}=\frac{80}{10}=8\ \text{h}
$$

$$
A_k
=\frac{MTBF}{MTBF+MRT}
=\frac{300}{300+8}
=0{,}974.
$$

**Svar:** $A_k=97{,}4\ \%$.

Förebyggande underhåll och väntetid ingår inte i den konstruktiva tillgängligheten.

### Operativ tillgänglighet

Medeltid mellan underhåll är

$$
MTBM=\frac{OT}{n_M}=\frac{3000}{10+10}=150\ \text{h}
$$

Den sammanlagda otillgängliga tiden är

$$
DT = CMT + PMT = 120+30=150\ \text{h}.
$$

där den avhjälpande underhållstiden (CMT) fås från

$$
CMT = RT + MWT_{CM} \cdot n_{Fail} = 80 + 4 \cdot 10 = 120 \text{h}
$$

Beräkningen av operativ tillgänglighet blir då

$$
MDT=\frac{DT}{n_M}=\frac{150}{20}=7{,}5\ \text{h}
$$

$$
A_o
=\frac{MTBM}{MTBM+MDT}
=\frac{150}{150+7{,}5}
=0{,}952.
$$

**Svar:** $A_o=95{,}2\ \%$.

## Upg 6: Tillgänglighet från en arbetsorderdata

Anläggningen togs i drift den 1 januari 2026 kl. 08.00.

### A) Planerad produktionstid

FU genomförs utanför krävd tid. Tiden för FU ska därför dras bort från tiden mellan felen.

#### I) Tid mellan fel
| Händelse-ID | Tid från föregående återställning | FU under intervallet | Tid mellan fel $TBF_i$ |
|---:|---:|---:|---:|
| 1 | 48 h | 0 h | 48 h |
| 3 | 96 h | 4 h | 92 h |
| 5 | 88 h | 2 h | 86 h |
| **Summa** |  |  | **226 h** | 

#### II) Reparationstid och otillgänglig tid
| Händelse-ID | Reparationstid $T_{Rep,i}$ | Otillgänglig tid $DT_i$ |
|---:|---:|---:|
| 1 | 2 h | 4 h |
| 3 | 4 h | 6 h |
| 5 | 4 h | 6 h |
| **Summa** |  **10 h** | **16 h** |

#### III) Medeltider
Medeltiderna blir

$$
MTBF=\frac{\sum_i TBF_i}{n_{Fail}}=\frac{226}{3}=75{,}33\ \text{h}
$$

$$
MRT=\frac{\sum_i T_{Rep,i}}{n_{Fail}}=\frac{10}{3}=3{,}33\ \text{h}
$$

$$
MDT=\frac{\sum_i DT_i}{n_{Fail}}=\frac{16}{3}=5{,}33\ \text{h}.
$$

#### IV) Tillgänglighet
Den konstruktiva tillgängligheten är

$$
A_k
=\frac{MTBF}{MTBF+MRT}
=\frac{75{,}33}{75{,}33+3{,}33}
=0{,}958.
$$

**Svar:** $A_k=95{,}8\ \%$.

Eftersom inga andra underhållsåtgärder genomförs under krävd tid sätts $MTBM=MTBF$. 

Den operativa tillgängligheten är

$$
A_o
=\frac{MTBM}{MTBM+MDT}
=\frac{75{,}33}{75{,}33+5{,}33}
=0{,}934.
$$

**Svar:** $A_o=93{,}4\ \%$.

### B) Kalendertid

Vid den kalenderbaserade beräkningen ingår FU i tiden mellan fel.

#### I) Tid mellan fel

| Händelse-ID | Beräkning | Tid mellan fel $TBF_i$ |
|---:|---|---:|
| 1 | Driftsättning till fel ID=1 | 48 h |
| 3 | Återställning efter fel ID1 till fel ID=3 | 96 h |
| 5 | Återställning efter fel ID=3 till fel ID=5 | 88 h |
| **Summa** |  | **232 h** |

#### II) Tid mellan underhåll

| Händelse-ID | Typ | Tid mellan underhåll $TBM_i$ |
|---:|:---:|---:|
| 1 | AU | 48 h |
| 2 | FU | 44 h |
| 3 | AU | 48 h |
| 4 | FU | 38 h |
| 5 | AU | 48 h |
| **Summa** |  | **226 h** |

#### III) Reparationstid och otillgänglig tid
| Händelse-ID | Typ | Aktiv underhållstid $T_{AM,i}$ | Väntetid | Otillgänglig tid $DT_{i}$|
|---:|:---:|---:|---:|---:|
| 1 | AU | 2 h | 2 h | 4 h |
| 2 | FU | 4 h | 0 h | 4 h |
| 3 | AU | 4 h | 2 h | 6 h |
| 4 | FU | 2 h | 0 h | 2 h |
| 5 | AU | 4 h | 2 h | 6 h |
| **Summa** |  | **16 h** | **6 h** | **22 h** |

Reparationstiderna $T_{Rep,i}$ är således 2, 4 och 4 timmar.

#### IV) Medelvärden
$$
MTBF=\frac{\sum_i TBF_i}{n_{Fail}}=\frac{232}{3}=77{,}33\ \text{h}
$$

$$
MRT=\frac{\sum_i T_{Rep,i}}{n_{Fail}}=\frac{2+4+4}{3}=3{,}33\ \text{h}.
$$

$$
MTBM=\frac{\sum_i TBM_i}{n_M}=\frac{226}{5}=45{,}2\ \text{h}.
$$

$$
MAMT=\frac{\sum_i T_{AM,i}}{n_M}=\frac{16}{5}=3{,}2\ \text{h}
$$

$$
MDT=\frac{\sum_i DT_i}{n_M}=\frac{22}{5}=4{,}4\ \text{h}.
$$

#### V) Tillgänglighet

Den konstruktiva tillgängligheten är

$$
A_k
=\frac{MTBF}{MTBF+MRT}
=\frac{77{,}33}{77{,}33+3{,}33}
=0{,}959.
$$

**Svar:** $A_k=95{,}9\ \%$.

Materialtillgängligheten är

$$
A_m
=\frac{MTBM}{MTBM+MAMT}
=\frac{45{,}2}{45{,}2+3{,}2}
=0{,}934.
$$

**Svar:** $A_m=93{,}4\ \%$.

Den operativa tillgängligheten är

$$
A_o
=\frac{MTBM}{MTBM+MDT}
=\frac{45{,}2}{45{,}2+4{,}4}
=0{,}911.
$$

**Svar:** $A_o=91{,}1\ \%$.
