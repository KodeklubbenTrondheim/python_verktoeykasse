## Beskrivelse

_Vanskelighetsgrad: Medium_

En for løkke kan brukes for å gå igjennom en liste med data.

## Oppgave 1

Her får du en liste med ti tall:

```python
tall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Kan du lage en løkke som går gjennom og summerer tallene?

Se på for i verktøykassen for hjelp.

Hint: når du ønsker å summere tall i en for loop så kan det være lurt å lage en startverdi tallene kan plusses på (`resultat = 0`).

<details>
  <summary>Klikk her for løsningsforslag</summary>

```python
tall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat = 0

for t in tall:
    resultat = resultat + t

print("Resultat er", resultat)
```

</details>

<br />

## Oppgave 2

Om du har fullført Oppgave 1 kan du bruke samme kode, men multiplisere tallene. Hvilke endringer må til for at koden skal fungere ordentlig?

<details>
  <summary>Klikk her for løsningsforslag</summary>

```python
tall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat = 1

for t in tall:
    resultat = resultat * t

print("Resultat er", resultat)
```

</details>
