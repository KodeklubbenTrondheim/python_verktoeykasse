_Vanskelighetsgrad: Enkel_

Nå skal vi lage et lite program som lar brukeren skrive inn sin egen informajson.

For å la brukeren skrive selv kan man bruke `input()` funksjonen, og for eksempel lagre det i en variabel kalt navn:

```
navn = input("Hva heter du?")
```

Dette kan så printes ut med `print(navn)`.

### Lag et lite intervju og skriv ut svarene på slutten.

For eksempel:

Maskin: Hva heter du?\
Person: Nils\
Maskin: Du heter Nils

<br/>

<details>
  <summary>Klikk her for løsningsforslag til eksempelet</summary>

```
navn = input("Hva heter du? \n")  # \n betyr ny linje
# Personen skriver "Nils"
print("Du heter " + navn)
```
</details>
