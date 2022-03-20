## Beskrivelse

_Vanskelighetsgrad: Veldig vanskelig_

Nils har begynt med enda vanskeligere matteoppgaver og han trenger å regne på `+`, `-`, `*` og `/`. Han må nå tenke smart. Hva om han kunne skrevet inn `"1 + 2"` og så `3`, eller `"4 * 2"` og fått `8`?

For enkelhetsskyld kan du bruke denne koden, men du står fritt til å finne ut alt selv:

```python
regnestykke = input("Skriv inn regnestykket: ")
komponenter = regnestykke.split(" ")
tall1 = int(komponenter[0])
operator = komponenter[1]
tall2 = int(komponenter[2])

print("Regner ut:", tall1, operator, tall2)

if operator == "+":
  ...
elif operator == "-":
  ...
...

print("Svar:", svar)
```

## Løsningsforslag

<details>
  <summary>Klikk her for løsningsforslag</summary>

```python
regnestykke = input("Skriv inn regnestykket: ")
komponenter = regnestykke.split(" ")
tall1 = int(komponenter[0])
operator = komponenter[1]
tall2 = int(komponenter[2])

print("Regner ut:", tall1, operator, tall2)

if operator == "+":
  svar = tall1 + tall2
elif operator == "-":
  svar = tall1 - tall2
elif operator == "*":
  svar = tall1 * tall2
elif operator == "/":
  svar = tall1 / tall2

print("Svar:", svar)
```

</details>
