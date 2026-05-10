import pytest
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from planificator_programari import PlanificatorProgramari


# I - Partitionare in clase de echivalenta

# rezerva()

# clasa valida: nume corect, interval valid, in program
def test_rezervare_normala():
    p = PlanificatorProgramari()
    assert p.rezerva("Ana", 480, 540) == True

# clasa invalida: nume gol
def test_rezervare_nume_gol():
    p = PlanificatorProgramari()
    with pytest.raises(ValueError):
        p.rezerva("", 480, 540)

# clasa invalida: start dupa stop
def test_rezervare_ore_gresite():
    p = PlanificatorProgramari()
    with pytest.raises(ValueError):
        p.rezerva("Ana", 480, 470)

# clasa invalida: interval suprapus cu o programare existenta
def test_doua_rezervari_aceeasi_ora():
    p = PlanificatorProgramari()
    p.rezerva("Ana", 500, 600)
    with pytest.raises(ValueError):
        p.rezerva("Iulian", 510, 700)

# clasa invalida: interval complet in afara orelor de lucru
def test_rezervare_in_afara_programului():
    p = PlanificatorProgramari()
    with pytest.raises(ValueError):
        p.rezerva("Ana", 300, 400)

# anuleaza()

# clasa valida: programarea exista
def test_anulare_existenta():
    p = PlanificatorProgramari()
    p.rezerva("Ana", 610, 620)
    assert p.anuleaza("Ana") == True

# clasa invalida: programarea nu exista
def test_anulare_inexistenta():
    p = PlanificatorProgramari()
    assert p.anuleaza("Ana") == False

# urmatorul_slot_liber()

# clasa valida: exista sloturi libere
def test_slot_liber_simplu():
    p = PlanificatorProgramari()
    assert p.urmatorul_slot_liber(30) is not None

# clasa invalida: zi complet ocupata
def test_slot_liber_ocupat():
    p = PlanificatorProgramari()
    p.rezerva("Ana", 480, 1080)
    assert p.urmatorul_slot_liber(30) is None

# clasa invalida: durata negativa
def test_slot_liber_durata_negativa():
    p = PlanificatorProgramari()
    with pytest.raises(ValueError):
        p.urmatorul_slot_liber(-10)

# este_liber()

# clasa valida: intervalul e liber
def test_este_liber_da():
    p = PlanificatorProgramari()
    assert p.este_liber(540, 600) == True

# clasa invalida: intervalul e ocupat
def test_este_liber_nu():
    p = PlanificatorProgramari()
    p.rezerva("Ana", 540, 600)
    assert p.este_liber(540, 600) == False

# get_programari()

# clasa valida: lista goala la inceput
def test_lista_goala_initial():
    p = PlanificatorProgramari()
    assert p.get_programari() == []

# clasa valida: lista are un element dupa rezervare
def test_lista_cu_o_programare():
    p = PlanificatorProgramari()
    p.rezerva("Ana", 540, 600)
    assert len(p.get_programari()) == 1

# slot_optim()

# clasa valida: zi libera, slot exact la ora preferata
def test_slot_optim_zi_libera():
    p = PlanificatorProgramari()
    assert p.slot_optim(60, 600) == (600, 660)

# clasa invalida: zi plina, niciun slot
def test_slot_optim_zi_plina():
    p = PlanificatorProgramari()
    p.rezerva("Ana", 480, 1080)
    assert p.slot_optim(60, 600) is None

# pauza_minima

# clasa invalida: pauza negativa
def test_pauza_negativa_invalida():
    with pytest.raises(ValueError):
        PlanificatorProgramari(pauza_minima=-5)

# clasa invalida: pauza insuficienta intre doua programari
def test_pauza_programari_prea_apropiate():
    p = PlanificatorProgramari(pauza_minima=10)
    p.rezerva("Ana", 540, 600)
    with pytest.raises(ValueError):
        p.rezerva("Bob", 605, 660)

# clasa valida: pauza respectata
def test_pauza_respectata():
    p = PlanificatorProgramari(pauza_minima=10)
    p.rezerva("Ana", 540, 600)
    assert p.rezerva("Bob", 610, 660) == True

# II - Analiza valorilor de frontiera

# rezerva()

# exact la limita de inceput a zilei (8:00 = 480 minute)
def test_frontiera_inceput_zi():
    p = PlanificatorProgramari()
    assert p.rezerva("Ana", 480, 540) == True

# exact la limita de sfarsit a zilei (18:00 = 1080 minute)
def test_frontiera_sfarsit_zi():
    p = PlanificatorProgramari()
    assert p.rezerva("Ana", 1020, 1080) == True

# start egal cu stop, durata zero nu are sens
def test_frontiera_start_egal_stop():
    p = PlanificatorProgramari()
    with pytest.raises(ValueError):
        p.rezerva("Ana", 480, 480)

# start cu un minut inainte de inceperea programului (7:59 = 479)
def test_frontiera_start_invalid():
    p = PlanificatorProgramari()
    with pytest.raises(ValueError):
        p.rezerva("Ana", 479, 800)

# stop cu un minut dupa sfarsitul programului (18:01 = 1081)
def test_frontiera_stop_invalid():
    p = PlanificatorProgramari()
    with pytest.raises(ValueError):
        p.rezerva("Ana", 480, 1081)

# durata de 1 minut, cel mai scurt interval posibil
def test_frontiera_durata_un_minut():
    p = PlanificatorProgramari()
    assert p.rezerva("Ana", 480, 481) == True

# doua programari care se ating exact, nu se suprapun
def test_frontiera_doua_cap_la_cap():
    p = PlanificatorProgramari()
    p.rezerva("Ana", 540, 600)
    assert p.rezerva("Bob", 600, 660) == True

# urmatorul_slot_liber()

# durata exact cat toata ziua (8:00-18:00 = 600 minute)
def test_frontiera_durata_exacta_zi():
    p = PlanificatorProgramari()
    assert p.urmatorul_slot_liber(600) is not None

# durata cu un minut mai mare decat ziua intreaga
def test_frontiera_durata_prea_mare():
    p = PlanificatorProgramari()
    assert p.urmatorul_slot_liber(601) is None

# III - Acoperire la nivel de instructiune / decizie / conditie

# ramura: nume None - eroare (conditie isinstance)
def test_acoperire_nume_none():
    p = PlanificatorProgramari()
    with pytest.raises(ValueError):
        p.rezerva(None, 540, 600)

# ramura: nume doar spatii - eroare (conditie strip)
def test_acoperire_nume_doar_spatii():
    p = PlanificatorProgramari()
    with pytest.raises(ValueError):
        p.rezerva("   ", 540, 600)

# ramura: start mai mic strict decat sfarsit - programare valida
def test_acoperire_interval_valid():
    p = PlanificatorProgramari()
    assert p.rezerva("Ana", 540, 541) == True

# ramura: start egal cu sfarsit - eroare
def test_acoperire_interval_zero():
    p = PlanificatorProgramari()
    with pytest.raises(ValueError):
        p.rezerva("Ana", 540, 540)

# ramura: in orele de lucru - ok
def test_acoperire_in_program():
    p = PlanificatorProgramari()
    assert p.rezerva("Ana", 600, 660) == True

# ramura: in afara orelor de lucru - eroare
def test_acoperire_in_afara():
    p = PlanificatorProgramari()
    with pytest.raises(ValueError):
        p.rezerva("Ana", 200, 300)

# ramura: intervalul e liber - True
def test_acoperire_este_liber_true():
    p = PlanificatorProgramari()
    assert p.este_liber(600, 660) == True

# ramura: intervalul e ocupat - False
def test_acoperire_este_liber_false():
    p = PlanificatorProgramari()
    p.rezerva("Ana", 600, 660)
    assert p.este_liber(620, 640) == False

# ramura: anuleaza returneaza True cand gaseste
def test_acoperire_anulare_gasit():
    p = PlanificatorProgramari()
    p.rezerva("Ion", 600, 660)
    assert p.anuleaza("Ion") == True

# ramura: anuleaza returneaza False cand nu gaseste
def test_acoperire_anulare_negasit():
    p = PlanificatorProgramari()
    assert p.anuleaza("Ion") == False


# IV - Circuite independente (complexitate ciclomatica McCabe)

# rezerva() are 4 conditii de validare
# fiecare test parcurge o cale diferita prin functie

# calea 1: validare nume esueaza
def test_circuit_P1_nume_invalid():
    p = PlanificatorProgramari()
    with pytest.raises(ValueError):
        p.rezerva("", 540, 600)

# calea 2: validare interval esueaza
def test_circuit_P2_interval_invalid():
    p = PlanificatorProgramari()
    with pytest.raises(ValueError):
        p.rezerva("Ana", 600, 540)

# calea 3: interval in afara orelor de lucru
def test_circuit_P3_afara_program():
    p = PlanificatorProgramari()
    with pytest.raises(ValueError):
        p.rezerva("Ana", 100, 200)

# calea 4: interval ocupat
def test_circuit_P4_ocupat():
    p = PlanificatorProgramari()
    p.rezerva("Ana", 540, 600)
    with pytest.raises(ValueError):
        p.rezerva("Bob", 540, 600)

# calea 5: toate validarile trec, rezervarea se face
def test_circuit_P5_succes():
    p = PlanificatorProgramari()
    assert p.rezerva("Ana", 540, 600) == True


# V - Teste suplimentare pentru mutanti
# ucide mutantul 67: schimba "durata <= 0" in "durata <= 1"
# efectul: slot_optim(1, ...) ar arunca eroare gresit
# testul verifica ca durata de 1 minut este acceptata
def test_mutant_slot_optim_durata_unu():
    p = PlanificatorProgramari()
    assert p.slot_optim(1, 600) is not None

# ucide mutantul 87: schimba "distanta < distanta_minima" in "distanta <= distanta_minima"
# efectul: cand doua sloturi sunt la distanta egala, se returneaza ultimul in loc de primul
# testul verifica ca se returneaza primul slot gasit (cel mai devreme)
def test_mutant_slot_optim_distanta_egala():
    p = PlanificatorProgramari()
    p.rezerva("Ana", 540, 720)
    assert p.slot_optim(60, 600) == (480, 540)
