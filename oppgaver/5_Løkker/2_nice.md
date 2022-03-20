## Beskrivelse

_Vanskelighetsgrad: Enkel / Medium_

En `while` loop kjører frem til en gitt påstand ikke lenger er sann.
Eksempelvis vil:

```python
x = 0
while(x < 3):
    print(x)
    x += 1
```

kjøre tre ganger før den hopper ut.

## Oppgave

Kan du skrive ferdig koden under så den printer `"Nice"` når brukeren har skrevet strengen `"Python"`, og fortsetter å spørre hvis ikke?

```python
favorittspråk = input("Hva er ditt favorittprogrammeringsspråk? ")
while favorittspråk != "python":
```

<details>
  <summary>Klikk her for løsningsforslag</summary>

```python
favorittspråk = input("Hva er ditt favorittprogrammeringsspråk? ")

while favorittspråk != "Python":
    favorittspråk = input("Hva er ditt favorittprogrammeringsspråk? ")

print("Nice")
```

</details>
