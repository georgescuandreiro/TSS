# Clasa pentru gestionarea programarilor dintr-o zi de lucru.
# Timpul este stocat in minute fata de miezul noptii.
# De exemplu: 8:00 = 480, 9:30 = 570, 17:45 = 1065


class PlanificatorProgramari:

    def __init__(self, ora_inceput=8, ora_sfarsit=18, pauza_minima=0):
        self.programari = []
        self.ora_inceput = ora_inceput * 60
        self.ora_sfarsit = ora_sfarsit * 60
        # pauza minima obligatorie intre doua programari consecutive (in minute)
        if pauza_minima < 0:
            raise ValueError("Pauza minima nu poate fi negativa")
        self.pauza_minima = pauza_minima

    def rezerva(self, nume, start, sfarsit):
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)
        self.programari.sort(key=lambda x: x["start"])
        return True

    def anuleaza(self, nume):
        for programare in self.programari:
            if programare["nume"] == nume:
                self.programari.remove(programare)
                return True
        return False

    def este_liber(self, start, sfarsit):
        # doua intervale se suprapun daca unul incepe inainte ca celalalt sa se termine
        # pauza_minima extinde zona ocupata in jurul fiecarei programari
        for programare in self.programari:
            if start < programare["sfarsit"] + self.pauza_minima and sfarsit > programare["start"] - self.pauza_minima:
                return False
        return True

    def get_programari(self):
        return list(self.programari)

    def urmatorul_slot_liber(self, durata):
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        curent = self.ora_inceput

        for programare in self.programari:
            # zona libera se termina inainte de pauza care precede programarea
            sfarsit_zona = programare["start"] - self.pauza_minima
            if sfarsit_zona - curent >= durata:
                return (curent, curent + durata)
            # urmatoarea zona libera incepe dupa programare plus pauza
            nova_pozitie = programare["sfarsit"] + self.pauza_minima
            if nova_pozitie > curent:
                curent = nova_pozitie

        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        return None

    def slot_optim(self, durata, ora_preferata):
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")
        if ora_preferata < self.ora_inceput or ora_preferata > self.ora_sfarsit:
            raise ValueError("Ora preferata este in afara orelor de lucru")

        sloturi = self._sloturi_libere(durata)

        if not sloturi:
            return None

        cel_mai_bun = None
        distanta_minima = float("inf")

        for slot_start, slot_sfarsit in sloturi:
            # incercam sa plasam programarea cat mai aproape de ora preferata
            start_ideal = ora_preferata
            if start_ideal < slot_start:
                start_ideal = slot_start
            elif start_ideal + durata > slot_sfarsit:
                start_ideal = slot_sfarsit - durata

            distanta = abs(start_ideal - ora_preferata)
            if distanta < distanta_minima:
                distanta_minima = distanta
                cel_mai_bun = (start_ideal, start_ideal + durata)

        return cel_mai_bun

    def _sloturi_libere(self, durata):
        # returnam toate intervalele libere de cel putin 'durata' minute
        sloturi = []
        curent = self.ora_inceput

        for programare in self.programari:
            sfarsit_zona = programare["start"] - self.pauza_minima
            if sfarsit_zona - curent >= durata:
                sloturi.append((curent, sfarsit_zona))
            nova_pozitie = programare["sfarsit"] + self.pauza_minima
            if nova_pozitie > curent:
                curent = nova_pozitie

        if self.ora_sfarsit - curent >= durata:
            sloturi.append((curent, self.ora_sfarsit))

        return sloturi
