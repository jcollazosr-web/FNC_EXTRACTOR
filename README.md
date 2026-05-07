# 🏥 Clinical Extractor Pro v15

> Extracción automática de información clínica con inteligencia artificial  
> Cumple **Ley 1581 de Colombia** · Estándares **HIPAA** · Integración Salesforce & Google Sheets

---

## 📋 Tabla de contenido

1. [¿Qué es esta aplicación?](#1-qué-es-esta-aplicación)
2. [Cómo ingresar](#2-cómo-ingresar)
3. [Roles y permisos](#3-roles-y-permisos)
4. [Páginas de la aplicación](#4-páginas-de-la-aplicación)
5. [Subir y procesar documentos](#5-subir-y-procesar-documentos)
6. [Ver y gestionar resultados](#6-ver-y-gestionar-resultados)
7. [Revisión manual](#7-revisión-manual)
8. [Control de duplicados](#8-control-de-duplicados)
9. [Panel de calidad](#9-panel-de-calidad)
10. [Configuración del sistema](#10-configuración-del-sistema)
11. [Integración con Salesforce](#11-integración-con-salesforce)
12. [Cola de procesamiento](#12-cola-de-procesamiento)
13. [Seguridad y privacidad](#13-seguridad-y-privacidad)
14. [Preguntas frecuentes](#14-preguntas-frecuentes)
15. [Soporte y contacto](#15-soporte-y-contacto)

---

## 1. ¿Qué es esta aplicación?

**Clinical Extractor Pro** es una herramienta diseñada para el sector salud que extrae automáticamente información clínica relevante de documentos médicos (historias clínicas, órdenes médicas, epicrisis, etc.) usando inteligencia artificial.

En lugar de leer manualmente cada documento para buscar datos como diagnósticos, medicamentos o signos vitales, la aplicación lo hace en segundos y organiza esa información en una tabla lista para consultar, exportar o cargar a sistemas como Salesforce o Google Sheets.

> 🔒 **Cumplimiento legal:** la aplicación está diseñada bajo los estándares de la Ley 1581 de Colombia (protección de datos personales) y cuenta con cifrado, control de accesos y registro de auditoría.

---

## 2. Cómo ingresar

El administrador del sistema le entregará:

- 🌐 **La dirección web** (URL) donde está instalada la aplicación
- 📧 **Su usuario** (correo electrónico)
- 🔑 **Su contraseña** temporal

Al ingresar por primera vez se recomienda cambiar la contraseña desde el menú de perfil.

> ⚠️ **Seguridad:** tras 5 intentos fallidos de contraseña, el acceso se bloquea por 15 minutos. Si queda bloqueado, contacte al administrador.

---

## 3. Roles y permisos

Existen tres tipos de usuario. El administrador asigna el rol a cada persona:

| Función | 👑 Administrador | ✏️ Editor | 👁️ Lector |
|---|:---:|:---:|:---:|
| Extraer documentos | ✅ | ✅ | ❌ |
| Ver resultados | ✅ | ✅ | ✅ |
| Editar resultados | ✅ | ✅ | ❌ |
| Exportar datos | ✅ | ✅ | ❌ |
| Modificar configuración | ✅ | ❌ | ❌ |
| Gestionar usuarios | ✅ | ❌ | ❌ |
| Ver registro de auditoría | ✅ | ❌ | ❌ |

- **👑 Administrador:** control total del sistema. Configura llaves de API, integraciones y gestiona usuarios.
- **✏️ Editor:** puede subir documentos, extraer información, editar y exportar resultados.
- **👁️ Lector:** solo puede consultar los resultados ya procesados. No puede modificar nada.

---

## 4. Páginas de la aplicación

La aplicación tiene 7 secciones accesibles desde el menú lateral izquierdo:

| Sección | Para qué sirve |
|---|---|
| 📤 Subir documentos | Cargar archivos PDF o imágenes para extraer información clínica |
| 📊 Resultados | Ver y editar los datos extraídos de los documentos procesados |
| ✏️ Revisión manual | Corregir campos con baja confianza o incoherencias clínicas detectadas |
| 🔁 Duplicados | Identificar documentos que ya fueron procesados anteriormente |
| 📈 Calidad | Métricas de confianza, tendencias y campos con más errores |
| ☁️ Salesforce | Extraer información directamente desde registros de Salesforce |
| ⚙️ Configuración | Ver (o modificar si es admin) las opciones del sistema |

---

## 5. Subir y procesar documentos

### Formatos aceptados

- PDF (texto nativo o escaneado)
- Imágenes: JPG, PNG, TIFF
- Documentos de texto de Salesforce (sin necesidad de archivo)

### Pasos para procesar un documento

1. Haga clic en **📤 Subir documentos** en el menú lateral.
2. Arrastre el archivo al área indicada o haga clic en **Examinar** para seleccionarlo.
3. Espere mientras la aplicación extrae el texto (puede tomar unos segundos si el PDF está escaneado).
4. Revise los campos extraídos en la tabla de resultados.
5. Si algún campo muestra baja confianza (marcado en amarillo o rojo), vaya a **✏️ Revisión manual**.

> 📷 **Documentos escaneados:** si el PDF es una fotografía del papel (no texto digital), la aplicación usa OCR (reconocimiento óptico de caracteres) para leer el contenido. La precisión depende de la calidad de la imagen. Se recomienda al menos 300 DPI.

### Procesamiento de múltiples documentos

Puede subir varios archivos a la vez. La aplicación los procesa en paralelo y muestra el progreso en pantalla. Al finalizar, todos quedan disponibles en la sección de Resultados.

---

## 6. Ver y gestionar resultados

En la sección **📊 Resultados** encontrará una tabla con todos los documentos procesados y los campos extraídos (diagnóstico, medicamentos, signos vitales, etc.).

### Indicadores de confianza

Cada campo tiene un nivel de confianza que indica qué tan segura está la inteligencia artificial de haber extraído correctamente el dato:

| Indicador | Significado |
|---|---|
| 🟢 Verde (≥ 75%) | Extracción confiable. Revisión opcional. |
| 🟡 Amarillo (50–74%) | Confianza media. Se recomienda revisar. |
| 🔴 Rojo (< 50%) | Confianza baja. Requiere revisión manual obligatoria. |

### Exportar resultados

Los usuarios con rol **Editor** o **Administrador** pueden exportar los resultados en cuatro formatos:

- **CSV** — para abrir en Excel o importar a otros sistemas
- **Excel (.xlsx)** — con formato listo para compartir
- **FHIR R4** — estándar internacional para interoperabilidad clínica
- **JSON** — para integración con otros sistemas de información

---

## 7. Revisión manual

La sección **✏️ Revisión manual** muestra los campos que necesitan atención:

- **Campos con baja confianza:** el sistema no está seguro del valor extraído
- **Incoherencias clínicas:** por ejemplo, un diagnóstico de embarazo en un paciente masculino, o un medicamento incompatible con el diagnóstico
- **Fragmento del documento:** puede ver el texto original del que se extrajo cada dato para verificarlo

Para corregir un campo, haga clic sobre él, escriba el valor correcto y confirme. El cambio queda registrado en el historial.

> ✅ **Importante:** las correcciones manuales quedan guardadas y sirven para mejorar la calidad de las extracciones futuras en documentos similares.

---

## 8. Control de duplicados

La aplicación detecta automáticamente cuando intenta procesar un documento que ya fue analizado anteriormente. Esto evita datos duplicados en los reportes.

En la sección **🔁 Duplicados** puede:

- Ver la lista de archivos que fueron omitidos por estar duplicados
- Consultar cuándo se procesó el original y desde qué proyecto
- **Forzar re-procesamiento** si necesita actualizar los datos de un documento
- Exportar el reporte de duplicados

---

## 9. Panel de calidad

La sección **📈 Calidad** muestra métricas acumuladas sobre el rendimiento de la extracción:

- **Confianza promedio:** qué tan bien está extrayendo la IA en general
- **Tendencia histórica:** gráfica de evolución a lo largo del tiempo
- **Campos con más conflictos:** cuáles datos se extraen con mayor dificultad
- **Tasa de error OCR:** calidad del reconocimiento de texto en documentos escaneados

Esta información ayuda al administrador a ajustar la configuración para mejorar los resultados.

---

## 10. Configuración del sistema

> 🔒 **Solo el Administrador puede modificar la configuración.** Los demás usuarios pueden verla en modo lectura pero no hacer cambios.

La configuración está dividida en secciones:

| Sección | Qué configura |
|---|---|
| 🤖 Modelo de IA | Proveedor (Claude o GPT-4o), llave de API, modelo específico, tokens máximos y umbral de confianza |
| 📋 Plantilla de extracción | Qué campos extraer según el tipo de consulta médica (urgencias, control, hospitalización, etc.) |
| 🔬 OCR | Idioma del documento, resolución de imagen, uso de EasyOCR o visión directa del modelo |
| 📊 Google Sheets | URL del spreadsheet para sincronización automática de resultados |
| ☁️ Salesforce | Credenciales y consultas SOQL para extracción desde Salesforce |
| ⚡ Procesamiento | Número de documentos que se procesan simultáneamente |
| 🔬 Robustez científica | Anonimización de datos, validación cruzada entre modelos, umbral de calidad OCR |

### Guardar la configuración

Al hacer cambios, el Administrador debe presionar el botón **💾 Guardar configuración en disco** para que los cambios persistan al reiniciar la aplicación. Si no guarda, los cambios solo duran hasta cerrar sesión.

---

## 11. Integración con Salesforce

Si su institución usa Salesforce, puede extraer información clínica directamente desde registros del CRM sin necesidad de descargar archivos.

1. Active la integración en **⚙️ Configuración → Salesforce** (solo Administrador).
2. Ingrese las credenciales de Salesforce: usuario, contraseña y Security Token.
3. Escriba la consulta SOQL para seleccionar los registros a procesar.
4. Haga clic en **Conectar Salesforce** y verifique que la conexión sea exitosa.
5. En la sección **☁️ Salesforce**, seleccione los registros y ejecute la extracción.

> 💡 **Modo incremental:** active esta opción para procesar solo los registros nuevos desde la última ejecución, evitando reprocesar documentos ya analizados.

---

## 12. Cola de procesamiento

Para documentos o lotes grandes, la aplicación cuenta con una cola de procesamiento persistente:

- Puede enviar documentos a la cola y cerrar sesión sin que se pierda el trabajo
- Cada tarea tiene un estado: `pendiente` → `procesando` → `completado` → `fallido`
- Los errores se reintentan automáticamente
- Puede ver el estado de todas las tareas en tiempo real

---

## 13. Seguridad y privacidad

### Protección de datos clínicos

- Toda la información clínica se almacena **cifrada con AES-256** en la base de datos local
- Las comunicaciones con la IA se realizan por canales seguros (HTTPS)
- No se almacenan datos de pacientes en servidores de terceros más allá de lo necesario para la extracción

### Anonimización

Si el Administrador activa el modo de **Anonimización**, la aplicación elimina automáticamente nombres, números de documento y otra información personal identificable (PII) antes de almacenar los resultados. En su lugar, genera un ID anónimo único por paciente para permitir seguimiento longitudinal sin exponer datos personales.

### Registro de auditoría

Todas las acciones quedan registradas automáticamente: quién accedió, qué hizo, desde qué IP y a qué hora. Este registro es **inmutable** — ni el Administrador puede borrarlo — y permite cumplir con los requisitos de la Ley 1581 de Colombia en caso de auditorías externas.

> ⚠️ Si nota actividad sospechosa (accesos en horarios inusuales, exportaciones no autorizadas), notifique inmediatamente al Administrador para que revise el registro de auditoría.

---

## 14. Preguntas frecuentes

**¿Por qué algunos campos aparecen en rojo?**  
La IA no pudo extraer ese dato con suficiente confianza. Debe revisarlo y corregirlo manualmente en la sección de Revisión manual.

**¿Qué pasa si subo el mismo documento dos veces?**  
La aplicación lo detecta como duplicado y lo omite. Puede verlo en la sección Duplicados y forzar re-procesamiento si lo necesita.

**¿Los datos se guardan si cierro sesión?**  
Sí. Los resultados se guardan en la base de datos local. Solo la configuración no guardada (sin presionar el botón de guardar) se pierde.

**¿Puedo usar la aplicación desde mi celular?**  
Sí, la interfaz es responsiva. Sin embargo, para cargar documentos se recomienda usar un computador.

**¿Qué hago si la extracción es muy imprecisa en un documento?**  
Verifique que el PDF tenga buena calidad. Si está escaneado, asegúrese de que la imagen sea nítida. El Administrador puede aumentar la resolución DPI en la configuración.

**¿Cómo cambio mi contraseña?**  
El Administrador puede cambiar contraseñas desde el panel de administración. Contacte al administrador del sistema.

**¿Qué es FHIR R4?**  
Es un estándar internacional de interoperabilidad en salud que permite compartir información clínica entre diferentes sistemas hospitalarios de forma estructurada.

---

## 15. Soporte y contacto

Para problemas técnicos o preguntas sobre el uso de la aplicación, contacte al administrador del sistema de su institución.

> 🔐 **Nunca comparta su contraseña con nadie**, incluido el personal de soporte técnico. Un soporte legítimo nunca le pedirá su contraseña.

---

*Clinical Extractor Pro v15 · Cumple Ley 1581 Colombia · Estándares HIPAA*
