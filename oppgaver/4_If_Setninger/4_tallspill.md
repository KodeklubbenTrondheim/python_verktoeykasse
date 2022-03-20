## Beskrivelse

_Vanskelighetsgrad: Vanskelig_

Et tallspill går ut på å gjette et tall mellom 1 og 100. Hvis spilleren gjetter et lavere tall må den få beskjed om å gjette høyere og det samme om tallet er for høyt. Hvis spilleren treffer riktig tall må den få beskjed om at den har vunnet.

For å velge vinnertallet kan du enten sette det selv eller gjøre det random ved bruk av denne koden:

```python
import random
vinnertall = random.randint(0, 100)
```

Lag dette spillet ved bruk av `if`, `input`, `while`, og `print`.

<details>
  <summary>Klikk her for løsningsforslag</summary>

```python
import random

vinnertall = random.randint(0, 100)

gjettet = False

while not gjettet:
    gjetning = int(input("Hva er gjetningen din? "))

    if gjetning > vinnertall:
        print("Gjetningen din var for stor!")
    elif gjetning < vinnertall:
        print("Gjetningen din var for lite!")
    else:
        print("Gratulerer, din gjetning var riktig!")
        gjettet = True
```

</details>
