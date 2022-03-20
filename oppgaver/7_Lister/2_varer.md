## Beskrivelse

_Vanskelighetsgrad: Medium_

Kan du lage et program som danner en liste fra brukernes inputter og skriver den ut?

For eksempel:

```python
Hvor mange varer vil du legge til? 2
Hva er vare 1? "Epler"
Hva er vare 2? "Dataspill"

Her er listen din: ["Epler", "Dataspill"]
```

<details>
  <summary>Klikk her for løsningsforslag</summary>

```python
antall_varer = int(input("Hvor mange varer vil du legge til? "))
varer = []

for i in range(0, antall_varer):
    vare = input("Hva er vare #" + str(i + 1) + " ?")
    varer.append(vare)

print("Her er listen din:", varer)
```

</details>
