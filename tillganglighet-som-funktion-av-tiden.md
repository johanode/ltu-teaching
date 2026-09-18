# Tillgänglighet som funktion av tiden
Matematiska beskrivningen på denna sida bygger på framställningen i Ben-Daya et al. (2016, avsnitt 7.4).[^BenDaya]

För en reparerbar enhet kan tillståndet vid tiden \(t\) beskrivas med indikatorfunktionen

$$
X(t)=
\begin{cases}
1, & \text{om enheten är funktionsduglig vid tiden }t,\\
0, & \text{om enheten är funktionsoduglig vid tiden }t.
\end{cases}
$$

Enheten växlar mellan funktionsdugliga och funktionsodugliga tillstånd. De efterföljande tillgängliga tidsintervallen (*uptime*, UT) och otillgängliga tidsintervallen (*downtime*, DT) kan betecknas

$$
UT_1,DT_1,UT_2,DT_2,\ldots
$$

## Punkttillgänglighet

Punkttillgängligheten \(A(t)\) är sannolikheten att enheten befinner sig i ett funktionsdugligt tillstånd vid tidpunkten \(t\):

$$
A(t)=P\{X(t)=1\},
$$

där \(P\{\cdot\}\) betecknar sannolikheten för en händelse.

Eftersom \(X(t)\) endast kan anta värdena 0 och 1 gäller

$$
\operatorname{E}[X(t)]
=
1\cdot P\{X(t)=1\}
+
0\cdot P\{X(t)=0\}
=
P\{X(t)=1\},
$$

där \(\operatorname{E}[\cdot]\) betecknar väntevärdet.

Punkttillgängligheten kan därför även skrivas som

$$
A(t)=\operatorname{E}[X(t)].
$$

Punkttillgänglighet används när det är relevant att bestämma sannolikheten för att enheten är funktionsduglig vid en bestämd tidpunkt.

## Intervalltillgänglighet

Den ackumulerade tillgängliga tiden (*cumulative uptime*) från tiden \(0\) till tiden \(t\) definieras som

$$
U(t)=\int_0^t X(s)\,ds.
$$

Låt \(UT[t_1,t_2]\) beteckna den sammanlagda tillgängliga tiden under intervallet $[t_1,t_2]$:

$$
UT[t_1,t_2]
=
U(t_2)-U(t_1).
$$

Den sammanlagda otillgängliga tiden under samma intervall betecknas \(DT[t_1,t_2]\) och ges av

$$
DT[t_1,t_2]
=
(t_2-t_1)-UT[t_1,t_2].
$$

Intervalltillgängligheten under tidsintervallet $[t_1,t_2]$ är den andel av intervallet då enheten är funktionsduglig:

$$
\widetilde{A}(t_1,t_2)
=
\frac{U(t_2)-U(t_1)}{t_2-t_1}.
$$

Intervalltillgängligheten är en slumpvariabel eftersom enhetens tillgängliga tid under intervallet beror på när fel och när funktionen återställs. För observerade data kan den skrivas som

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
\frac{\operatorname{E}[U(t_2)-U(t_1)]}{t_2-t_1}.
$$

Den kan även uttryckas med hjälp av punkttillgängligheten:

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

Antag att de efterföljande cyklerna av tillgängliga tidsintervall \(UT_i\) och otillgängliga tidsintervall \(DT_i\) är oberoende och likafördelade samt har ändliga väntevärden. Den asymptotiska genomsnittliga intervalltillgängligheten ges då av

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

beteckna medeltiden för de tillgängliga respektive otillgängliga tidsintervallen. Då kan den asymptotiska tillgängligheten skrivas som

$$
A_\infty
=
\frac{\overline{UT}}
{\overline{UT}+\overline{DT}}.
$$

Den asymptotiska genomsnittliga intervalltillgängligheten kan uttryckas med olika medeltider beroende på vilka orsaker till otillgänglighet som inkluderas, se också [Tre mått på tillgänglighet (Ak, Am, Ao)](berakning-tillganglighet.md#tre-mått-på-tillgänglighet-ak-am-ao). Konstruktiv och operativ tillgänglighet är två mått som bygger på denna princip men har olika avgränsningar.
Den konstruktiva tillgängligheten beräknas enligt

$$
A_k=\frac{MTBF}{MTBF+MRT},
$$

där \(MTBF\) (*Mean Time Between Failures*) är medeltiden mellan fel och \(MRT\) (*Mean Repair Time*) är medelreparationstiden.

Den operativa tillgängligheten beräknas enligt

$$
A_o=\frac{MTBM}{MTBM+MDT},
$$

där \(MTBM\) (*Mean Time Between Maintenance*) är medeltiden mellan underhållsåtgärder och \(MDT\) (*Mean Down Time*) är den genomsnittliga otillgängliga tiden per underhållsåtgärd.

Båda måtten beskriver således asymptotisk genomsnittlig intervalltillgänglighet, men med olika avgränsningar av vilka tider och underhållshändelser som ingår.

[^BenDaya]: Ben-Daya, M., Kumar, U. & Murthy, D. N. P. (2016). *Introduction to Maintenance Engineering: Modelling, Optimization and Management*. John Wiley & Sons. https://doi.org/10.1002/9781118926581.
