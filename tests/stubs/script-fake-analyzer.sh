#!/bin/bash
#Simula el funcionamiento de un binario, recibe parametros y devuelve códigos de salida

if [ "$1" == "parametro-incorrecto1" ]; then
    echo "Error en la ejecución"
    exit 0
fi

if ["$2"== "parametro-incorrecto2"]; then
    echo "Error en la ejecución"
    exit 0
fi

if [ "$1" == "parametro-correcto" && "$2"=="parametro-corecto"]; then
    echo "Ejecución exitosa"
    exit 0
fi