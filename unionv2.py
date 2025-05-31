import tkinter as tk
from tkinter import filedialog, messagebox
import os
import threading
from pypdf import PdfReader, PdfWriter
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x520")
        self.pdf_files = []

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        title = ttk.Label(frame, text="🔗 Unir PDFs", font=("Helvetica", 18, "bold"), bootstyle="primary")
        title.pack(pady=(0, 15))

        list_frame = ttk.LabelFrame(frame, text="📋 Archivos seleccionados", padding=10)
        list_frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(list_frame, height=10, borderwidth=0, highlightthickness=0)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.add_files_button = ttk.Button(frame, text="➕ Añadir archivos PDF", command=self.add_files)
        self.add_files_button.pack(fill=tk.X, pady=(10, 5))

        self.add_folder_button = ttk.Button(frame, text="📂 Añadir carpeta", command=self.add_folder)
        self.add_folder_button.pack(fill=tk.X, pady=5)

        self.remove_button = ttk.Button(frame, text="❌ Eliminar seleccionados", command=self.remove_selected)
        self.remove_button.pack(fill=tk.X, pady=5)

        self.merge_button = ttk.Button(frame, text=" Unir PDFs", bootstyle="success", command=self.merge_pdfs)
        self.merge_button.pack(fill=tk.X, pady=(10, 5))

        # Barra de progreso real
        self.progress = ttk.Progressbar(frame, mode="determinate", bootstyle="info", maximum=100)
        self.progress.pack(fill=tk.X, pady=(10, 0))

        self.progress_label = ttk.Label(frame, text="0%", font=("Helvetica", 10))
        self.progress_label.pack()

    def add_files(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        for file in files:
            if file not in self.pdf_files:
                self.pdf_files.append(file)
                self.listbox.insert(tk.END, os.path.basename(file))

    def add_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            for filename in sorted(os.listdir(folder)):
                if filename.lower().endswith(".pdf"):
                    full_path = os.path.join(folder, filename)
                    if full_path not in self.pdf_files:
                        self.pdf_files.append(full_path)
                        self.listbox.insert(tk.END, filename)

    def remove_selected(self):
        selected_indices = self.listbox.curselection()
        for index in reversed(selected_indices):
            self.listbox.delete(index)
            del self.pdf_files[index]

    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showwarning("Atención", "No has seleccionado archivos PDF.")
            return

        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Guardar PDF unido como..."
        )

        if output_path:
            threading.Thread(target=self._merge_pdfs_background, args=(output_path,), daemon=True).start()

    def _merge_pdfs_background(self, output_path):
        try:
            self.root.after(0, lambda: self.progress.configure(value=0))
            self.root.after(0, lambda: self.progress_label.configure(text="0%"))

            writer = PdfWriter()

            total_paginas = sum(len(PdfReader(pdf).pages) for pdf in self.pdf_files)
            paginas_procesadas = 0

            for pdf in self.pdf_files:
                reader = PdfReader(pdf)
                for page in reader.pages:
                    writer.add_page(page)
                    paginas_procesadas += 1
                    porcentaje = int((paginas_procesadas / total_paginas) * 100)
                    self.root.after(0, lambda v=porcentaje: self.progress.configure(value=v))
                    self.root.after(0, lambda v=porcentaje: self.progress_label.configure(text=f"{v}%"))

            with open(output_path, "wb") as f:
                writer.write(f)

            final_reader = PdfReader(output_path)
            total_paginas_final = len(final_reader.pages)
            paginas_blancas = self.detectar_paginas_blancas(final_reader)

            if paginas_blancas:
                mensaje_blancas = f"\nPáginas en blanco detectadas ({len(paginas_blancas)}): {paginas_blancas}"
            else:
                mensaje_blancas = "\nNo se encontraron páginas en blanco."

            self.root.after(0, lambda: messagebox.showinfo(
                "Éxito",
                f"PDFs unidos correctamente:\n{output_path}\n\nTotal de páginas: {total_paginas_final}{mensaje_blancas}"
            ))

        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Ocurrió un error al unir los archivos:\n{str(e)}"))
        finally:
            self.root.after(0, lambda: self.progress.configure(value=0))
            self.root.after(0, lambda: self.progress_label.configure(text="0%"))

    def detectar_paginas_blancas(self, pdf_reader):
        paginas_en_blanco = []
        for i, page in enumerate(pdf_reader.pages):
            text = page.extract_text() or ""
            if not text.strip():
                paginas_en_blanco.append(i + 1)
        return paginas_en_blanco


if __name__ == "__main__":
    app = ttk.Window(themename="cosmo", title="Unir PDFs")
    PDFMergerApp(app)
    app.mainloop()