##Ejercicio 3
Por que pide los paquetes: 
- ../tests/test_config.py as test_config
- ../tests/load_tests/ddos_simulation.py as ddos_simulation
Si estos paquetes no existen, yo los cree para que pueda pasar los assert

Este assert comparaba un paquete que no pedia importar en la actividad:
assert deploy_travis.name == "deploy_travis"
Lo solucione eliminando el assert pero no creo que este bien