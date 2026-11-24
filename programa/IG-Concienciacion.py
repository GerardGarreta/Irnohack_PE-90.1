#!/usr/bin/env python3

from datetime import datetime
import json
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk


AREAS_LOGISTICFY = [
    "Operaciones",
    "Atención al Cliente",
    "Administración",
    "Comercial",
    "Tecnología/IT",
    "Dirección",
    "Persona en prácticas",
]

NORMAS_LOGISTICFY = [
    {
        "id": "N-01",
        "titulo": "Uso personal de cuentas y control de sesión",
        ""
        "destinatarios": "Todo el personal (incluida la persona en prácticas).",
        "conducta": (
            "Utilizar exclusivamente la cuenta personal asignada (IAM-01), no compartir "
            "contraseñas ni credenciales y bloquear el equipo Windows 11 (HW-01) al ausentarse."
        ),
        "verificacion": (
            "Revisión de políticas de bloqueo de sesión, registros de autenticación (MON-01) "
            "o comprobaciones visuales en el puesto."
        ),
        "excepciones": (
            "No se admiten cuentas compartidas ordinarias; cualquier acceso temporal o de soporte "
            "se tramita por vías autorizadas por Tecnología/IT."
        ),
    },
    {
        "id": "N-02",
        "titulo": "Acceso según función y entorno",
        ""
        "destinatarios": "Todo el personal, con especial atención a Tecnología/IT, Operaciones y Administración.",
        "conducta": (
            "Limitar el acceso a aplicaciones, base de datos, repositorios y entornos técnicos "
            "(SW-01, DAT-01, SW-03, INF-01, BKP-01, MON-01) al rol asignado y operar por los flujos previstos."
        ),
        "verificacion": (
            "Revisión periódica de perfiles/permisos en IAM-01 y consulta de registros de acceso y "
            "cambios en MON-01."
        ),
        "excepciones": (
            "Excepciones puntuales o urgentes requieren autorización previa del responsable del área "
            "y del Responsable IT (y de Dirección si el impacto es relevante), con caducidad."
        ),
    },
    {
        "id": "N-03",
        "titulo": "Uso adecuado de equipos y software corporativo",
        ""
        "destinatarios": "Todo el personal (incluida la persona en prácticas).",
        "conducta": (
            "Emplear los equipos Windows (HW-01) para fines profesionales; no instalar software no "
            "autorizado, no desactivar controles de seguridad ni conectar almacenamiento externo no permitido."
        ),
        "verificacion": (
            "Inventario de software y configuraciones en HW-01 y registros de sistema/seguridad (MON-01)."
        ),
        "excepciones": (
            "Tecnología/IT puede usar herramientas técnicas específicas para administración y soporte "
            "dentro de su ámbito autorizado."
        ),
    },
    {
        "id": "N-04",
        "titulo": "Tratamiento cuidadoso de datos de envíos, clientes y personas",
        ""
        "destinatarios": "Todo el personal, especialmente Operaciones, Atención al Cliente, Comercial y Administración.",
        "conducta": (
            "Consultar y usar datos de clientes, contactos, destinatarios, direcciones, incidencias y "
            "facturación (DAT-01) solo para el servicio; evitar descargas o envíos no autorizados."
        ),
        "verificacion": (
            "Control de copias locales en HW-01, revisión de incidencias de información y registros."
        ),
        "excepciones": (
            "Solo se comparten datos estrictamente necesarios con transportistas (EXT-01) o clientes "
            "por canales y procesos habilitados."
        ),
    },
    {
        "id": "N-05",
        "titulo": "Verificación en correo y canales externos",
        ""
        "destinatarios": "Todo el personal, especialmente Comercial, Administración, Operaciones y Atención al Cliente.",
        "conducta": (
            "Antes de abrir enlaces/adjuntos inesperados o aplicar cambios sensibles (pagos, cuentas, "
            "direcciones o envíos) en COM-01 o mensajería, verificar la identidad por un canal fiable."
        ),
        "verificacion": (
            "Análisis de incidentes reportados en COM-01 y ejercicios o revisiones periódicas."
        ),
        "excepciones": "No aplica excepción a la verificación previa ante solicitudes inusuales o sensibles.",
    },
    {
        "id": "N-06",
        "titulo": "Seguridad física en oficina y red",
        ""
        "destinatarios": "Todo el personal en oficina (incluida la persona en prácticas).",
        "conducta": (
            "No dejar documentación confidencial o credenciales a la vista en PHY-01, controlar visitas, "
            "usar la red corporativa autorizada (NET-01) y no conectar dispositivos desconocidos."
        ),
        "verificacion": "Rondas de orden y limpieza en PHY-01 y revisión de conexiones/dispositivos en NET-01.",
        "excepciones": (
            "El acceso de visitas o proveedores externos a zonas de trabajo requiere acompañamiento "
            "o autorización de la persona responsable designada."
        ),
    },
    {
        "id": "N-07",
        "titulo": "Comunicación inmediata de anomalías",
        ""
        "destinatarios": "Todo el personal (incluida la persona en prácticas).",
        "conducta": (
            "Comunicar de inmediato por el canal interno cualquier sospecha de phishing, pérdida/robo, "
            "acceso indebido, fallo de integración (SW-02 / EXT-01) o alteración de datos (DAT-01), "
            "conservando evidencias básicas sin manipular."
        ),
        "verificacion": "Registro y seguimiento de avisos recibidos y contraste con eventos en MON-01.",
        "excepciones": "No existe excepción a la obligación de notificar una sospecha razonable de incidencia.",
    },
]

OBJETIVOS_LOGISTICFY = [
    {
        "id": "O-01",
        "objetivo": (
            "Detectar correos o mensajes sospechosos (phishing / suplantación) y verificar "
            "cambios de datos, envíos, facturas o enlaces por un canal fiable antes de actuar."
        ),
        ""
        "destinatarios": "Todo el personal, con prioridad en Operaciones, Atención al Cliente, Comercial y Administración.",
        "justificacion": (
            "Gestionan a diario solicitudes, incidencias, contactos comerciales y facturación a través "
            "de COM-01 y plataformas vinculadas a expediciones y clientes."
        ),
    },
    {
        "id": "O-02",
        "objetivo": (
            "Manejar de forma segura los datos de expediciones, clientes, destinatarios, incidencias "
            "y facturación, evitando descargas o envíos indebidos y cuidando puesto y espacio."
        ),
        ""
        "destinatarios": "Operaciones, Atención al Cliente, Administración y Comercial (extensible al resto).",
        "justificacion": (
            "Una expedición recorre varios procesos y áreas (DAT-01, SW-01, HW-01, PHY-01); un error "
            "de manejo o envío puede exponer datos o generar incidencias operativas."
        ),
    },
    {
        "id": "O-03",
        "objetivo": (
            "Adoptar hábitos seguros de autenticación, control de sesión y uso de recursos técnicos "
            "conforme al rol y a los procedimientos establecidos."
        ),
        ""
        "destinatarios": "Todo el personal, con atención específica a la persona en prácticas y a Tecnología/IT.",
        "justificacion": (
            "La persona en prácticas necesita conocer desde el inicio las reglas de acceso (IAM-01), "
            "uso de HW-01 y límites de actuación; Tecnología/IT requiere rigor en accesos y entornos."
        ),
    },
    {
        "id": "O-04",
        "objetivo": (
            "Reconocer indicios tempranos de anomalía en accesos, envíos, integraciones o equipos "
            "y notificarlos con rapidez por el canal interno."
        ),
        ""
        "destinatarios": "Toda la plantilla (20 personas: 19 empleados y persona en prácticas).",
        "justificacion": (
            "La detección rápida por parte de los usuarios complementa a MON-01 y permite contener "
            "problemas en SW-01, SW-02, EXT-01, COM-01 o HW-01 antes de que escalen."
        ),
    },
]

ACCIONES_LOGISTICFY = [
    {
        "id": "A-01",
        "objetivo": "O-01 (y apoyo a O-04)",
        ""
        "destinatarios": "Operaciones, Atención al Cliente, Comercial y Administración (abierta al resto).",
        "accion_canal": (
            "Taller práctico de 35 min y distribución de guía sobre phishing y verificación de "
            "solicitudes/incidencias. Canal: sesión presencial o sala/videollamada, COM-01/repositorio y script Python."
        ),
        "temporalizacion": "Mes 1 (sesión de 35 min en franja de menor carga; consulta continua).",
        "responsable": "Responsable IT (con apoyo de referente de Operaciones o Atención al Cliente).",
        "material": "M-01 (Guía rápida y programa interactivo en Python).",
    },
    {
        "id": "A-02",
        "objetivo": "O-02",
        ""
        "destinatarios": "Operaciones, Atención al Cliente, Administración y Comercial.",
        "accion_canal": (
            "Cápsula operativa de 25 min por grupos reducidos sobre ciclo seguro del dato en "
            "expediciones, incidencias y facturación y orden en puesto/oficina. Canal: sesiones cortas por área."
        ),
        "temporalizacion": "Mes 2 (sesiones de 25 min por grupo fuera de horas punta).",
        "responsable": "Responsable de operaciones (con apoyo de Tecnología/IT).",
        "material": "M-02 (Ficha del ciclo seguro del dato en expediciones y facturación).",
    },
    {
        "id": "A-03",
        "objetivo": "O-03",
        ""
        "destinatarios": "Persona en prácticas y nuevas incorporaciones (recordatorio general a la plantilla).",
        "accion_canal": (
            "Sesión de acogida de seguridad en el puesto y repaso de accesos/normativa (IAM-01, "
            "HW-01, NET-01, N-01 a N-03). Canal: acompañamiento directo en el puesto y apoyo documental."
        ),
        "temporalizacion": "Al inicio de la incorporación (25 min) y recordatorio cada 3 meses.",
        "responsable": "Responsable IT / Administrador de sistemas (con tutoría del área).",
        "material": "M-03 (Lista de comprobación inicial del puesto y accesos).",
    },
    {
        "id": "A-04",
        "objetivo": "O-04 (refuerza O-01 a O-03)",
        ""
        "destinatarios": "Toda la plantilla (20 personas).",
        "accion_canal": (
            "Ejercicio sencillo de notificación de anomalías (N-07) y recordatorios mensuales breves. "
            "Canal: aviso controlado sin impacto en producción y canal interno habitual."
        ),
        "temporalizacion": "Trimestral (ejercicio de 15 min) + recordatorio mensual breve.",
        "responsable": "Responsable IT (en coordinación con el responsable de operaciones).",
        "material": "M-04 (Guion del ejercicio de notificación de anomalías y recordatorios).",
    },
]

CASOS_PRACTICOS = [
    {
        "id": "CASO-01",
        "area": "Administración / Comercial",
        "escenario": (
            "Recibes un correo urgente en COM-01 supuestamente de uno de los "
            "25 clientes empresariales indicando que ha cambiado su cuenta bancaria "
            "para la factura de las expediciones de esta semana y pide aplicarlo hoy mismo."
        ),
        "opciones": {
            "A": "Actualizar los datos bancarios directamente para no retrasar la facturación.",
            "B": (
                "No aplicar el cambio aún; comprobar el historial con el cliente y "
                "confirmar la solicitud por teléfono o canal habitual previamente verificado (N-05)."
            ),
            "C": "Reenviar el correo a toda la plantilla preguntando si alguien conoce el cambio.",
        },
        "correcta": "B",
        "explicacion": (
            "(Norma N-05 / Objetivo O-01 / Acción A-01). Los cambios urgentes de "
            "cuentas bancarias o pagos requieren verificación por un canal fiable distinto antes "
            "de modificar datos en facturación."
        ),
    },
    {
        "id": "CASO-02",
        "area": "Operaciones / Atención al Cliente",
        "escenario": (
            "Llega un correo con asunto 'Incidencia crítica en entrega #EXP-4092' desde "
            "un dominio muy parecido al de uno de los tres transportistas externos, con un "
            "enlace que pide iniciar sesión con tu cuenta corporativa de Logisticfy."
        ),
        "opciones": {
            "A": "Introducir usuario y contraseña para ver qué ha pasado con la expedición.",
            "B": "Responder al correo enviando los datos del destinatario para agilizar la entrega.",
            "C": (
                "No pulsar el enlace ni introducir credenciales, comprobar el estado real de "
                "la expedición en la plataforma (SW-01) y avisar a Tecnología/IT (N-05 y N-07)."
            ),
        },
        "correcta": "C",
        "explicacion": (
            "(Normas N-01, N-05 y N-07 / Objetivos O-01 y O-04). Nunca deben "
            "introducirse credenciales corporativas en enlaces recibidos por correo ni "
            "compartir datos de envío sin verificar la identidad del remitente."
        ),
    },
    {
        "id": "CASO-03",
        "area": "Atención al Cliente / Operaciones",
        "escenario": (
            "Un supuesto contacto externo escribe pidiendo un listado completo en Excel/CSV "
            "con todas las expediciones, direcciones de destinatarios y teléfonos de contacto "
            "del último mes para 'revisar estadísticas del servicio'."
        ),
        "opciones": {
            "A": "Exportar la tabla desde el backoffice y enviarla por correo para dar buen servicio.",
            "B": (
                "No exportar ni enviar listados masivos; verificar si la petición es legítima "
                "con el responsable del área y compartir solo lo estrictamente necesario por "
                "canales autorizados (N-04)."
            ),
            "C": "Guardar el archivo en el escritorio del puesto compartido para revisarlo más tarde.",
        },
        "correcta": "B",
        "explicacion": (
            "(Norma N-04 / Objetivo O-02). Aunque Logisticfy opera en B2B, "
            "las expediciones incluyen datos de contactos, destinatarios y direcciones que "
            "deben protegerse frente a exportaciones o envíos innecesarios."
        ),
    },
    {
        "id": "CASO-04",
        "area": "Toda la plantilla (incl. persona en prácticas)",
        "escenario": (
            "Al volver a tu puesto Windows 11 (HW-01) tras una pausa breve, notas que lo "
            "habías dejado sin bloquear y ves una ventana emergente inusual que no habías abierto."
        ),
        "opciones": {
            "A": "Cerrar la ventana rápidamente y seguir trabajando sin decírselo a nadie.",
            "B": "Apagar el equipo a la fuerza y cambiar de ordenador con un compañero.",
            "C": (
                "No manipular ni borrar evidencias, avisar de inmediato a Tecnología/IT "
                "y recordar bloquear siempre la sesión al ausentarse (N-01 y N-07)."
            ),
        },
        "correcta": "C",
        "explicacion": (
            "(Normas N-01 y N-07 / Objetivos O-03 y O-04). Bloquear la pantalla "
            "protege la cuenta personal, y avisar pronto a Tecnología/IT permite "
            "revisar registros y contener cualquier incidencia a tiempo."
        ),
    },
    {
        "id": "CASO-05",
        "area": "Tecnología/IT / Operaciones",
        "escenario": (
            "Durante la gestión diaria de 80-120 expediciones, un compañero pide que le "
            "prestes tu cuenta porque la suya no tiene permisos para modificar un dato urgente."
        ),
        "opciones": {
            "A": "Dejarle tu sesión abierta un momento para resolver la urgencia.",
            "B": (
                "No compartir cuentas ni credenciales; tramitar la operación por el flujo "
                "correspondiente o gestionar una autorización puntual con Tecnología/IT (N-01 y N-02)."
            ),
            "C": "Apuntar tu contraseña en un papel en la mesa por si vuelve a hacer falta.",
        },
        "correcta": "B",
        "explicacion": (
            "(Normas N-01, N-02 y N-06 / Objetivo O-03). Las cuentas son personales "
            "e intransferibles para mantener la trazabilidad y el mínimo privilegio."
        ),
    },
]

TEXTO_GUIA_RAPIDA = """GUÍA RÁPIDA LOGISTICFY
Detectar correos sospechosos y verificar cambios en envíos y facturación


1. CINCO SEÑALES DE ALERTA EN CORREO Y CANALES EXTERNOS

   • Urgencia artificial o presión para actuar sin comprobar.
   • Cambios sensibles inesperados (cuentas bancarias, direcciones de entrega, facturas).
   • Remitentes o dominios parecidos a clientes o transportistas externos.
   • Enlaces a páginas externas de inicio de sesión o adjuntos inesperados.
   • Datos de expedición o incidencia que no coinciden con la plataforma.

2. REGLA DE ORO ANTES DE ACTUAR 

   • Comprueba primero la información en la plataforma interna.
   • Verifica cualquier cambio sensible por un canal fiable y conocido (nunca respondas
     directamente sobre un correo sospechoso si dudas de su autenticidad).
   • Protege los datos: no exportes ni envíes listados de clientes, contactos
     o destinatarios sin necesidad operativa ni por canales no autorizados.

3. PROTECCIÓN DEL PUESTO Y NOTIFICACIÓN TEMPRANA

   • Utiliza exclusivamente tu cuenta personal y bloquea tu equipo Windows 11
     cada vez que te ausentes de tu puesto.
   • Mantén el puesto limpio de documentos sensibles y usa solo la red autorizada.
   • Ante cualquier sospecha, enlace pulsado o comportamiento extraño, no borres evidencias
     y avisa de inmediato a Tecnología/IT y a tu responsable directo.
"""

RUTA_EVIDENCIAS = Path("evidencias_taller_A01.json")

def insertar_linea_clave(widget: scrolledtext.ScrolledText, etiqueta: str, valor: str) -> None:
    widget.insert("end", f"  • {etiqueta:<16}: ", "etiqueta")
    widget.insert("end", f"{valor}\n")

def construir_texto_normas_y_programa() -> str:
    lineas = [
        "MARCO NORMATIVO Y PROGRAMA DE CONCIENCIACIÓN · LOGISTICFY",
        ""
        "",
        "1. NORMATIVA DEL PUESTO DE TRABAJO (N-01 a N-07)",
        "",
    ]
    for n in NORMAS_LOGISTICFY:
        lineas.extend(
            [
                f"[{n['id']}] {n['titulo']}",
                "",
                f"  • Destinatarios : {n['destinatarios']}",
                f"  • Conducta      : {n['conducta']}",
                f"  • Verificación  : {n['verificacion']}",
                f"  • Excepciones   : {n['excepciones']}",
                "",
            ]
        )

    lineas.extend(
        [
            "2. OBJETIVOS DE CONCIENCIACIÓN (O-01 a O-04)",
            "",
        ]
    )
    for o in OBJETIVOS_LOGISTICFY:
        lineas.extend(
            [
                f"[{o['id']}] {o['objetivo']}",
                "",
                f"  • Destinatarios : {o['destinatarios']}",
                f"  • Justificación : {o['justificacion']}",
                "",
            ]
        )

    lineas.extend(
        [
            "3. PLAN DE ACCIONES (A-01 a A-04)",
            "",
        ]
    )
    for a in ACCIONES_LOGISTICFY:
        lineas.extend(
            [
                f"[{a['id']}] Objetivo: {a['objetivo']}  |  Material: {a['material']}",
                "",
                f"  • Destinatarios   : {a['destinatarios']}",
                f"  • Acción y canal  : {a['accion_canal']}",
                f"  • Temporalización : {a['temporalizacion']}",
                f"  • Responsable     : {a['responsable']}",
                "",
            ]
        )

    return "\n".join(lineas)


def guardar_evidencia_json(
    area: str, aciertos: int, total: int, detalle: list[dict]
) -> Path:
    registro = []
    if RUTA_EVIDENCIAS.exists():
        try:
            registro = json.loads(RUTA_EVIDENCIAS.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            registro = []

    porcentaje = round((aciertos / total) * 100, 1)
    registro.append(
        {
            "fecha": datetime.now().isoformat(timespec="seconds"),
            "accion": "A-01",
            "material": "M-01",
            "area": area,
            "aciertos": aciertos,
            "total_casos": total,
            "porcentaje_acierto": porcentaje,
            "detalle": detalle,
        }
    )
    RUTA_EVIDENCIAS.write_text(
        json.dumps(registro, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return RUTA_EVIDENCIAS


def formatear_evidencias_texto_claro(ruta: Path) -> str:
    if not ruta.exists():
        return (
            "Todavía no hay evidencias guardadas.\n"
            "Completa el Taller Práctico (pestaña 2) y guarda el resultado para generar "
            
        )

    try:
        datos = json.loads(ruta.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return "El archivo de evidencias existe, pero no tiene un formato JSON válido."

    if not isinstance(datos, list) or len(datos) == 0:
        return "El archivo de evidencias está vacío."

    total_sesiones = len(datos)
    media_porcentaje = round(
        sum(float(item.get("porcentaje_acierto", 0)) for item in datos) / total_sesiones,
        1,
    )

    lineas = [
        "RESUMEN DE EVIDENCIAS",
        "",
        f"Sesiones registradas (anónimas): {total_sesiones}   |   Acierto medio: {media_porcentaje}%",
        "",
        "",
    ]

    for idx, item in enumerate(datos, start=1):
        fecha_raw = str(item.get("fecha", ""))
        try:
            fecha_legible = datetime.fromisoformat(fecha_raw).strftime("%d/%m/%Y a las %H:%M:%S")
        except ValueError:
            fecha_legible = fecha_raw or "Sin fecha"

        area = item.get("area", "No especificada")
        aciertos = item.get("aciertos", 0)
        total_casos = item.get("total_casos", 0)
        porcentaje = item.get("porcentaje_acierto", 0)

        detalle_items = item.get("detalle", [])
        resumen_casos = ", ".join(
            f"{d.get('caso', '?')}: {'OK' if d.get('acierto') else 'REVISAR'}"
            for d in detalle_items
        )

        lineas.extend(
            [
                f"Sesión #{idx} · {fecha_legible}",
                "",
                f"  • Departamento / perfil : {area}",
                f"  • Resultado             : {aciertos}/{total_casos} ({porcentaje}%)",
                f"  • Detalle por caso      : {resumen_casos if resumen_casos else 'Sin detalle'}",
                "",
            ]
        )

    return "\n".join(lineas)


class AppConcienciacionLogisticfy:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Logisticfy · Programa de Concienciación en Ciberseguridad")
        self.root.geometry("940x680")
        self.root.minsize(840, 620)
        self.root.configure(bg="#F4F6F9")

        self.indice_caso = 0
        self.aciertos = 0
        self.respondido_actual = False
        self.detalle_sesion: list[dict] = []
        self.opcion_seleccionada = tk.StringVar(value="")
        self.area_seleccionada = tk.StringVar(value=AREAS_LOGISTICFY[0])

        self._configurar_estilos()
        self._construir_interfaz()

    def _configurar_estilos(self) -> None:
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("TNotebook", background="#F4F6F9", borderwidth=0)
        style.configure(
            "TNotebook.Tab",
            font=("Segoe UI", 10, "bold"),
            padding=(14, 8),
        )
        style.configure(
            "Accent.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(14, 8),
        )

    def _construir_interfaz(self) -> None:
        header = tk.Frame(self.root, bg="#1B365D", padx=20, pady=14)
        header.pack(fill="x")

        tk.Label(
            header,
            text="LOGISTICFY · CIBERSEGURIDAD Y CONCIENCIACIÓN",
            font=("Segoe UI", 14, "bold"),
            fg="#FFFFFF",
            bg="#1B365D",
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Taller práctico",
            font=("Segoe UI", 9),
            fg="#D0DCEB",
            bg="#1B365D",
        ).pack(anchor="w", pady=(2, 0))

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=16, pady=14)

        self.tab_guia = tk.Frame(self.notebook, bg="#F4F6F9")
        self.tab_taller = tk.Frame(self.notebook, bg="#F4F6F9")
        self.tab_evidencias = tk.Frame(self.notebook, bg="#F4F6F9")
        self.tab_marco = tk.Frame(self.notebook, bg="#F4F6F9")

        self.notebook.add(self.tab_guia, text="  1. Guía Rápida ")
        self.notebook.add(self.tab_taller, text="  2. Taller Práctico ")
        self.notebook.add(self.tab_evidencias, text="  3. Evidencias Guardadas ")
        self.notebook.add(self.tab_marco, text="  4. Normas, Objetivos y Acciones  ")

        self._construir_tab_guia()
        self._construir_tab_taller()
        self._construir_tab_evidencias()
        self._construir_tab_marco()

        self.notebook.bind("<<NotebookTabChanged>>", self._al_cambiar_pestana)

    def _construir_tab_guia(self) -> None:
        marco = tk.Frame(self.tab_guia, bg="#FFFFFF", bd=1, relief="solid", padx=16, pady=16)
        marco.pack(fill="both", expand=True, pady=6)

        texto = scrolledtext.ScrolledText(
            marco,
            wrap="word",
            font=("Consolas", 10),
            bg="#FFFFFF",
            fg="#1F2933",
            relief="flat",
            padx=8,
            pady=8,
        )
        texto.insert("1.0", TEXTO_GUIA_RAPIDA)
        texto.configure(state="disabled")
        texto.pack(fill="both", expand=True)

        pie = tk.Frame(self.tab_guia, bg="#F4F6F9")
        pie.pack(fill="x", pady=(6, 0))
        ttk.Button(
            pie,
            text="Ir al Taller Práctico →",
            style="Accent.TButton",
            command=lambda: self.notebook.select(self.tab_taller),
        ).pack(side="right")

    def _construir_tab_taller(self) -> None:
        barra = tk.Frame(self.tab_taller, bg="#FFFFFF", bd=1, relief="solid", padx=14, pady=10)
        barra.pack(fill="x", pady=(6, 10))

        tk.Label(
            barra,
            text="Departamento / perfil:",
            font=("Segoe UI", 10, "bold"),
            bg="#FFFFFF",
            fg="#1F2933",
        ).pack(side="left")

        combo_area = ttk.Combobox(
            barra,
            textvariable=self.area_seleccionada,
            values=AREAS_LOGISTICFY,
            state="readonly",
            width=26,
            font=("Segoe UI", 10),
        )
        combo_area.pack(side="left", padx=(8, 16))

        self.lbl_progreso = tk.Label(
            barra,
            text="",
            font=("Segoe UI", 10, "bold"),
            bg="#FFFFFF",
            fg="#1B365D",
        )
        self.lbl_progreso.pack(side="right")

        self.card_caso = tk.Frame(
            self.tab_taller, bg="#FFFFFF", bd=1, relief="solid", padx=18, pady=16
        )
        self.card_caso.pack(fill="both", expand=True)

        self.lbl_caso_titulo = tk.Label(
            self.card_caso,
            text="",
            font=("Segoe UI", 11, "bold"),
            bg="#FFFFFF",
            fg="#1B365D",
        )
        self.lbl_caso_titulo.pack(anchor="w")

        self.lbl_escenario = tk.Label(
            self.card_caso,
            text="",
            font=("Segoe UI", 10),
            bg="#F8FAFC",
            fg="#1F2933",
            wraplength=840,
            justify="left",
            padx=12,
            pady=10,
            bd=1,
            relief="groove",
        )
        self.lbl_escenario.pack(fill="x", pady=(10, 14))

        self.frame_opciones = tk.Frame(self.card_caso, bg="#FFFFFF")
        self.frame_opciones.pack(fill="x")

        self.radios: dict[str, tk.Radiobutton] = {}
        for clave in ("A", "B", "C"):
            rb = tk.Radiobutton(
                self.frame_opciones,
                text="",
                variable=self.opcion_seleccionada,
                value=clave,
                font=("Segoe UI", 10),
                bg="#FFFFFF",
                fg="#1F2933",
                activebackground="#EEF2F7",
                wraplength=820,
                justify="left",
                anchor="w",
                pady=6,
            )
            rb.pack(fill="x", anchor="w")
            self.radios[clave] = rb

        self.lbl_feedback = tk.Label(
            self.card_caso,
            text="",
            font=("Segoe UI", 10),
            bg="#FFFFFF",
            fg="#1F2933",
            wraplength=840,
            justify="left",
            padx=12,
            pady=10,
        )
        self.lbl_feedback.pack(fill="x", pady=(14, 6))

        botones = tk.Frame(self.tab_taller, bg="#F4F6F9")
        botones.pack(fill="x", pady=(10, 0))

        ttk.Button(
            botones,
            text="Reiniciar taller",
            command=self._reiniciar_taller,
        ).pack(side="left")

        self.btn_siguiente = ttk.Button(
            botones,
            text="Siguiente caso →",
            command=self._siguiente_caso,
            state="disabled",
        )
        self.btn_siguiente.pack(side="right", padx=(8, 0))

        self.btn_comprobar = ttk.Button(
            botones,
            text="Comprobar decisión",
            style="Accent.TButton",
            command=self._comprobar_respuesta,
        )
        self.btn_comprobar.pack(side="right")

        self._cargar_caso_actual()

    def _construir_tab_evidencias(self) -> None:
        barra = tk.Frame(self.tab_evidencias, bg="#FFFFFF", bd=1, relief="solid", padx=14, pady=10)
        barra.pack(fill="x", pady=(6, 10))

        tk.Label(
            barra,
            text="Informe de evidencias del taller páctico",
            font=("Segoe UI", 10, "bold"),
            bg="#FFFFFF",
            fg="#1F2933",
        ).pack(side="left")

        ttk.Button(
            barra,
            text="Actualizar vista",
            command=self._refrescar_evidencias,
        ).pack(side="right")

        marco = tk.Frame(self.tab_evidencias, bg="#FFFFFF", bd=1, relief="solid", padx=14, pady=14)
        marco.pack(fill="both", expand=True)

        self.txt_evidencias = scrolledtext.ScrolledText(
            marco,
            wrap="word",
            font=("Consolas", 10),
            bg="#FFFFFF",
            fg="#1F2933",
            relief="flat",
        )
        self.txt_evidencias.pack(fill="both", expand=True)
        self._refrescar_evidencias()

    def _construir_tab_marco(self) -> None:
        barra = tk.Frame(self.tab_marco, bg="#FFFFFF", bd=1, relief="solid", padx=14, pady=10)
        barra.pack(fill="x", pady=(6, 10))

        tk.Label(
            barra,
            text="Referencia de Normas (N-01..N-07), Objetivos (O-01..O-04) y Acciones (A-01..A-04)",
            font=("Segoe UI", 10, "bold"),
            bg="#FFFFFF",
            fg="#1F2933",
        ).pack(side="left")

        marco = tk.Frame(self.tab_marco, bg="#FFFFFF", bd=1, relief="solid", padx=14, pady=14)
        marco.pack(fill="both", expand=True)

        txt = scrolledtext.ScrolledText(
            marco,
            wrap="word",
            font=("Consolas", 10),
            bg="#FFFFFF",
            fg="#1F2933",
            relief="flat",
        )
        txt.insert("1.0", construir_texto_normas_y_programa())
        txt.configure(state="disabled")
        txt.pack(fill="both", expand=True)
        
    def _cargar_caso_actual(self) -> None:
        caso = CASOS_PRACTICOS[self.indice_caso]
        total = len(CASOS_PRACTICOS)
        self.respondido_actual = False
        self.opcion_seleccionada.set("")

        self.lbl_progreso.configure(
            text=f"Caso {self.indice_caso + 1} de {total} · Aciertos: {self.aciertos}"
        )
        self.lbl_caso_titulo.configure(
            text=f"{caso['id']} · Ámbito habitual: {caso['area']}"
        )
        self.lbl_escenario.configure(text=caso["escenario"])

        for clave, texto in caso["opciones"].items():
            self.radios[clave].configure(text=f"{clave})  {texto}", state="normal")

        self.lbl_feedback.configure(text="", bg="#FFFFFF", bd=0)
        self.btn_comprobar.configure(state="normal")
        self.btn_siguiente.configure(
            state="disabled",
            text="Finalizar taller" if self.indice_caso == total - 1 else "Siguiente caso →",
        )

    def _comprobar_respuesta(self) -> None:
        if self.respondido_actual:
            return

        elegida = self.opcion_seleccionada.get()
        if elegida not in ("A", "B", "C"):
            messagebox.showwarning(
                "Selección requerida",
                "Por favor, selecciona una opción (A, B o C) antes de comprobar.",
            )
            return

        caso = CASOS_PRACTICOS[self.indice_caso]
        es_correcta = elegida == caso["correcta"]
        self.respondido_actual = True

        if es_correcta:
            self.aciertos += 1
            estado = "CORRECTA"
            bg_color = "#E6F4EA"
            fg_color = "#137333"
        else:
            estado = f"INCORRECTA (Opción correcta: {caso['correcta']})"
            bg_color = "#FEF7E0"
            fg_color = "#B06000"

        self.detalle_sesion.append({"caso": caso["id"], "acierto": es_correcta})

        for rb in self.radios.values():
            rb.configure(state="disabled")

        self.lbl_progreso.configure(
            text=f"Caso {self.indice_caso + 1} de {len(CASOS_PRACTICOS)} · Aciertos: {self.aciertos}"
        )
        self.lbl_feedback.configure(
            text=f"{estado}\n{caso['explicacion']}",
            bg=bg_color,
            fg=fg_color,
            bd=1,
            relief="solid",
        )
        self.btn_comprobar.configure(state="disabled")
        self.btn_siguiente.configure(state="normal")

    def _siguiente_caso(self) -> None:
        if self.indice_caso < len(CASOS_PRACTICOS) - 1:
            self.indice_caso += 1
            self._cargar_caso_actual()
        else:
            self._finalizar_taller()

    def _finalizar_taller(self) -> None:
        total = len(CASOS_PRACTICOS)
        porcentaje = round((self.aciertos / total) * 100, 1)
        area = self.area_seleccionada.get()

        guardar = messagebox.askyesno(
            "Taller finalizado",
            f"Has completado el taller práctico.\n\n"
            f"Área: {area}\n"
            f"Puntuación: {self.aciertos}/{total} ({porcentaje}%)\n\n"
            f"¿Deseas guardar el resultado agregado y anónimo en '{RUTA_EVIDENCIAS}' "
            f"como evidencia de seguimiento (apartado 2.3)?",
        )
        if guardar:
            ruta = guardar_evidencia_json(area, self.aciertos, total, self.detalle_sesion)
            self._refrescar_evidencias()
            messagebox.showinfo(
                "Evidencia guardada",
                f"Resultado registrado correctamente en:\n{ruta.resolve()}\n\n"
                "(Sin datos personales identificativos).",
            )
            self.notebook.select(self.tab_evidencias)

        self._reiniciar_taller()

    def _reiniciar_taller(self) -> None:
        self.indice_caso = 0
        self.aciertos = 0
        self.detalle_sesion = []
        self._cargar_caso_actual()

    def _refrescar_evidencias(self) -> None:
        self.txt_evidencias.configure(state="normal")
        self.txt_evidencias.delete("1.0", "end")
        self.txt_evidencias.insert("1.0", formatear_evidencias_texto_claro(RUTA_EVIDENCIAS))
        self.txt_evidencias.configure(state="disabled")

    def _al_cambiar_pestana(self, _event: tk.Event) -> None:
        if self.notebook.index(self.notebook.select()) == 2:
            self._refrescar_evidencias()


def main() -> None:
    root = tk.Tk()
    AppConcienciacionLogisticfy(root)
    root.mainloop()


if __name__ == "__main__":
    main()