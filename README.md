# Tisícka slovíčok

Aplikácia na učenie 1000 základných anglických slov.

- Stránka: https://lucia-ship-it.github.io/slovicka/
- Triedenie po 50 slovách (Viem / Váham / Nové), potom kartičky a písanie.
- Písanie sa odomkne, keď je v skupinách Váham a Nové aspoň 20 slov.
- Pokrok sa ukladá v prehliadači (localStorage), takže sa medzi zariadeniami neprenáša.

## Súbory

- `index.html` je hotová stránka. Vzniká automaticky, neupravuj ju ručne.
- `zdroj/all.txt` je zoznam slov, jedno na riadok v tvare `anglicky|slovensky|vzorová veta`.
- `zdroj/template.html` je vzhľad a logika aplikácie.
- `zdroj/build.py` poskladá `index.html` zo zoznamu slov a šablóny.

## Pridanie slovíčok

1. Pridaj riadky na koniec `zdroj/all.txt` v tvare `anglicky|slovensky|vzorová veta`.
2. Spusti v termináli v priečinku `slovicka`:

```bash
python3 zdroj/build.py
```

3. Nahraj zmeny na GitHub (cez VS Code: Source Control, Commit, Sync, alebo príkazmi):

```bash
git add -A && git commit -m "Nové slovíčka" && git push
```

4. Stránka sa aktualizuje do minúty-dvoch. Pokrok sa nestratí, nové slová sa objavia na konci triedenia.

Zmeny vzhľadu alebo funkcií sa robia v `zdroj/template.html`, potom znova spusti `build.py` a nahraj.

## Nápady na neskôr

- Prenos pokroku medzi počítačom a telefónom (potrebuje úložisko).
- Ďalšie slovíčka a kategórie.
- Výber zo 4 možností a počúvanie.
