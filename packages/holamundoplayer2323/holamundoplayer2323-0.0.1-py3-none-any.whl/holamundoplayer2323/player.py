"""
Esta es la documentacion de player
incluye la clase de reproductor de musica
"""


class Player:
    """
    Esta clase crea un reproductor de musica
    """

    def play(self, song):
        """
        Reproduce la cancion que recibio como parametro

        Parameters:
        song (str): este es un str con el path de la cancion

        Returns:
        int: devuelve 1 si reproduce con exito, en caso de fracaso devuelve 0
        """
        print("Reproduciendo canción")

    def stop(self):
        print("stopping")
