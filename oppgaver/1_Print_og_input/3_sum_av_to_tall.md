## Beskrivelse

_Vanskelighetsgrad: medium_

Når vi bruker input() henter vi inn en tekst, men hva om vi vil ha inn tall? Da kan vi bruke int()-funksjonen (eller float() om du vil ha med kommatall).
For eksmepel: hvis vi vil gjøre om teksten "10" til tallet 10, kan vi bruke `int("10")` og får `10`.

## Oppgave

Lag et program som printer ut summen av to tall som brukeren skriver inn:

```
tall1 = input(<skriv noe her>)
tall2 = input(<skriv noe her>)

<gjør noe med tall1 og tall2>

print(tall1 + tall2)
```

Du kan godt prøve å ikke bruke `int()` først og se hva som skjer! Hva får du hvis du tar `2+2`?

## Løsningsforslag

<details>
  <summary>Klikk her for løsningsforslag</summary>

```
# Tar inn begge tallene
tall1_streng = input("Tall 1: ")
tall2_streng = input("Tall 2: ")

# Tallene vi tar inn er fortsatt strenger, altså for eksempel "1". Men vi vil ha tallet 1. Da må vi gjøre om til tall med int()
tall1 = int(tall1_streng)
tall2 = int(tall2_streng)

# Printer til slutt summen av tallene
print(tall1 + tall2)
```
</details>
