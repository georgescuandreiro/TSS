from planificator_programari import PlanificatorProgramari


def ora_la_minute(text):
    # converteste "HH:MM" in minute, ex: "9:30" -> 570
    parti = text.strip().split(":")
    if len(parti) != 2:
        raise ValueError("Formatul orei trebuie sa fie HH:MM (ex: 9:30)")
    ora, minute = int(parti[0]), int(parti[1])
    if not (0 <= ora <= 23) or not (0 <= minute <= 59):
        raise ValueError("Ora sau minutele sunt invalide")
    return ora * 60 + minute


def minute_la_ora(minute):
    # converteste minutele inapoi in text, ex: 570 -> "9:30"
    return f"{minute // 60}:{minute % 60:02d}"


def afiseaza_programari(scheduler):
    lista = scheduler.get_programari()
    if not lista:
        print("  Nu exista nicio programare.")
        return
    print(f"  {'Nume':<20} {'Start':<10} {'Sfarsit'}")
    print("  " + "-" * 40)
    for p in lista:
        print(f"  {p['nume']:<20} {minute_la_ora(p['start']):<10} {minute_la_ora(p['sfarsit'])}")


def meniu_principal():
    print("\n--- Planificator Programari ---")
    print("  1. Adauga programare")
    print("  2. Anuleaza programare")
    print("  3. Vezi toate programarile")
    print("  4. Verifica disponibilitate interval")
    print("  5. Gaseste urmatorul slot liber")
    print("  6. Gaseste slot optim dupa preferinta")
    print("  0. Iesire")
    return input("Alegere: ").strip()


def main():
    ora_start = input("Ora de inceput a zilei (default 8): ").strip() or "8"
    ora_sfarsit = input("Ora de sfarsit a zilei (default 18): ").strip() or "18"
    pauza = input("Pauza minima intre programari in minute (default 0): ").strip() or "0"
    scheduler = PlanificatorProgramari(int(ora_start), int(ora_sfarsit), int(pauza))
    print(f"Program: {ora_start}:00 - {ora_sfarsit}:00, pauza minima: {pauza} minute")

    while True:
        alegere = meniu_principal()

        if alegere == "1":
            print("\n-- Adauga programare --")
            try:
                nume = input("  Nume: ").strip()
                start = ora_la_minute(input("  Ora start (HH:MM): "))
                sfarsit = ora_la_minute(input("  Ora sfarsit (HH:MM): "))
                scheduler.rezerva(nume, start, sfarsit)
                print(f"  Programare adaugata: {nume} {minute_la_ora(start)} - {minute_la_ora(sfarsit)}")
            except ValueError as e:
                print(f"  Eroare: {e}")

        elif alegere == "2":
            print("\n-- Anuleaza programare --")
            nume = input("  Numele programarii de anulat: ").strip()
            if scheduler.anuleaza(nume):
                print(f"  Programarea '{nume}' a fost anulata.")
            else:
                print(f"  Nu exista nicio programare cu numele '{nume}'.")

        elif alegere == "3":
            print("\n-- Programari existente --")
            afiseaza_programari(scheduler)

        elif alegere == "4":
            print("\n-- Verifica disponibilitate --")
            try:
                start = ora_la_minute(input("  Ora start (HH:MM): "))
                sfarsit = ora_la_minute(input("  Ora sfarsit (HH:MM): "))
                if scheduler.este_liber(start, sfarsit):
                    print(f"  Intervalul {minute_la_ora(start)} - {minute_la_ora(sfarsit)} este LIBER.")
                else:
                    print(f"  Intervalul {minute_la_ora(start)} - {minute_la_ora(sfarsit)} este OCUPAT.")
            except ValueError as e:
                print(f"  Eroare: {e}")

        elif alegere == "5":
            print("\n-- Urmatorul slot liber --")
            try:
                durata = int(input("  Durata dorita (minute): ").strip())
                slot = scheduler.urmatorul_slot_liber(durata)
                if slot:
                    print(f"  Primul slot liber: {minute_la_ora(slot[0])} - {minute_la_ora(slot[1])}")
                else:
                    print(f"  Nu exista niciun slot liber de {durata} minute in aceasta zi.")
            except ValueError as e:
                print(f"  Eroare: {e}")

        elif alegere == "6":
            print("\n-- Slot optim dupa preferinta --")
            try:
                durata = int(input("  Durata dorita (minute): ").strip())
                preferinta = ora_la_minute(input("  Ora preferata (HH:MM): "))
                slot = scheduler.slot_optim(durata, preferinta)
                if slot:
                    print(f"  Slot recomandat: {minute_la_ora(slot[0])} - {minute_la_ora(slot[1])}")
                else:
                    print(f"  Nu exista niciun slot liber de {durata} minute in aceasta zi.")
            except ValueError as e:
                print(f"  Eroare: {e}")

        elif alegere == "0":
            print("La revedere!")
            break

        else:
            print("  Optiune invalida. Alege un numar intre 0 si 6.")


if __name__ == "__main__":
    main()
