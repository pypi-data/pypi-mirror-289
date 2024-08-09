# Este archivo nos sirve cuando a la hora de importar el paquete cuando haga "from hack4u" o "import hack4u" quiero que por 
# detras se importen los modulos correspondientes, con todas sus funciones y clases definidas

from .courses import *
# Esto nos permite hacer lo siguiente: from hack4u import list_courses (de lo contrario nos daria error ya que no sabe 
# "list_courses" en que modulo esta)

from .utils import *