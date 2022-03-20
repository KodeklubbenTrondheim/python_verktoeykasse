## Beskrivelse

_Vanskelighetsgrad: Vanskelig_

Å nei! Listen over alle dine favoritte varer er blitt helt blandet, og den neste handleturen kommer til å bli ganske ineffektiv.

Heldigvis er du en godt organisert person, og listen din ble skrevet med hjelpen av dictionary:

```python
handleliste = [
    {"kategori": "frukt", "vare": "Epler"},
    {"kategori": "frukt", "vare": "Bananer"},
    {"kategori": "grønnsaker", "vare": "Gulerøtter"},
    {"kategori": "frukt", "vare": "Pærer"},
    {"kategori": "daglig", "vare": "Tannkrem"},
    {"kategori": "media", "vare": "Dagsrevyen: Klassiske Øyeblikker"},
    {"kategori": "grønnsaker", "vare": "Poteter"},
    {"kategori": "daglig", "vare": "Tørkerulle"},
    {"kategori": "frukt", "vare": "Tomater"}
]
```

## Oppgave

Kan du skrive et program som tar inn flere kategorier og skriver ut bare de varene som tilhører kategoriene, i samme rekkefølge som kategoriene ble tilgitt?

Enten kan du bruke handleliste til øvers, ellers kan du lage din egen!

Programmet bør fungere som dette:

> _Gyldige kategorier: frukt, grønnsaker, daglig, media_
>
> _Hvilke kategorier vil du vise? Skill kategoriene med komma._
>
> daglig,media

Så printer programmet:

> daglig
>
> - Tannkrem
> - Tørkerulle
>
> media
>
> - Dagsrevyen: Klassiske Øyeblikker

<details>
  <summary>Klikk her for løsningsforslag</summary>

```python
handleliste = [
    {"kategori": "frukt", "navn": "Epler"},
    {"kategori": "frukt", "navn": "Bananer"},
    {"kategori": "grønnsaker", "navn": "Gulerøtter"},
    {"kategori": "frukt", "navn": "Pærer"},
    {"kategori": "daglig", "navn": "Tannkrem"},
    {"kategori": "media", "navn": "Dagsrevyen: Klassiske Øyeblikker"},
    {"kategori": "grønnsaker", "navn": "Poteter"},
    {"kategori": "daglig", "navn": "Tørkerulle"},
    {"kategori": "frukt", "navn": "Tomater"}
]

print("Gyldige kategorier: frukt, grønnsaker, daglig, media")

# Her bruker vi komma for å splitte varene.
# Men det er like gyldig å bruke løkker for å hente kategoriene.
kategorier = input("Hvilke kategorier vil du vise? Skill kategoriene med komma: ").split(",")

for kategori in kategorier:
    print("\n" + kategori)
    print("-----------------")
    for vare in handleliste:
        if vare["kategori"] == kategori:
            print(vare["navn"])
```

</details>
