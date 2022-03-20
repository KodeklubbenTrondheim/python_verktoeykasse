## Beskrivelse

_Vanskelighetsgrad: Enkel_

Laiba klarer ikke å få nok av kuer, derfor ønsker hun å lage en funskjon som vil printe en ku om den blir kalt. Se på tidligere oppgaver og verktøykassen for hjelp.

## Oppgave

Skriv et program som tar et tall fra brukeren og printer så mange kuer.

For eksempel, hvis brukeren skriver `3`, bør tre kuer bli printet.

<details>
  <summary>Klikk her for løsningsforslag</summary>

```python
def print_ku():
    print('^__^')
    print('(oo)\_______')
    print('(__)\       )')
    print('    ||----W |')
    print('    ||     ||')

antall = int(input("Hvor mange kuer vil du ha?" ))

for i in range(0, antall):
    print_ku()
```

</details>
