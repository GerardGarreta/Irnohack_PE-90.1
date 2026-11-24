# Propuesta de prevención y concienciación para Logisticfy

### 1.1. Análisis del contexto y necesidades de protección

Logisticfy es una startup logística B2B con sede en Barcelona y una plantilla de 20 personas (19 empleados y 1 persona en prácticas) que gestiona entre 80 y 120 expediciones diarias para unos 25 clientes empresariales, apoyándose en 3 transportistas externos.

Su actividad gira en torno a un flujo continuo de datos entre: 

- Procesos
- Creación de expediciones
- Validación y gestión por Operaciones
- Asignación de transportistas
- Seguimiento de envíos
- Atención de incidencias junto con Atención al Cliente
- Facturación por Administración, soportado por un portal de clientes
- Un backoffice
- Una API REST
- Una base de datos PostgreSQL
- Puestos Windows 11
- Red de oficina
- Correo corporativo externo
- Copias de seguridad
- Registros.


## Hechos documentados vs. supuestos y propuestas:

Hechos documentados: 

- Estructura organizativa y de procesos; arquitectura conceptual sin direcciones IP, versiones, configuraciones ni distribución física concreta; inventario de 13 activos (SW-01 a PHY-01); inexistencia de precios fijados y de una auditoría o certificación previa de controles.
- La falta de detalle técnico o de control documentado en la ficha no implica incumplimiento.

Propuestas y supuestos de diseño: 

- Este documento plantea un marco de protección, un programa de concienciación y un material formativo (M-01). Cuando se mencionan mecanismos como el registro de actividad o el control de accesos, se entienden como ámbitos o líneas de trabajo a definir y operar en la organización, no como controles ya implantados o verificados.

| ID | Activo | Necesidad de protección | Proceso o función relacionada | 
| :--- | :--- | :--- | :--- |
| SW-01 | Plataforma web y backoffice | Mantener la disponibilidad e integridad del portal y del backoffice para evitar interrupciones en la operativa diaria (80–120 expediciones/día) y accesos no autorizados a datos operativos o de clientes. | Creación de expediciones; validación y gestión de solicitudes; seguimiento de envíos; atención de incidencias; facturación. | 
| SW-02 | API de integración con transportistas | Asegurar la integridad, autenticidad y disponibilidad del intercambio de información entre la plataforma de Logisticfy y los transportistas para no perder o alterar estados y datos de envío. | Asignación de transportistas; seguimiento de envíos. | 
| DAT-01 | Base de datos de clientes, envíos y facturación | Proteger la confidencialidad, integridad y disponibilidad de datos de empresas clientes, contactos, destinatarios, direcciones, incidencias y facturación, incluidos datos personales asociados a operaciones B2B. | Todos los procesos del negocio (desde la solicitud hasta el seguimiento, incidencias y facturación). |
| IAM-01 | Identidades y mecanismos de acceso | Evitar accesos indebidos o privilegios excesivos sobre cuentas, aplicaciones y datos críticos mediante autenticación adecuada y separación de funciones acorde a cada puesto. | Acceso transversal a SW-01, DAT-01, SW-03, COM-01 y entornos de administración (INF-01, MON-01, BKP-01). |
| COM-01 | Correo corporativo | Prevenir engaños (phishing), suplantación o fugas de información a través de un servicio externo clave para coordinar con clientes, transportistas y gestiones internas. | Atención de incidencias del servicio logístico; asignación de transportistas; comunicación comercial y administrativa. |
| EXT-01 | Integraciones con tres transportistas externos | Controlar la dependencia y el intercambio de información con proveedores externos para que fallos, incidencias o accesos indebidos en las conexiones no comprometan las expediciones ni los datos de Logisticfy. | Asignación de transportistas; seguimiento de envíos; atención de incidencias. |
| HW-01 | Equipos Windows del personal | Mantener los puestos de trabajo en condiciones seguras y libres de software malicioso o configuraciones inadecuadas que expongan credenciales o información de la empresa. | Trabajo cotidiano de Operaciones, Atención al Cliente, Administración, Comercial y Tecnología/IT. |
| MON-01 | Registros y sistema de monitorización | Conservar información fiable y accesible de aplicación, sistema y autenticación para detectar anomalías, investigar incidencias y reconstruir eventos operativos o de seguridad. | Sostenimiento técnico (INF-01, SW-01, SW-02), atención de incidencias y control de accesos (IAM-01). | 
| BKP-01 | Copias de seguridad | Garantizar la recuperación de información y elementos clave ante borrados accidentales, fallos o incidentes, verificando periódicamente su disponibilidad e integridad. | Continuidad de la información de negocio (DAT-01), código (SW-03), registros (MON-01) y configuración/servicios (INF-01). |

### 1.2. Principios generales de ciberseguridad

| ID | Principio propuesto | Aplicación en Logisticfy | Justificación |
| :--- | :--- | :--- | :--- |
| P-01 | Responsabilidad y rendición de cuentas | Cada puesto de trabajo y departamento asume la responsabilidad de aplicar las normas de seguridad en sus tareas habituales, con coordinación de Dirección y apoyo técnico de Tecnología/IT. | Una plantilla de 20 personas (incluida 1 persona en prácticas) requiere corresponsabilidad clara para proteger expediciones, incidencias y datos compartidos entre áreas. |
| P-02 | Mínimo privilegio y separación de funciones | Cada cuenta o usuario accede únicamente a los sistemas, datos y funciones estrictamente necesarios para su rol (por ejemplo, gestores operativos frente a administración económica o administración de sistemas). | Protege DAT-01, SW-01, SW-03 e INF-01 mediante IAM-01, reduciendo el impacto de errores humanos o cuentas comprometidas en la operativa diaria. |
| P-03 | Protección del dato a lo largo de su ciclo de vida | Los datos de clientes, contactos, destinatarios, direcciones, expediciones, incidencias y facturación se tratan con cuidado desde su captura hasta su archivo o eliminación, incluyendo datos de personas en el entorno B2B. | Una misma expedición circula por solicitud, validación, transporte, seguimiento, incidencias y facturación (DAT-01), por lo que su integridad y confidencialidad son críticas en todo el flujo. |
| P-04 | Resiliencia operativa y continuidad | Se prioriza mantener operativos los servicios de gestión de envíos y contar con medios de recuperación y trazabilidad ante fallos o incidentes. | Gestionar entre 80 y 120 expediciones diarias depende de SW-01, SW-02, EXT-01 e INF-01, respaldados por BKP-01 y MON-01. |
| P-05 | Confianza verificada en proveedores y canales externos | Las comunicaciones por correo y las conexiones con terceros se tratan con cautela, verificando remitentes, canales y alcances de intercambio antes de actuar o compartir información. | Logisticfy opera con 3 transportistas externos (EXT-01), correo corporativo externo (COM-01) y alojamiento cloud, lo que exige no dar por segura cualquier interacción externa. |
| P-06 | Notificación temprana y aprendizaje continuo | Cualquier indicio de fallo, acceso anómalo, mensaje sospechoso o error operativo con impacto en seguridad se comunica con rapidez y se utiliza para reforzar hábitos y controles. | La detección temprana en puestos (HW-01, COM-01) y sistemas (MON-01) evita que un incidente menor afecte a clientes, expediciones o a la organización.|

Conocimiento y respaldo de DirecciónPresentación a Dirección: 

- El responsable de operaciones (junto con el consultor externo o el Responsable IT, según la fase del encargo) presentaría estos principios en una sesión breve de trabajo con Dirección (CEO y responsable de operaciones), centrada en su vínculo con la continuidad de las 80–120 expediciones diarias, la relación con los 25 clientes y los 3 transportistas, y su carácter orientador sin añadir cargas burocráticas innecesarias.

Constancia del respaldo: 

- El respaldo se propondría formalizar mediante un documento breve de aprobación o acta de reunión de Dirección firmado o validado por CEO y responsable de operaciones, donde conste la fecha, los principios aprobados (P-01 a P-06) y el mandato para elaborar y difundir la normativa del puesto de trabajo y el programa de concienciación.

Comunicación al personal:

- Una vez respaldados por Dirección, se difundirían a toda la plantilla (19 empleados y persona en prácticas) mediante una comunicación interna oficial y una sesión breve o espacio accesible en los canales habituales de la empresa, explicando qué significan en el día a día de cada departamento y enlazando con la normativa aplicable.

### 1.3. Normativa de protección del puesto de trabajo

Ámbito de aplicación: 

- Aplica a todas las personas que trabajan o colaboran en Logisticfy —incluidos Dirección, Operaciones, Atención al Cliente, Tecnología/IT, Comercial, Administración y la persona en prácticas— en el uso de sistemas, información, comunicaciones y espacios de trabajo de la organización, ya sea de forma presencial o remota cuando corresponda.

Responsabilidades generales: 

- Dirección impulsa y respalda la normativa; el responsable de operaciones coordina su alineación con la actividad de negocio; cada responsable de área vela por su aplicación en su equipo; Tecnología/IT presta soporte técnico y asesora en medidas técnicas y registros; y cada persona trabajadora es responsable de cumplir las normas en su puesto y notificar anomalías.

| ID | Norma propuesta | Destinatarios | Aplicación y posible verificación | Excepciones, si procede | 
| :--- | :--- | :--- | :--- | :--- |
| N-01 | Uso personal de cuentas y control de sesión: Cada persona utiliza exclusivamente su propia cuenta asignada (IAM-01), no comparte contraseñas ni credenciales y bloquea la pantalla de su equipo (HW-01) al ausentarse de su puesto. | Todo el personal (incluida la persona en prácticas). | Aplicación: Iniciar sesión con credencial propia y pulsar bloqueo de pantalla al levantarse o finalizar la jornada. Verificación: Revisión de políticas de bloqueo de sesión en equipos y análisis de registros de autenticación (MON-01) o comprobaciones visuales en puesto. | No se admiten cuentas compartidas ordinarias; cualquier acceso temporal o de soporte técnico se canaliza mediante procedimientos autorizados por Tecnología/IT. |
| N-02 | Acceso según función y entorno: El acceso a aplicaciones, base de datos, repositorios y entornos técnicos (SW-01, DAT-01, SW-03, INF-01, BKP-01, MON-01) se limita al rol asignado; no se realizan cambios directos en datos o entornos productivos fuera del procedimiento establecido. | Todo el personal, con especial atención a Tecnología/IT, Operaciones y Administración. | Aplicación: Solicitar permisos acordes al puesto y operar por los flujos previstos en backoffice, base de datos o sistemas. Verificación: Revisión periódica de perfiles/permisos en IAM-01 y consulta de registros de acceso y cambios en MON-01. | Excepciones puntuales o urgentes requerirían autorización previa del responsable correspondiente y del Responsable IT, quedando registradas para su revisión posterior. | 
| N-03 | Uso adecuado de equipos y software corporativo: Los equipos Windows (HW-01) se emplean para fines profesionales; no se instalan programas no autorizados, no se desactivan controles de seguridad ni se conecta almacenamiento externo no permitido. | Todo el personal (incluida la persona en prácticas). | Aplicación: Trabajar únicamente con aplicaciones corporativas autorizadas y solicitar a Tecnología/IT cualquier herramienta o instalación necesaria. Verificación: Inventario de software y configuraciones en HW-01 y registros de sistema/seguridad (MON-01). | El personal de Tecnología/IT puede utilizar herramientas técnicas específicas para administración y soporte dentro de su ámbito autorizado. | 
| N-04 | Tratamiento cuidadoso de datos de envíos, clientes y personas: La información de clientes, contactos, destinatarios, direcciones, incidencias y facturación (DAT-01) se consulta y utiliza solo para fines del servicio; no se exportan ni descargan listados innecesarios ni se envían por canales no autorizados. | Todo el personal, especialmente Operaciones, Atención al Cliente, Comercial y Administración. | Aplicación: Gestionar expediciones, consultas e incidencias desde las herramientas corporativas y evitar copias locales o envíos externos sin justificación operativa. Verificación: Revisión de accesos/exportaciones cuando aplique, control de copias locales en HW-01 y revisión de incidencias de información. | Solo se comparten los datos estrictamente necesarios con transportistas (EXT-01) o clientes a través de los canales y procesos habilitados. | 
| N-05 | Verificación en correo y canales externos: Antes de abrir enlaces o adjuntos inesperados o atender cambios de instrucciones (pagos, cuentas, direcciones sensibles o envíos) en correo (COM-01) o mensajería, se verifica la identidad y solicitud por un canal fiable. | Todo el personal, especialmente Comercial, Administración, Operaciones y Atención al Cliente. | Aplicación: Revisar remitente, contexto y coherencia con la operación en curso; confirmar por vía alternativa o interna ante cualquier duda. Verificación: Análisis de incidentes reportados en COM-01 y ejercicios o revisiones periódicas de hábitos de comunicación. | No aplica excepción a la verificación previa ante solicitudes inusuales o sensibles. | 
| N-06 | Seguridad física en oficina y red: En la oficina (PHY-01) y la red (NET-01), no se deja documentación confidencial o credenciales a la vista, se controla el acceso de visitas o entregas, se usa la red corporativa autorizada y no se conectan dispositivos desconocidos. | Todo el personal en oficina (incluida la persona en prácticas). | Aplicación: Recoger documentos con datos de envíos o facturación al terminar, acompañar o registrar visitas según pauta y conectarse únicamente a NET-01. Verificación: Rondas de orden y limpieza física en PHY-01 y revisión de conexiones/dispositivos en NET-01. | El acceso de visitas o proveedores externos a zonas de trabajo requiere acompañamiento o autorización de la persona responsable designada. |
| N-07 | Comunicación inmediata de anomalías: Cualquier sospecha de phishing, pérdida o robo de equipo/credencial, acceso indebido, fallo de integración (SW-02 / EXT-01) o alteración de datos (DAT-01) se comunica de inmediato por el canal interno establecido. | Todo el personal (incluida la persona en prácticas). | Aplicación: Avisar sin demora al contacto designado de Tecnología/IT y al responsable directo, conservando evidencias básicas (como el correo o mensaje) sin manipular. Verificación: Registro y seguimiento de avisos recibidos y contraste con alertas o eventos en MON-01. | No existe excepción a la obligación de notificar una sospecha razonable de incidencia de seguridad. | 

## Comunicación y revisión de la normativa

Comunicación al personal: 

- La normativa se difundiría mediante entrega o publicación accesible a toda la plantilla (incluyendo su incorporación en la acogida de nuevas incorporaciones y de la persona en prácticas), acompañada de una explicación práctica por departamentos para que cada persona identifique las normas más relevantes para su tarea.

Gestión de excepciones: 

- Cuando una necesidad operativa o técnica requiera apartarse temporalmente de una regla (por ejemplo, un acceso puntual o un procedimiento excepcional), se solicitaría por escrito o por el canal formal previsto indicando motivo, alcance, duración y medidas compensatorias, requiriendo aprobación del responsable del área afectada y del Responsable IT (y de Dirección si el impacto es relevante), con fecha de caducidad.

Revisión y actualización:

- La normativa se revisaría al menos una vez al año o de forma extraordinaria ante cambios relevantes en la organización, procesos, sistemas o incidentes significativos, coordinando los ajustes entre Dirección, Tecnología/IT y las áreas afectadas, y comunicando los cambios a la plantilla.Programa de concienciación

### 2.1. Objetivos y destinatarios

| ID | Objetivo de concienciación | Destinatarios | Justificación |
| :--- | :--- | :--- | :--- |
| O-01 | Identificar correos o mensajes sospechosos (phishing, suplantación de clientes, transportistas o proveedores) y aplicar la verificación previa antes de actuar o compartir datos. | Todo el personal, con foco prioritario en Operaciones, Atención al Cliente, Comercial y Administración. | Estos equipos gestionan a diario solicitudes, incidencias, contactos comerciales y facturación a través de COM-01 y plataformas vinculadas a expediciones y clientes. |
| O-02 | Tratar de forma segura los datos de expediciones, clientes, destinatarios, incidencias y facturación, evitando descargas o envíos indebidos y manteniendo el orden en puestos y canales. | Operaciones, Atención al Cliente, Administración y Comercial (y todo el personal que maneje datos operativos). | Una misma expedición recorre varios procesos y departamentos (DAT-01, SW-01, HW-01, PHY-01); un error de manejo o envío puede exponer datos o generar incidencias operativas. |
| O-03 | Aplicar hábitos seguros de autenticación, control de sesión y uso de recursos técnicos conforme al rol y a los procedimientos establecidos. | Todo el personal, incluyendo específicamente a la persona en prácticas y a Tecnología/IT. | La persona en prácticas se incorpora a entornos de trabajo y sistemas que requieren conocer desde el inicio las reglas de acceso (IAM-01), uso de HW-01 y límites de actuación; Tecnología/IT necesita reforzar buenas prácticas de administración y segregación. |
| O-04 | Reconocer señales tempranas de anomalía (en accesos, envíos, integraciones o equipos) y notificarlas rápidamente siguiendo el circuito interno. | Todo el personal (19 empleados y persona en prácticas). | La detección rápida por parte de cualquier usuario complementa a MON-01 y permite contener problemas en SW-01, SW-02, EXT-01, COM-01 o HW-01 antes de que escalen. | 

### 2.2. Plan de acciones de concienciación

| ID | Objetivo | Destinatarios | Acción y canal | Temporalización | Responsable | Material |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| A-01 | O-01 (y apoyo a O-04) | Operaciones, Atención al Cliente, Comercial y Administración (extensible a toda la plantilla). | Taller práctico breve y distribución de guía sobre phishing y verificación de solicitudes/incidencias: sesión presencial o en sala de reunión/videollamada de 30–40 min con casos reales adaptados a logística (cambios de entrega, facturas o transportistas), apoyada por canal interno (COM-01 o espacio corporativo). | Mes 1 del programa (una sesión de 35 min; consulta permanente posterior). | Responsable IT (con apoyo de un referente de Operaciones o Atención al Cliente). | M-01 (Guía rápida: cómo detectar correos sospechosos y verificar cambios en envíos y facturación). |
| A-02 | O-02 | Operaciones, Atención al Cliente, Administración y Comercial. | Cápsula operativa por departamentos sobre manejo seguro de datos de expediciones, clientes y facturación: dinámica de 20–25 min por grupos reducidos revisando el flujo de una expedición desde la solicitud hasta la facturación y el orden en puesto/archivos. | Mes 2 del programa (sesiones de 25 min por grupo). | Responsable de operaciones / Responsable de área con apoyo de Tecnología/IT. | M-02 (Ficha de flujo seguro de datos en expediciones y facturación). |
| A-03 | O-03 | Persona en prácticas y nuevas incorporaciones (con recordatorio general para la plantilla). | Sesión de acogida de seguridad en el puesto y verificación de accesos/normativa: recorrido guiado de 25 min al inicio de la incorporación (y recordatorio trimestral breve) sobre cuentas, bloqueo de pantalla, uso de HW-01, NET-01 y alcance de permisos. | Al inicio de la incorporación (25 min) y recordatorio cada 3 meses. | Responsable IT / Administrador de sistemas (con tutoría del área correspondiente). | M-03 (Lista de comprobación inicial del puesto y accesos). |
| A-04 | O-04 (y refuerzo de O-01–O-03) | Todo el personal (20 personas). | Simulacro sencillo de reporte de anomalía y recordatorio periódico: envío de un aviso o caso práctico de prueba controlado (sin impacto en producción) y publicación de recordatorios breves por canal interno para practicar cuándo y cómo avisar. | Trimestral (ejercicio de 15 min + recordatorio mensual breve). | Responsable IT (con coordinación del responsable de operaciones). | M-04 (Guion de ejercicio de notificación de anomalías y recordatorios trimestrales). |

### 2.3. Seguimiento y evaluación del programa

| Objetivo o acción | Indicador | Evidencia prevista | Momento de revisión |
| :--- | :--- | :--- | :--- |
| A-01 / O-01 | Porcentaje de asistentes convocados que participan en la sesión y porcentaje de respuestas correctas en casos prácticos de verificación antes de actuar. | Registro de asistencia a la sesión y resultados anónimos o agregados de los casos prácticos/cuestionario breve realizado al cierre. | Al finalizar el Mes 1 y en la revisión trimestral del programa. |
| A-02 / O-02 | Porcentaje de departamentos/perfiles clave que completan la cápsula y reducción de incidencias o consultas por manejo inadecuado de datos/documentos en el puesto. | Registro de realización de las sesiones por grupo y revisión de anotaciones de incidencias operativas o de seguridad vinculadas a datos. | Al finalizar el Mes 2 y en la revisión semestral. |
| A-03 / O-03 | Porcentaje de nuevas incorporaciones o personas en prácticas que completan la sesión de acogida inicial y ausencia de incidencias básicas por sesiones abiertas o usos no autorizados. | Registro de acogida inicial completada y comprobaciones técnicas/operativas periódicas acordes a la normativa (N-01 a N-03). | Tras cada incorporación y en cada revisión trimestral. |
| A-04 / O-04 | Tiempo de reacción y porcentaje de personas que comunican la anomalía simulada por el canal correcto siguiendo la pauta (N-07). | Registro del ejercicio de prueba (quién notificó, por qué canal y en qué plazo aproximado) y registro de avisos reales recibidos. | Tras cada ejercicio trimestral. | 

Revisión y mejora:

- Los resultados del seguimiento se revisarían trimestralmente (y con una evaluación general al cabo de 6 y 12 meses) entre el Responsable IT, el responsable de operaciones y las áreas implicadas.
- Si un indicador muestra baja participación, dudas recurrentes sobre un tipo de mensaje o retrasos en la notificación de anomalías, se ajustarían los ejemplos prácticos de las sesiones, se reforzaría el material de apoyo o se adaptarían los horarios y formatos a la carga de trabajo de las 80–120 expediciones diarias.

## Desarrollo del material de concienciación

### 3.1. Material desarrollado

- ID del material: M-01
- Título: Guía Logisticfy - Detectar correos sospechosos y verificar cambios en envíos y facturación
- Formato: Guía breve - Ficha operativa de consulta.

Contenido del material

Guía Logisticfy (M-01)

Detectar correos sospechosos y verificar cambios en envíos y facturaciónPara equipos de Operaciones, Atención al Cliente, Comercial y Administración (y toda la plantilla)

En el trabajo diario gestionamos decenas de expediciones, consultas, proveedores de transporte y datos de clientes y facturación. Muchos intentos de engaño (phishing) aprovechan precisamente ese ritmo: parecen venir de un cliente, de un transportista o de un compañero y piden actuar rápido.

1. Cinco señales de alerta frecuentes en el correo (COM-01)Urgencia artificial o presión:

- "Urgente: bloqueamos la entrega si no respondes hoy" o "Revisa esta factura/incidencia de inmediato".
- Cambios sensibles inesperados: Nuevas cuentas bancarias para cobros/pagos, cambios de dirección de entrega o facturación no tramitados por el canal habitual, o peticiones de listados de clientes/expediciones.
- Remitente engañoso: Dirección parecida a la real pero con pequeñas diferencias (letras cambiadas, otro dominio o nombre visible distinto a la dirección de correo).
- Enlaces o adjuntos poco claros: Enlaces que llevan a páginas de inicio de sesión externas o archivos comprimidos/documentos inesperados vinculados a un supuesto envío o incidencia.
- Desfase con la operativa real: El mensaje menciona una expedición, cliente o incidencia que no encaja con lo que consta en la plataforma o en el trabajo del área.

2. Regla de oro antes de actuar (N-05 y N-04)

Si hay duda o el mensaje pide algo sensible, no respondas dando datos, no abras enlaces sospechosos y no ejecutes el cambio a ciegas.

- Comprueba en la operativa: Revisa si la solicitud o el estado del envío encaja con la información registrada en el sistema.
- Verifica por un canal fiable: Confirma el cambio o la petición con el contacto habitual o con el responsable/compañero correspondiente utilizando un medio conocido y de confianza (no respondas directamente sobre un correo dudoso si sospechas suplantación).
- Protege los datos: No envíes información de clientes, destinatarios, expediciones o facturación a direcciones externas no verificadas.

3. ¿Qué hacer si sospechas que es un engaño o un problema? (N-07)

- No lo reenvíes masivamente ni borres las pruebas básicas si puedes evitarlo.
- Avisa de inmediato al contacto designado de Tecnología/IT y a tu responsable directo indicando qué has visto y a qué hora.
- Si ya hiciste clic en un enlace, descargaste un archivo o facilitaste datos/credenciales, notifícalo sin demora para poder actuar rápido.

### 3.2. Vinculación con el programa

- Objetivo relacionado: O-01 (y apoyo a O-04).
- Acción relacionada: A-01 (Taller práctico breve y distribución de guía sobre phishing y verificación de solicitudes/incidencias).
- Destinatarios: Operaciones, Atención al Cliente, Comercial y Administración (extensible a toda la plantilla).
- Canal: Sesión breve presencial o en sala/videollamada de apoyo y difusión a través del correo corporativo (COM-01) o espacio interno de consulta habitual.
- Uso previsto: Se entregaría o proyectaría al inicio y durante el taller práctico (A-01) para analizar casos concretos de envíos, incidencias y facturación, y quedaría disponible como hoja de consulta rápida en el puesto de trabajo para aplicar la verificación antes de actuar.
- Ubicación del archivo: Incluido íntegramente en este documento (apartado 3.1, Contenido del material, identificado como M-01).

## Fuentes, supuestos y autoría

### 4.1. Fuentes y recursos utilizados

| Fuente o recurso | Referencia | Uso realizado |
| :--- | :--- | :--- |
| [PE 90.1] Logisticfy | Contexto empresarial, organización, procesos, sistemas e inventario de activos (SW-01 a PHY-01). | Base del análisis de contexto, selección de activos y procesos, diseño de principios, normativa, programa de concienciación y casos prácticos de M-01. | 
| [PE 90.1] Breafing / Actividades / Plantilla / Comprobaciones | Directrices del encargo, estructura de bloques, criterios de evaluación y lista de verificación. | Estructura de la entrega, diferenciación entre hechos y propuestas, y alineación con los requisitos solicitados. | 
| Biblioteca estándar de Python 3 | Módulos datetime, json y pathlib. | Implementación sin dependencias externas de programa/IG-Concienciacion.py. | 

### 4.2. Supuestos y limitaciones

- Información conocida vs. propuesta: El contexto organizativo, operativo y de activos procede de [PE 90.1] Logisticfy. La arquitectura descrita en el caso es conceptual (sin IPs, versiones, configuraciones ni distribución física fijada), y no se dispone de precios comerciales, configuraciones técnicas concretas ni historial de auditorías previas.
- Supuestos de diseño: Todos los principios, normas, acciones del programa y el recurso M-01 se formulan como propuesta de diseño para Logisticfy, sin asumir que existan controles implantados o verificados de antemano cuando la documentación del caso no lo especifica. La verificación efectiva del cumplimiento se reserva a fases posteriores según el propio encargo.

### 4.3. Autoría y revisiones

- Decisiones propias y revisiones: Se ha optado por una propuesta proporcionada al tamaño y actividad real de Logisticfy (20 personas, 80–120 expediciones diarias, 25 clientes y 3 transportistas), evitando medidas desproporcionadas o controles ficticios no respaldados por el caso, y asegurando la coherencia entre el análisis (1.1), los principios (1.2), la normativa (1.3), el programa (2.1–2.3) y el material terminado M-01 (3.1–3.2).
- Apoyo de IA: Asistencia de inteligencia artificial para revisar y ajustar el contenido a los criterios de la rúbrica y a la plantilla proporcionada.

