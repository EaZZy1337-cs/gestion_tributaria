from datetime import datetime

from rest_framework.exceptions import ValidationError

from apps.tributario.repositories import CalificacionRepository


class CalificacionService:
    """
    Servicio encargado de gestionar las Calificaciones Tributarias.

    Historia de Usuario:
    HU-01 - Registrar Calificación Tributaria.

    Responsabilidades:
    - Registrar nuevas calificaciones.
    - Validar reglas de negocio.
    - Evitar registros duplicados.
    - Validar consistencia entre Instrumento y Dividendo.
    """

    @staticmethod
    def listar():
        return CalificacionRepository.listar()

    @staticmethod
    def obtener(pk):
        return CalificacionRepository.obtener(pk)

    @staticmethod
    def registrar_calificacion(datos):

        ejercicio = datos["ejercicio"]

        año_actual = datetime.now().year

        if ejercicio < 2000 or ejercicio > año_actual + 1:
            raise ValidationError(
                "El ejercicio ingresado no es válido."
            )

        if datos["dividendo"].instrumento != datos["instrumento"]:
            raise ValidationError(
                "El dividendo seleccionado no pertenece al instrumento."
            )

        existe = CalificacionRepository.existe(
            datos["instrumento"],
            ejercicio,
            datos["numero_evento"],
        )

        if existe:
            raise ValidationError(
                "Ya existe una calificación para ese instrumento, ejercicio y evento."
            )

        return CalificacionRepository.crear(**datos)

    @staticmethod
    def actualizar_calificacion(instancia, datos):

        if instancia.estado != "ACTIVO":
            raise ValidationError(
                "Solo pueden modificarse calificaciones activas."
            )

        return CalificacionRepository.actualizar(
            instancia,
            **datos,
        )

    @staticmethod
    def eliminar(instancia):

        if instancia.estado != "ACTIVO":
            raise ValidationError(
                "La calificación ya se encuentra inactiva."
            )

        CalificacionRepository.eliminar(instancia)