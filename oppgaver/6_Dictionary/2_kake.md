## Beskrivelse

En baker har følgende ingredienser i kjøleskapet:

- 10 egg
- 5 liter melk
- 2 kg smør
- 1 liter fløte.

Dette kan skrives i en dictionary slik:

```python
kjøleskap = {"egg": 10, "melk": 5, "smør": 2, "fløte": 1}
```

## Oppgave 1

_Vanskelighetsgrad: Vanskelig_

Han ønsker å bake en kake som krever 3 egg, 1 liter melk, 1 kg smør og 1 liter fløte. Skriv et program som oppdaterer verdiene i kjøleskapet etter kaken er bakt.

<details>
  <summary>Klikk her for løsningsforslag</summary>

```python
kjøleskap = {"egg": 10, "melk": 5, "smør": 2, "fløte": 1}

kjøleskap["egg"] = kjøleskap["egg"] - 3
kjøleskap["melk"] = kjøleskap["melk"] - 1
kjøleskap["smør"] = kjøleskap["smør"] - 1
kjøleskap["fløte"] = kjøleskap["fløte"] - 1

print("Etter at kaken ble bakt, inneholder nå kjøleskapet:", kjøleskap)
```

</details>

<br />

## Oppgave 2

_Vanskelighetsgrad: Vanskelig_

Endre tallene til noe større enn det bakeren har, finn en måte å fortelle ham at han må på butikken.

<details>
  <summary>Klikk her for løsningsforslag</summary>

```python
kjøleskap = {"egg": 10, "melk": 5, "smør": 2, "fløte": 1}

kjøleskap["egg"] = kjøleskap["egg"] - 10
kjøleskap["melk"] = kjøleskap["melk"] - 5
kjøleskap["smør"] = kjøleskap["smør"] - 1
kjøleskap["fløte"] = kjøleskap["fløte"] - 1

if kjøleskap["egg"] < 1:
    print("Kjøleskapet er tomt for egg! Du må på butikken!")

if kjøleskap["melk"] < 1:
    print("Kjøleskapet er tomt for melk! Du må på butikken!")

if kjøleskap["smør"] < 1:
    print("Kjøleskapet er tomt for smør! Du må på butikken!")

if kjøleskap["fløte"] < 1:
    print("Kjøleskapet er tomt for fløte! Du må på butikken!")
```

</details>
