## variable scope

variable scope - czyli zakres zmiennej, określa region w którym ta zmienna jest rozpoznawana.
Zmienna jest rozpoznawana tylko w obszarze w którym została stworzona, na przykład w funkcji.
Możemy tworzyć zmienne lokalne (np. w funkcji) oraz zmienne globalne (dla całego programu)

### LEGB
LEGB - to zasada w Python'ie, która najpierw sprawdza czy zmienna była zdefiniowana w lokalnym
w wewnętrznej funkcji, następnie w zewnętrznej, następnie sprawdza globalną zmienną,  a na końcu wbudowaną w język

L = Local
E = Enclosing
G = Global
B = Built-in