
from setuptools import setup

with open("README.rst", "r", encoding="utf-8") as hoja:
    long_description = hoja.read()

setup(
        name= "consigue",
        version= "1.0",
        author= "El Señor es el único eterno. Que la ciencia lo honre a Él.",
        author_email= "from.colombia.to.all@gmail.com",

        description= "Tratamiento de Datos mediante fases de procesos",
        long_description=long_description,
        long_description_content_type="text/x-rst",
        
        license="Mozilla Public License 2.0 (MPL 2.0)",
        license_files=("license.txt",),
        
        packages= ["consigue"],
        
        package_data={
            '': ['license.txt'],
        },
        include_package_data= True,
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        ],
        
        python_requires= ">=3.11.3"
        #install_requires=['matplotlib', 'Pillow'],
)

