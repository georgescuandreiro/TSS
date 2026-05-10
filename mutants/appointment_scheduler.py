# Clasa pentru gestionarea programarilor intr-o zi de lucru.
# Timpul este reprezentat in minute fata de miezul noptii.
# Exemplu: 8:00 = 480, 9:30 = 570, 17:45 = 1065


from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore
class AppointmentScheduler:

    def __init__(self, ora_inceput=8, ora_sfarsit=18):
        args = [ora_inceput, ora_sfarsit]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁAppointmentSchedulerǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁAppointmentSchedulerǁ__init____mutmut_mutants'), args, kwargs, self)

    def xǁAppointmentSchedulerǁ__init____mutmut_orig(self, ora_inceput=8, ora_sfarsit=18):
        # programarile sunt stocate ca o lista de dictionare
        self.programari = []
        # convertim orele de lucru in minute
        self.ora_inceput = ora_inceput * 60
        self.ora_sfarsit = ora_sfarsit * 60

    def xǁAppointmentSchedulerǁ__init____mutmut_1(self, ora_inceput=9, ora_sfarsit=18):
        # programarile sunt stocate ca o lista de dictionare
        self.programari = []
        # convertim orele de lucru in minute
        self.ora_inceput = ora_inceput * 60
        self.ora_sfarsit = ora_sfarsit * 60

    def xǁAppointmentSchedulerǁ__init____mutmut_2(self, ora_inceput=8, ora_sfarsit=19):
        # programarile sunt stocate ca o lista de dictionare
        self.programari = []
        # convertim orele de lucru in minute
        self.ora_inceput = ora_inceput * 60
        self.ora_sfarsit = ora_sfarsit * 60

    def xǁAppointmentSchedulerǁ__init____mutmut_3(self, ora_inceput=8, ora_sfarsit=18):
        # programarile sunt stocate ca o lista de dictionare
        self.programari = None
        # convertim orele de lucru in minute
        self.ora_inceput = ora_inceput * 60
        self.ora_sfarsit = ora_sfarsit * 60

    def xǁAppointmentSchedulerǁ__init____mutmut_4(self, ora_inceput=8, ora_sfarsit=18):
        # programarile sunt stocate ca o lista de dictionare
        self.programari = []
        # convertim orele de lucru in minute
        self.ora_inceput = None
        self.ora_sfarsit = ora_sfarsit * 60

    def xǁAppointmentSchedulerǁ__init____mutmut_5(self, ora_inceput=8, ora_sfarsit=18):
        # programarile sunt stocate ca o lista de dictionare
        self.programari = []
        # convertim orele de lucru in minute
        self.ora_inceput = ora_inceput / 60
        self.ora_sfarsit = ora_sfarsit * 60

    def xǁAppointmentSchedulerǁ__init____mutmut_6(self, ora_inceput=8, ora_sfarsit=18):
        # programarile sunt stocate ca o lista de dictionare
        self.programari = []
        # convertim orele de lucru in minute
        self.ora_inceput = ora_inceput * 61
        self.ora_sfarsit = ora_sfarsit * 60

    def xǁAppointmentSchedulerǁ__init____mutmut_7(self, ora_inceput=8, ora_sfarsit=18):
        # programarile sunt stocate ca o lista de dictionare
        self.programari = []
        # convertim orele de lucru in minute
        self.ora_inceput = ora_inceput * 60
        self.ora_sfarsit = None

    def xǁAppointmentSchedulerǁ__init____mutmut_8(self, ora_inceput=8, ora_sfarsit=18):
        # programarile sunt stocate ca o lista de dictionare
        self.programari = []
        # convertim orele de lucru in minute
        self.ora_inceput = ora_inceput * 60
        self.ora_sfarsit = ora_sfarsit / 60

    def xǁAppointmentSchedulerǁ__init____mutmut_9(self, ora_inceput=8, ora_sfarsit=18):
        # programarile sunt stocate ca o lista de dictionare
        self.programari = []
        # convertim orele de lucru in minute
        self.ora_inceput = ora_inceput * 60
        self.ora_sfarsit = ora_sfarsit * 61
    
    xǁAppointmentSchedulerǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁAppointmentSchedulerǁ__init____mutmut_1': xǁAppointmentSchedulerǁ__init____mutmut_1, 
        'xǁAppointmentSchedulerǁ__init____mutmut_2': xǁAppointmentSchedulerǁ__init____mutmut_2, 
        'xǁAppointmentSchedulerǁ__init____mutmut_3': xǁAppointmentSchedulerǁ__init____mutmut_3, 
        'xǁAppointmentSchedulerǁ__init____mutmut_4': xǁAppointmentSchedulerǁ__init____mutmut_4, 
        'xǁAppointmentSchedulerǁ__init____mutmut_5': xǁAppointmentSchedulerǁ__init____mutmut_5, 
        'xǁAppointmentSchedulerǁ__init____mutmut_6': xǁAppointmentSchedulerǁ__init____mutmut_6, 
        'xǁAppointmentSchedulerǁ__init____mutmut_7': xǁAppointmentSchedulerǁ__init____mutmut_7, 
        'xǁAppointmentSchedulerǁ__init____mutmut_8': xǁAppointmentSchedulerǁ__init____mutmut_8, 
        'xǁAppointmentSchedulerǁ__init____mutmut_9': xǁAppointmentSchedulerǁ__init____mutmut_9
    }
    xǁAppointmentSchedulerǁ__init____mutmut_orig.__name__ = 'xǁAppointmentSchedulerǁ__init__'

    def rezerva(self, nume, start, sfarsit):
        args = [nume, start, sfarsit]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁAppointmentSchedulerǁrezerva__mutmut_orig'), object.__getattribute__(self, 'xǁAppointmentSchedulerǁrezerva__mutmut_mutants'), args, kwargs, self)

    def xǁAppointmentSchedulerǁrezerva__mutmut_orig(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_1(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) and nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_2(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_3(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() != "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_4(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "XXXX":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_5(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError(None)

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_6(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("XXNumele nu poate fi golXX")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_7(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_8(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("NUMELE NU POATE FI GOL")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_9(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start > sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_10(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError(None)

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_11(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("XXOra de start trebuie sa fie inainte de sfarsitXX")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_12(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_13(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("ORA DE START TREBUIE SA FIE INAINTE DE SFARSIT")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_14(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput and sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_15(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start <= self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_16(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit >= self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_17(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError(None)

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_18(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("XXProgramarea este in afara orelor de lucruXX")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_19(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_20(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("PROGRAMAREA ESTE IN AFARA ORELOR DE LUCRU")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_21(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_22(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(None, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_23(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, None):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_24(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_25(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, ):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_26(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError(None)

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_27(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("XXIntervalul ales este deja ocupatXX")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_28(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_29(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("INTERVALUL ALES ESTE DEJA OCUPAT")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_30(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = None
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_31(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"XXnumeXX": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_32(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"NUME": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_33(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "XXstartXX": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_34(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "START": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_35(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "XXsfarsitXX": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_36(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "SFARSIT": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_37(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(None)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_38(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=None)
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_39(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: None)
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_40(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["XXstartXX"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_41(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["START"])
        return True

    def xǁAppointmentSchedulerǁrezerva__mutmut_42(self, nume, start, sfarsit):
        # verificam ca numele sa fie un string nevid
        if not isinstance(nume, str) or nume.strip() == "":
            raise ValueError("Numele nu poate fi gol")

        # intervalul trebuie sa aiba durata pozitiva
        if start >= sfarsit:
            raise ValueError("Ora de start trebuie sa fie inainte de sfarsit")

        # programarea trebuie sa fie in cadrul orelor de lucru
        if start < self.ora_inceput or sfarsit > self.ora_sfarsit:
            raise ValueError("Programarea este in afara orelor de lucru")

        # verificam sa nu se suprapuna cu o alta programare existenta
        if not self.este_liber(start, sfarsit):
            raise ValueError("Intervalul ales este deja ocupat")

        programare = {"nume": nume, "start": start, "sfarsit": sfarsit}
        self.programari.append(programare)

        # mentinem lista sortata dupa ora de start
        self.programari.sort(key=lambda x: x["start"])
        return False
    
    xǁAppointmentSchedulerǁrezerva__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁAppointmentSchedulerǁrezerva__mutmut_1': xǁAppointmentSchedulerǁrezerva__mutmut_1, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_2': xǁAppointmentSchedulerǁrezerva__mutmut_2, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_3': xǁAppointmentSchedulerǁrezerva__mutmut_3, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_4': xǁAppointmentSchedulerǁrezerva__mutmut_4, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_5': xǁAppointmentSchedulerǁrezerva__mutmut_5, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_6': xǁAppointmentSchedulerǁrezerva__mutmut_6, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_7': xǁAppointmentSchedulerǁrezerva__mutmut_7, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_8': xǁAppointmentSchedulerǁrezerva__mutmut_8, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_9': xǁAppointmentSchedulerǁrezerva__mutmut_9, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_10': xǁAppointmentSchedulerǁrezerva__mutmut_10, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_11': xǁAppointmentSchedulerǁrezerva__mutmut_11, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_12': xǁAppointmentSchedulerǁrezerva__mutmut_12, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_13': xǁAppointmentSchedulerǁrezerva__mutmut_13, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_14': xǁAppointmentSchedulerǁrezerva__mutmut_14, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_15': xǁAppointmentSchedulerǁrezerva__mutmut_15, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_16': xǁAppointmentSchedulerǁrezerva__mutmut_16, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_17': xǁAppointmentSchedulerǁrezerva__mutmut_17, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_18': xǁAppointmentSchedulerǁrezerva__mutmut_18, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_19': xǁAppointmentSchedulerǁrezerva__mutmut_19, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_20': xǁAppointmentSchedulerǁrezerva__mutmut_20, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_21': xǁAppointmentSchedulerǁrezerva__mutmut_21, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_22': xǁAppointmentSchedulerǁrezerva__mutmut_22, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_23': xǁAppointmentSchedulerǁrezerva__mutmut_23, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_24': xǁAppointmentSchedulerǁrezerva__mutmut_24, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_25': xǁAppointmentSchedulerǁrezerva__mutmut_25, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_26': xǁAppointmentSchedulerǁrezerva__mutmut_26, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_27': xǁAppointmentSchedulerǁrezerva__mutmut_27, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_28': xǁAppointmentSchedulerǁrezerva__mutmut_28, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_29': xǁAppointmentSchedulerǁrezerva__mutmut_29, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_30': xǁAppointmentSchedulerǁrezerva__mutmut_30, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_31': xǁAppointmentSchedulerǁrezerva__mutmut_31, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_32': xǁAppointmentSchedulerǁrezerva__mutmut_32, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_33': xǁAppointmentSchedulerǁrezerva__mutmut_33, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_34': xǁAppointmentSchedulerǁrezerva__mutmut_34, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_35': xǁAppointmentSchedulerǁrezerva__mutmut_35, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_36': xǁAppointmentSchedulerǁrezerva__mutmut_36, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_37': xǁAppointmentSchedulerǁrezerva__mutmut_37, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_38': xǁAppointmentSchedulerǁrezerva__mutmut_38, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_39': xǁAppointmentSchedulerǁrezerva__mutmut_39, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_40': xǁAppointmentSchedulerǁrezerva__mutmut_40, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_41': xǁAppointmentSchedulerǁrezerva__mutmut_41, 
        'xǁAppointmentSchedulerǁrezerva__mutmut_42': xǁAppointmentSchedulerǁrezerva__mutmut_42
    }
    xǁAppointmentSchedulerǁrezerva__mutmut_orig.__name__ = 'xǁAppointmentSchedulerǁrezerva'

    def anuleaza(self, nume):
        args = [nume]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁAppointmentSchedulerǁanuleaza__mutmut_orig'), object.__getattribute__(self, 'xǁAppointmentSchedulerǁanuleaza__mutmut_mutants'), args, kwargs, self)

    def xǁAppointmentSchedulerǁanuleaza__mutmut_orig(self, nume):
        # cautam programarea dupa nume si o stergem daca o gasim
        for programare in self.programari:
            if programare["nume"] == nume:
                self.programari.remove(programare)
                return True

        # nu am gasit nicio programare cu numele dat
        return False

    def xǁAppointmentSchedulerǁanuleaza__mutmut_1(self, nume):
        # cautam programarea dupa nume si o stergem daca o gasim
        for programare in self.programari:
            if programare["XXnumeXX"] == nume:
                self.programari.remove(programare)
                return True

        # nu am gasit nicio programare cu numele dat
        return False

    def xǁAppointmentSchedulerǁanuleaza__mutmut_2(self, nume):
        # cautam programarea dupa nume si o stergem daca o gasim
        for programare in self.programari:
            if programare["NUME"] == nume:
                self.programari.remove(programare)
                return True

        # nu am gasit nicio programare cu numele dat
        return False

    def xǁAppointmentSchedulerǁanuleaza__mutmut_3(self, nume):
        # cautam programarea dupa nume si o stergem daca o gasim
        for programare in self.programari:
            if programare["nume"] != nume:
                self.programari.remove(programare)
                return True

        # nu am gasit nicio programare cu numele dat
        return False

    def xǁAppointmentSchedulerǁanuleaza__mutmut_4(self, nume):
        # cautam programarea dupa nume si o stergem daca o gasim
        for programare in self.programari:
            if programare["nume"] == nume:
                self.programari.remove(None)
                return True

        # nu am gasit nicio programare cu numele dat
        return False

    def xǁAppointmentSchedulerǁanuleaza__mutmut_5(self, nume):
        # cautam programarea dupa nume si o stergem daca o gasim
        for programare in self.programari:
            if programare["nume"] == nume:
                self.programari.remove(programare)
                return False

        # nu am gasit nicio programare cu numele dat
        return False

    def xǁAppointmentSchedulerǁanuleaza__mutmut_6(self, nume):
        # cautam programarea dupa nume si o stergem daca o gasim
        for programare in self.programari:
            if programare["nume"] == nume:
                self.programari.remove(programare)
                return True

        # nu am gasit nicio programare cu numele dat
        return True
    
    xǁAppointmentSchedulerǁanuleaza__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁAppointmentSchedulerǁanuleaza__mutmut_1': xǁAppointmentSchedulerǁanuleaza__mutmut_1, 
        'xǁAppointmentSchedulerǁanuleaza__mutmut_2': xǁAppointmentSchedulerǁanuleaza__mutmut_2, 
        'xǁAppointmentSchedulerǁanuleaza__mutmut_3': xǁAppointmentSchedulerǁanuleaza__mutmut_3, 
        'xǁAppointmentSchedulerǁanuleaza__mutmut_4': xǁAppointmentSchedulerǁanuleaza__mutmut_4, 
        'xǁAppointmentSchedulerǁanuleaza__mutmut_5': xǁAppointmentSchedulerǁanuleaza__mutmut_5, 
        'xǁAppointmentSchedulerǁanuleaza__mutmut_6': xǁAppointmentSchedulerǁanuleaza__mutmut_6
    }
    xǁAppointmentSchedulerǁanuleaza__mutmut_orig.__name__ = 'xǁAppointmentSchedulerǁanuleaza'

    def este_liber(self, start, sfarsit):
        args = [start, sfarsit]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁAppointmentSchedulerǁeste_liber__mutmut_orig'), object.__getattribute__(self, 'xǁAppointmentSchedulerǁeste_liber__mutmut_mutants'), args, kwargs, self)

    def xǁAppointmentSchedulerǁeste_liber__mutmut_orig(self, start, sfarsit):
        # doua intervale [a, b] si [c, d] se suprapun daca a < d si b > c
        for programare in self.programari:
            if start < programare["sfarsit"] and sfarsit > programare["start"]:
                return False
        return True

    def xǁAppointmentSchedulerǁeste_liber__mutmut_1(self, start, sfarsit):
        # doua intervale [a, b] si [c, d] se suprapun daca a < d si b > c
        for programare in self.programari:
            if start < programare["sfarsit"] or sfarsit > programare["start"]:
                return False
        return True

    def xǁAppointmentSchedulerǁeste_liber__mutmut_2(self, start, sfarsit):
        # doua intervale [a, b] si [c, d] se suprapun daca a < d si b > c
        for programare in self.programari:
            if start <= programare["sfarsit"] and sfarsit > programare["start"]:
                return False
        return True

    def xǁAppointmentSchedulerǁeste_liber__mutmut_3(self, start, sfarsit):
        # doua intervale [a, b] si [c, d] se suprapun daca a < d si b > c
        for programare in self.programari:
            if start < programare["XXsfarsitXX"] and sfarsit > programare["start"]:
                return False
        return True

    def xǁAppointmentSchedulerǁeste_liber__mutmut_4(self, start, sfarsit):
        # doua intervale [a, b] si [c, d] se suprapun daca a < d si b > c
        for programare in self.programari:
            if start < programare["SFARSIT"] and sfarsit > programare["start"]:
                return False
        return True

    def xǁAppointmentSchedulerǁeste_liber__mutmut_5(self, start, sfarsit):
        # doua intervale [a, b] si [c, d] se suprapun daca a < d si b > c
        for programare in self.programari:
            if start < programare["sfarsit"] and sfarsit >= programare["start"]:
                return False
        return True

    def xǁAppointmentSchedulerǁeste_liber__mutmut_6(self, start, sfarsit):
        # doua intervale [a, b] si [c, d] se suprapun daca a < d si b > c
        for programare in self.programari:
            if start < programare["sfarsit"] and sfarsit > programare["XXstartXX"]:
                return False
        return True

    def xǁAppointmentSchedulerǁeste_liber__mutmut_7(self, start, sfarsit):
        # doua intervale [a, b] si [c, d] se suprapun daca a < d si b > c
        for programare in self.programari:
            if start < programare["sfarsit"] and sfarsit > programare["START"]:
                return False
        return True

    def xǁAppointmentSchedulerǁeste_liber__mutmut_8(self, start, sfarsit):
        # doua intervale [a, b] si [c, d] se suprapun daca a < d si b > c
        for programare in self.programari:
            if start < programare["sfarsit"] and sfarsit > programare["start"]:
                return True
        return True

    def xǁAppointmentSchedulerǁeste_liber__mutmut_9(self, start, sfarsit):
        # doua intervale [a, b] si [c, d] se suprapun daca a < d si b > c
        for programare in self.programari:
            if start < programare["sfarsit"] and sfarsit > programare["start"]:
                return False
        return False
    
    xǁAppointmentSchedulerǁeste_liber__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁAppointmentSchedulerǁeste_liber__mutmut_1': xǁAppointmentSchedulerǁeste_liber__mutmut_1, 
        'xǁAppointmentSchedulerǁeste_liber__mutmut_2': xǁAppointmentSchedulerǁeste_liber__mutmut_2, 
        'xǁAppointmentSchedulerǁeste_liber__mutmut_3': xǁAppointmentSchedulerǁeste_liber__mutmut_3, 
        'xǁAppointmentSchedulerǁeste_liber__mutmut_4': xǁAppointmentSchedulerǁeste_liber__mutmut_4, 
        'xǁAppointmentSchedulerǁeste_liber__mutmut_5': xǁAppointmentSchedulerǁeste_liber__mutmut_5, 
        'xǁAppointmentSchedulerǁeste_liber__mutmut_6': xǁAppointmentSchedulerǁeste_liber__mutmut_6, 
        'xǁAppointmentSchedulerǁeste_liber__mutmut_7': xǁAppointmentSchedulerǁeste_liber__mutmut_7, 
        'xǁAppointmentSchedulerǁeste_liber__mutmut_8': xǁAppointmentSchedulerǁeste_liber__mutmut_8, 
        'xǁAppointmentSchedulerǁeste_liber__mutmut_9': xǁAppointmentSchedulerǁeste_liber__mutmut_9
    }
    xǁAppointmentSchedulerǁeste_liber__mutmut_orig.__name__ = 'xǁAppointmentSchedulerǁeste_liber'

    def get_programari(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁAppointmentSchedulerǁget_programari__mutmut_orig'), object.__getattribute__(self, 'xǁAppointmentSchedulerǁget_programari__mutmut_mutants'), args, kwargs, self)

    def xǁAppointmentSchedulerǁget_programari__mutmut_orig(self):
        # returnam o copie a listei ca sa nu fie modificata din exterior
        return list(self.programari)

    def xǁAppointmentSchedulerǁget_programari__mutmut_1(self):
        # returnam o copie a listei ca sa nu fie modificata din exterior
        return list(None)
    
    xǁAppointmentSchedulerǁget_programari__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁAppointmentSchedulerǁget_programari__mutmut_1': xǁAppointmentSchedulerǁget_programari__mutmut_1
    }
    xǁAppointmentSchedulerǁget_programari__mutmut_orig.__name__ = 'xǁAppointmentSchedulerǁget_programari'

    def urmatorul_slot_liber(self, durata):
        args = [durata]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_orig'), object.__getattribute__(self, 'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_mutants'), args, kwargs, self)

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_orig(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_1(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata < 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_2(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 1:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_3(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError(None)

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_4(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("XXDurata trebuie sa fie un numar pozitiv de minuteXX")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_5(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_6(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("DURATA TREBUIE SA FIE UN NUMAR POZITIV DE MINUTE")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_7(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = None

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_8(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] + curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_9(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["XXstartXX"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_10(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["START"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_11(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent > durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_12(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent - durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_13(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["XXsfarsitXX"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_14(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["SFARSIT"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_15(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] >= curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_16(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = None

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_17(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["XXsfarsitXX"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_18(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["SFARSIT"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_19(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit + curent >= durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_20(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent > durata:
            return (curent, curent + durata)

        # nu exista niciun slot disponibil
        return None

    def xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_21(self, durata):
        # durata trebuie sa fie strict pozitiva
        if durata <= 0:
            raise ValueError("Durata trebuie sa fie un numar pozitiv de minute")

        # cautam incepand de la prima ora disponibila din zi
        curent = self.ora_inceput

        for programare in self.programari:
            # verificam daca incape un slot de durata ceruta inainte de programarea curenta
            if programare["start"] - curent >= durata:
                return (curent, curent + durata)

            # daca programarea se termina dupa pozitia curenta, avansam
            if programare["sfarsit"] > curent:
                curent = programare["sfarsit"]

        # verificam daca mai este loc dupa ultima programare
        if self.ora_sfarsit - curent >= durata:
            return (curent, curent - durata)

        # nu exista niciun slot disponibil
        return None
    
    xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_1': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_1, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_2': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_2, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_3': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_3, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_4': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_4, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_5': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_5, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_6': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_6, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_7': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_7, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_8': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_8, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_9': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_9, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_10': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_10, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_11': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_11, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_12': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_12, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_13': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_13, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_14': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_14, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_15': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_15, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_16': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_16, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_17': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_17, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_18': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_18, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_19': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_19, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_20': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_20, 
        'xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_21': xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_21
    }
    xǁAppointmentSchedulerǁurmatorul_slot_liber__mutmut_orig.__name__ = 'xǁAppointmentSchedulerǁurmatorul_slot_liber'
