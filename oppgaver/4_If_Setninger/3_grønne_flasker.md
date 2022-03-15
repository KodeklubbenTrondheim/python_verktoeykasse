## Beskrivelse

_Vanskelighetsgrad: Vanskelig_

Arne synes det er hyggelig å høre på musikk. En av sine favoritte sanger er "Ti grønne flasker". Den høres ut som:

```python
"Ti grønne flasker sitter fast på veggen"
"Ti grønne flasker sitter fast på veggen"
"Og hvis et grønt flask skulle komme til å falle"
"Blir det ni grønne flakser som sitter fast på veggen"
```

Teksten gjentas ti ganger, med et forskellige tall hver gang, til det ikke er noen flasker igjen.

## Oppgave

Kan du skrive et program som skrives ut hele sangen?

## Løsningsoppgave

<details>
  <summary>Klikk her for løsningsforslag</summary>

```python
tallord = {
    1: "Ett",
    2: "To",
    3: "Tre",
    4: "Fire",
    5: "Fem",
    6: "Seks",
    7: "Sju",
    8: "Åtte",
    9: "Ni",
    10: "Ti"
}

for i in range(10, 1, -1):
    flaske_ord = "flaske"
    if i >= 2:
        flaske_ord = flaske_ord + "r"

    grønnt_ord = 'grønnt'
    if i >= 2:
        grønnt_ord = 'grønne'

    neste_flaske_ord = "flaske"
    if i - 1 >= 2:
        neste_flaske_ord = neste_flaske_ord + 'r'

    neste_grønnt_ord = 'grønnt'
    if i - 1 >= 2:
        neste_grønnt_ord = 'grønne'

    print("\n")
    print(tallord[i] + ' ' + grønnt_ord + ' ' + flaske_ord + ' sitter fast på veggen')
    print(tallord[i] + ' ' + grønnt_ord + ' ' + flaske_ord + ' sitter fast på veggen')
    print("Hvis ett grønnt flaske skulle komme til å falle")
    print("Blir det " + (tallord[i - 1]).lower() + ' ' + neste_grønnt_ord + ' ' + neste_flaske_ord + ' som sitter fast på veggen')
```
</details>
