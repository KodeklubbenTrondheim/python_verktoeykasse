## Beskrivelse

_Vanskelighetsgrad: Medium_

Du har fått en pirat på besøk! Dessverre sliter han med å fortså hva du sier. Du ønsker derfor å lage en for-løkke som kan gå igjennom en setning du skriver og oversetter den til piratspråk.

Piratspråk innebærer at alle konsonanter får en ending på o og konsonanten igjen. For eksempel blir strengen `"my name is bob"` til `"momy nonamome isos bobobob"`.

Her får du en streng med konsonanter:

```python
kons = "bcdfghjklmnpqrstvwxz"
```

## Oppgave

Kan du skrive et program som tar en streng fra brukeren og forvandler den til piratspråk?

<details>
  <summary>Klikk her for løsningsforslag</summary>

```python
setning  = input("Skriv inn en setning: ").lower()
kons = "bcdfghjklmnpqrstvwxz"

ny_streng = ""
for i in setning:
    if i in kons:
        ny_streng += i + "o"
    ny_streng += i

print(ny_streng)
```

</details>
