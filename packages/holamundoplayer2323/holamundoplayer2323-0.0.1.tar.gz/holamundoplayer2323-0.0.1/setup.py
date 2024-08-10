import setuptools
from pathlib import Path

long_desc = Path("README.md").read_text()
setuptools.setup(
    name="holamundoplayer2323",
    version="0.0.1",
    long_description=long_desc,
    packages=setuptools.find_packages(exclude=["mocks", "test"]),
)
# CREAR EL EMPAQUETADO---
# python setup.py sdist bdist_wheel
#
# SDIST= SOURCE DISTRIBUTION
# BDIST= BUILD DISTRIBUTION
# CREAN DOS CARPETAS DE BUILD Y DIST ADEMAS DE OTRA .EGG-INFO
# DIST CONSTA DE UN TAR CON LOS ARCHIVOS COMPRIMIDOS

# SUBIR LOS PAQUETES A PYPI
# twine upload dist/*   -- Suba todo de la carpeta dist
WS
