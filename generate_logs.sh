##!/bin/bash
# ejecutar scripts .sh para redirigir la salida a un archivo de log

# tambieen redirige el error 
bash manage_deployment.sh > logs/deploy.log 2>&1
bash tests/stubs/script-fake-analyzer.sh parametro-correcto parametro-corecto > logs/fake-analyzer.log 2>&1