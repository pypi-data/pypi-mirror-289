from setuptools import setup, find_packages

# Leer el contenido del archivo README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hack4u_SKY_Daxxx",
    version="0.1.0",
    packages=find_packages(), # es una utilidad que nos permite descubrir para el paquete que hemos creado todos los paquetes que existen
    install_requires=[],
    author="SKY_Daxxx",
    description="Una biblioteca para consultar los cursos de hack4u.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://hack4u.io"
)