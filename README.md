# PDF Merger 🧩

Una herramienta de escritorio moderna, ligera y práctica para **unir múltiples archivos PDF** en un único documento. Construida con Python y diseñada con una interfaz intuitiva gracias a `ttkbootstrap`, esta aplicación es ideal para trabajos administrativos, digitalización de documentos o presentaciones.

---

## ✨ Características

- 🗂️ Unión de múltiples archivos PDF
- 📁 Posibilidad de añadir archivos sueltos o carpetas completas
- 📊 Barra de progreso interactiva con porcentaje
- 📄 Conteo total de páginas al finalizar
- 📃 Detección de páginas en blanco y su posición
- 🎨 Interfaz moderna 
- 🖱️ Uso completamente gráfico, sin necesidad de usar la terminal

---

## 🖼️ Captura de pantalla



<img width="596" alt="1" src="https://github.com/user-attachments/assets/12319065-4257-4123-8325-9b76d103baca" />
<img width="596" alt="2" src="https://github.com/user-attachments/assets/e2f9bfb4-bbc1-4783-897b-90b5d184cb11" />



---

## 🛠️ Tecnologías utilizadas

- `Python 3.10+`
- `tkinter`
- `ttkbootstrap`
- `pypdf`

---

## 🧰 Instalación

### 🔧 Requisitos

- Python 3.10 o superior
- Sistema operativo: macOS (funciona también en Windows/Linux con mínimos ajustes)

### 💻 Instalación local

```bash
git clone https://github.com/tuusuario/pdf-merger.git
cd pdf-merger
pip install -r requirements.txt
python unionpdf.py
```

---

## 📦 Uso

1. Abre la aplicación.
2. Haz clic en “Añadir archivos” o “Añadir carpeta”.
3. Organiza los archivos si es necesario (puedes eliminar).
4. Haz clic en “Unir PDFs” y elige el nombre de salida.
5. Observa el progreso y los resultados.

---

## 📁 Estructura del proyecto

```
📦 pdf-merger/
├── 📄 unionpdf.py           # Código principal de la aplicación
├── 📄 requirements.txt      # Dependencias necesarias
├── 📄 README.md             # Este archivo
├── 📄 icono.ico             # (opcional) Icono de la app
```

---

## 🚀 Compilación como App

Para generar un `.app` en macOS o `.exe` en Windows, puedes usar `pyinstaller`:

```bash
pyinstaller --noconfirm --onefile --windowed unionpdf.py --icon=icono.ico
```

---

## 📌 Posibilidades de mejora

- Exportación automática de informe en PDF
- OCR para escaneos sin texto real
- Drag & Drop de archivos directamente sobre la ventana
- Localización en múltiples idiomas

---

## 🤝 Créditos

Desarrollado con ❤️ en Python. Inspirado en la necesidad de tener herramientas de productividad simples y efectivas.

---

## 📃 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
