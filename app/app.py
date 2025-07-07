import subprocess
import requests

# Clase que ejecuta un analizador externo
class ExternalAnalyzer:

    def __init__(self):
        self.apikey = "none"
        self.set_path_binary_file()
        
    def set_path_binary_file(self):
        self.path_binary_file = "/usr/local/bin/externarl-analyzer"

    def run(self):
        # Ejecutar el binario con subproccess
        subprocess.run([self.path_binary_file], check=True)

    # llamado a API REST
    def search_api(self) -> dict:
        resultados = requests.get(f"https://imdb-api.com/API/SearchTitle/{self.apikey}/")
        if resultados.status_code == 200: 
            return resultados.json()
        return {}