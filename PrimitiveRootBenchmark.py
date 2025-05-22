import time
from sympy import isprime, primefactors


# Kriterium aus der VO
# Prüft mit dem naiven Verfahren, ob g eine Primitivwurzel modulo p ist:
# Es wird geprüft, ob die Potenzen von g modulo p alle Zahlen von 1 bis p-1 erzeugen.
def is_primitive_naive(g, p):
    return set(pow(g, i, p) for i in range(1, p)) == set(range(1, p))


# Faktorisierungskriterium prüft mit einem effizienten Verfahren, ob g eine Primitivwurzel modulo p ist:
# g ist genau dann eine Primitivwurzel, wenn für jeden Primfaktor q von p-1 gilt:
#     g^((p-1)/q) mod p ≠ 1
# Dies basiert auf Gruppentheorie und ist deutlich schneller (O(log(p))) als das naive Verfahren (O(p)).
def is_primitive_efficient(g, p):
    factors = primefactors(p - 1)  # Faktorisierung von p-1
    for q in factors:
        # Wenn eine dieser Potenzen 1 ergibt, ist g KEINE Primitivwurzel
        if pow(g, (p - 1) // q, p) == 1:
            return False
    return True


# Führt den Laufzeitvergleich beider Methoden für verschiedene Primzahlen p durch.
def benchmark(p_values):
    for p in p_values:
        assert isprime(p)  # p muss Primzahl sein
        print(f"Modulgröße: {p}")
        g = 2  # Testkandidat für mögliche Primitivwurzel

        # Zeitmessung für das naive Verfahren
        start_naive = time.perf_counter()
        naive_result = is_primitive_naive(g, p)
        duration_naive = time.perf_counter() - start_naive

        # Zeitmessung für das effiziente Verfahren
        start_eff = time.perf_counter()
        eff_result = is_primitive_efficient(g, p)
        duration_eff = time.perf_counter() - start_eff

        # Ausgabe der Ergebnisse mit Zeit
        print(f" Naiv: {duration_naive:.9f}s, Ergebnis: {naive_result}")
        print(f" Effizient: {duration_eff:.9f}s, Ergebnis: {eff_result}\n")


# Liste der getesteten Primzahlen
benchmark([101, 211, 409, 613, 1223, 2459])
