from src.seleccionestudiante.modelo.Asignatura import Asignatura
from src.seleccionestudiante.modelo.declarative_base import engine, Base, session


class GestionAsignatura():

    def __init__(self):
        Base.metadata.create_all(engine)

    def agregar_asignatura(self, nombreAsignatura):
        if len(nombreAsignatura) == 0:
            return False
        busqueda = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombreAsignatura).all()
        if len(busqueda) == 0:
            asignatura = Asignatura(nombreAsignatura=nombreAsignatura)
            session.add(asignatura)
            session.commit()
            return True
        else:
            return False

    def editar_asignatura(self, nombreAsignatura, nombreNuevo):
        if len(nombreAsignatura) == 0 or len(nombreNuevo) == 0:
            return False
        asignatura = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombreAsignatura).all()
        if len(asignatura) != 0:
            nombreNuevo = nombreNuevo.title()
            session.query(Asignatura).filter_by(nombreAsignatura=nombreAsignatura).update({"nombreAsignatura": nombreNuevo})
            session.commit()
            return True
        else:
            return False
