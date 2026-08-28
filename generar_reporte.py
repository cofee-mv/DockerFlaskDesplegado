from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Reporte de Vulnerabilidades de Seguridad', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.add_page()

# Titulo
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Proyecto: DockerFlaskDesplegado', 0, 1, 'L')
pdf.cell(0, 10, 'Fecha: 25 de Agosto de 2026', 0, 1, 'L')
pdf.ln(10)

# Tabla de Reporte de Vulnerabilidades
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, '1. Tabla de Reporte de Vulnerabilidades', 0, 1, 'L')
pdf.ln(5)

# Encabezados de la tabla
pdf.set_font('Arial', 'B', 10)
pdf.set_fill_color(200, 200, 200)
pdf.cell(50, 8, 'Herramienta', 1, 0, 'C', 1)
pdf.cell(50, 8, 'Nombre del Fallo', 1, 0, 'C', 1)
pdf.cell(30, 8, 'Severidad', 1, 0, 'C', 1)
pdf.cell(60, 8, 'Solucion', 1, 1, 'C', 1)

# Fila 1 - Bandit
pdf.set_font('Arial', '', 9)
pdf.cell(50, 8, 'Bandit (SAST)', 1, 0, 'C')
pdf.cell(50, 8, 'Hardcoded Password', 1, 0, 'C')
pdf.set_text_color(255, 0, 0)
pdf.cell(30, 8, 'HIGH', 1, 0, 'C')
pdf.set_text_color(0, 0, 0)
pdf.cell(60, 8, 'Usar variable de entorno os.getenv()', 1, 1, 'C')

# Fila 2 - Bandit
pdf.cell(50, 8, 'Bandit (SAST)', 1, 0, 'C')
pdf.cell(50, 8, 'Debug Mode Enabled', 1, 0, 'C')
pdf.set_text_color(255, 0, 0)
pdf.cell(30, 8, 'MEDIUM', 1, 0, 'C')
pdf.set_text_color(0, 0, 0)
pdf.cell(60, 8, 'Remover debug=True del codigo', 1, 1, 'C')

# Fila 3 - Trivy
pdf.cell(50, 8, 'Trivy (Imagen)', 1, 0, 'C')
pdf.cell(50, 8, 'Vulnerable Base Image', 1, 0, 'C')
pdf.set_text_color(255, 0, 0)
pdf.cell(30, 8, 'CRITICAL', 1, 0, 'C')
pdf.set_text_color(0, 0, 0)
pdf.cell(60, 8, 'Actualizar a python:3.12-slim', 1, 1, 'C')

# Fila 4 - Pytest
pdf.cell(50, 8, 'Pytest (Prueba)', 1, 0, 'C')
pdf.cell(50, 8, 'Test Failure Status 500', 1, 0, 'C')
pdf.set_text_color(255, 0, 0)
pdf.cell(30, 8, 'HIGH', 1, 0, 'C')
pdf.set_text_color(0, 0, 0)
pdf.cell(60, 8, 'Restaurar assert status_code == 200', 1, 1, 'C')

pdf.ln(15)

# Explicacion de las soluciones
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, '2. Explicacion de las Soluciones', 0, 1, 'L')
pdf.ln(5)

pdf.set_font('Arial', '', 10)

soluciones = [
    ("Fallo SAST (Bandit) - Clave Hardcodeada:", 
     "Se removio la variable MYSQL_PASSWORD = 'super_secret_123' del codigo. Se reemplazo por os.getenv('password') para leer la contrasena desde variables de entorno, manteniendo las credenciales fuera del repositorio."),
    ("Fallo SAST (Bandit) - Debug Mode:", 
     "Se removio el parametro debug=True de sample.run(). El modo de depuracion en produccion puede exponer informacion sensible y rastros de errores."),
    ("Fallo Imagen (Trivy):", 
     "Se cambio la imagen base de python:3.8-slim-buster a python:3.12-slim. La imagen anterior contenia multiples vulnerabilidades conocidas (CVEs) en el sistema operativo y librerias del sistema."),
    ("Fallo Prueba (Pytest):", 
     "Se restauro el assert de status_code == 500 a status_code == 200. La ruta / debe devolver exitosamente la pagina de estado de la base de datos.")
]

for titulo, descripcion in soluciones:
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 8, titulo, 0, 1, 'L')
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 6, descripcion)
    pdf.ln(5)

pdf.ln(10)

# Capturas de evidencia
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, '3. Evidencias del Pipeline', 0, 1, 'L')
pdf.ln(5)

pdf.set_font('Arial', 'B', 10)
pdf.cell(0, 8, 'Captura 1: Pipeline Fallido (ROJO)', 0, 1, 'L')
pdf.set_font('Arial', '', 10)
pdf.multi_cell(0, 6, 'El pipeline de GitHub Actions falla en la etapa de testing/seguridad. Bandit detecta la clave hardcodeada y pytest falla porque la ruta / devuelve 500 en lugar de 200. El despliegue automatico se cancela.')
pdf.ln(5)

pdf.set_font('Arial', 'B', 10)
pdf.cell(0, 8, 'Captura 2: Pipeline Exitoso (VERDE)', 0, 1, 'L')
pdf.set_font('Arial', '', 10)
pdf.multi_cell(0, 6, 'Despues de aplicar los parches de seguridad, el pipeline pasa todas las verificaciones: Bandit no detecta vulnerabilidades, pytest pasa exitosamente, Trivy no encuentra vulnerabilidades criticas en la imagen. El despliegue se ejecuta correctamente.')
pdf.ln(5)

pdf.set_font('Arial', 'B', 10)
pdf.cell(0, 8, 'Captura 3: Verificacion Final de la API', 0, 1, 'L')
pdf.set_font('Arial', '', 10)
pdf.multi_cell(0, 6, 'La aplicacion Flask esta funcionando correctamente en el dominio HTTPS de DuckDNS. La ruta / muestra el estado de conexion a la base de datos y la API responde con status 200 OK.')

# Guardar PDF
pdf.output('C:/Users/saram/DockerFlaskDesplegado/Reporte_Vulnerabilidades_Seguridad.pdf')
print("PDF generado exitosamente: Reporte_Vulnerabilidades_Seguridad.pdf")
