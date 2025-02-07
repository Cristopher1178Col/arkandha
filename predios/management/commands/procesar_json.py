from django.core.management.base import BaseCommand
import os, re, json

class Command(BaseCommand):
    help = 'Procesa archivos JSON para extraer códigos de especificación de anotaciones'

    def extract_specification_codes(self, text):
        """Extrae códigos de especificación con 3 a 5 dígitos después de 'ESPECIFICACION:'"""
        return re.findall(r'ESPECIFICACION:\s*([0-9]{3,5})', text)

    def handle(self, *args, **options):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        data_dir = os.path.join(base_dir, 'data')
        if not os.path.isdir(data_dir):
            self.stdout.write(self.style.ERROR(f'La carpeta de datos no existe: {data_dir}'))
            return

        results = []
        for filename in os.listdir(data_dir):
            if not filename.endswith('.json'):
                continue
            file_path = os.path.join(data_dir, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except json.JSONDecodeError as e:
                self.stdout.write(self.style.ERROR(f'Error al decodificar {filename}: {e}'))
                continue

            # El archivo de json esta en fomrmato diccionario, aca se envuelve en una lista
            if isinstance(data, dict):
                if 'textoAnotaciones' in data:
                    data = [data]
                else:
                    self.stdout.write(self.style.ERROR(f'Formato incorrecto en {filename}: No se encontró "textoAnotaciones".'))
                    continue
            elif not isinstance(data, list):
                self.stdout.write(self.style.ERROR(f'Formato inesperado en {filename}: {type(data)}'))
                continue

            for predio in data:
                if not isinstance(predio, dict):
                    self.stdout.write(self.style.ERROR(f'Error en {filename}: Se esperaba un diccionario, pero se encontró {type(predio).__name__}.'))
                    continue
                nombre = predio.get('nombre', 'N/A')
                anotaciones = predio.get('textoAnotaciones', '')
                full_text = " ".join(anotaciones) if isinstance(anotaciones, list) else (anotaciones if isinstance(anotaciones, str) else '')
                full_text = re.sub(r'<br\s*/?>', ' ', full_text)
                codes = self.extract_specification_codes(full_text)
                results.append({'nombre': nombre, 'codes': codes})

        # Imprimir resultados
        for res in results:
            self.stdout.write(f"Predio: {res['nombre']}")
            if res['codes']:
                self.stdout.write("  Códigos de especificación: " + ", ".join(res['codes']))
            else:
                self.stdout.write("  No se encontraron códigos de especificación.")
