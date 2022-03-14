## Beskrivelse

_Vanskelighetsgrad: Medium_

Linda liker tall, og vil gjerne får vite om et tall er større enn et annet.

## Oppgave

Kan du skrive et program som tar to tall fra brukeren og forteller hvilket er større?

For eksempel, med tallene:

Tall A: `89`

Tall B: `35`

Skulle programmet ditt skrive ut: `"89 er større enn 35"`.
Husk å tenke om like tall!

## Løsningsforslag

<details>
  <summary>Klikk her for løsningsforslag</summary>

```python
tall1_streng = input("Hva er tall nummer ett? ")
tall2_streng = input("Hva er tall nummer to? ")

tall_1 = int(tall1_streng)
tall_2 = int(tall2_streng)

if tall_1 > tall_2:
    print(tall1_streng + ' er større enn ' + tall2_streng)
elif tall_2 > tall_1:
    print(tall2_streng + ' er større enn ' + tall1_streng)
else:
    print("Begge tall er like")
```
</details>
