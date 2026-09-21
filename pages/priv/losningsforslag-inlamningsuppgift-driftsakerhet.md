# Lösningsförslag – inlämningsuppgift i driftsäkerhet

## 1 Tillgänglig tid

### a) Beräkning

Enheten är tillgänglig både när den är i drift och när den står i beredskap och kan tas i drift. Den tillgängliga tiden är därför

$$
UT = 170 + 10 = 180\ \text{h}.
$$

**Svar:** Den tillgängliga tiden är **180 timmar**.

Som kontroll kan den otillgängliga tiden beräknas från de registrerade underhållstiderna:

| Orsak till otillgänglighet | Beräkning | Sammanlagd tid |
|---|---:|---:|
| Reparation | $4\cdot 1$ h | 4 h |
| Väntetid vid avhjälpande underhåll | $4\cdot 2$ h | 8 h |
| Förebyggande underhåll | $2\cdot 3$ h | 6 h |
| Väntetid vid förebyggande underhåll | $2\cdot 1$ h | 2 h |
| **Summa otillgänglig tid** |  | **20 h** |

Den tillgängliga tiden kan då även beräknas som

$$
UT = 200 - 20 = 180\ \text{h}.
$$

### b) Skillnaden mellan driftstid och tillgänglig tid

Driftstiden är den tid då produktionslinjen faktiskt används. Tillgänglig tid omfattar även beredskapstid, eftersom linjen då är funktionsduglig och beredd att tas i drift. Därför är den tillgängliga tiden 180 timmar, trots att linjen endast var i drift under 170 timmar.

## 2 Vad ingår i tillgänglighetsmåtten?

I tabellen betyder *ingår* att tidskategorin räknas som otillgänglig tid i måttet.

| Tidskategori | $A_k$ | $A_m$ | $A_o$ |
|---|:---:|:---:|:---:|
| Reparationstid | Ingår | Ingår | Ingår |
| Väntetid vid avhjälpande underhåll | Ingår inte | Ingår inte | Ingår |
| Förebyggande underhåll | Ingår inte | Ingår | Ingår |
| Väntetid vid förebyggande underhåll | Ingår inte | Ingår inte | Ingår |

Den konstruktiva tillgängligheten $A_k$ beskriver enhetens inneboende förmåga och tar därför endast hänsyn till fel och den reparationstid som krävs för att återställa funktionen.

Materialtillgängligheten $A_m$ tar hänsyn till både avhjälpande och förebyggande underhåll, men inte till väntetider i samband med underhållet.

Den operativa tillgängligheten $A_o$ omfattar samtliga relevanta orsaker till otillgänglighet. Här ingår därför både avhjälpande och förebyggande underhåll samt tillhörande väntetider.

## 3 Beräkning av tillgänglighet

### 3.1 Konstruktiv tillgänglighet

Under perioden inträffade fyra fel. Medeltiden mellan fel blir

$$
MTBF = \frac{180+8}{4}=47\ \text{h}.
$$

Medelreparationstiden är given som

$$
MRT=1\ \text{h}.
$$

Den konstruktiva tillgängligheten blir

$$
A_k
=
\frac{MTBF}{MTBF+MRT}
=
\frac{47}{47+1}
=
0{,}979.
$$

**Svar:** $A_k=97{,}9\ \%$.

### 3.2 Materialtillgänglighet

Totalt genomfördes fyra avhjälpande och två förebyggande underhållsåtgärder. Medeltiden mellan underhållsåtgärder blir

$$
MTBM = \frac{180}{4+2}=30\ \text{h}.
$$

Den genomsnittliga underhållstiden per underhållsåtgärd blir

$$
MAMT = \frac{4\cdot 1+2\cdot 3}{4+2}=1{,}67\ \text{h}.
$$

Materialtillgängligheten blir

$$
A_m
=
\frac{MTBM}{MTBM+MAMT}
=
\frac{30}{30+1{,}67}
=
0{,}947.
$$

**Svar:** $A_m=94{,}7\ \%$.

### 3.3 Operativ tillgänglighet

Den sammanlagda otillgängliga tiden är 20 timmar. Den genomsnittliga otillgängliga tiden per underhållsåtgärd blir

$$
MDT = \frac{4\cdot (1+2)+2\cdot (3+1)}{4+2}=3{,}33\ \text{h}.
$$

Den operativa tillgängligheten blir

$$
A_o
=
\frac{MTBM}{MTBM+MDT}
=
\frac{30}{30+3{,}33}
=
0{,}900.
$$

**Svar:** $A_o=90{,}0\ \%$.

Detta stämmer även med andelen tillgänglig tid under den krävda tiden:

$$
A_o=\frac{180}{200}=0{,}900=90{,}0\ \%.
$$

### Sammanställning

| Tillgänglighetsmått | Resultat |
|---|---:|
| Konstruktiv tillgänglighet $A_k$ | 97,9 % |
| Materialtillgänglighet $A_m$ | 94,7 % |
| Operativ tillgänglighet $A_o$ | 90,0 % |

## 4 Tolkning

### 1. Varför får måtten olika värden?

Måtten får olika värden eftersom de omfattar olika orsaker till otillgänglighet. $A_k$ tar endast hänsyn till reparation efter fel. $A_m$ tar dessutom hänsyn till förebyggande underhåll. $A_o$ omfattar även väntetider och ger därför det lägsta värdet.

### 2. Vilket mått är mest relevant för produktionsledaren?

Den operativa tillgängligheten $A_o$ är mest relevant. Den visar hur stor andel av den krävda tiden som linjen faktiskt är funktionsduglig, oavsett varför den annars är otillgänglig. I detta fall är linjen tillgänglig under 90,0 % av den krävda tiden.

### 3. Vilken tidskategori visar störst förbättringspotential?

Väntetiden vid avhjälpande underhåll är den största enskilda tidskategorin. Den uppgår till

$$
4\cdot 2=8\ \text{h}.
$$

En möjlig åtgärd är att förbättra tillgången till underhållspersonal, reservdelar eller teknisk information så att reparationen kan påbörjas snabbare.

Om medelväntetiden vid avhjälpande underhåll exempelvis minskar från två till en timme minskar den sammanlagda väntetiden från åtta till fyra timmar. Den tillgängliga tiden ökar då från 180 till 184 timmar och den operativa tillgängligheten blir

$$
A_o=\frac{184}{200}=0{,}920=92{,}0\ \%.
$$

Andra förbättringsförslag kan också vara riktiga om de är relevanta och konsekvenserna för tillgängligheten förklaras.
