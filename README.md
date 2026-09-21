# Driftsäkerhet och underhåll

Detta projekt innehåller ett grundläggande undervisningsmaterial om driftsäkerhet och underhåll. Materialet är skapat med [Quarto](https://quarto.org/) och publiceras som HTML och PDF.

## Innehåll

Materialet behandlar:

- driftsäkerhet och RAMS
- tillgänglighet
- funktionssäkerhet och grundläggande tillförlitlighetsanalys
- systemtillförlitlighet
- centrala formler för drift och underhåll

## Projektets filer

- `index.qmd` – startsida
- `rams.qmd` – driftsäkerhet och RAMS
- `tillganglighet.qmd` – beräkning av tillgänglighet
- `tillforlitlighet.qmd` – funktionssäkerhet och tillförlitlighetsanalys
- `formelsamling.qmd` – formelsamling
- `references.qmd` – referenslista
- `references.bib` – bibliografiska uppgifter
- `_quarto.yml` – projektets konfiguration

## Förhandsgranska lokalt

Installera [Quarto](https://quarto.org/docs/get-started/) och kör följande kommando i projektmappen:

```bash
quarto preview
```

## Rendera materialet

```bash
quarto render
```

## Publicera på GitHub Pages

```bash
quarto publish gh-pages
```

Den publicerade webbplatsen finns på:

<https://johanode.github.io/ltu-teaching/>
