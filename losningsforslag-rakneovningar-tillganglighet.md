# Lösningsförslag till räkneövningar i driftsäkerhet

Tillhör [Räkneövningar i driftsäkerhet](rakneovningar-driftsakerhet.md).


## Uppgift 1 Konstruktiv tillgänglighet för en pump

Medelreparationstiden är

$$
MRT=\frac{\sum T_{Rep}}{n_{Fail}}=\frac{200}{100}=2\ \text{h}.
$$

Den konstruktiva tillgängligheten blir

$$
A_k
=\frac{MTBF}{MTBF+MRT}
=\frac{20}{20+2}
=0{,}909.
$$

**Svar:** $A_k=90{,}9\ \%$.

## Uppgift 2 Konstruktiv tillgänglighet baserad på drifttid

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

## Uppgift 3 Tre mått på tillgänglighet för ett borraggregat

### Konstruktiv tillgänglighet
Det förebyggande underhållet (*preventive maintenance time*, PMT) genomförs under krävd tid och ingår därför i tiden mellan fel. 

$$
MTBF=\frac{UT+PMT}}{n_{Fail}}=\frac{1600+400}{200}=10\ \text{h}
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

## Uppgift 4 Tillgänglighet för en asfalteringsmaskin

Den sammanlagda tiden för förebyggande underhåll är

$$
12\cdot4=48\ \text{h}.
$$

Antalet underhållsåtgärder är

$$
n_M=50+12=62.
$$

### Konstruktiv tillgänglighet

Eftersom det förebyggande underhållet genomförs under krävd tid ingår de 48 timmarna i tiden mellan fel.

$$
MTBF=\frac{7\,952+48}{50}=160\ \text{h}
$$

$$
MRT=\frac{400}{50}=8\ \text{h}
$$

$$
A_k
=\frac{160}{160+8}
=0{,}952.
$$

**Svar:** $A_k=95{,}2\ \%$.

### Materialtillgänglighet

$$
MTBM=\frac{7\,952}{62}=128{,}26\ \text{h}
$$

$$
MAMT=\frac{400+48}{62}=7{,}23\ \text{h}
$$

$$
A_m
=\frac{128{,}26}{128{,}26+7{,}23}
=0{,}947.
$$

**Svar:** $A_m=94{,}7\ \%$.

### Operativ tillgänglighet

Den sammanlagda otillgängliga tiden är

$$
400+100+48=548\ \text{h}.
$$

$$
MDT=\frac{548}{62}=8{,}84\ \text{h}
$$

$$
A_o
=\frac{128{,}26}{128{,}26+8{,}84}
=0{,}936.
$$

**Svar:** $A_o=93{,}6\ \%$.

## Uppgift 5 Konstruktiv och operativ tillgänglighet

Beräkningarna ska baseras på drifttid. Antalet underhållsåtgärder är

$$
n_M=10+10=20.
$$

### Konstruktiv tillgänglighet

$$
MTBF=\frac{3\,000}{10}=300\ \text{h}
$$

$$
MRT=\frac{80}{10}=8\ \text{h}
$$

$$
A_k
=\frac{300}{300+8}
=0{,}974.
$$

**Svar:** $A_k=97{,}4\ \%$.

Förebyggande underhåll och väntetid ingår inte i den konstruktiva tillgängligheten.

### Operativ tillgänglighet

$$
MTBM=\frac{3\,000}{20}=150\ \text{h}
$$

Den sammanlagda otillgängliga tiden är

$$
80+40+30=150\ \text{h}.
$$

$$
MDT=\frac{150}{20}=7{,}5\ \text{h}
$$

$$
A_o
=\frac{150}{150+7{,}5}
=0{,}952.
$$

**Svar:** $A_o=95{,}2\ \%$.

## Uppgift 6 Tillgänglighet från en händelselogg

Anläggningen togs i drift den 1 januari 2026 kl. 08.00.

### a) Planerad produktionstid

FU genomförs utanför krävd tid. Tiden för FU ska därför dras bort från tiden mellan felen.

| Händelse-ID | Tid från föregående återställning | FU under intervallet | Tid mellan fel | Reparationstid | Otillgänglig tid |
|---:|---:|---:|---:|---:|---:|
| 1 | 48 h | 0 h | 48 h | 2 h | 4 h |
| 3 | 96 h | 4 h | 92 h | 4 h | 6 h |
| 5 | 88 h | 2 h | 86 h | 4 h | 6 h |
| **Summa** |  |  | **226 h** | **10 h** | **16 h** |

Medeltiderna blir

$$
MTBF=\frac{226}{3}=75{,}33\ \text{h}
$$

$$
MRT=\frac{10}{3}=3{,}33\ \text{h}
$$

$$
MDT=\frac{16}{3}=5{,}33\ \text{h}.
$$

Den konstruktiva tillgängligheten är

$$
A_k
=\frac{75{,}33}{75{,}33+3{,}33}
=0{,}958.
$$

**Svar:** $A_k=95{,}8\ \%$.

Eftersom inga andra underhållsåtgärder genomförs under krävd tid sätts $MTBM=MTBF$.

$$
A_o
=\frac{75{,}33}{75{,}33+5{,}33}
=0{,}934.
$$

**Svar:** $A_o=93{,}4\ \%$.

### b) Kalendertid

Vid den kalenderbaserade beräkningen ingår FU i tiden mellan fel.

#### Tid mellan fel

| Händelse-ID | Beräkning | Tid mellan fel |
|---:|---|---:|
| 1 | Driftsättning till fel 1 | 48 h |
| 3 | Återställning efter fel 1 till fel 3 | 96 h |
| 5 | Återställning efter fel 3 till fel 5 | 88 h |
| **Summa** |  | **232 h** |

$$
MTBF=\frac{232}{3}=77{,}33\ \text{h}
$$

Reparationstiderna för AU är 2, 4 och 4 timmar. Därför blir

$$
MRT=\frac{2+4+4}{3}=3{,}33\ \text{h}.
$$

$$
A_k
=\frac{77{,}33}{77{,}33+3{,}33}
=0{,}959.
$$

**Svar:** $A_k=95{,}9\ \%$.

#### Tid mellan underhåll

| Händelse-ID | Typ | Från föregående återställning till nästa anmälan |
|---:|:---:|---:|
| 1 | AU | 48 h |
| 2 | FU | 44 h |
| 3 | AU | 48 h |
| 4 | FU | 38 h |
| 5 | AU | 48 h |
| **Summa** |  | **226 h** |

$$
MTBM=\frac{226}{5}=45{,}2\ \text{h}.
$$

#### Underhållstider

| Händelse-ID | Typ | Aktiv underhållstid | Väntetid | Otillgänglig tid |
|---:|:---:|---:|---:|---:|
| 1 | AU | 2 h | 2 h | 4 h |
| 2 | FU | 4 h | 0 h | 4 h |
| 3 | AU | 4 h | 2 h | 6 h |
| 4 | FU | 2 h | 0 h | 2 h |
| 5 | AU | 4 h | 2 h | 6 h |
| **Summa** |  | **16 h** | **6 h** | **22 h** |

$$
MAMT=\frac{16}{5}=3{,}2\ \text{h}
$$

$$
MDT=\frac{22}{5}=4{,}4\ \text{h}.
$$

Materialtillgängligheten är

$$
A_m
=\frac{45{,}2}{45{,}2+3{,}2}
=0{,}934.
$$

**Svar:** $A_m=93{,}4\ \%$.

Den operativa tillgängligheten är

$$
A_o
=\frac{45{,}2}{45{,}2+4{,}4}
=0{,}911.
$$

**Svar:** $A_o=91{,}1\ \%$.

## Sammanställning

| Uppgift | $A_k$ | $A_m$ | $A_o$ |
|---|---:|---:|---:|
| 1 | 90,9 % | – | – |
| 2 | 89,7 % | – | – |
| 3 | 95,2 % | 76,9 % | 74,4 % |
| 4 | 95,2 % | 94,7 % | 93,6 % |
| 5 | 97,4 % | – | 95,2 % |
| 6a | 95,8 % | – | 93,4 % |
| 6b | 95,9 % | 93,4 % | 91,1 % |
