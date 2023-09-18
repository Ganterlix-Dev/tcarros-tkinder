from models.modelo_vehiculo import mecanic as mecanico

class meca():
    @classmethod
    def select_all(self):
        mec = mecanico.select_all()
        return {"error": False, "msg": mec}
    