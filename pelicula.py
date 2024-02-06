import uuid


class Pelicula:
    def __init__(self, titulo, anio, director):
        self.titulo = titulo       
        self.anio = anio
        self.director = director
        self._id = uuid.uuid4().hex 

    def get_id(self): #método getter
        return self._id


