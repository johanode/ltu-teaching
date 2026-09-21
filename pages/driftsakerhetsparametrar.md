# Statistisk beskrivning av driftsäkerhetsparametrar

Tider mellan fel, reparationstider och väntetider kan betraktas som slumpvariabler. Parametrar som MTBF och MRT är då väntevärden för motsvarande slumpmässiga tider.

## Slumpmässiga tider och väntevärden

För en icke-negativ slumpvariabel $T$ med täthetsfunktion $f_T(t)$ gäller

$$
\operatorname{E}[T]
=
\int_0^\infty t f_T(t)\,dt.
$$

Väntevärdet kan också uttryckas med hjälp av sannolikheten att tiden överstiger $t$:

$$
\operatorname{E}[T]
=
\int_0^\infty P(T>t)\,dt.
$$

Vilken sannolikhetsfördelning som är lämplig beror på vilken typ av tid som studeras och på det observerade datamaterialet.

## Tid mellan fel

Låt $T_{\mathrm{BF}}$ beteckna tiden mellan fel. MTBF definieras som

$$
\mathrm{MTBF}
=
\operatorname{E}[T_{\mathrm{BF}}].
$$

Om $f_{\mathrm{BF}}(t)$ är täthetsfunktionen för tiden mellan fel och

$$
R(t)
=
P(T_{\mathrm{BF}}>t)
$$

är *reliability function* (också överlevnadsfunktionen / *survival function*), kan MTBF skrivas som

$$
\mathrm{MTBF}
=
\int_0^\infty t f_{\mathrm{BF}}(t)\,dt
=
\int_0^\infty R(t)\,dt.
$$

Om tiden mellan fel är exponentialfördelad med felbenägenhet $\lambda$ gäller

$$
\mathrm{MTBF}
=
\frac{1}{\lambda}.
$$

Om tiden mellan fel är Weibullfördelad med skalparameter $\alpha$ och formparameter $\beta$ gäller

$$
\mathrm{MTBF}
=
\alpha\,
\Gamma\!\left(1+\frac{1}{\beta}\right).
$$

## Reparationstid

Låt $T_{\mathrm{Rep}}$ beteckna reparationstiden. MRT definieras som

$$
\mathrm{MRT}
=
\operatorname{E}[T_{\mathrm{Rep}}].
$$

Om $f_{\mathrm{Rep}}(t)$ är reparationstidens täthetsfunktion gäller

$$
\mathrm{MRT}
=
\int_0^\infty t f_{\mathrm{Rep}}(t)\,dt.
$$

Om $M(t)$ betecknar reparationstidens fördelningsfunktion

$$
M(t)
=
P(T_{\mathrm{Rep}}\leq t),
$$

det vill säga sannolikheten att reparationen har slutförts inom tiden $t$. MRT kan då även skrivas som

$$
\mathrm{MRT}
=
\int_0^\infty [1-M(t)]\,dt.
$$

Reparationstider är positiva och kan vara högerskeva. Lognormalfördelningen är därför en vanligt förekommande modell för reparationstider, men valet av fördelning behöver prövas mot observerade data.

Om

$$
\ln T_{\mathrm{Rep}}
\sim
N(\mu,\sigma^2),
$$

är reparationstiden lognormalfördelad och

$$
\mathrm{MRT}
=
\exp\!\left(\mu+\frac{\sigma^2}{2}\right).
$$

Medianen är i detta fall

$$
\operatorname{median}(T_{\mathrm{Rep}})
=
\exp(\mu),
$$

vilket innebär att MRT normalt är större än medianreparationstiden när fördelningen är högerskev.

## Övriga driftsäkerhetsparametrar

På motsvarande sätt kan övriga parametrar definieras som väntevärden:

$$
\mathrm{MTBM}
=
\operatorname{E}[T_{\mathrm{M}}],
$$

$$
\mathrm{MAMT}
=
\operatorname{E}[T_{\mathrm{AM}}],
$$

$$
\mathrm{MDT}
=
\operatorname{E}[T_{\mathrm{D}}],
$$

och

$$
\mathrm{MWT}
=
\operatorname{E}[T_{\mathrm{Wait}}].
$$

Om den otillgängliga tiden för varje underhållsåtgärd kan delas upp enligt

$$
T_{\mathrm{D}}
=
T_{\mathrm{AM}}
+
T_{\mathrm{Wait}},
$$

ger väntevärdets linearitet

$$
\mathrm{MDT}
=
\mathrm{MAMT}
+
\mathrm{MWT}.
$$

Detta samband kräver inte att den aktiva underhållstiden och väntetiden är statistiskt oberoende. Det förutsätter däremot att tiderna avser samma population av underhållsåtgärder och samma avgränsning av den otillgängliga tiden.

## Skattning från observerade data

Om $T_1,T_2,\ldots,T_n$ är observerade tider kan väntevärdet skattas med det aritmetiska medelvärdet:

$$
\widehat{\operatorname{E}[T]}
=
\frac{1}{n}\sum_{i=1}^n T_i.
$$

Exempelvis skattas MTBF och MRT som

$$
\widehat{\mathrm{MTBF}}
=
\frac{1}{n_{\mathrm{Fail}}}
\sum_{i=1}^{n_{\mathrm{Fail}}}T_{\mathrm{BF},i}
$$

och

$$
\widehat{\mathrm{MRT}}
=
\frac{1}{n_{\mathrm{Fail}}}
\sum_{i=1}^{n_{\mathrm{Fail}}}T_{\mathrm{Rep},i}.
$$

Det aritmetiska medelvärdet är en direkt skattning när observationerna utgör fullständigt observerade och jämförbara tidsintervall. Om observationsperioden avslutas innan ett fel eller en reparation har inträffat är observationen censurerad. Då kan metoder för livslängds- och tillförlitlighetsanalys behöva användas i stället för att enbart beräkna medelvärdet av de fullständiga observationerna.
