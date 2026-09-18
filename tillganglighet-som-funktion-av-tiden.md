# Tillgänglighet som funktion av tiden

För en reparerbar enhet kan tillståndet vid tiden \(t\) beskrivas med indikatorfunktionen

$$
X(t)=
\begin{cases}
1, & \text{om enheten är funktionsduglig vid tiden }t,\\
0, & \text{om enheten är funktionsoduglig vid tiden }t.
\end{cases}
$$

Enheten växlar mellan funktionsdugliga och funktionsodugliga tillstånd. De efterföljande tillgängliga och otillgängliga tidsintervallen kan betecknas \(T_1,D_1,T_2,D_2,\ldots\).

## Punkttillgänglighet

Punkttillgängligheten \(A(t)\) är sannolikheten att enheten befinner sig i ett funktionsdugligt tillstånd vid tidpunkten \(t\):

$$
A(t)=P\{X(t)=1\}.
$$

Eftersom \(X(t)\) endast kan anta värdena 0 och 1 gäller

$$
\operatorname{E}[X(t)]
=
1\cdot P\{X(t)=1\}
+
0\cdot P\{X(t)=0\}
=
P\{X(t)=1\}.
$$

Punkttillgängligheten kan därför även skrivas som

$$
A(t)=\operatorname{E}[X(t)].
$$

Punkttillgänglighet används när det är relevant att bestämma sannolikheten för att enheten är funktionsduglig vid en bestämd tidpunkt.

## Intervalltillgänglighet

Den ackumulerade tillgängliga tiden från tiden \(0\) till tiden \(t\) definieras som

$$
U(t)=\int_0^t X(s)\,ds.
$$

Intervalltillgängligheten under tidsintervallet \([t_1,t_2]\) är den andel av intervallet då enheten är funktionsduglig:

$$
\widetilde{A}(t_1,t_2)
=
\frac{U(t_2)-U(t_1)}{t_2-t_1}.
$$

Intervalltillgängligheten är en slumpvariabel eftersom enhetens tillgängliga tid under intervallet beror på när fel och återställanden inträffar. För observerade data motsvarar den

$$
\widetilde{A}(t_1,t_2)
=
\frac{\text{Tillgänglig tid under }[t_1,t_2]}
{\text{Tillgänglig tid}+\text{Otillgänglig tid under }[t_1,t_2]}.
$$

## Genomsnittlig intervalltillgänglighet

Den genomsnittliga intervalltillgängligheten är väntevärdet av intervalltillgängligheten under \([t_1,t_2]\):

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

## Asymptotisk tillgänglighet

Den asymptotiska genomsnittliga intervalltillgängligheten är gränsvärdet för den genomsnittliga intervalltillgängligheten när observationsperiodens längd går mot oändligheten:

$$
A_\infty
=
\lim_{T\rightarrow\infty}A(0,T).
$$

För en alternerande reparationsprocess med ändliga medeltider för tillgängliga och otillgängliga perioder erhålls

$$
A_\infty
=
\frac{\operatorname{E}[T_{\mathrm{up}}]}
{\operatorname{E}[T_{\mathrm{up}}]
+
\operatorname{E}[T_{\mathrm{down}}]}.
$$

När de tillgängliga och otillgängliga perioderna representeras av motsvarande medeltider kan detta skrivas som

$$
A_\infty
=
\frac{\text{Medeltillgänglig tid}}
{\text{Medeltillgänglig tid}+\text{Medelotillgänglig tid}}.
$$

Uttryck som

$$
A_k=\frac{MTBF}{MTBF+MRT}
$$

och

$$
A_o=\frac{MTBM}{MTBM+MDT}
$$

beskriver således asymptotisk tillgänglighet, med olika avgränsningar av vilka tider och underhållshändelser som ingår. Kvoten av de faktiskt observerade tillgängliga och otillgängliga tiderna under en bestämd period beskriver däremot intervalltillgängligheten för den observerade perioden.
