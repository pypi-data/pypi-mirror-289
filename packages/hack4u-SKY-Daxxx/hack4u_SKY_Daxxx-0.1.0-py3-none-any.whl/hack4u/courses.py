class Course:

    def __init__(self, name, duration, link):
        self.name = name
        self.duration = duration
        self.link = link

    def __repr__(self): # otra forma de representar informacion (__repr__) 
        return f"{self.name} [{self.duration} horas] ({self.link})"

# Creamos una lista de objetos
# Creamos objetos temporales que no almacenamos en variables pero sean instancias de la clase para que sean 
# recogidos como una lista de objetos
courses = [
    Course("Introducion a Linux", 15, "https://hack4u.io/cursos/introduccion-a-linux/"),
    Course("Personalizacion de Linux", 3, "https://hack4u.io/cursos/personalizacion-de-entorno-en-linux/"),
    Course("Introduccion al Hacking", 53, "https://hack4u.io/cursos/introduccion-al-hacking/")
]

def list_courses():
    for course in courses:
        print(course)

def search_course_by_name(name):
    for course in courses:
        if course.name == name:
            return course
        
    return None