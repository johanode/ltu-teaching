# Tillgänglighet som funktion av tiden
Den matematiska beskrivningen på denna sida bygger på framställningen i Ben-Daya et al. (2016, avsnitt 7.4).[^BenDaya]

För en reparerbar enhet kan tillståndet vid tiden $t$ beskrivas med funktionen

$$
X(t)=
\begin{cases}
1, & \text{om enheten är funktionsduglig vid tiden }t,\\
0, & \text{om enheten är funktionsoduglig vid tiden }t.
\end{cases}
$$

Enheten växlar mellan funktionsdugliga (*up state*) och funktionsodugliga tillstånd (*down state*). De efterföljande tillgängliga tidsintervallen (*uptime*, UT) och otillgängliga tidsintervallen (*downtime*, DT) kan betecknas

$$
UT_1,DT_1,UT_2,DT_2,\ldots
$$

## Punkttillgänglighet

Punkttillgängligheten $A(t)$ är sannolikheten att enheten befinner sig i ett funktionsdugligt tillstånd vid tidpunkten $t$:

$$
A(t)=P\{X(t)=1\},
$$

Väntevärdet för $X(t)$ beskriver det genomsnittliga tillståndet om många likadana enheter observeras vid samma tidpunkt $t$. För en diskret variabel beräknas väntevärdet genom att varje möjligt utfall multipliceras med sin sannolikhet: 

$$
\operatorname{E}[X(t)]
=
\sum_{x\in\{0,1\}}
xP\{X(t)=x\}.
$$

Eftersom $X(t)$ endast kan anta värdena 0 och 1 gäller

$$
\operatorname{E}[X(t)]
=
1\cdot P\{X(t)=1\}
+
0\cdot P\{X(t)=0\}
=
P\{X(t)=1\},
$$

Värdet 1 bidrar alltså när enheten fungerar, medan värdet 0 inte bidrar när enheten är funktionsoduglig. Väntevärdet blir därför lika med sannolikheten att enheten fungerar vid tidpunkten $t$.

Punkttillgängligheten kan därmed även skrivas som

$$
A(t)=\operatorname{E}[X(t)].
$$

Punkttillgänglighet används när det är relevant att bestämma sannolikheten för att enheten är funktionsduglig vid en bestämd tidpunkt.

## Intervalltillgänglighet

Den ackumulerade tillgängliga tiden (*cumulative uptime*) från tiden $0$ till tiden $t$ definieras som

$$
U(t)=\int_0^t X(s)\,ds.
$$

Eftersom $X(s)=1$ när enheten fungerar och $X(s)=0$ när den inte fungerar summerar integralen all tillgänglig tid fram till tiden $t$.

Låt $UT[t_1,t_2]$ beteckna den sammanlagda tillgängliga tiden under intervallet $[t_1,t_2]$:

$$
UT[t_1,t_2]
=
U(t_2)-U(t_1).
$$

Den sammanlagda otillgängliga tiden under samma intervall betecknas $DT[t_1,t_2]$ och beräknas som intervallets totala längd minus den tillgängliga tiden:

$$
DT[t_1,t_2]
=
(t_2-t_1)-UT[t_1,t_2].
$$

Intervalltillgängligheten under tidsintervallet $[t_1,t_2]$ är den andel av intervallets totala längd som enheten är funktionsduglig:

$$
\widetilde{A}(t_1,t_2)
=
\frac{U(t_2)-U(t_1)}{t_2-t_1}.
$$

Intervalltillgängligheten är en stokastisk variabel eftersom det varierar när och hur länge enheten kan utföra krävd funktion under intervallet. För ett observerat tidsintervall beräknas den som

$$
\widetilde{A}(t_1,t_2)
=
\frac{UT[t_1,t_2]}{t_2-t_1}
=
\frac{UT[t_1,t_2]}
{UT[t_1,t_2]+DT[t_1,t_2]}.
$$

## Genomsnittlig intervalltillgänglighet

Den genomsnittliga intervalltillgängligheten är väntevärdet av intervalltillgängligheten under $[t_1,t_2]$:

$$
A(t_1,t_2)
=
\operatorname{E}\!\left[\widetilde{A}(t_1,t_2)\right]
=
\frac{\operatorname{E}[U(t_2)-U(t_1)]}{t_2-t_1}
=
\frac{\operatorname{E}[UT[t_1, t_2]]}{t_2-t_1}.
$$

Den genomsnittliga intervalltillgängligheten kan även beräknas som medelvärdet av punkttillgängligheten under intervallet:


$$
A(t_1,t_2)
=
\frac{1}{t_2-t_1}
\int_{t_1}^{t_2} A(t)\,dt.
$$

## Asymptotisk genomsnittlig intervalltillgänglighet

Den asymptotiska genomsnittliga intervalltillgängligheten är gränsvärdet för den genomsnittliga intervalltillgängligheten när observationsperiodens längd går mot oändligheten:

$$
A_\infty
=
\lim_{T\rightarrow\infty}A(0,T).
$$

Antag att cyklerna $(UT_i,DT_i)$ är oberoende och likafördelade mellan cyklerna samt har ändliga väntevärden. Den asymptotiska genomsnittliga intervalltillgängligheten ges då av

$$
A_\infty
=
\frac{\operatorname{E}[UT_i]}
{\operatorname{E}[UT_i]+\operatorname{E}[DT_i]}.
$$

Låt

$$
\overline{UT}=\operatorname{E}[UT_i]
\qquad\text{och}\qquad
\overline{DT}=\operatorname{E}[DT_i]
$$

beteckna medeltiden för de tillgängliga respektive otillgängliga tidsintervallen. Den asymptotiska tillgängligheten kan då skrivas som

$$
A_\infty
=
\frac{\overline{UT}}
{\overline{UT}+\overline{DT}}.
$$

Det finns flera definitioner av tillgänglighet beroende på vilka orsaker till otillgänglighet som inkluderas. Se även [Tre mått på tillgänglighet (Ak, Am, Ao)](berakning-tillganglighet.md#tre-mått-på-tillgänglighet-ak-am-ao).

Om samtliga relevanta orsaker till otillgänglighet inkluderas, såsom avhjälpande och förebyggande underhåll samt tillhörande väntetider, kan den asymptotiska genomsnittliga intervalltillgängligheten uttryckas som operativ tillgänglighet:

$$
A_o
=
\frac{MTBM}
{MTBM+MDT}
$$

där **MTBM** (*Mean Time Between Maintenance*) är medeltiden mellan underhållsåtgärder och **MDT** (*Mean Down Time*) är den genomsnittliga otillgängliga tiden per underhållsåtgärd.

Om endast fel och reparationstid inkluderas erhålls den konstruktiva tillgängligheten:

$$
A_k
=
\frac{MTBF}{MTBF+MRT}
$$

där **MTBF** (*Mean Time Between Failures*) är medeltiden mellan fel och **MRT** (*Mean Repair Time*) är medelreparationstiden.


[^BenDaya]: Ben-Daya, M., Kumar, U. & Murthy, D. N. P. (2016). *Introduction to Maintenance Engineering: Modelling, Optimization and Management*. John Wiley & Sons. https://doi.org/10.1002/9781118926581.
