"""
Classe Rectangle
"""
class Rectangle:

    """
    Constructeur de la classe
    @param longueur : correspond au longueur du rectangle
    @param largeur : correspond à la largeur du rectangle
    """
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur


    """
    Setter de l'attribut longueur
    @param longueur : nouvelle longueur
    """
    def setLongueur(self, longueur):
        self.longueur = longueur
        

    """
    Setter de l'attribut largeur
    @param largeur : nouvelle largeur
    """
    def setLargeur(self, largeur):
        self.largeur = largeur

    """
    Méthode perimetre : permet de calculer le perimetre du rectangle
    @return result : correspond au périmètre du rectanlge
    """
    def perimetre(self):
        result = (self.longueur * 2) + (self.largeur * 2)
        return result

    """
    Méthode surface : permet de calculer la surface du rectangle
    @return result : correspond à la surface du rectanlge
    """
    def surface(self):
        result = self.longueur * self.largeur
        return result

    """
    Méthode afficher : affiche les caractéristiques du rectangle
    """
    def afficher(self):
        print("Rectangle de longueur ", self.longueur, " et de largeur ", self.largeur)
        print("Périmètre du rectangle : ", self.perimetre())
        print("Surface du rectangle : ", self.surface())


    
    
rectangle_1 = Rectangle(20, 10)
rectangle_1.afficher()

print("\n")

print(rectangle_1.perimetre())
print(rectangle_1.surface())

print("\n")

rectangle_1.setLargeur(30)
rectangle_1.afficher()
print(rectangle_1.surface())

print("\n")

rectangle_1.setLongueur(15)
rectangle_1.afficher()

print("\n")

rectangle_1.setLargeur(-25)
rectangle_1.setLongueur(-45)
rectangle_1.afficher()



