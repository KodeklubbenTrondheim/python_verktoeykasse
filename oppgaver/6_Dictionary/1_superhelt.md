## Beskrivelse

Alle i Norge er glad i superhelter! Gjennom denne oppgaven skal vi bruke dictionary for å utforske superheltenes verden.

Sjekk verktøykassen for en oversikt over og hjelp med dictionary!

## Oppgave 1

_Vanskelighetsgrad: Enkel_

Vi ønsker å ha en oversikt over navnet til superhelter. Lag først en dictionary som inneholder følgende nøkkel og verdi-par:

- Batman -> Bruce Wayne
- Wonder woman -> Diana Prince
- Black Widow -> Natasha Romanoff
- Spider-man -> Peter Parker

<details>
  <summary>Klikk her for løsningsforslag</summary>

```python
superhelter = {
    "Black panther": "T'Challa",
    "Wonder woman": "Diana Prince",
    "Black Widow": "Natasha Romanoff",
    "Batman": "Bruce Wayne"
}
```

</details>

<br />

## Oppgave 2

_Vanskelighetsgrad: Enkel_

Nå ønsker vi å ta inn en superhelt fra brukeren (bruk `input`), for eksempel `"Batman"`. Hent så ut navnet til superhelten, og print navnet.

<details>
  <summary>Klikk her for løsningsforslag</summary>

```python
navn = input("Skriv navn på superhelten: ")

superhelt = superhelter[navn]

print(superhelt)
```

</details>

<br />

## Oppgave 3

_Vanskelighetsgrad: Medium_

Det er lett å skrive navnet til superheltene feil. Skriv kode som sjekker at det er en gyldig nøkkel som blir skrevet inn.

<details>
  <summary>Klikk her for løsningsforslag</summary>

```python
navn = input("Skriv navn på superhelten: ")

# Enten:
if navn in superhelter: # defaults to .keys()
    print("Du har skrevet feil navn.")
    return

# Eller
if navn != "Black panther" and navn != ...:
    print("Du har skrevet feil navn.")
    return

superhelt = superhelter[navn]

print(superhelt)
```

</details>
