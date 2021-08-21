### Opgave

Pasen valt op de eerste zondag na de eerste volle maan van de lente. In zijn boek “Astronomical Algorithms” geeft de Belgische wiskundige en astronoom Jean Meeus (1928 – ) een algoritme om de datum van Pasen in het jaar x (x > 1582) te berekenen.

Schematisch ziet het er uit als volgt:

| Deel                  | door || (gehele) quotiënt | rest |
|:---------------------:|:----:|:-----------------:|:----:|
| het jaartal x         | 19   | /                 | a    |
| het jaartal x         | 100  | b                 | c    |
| b                     | 4    | d                 | e    |
| b + 8                 | 25   | f                 | /    |
| b - f + 1             | 3    | g                 | /    |
| 19a + b - d - g + 15  | 30   | /                 | h    |
| c                     | 4    | i                 | k    |
| 32 + 2e + 2i - h - k  | 7    | /                 | l    |
| a + 11h + 22l         | 451  | m                 | /    |
| h + l - 7m + 114      | 31   | n                 | p    |

De waarde van n die je zo bekomt, is gelijk aan de maand waarin Pasen valt in het jaar x (3 = maart, 4 = april). De dag waarop Pasen valt, is gelijk aan p + 1. Implementeer dit algoritme in Python. Bereken de datum van Pasen in 2022. Als uitvoer geeft het programma de paasdatum in de vorm 12 4 2020.
