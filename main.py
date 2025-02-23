import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Función para conectar a la base de datos python_proyecto
def conectar_db():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_proyecto",
    )
    return conexion


# Aplicación "Agenda de Contactos"
class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Contactos en Python")
        self.root.geometry("1920x1080")

        # Treeview para mostrar los contactos
        self.tree = ttk.Treeview(
            root, columns=("ID", "Nombre", "Teléfono", "Email", "Notas")
        )
        self.tree.heading("#1", text="ID")
        self.tree.heading("#2", text="Nombre")
        self.tree.heading("#3", text="Teléfono")
        self.tree.heading("#4", text="Email")
        self.tree.heading("#5", text="Notas")
        self.tree.pack()

        # MOSTRAR
        # Botón para mostrar los contactos
        self.boton_mostrar = tk.Button(
            root, text="Mostrar contactos", command=self.mostrar_contactos
        )
        self.boton_mostrar.pack(fill=tk.X)

        # INSERTAR
        # Campos de entrada del nuevo contacto
        self.etiqueta_nombre = tk.Label(root, text="Nombre:")
        self.etiqueta_nombre.pack()

        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()

        self.etiqueta_telefono = tk.Label(root, text="Teléfono:")
        self.etiqueta_telefono.pack()

        self.entry_telefono = tk.Entry(root)
        self.entry_telefono.pack()

        self.etiqueta_email = tk.Label(root, text="Email:")
        self.etiqueta_email.pack()

        self.entry_email = tk.Entry(root)
        self.entry_email.pack()

        self.etiqueta_notas = tk.Label(root, text="Notas:")
        self.etiqueta_notas.pack()

        self.entry_notas = tk.Entry(root)
        self.entry_notas.pack()

        # botón para insertar contacto
        self.boton_insertar = tk.Button(
            root, text="Insertar Contacto", command=self.insertar_contacto
        )
        self.boton_insertar.pack(fill=tk.X)

        # EDITAR
        # Campos de entrada para editar un contacto
        self.etiqueta_id_editar = tk.Label(root, text="ID del contacto a Editar:")
        self.etiqueta_id_editar.pack()

        self.entry_id_editar = tk.Entry(root)
        self.entry_id_editar.pack()

        self.etiqueta_nuevo_nombre = tk.Label(root, text="Nuevo Nombre:")
        self.etiqueta_nuevo_nombre.pack()

        self.entry_nuevo_nombre = tk.Entry(root)
        self.entry_nuevo_nombre.pack()

        self.etiqueta_nuevo_telefono = tk.Label(root, text="Nuevo Teléfono:")
        self.etiqueta_nuevo_telefono.pack()

        self.entry_nuevo_telefono = tk.Entry(root)
        self.entry_nuevo_telefono.pack()

        self.etiqueta_nuevo_email = tk.Label(root, text="Nuevo Email:")
        self.etiqueta_nuevo_email.pack()

        self.entry_nuevo_email = tk.Entry(root)
        self.entry_nuevo_email.pack()

        self.etiqueta_nuevas_notas = tk.Label(root, text="Nuevas Notas:")
        self.etiqueta_nuevas_notas.pack()

        self.entry_nuevas_notas = tk.Entry(root)
        self.entry_nuevas_notas.pack()

        # botón para editar contacto
        self.boton_editar = tk.Button(
            root, text="Editar Contacto", command=self.editar_contacto
        )
        self.boton_editar.pack(fill=tk.X)

        # BORRAR
        # Campos de entrada para la id del contacto que queremos eliminar
        self.etiqueta_id_eliminar = tk.Label(root, text="ID del contacto a Borrar:")
        self.etiqueta_id_eliminar.pack()

        self.entry_id_eliminar = tk.Entry(root)
        self.entry_id_eliminar.pack()

        # botón para borrar contacto
        self.boton_borrar = tk.Button(
            root, text="Borrar Contacto", command=self.borrar_contacto
        )
        self.boton_borrar.pack(fill=tk.X)

        # BUSCAR
        # Campo de búsqueda por nombre
        self.etiqueta_nombre_buscado = tk.Label(root, text="Nombre del Contacto: ")
        self.etiqueta_nombre_buscado.pack()

        self.entry_nombre_buscado = tk.Entry(root)
        self.entry_nombre_buscado.pack()

        # botón para buscar contacto por nombre
        self.boton_buscar_por_nombre = tk.Button(
            root, text="Buscar", command=self.buscar_contacto
        )
        self.boton_buscar_por_nombre.pack(fill=tk.X)

    # FUNCIONES DE LA APLICACIÓN
    # Función para insertar los datos de un nuevo contacto
    def insertar_contacto(self):
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()
        email = self.entry_email.get()
        notas = self.entry_notas.get()
        if nombre and telefono and email and notas:
            # Conectar a la base de datos e insertar un nuevo contacto
            conexion = conectar_db()
            cursor = conexion.cursor()
            cursor.execute(
                """
            INSERT INTO contactos (nombre, telefono, email, notas)
            VALUES (%s, %s, %s, %s)
        """,
                (nombre, telefono, email, notas),
            )
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Contacto insertado correctamente.")
            # Limpia los campo de entrada
            self.entry_nombre.delete(0, tk.END)
            self.entry_telefono.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_notas.delete(0, tk.END)
        else:
            messagebox.showwarning(
                "Advertencia", "Por favor, completa todos los campos."
            )

    # Función para editar los datos de un contacto
    def editar_contacto(self):
        id_editar = self.entry_id_editar.get()
        nuevo_nombre = self.entry_nuevo_nombre.get()
        nuevo_telefono = self.entry_nuevo_telefono.get()
        nuevo_email = self.entry_nuevo_email.get()
        nuevas_notas = self.entry_nuevas_notas.get()
        if (
            id_editar
            and nuevo_nombre
            and nuevo_telefono
            and nuevo_email
            and nuevas_notas
        ):
            # Conectar a la base de datos y editar el contacto
            conexion = conectar_db()
            cursor = conexion.cursor()
            cursor.execute(
                """
            UPDATE contactos
            SET nombre = %s, telefono = %s, email = %s, notas = %s
            WHERE id_contacto = %s
        """,
                (nuevo_nombre, nuevo_telefono, nuevo_email, nuevas_notas, id_editar),
            )
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Contacto editado correctamente.")
            # Limpia los campos de entrada
            self.entry_id_editar.delete(0, tk.END)
            self.entry_nuevo_nombre.delete(0, tk.END)
            self.entry_nuevo_telefono.delete(0, tk.END)
            self.entry_nuevo_email.delete(0, tk.END)
            self.entry_nuevas_notas.delete(0, tk.END)
        else:
            messagebox.showwarning(
                "Advertencia", "Por favor, completa todos los campos."
            )

    # Función para borrar los datos de un contacto por su ID
    def borrar_contacto(self):
        id_borrar = self.entry_id_eliminar.get()
        if id_borrar:
            # Conectar a la base de datos y borrar el contacto
            conexion = conectar_db()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM contactos WHERE id_contacto = %s", (id_borrar,))
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Contacto eliminado correctamente.")
            # Limpia el campo de entrada
            self.entry_id_eliminar.delete(0, tk.END)
        else:
            messagebox.showwarning(
                "Advertencia", "Por favor, complete el campo de ID del contacto."
            )

    # Función para buscar un contacto por el nombre
    def buscar_contacto(self):
        nombre_buscado = self.entry_nombre_buscado.get()
        # Limpia los datos en el Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Conectar a la base de datos y mostrar el contacto buscado
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id_contacto, nombre, telefono, email, notas FROM contactos WHERE nombre = %s",
            (nombre_buscado,),
        )
        registros = cursor.fetchall()
        conexion.close()

        # Mostrar el contacto buscado en el treeview
        for registro in registros:
            self.tree.insert("", "end", values=registro)

    # Función para mostrar todos los contactos de la base de datos
    def mostrar_contactos(self):
        # Limpia los datos en el Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Conectar a la base de datos y mostrar los datos
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id_contacto, nombre, telefono, email, notas FROM contactos"
        )
        registros = cursor.fetchall()
        conexion.close()

        # Mostrar los contactos en el treeview
        for registro in registros:
            self.tree.insert("", "end", values=registro)


# EJECUCIÓN
root = tk.Tk()
app = Aplicacion(root)
root.mainloop()
