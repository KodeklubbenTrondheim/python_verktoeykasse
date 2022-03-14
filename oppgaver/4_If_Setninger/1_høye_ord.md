## Beskrivelse

_Vanskelighetsgrad: Enkel_

Det er greit å vite om noen snakker for høyt! Hvis noen skriver en setning som BARE ER I STORE BOKSTAVER, kan vi være sikkert at den er for høyt.

## Oppgave

Kan du skrive et program som tar en setning fra brukeren og skriver ut om den er for høy? For eksempel:

`"HALLO JEG STÅR UTENFOR"`
Skrives ut `"Denne setningen er høy"`, mens:

`"Hei, jeg står utenfor"`
Skrives ut `"Denne setningen er stille"`

## Løsningsforslag

<details>
  <summary>Klikk her for løsningsforslag</summary>

```
setning = input("Hva er setningen din? ")

if setning.upper() == setning:
    print("Denne setningen er høy")
else:
    print("Denne setningen er stille")
```
</details>
