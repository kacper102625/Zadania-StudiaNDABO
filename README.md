# Zadania-StudiaNDABO
Zadania na przedmiot studiów Narzędzia do Automatyzacji budowy oprogramowania

## Spis treści
- [Opis projektu](#opis-projektu)
- [Instalacja](#instalacja)
- [Użycie](#użycie)
- [Historia](#historia)
- [Bibliografia](#bibliografia)
- [Licencja](#licencja)
- [Autorzy](#autorzy)

## Opis projektu
Projekt zawiera zadania związane z przedmiotem **Narzędzia do Automatyzacji Budowy Oprogramowania**.

## Instalacja
Aby skorzystać z repozytorium, wykonaj poniższe kroki:
1. Sklonuj repozytorium:
    ```
    git clone https://github.com/kacper102625/Zadania-StudiaNDABO.git
    ```
2. Przejdź do folderu projektu
    ```
    cd Zadania-StudiaNDABO
    ```
## Użycie
Uruchomienie aplikacji w zależności od technologii:
    ```
    python main.py  # Dla Python
    node index.js   # Dla JavaScript
    javac Main.java && java Main  # Dla Java
    ```
## Historia
Aby sprawdzić historię commitów, użyj:
    ```
    git log --oneline --graph --decorate --all
    ```
    
## Rozwiązywanie konfliktów w projekcie

Podczas łączenia gałęzi `feature/header-design-a` oraz `feature/header-design-b` z `main` wystąpił konflikt w pliku `src/components/header.html`.

### Opis konfliktu

Obie gałęzie zmieniały ten sam fragment nagłówka strony, ale w różny sposób:

- `feature/header-design-a` wprowadziła nowe style i zmodyfikowała tekst nagłówka.
- `feature/header-design-b` zmieniła strukturę HTML nagłówka.

### Proces rozwiązania konfliktu

1. Git oznaczył konflikt w pliku `src/components/header.html`.
2. Ręcznie przeanalizowano różnice i połączono zmiany, tak aby zachować zarówno nowy styl, jak i poprawioną strukturę HTML.
3. Sprawdzono działanie nagłówka po scaleniu — wszystko wyświetla się poprawnie.
4. Zatwierdzono rozwiązanie konfliktu w repozytorium za pomocą:

## Bibliografia
- Oficjalna dokumentacja Git: [git-scm.com/doc](git-scm.com/doc)
- Oficjalna książka Pro Git: [git-scm.com/book/pl/v2](git-scm.com/book/pl/v2)
- GitHub Docs: [docs.github.com/en](docs.github.com/en)
- GitHub Learning Lab: [github.com/apps/github-learning-lab](github.com/apps/github-learning-lab)
- Interaktywny kurs Git: [learngitbranching.js.org](learngitbranching.js.org)
- Cheat sheet Markdown: [github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet](github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Licencja
Ten projekt jest licencjonowany pod [licencją MIT](https://pl.wikipedia.org/wiki/Licencja_MIT).

## Autorzy
- Kacper – [GitHub](https://github.com/kacper102625)

