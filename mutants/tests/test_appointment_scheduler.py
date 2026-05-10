import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from appointment_scheduler import AppointmentScheduler

# Constante pentru timpii folositi frecvent in teste (minute de la miezul noptii)
ORA_8_00  = 480
ORA_8_30  = 510
ORA_9_00  = 540
ORA_9_30  = 570
ORA_10_00 = 600
ORA_12_00 = 720
ORA_17_00 = 1020
ORA_18_00 = 1080


# ==============================================================================
# 1. PARTITIONARE IN CLASE DE ECHIVALENTA
# ==============================================================================

class TestEchivalentaRezerva:
    """
    Clase de echivalenta pentru rezerva(nume, start, sfarsit):
      EC1 - input complet valid
      EC2 - nume gol (sir vid)
      EC3 - nume nu este string
      EC4 - start >= sfarsit (interval invalid)
      EC5 - programare incepe inainte de ora de lucru
      EC6 - programare se termina dupa ora de lucru
      EC7 - interval suprapus peste o programare existenta
    """

    def test_EC1_rezervare_valida(self):
        scheduler = AppointmentScheduler()
        assert scheduler.rezerva("Ana", ORA_9_00, ORA_10_00) == True

    def test_EC2_nume_gol(self):
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError):
            scheduler.rezerva("", ORA_9_00, ORA_10_00)

    def test_EC3_nume_not_string(self):
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError):
            scheduler.rezerva(123, ORA_9_00, ORA_10_00)

    def test_EC4_interval_inversat(self):
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_10_00, ORA_9_00)

    def test_EC5_inainte_de_program(self):
        # 7:59 - 9:00, incepe inainte de 8:00
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_8_00 - 1, ORA_9_00)

    def test_EC6_dupa_program(self):
        # 17:00 - 18:01, se termina dupa 18:00
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_17_00, ORA_18_00 + 1)

    def test_EC7_suprapunere(self):
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        with pytest.raises(ValueError):
            scheduler.rezerva("Bob", ORA_9_30, ORA_10_00 + 30)


class TestEchivalentaAnuleaza:
    """
    Clase de echivalenta pentru anuleaza(nume):
      EC1 - programarea exista -> True
      EC2 - programarea nu exista -> False
    """

    def test_EC1_anulare_existenta(self):
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.anuleaza("Ana") == True

    def test_EC2_anulare_inexistenta(self):
        scheduler = AppointmentScheduler()
        assert scheduler.anuleaza("Necunoscut") == False


class TestEchivalentaEsteLiber:
    """
    Clase de echivalenta pentru este_liber(start, sfarsit):
      EC1 - intervalul este liber -> True
      EC2 - intervalul este ocupat -> False
    """

    def test_EC1_interval_liber(self):
        scheduler = AppointmentScheduler()
        assert scheduler.este_liber(ORA_9_00, ORA_10_00) == True

    def test_EC2_interval_ocupat(self):
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.este_liber(ORA_9_00, ORA_10_00) == False


class TestEchivalentaUrmatorul:
    """
    Clase de echivalenta pentru urmatorul_slot_liber(durata):
      EC1 - durata invalida (<= 0) -> ValueError
      EC2 - nu exista programari, slot disponibil imediat
      EC3 - exista programari, exista slot disponibil
      EC4 - ziua este plina, nu exista slot
    """

    def test_EC1_durata_negativa(self):
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError):
            scheduler.urmatorul_slot_liber(-10)

    def test_EC2_fara_programari(self):
        scheduler = AppointmentScheduler()
        assert scheduler.urmatorul_slot_liber(60) == (ORA_8_00, ORA_9_00)

    def test_EC3_cu_programari_slot_disponibil(self):
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.urmatorul_slot_liber(30) == (ORA_8_00, ORA_8_30)

    def test_EC4_niciun_slot_disponibil(self):
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_8_00, ORA_18_00)
        assert scheduler.urmatorul_slot_liber(60) is None


# ==============================================================================
# 2. ANALIZA VALORILOR DE FRONTIERA
# ==============================================================================

class TestFrontieraRezerva:
    """
    Valori de frontiera pentru rezerva():
      BV1 - start = ora_inceput (480, exact 8:00)          -> valid
      BV2 - start = ora_inceput - 1 (479, adica 7:59)      -> invalid
      BV3 - sfarsit = ora_sfarsit (1080, exact 18:00)       -> valid
      BV4 - sfarsit = ora_sfarsit + 1 (1081, adica 18:01)   -> invalid
      BV5 - start = sfarsit (durata 0)                      -> invalid
      BV6 - sfarsit = start + 1 (durata 1 minut)            -> valid
    """

    def test_BV1_start_exact_ora_inceput(self):
        scheduler = AppointmentScheduler()
        assert scheduler.rezerva("Ana", ORA_8_00, ORA_9_00) == True

    def test_BV2_start_cu_un_minut_inainte(self):
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_8_00 - 1, ORA_9_00)

    def test_BV3_sfarsit_exact_ora_sfarsit(self):
        scheduler = AppointmentScheduler()
        assert scheduler.rezerva("Ana", ORA_17_00, ORA_18_00) == True

    def test_BV4_sfarsit_cu_un_minut_dupa(self):
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_17_00, ORA_18_00 + 1)

    def test_BV5_start_egal_sfarsit(self):
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_9_00, ORA_9_00)

    def test_BV6_durata_un_minut(self):
        scheduler = AppointmentScheduler()
        assert scheduler.rezerva("Ana", ORA_9_00, ORA_9_00 + 1) == True


class TestFrontieraUrmatorul:
    """
    Valori de frontiera pentru urmatorul_slot_liber():
      BV7  - durata = 0                          -> invalid
      BV8  - durata = 1 (minim valid)            -> returneaza slot
      BV9  - durata = exact spatiul ramas        -> returneaza slot
      BV10 - durata = spatiul ramas + 1          -> None
    """

    def test_BV7_durata_zero(self):
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError):
            scheduler.urmatorul_slot_liber(0)

    def test_BV8_durata_un_minut(self):
        scheduler = AppointmentScheduler()
        assert scheduler.urmatorul_slot_liber(1) == (ORA_8_00, ORA_8_00 + 1)

    def test_BV9_durata_exact_cat_spatiul_ramas(self):
        # Ana ocupa 9:00-18:00, raman exact 60 min inainte (8:00-9:00)
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_9_00, ORA_18_00)
        assert scheduler.urmatorul_slot_liber(60) == (ORA_8_00, ORA_9_00)

    def test_BV10_durata_mai_mare_decat_spatiul(self):
        # Ana ocupa 9:00-18:00, spatiu liber = 60 min, cerem 61
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_9_00, ORA_18_00)
        assert scheduler.urmatorul_slot_liber(61) is None


# ==============================================================================
# 3. ACOPERIRE INSTRUCTIUNE / DECIZIE / CONDITIE
# ==============================================================================

class TestAcoperireConditiiRezerva:
    """
    Acoperire conditii individuale din rezerva():
      - `not isinstance(nume, str)` = True
      - `nume.strip() == ""` = True
      - `start >= sfarsit` = True
      - `start < self.ora_inceput` = True
      - `sfarsit > self.ora_sfarsit` = True
      - toate conditiile = False (cale de succes)
    """

    def test_conditie_nume_none(self):
        # not isinstance(nume, str) -> True
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError):
            scheduler.rezerva(None, ORA_9_00, ORA_10_00)

    def test_conditie_nume_doar_spatii(self):
        # nume.strip() == "" -> True
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError):
            scheduler.rezerva("   ", ORA_9_00, ORA_10_00)

    def test_conditie_start_mai_mare_decat_sfarsit(self):
        # start >= sfarsit -> True
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_10_00, ORA_9_00)

    def test_conditie_start_inainte_de_ora_inceput(self):
        # start < self.ora_inceput -> True
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_8_00 - 10, ORA_9_00)

    def test_conditie_sfarsit_dupa_ora_sfarsit(self):
        # sfarsit > self.ora_sfarsit -> True
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_9_00, ORA_18_00 + 10)

    def test_toate_conditiile_false(self):
        # toate conditiile de eroare sunt False -> se ajunge la append
        scheduler = AppointmentScheduler()
        assert scheduler.rezerva("Ana", ORA_9_00, ORA_10_00) == True
        assert len(scheduler.get_programari()) == 1


class TestAcoperireConditiiEsteLiber:
    """
    Acoperire conditii individuale din este_liber():
      - lista goala -> True direct (bucla nu se executa)
      - suprapunere partiala la stanga
      - suprapunere partiala la dreapta
      - noul interval cuprins complet in cel existent
      - noul interval complet inainte -> True
      - noul interval complet dupa -> True
    """

    def test_lista_goala(self):
        scheduler = AppointmentScheduler()
        assert scheduler.este_liber(ORA_9_00, ORA_10_00) == True

    def test_suprapunere_partiala_stanga(self):
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.este_liber(ORA_8_30, ORA_9_30) == False

    def test_suprapunere_partiala_dreapta(self):
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.este_liber(ORA_9_30, ORA_10_00 + 30) == False

    def test_cuprins_in_interior(self):
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_8_00, ORA_18_00)
        assert scheduler.este_liber(ORA_9_00, ORA_10_00) == False

    def test_complet_inainte(self):
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_10_00, ORA_12_00)
        assert scheduler.este_liber(ORA_8_00, ORA_9_00) == True

    def test_complet_dupa(self):
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_8_00, ORA_9_00)
        assert scheduler.este_liber(ORA_10_00, ORA_12_00) == True


# ==============================================================================
# 4. CIRCUITE INDEPENDENTE (COMPLEXITATE CICLOMATICA McCABE)
# ==============================================================================

class TestCircuiteRezerva:
    """
    Complexitate ciclomatica V(G) = 5 pentru rezerva().
    Exista 4 decizii => 5 cai independente:
      P1: nume invalid -> ValueError
      P2: start >= sfarsit -> ValueError
      P3: in afara orelor de lucru -> ValueError
      P4: interval ocupat -> ValueError
      P5: toate valide -> True
    """

    def test_P1_nume_invalid(self):
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError, match="Numele"):
            scheduler.rezerva("", ORA_9_00, ORA_10_00)

    def test_P2_interval_invalid(self):
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError, match="start"):
            scheduler.rezerva("Ana", ORA_10_00, ORA_9_00)

    def test_P3_in_afara_orelor(self):
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError, match="afara"):
            scheduler.rezerva("Ana", ORA_8_00 - 60, ORA_9_00)

    def test_P4_interval_ocupat(self):
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        with pytest.raises(ValueError, match="ocupat"):
            scheduler.rezerva("Bob", ORA_9_00, ORA_10_00)

    def test_P5_succes(self):
        scheduler = AppointmentScheduler()
        assert scheduler.rezerva("Ana", ORA_9_00, ORA_10_00) == True


class TestCircuiteUrmatorul:
    """
    Complexitate ciclomatica V(G) = 4 pentru urmatorul_slot_liber().
    Exista 3 decizii => 4 cai independente:
      P1: durata invalida -> ValueError
      P2: slot disponibil inainte de prima programare
      P3: slot disponibil dupa ultima programare
      P4: niciun slot disponibil
    """

    def test_P1_durata_invalida(self):
        scheduler = AppointmentScheduler()
        with pytest.raises(ValueError):
            scheduler.urmatorul_slot_liber(0)

    def test_P2_slot_inainte_de_prima_programare(self):
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_10_00, ORA_12_00)
        assert scheduler.urmatorul_slot_liber(60) == (ORA_8_00, ORA_9_00)

    def test_P3_slot_dupa_ultima_programare(self):
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_8_00, ORA_17_00)
        assert scheduler.urmatorul_slot_liber(60) == (ORA_17_00, ORA_18_00)

    def test_P4_niciun_slot(self):
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_8_00, ORA_18_00)
        assert scheduler.urmatorul_slot_liber(30) is None


# ==============================================================================
# 5. TESTE SUPLIMENTARE PENTRU MUTANTI
# Adaugate dupa analiza raportului generat de mutmut.
# Omoara 2 mutanti neechivalenti care au supravietuit suita initiala de teste.
# ==============================================================================

class TestMutanti:
    """
    Mutant M1 (supravietuitor):
      Locatie: este_liber(), conditia `sfarsit > programare["start"]`
      Mutatie:  `>` inlocuit cu `>=`
      Efect:    doua programari adiacente (sfarsit1 == start2) ar fi
                considerate in conflict, desi sunt perfect valide.
      Test:     rezervam "Ana" 9:00-10:00 si "Bob" 10:00-12:00 (adiacente).
                Ambele trebuie sa reuseasca. Mutantul ar arunca ValueError la a doua.

    Mutant M2 (supravietuitor):
      Locatie: urmatorul_slot_liber(), conditia `programare["start"] - curent >= durata`
      Mutatie:  `>=` inlocuit cu `>`
      Efect:    un slot de exact dimensiunea necesara nu ar fi returnat.
      Test:     spatiu liber = exact 60 min, cerem 60 min.
                Trebuie sa returneze slotul. Mutantul ar returna None.
    """

    def test_M1_programari_adiacente_sunt_valide(self):
        # Ana: 9:00-10:00, Bob: 10:00-12:00 -> adiacente, nu suprapuse
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.rezerva("Bob", ORA_10_00, ORA_12_00) == True

    def test_M2_slot_exact_dimensiunea_necesara(self):
        # Ana ocupa 9:00-18:00, spatiu liber inainte = exact 60 min (8:00-9:00)
        scheduler = AppointmentScheduler()
        scheduler.rezerva("Ana", ORA_9_00, ORA_18_00)
        assert scheduler.urmatorul_slot_liber(60) == (ORA_8_00, ORA_9_00)
