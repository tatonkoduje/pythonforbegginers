## daemon thread

**daemon thread** - jest to rodzaj wątku, który jest uruchomiony w tle i nie jest istotny dla działania 
programu. Program nie czeka aż ten wątek się zakończy. Używa się go dla zadań oczekujących w tle programu, np. czekanie 
na akcje usere.
Daemon thread się zakończy wtedy, gdy zakończą się wszystkie nie daemonowe wątki.