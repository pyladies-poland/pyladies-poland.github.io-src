1. Pobierz repozytorium strony:

git clone https://github.com/pyladies-poland/pyladies-poland.github.io-src

2. Aby dodać:
  * osobę, dodaj plik rst do folderu content/people
  * wydarzenie, dodaj plik rst do folderu content/events

  Treści wyświetlane na stronie głównej znajdują się w katalogu content/main.

3. Zcommituj zmiany w treści.

4. Aby wygenerować strony z nowymi treściami, wykonaj:
  * make html

5. Następnie przejdź do katalogu output i scommituj wszystkie zmiany w treściach.
   Po tym wypchnij zmiany do mastera:

   ``
   cd output
   git add .
   git commit -m "Update the contents"
   git push origin master
   ``

6. Przejdź do głównego repozytorium i scommituj zmiany w katalogu output (dzięki temu
  nasze repozytorium będzie wskazywać na ostatni commit submodułu z treścią strony):

  ``
  cd ..
  git add output
  git commit -m "Update output version"
  git push origin master
  ``

UWAGA: Zamiast punktów 4-6 można wykonać skrypt deploy.sh
