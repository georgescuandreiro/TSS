import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from planificator_programari import PlanificatorProgramari

# timpi folositi des in teste, in minute de la miezul noptii
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
      EC2 - nume gol
      EC3 - nume nu este string
      EC4 - start mai mare decat sfarsit
      EC5 - programare incepe inainte de ora de lucru
      EC6 - programare se termina dupa ora de lucru
      EC7 - interval suprapus cu o programare existenta
    """

    def test_EC1_rezervare_valida(self):
        scheduler = PlanificatorProgramari()
        assert scheduler.rezerva("Ana", ORA_9_00, ORA_10_00) == True

    def test_EC2_nume_gol(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.rezerva("", ORA_9_00, ORA_10_00)

    def test_EC3_nume_not_string(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.rezerva(123, ORA_9_00, ORA_10_00)

    def test_EC4_interval_inversat(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_10_00, ORA_9_00)

    def test_EC5_inainte_de_program(self):
        # 7:59 - 9:00, incepe inainte de 8:00
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_8_00 - 1, ORA_9_00)

    def test_EC6_dupa_program(self):
        # 17:00 - 18:01, se termina dupa 18:00
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_17_00, ORA_18_00 + 1)

    def test_EC7_suprapunere(self):
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        with pytest.raises(ValueError):
            scheduler.rezerva("Bob", ORA_9_30, ORA_10_00 + 30)


class TestEchivalentaAnuleaza:
    """
    Clase de echivalenta pentru anuleaza(nume):
      EC1 - programarea exista, returneaza True
      EC2 - programarea nu exista, returneaza False
    """

    def test_EC1_anulare_existenta(self):
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.anuleaza("Ana") == True

    def test_EC2_anulare_inexistenta(self):
        scheduler = PlanificatorProgramari()
        assert scheduler.anuleaza("Necunoscut") == False


class TestEchivalentaEsteLiber:
    """
    Clase de echivalenta pentru este_liber(start, sfarsit):
      EC1 - intervalul este liber, returneaza True
      EC2 - intervalul este ocupat, returneaza False
    """

    def test_EC1_interval_liber(self):
        scheduler = PlanificatorProgramari()
        assert scheduler.este_liber(ORA_9_00, ORA_10_00) == True

    def test_EC2_interval_ocupat(self):
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.este_liber(ORA_9_00, ORA_10_00) == False


class TestEchivalentaUrmatorul:
    """
    Clase de echivalenta pentru urmatorul_slot_liber(durata):
      EC1 - durata invalida, zero sau negativa
      EC2 - nu exista programari, slot disponibil imediat
      EC3 - exista programari dar mai este loc
      EC4 - ziua este plina, nu exista slot
    """

    def test_EC1_durata_negativa(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.urmatorul_slot_liber(-10)

    def test_EC2_fara_programari(self):
        scheduler = PlanificatorProgramari()
        assert scheduler.urmatorul_slot_liber(60) == (ORA_8_00, ORA_9_00)

    def test_EC3_cu_programari_slot_disponibil(self):
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.urmatorul_slot_liber(30) == (ORA_8_00, ORA_8_30)

    def test_EC4_niciun_slot_disponibil(self):
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_8_00, ORA_18_00)
        assert scheduler.urmatorul_slot_liber(60) is None


# ==============================================================================
# 2. ANALIZA VALORILOR DE FRONTIERA
# ==============================================================================

class TestFrontieraRezerva:
    """
    Valori de frontiera pentru rezerva():
      BV1 - start = 480, exact 8:00, valid
      BV2 - start = 479, adica 7:59, invalid
      BV3 - sfarsit = 1080, exact 18:00, valid
      BV4 - sfarsit = 1081, adica 18:01, invalid
      BV5 - start egal cu sfarsit, durata 0, invalid
      BV6 - durata 1 minut, valoare minima valida
    """

    def test_BV1_start_exact_ora_inceput(self):
        scheduler = PlanificatorProgramari()
        assert scheduler.rezerva("Ana", ORA_8_00, ORA_9_00) == True

    def test_BV2_start_cu_un_minut_inainte(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_8_00 - 1, ORA_9_00)

    def test_BV3_sfarsit_exact_ora_sfarsit(self):
        scheduler = PlanificatorProgramari()
        assert scheduler.rezerva("Ana", ORA_17_00, ORA_18_00) == True

    def test_BV4_sfarsit_cu_un_minut_dupa(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_17_00, ORA_18_00 + 1)

    def test_BV5_start_egal_sfarsit(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_9_00, ORA_9_00)

    def test_BV6_durata_un_minut(self):
        scheduler = PlanificatorProgramari()
        assert scheduler.rezerva("Ana", ORA_9_00, ORA_9_00 + 1) == True


class TestFrontieraUrmatorul:
    """
    Valori de frontiera pentru urmatorul_slot_liber():
      BV7  - durata = 0, invalid
      BV8  - durata = 1, minim valid
      BV9  - durata egala cu spatiul ramas, returneaza slot
      BV10 - durata mai mare cu 1 decat spatiul ramas, nu gaseste slot
    """

    def test_BV7_durata_zero(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.urmatorul_slot_liber(0)

    def test_BV8_durata_un_minut(self):
        scheduler = PlanificatorProgramari()
        assert scheduler.urmatorul_slot_liber(1) == (ORA_8_00, ORA_8_00 + 1)

    def test_BV9_durata_exact_cat_spatiul_ramas(self):
        # Ana ocupa 9:00-18:00, raman exact 60 min inainte
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_9_00, ORA_18_00)
        assert scheduler.urmatorul_slot_liber(60) == (ORA_8_00, ORA_9_00)

    def test_BV10_durata_mai_mare_decat_spatiul(self):
        # Ana ocupa 9:00-18:00, spatiu liber = 60 min, cerem 61
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_9_00, ORA_18_00)
        assert scheduler.urmatorul_slot_liber(61) is None


# ==============================================================================
# 3. ACOPERIRE INSTRUCTIUNE / DECIZIE / CONDITIE
# ==============================================================================

class TestAcoperireConditiiRezerva:
    """
    Testam fiecare conditie din rezerva() separat.
    Acoperim toate ramurile if/else cel putin o data.
    """

    def test_conditie_nume_none(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.rezerva(None, ORA_9_00, ORA_10_00)

    def test_conditie_nume_doar_spatii(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.rezerva("   ", ORA_9_00, ORA_10_00)

    def test_conditie_start_mai_mare_decat_sfarsit(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_10_00, ORA_9_00)

    def test_conditie_start_inainte_de_ora_inceput(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_8_00 - 10, ORA_9_00)

    def test_conditie_sfarsit_dupa_ora_sfarsit(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.rezerva("Ana", ORA_9_00, ORA_18_00 + 10)

    def test_toate_conditiile_false(self):
        # nicio conditie de eroare nu se declanseaza, programarea se adauga
        scheduler = PlanificatorProgramari()
        assert scheduler.rezerva("Ana", ORA_9_00, ORA_10_00) == True
        assert len(scheduler.get_programari()) == 1


class TestAcoperireConditiiEsteLiber:
    """
    Testam toate cazurile de suprapunere din este_liber().
    """

    def test_lista_goala(self):
        scheduler = PlanificatorProgramari()
        assert scheduler.este_liber(ORA_9_00, ORA_10_00) == True

    def test_suprapunere_partiala_stanga(self):
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.este_liber(ORA_8_30, ORA_9_30) == False

    def test_suprapunere_partiala_dreapta(self):
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.este_liber(ORA_9_30, ORA_10_00 + 30) == False

    def test_cuprins_in_interior(self):
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_8_00, ORA_18_00)
        assert scheduler.este_liber(ORA_9_00, ORA_10_00) == False

    def test_complet_inainte(self):
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_10_00, ORA_12_00)
        assert scheduler.este_liber(ORA_8_00, ORA_9_00) == True

    def test_complet_dupa(self):
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_8_00, ORA_9_00)
        assert scheduler.este_liber(ORA_10_00, ORA_12_00) == True


# ==============================================================================
# 4. CIRCUITE INDEPENDENTE (COMPLEXITATE CICLOMATICA McCABE)
# ==============================================================================

class TestCircuiteRezerva:
    """
    rezerva() are 4 conditii if, deci complexitatea ciclomatica V(G) = 5.
    Fiecare test parcurge o cale independenta prin functie:
      P1 - nume invalid
      P2 - interval invalid
      P3 - in afara orelor de lucru
      P4 - interval ocupat
      P5 - toate datele corecte
    """

    def test_P1_nume_invalid(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError, match="Numele"):
            scheduler.rezerva("", ORA_9_00, ORA_10_00)

    def test_P2_interval_invalid(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError, match="start"):
            scheduler.rezerva("Ana", ORA_10_00, ORA_9_00)

    def test_P3_in_afara_orelor(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError, match="afara"):
            scheduler.rezerva("Ana", ORA_8_00 - 60, ORA_9_00)

    def test_P4_interval_ocupat(self):
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        with pytest.raises(ValueError, match="ocupat"):
            scheduler.rezerva("Bob", ORA_9_00, ORA_10_00)

    def test_P5_succes(self):
        scheduler = PlanificatorProgramari()
        assert scheduler.rezerva("Ana", ORA_9_00, ORA_10_00) == True


class TestCircuiteUrmatorul:
    """
    urmatorul_slot_liber() are 3 conditii if, deci V(G) = 4.
    Cele 4 cai independente:
      P1 - durata invalida
      P2 - slot gasit inainte de prima programare
      P3 - slot gasit dupa ultima programare
      P4 - nu exista niciun slot
    """

    def test_P1_durata_invalida(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.urmatorul_slot_liber(0)

    def test_P2_slot_inainte_de_prima_programare(self):
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_10_00, ORA_12_00)
        assert scheduler.urmatorul_slot_liber(60) == (ORA_8_00, ORA_9_00)

    def test_P3_slot_dupa_ultima_programare(self):
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_8_00, ORA_17_00)
        assert scheduler.urmatorul_slot_liber(60) == (ORA_17_00, ORA_18_00)

    def test_P4_niciun_slot(self):
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_8_00, ORA_18_00)
        assert scheduler.urmatorul_slot_liber(30) is None


# ==============================================================================
# 5. TESTE SUPLIMENTARE PENTRU MUTANTI
# ==============================================================================

class TestMutanti:
    """
    Mutanti echivalenti (nu pot fi omorati):
      ID 61  - >= vs > la avansarea pozitiei in urmatorul_slot_liber: cand egale, rezultat identic
      ID 75  - cel_mai_bun = "" vs None: bucla suprascrie mereu valoarea initiala
      ID 79  - <= vs < la slot_start: cand egale, ajustarea la aceeasi valoare
      ID 82  - >= vs > la slot_sfarsit: cand egale, ajustarea la aceeasi valoare
      ID 101 - >= vs > in _sloturi_libere: identic cu ID 61

    Mutanti ne-echivalenti omorati:
      ID 19  - schimba mesajul erorii pentru nume gol
      ID 27  - schimba mesajul erorii pentru interval ocupat
      ID 42  - schimba operatorul in verificarea de suprapunere din este_liber
      ID 44  - schimba - cu + in conditia de suprapunere cu pauza_minima
      ID 50  - schimba mesajul erorii pentru durata invalida in urmatorul_slot_liber
      ID 53  - schimba - cu + la calculul sfarsit_zona in urmatorul_slot_liber
      ID 59  - schimba + cu - la calculul nova_pozitie in urmatorul_slot_liber
      ID 68  - schimba mesajul erorii pentru durata invalida in slot_optim
      ID 72  - schimba mesajul erorii pentru ora_preferata invalida
      ID 94  - schimba - cu + la calculul sfarsit_zona in _sloturi_libere
      ID 99  - schimba + cu - la calculul nova_pozitie in _sloturi_libere
      ID 104 - schimba >= cu > la verificarea spatiului final in _sloturi_libere
    """

    def test_M_mesaj_nume_gol(self):
        # ucide ID 19: mesajul trebuie sa inceapa exact cu "Numele"
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError, match="^Numele"):
            scheduler.rezerva("", ORA_9_00, ORA_10_00)

    def test_M_mesaj_interval_ocupat(self):
        # ucide ID 27: mesajul trebuie sa inceapa exact cu "Intervalul"
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        with pytest.raises(ValueError, match="^Intervalul"):
            scheduler.rezerva("Bob", ORA_9_00, ORA_10_00)

    def test_M_programari_adiacente(self):
        # ucide ID 42: doua programari adiacente nu trebuie tratate ca suprapunere
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.rezerva("Bob", ORA_8_00, ORA_9_00) == True

    def test_M_pauza_inainte_de_programare(self):
        # ucide ID 44: interval care se termina in zona de pauza trebuie refuzat
        # Bob se termina la 8:50 (530), dar pauza_minima=15 face zona protejata 8:45-9:00
        scheduler = PlanificatorProgramari(pauza_minima=15)
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        with pytest.raises(ValueError):
            scheduler.rezerva("Bob", ORA_8_00, ORA_9_00 - 10)

    def test_M_mesaj_durata_slot_liber(self):
        # ucide ID 50: mesajul pentru durata invalida in urmatorul_slot_liber
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError, match="^Durata"):
            scheduler.urmatorul_slot_liber(0)

    def test_M_slot_liber_respecta_pauza_inainte(self):
        # ucide ID 53: cu pauza 15 min si Ana la 9:00, zona libera inainte se termina la 8:45
        # un slot de 55 min nu incape inainte de 8:45, asa ca e returnat dupa Ana
        scheduler = PlanificatorProgramari(pauza_minima=15)
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.urmatorul_slot_liber(55) == (ORA_10_00 + 15, ORA_10_00 + 70)

    def test_M_slot_liber_respecta_pauza_dupa(self):
        # ucide ID 59: nova_pozitie dupa Ana trebuie sa fie sfarsit + pauza, nu sfarsit - pauza
        # Ana ocupa pana la 17:30 (1050), cu pauza 15 raman doar 15 min -> nu incape slot de 30
        scheduler = PlanificatorProgramari(pauza_minima=15)
        scheduler.rezerva("Ana", ORA_8_00, ORA_17_00 + 30)
        assert scheduler.urmatorul_slot_liber(30) is None

    def test_M_mesaj_durata_slot_optim(self):
        # ucide ID 68: mesajul pentru durata invalida in slot_optim
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError, match="^Durata"):
            scheduler.slot_optim(0, ORA_10_00)

    def test_M_mesaj_ora_preferata(self):
        # ucide ID 72: mesajul pentru ora_preferata in afara programului
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError, match="^Ora preferata"):
            scheduler.slot_optim(60, ORA_8_00 - 60)

    def test_M_sloturi_libere_pauza_inainte(self):
        # ucide ID 94: sfarsit_zona in _sloturi_libere trebuie calculat cu -, nu cu +
        # cu pauza 15, preferinta 530 (8:50), slotul de 45 min trebuie sa fie (480, 525)
        scheduler = PlanificatorProgramari(pauza_minima=15)
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.slot_optim(45, ORA_9_00 - 10) == (ORA_8_00, ORA_8_00 + 45)

    def test_M_sloturi_libere_pauza_dupa(self):
        # ucide ID 99: nova_pozitie in _sloturi_libere trebuie sa fie sfarsit + pauza
        # Ana ocupa pana la 17:40 (1060), cu pauza 10 raman 10 min -> slot_optim returneaza None
        scheduler = PlanificatorProgramari(pauza_minima=10)
        scheduler.rezerva("Ana", ORA_8_00, ORA_17_00 + 40)
        assert scheduler.slot_optim(15, ORA_10_00) is None

    def test_M_sloturi_libere_frontiera_exacta(self):
        # ucide ID 104: >= trebuie pastrat, > ar elimina slotul cand spatiul == durata exact
        # dupa Ana la 10:00, raman exact 480 min pana la 18:00
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.slot_optim(480, ORA_10_00) == (ORA_10_00, ORA_18_00)


# ==============================================================================
# 6. TESTE PAUZA MINIMA
# ==============================================================================

class TestEchivalentaPauza:
    """
    Clase de echivalenta pentru pauza_minima:
      EC1 - pauza_minima = 0, comportament normal fara restrictii
      EC2 - pauza_minima pozitiva, gap suficient intre programari
      EC3 - pauza_minima pozitiva, gap insuficient intre programari
      EC4 - pauza_minima negativa, invalida
    """

    def test_EC1_fara_pauza(self):
        # cu pauza 0 doua programari pot fi consecutive
        scheduler = PlanificatorProgramari(pauza_minima=0)
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.rezerva("Bob", ORA_10_00, ORA_12_00) == True

    def test_EC2_cu_pauza_gap_suficient(self):
        # pauza 15 min, Bob incepe la 15 min dupa ce Ana se termina
        scheduler = PlanificatorProgramari(pauza_minima=15)
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.rezerva("Bob", ORA_10_00 + 15, ORA_12_00) == True

    def test_EC3_cu_pauza_gap_insuficient(self):
        # pauza 15 min, Bob incepe la doar 10 min dupa Ana
        scheduler = PlanificatorProgramari(pauza_minima=15)
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        with pytest.raises(ValueError):
            scheduler.rezerva("Bob", ORA_10_00 + 10, ORA_12_00)

    def test_EC4_pauza_negativa(self):
        with pytest.raises(ValueError):
            PlanificatorProgramari(pauza_minima=-1)


class TestFrontieraPauza:
    """
    Valori de frontiera pentru pauza_minima = 15 minute:
      BV1 - gap exact cat pauza minima, valid
      BV2 - gap cu un minut mai mic decat pauza, invalid
      BV3 - pauza_minima = 0, valoarea minima valida
    """

    def test_BV1_gap_exact_cat_pauza(self):
        # Bob incepe exact la 15 min dupa ce Ana se termina
        scheduler = PlanificatorProgramari(pauza_minima=15)
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.rezerva("Bob", ORA_10_00 + 15, ORA_12_00) == True

    def test_BV2_gap_cu_un_minut_mai_mic(self):
        # Bob incepe la 14 min dupa Ana, cu un minut sub pauza minima
        scheduler = PlanificatorProgramari(pauza_minima=15)
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        with pytest.raises(ValueError):
            scheduler.rezerva("Bob", ORA_10_00 + 14, ORA_12_00)

    def test_BV3_pauza_zero(self):
        scheduler = PlanificatorProgramari(pauza_minima=0)
        assert scheduler is not None


class TestUrmatorul_cu_pauza:
    """
    Verificam ca urmatorul_slot_liber tine cont de pauza_minima.
    """

    def test_slot_liber_respecta_pauza(self):
        # cu pauza 15 min si Ana 9:00-10:00, zona libera inainte de Ana
        # se termina la 8:45, deci primul slot de 30 min este 8:00-8:30
        scheduler = PlanificatorProgramari(pauza_minima=15)
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        assert scheduler.urmatorul_slot_liber(30) == (ORA_8_00, ORA_8_30)

    def test_slot_respecta_limita_de_pauza(self):
        # slotul returnat nu poate fi prea aproape de o programare existenta
        scheduler = PlanificatorProgramari(pauza_minima=15)
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00)
        rezultat = scheduler.urmatorul_slot_liber(30)
        assert rezultat is not None
        # slotul trebuie sa fie fie inainte de pauza, fie dupa programare plus pauza
        assert rezultat[1] <= ORA_9_00 - 15 or rezultat[0] >= ORA_10_00 + 15


# ==============================================================================
# 7. TESTE SLOT OPTIM
# ==============================================================================

class TestSlotOptim:
    """
    Clase de echivalenta pentru slot_optim(durata, ora_preferata):
      EC1 - durata invalida
      EC2 - ora preferata in afara orelor de lucru
      EC3 - slot disponibil exact la ora preferata
      EC4 - ora preferata in zona ocupata, se gaseste slotul cel mai apropiat
      EC5 - niciun slot disponibil
    """

    def test_EC1_durata_invalida(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.slot_optim(0, ORA_10_00)

    def test_EC2_ora_preferata_in_afara(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.slot_optim(60, ORA_8_00 - 60)

    def test_EC3_slot_exact_la_ora_preferata(self):
        # ziua e libera, vrem 1h la 10:00, trebuie sa primim exact 10:00-11:00
        scheduler = PlanificatorProgramari()
        assert scheduler.slot_optim(60, ORA_10_00) == (ORA_10_00, ORA_10_00 + 60)

    def test_EC4_ora_preferata_ocupata(self):
        # Ana ocupa 9:00-11:00, vrem 1h cat mai aproape de 10:00
        # slotul de dupa Ana (11:00) este mai aproape de 10:00 decat cel de dinainte (8:00)
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_9_00, ORA_10_00 + 60)
        rezultat = scheduler.slot_optim(60, ORA_10_00)
        assert rezultat == (ORA_10_00 + 60, ORA_10_00 + 120)

    def test_EC5_niciun_slot(self):
        scheduler = PlanificatorProgramari()
        scheduler.rezerva("Ana", ORA_8_00, ORA_18_00)
        assert scheduler.slot_optim(60, ORA_10_00) is None


class TestFrontieraSlotOptim:
    """
    Valori de frontiera pentru slot_optim():
      BV1 - ora_preferata la inceputul zilei, valid
      BV2 - ora_preferata la sfarsitul zilei, valid
      BV3 - ora_preferata cu un minut inainte de zi, invalid
      BV4 - slot gasit exact la ora preferata, distanta 0
    """

    def test_BV1_preferinta_la_inceput_zilei(self):
        scheduler = PlanificatorProgramari()
        assert scheduler.slot_optim(60, ORA_8_00) == (ORA_8_00, ORA_9_00)

    def test_BV2_preferinta_la_sfarsitul_zilei(self):
        # start la 18:00 ar depasi ziua, asa ca se returneaza ultimul slot posibil
        scheduler = PlanificatorProgramari()
        assert scheduler.slot_optim(60, ORA_18_00) == (ORA_17_00, ORA_18_00)

    def test_BV3_preferinta_inainte_de_zi(self):
        scheduler = PlanificatorProgramari()
        with pytest.raises(ValueError):
            scheduler.slot_optim(60, ORA_8_00 - 1)

    def test_BV4_distanta_zero(self):
        # slotul se returneaza exact la ora preferata
        scheduler = PlanificatorProgramari()
        assert scheduler.slot_optim(60, ORA_12_00) == (ORA_12_00, ORA_12_00 + 60)
