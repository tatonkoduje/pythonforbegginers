## threading

**threading** - jest używany w Python'nie to uruchamiania wileu wątków (np. wywoływania funkcji) w tym samym czasie.

**thread (wątek)** - to część programu wykonywana współbieżnie w obrębie jednego procesu.
W jednym procesie może istnieć wiele wątków.

**GIL (Global Interpreter Lock)** - jest to muteks, który chroni dostep do obiektu przed wykonywaniem na nim zadań
przez wiele wątków jednocześnie.

**mutex** - to algorytm wzajemnego wykluczania, używany w celu  uniknięcia równoczesnego użycia wspólnego
zasobu (obiektu, zmiennej itd.). Nazwą mutex określane są obiekty negocjujące dostęp pomiędzy wątkami, 
zwane również blokadami.

**cpu bound** - program/zadanie spędza większość swojego czasu czekając na wewnętrzne zdarzewnie. 
Np. duża ilość obliczeń wymaga użycia multiprocessingu.

**io bound** - program/zadanie spędza większość swojego czasu czekając na zewnętrzne zdarzenie.
Np. user input wymaga życia multithreadingu.