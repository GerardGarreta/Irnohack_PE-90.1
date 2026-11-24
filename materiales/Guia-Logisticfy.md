# Guía Logisticfy · `M-01`

### Detectar correos sospechosos y verificar cambios en envíos y facturación

* **Código del material:** `M-01`
* **Objetivo y acción vinculados:** Objetivo **O-01** (con apoyo a **O-02** y **O-04**) · Acción **A-01**
* **Destinatarios principales:** Operaciones, Atención al Cliente, Comercial y Administración *(extensible a toda la plantilla, incluida la persona en prácticas)*
* **Normativa de referencia:** Normas **N-01**, **N-04**, **N-05** y **N-07** · Principios **P-01**, **P-03**, **P-05** y **P-06**
* **Recurso interactivo complementario:** [`../programa/IG-Concienciacion.py`](../programa/IG-Concienciacion.py)



### ¿Por qué es clave en Logisticfy?

En el trabajo diario gestionamos entre **80 y 120 expediciones diarias** para unos **25 clientes empresariales**, coordinándonos con **3 transportistas externos** y compartiendo información de expediciones, contactos, destinatarios, incidencias y facturación entre áreas.

Muchos intentos de engaño (*phishing* o suplantación) aprovechan precisamente ese ritmo operativo: aparentan proceder de un cliente, de un transportista o de una persona de la empresa y piden actuar con rapidez o facilitar datos y accesos.



### 1. Cinco señales de alerta frecuentes (`COM-01` y `EXT-01`)

1. **Urgencia artificial o presión:** Mensajes que exigen responder o cambiar algo de inmediato (*"Urgente: bloqueamos la entrega si no confirmas hoy"*, *"Revisa esta factura/incidencia antes de las 12:00"*).
2. **Cambios sensibles inesperados:** Nuevas cuentas bancarias para cobros o pagos, modificaciones de dirección de entrega o facturación no tramitadas por el cauce habitual, o solicitudes de listados amplios de clientes, destinatarios o expediciones.
3. **Remitente engañoso:** Direcciones similares a las habituales pero con pequeñas alteraciones (letras cambiadas, dominios distintos o un nombre visible que no coincide con la dirección real del correo).
4. **Enlaces o adjuntos poco claros:** Enlaces que llevan a páginas externas de inicio de sesión o archivos comprimidos/documentos inesperados asociados a una supuesta incidencia o envío.
5. **Desfase con la operativa real:** Referencias a una expedición, incidencia, cliente o transportista que no coinciden con lo registrado en la plataforma (`SW-01`) o con el trabajo del área.



### 2. Regla de oro antes de actuar (`N-04` y `N-05`)

> **Si hay duda o el mensaje pide algo sensible, no respondas facilitando información, no abras enlaces sospechosos ni introduzcas credenciales en ellos, y no apliques el cambio a ciegas.**

* **1. Comprueba en la operativa:** Revisa si la solicitud, el estado de la expedición o la incidencia encajan con la información disponible en la plataforma (`SW-01`).
* **2. Verifica por un canal fiable:** Confirma los cambios sensibles (cuentas, direcciones, datos de facturación o peticiones inusuales) con el contacto habitual o con la persona responsable correspondiente a través de un medio conocido y de confianza (no respondas directamente sobre un mensaje dudoso si sospechas suplantación).
* **3. Protege los datos:** Trata la información de clientes, contactos, destinatarios, expediciones, incidencias y facturación (`DAT-01`) solo para fines del servicio, evitando exportaciones o envíos a direcciones externas no verificadas (`N-04`).



### 3. Qué hacer ante una sospecha o incidencia (`N-01`, `N-06` y `N-07`)

* **No lo reenvíes masivamente** ni borres las pruebas básicas (como el correo o mensaje sospechoso) si puedes evitarlo.
* **Avisa de inmediato** al contacto designado de **Tecnología/IT** y a tu responsable directo, indicando qué has observado, a qué hora y qué sistema o dato podría verse afectado.
* **Actúa sin demora si ya hubo interacción:** Si abriste un enlace extraño, descargaste un archivo sospechoso o compartiste datos o credenciales (`IAM-01`), notifícalo enseguida para que pueda revisarse (`MON-01`) y contenerse cuanto antes.
* **Cuida tu puesto y sesión:** Utiliza siempre tu cuenta personal, bloquea tu equipo (`HW-01`) al ausentarte y mantén el orden en tu espacio de trabajo (`PHY-01`).



### 4. Uso en el taller práctico (`A-01`)

Durante la acción **A-01**, esta guía se utiliza como hoja de consulta rápida junto con el programa interactivo:

```bash
python3 programa/IG-Concienciacion.py
```
