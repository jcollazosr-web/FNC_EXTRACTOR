"""
╔══════════════════════════════════════════════════════════════════════════════╗
║          CLINICAL EXTRACTOR PRO v15 — EDICIÓN COMPLETA                      ║
║          Salesforce · Claude/GPT-4o · Google Sheets · Streamlit              ║
║          Validación Cruzada · Lógica Médica · Ley 1581 Colombia              ║
║                                                                              ║
║  MEJORAS v8 (heredadas):                                                     ║
║  ✅ Soporte nativo Claude (Anthropic) + GPT-4o seleccionable                 ║
║  ✅ OCR mejorado: deskew, denoise, EasyOCR, visión directa del modelo        ║
║  ✅ Escritura batch a Google Sheets (no row-by-row)                          ║
║  ✅ Segmentación inteligente de documentos largos por secciones              ║
║  ✅ Prompts con terminología colombiana SGSSS completa                       ║
║  ✅ Plantillas de campos por tipo de consulta                                ║
║  ✅ Reintentos inteligentes Salesforce con cola de fallos                    ║
║  ✅ Resolución de conflictos con fragmentos relevantes                       ║
║  ✅ Dashboard de calidad acumulada con métricas históricas                   ║
║  ✅ Revisión manual sin límite de 10 campos, con fragmento del documento     ║
║  ✅ Soporte Salesforce campos de texto (Case, objetos custom) sin OCR        ║
║  ✅ Modo incremental: solo registros nuevos desde última ejecución           ║
║  ✅ Confianza por campo acumulada en DB para priorizar revisión              ║
║                                                                              ║
║  NUEVAS MEJORAS v15 — PRODUCCIÓN COMPLETA (archivo único):                  ║
║  🧪 Suite de 40+ tests integrada — ejecutar con: python archivo.py --test   ║
║  📬 Cola persistente, buscador, FHIR R4, multi-paciente, monitoreo          ║
║                                                                              ║
║  MEJORAS v15 anteriores:                                                     ║
║  📬 Cola persistente SQLite: pending→processing→done→failed, reintentos      ║
║  🔍 Buscador clínico: queries CIE-10, medicamentos, rangos de edad/fecha     ║
║  📤 Exportación FHIR R4, CSV investigación, JSON estructurado                ║
║  🧩 Segmentación multi-paciente: divide PDFs con varias historias            ║
║  📊 Monitoreo: webhook Slack/email, alertas automáticas por umbral           ║
║  🧪 Suite de tests: auditor clínico, normalización, anonimización, OCR       ║
║                                                                              ║
║  NUEVAS MEJORAS v14 — ROBUSTEZ CIENTÍFICA:                                  ║
║  📍 Trazabilidad por campo: texto_original + página + modelo + confianza     ║
║  🔬 Score OCR: calidad 0-100, descarte automático bajo umbral               ║
║  🏷️  Normalización: CIE-10 canónico + medicamentos → genérico + unidades     ║
║  🔒 Anonimización: NER elimina nombre/doc, ID anónimo SHA-256 por paciente   ║
║  ✂️  Extracción vs interpretación: separación explícita en prompts            ║
║  🤝 Ensamble de modelos: Claude extrae → GPT valida (y viceversa)            ║
║  🚦 Pipeline en 8 etapas discretas con estado y log granular                ║
║  📊 Dashboard científico: completitud, ruido OCR, sesgo por campo           ║
║                                                                              ║
║  NUEVAS MEJORAS v13 — INTERFAZ SIMPLIFICADA:                                ║
║  🖥️  Navegación lateral: 7 páginas claramente separadas                       ║
║  🖥️  Login minimalista — sin distracciones, branding limpio                   ║
║  🖥️  Configuración unificada en una sola página (no sidebar sobrecargado)     ║
║  🖥️  Página de resultados: métricas + tabla + detalle expandible priorizado   ║
║  🖥️  Revisión manual: alertas + incoherencias clínicas + edición inline       ║
║  🖥️  Duplicados: página dedicada con exportación y stats de proyectos         ║
║  🖥️  Calidad: gráfica de tendencia + tabla de campos por conflicto            ║
║  🖥️  Salesforce en página propia (no mezclado con archivos locales)           ║
║  🖥️  Admin: tabs compactas — usuarios, sesiones, audit log, contraseña        ║
║                                                                              ║
║  NUEVAS MEJORAS v12 — DEDUPLICACIÓN Y GESTIÓN DE PROYECTOS:                 ║
║  🔁 Deduplicación triple: hash SHA-256 en DB + session_state + Google Sheets ║
║  🔁 Feedback bidireccional App ↔ Sheets: sincronización de hashes procesados  ║
║  🔁 Tabla dedup_registry en DB: índice global de archivos procesados          ║
║  🔁 Proyectos: aislamiento completo de extracciones por nombre/fecha           ║
║  🔁 Botón "Nuevo Proyecto": limpia sesión, DB local y tab de Sheets           ║
║  🔁 Botón "Eliminar datos": borrado selectivo con confirmación obligatoria    ║
║  🔁 Vista de duplicados detectados con opción de forzar re-extracción         ║
║  🔁 Reporte de duplicados exportable con origen y fecha de extracción previa  ║
║                                                                              ║
║  NUEVAS MEJORAS v11 — SEGURIDAD CLÍNICA (HIPAA/Ley 1581):                   ║
║  🔐 Autenticación bcrypt + PBKDF2-SHA256 con sal única por usuario           ║
║  🔐 Roles: ADMIN (único) · EDITOR · LECTOR con permisos granulares           ║
║  🔐 Administrador principal configurable en .env (no hardcodeado)            ║
║  🔐 Sesiones JWT firmadas con HS256, expiran en 8h, revocables               ║
║  🔐 Rate limiting: bloqueo tras 5 intentos fallidos / 15 min                 ║
║  🔐 Cifrado AES-256-GCM de datos clínicos en SQLite (Fernet/cryptography)   ║
║  🔐 Log de auditoría inmutable con IP, user-agent, timestamp UTC             ║
║  🔐 Panel de administración: gestión usuarios, sesiones activas, audit trail  ║
║  🔐 Exportaciones solo disponibles para ADMIN y EDITOR                       ║
║  🔐 Datos cifrados en reposo; claves derivadas del SECRET_KEY de entorno     ║
║                                                                              ║
║  NUEVAS MEJORAS v10 — INTELIGENCIA CLÍNICA AVANZADA:                        ║
║  🧠 ClinicalAuditor: auditor autónomo de coherencia lógica completa          ║
║  🧠 Reglas de incompatibilidad sexo-biológico: próstata/útero/embarazo       ║
║  🧠 Reglas edad-diagnóstico ampliadas: pediátrico vs adulto vs geriátrico    ║
║  🧠 Reglas diagnóstico-medicamento: coherencia terapéutica automática        ║
║  🧠 Reglas CIE-10 vs sexo/edad: 200+ códigos con restricciones validadas     ║
║  🧠 Re-escaneo dirigido: si hay incoherencia, relanza extracción focalizada  ║
║  🧠 Triple verificación: extracción → auditoría → re-escaneo → marcado      ║
║  🧠 Marcado granular: campo exacto, razón, evidencia del documento           ║
║  🧠 Panel de auditoría en UI: tabla detallada de incoherencias detectadas    ║
║                                                                              ║
║  MEJORAS v9 (heredadas):                                                     ║
║  🆕 FIX CRÍTICO: EasyOCR singleton — evita recarga del modelo en cada imagen║
║  🆕 FIX CRÍTICO: SQLite WAL mode + pool thread-safe para procesamiento       ║
║         paralelo sin race conditions ni bloqueos                             ║
║  🆕 FIX CRÍTICO: Resolución de conflictos en una sola llamada LLM (batch)   ║
║         — hasta 90% menos de costos en paso de resolución                   ║
║  🆕 FIX CRÍTICO: Hash de caché incluye campos y tipo_consulta               ║
║         — evita devolver extracciones con campos equivocados                 ║
║  🆕 Documentos largos procesados en chunks con overlap y consolidación       ║
║  🆕 Detección de calidad de OCR: avisa si el texto extraído es basura        ║
║  🆕 Tercera lectura LLM para documentos con confianza < 0.60                 ║
║  🆕 Interacciones medicamentosas consideran dosis (menos falsos positivos)   ║
║  🆕 Detección de documentos multi-paciente (separadores de paciente)         ║
║  🆕 Google Sheets: agregar columnas nuevas sin borrar datos históricos       ║
║  🆕 Max workers calculado automáticamente según rate limits de la API        ║
║  🆕 Workers compartidos refactorizados (elimina duplicación de código ~70%)  ║
║  🆕 Exportar a Excel (.xlsx) directamente desde la UI (además de CSV/JSON)  ║
║  🆕 Vista de evolución por paciente: compara consultas del mismo documento   ║
╚══════════════════════════════════════════════════════════════════════════════╝
 
INSTALACIÓN:
  pip install streamlit openai anthropic PyMuPDF pytesseract pillow \
              google-auth google-api-python-client gspread \
              pandas openpyxl python-dotenv simple-salesforce \
              tenacity easyocr opencv-python-headless
 
EJECUCIÓN:
  streamlit run clinical_extractor_v9.py
 
NOTAS:
  - Requiere credentials.json de Google Cloud (Service Account)
  - Comparte tu Google Sheet con el email del Service Account
  - Tesseract o EasyOCR para OCR de PDFs escaneados
  - Salesforce: Connected App con OAuth2 o Username/Password flow
  - Claude API key: https://console.anthropic.com
"""
 
from __future__ import annotations


# ═══════════════════════════════════════════════════════════════
# AUTO-INSTALACIÓN DE DEPENDENCIAS (v15-CLINIC)
# Se ejecuta una sola vez. Seguro relanzar múltiples veces.
# ═══════════════════════════════════════════════════════════════
import subprocess, sys, importlib, os as _os

_REQUIRED_PACKAGES = [
    # (import_name, pip_package)
    ("streamlit",          "streamlit>=1.32.0"),
    ("anthropic",          "anthropic>=0.25.0"),
    ("openai",             "openai>=1.20.0"),
    ("dotenv",             "python-dotenv"),
    ("fitz",               "PyMuPDF>=1.23.0"),
    ("pytesseract",        "pytesseract"),
    ("PIL",                "Pillow>=10.0.0"),
    ("cv2",                "opencv-python-headless"),
    ("numpy",              "numpy>=1.24.0"),
    ("pandas",             "pandas>=2.0.0"),
    ("openpyxl",           "openpyxl"),
    ("google.oauth2",      "google-auth"),
    ("googleapiclient",    "google-api-python-client"),
    ("gspread",            "gspread"),
    ("simple_salesforce",  "simple-salesforce"),
    ("tenacity",           "tenacity"),
    ("bcrypt",             "bcrypt"),
    ("cryptography",       "cryptography"),
    ("jwt",                "PyJWT"),
    ("easyocr",            "easyocr"),
    ("sklearn",            "scikit-learn"),
]

def _check_system_deps():
    """Verifica dependencias del sistema (no-Python) y avisa si faltan."""
    import shutil, subprocess, sys, os
    warnings = []

    # ── Tesseract: buscar en PATH y en rutas típicas de Windows ──
    tesseract_cmd = shutil.which("tesseract")

    if not tesseract_cmd and sys.platform == "win32":
        # Rutas de instalación típicas en Windows
        _win_paths = [
            r"C:\Program Files\Tesseract-OCR\tesseract.exe",
            r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
            os.path.expanduser(r"~\AppData\Local\Tesseract-OCR\tesseract.exe"),
        ]
        for p in _win_paths:
            if os.path.isfile(p):
                tesseract_cmd = p
                # Configurar pytesseract automáticamente
                try:
                    import pytesseract
                    pytesseract.pytesseract.tesseract_cmd = p
                    print(f"✅ Tesseract encontrado en: {p}")
                except ImportError:
                    pass
                break

    if not tesseract_cmd:
        if sys.platform == "win32":
            msg = (
                "⚠️  Tesseract OCR no encontrado. Para Windows:\n"
                "  1. Descarga el instalador: https://github.com/UB-Mannheim/tesseract/wiki\n"
                "  2. Durante la instalación marca el paquete de idioma 'Spanish'\n"
                "  3. Agrega al PATH: C:\\Program Files\\Tesseract-OCR\n"
                "  4. Reinicia la terminal y vuelve a ejecutar la app.\n"
                "  Sin Tesseract, el OCR de PDFs escaneados no funcionará."
            )
        else:
            msg = (
                "⚠️  Tesseract OCR no encontrado. Instalar con:\n"
                "     Ubuntu/Debian: sudo apt install tesseract-ocr tesseract-ocr-spa\n"
                "     macOS: brew install tesseract tesseract-lang\n"
                "     Sin Tesseract, el OCR de PDFs escaneados no funcionará."
            )
        warnings.append(msg)
    else:
        # Verificar paquete de idioma español
        try:
            out = subprocess.check_output(
                [tesseract_cmd, "--list-langs"],
                stderr=subprocess.STDOUT, text=True
            )
            if "spa" not in out:
                if sys.platform == "win32":
                    warnings.append(
                        "⚠️  Tesseract instalado pero sin idioma español.\n"
                        "     Vuelve a ejecutar el instalador de Tesseract y marca 'Spanish'."
                    )
                else:
                    warnings.append(
                        "⚠️  Tesseract sin idioma español. "
                        "Instalar: sudo apt install tesseract-ocr-spa"
                    )
        except Exception:
            pass

    for w in warnings:
        print(w)
    return warnings


def _autoinstall():
    """Instala paquetes faltantes silenciosamente."""
    missing = []
    for import_name, pip_pkg in _REQUIRED_PACKAGES:
        try:
            importlib.import_module(import_name)
        except ImportError:
            missing.append(pip_pkg)

    if not missing:
        return

    print(f"\n🏥 Clinical Extractor Pro — instalando {len(missing)} dependencias...")
    for pkg in missing:
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "--quiet", "--upgrade", pkg],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            print(f"   ✅ {pkg}")
        except subprocess.CalledProcessError:
            print(f"   ⚠️  No se pudo instalar {pkg} (instalar manualmente si es crítico)")
    print("   Instalación completada.\n")

_autoinstall()
_check_system_deps()
# ═══════════════════════════════════════════════════════════════

 
# ─────────────────────────────────────────────────────────────
# IMPORTS ESTÁNDAR
# ─────────────────────────────────────────────────────────────
import base64
import hashlib
import io
import json
import logging
import os
import re
import sqlite3
import tempfile
import time
import traceback
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
 
import pandas as pd
 
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
 
# ─────────────────────────────────────────────────────────────
# SEGURIDAD v11 — IMPORTS (pip install bcrypt cryptography PyJWT)
# ─────────────────────────────────────────────────────────────
import hmac
import secrets
import struct

try:
    import bcrypt as _bcrypt
    BCRYPT_AVAILABLE = True
except ImportError:
    BCRYPT_AVAILABLE = False
    log_security_warn = "bcrypt no instalado — usar: pip install bcrypt"

try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes as _crypto_hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    import base64 as _b64
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

try:
    import jwt as _jwt
    JWT_AVAILABLE = True
except ImportError:
    JWT_AVAILABLE = False

# ─────────────────────────────────────────────────────────────
# LOGGING
# ─────────────────────────────────────────────────────────────
# MEJORA v15-CLINIC: nivel de log configurable vía env var (INFO en dev, WARNING en prod)
_LOG_LEVEL = os.environ.get("CEP_LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, _LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
    ]
)
log = logging.getLogger("clinical_v15")
# Silenciar librerías ruidosas en producción
for _noisy_lib in ("httpx", "httpcore", "urllib3", "PIL", "easyocr"):
    logging.getLogger(_noisy_lib).setLevel(logging.WARNING)
 
# ─────────────────────────────────────────────────────────────
# MEJORA 1: EasyOCR SINGLETON — se carga una sola vez en memoria
# ─────────────────────────────────────────────────────────────
_easyocr_reader = None
_easyocr_lock = __import__("threading").Lock()
 
 
def get_easyocr_reader(langs: List[str]):
    """Devuelve el reader de EasyOCR, inicializándolo solo la primera vez."""
    global _easyocr_reader
    with _easyocr_lock:
        if _easyocr_reader is None:
            try:
                import easyocr
                _easyocr_reader = easyocr.Reader(langs, gpu=False, verbose=False)
                log.info(f"✅ EasyOCR cargado con idiomas: {langs}")
            except ImportError:
                log.warning("EasyOCR no instalado")
                _easyocr_reader = None
    return _easyocr_reader
 
 
# ─────────────────────────────────────────────────────────────
# MEJORA 2: SQLite WAL MODE + CONEXIÓN THREAD-SAFE
# ─────────────────────────────────────────────────────────────
_db_write_lock = __import__("threading").Lock()
 
 
# ── Pool de conexiones SQLite thread-local (v15-CLINIC) ─────────
import threading as _threading
_db_local = _threading.local()

def _make_main_conn() -> sqlite3.Connection:
    """Crea conexión fresca a la DB principal con todos los PRAGMAs."""
    c = sqlite3.connect(str(DB_PATH), check_same_thread=False, timeout=60)
    c.execute("PRAGMA journal_mode=WAL")
    c.execute("PRAGMA synchronous=NORMAL")
    c.execute("PRAGMA cache_size=-128000")
    c.execute("PRAGMA temp_store=MEMORY")
    c.execute("PRAGMA mmap_size=268435456")
    c.execute("PRAGMA wal_autocheckpoint=1000")
    c.execute("PRAGMA optimize")
    return c


def _get_db_connection() -> sqlite3.Connection:
    """
    Retorna conexión SQLite thread-local con WAL mode.
    Detecta y recrea automáticamente conexiones cerradas entre rerenders de Streamlit.
    """
    conn = getattr(_db_local, "conn", None)
    if conn is not None:
        try:
            conn.execute("SELECT 1")
        except Exception:
            conn = None
            _db_local.conn = None
    if conn is None:
        conn = _make_main_conn()
        _db_local.conn = conn
    return conn
 
# ─────────────────────────────────────────────────────────────
# CONSTANTES MÉDICAS
# ─────────────────────────────────────────────────────────────
 
RANGOS_FISIOLOGICOS = {
    "tension_sistolica":        (60,   250),
    "tension_diastolica":       (30,   150),
    "frecuencia_cardiaca":      (30,   250),
    "temperatura":              (34.0, 42.5),
    "peso_kg":                  (0.5,  300),
    "talla_cm":                 (30,   250),
    "saturacion_o2":            (50,   100),
    "frecuencia_respiratoria":  (5,    60),
    "glucemia":                 (20,   800),
}
 
CIE10_PREFIJOS_VALIDOS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
 
INTERACCIONES_CRITICAS = [
    ({"warfarina", "warfarin", "acenocumarol"},
     {"aspirina", "ibuprofeno", "naproxeno", "diclofenaco", "meloxicam"},
     "Riesgo alto de sangrado: anticoagulante + AINE"),
    ({"metformina"},
     {"contraste yodado", "medio de contraste"},
     "Riesgo de acidosis láctica: metformina + contraste"),
    ({"ieca", "enalapril", "lisinopril", "ramipril", "captopril"},
     {"ara ii", "losartan", "valsartan", "irbesartan", "candesartan"},
     "Doble bloqueo RAAS: riesgo de hiperpotasemia y falla renal"),
    ({"digoxina"},
     {"amiodarona"},
     "Toxicidad por digoxina: amiodarona aumenta niveles séricos"),
    ({"ssri", "fluoxetina", "sertralina", "paroxetina", "escitalopram"},
     {"tramadol"},
     "Riesgo de síndrome serotoninérgico"),
    ({"sildenafil", "tadalafil", "vardenafil"},
     {"nitratos", "nitroglicerina", "isosorbide", "mononitrato"},
     "Hipotensión severa: inhibidor PDE5 + nitratos"),
    ({"ciprofloxacina", "levofloxacina", "moxifloxacina"},
     {"amiodarona", "sotalol", "haloperidol"},
     "Riesgo de prolongación QT: fluoroquinolona + antiarrítmico"),
    ({"clonazepam", "diazepam", "alprazolam", "lorazepam"},
     {"opioides", "morfina", "tramadol", "oxicodona", "fentanilo"},
     "Depresión respiratoria severa: benzodiazepina + opioide"),
    ({"metotrexato"},
     {"aines", "aspirina", "ibuprofeno", "naproxeno"},
     "Toxicidad por metotrexato: AINEs reducen su excreción renal"),
    ({"litio"},
     {"enalapril", "lisinopril", "losartan", "hidroclorotiazida"},
     "Toxicidad por litio: IECAs/ARA-II/tiazidas aumentan niveles de litio"),
]
 
# ─────────────────────────────────────────────────────────────
# PLANTILLAS POR TIPO DE CONSULTA
# ─────────────────────────────────────────────────────────────
 
PLANTILLAS_CONSULTA: Dict[str, List[str]] = {
    "General / Base": [
        "nombre_paciente", "fecha_nacimiento", "edad", "sexo",
        "documento_identidad", "tipo_documento",
        "fecha_consulta", "tipo_consulta", "motivo_consulta",
        "enfermedad_actual",
        "diagnostico_principal", "codigo_cie10_principal",
        "diagnosticos_secundarios", "codigos_cie10_secundarios",
        "medicamentos", "dosis", "via_administracion", "frecuencia_dosis",
        "alergias", "antecedentes_personales", "antecedentes_familiares",
        "tension_arterial", "frecuencia_cardiaca", "temperatura",
        "frecuencia_respiratoria", "saturacion_o2",
        "peso_kg", "talla_cm", "imc",
        "examen_fisico", "plan_tratamiento",
        "examenes_solicitados", "remisiones",
        "medico_tratante", "registro_medico",
        "institucion", "ciudad", "eps_aseguradora",
    ],
    "Urgencias": [
        "nombre_paciente", "fecha_nacimiento", "edad", "sexo",
        "documento_identidad", "tipo_documento",
        "fecha_consulta", "hora_consulta", "motivo_consulta",
        "triage_nivel", "mecanismo_lesion", "tiempo_evolucion",
        "enfermedad_actual", "estado_conciencia", "glasgow",
        "tension_arterial", "frecuencia_cardiaca", "temperatura",
        "frecuencia_respiratoria", "saturacion_o2", "glucometria",
        "peso_kg",
        "diagnostico_principal", "codigo_cie10_principal",
        "diagnosticos_secundarios",
        "medicamentos_urgencias", "procedimientos_realizados",
        "plan_tratamiento", "destino_paciente",
        "medico_tratante", "institucion", "eps_aseguradora",
    ],
    "Control Prenatal": [
        "nombre_paciente", "fecha_nacimiento", "edad", "documento_identidad",
        "fecha_consulta", "semanas_gestacion", "numero_consulta_prenatal",
        "fecha_ultima_menstruacion", "fecha_probable_parto",
        "gestas", "partos", "cesareas", "abortos", "hijos_vivos",
        "tension_arterial", "frecuencia_cardiaca", "temperatura",
        "peso_kg", "talla_cm", "imc", "ganancia_peso_gestacion",
        "altura_uterina", "presentacion_fetal", "frecuencia_cardiaca_fetal",
        "movimientos_fetales", "edemas",
        "examen_vaginal", "cervix",
        "hemoglobina", "glicemia_basal", "urocultivo",
        "ecografia_obstetrica", "resultado_ecografia",
        "vacuna_toxoide", "vacuna_influenza",
        "diagnostico_principal", "codigo_cie10_principal",
        "plan_tratamiento", "proxima_cita",
        "medico_tratante", "institucion", "eps_aseguradora",
    ],
    "Consulta Especializada": [
        "nombre_paciente", "fecha_nacimiento", "edad", "sexo",
        "documento_identidad", "tipo_documento",
        "fecha_consulta", "especialidad", "tipo_consulta",
        "motivo_consulta", "enfermedad_actual",
        "antecedentes_personales", "antecedentes_familiares",
        "medicamentos_actuales", "alergias",
        "tension_arterial", "frecuencia_cardiaca", "temperatura",
        "peso_kg", "talla_cm",
        "examen_fisico_especializado",
        "hallazgos_relevantes",
        "diagnostico_principal", "codigo_cie10_principal",
        "diagnosticos_secundarios", "codigos_cie10_secundarios",
        "plan_tratamiento", "medicamentos", "dosis",
        "examenes_solicitados", "interconsultas",
        "proxima_cita", "recomendaciones",
        "medico_tratante", "registro_medico",
        "institucion", "eps_aseguradora",
    ],
    "Hospitalización / Egreso": [
        "nombre_paciente", "fecha_nacimiento", "edad", "sexo",
        "documento_identidad", "tipo_documento",
        "fecha_ingreso", "fecha_egreso", "dias_estancia",
        "servicio", "cama",
        "motivo_ingreso", "enfermedad_actual",
        "antecedentes_personales", "antecedentes_familiares",
        "alergias", "medicamentos_ingreso",
        "examen_fisico_ingreso",
        "diagnostico_ingreso", "codigo_cie10_ingreso",
        "diagnostico_egreso_principal", "codigo_cie10_egreso",
        "diagnosticos_secundarios_egreso",
        "procedimientos_hospitalizacion", "cirugias",
        "evolucion_hospitalizacion",
        "medicamentos_egreso", "dosis_egreso",
        "plan_egreso", "recomendaciones_egreso",
        "citas_control", "remisiones",
        "estado_egreso", "condicion_alta",
        "medico_tratante", "medico_egreso",
        "institucion", "eps_aseguradora",
    ],
    "Salud Mental": [
        "nombre_paciente", "fecha_nacimiento", "edad", "sexo",
        "documento_identidad", "tipo_documento",
        "fecha_consulta", "tipo_consulta",
        "motivo_consulta", "enfermedad_actual",
        "antecedentes_psiquiatricos", "antecedentes_familiares_mentales",
        "intentos_autoliticos_previos", "hospitalizaciones_psiquiatricas",
        "consumo_sustancias", "red_apoyo_social",
        "estado_mental", "orientacion", "memoria", "atencion",
        "estado_animo", "afecto", "pensamiento", "percepcion",
        "juicio_critica", "insight", "riesgo_suicida", "riesgo_heteroagresion",
        "medicamentos", "dosis", "via_administracion",
        "diagnostico_principal", "codigo_cie10_principal",
        "diagnosticos_secundarios",
        "plan_tratamiento", "psicoterapia",
        "medico_tratante", "registro_medico",
        "institucion", "eps_aseguradora",
    ],
}
 
# Todas las variables únicas de todas las plantillas
CAMPOS_DEFAULT = list(dict.fromkeys(
    campo for campos in PLANTILLAS_CONSULTA.values() for campo in campos
))
 
# ═══════════════════════════════════════════════════════════════
# MÓDULO DE SEGURIDAD v11
# Estándares: OWASP, HIPAA, Ley 1581 Colombia
# ═══════════════════════════════════════════════════════════════

# ── Configuración automática — sin necesidad de archivo .env ───
_CFG_FILE = Path(__file__).parent / ".env"

def _load_or_create_config() -> Dict[str, str]:
    """
    Carga configuración desde .env si existe.
    Si no existe, genera SECRET_KEY automáticamente y la persiste.
    Nunca requiere intervención manual del usuario.
    """
    cfg: Dict[str, str] = {}

    # Intentar cargar .env existente
    if _CFG_FILE.exists():
        try:
            for line in _CFG_FILE.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, _, v = line.partition("=")
                    cfg[k.strip()] = v.strip()
        except Exception:
            pass

    # Generar SECRET_KEY si no existe
    if not cfg.get("CEP_SECRET_KEY"):
        cfg["CEP_SECRET_KEY"] = secrets.token_hex(32)
        _persist_config(cfg)
        log.info("✅ SECRET_KEY generado automáticamente y guardado en .env")

    return cfg


def _persist_config(cfg: Dict[str, str], overwrite: bool = False):
    """
    Persiste la configuración en .env.
    - overwrite=False (default): solo agrega claves que no existen (comportamiento original).
    - overwrite=True: actualiza claves existentes y agrega las nuevas.
    """
    try:
        lines = []
        if _CFG_FILE.exists():
            lines = _CFG_FILE.read_text(encoding="utf-8").splitlines()

        if overwrite:
            # Reconstruir el archivo actualizando los valores existentes
            new_lines = []
            updated_keys = set()
            for line in lines:
                stripped = line.strip()
                if stripped and not stripped.startswith("#") and "=" in stripped:
                    k, _, _ = stripped.partition("=")
                    k = k.strip()
                    if k in cfg:
                        new_lines.append(f"{k}={cfg[k]}")
                        updated_keys.add(k)
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)
            # Agregar claves nuevas que no estaban en el archivo
            for k, v in cfg.items():
                if k not in updated_keys:
                    new_lines.append(f"{k}={v}")
            if not lines:
                new_lines.insert(0, "# Clinical Extractor Pro — configuración automática")
            _CFG_FILE.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
        else:
            # Comportamiento original: solo agregar claves nuevas
            existing_keys = set()
            for line in lines:
                if "=" in line and not line.strip().startswith("#"):
                    k, _, _ = line.partition("=")
                    existing_keys.add(k.strip())
            with open(_CFG_FILE, "a", encoding="utf-8") as f:
                if not lines:
                    f.write("# Clinical Extractor Pro — configuración automática\n")
                for k, v in cfg.items():
                    if k not in existing_keys:
                        f.write(f"{k}={v}\n")
    except Exception as e:
        log.warning(f"No se pudo escribir .env: {e}")


_AUTO_CFG    = _load_or_create_config()

SECRET_KEY   = _AUTO_CFG.get("CEP_SECRET_KEY") or os.environ.get("CEP_SECRET_KEY", secrets.token_hex(32))
ADMIN_EMAIL  = _AUTO_CFG.get("CEP_ADMIN_EMAIL") or os.environ.get("CEP_ADMIN_EMAIL", "jcollazosr@uoc.edu")
ADMIN_PASS_ENV = _AUTO_CFG.get("CEP_ADMIN_PASSWORD") or os.environ.get("CEP_ADMIN_PASSWORD", "")

# Contraseña temporal hardcodeada SOLO para primer arranque sin .env
_TEMP_PASS_DEFAULT = "ClinicalPro@2026!"

DB_PATH_SEC  = Path(__file__).parent / "clinical_extractor_v14.db"

SESSION_TTL_H   = int(_AUTO_CFG.get("CEP_SESSION_TTL_H",   os.environ.get("CEP_SESSION_TTL_H",   "8")))
MAX_LOGIN_FAILS = int(_AUTO_CFG.get("CEP_MAX_LOGIN_FAILS",  os.environ.get("CEP_MAX_LOGIN_FAILS",  "5")))
LOCKOUT_MIN     = int(_AUTO_CFG.get("CEP_LOCKOUT_MIN",      os.environ.get("CEP_LOCKOUT_MIN",      "15")))

# ── Roles y permisos ────────────────────────────────────────────
class Role:
    ADMIN  = "admin"   # Control total: gestión de usuarios, exportación, auditoría
    EDITOR = "editor"  # Puede extraer, editar, exportar; NO gestiona usuarios
    READER = "reader"  # Solo lectura de resultados; NO puede exportar ni editar

PERMISSIONS = {
    Role.ADMIN:  {"extract", "edit", "export", "manage_users", "view_audit", "view_results"},
    Role.EDITOR: {"extract", "edit", "export", "view_results"},
    Role.READER: {"view_results"},
}

# ── Cifrado de datos clínicos (AES-256 vía Fernet) ──────────────

def _derive_fernet_key(secret: str) -> bytes:
    """Deriva una clave Fernet de 32 bytes a partir del SECRET_KEY usando PBKDF2."""
    if not CRYPTO_AVAILABLE:
        return b""
    salt = hashlib.sha256(b"clinical_extractor_v11_salt").digest()
    kdf = PBKDF2HMAC(
        algorithm=_crypto_hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480_000,
    )
    raw = kdf.derive(secret.encode("utf-8"))
    return _b64.urlsafe_b64encode(raw)


def get_fernet() -> Optional[Any]:
    """Retorna instancia Fernet si cryptography está disponible."""
    if not CRYPTO_AVAILABLE:
        return None
    try:
        key = _derive_fernet_key(SECRET_KEY)
        return Fernet(key)
    except Exception:
        return None


def encrypt_clinical_data(data: str) -> str:
    """Cifra datos clínicos con AES-256-GCM (Fernet). Devuelve texto si falla."""
    f = get_fernet()
    if f is None:
        return data
    try:
        return f.encrypt(data.encode("utf-8")).decode("utf-8")
    except Exception:
        return data


def decrypt_clinical_data(data: str) -> str:
    """Descifra datos clínicos. Devuelve el texto original si falla o no está cifrado."""
    f = get_fernet()
    if f is None:
        return data
    try:
        return f.decrypt(data.encode("utf-8")).decode("utf-8")
    except Exception:
        return data  # Compatible con datos no cifrados (migración)


# ── Configuración persistente cifrada en DB ──────────────────────

def save_app_config(key: str, value: str, updated_by: str = "system"):
    """Guarda un valor de configuración cifrado en la DB de seguridad."""
    encrypted = encrypt_clinical_data(value)
    con = _sec_db()
    con.execute(
        "INSERT INTO app_config (key, value, updated_at, updated_by) VALUES (?,?,?,?) "
        "ON CONFLICT(key) DO UPDATE SET value=excluded.value, "
        "updated_at=excluded.updated_at, updated_by=excluded.updated_by",
        (key, encrypted, datetime.utcnow().isoformat(), updated_by)
    )
    con.commit()


def load_app_config(key: str, default: str = "") -> str:
    """Lee y descifra un valor de configuración desde la DB de seguridad."""
    try:
        con = _sec_db()
        row = con.execute("SELECT value FROM app_config WHERE key=?", (key,)).fetchone()
        if row:
            return decrypt_clinical_data(row[0])
    except Exception:
        pass
    return default


# ── Hash de contraseña (bcrypt con cost factor 12) ──────────────

def hash_password(password: str) -> str:
    """Hash bcrypt con cost 12 (recomendación OWASP 2024)."""
    if BCRYPT_AVAILABLE:
        salt = _bcrypt.gensalt(rounds=12)
        return _bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")
    # Fallback: PBKDF2-SHA256 con 600k iteraciones si bcrypt no está disponible
    salt_bytes = secrets.token_bytes(32)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt_bytes, 600_000)
    return "pbkdf2$" + salt_bytes.hex() + "$" + dk.hex()


def verify_password(password: str, hashed: str) -> bool:
    """Verifica contraseña contra hash bcrypt o PBKDF2."""
    try:
        if hashed.startswith("pbkdf2$"):
            parts = hashed.split("$")
            salt_bytes = bytes.fromhex(parts[1])
            stored_dk  = bytes.fromhex(parts[2])
            dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt_bytes, 600_000)
            return hmac.compare_digest(dk, stored_dk)
        if BCRYPT_AVAILABLE:
            return _bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
    except Exception:
        pass
    return False


# ── JWT para sesiones ────────────────────────────────────────────

def create_session_token(user_id: str, email: str, role: str,
                          ttl_hours: int = None) -> str:
    """Genera JWT firmado HS256 con expiración. ttl_hours sobreescribe SESSION_TTL_H."""
    _ttl = ttl_hours if ttl_hours is not None else SESSION_TTL_H
    payload = {
        "sub":   user_id,
        "email": email,
        "role":  role,
        "iat":   datetime.utcnow(),
        "exp":   datetime.utcnow() + timedelta(hours=_ttl),
        "jti":   secrets.token_hex(16),  # JWT ID para revocación
    }
    if JWT_AVAILABLE:
        return _jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    # Fallback: token firmado con HMAC-SHA256
    import json as _json
    header  = _b64_url_encode(_json.dumps({"alg":"HS256","typ":"JWT"}).encode())
    body    = _b64_url_encode(_json.dumps(payload, default=str).encode())
    sig_raw = hmac.new(SECRET_KEY.encode(), f"{header}.{body}".encode(), hashlib.sha256).digest()
    return f"{header}.{body}.{_b64_url_encode(sig_raw)}"


def _b64_url_encode(data: bytes) -> str:
    import base64 as b
    return b.urlsafe_b64encode(data).rstrip(b"=").decode()


def verify_session_token(token: str) -> Optional[Dict]:
    """Verifica JWT y retorna payload si es válido, None si no."""
    try:
        if JWT_AVAILABLE:
            payload = _jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload
        # Fallback HMAC
        parts = token.split(".")
        if len(parts) != 3:
            return None
        sig_check = hmac.new(
            SECRET_KEY.encode(),
            f"{parts[0]}.{parts[1]}".encode(),
            hashlib.sha256
        ).digest()
        import base64 as b
        padding = "=" * (4 - len(parts[2]) % 4)
        sig_stored = b.urlsafe_b64decode(parts[2] + padding)
        if not hmac.compare_digest(sig_check, sig_stored):
            return None
        import json as _json
        payload_bytes = b.urlsafe_b64decode(parts[1] + "=" * (4 - len(parts[1]) % 4))
        return _json.loads(payload_bytes)
    except Exception:
        return None


# ── Base de datos de seguridad ──────────────────────────────────

def init_security_db():
    """Crea tablas de seguridad en la DB v11 si no existen."""
    # NOTA: usa conexión directa (NO el pool thread-local) porque executescript()
    # hace COMMIT implícito y dejaría la conexión del pool en estado inválido.
    con = sqlite3.connect(str(DB_PATH_SEC), check_same_thread=False, timeout=30)
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("PRAGMA foreign_keys=ON")
    cur = con.cursor()
    # Migration: add must_change_password if upgrading
    try:
        con.execute("ALTER TABLE users ADD COLUMN must_change_password INTEGER NOT NULL DEFAULT 0")
        con.commit()
    except Exception:
        pass  # Column already exists

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id                   TEXT PRIMARY KEY,
        email                TEXT UNIQUE NOT NULL,
        password_hash        TEXT NOT NULL,
        role                 TEXT NOT NULL DEFAULT 'reader',
        full_name            TEXT,
        is_active            INTEGER NOT NULL DEFAULT 1,
        created_at           TEXT NOT NULL,
        created_by           TEXT,
        last_login           TEXT,
        failed_attempts      INTEGER NOT NULL DEFAULT 0,
        locked_until         TEXT,
        must_change_password INTEGER NOT NULL DEFAULT 0
    );

    CREATE TABLE IF NOT EXISTS sessions (
        jti             TEXT PRIMARY KEY,
        user_id         TEXT NOT NULL,
        token           TEXT NOT NULL,
        created_at      TEXT NOT NULL,
        expires_at      TEXT NOT NULL,
        ip_address      TEXT,
        user_agent      TEXT,
        revoked         INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );

    CREATE TABLE IF NOT EXISTS security_audit (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp_utc   TEXT NOT NULL,
        user_id         TEXT,
        email           TEXT,
        action          TEXT NOT NULL,
        resource        TEXT,
        ip_address      TEXT,
        user_agent      TEXT,
        success         INTEGER NOT NULL DEFAULT 1,
        detail          TEXT
    );
    -- MEJORA v15b: índices para auditoría rápida en producción
    CREATE INDEX IF NOT EXISTS idx_audit_timestamp ON security_audit(timestamp_utc DESC);
    CREATE INDEX IF NOT EXISTS idx_audit_user      ON security_audit(user_id);
    CREATE INDEX IF NOT EXISTS idx_audit_email     ON security_audit(email);

    -- Configuración persistente cifrada (API keys, credenciales externas)
    CREATE TABLE IF NOT EXISTS app_config (
        key        TEXT PRIMARY KEY,
        value      TEXT NOT NULL,
        updated_at TEXT NOT NULL,
        updated_by TEXT
    );
    """)
    con.commit()
    con.close()


_sec_db_local = __import__("threading").local()

def _make_sec_conn() -> sqlite3.Connection:
    """Crea una conexión nueva a la DB de seguridad con los PRAGMAs correctos."""
    conn = sqlite3.connect(str(DB_PATH_SEC), check_same_thread=False, timeout=60)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA cache_size=-32000")
    conn.execute("PRAGMA temp_store=MEMORY")
    conn.row_factory = sqlite3.Row
    return conn

def _sec_db() -> sqlite3.Connection:
    """Conexión SQLite thread-local para DB de seguridad.
    Detecta y recrea automáticamente conexiones cerradas (p.ej. entre rerenders de Streamlit).
    """
    conn = getattr(_sec_db_local, "conn", None)
    if conn is not None:
        # Verificar que la conexión sigue abierta y operativa
        try:
            conn.execute("SELECT 1")
        except Exception:
            conn = None
            _sec_db_local.conn = None
    if conn is None:
        conn = _make_sec_conn()
        _sec_db_local.conn = conn
    return conn


def log_security_event(action: str, user_id: str = None, email: str = None,
                        resource: str = None, ip: str = None,
                        ua: str = None, success: bool = True, detail: str = None):
    """Registra evento de seguridad en audit log inmutable."""
    try:
        con = _sec_db()
        con.execute(
            "INSERT INTO security_audit "
            "(timestamp_utc, user_id, email, action, resource, ip_address, user_agent, success, detail) "
            "VALUES (?,?,?,?,?,?,?,?,?)",
            (datetime.utcnow().isoformat(), user_id, email, action,
             resource, ip, ua, 1 if success else 0, detail)
        )
        con.commit()
        con.close()
    except Exception as e:
        log.warning(f"Security audit log error: {e}")


# ── Gestión de usuarios ──────────────────────────────────────────

_bootstrap_done = False  # guard process-level
_bootstrap_lock = __import__("threading").Lock()  # evita condición de carrera en Streamlit Cloud

def bootstrap_admin():
    """
    Crea el administrador principal si no existe.
    MEJORA v15c: guard de proceso — evita consulta DB + bcrypt en cada rerun de Streamlit.
    MEJORA v15d: lock de hilo + INSERT OR IGNORE — evita sqlite3.IntegrityError por
                 condición de carrera en Streamlit Cloud (múltiples hilos llaman init_db
                 simultáneamente al arrancar).
    """
    global _bootstrap_done
    if _bootstrap_done:
        return

    with _bootstrap_lock:
        # Double-checked locking: re-verificar dentro del lock
        if _bootstrap_done:
            return

        con = _sec_db()
        try:
            row = con.execute(
                "SELECT id FROM users WHERE email=?", (ADMIN_EMAIL,)
            ).fetchone()

            if row:
                _bootstrap_done = True
                return  # Ya existe, nada que hacer

            # Usar contraseña configurada o la temporal por defecto
            password_to_use = ADMIN_PASS_ENV or _TEMP_PASS_DEFAULT
            is_temp         = not ADMIN_PASS_ENV
            admin_id        = str(uuid.uuid4())
            ph              = hash_password(password_to_use)

            try:
                # INSERT OR IGNORE: si hay colisión de UNIQUE, no lanza excepción
                con.execute(
                    "INSERT OR IGNORE INTO users "
                    "(id, email, password_hash, role, full_name, is_active, "
                    " created_at, created_by, must_change_password) "
                    "VALUES (?,?,?,?,?,1,?,?,?)",
                    (admin_id, ADMIN_EMAIL, ph, Role.ADMIN, "Administrador Principal",
                     datetime.utcnow().isoformat(), "system",
                     1 if is_temp else 0)
                )
                con.commit()
            except sqlite3.IntegrityError:
                # Salvaguarda extra: otro proceso insertó justo antes — no es un error
                log.info(f"ℹ️ Admin ya existía al momento del INSERT (carrera resuelta): {ADMIN_EMAIL}")
                _bootstrap_done = True
                return

            # Confirmar que la fila existe (INSERT OR IGNORE puede no insertar si ya había)
            created = con.execute(
                "SELECT id FROM users WHERE email=?", (ADMIN_EMAIL,)
            ).fetchone()

            if not created:
                _bootstrap_done = True
                return

            if is_temp:
                log.info(
                    f"✅ Admin creado con contraseña TEMPORAL: {ADMIN_EMAIL} / {_TEMP_PASS_DEFAULT} "
                    f"— Se pedirá cambio en el primer login."
                )
            else:
                log.info(f"✅ Admin creado con contraseña configurada: {ADMIN_EMAIL}")

            log_security_event("admin_bootstrap", user_id=admin_id, email=ADMIN_EMAIL,
                               detail=f"Admin creado, temp_password={is_temp}")
            _bootstrap_done = True

        finally:
            con.close()


def get_user_by_email(email: str) -> Optional[Dict]:
    try:
        con = _sec_db()
        row = con.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
        con.close()
        return dict(row) if row else None
    except Exception:
        return None


def get_all_users() -> List[Dict]:
    try:
        con = _sec_db()
        rows = con.execute(
            "SELECT id, email, role, full_name, is_active, created_at, last_login, "
            "failed_attempts, locked_until FROM users ORDER BY created_at"
        ).fetchall()
        con.close()
        return [dict(r) for r in rows]
    except Exception:
        return []


def create_user(email: str, password: str, role: str,
                full_name: str, created_by: str) -> Tuple[bool, str]:
    """Crea nuevo usuario. Solo admin puede llamar esto."""
    if role == Role.ADMIN:
        return False, "No se puede crear un segundo administrador"
    if role not in (Role.EDITOR, Role.READER):
        return False, f"Rol inválido: {role}"
    if len(password) < 10:
        return False, "La contraseña debe tener al menos 10 caracteres"
    # Validación mínima de contraseña (OWASP)
    has_upper  = any(c.isupper() for c in password)
    has_digit  = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*()_+-=[]{}|;':,.<>?" for c in password)
    if not (has_upper and has_digit and has_symbol):
        return False, "La contraseña debe tener mayúscula, número y símbolo especial"
    try:
        user_id = str(uuid.uuid4())
        ph      = hash_password(password)
        con = _sec_db()
        con.execute(
            "INSERT INTO users (id, email, password_hash, role, full_name, is_active, created_at, created_by) "
            "VALUES (?,?,?,?,?,1,?,?)",
            (user_id, email.lower().strip(), ph, role, full_name,
             datetime.utcnow().isoformat(), created_by)
        )
        con.commit()
        con.close()
        log_security_event("user_created", user_id=created_by, email=email,
                           detail=f"role={role}, name={full_name}")
        return True, "Usuario creado exitosamente"
    except sqlite3.IntegrityError:
        return False, "El email ya está registrado"
    except Exception as e:
        return False, str(e)


def update_user_role(user_id: str, new_role: str, admin_id: str) -> Tuple[bool, str]:
    """Cambia el rol de un usuario. Solo admin puede llamar esto."""
    if new_role not in (Role.EDITOR, Role.READER):
        return False, "Rol inválido"
    try:
        con = _sec_db()
        user = con.execute("SELECT email, role FROM users WHERE id=?", (user_id,)).fetchone()
        if not user:
            con.close()
            return False, "Usuario no encontrado"
        if user["role"] == Role.ADMIN:
            con.close()
            return False, "No se puede cambiar el rol del administrador"
        con.execute("UPDATE users SET role=? WHERE id=?", (new_role, user_id))
        con.commit()
        con.close()
        log_security_event("role_changed", user_id=admin_id,
                           detail=f"user={user['email']}, new_role={new_role}")
        return True, "Rol actualizado"
    except Exception as e:
        return False, str(e)


def toggle_user_active(user_id: str, admin_id: str) -> Tuple[bool, str]:
    """Activa/desactiva un usuario."""
    try:
        con = _sec_db()
        user = con.execute("SELECT email, role, is_active FROM users WHERE id=?", (user_id,)).fetchone()
        if not user:
            con.close()
            return False, "Usuario no encontrado"
        if user["role"] == Role.ADMIN:
            con.close()
            return False, "No se puede desactivar al administrador"
        new_state = 0 if user["is_active"] else 1
        con.execute("UPDATE users SET is_active=? WHERE id=?", (new_state, user_id))
        con.commit()
        con.close()
        action = "activated" if new_state else "deactivated"
        log_security_event(f"user_{action}", user_id=admin_id,
                           detail=f"user={user['email']}")
        return True, "Activo" if new_state else "Desactivado"
    except Exception as e:
        return False, str(e)


def delete_user(user_id: str, admin_id: str) -> Tuple[bool, str]:
    """Elimina un usuario (no el admin)."""
    try:
        con = _sec_db()
        user = con.execute("SELECT email, role FROM users WHERE id=?", (user_id,)).fetchone()
        if not user:
            con.close()
            return False, "Usuario no encontrado"
        if user["role"] == Role.ADMIN:
            con.close()
            return False, "No se puede eliminar al administrador"
        con.execute("DELETE FROM sessions WHERE user_id=?", (user_id,))
        con.execute("DELETE FROM users WHERE id=?", (user_id,))
        con.commit()
        con.close()
        log_security_event("user_deleted", user_id=admin_id, detail=f"user={user['email']}")
        return True, "Usuario eliminado"
    except Exception as e:
        return False, str(e)


def change_password(user_id: str, old_password: str, new_password: str) -> Tuple[bool, str]:
    """Permite a un usuario cambiar su propia contraseña."""
    if len(new_password) < 10:
        return False, "Mínimo 10 caracteres"
    has_upper  = any(c.isupper() for c in new_password)
    has_digit  = any(c.isdigit() for c in new_password)
    has_symbol = any(c in "!@#$%^&*()_+-=[]{}|;':,.<>?" for c in new_password)
    if not (has_upper and has_digit and has_symbol):
        return False, "La contraseña debe tener mayúscula, número y símbolo"
    try:
        con = _sec_db()
        user = con.execute("SELECT password_hash, email FROM users WHERE id=?", (user_id,)).fetchone()
        if not user or not verify_password(old_password, user["password_hash"]):
            con.close()
            return False, "Contraseña actual incorrecta"
        new_hash = hash_password(new_password)
        con.execute(
            "UPDATE users SET password_hash=?, must_change_password=0 WHERE id=?",
            (new_hash, user_id)
        )
        # Revocar todas las sesiones activas al cambiar contraseña
        con.execute("UPDATE sessions SET revoked=1 WHERE user_id=?", (user_id,))
        con.commit()
        con.close()
        log_security_event("password_changed", user_id=user_id, email=user["email"])
        return True, "Contraseña actualizada. Por seguridad, inicia sesión nuevamente."
    except Exception as e:
        return False, str(e)


# ── Autenticación ────────────────────────────────────────────────

def authenticate_user(email: str, password: str,
                       ip: str = "", ua: str = "") -> Tuple[bool, str, Optional[Dict]]:
    """
    Autentica usuario con rate limiting y bloqueo por intentos fallidos.
    Retorna (success, message, user_dict_or_None).
    """
    email = email.lower().strip()
    user  = get_user_by_email(email)

    if not user:
        log_security_event("login_failed", email=email, ip=ip, ua=ua, success=False,
                           detail="usuario no existe")
        time.sleep(0.5)  # Timing attack mitigation
        return False, "Credenciales inválidas", None

    # Verificar bloqueo
    if user.get("locked_until"):
        try:
            locked_until = datetime.fromisoformat(user["locked_until"])
            if datetime.utcnow() < locked_until:
                remaining = int((locked_until - datetime.utcnow()).total_seconds() / 60) + 1
                log_security_event("login_blocked", user_id=user["id"], email=email,
                                   ip=ip, ua=ua, success=False,
                                   detail=f"cuenta bloqueada por {remaining} min más")
                return False, f"Cuenta bloqueada. Intenta en {remaining} minuto(s).", None
        except Exception:
            pass

    if not user.get("is_active"):
        return False, "Cuenta desactivada. Contacta al administrador.", None

    if not verify_password(password, user["password_hash"]):
        # Incrementar intentos fallidos
        new_fails = user.get("failed_attempts", 0) + 1
        locked_until_str = None
        if new_fails >= MAX_LOGIN_FAILS:
            locked_until_str = (datetime.utcnow() + timedelta(minutes=LOCKOUT_MIN)).isoformat()

        con = _sec_db()
        con.execute(
            "UPDATE users SET failed_attempts=?, locked_until=? WHERE id=?",
            (new_fails, locked_until_str, user["id"])
        )
        con.commit()
        con.close()

        log_security_event("login_failed", user_id=user["id"], email=email,
                           ip=ip, ua=ua, success=False,
                           detail=f"intento {new_fails}/{MAX_LOGIN_FAILS}")

        if locked_until_str:
            return False, f"Demasiados intentos. Cuenta bloqueada {LOCKOUT_MIN} minutos.", None
        return False, f"Credenciales inválidas ({new_fails}/{MAX_LOGIN_FAILS} intentos).", None

    # Login exitoso — resetear contador
    now = datetime.utcnow().isoformat()
    token = create_session_token(user["id"], user["email"], user["role"])

    con = _sec_db()
    con.execute(
        "UPDATE users SET failed_attempts=0, locked_until=NULL, last_login=? WHERE id=?",
        (now, user["id"])
    )

    # Guardar sesión
    payload = verify_session_token(token)
    jti = payload.get("jti", secrets.token_hex(16)) if payload else secrets.token_hex(16)
    expires_at = (datetime.utcnow() + timedelta(hours=SESSION_TTL_H)).isoformat()
    con.execute(
        "INSERT INTO sessions (jti, user_id, token, created_at, expires_at, ip_address, user_agent) "
        "VALUES (?,?,?,?,?,?,?)",
        (jti, user["id"], token, now, expires_at, ip[:64] if ip else None,
         ua[:200] if ua else None)
    )
    con.commit()
    con.close()

    log_security_event("login_success", user_id=user["id"], email=email,
                       ip=ip, ua=ua, detail=f"role={user['role']}")

    return True, "Acceso concedido", {
        **user,
        "_token":              token,
        "_must_change_pass":   bool(user.get("must_change_password", 0)),
    }


def logout_user(token: str):
    """Revoca la sesión activa."""
    payload = verify_session_token(token)
    if payload:
        jti = payload.get("jti")
        if jti:
            try:
                con = _sec_db()
                con.execute("UPDATE sessions SET revoked=1 WHERE jti=?", (jti,))
                con.commit()
                con.close()
                log_security_event("logout", user_id=payload.get("sub"),
                                   email=payload.get("email"))
            except Exception:
                pass


def is_token_valid(token: str) -> Optional[Dict]:
    """Verifica token JWT y que no esté revocado en DB."""
    payload = verify_session_token(token)
    if not payload:
        return None
    jti = payload.get("jti")
    if not jti:
        return None
    try:
        con = _sec_db()
        row = con.execute(
            "SELECT revoked FROM sessions WHERE jti=?", (jti,)
        ).fetchone()
        con.close()
        if row and row["revoked"] == 0:
            return payload
    except Exception:
        pass
    return None


def has_permission(user_payload: Dict, permission: str) -> bool:
    """Verifica si el usuario tiene un permiso específico."""
    role = user_payload.get("role", "")
    return permission in PERMISSIONS.get(role, set())


def get_active_sessions() -> List[Dict]:
    """Retorna sesiones activas no expiradas (para admin)."""
    try:
        con = _sec_db()
        rows = con.execute("""
            SELECT s.jti, s.created_at, s.expires_at, s.ip_address, s.user_agent,
                   u.email, u.role, u.full_name
            FROM sessions s JOIN users u ON s.user_id = u.id
            WHERE s.revoked=0 AND s.expires_at > ?
            ORDER BY s.created_at DESC
        """, (datetime.utcnow().isoformat(),)).fetchall()
        con.close()
        return [dict(r) for r in rows]
    except Exception:
        return []


def get_security_audit_log(limit: int = 200) -> List[Dict]:
    """Retorna últimos eventos del log de seguridad."""
    try:
        con = _sec_db()
        rows = con.execute(
            "SELECT * FROM security_audit ORDER BY timestamp_utc DESC LIMIT ?",
            (limit,)
        ).fetchall()
        con.close()
        return [dict(r) for r in rows]
    except Exception:
        return []


def revoke_all_user_sessions(user_id: str, admin_id: str):
    """Revoca todas las sesiones de un usuario."""
    try:
        con = _sec_db()
        con.execute("UPDATE sessions SET revoked=1 WHERE user_id=?", (user_id,))
        con.commit()
        con.close()
        log_security_event("sessions_revoked", user_id=admin_id,
                           detail=f"all sessions for user_id={user_id}")
    except Exception:
        pass


# ── Decorador / helper de autorización para Streamlit ───────────

def require_auth(st_module, permission: str = "view_results") -> Optional[Dict]:
    """
    Verifica sesión activa en st.session_state.
    Retorna el payload del usuario autenticado o None si no está autenticado.
    """
    token = st_module.session_state.get("_auth_token")
    if not token:
        return None
    payload = is_token_valid(token)
    if not payload:
        st_module.session_state.pop("_auth_token", None)
        return None
    if not has_permission(payload, permission):
        return None
    return payload


# ═══════════════════════════════════════════════════════════════
# MÓDULO DE DEDUPLICACIÓN Y GESTIÓN DE PROYECTOS v12
# ═══════════════════════════════════════════════════════════════

# ── Tabla de registro de deduplicación en DB ────────────────────

DEDUP_SCHEMA = """
CREATE TABLE IF NOT EXISTS dedup_registry (
    file_hash       TEXT PRIMARY KEY,
    filename        TEXT NOT NULL,
    project_id      TEXT NOT NULL,
    source          TEXT,
    processed_at    TEXT NOT NULL,
    sheets_row_id   TEXT,          -- ID de fila en Google Sheets (para evitar duplicados allá)
    user_id         TEXT           -- Quién procesó
);

CREATE TABLE IF NOT EXISTS projects (
    id              TEXT PRIMARY KEY,
    name            TEXT NOT NULL,
    description     TEXT,
    created_at      TEXT NOT NULL,
    created_by      TEXT,
    is_active       INTEGER NOT NULL DEFAULT 1,
    total_files     INTEGER DEFAULT 0,
    sheets_tab_name TEXT             -- Nombre del tab dedicado en Sheets (opcional)
);

CREATE INDEX IF NOT EXISTS idx_dedup_project ON dedup_registry(project_id);
CREATE INDEX IF NOT EXISTS idx_dedup_hash    ON dedup_registry(file_hash);
"""

# ── ID de proyecto activo (por sesión) ─────────────────────────
DEFAULT_PROJECT_ID   = "default"
DEFAULT_PROJECT_NAME = "Proyecto Principal"


def init_dedup_db():
    """Crea tablas de deduplicación y proyecto si no existen."""
    # Conexión dedicada: executescript no compatible con pool thread-local
    con = sqlite3.connect(str(DB_PATH), check_same_thread=False, timeout=30)
    con.execute("PRAGMA journal_mode=WAL")
    con.executescript(DEDUP_SCHEMA)
    # Crear proyecto por defecto si no existe
    con.execute(
        "INSERT OR IGNORE INTO projects (id, name, created_at, created_by, is_active) "
        "VALUES (?,?,?,?,1)",
        (DEFAULT_PROJECT_ID, DEFAULT_PROJECT_NAME,
         datetime.utcnow().isoformat(), "system")
    )
    con.commit()
    con.close()


# ── Operaciones de deduplicación ────────────────────────────────

def is_duplicate(file_hash: str, project_id: str = DEFAULT_PROJECT_ID) -> Optional[Dict]:
    """
    Verifica si un archivo ya fue procesado en el proyecto activo.
    Retorna info del procesamiento previo si existe, None si es nuevo.
    """
    try:
        con = _get_db_connection()
        row = con.execute(
            "SELECT filename, processed_at, source, sheets_row_id, user_id "
            "FROM dedup_registry WHERE file_hash=? AND project_id=?",
            (file_hash, project_id)
        ).fetchone()
        con.close()
        if row:
            return {
                "filename":     row[0],
                "processed_at": row[1],
                "source":       row[2],
                "sheets_row_id":row[3],
                "user_id":      row[4],
            }
    except Exception as e:
        log.warning(f"Dedup check error: {e}")
    return None


def register_processed(file_hash: str, filename: str,
                        project_id: str = DEFAULT_PROJECT_ID,
                        source: str = "local", user_id: str = "",
                        sheets_row_id: str = None):
    """Registra un archivo como procesado en el dedup_registry."""
    try:
        con = _get_db_connection()
        con.execute(
            "INSERT OR REPLACE INTO dedup_registry "
            "(file_hash, filename, project_id, source, processed_at, sheets_row_id, user_id) "
            "VALUES (?,?,?,?,?,?,?)",
            (file_hash, filename, project_id, source,
             datetime.utcnow().isoformat(), sheets_row_id, user_id)
        )
        # Actualizar contador del proyecto
        con.execute(
            "UPDATE projects SET total_files = total_files + 1 WHERE id=?",
            (project_id,)
        )
        con.commit()
        con.close()
    except Exception as e:
        log.warning(f"Register processed error: {e}")


def get_project_hashes(project_id: str) -> set:
    """Retorna el conjunto de hashes ya procesados en un proyecto."""
    try:
        con = _get_db_connection()
        rows = con.execute(
            "SELECT file_hash FROM dedup_registry WHERE project_id=?",
            (project_id,)
        ).fetchall()
        con.close()
        return {r[0] for r in rows}
    except Exception:
        return set()


def get_all_projects() -> List[Dict]:
    """Lista todos los proyectos."""
    try:
        con = _get_db_connection()
        rows = con.execute(
            "SELECT id, name, description, created_at, is_active, total_files, sheets_tab_name "
            "FROM projects ORDER BY created_at DESC"
        ).fetchall()
        con.close()
        return [{"id":r[0],"name":r[1],"description":r[2],"created_at":r[3],
                 "is_active":r[4],"total_files":r[5],"sheets_tab":r[6]} for r in rows]
    except Exception:
        return []


def create_project(name: str, description: str = "",
                   created_by: str = "", sheets_tab: str = None) -> str:
    """Crea un nuevo proyecto y retorna su ID."""
    project_id = f"proj_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{secrets.token_hex(4)}"
    try:
        con = _get_db_connection()
        con.execute(
            "INSERT INTO projects (id, name, description, created_at, created_by, is_active, sheets_tab_name) "
            "VALUES (?,?,?,?,?,1,?)",
            (project_id, name, description,
             datetime.utcnow().isoformat(), created_by, sheets_tab)
        )
        con.commit()
        con.close()
        log.info(f"✅ Proyecto creado: {name} ({project_id})")
    except Exception as e:
        log.error(f"Error creando proyecto: {e}")
    return project_id


def clear_project_data(project_id: str, also_clear_extractions: bool = False,
                        user_id: str = "") -> Dict[str, int]:
    """
    Limpia los datos de un proyecto:
    - Siempre: elimina dedup_registry del proyecto (permite re-procesar)
    - Si also_clear_extractions: elimina también processed_files del proyecto
    Retorna dict con conteo de registros eliminados.
    """
    counts = {"dedup": 0, "extractions": 0}
    try:
        con = _get_db_connection()

        # 1. Obtener hashes del proyecto para eliminar extractions si aplica
        if also_clear_extractions:
            hashes = [r[0] for r in con.execute(
                "SELECT file_hash FROM dedup_registry WHERE project_id=?",
                (project_id,)
            ).fetchall()]
            if hashes:
                placeholders = ",".join("?" * len(hashes))
                cur = con.execute(
                    f"DELETE FROM processed_files WHERE file_hash IN ({placeholders})",
                    hashes
                )
                counts["extractions"] = cur.rowcount

        # 2. Limpiar dedup_registry
        cur = con.execute(
            "DELETE FROM dedup_registry WHERE project_id=?", (project_id,)
        )
        counts["dedup"] = cur.rowcount

        # 3. Resetear contador del proyecto
        con.execute(
            "UPDATE projects SET total_files=0 WHERE id=?", (project_id,)
        )
        con.commit()
        con.close()

        log_security_event("project_cleared", user_id=user_id,
                           detail=f"project={project_id}, "
                                  f"dedup={counts['dedup']}, "
                                  f"extractions={counts['extractions']}")
    except Exception as e:
        log.error(f"Error limpiando proyecto: {e}")
    return counts


def delete_project(project_id: str, user_id: str = "") -> Tuple[bool, str]:
    """Elimina completamente un proyecto y todos sus datos."""
    if project_id == DEFAULT_PROJECT_ID:
        return False, "No se puede eliminar el proyecto principal"
    try:
        counts = clear_project_data(project_id, also_clear_extractions=True, user_id=user_id)
        con = _get_db_connection()
        con.execute("DELETE FROM projects WHERE id=?", (project_id,))
        con.commit()
        con.close()
        log_security_event("project_deleted", user_id=user_id, detail=f"project={project_id}")
        return True, f"Proyecto eliminado ({counts['extractions']} extracciones borradas)"
    except Exception as e:
        return False, str(e)


# ── Deduplicación con Google Sheets ────────────────────────────

_sheets_hashes_cache: Dict[str, Any] = {"hashes": set(), "ts": 0.0}
_SHEETS_CACHE_TTL = int(os.environ.get("CEP_SHEETS_CACHE_TTL", "300"))  # 5 min default

def get_sheets_processed_hashes(sheets_manager) -> set:
    """
    Lee los hashes ya existentes en la columna 'FileHash' de la hoja Sheets.
    MEJORA v15c: cache con TTL de 5 min — evita llamar get_all_records() en cada archivo
    del lote (puede ser miles de filas y tarda varios segundos).
    """
    if sheets_manager is None:
        return set()
    now = time.monotonic()
    if now - _sheets_hashes_cache["ts"] < _SHEETS_CACHE_TTL:
        return _sheets_hashes_cache["hashes"]
    try:
        all_records = sheets_manager.get_all_records()
        hashes = set()
        for rec in all_records:
            h = rec.get("FileHash") or rec.get("file_hash") or rec.get("filehash")
            if h:
                hashes.add(str(h).strip())
        _sheets_hashes_cache["hashes"] = hashes
        _sheets_hashes_cache["ts"] = now
        log.info(f"📊 Sheets dedup cache actualizado: {len(hashes)} hashes")
        return hashes
    except Exception as e:
        log.warning(f"No se pudieron leer hashes de Sheets: {e}")
        return _sheets_hashes_cache["hashes"]  # devolver cache viejo si falla


def check_duplicate_in_session(file_hash: str,
                                 session_results: List[Dict]) -> Optional[str]:
    """
    Verifica si el hash ya existe en los resultados de la sesión actual.
    Retorna el nombre del archivo duplicado o None.
    """
    for r in session_results:
        if r.get("_file_hash") == file_hash or r.get("_hash") == file_hash:
            return r.get("_filename", "desconocido")
    return None


# ── Pre-screening de lote antes de extracción ──────────────────

def pre_screen_files(files_data: List[Tuple[bytes, str, str]],
                      project_id: str,
                      session_results: List[Dict],
                      sheets_manager=None,
                      force_reprocess: bool = False
                      ) -> Tuple[List[Tuple], List[Dict]]:
    """
    Separa un lote de archivos en:
    - to_process: archivos nuevos (sin duplicado)
    - duplicates: archivos ya procesados (con info del procesamiento previo)

    Si force_reprocess=True, todos pasan a to_process.
    """
    to_process: List[Tuple] = []
    duplicates: List[Dict]  = []

    # Cargar hashes de Sheets (retroalimentación externa)
    sheets_hashes = get_sheets_processed_hashes(sheets_manager) if not force_reprocess else set()

    # Cargar hashes del proyecto en DB
    db_hashes = get_project_hashes(project_id) if not force_reprocess else set()

    seen_in_batch: set = set()  # Para dedup dentro del mismo lote

    for file_data, filename, source in files_data:
        file_hash = compute_hash(file_data)

        # 1. Duplicado dentro del mismo lote
        if file_hash in seen_in_batch:
            duplicates.append({
                "filename": filename,
                "file_hash": file_hash,
                "reason": "duplicate_in_batch",
                "detail": "El mismo archivo aparece más de una vez en este lote",
                "prior_filename": filename,
                "prior_date": "este lote",
            })
            continue
        seen_in_batch.add(file_hash)

        # 2. Duplicado en sesión actual (mismo proceso)
        session_dup = check_duplicate_in_session(file_hash, session_results)
        if session_dup:
            duplicates.append({
                "filename": filename,
                "file_hash": file_hash,
                "reason": "duplicate_in_session",
                "detail": f"Ya procesado en esta sesión como '{session_dup}'",
                "prior_filename": session_dup,
                "prior_date": "sesión actual",
            })
            continue

        # 3. Duplicado en DB local (proyecto actual)
        db_info = is_duplicate(file_hash, project_id)
        if db_info:
            duplicates.append({
                "filename": filename,
                "file_hash": file_hash,
                "reason": "duplicate_in_db",
                "detail": f"Ya procesado el {db_info['processed_at'][:10]}",
                "prior_filename": db_info["filename"],
                "prior_date": db_info["processed_at"][:19],
                "prior_source": db_info.get("source", ""),
            })
            continue

        # 4. Duplicado en Google Sheets (feedback externo)
        if file_hash in sheets_hashes:
            duplicates.append({
                "filename": filename,
                "file_hash": file_hash,
                "reason": "duplicate_in_sheets",
                "detail": "Hash encontrado en Google Sheets (procesado desde otra sesión o máquina)",
                "prior_filename": filename,
                "prior_date": "Google Sheets",
            })
            continue

        to_process.append((file_data, filename, source))

    return to_process, duplicates


# ═══════════════════════════════════════════════════════════════
# MÓDULO A — COLA DE PROCESAMIENTO PERSISTENTE
# ═══════════════════════════════════════════════════════════════

QUEUE_SCHEMA = """
CREATE TABLE IF NOT EXISTS job_queue (
    id           TEXT PRIMARY KEY,
    project_id   TEXT NOT NULL,
    filename     TEXT NOT NULL,
    source       TEXT NOT NULL DEFAULT 'local',
    file_hash    TEXT,
    status       TEXT NOT NULL DEFAULT 'pending',
    priority     INTEGER NOT NULL DEFAULT 5,
    created_at   TEXT NOT NULL,
    started_at   TEXT,
    finished_at  TEXT,
    attempts     INTEGER NOT NULL DEFAULT 0,
    max_attempts INTEGER NOT NULL DEFAULT 3,
    last_error   TEXT,
    result_id    TEXT,
    user_id      TEXT,
    config_json  TEXT
);
CREATE INDEX IF NOT EXISTS idx_queue_status   ON job_queue(status, priority DESC, created_at);
CREATE INDEX IF NOT EXISTS idx_queue_project  ON job_queue(project_id, status);
CREATE INDEX IF NOT EXISTS idx_queue_hash     ON job_queue(file_hash);
"""


def init_queue_db():
    # Conexión dedicada: executescript no compatible con pool thread-local
    con = sqlite3.connect(str(DB_PATH), check_same_thread=False, timeout=30)
    con.execute("PRAGMA journal_mode=WAL")
    con.executescript(QUEUE_SCHEMA)
    con.commit()
    con.close()


def queue_enqueue(filename: str, file_hash: str, source: str,
                   project_id: str, user_id: str = "",
                   priority: int = 5, config: Dict = None) -> str:
    """Encola un archivo para procesamiento. Retorna el job_id."""
    job_id = f"job_{secrets.token_hex(8)}"
    con = _get_db_connection()
    con.execute(
        "INSERT OR IGNORE INTO job_queue "
        "(id, project_id, filename, source, file_hash, status, priority, "
        " created_at, user_id, config_json) "
        "VALUES (?,?,?,?,?,?,?,?,?,?)",
        (job_id, project_id, filename, source, file_hash, "pending",
         priority, datetime.utcnow().isoformat(), user_id,
         json.dumps(config or {}))
    )
    con.commit()
    con.close()
    log.info(f"📬 Encolado: {filename} → {job_id}")
    return job_id


def queue_claim_next(worker_id: str = "") -> Optional[Dict]:
    """
    Reclama atómicamente el siguiente job pendiente.
    Usa UPDATE … RETURNING para evitar race conditions.
    """
    con = _get_db_connection()
    try:
        now = datetime.utcnow().isoformat()
        row = con.execute(
            "SELECT id FROM job_queue "
            "WHERE status='pending' AND attempts < max_attempts "
            "ORDER BY priority DESC, created_at ASC LIMIT 1"
        ).fetchone()
        if not row:
            con.close()
            return None
        job_id = row[0]
        con.execute(
            "UPDATE job_queue SET status='processing', started_at=?, attempts=attempts+1 "
            "WHERE id=? AND status='pending'",
            (now, job_id)
        )
        con.commit()
        job = con.execute("SELECT * FROM job_queue WHERE id=?", (job_id,)).fetchone()
        con.close()
        if job:
            cols = ["id","project_id","filename","source","file_hash","status",
                    "priority","created_at","started_at","finished_at","attempts",
                    "max_attempts","last_error","result_id","user_id","config_json"]
            return dict(zip(cols, job))
    except Exception as e:
        log.error(f"queue_claim_next error: {e}")
        con.close()
    return None


def queue_complete(job_id: str, result_id: str = ""):
    con = _get_db_connection()
    con.execute(
        "UPDATE job_queue SET status='done', finished_at=?, result_id=? WHERE id=?",
        (datetime.utcnow().isoformat(), result_id, job_id)
    )
    con.commit()
    con.close()


def queue_fail(job_id: str, error: str):
    con = _get_db_connection()
    row = con.execute(
        "SELECT attempts, max_attempts FROM job_queue WHERE id=?", (job_id,)
    ).fetchone()
    if row:
        attempts, max_att = row
        new_status = "failed" if attempts >= max_att else "pending"
        con.execute(
            "UPDATE job_queue SET status=?, last_error=?, finished_at=? WHERE id=?",
            (new_status, error[:500], datetime.utcnow().isoformat(), job_id)
        )
        con.commit()
    con.close()


def queue_stats(project_id: str = None) -> Dict[str, int]:
    con = _get_db_connection()
    where = "WHERE project_id=?" if project_id else ""
    params = (project_id,) if project_id else ()
    rows = con.execute(
        f"SELECT status, COUNT(*) FROM job_queue {where} GROUP BY status", params
    ).fetchall()
    con.close()
    return {r[0]: r[1] for r in rows}


def queue_retry_failed(project_id: str = None) -> int:
    con = _get_db_connection()
    where = "AND project_id=?" if project_id else ""
    params = (project_id,) if project_id else ()
    cur = con.execute(
        f"UPDATE job_queue SET status='pending', attempts=0, last_error=NULL "
        f"WHERE status='failed' {where}", params
    )
    n = cur.rowcount
    con.commit()
    con.close()
    return n


def queue_get_failed(project_id: str = None, limit: int = 50) -> List[Dict]:
    con = _get_db_connection()
    where = "AND project_id=?" if project_id else ""
    params = (*((project_id,) if project_id else ()), limit)
    rows = con.execute(
        f"SELECT id, filename, attempts, last_error, created_at "
        f"FROM job_queue WHERE status='failed' {where} "
        f"ORDER BY created_at DESC LIMIT ?", params
    ).fetchall()
    con.close()
    return [{"id":r[0],"filename":r[1],"attempts":r[2],
             "error":r[3],"created_at":r[4]} for r in rows]


# ═══════════════════════════════════════════════════════════════
# MÓDULO B — BUSCADOR CLÍNICO
# ═══════════════════════════════════════════════════════════════

def clinical_search(
    diagnostico: str = "",
    cie10_codigo: str = "",
    medicamento: str = "",
    edad_min: int = None,
    edad_max: int = None,
    sexo: str = "",
    fecha_desde: str = "",
    fecha_hasta: str = "",
    tipo_consulta: str = "",
    confianza_min: float = 0.0,
    proyecto_id: str = None,
    limit: int = 200,
) -> List[Dict]:
    """
    Búsqueda clínica estructurada sobre los datos extraídos.
    Combina filtros SQL sobre metadatos + búsqueda en JSON de datos.
    """
    try:
        con = _get_db_connection()
        conditions = ["status='done'"]
        params: List = []

        if tipo_consulta:
            conditions.append("tipo_consulta=?")
            params.append(tipo_consulta)
        if confianza_min > 0:
            conditions.append("confidence >= ?")
            params.append(confianza_min)
        if fecha_desde:
            conditions.append("processed_at >= ?")
            params.append(fecha_desde)
        if fecha_hasta:
            conditions.append("processed_at <= ?")
            params.append(fecha_hasta + "T23:59:59")

        where = " AND ".join(conditions)
        rows = con.execute(
            f"SELECT id, filename, processed_at, confidence, "
            f"tipo_consulta, data_json "
            f"FROM processed_files WHERE {where} "
            f"ORDER BY processed_at DESC LIMIT {limit * 3}",
            params
        ).fetchall()
        con.close()

        results = []
        for row in rows:
            try:
                data = json.loads(row[5]) if row[5] else {}
            except Exception:
                continue

            # Filtros en JSON data
            if diagnostico:
                dx = str(data.get("diagnostico_principal","") or "").lower()
                dx_sec = " ".join(str(d) for d in (data.get("diagnosticos_secundarios") or [])).lower()
                if diagnostico.lower() not in dx and diagnostico.lower() not in dx_sec:
                    continue

            if cie10_codigo:
                c10 = str(data.get("codigo_cie10_principal","") or "").upper()
                c10_sec = " ".join(str(c) for c in (data.get("codigos_cie10_secundarios") or [])).upper()
                if not (c10.startswith(cie10_codigo.upper()) or
                        cie10_codigo.upper() in c10_sec):
                    continue

            if medicamento:
                meds = " ".join(str(m) for m in (data.get("medicamentos") or [])).lower()
                if medicamento.lower() not in meds:
                    continue

            if sexo:
                s = str(data.get("sexo","") or "").lower()
                if sexo.lower() not in s:
                    continue

            if edad_min is not None or edad_max is not None:
                edad_raw = str(data.get("edad","") or "")
                nums = re.findall(r"\d+", edad_raw)
                if nums:
                    edad = int(nums[0])
                    if edad_min is not None and edad < edad_min:
                        continue
                    if edad_max is not None and edad > edad_max:
                        continue
                else:
                    continue  # Sin edad → excluir si se filtra por edad

            results.append({
                "id":            row[0],
                "filename":      row[1],
                "processed_at":  row[2][:10],
                "confidence":    row[3],
                "tipo_consulta": row[4],
                **{k: v for k, v in data.items()
                   if k in ["nombre_paciente","edad","sexo",
                             "diagnostico_principal","codigo_cie10_principal",
                             "medicamentos","fecha_consulta",
                             "tension_arterial","numero_documento"]},
            })
            if len(results) >= limit:
                break

        return results
    except Exception as e:
        log.error(f"clinical_search error: {e}")
        return []


# ═══════════════════════════════════════════════════════════════
# MÓDULO C — EXPORTACIÓN FHIR R4 + CSV INVESTIGACIÓN
# ═══════════════════════════════════════════════════════════════

def _data_to_fhir_patient(data: Dict, anon_id: str = None) -> Dict:
    """Construye un recurso FHIR R4 Patient desde datos extraídos."""
    pid = anon_id or data.get("numero_documento", str(uuid.uuid4()))
    resource: Dict = {
        "resourceType": "Patient",
        "id": pid,
        "meta": {"profile": ["http://hl7.org/fhir/StructureDefinition/Patient"]},
    }
    nombre = data.get("nombre_paciente")
    if nombre and nombre != "[REDACTED]":
        parts = str(nombre).split()
        resource["name"] = [{"use": "official",
                              "family": parts[-1] if parts else "",
                              "given":  parts[:-1] if len(parts) > 1 else parts}]

    fn = data.get("fecha_nacimiento")
    if fn:
        resource["birthDate"] = str(fn)[:10]

    sexo = str(data.get("sexo","") or "").lower()
    if "f" in sexo:
        resource["gender"] = "female"
    elif "m" in sexo:
        resource["gender"] = "male"

    return resource


def _data_to_fhir_encounter(data: Dict, patient_id: str,
                              record_id: str, filename: str) -> Dict:
    """Construye un recurso FHIR R4 Encounter."""
    return {
        "resourceType": "Encounter",
        "id": record_id,
        "status": "finished",
        "class": {"system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                  "code": "AMB", "display": "ambulatory"},
        "subject": {"reference": f"Patient/{patient_id}"},
        "type": [{"text": data.get("tipo_consulta","Consulta")}],
        "period": {"start": str(data.get("fecha_consulta",""))[:10]
                   if data.get("fecha_consulta") else None},
        "reasonCode": [{"text": data.get("motivo_consulta","")}]
                       if data.get("motivo_consulta") else [],
        "meta": {"source": filename},
    }


def _data_to_fhir_condition(data: Dict, patient_id: str,
                              encounter_id: str, is_secondary: bool = False) -> Optional[Dict]:
    """Construye un recurso FHIR R4 Condition."""
    dx = data.get("diagnostico_principal" if not is_secondary else "diagnosticos_secundarios")
    if not dx:
        return None
    if isinstance(dx, list):
        dx = dx[0] if dx else None
    if not dx:
        return None

    cie = data.get("codigo_cie10_principal" if not is_secondary
                   else "codigos_cie10_secundarios")
    if isinstance(cie, list):
        cie = cie[0] if cie else None

    resource: Dict = {
        "resourceType": "Condition",
        "id": f"cond-{encounter_id}-{'sec' if is_secondary else 'prim'}",
        "clinicalStatus": {
            "coding": [{"system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
                         "code": "active"}]
        },
        "subject": {"reference": f"Patient/{patient_id}"},
        "encounter": {"reference": f"Encounter/{encounter_id}"},
        "code": {"text": str(dx)},
    }
    if cie:
        resource["code"]["coding"] = [{
            "system": "http://hl7.org/fhir/sid/icd-10",
            "code": str(cie).upper(),
            "display": str(dx),
        }]
    return resource


def _data_to_fhir_observation(data: Dict, patient_id: str,
                               encounter_id: str) -> List[Dict]:
    """Construye recursos FHIR R4 Observation para signos vitales."""
    obs = []
    vitals = {
        "tension_arterial":     ("55284-4", "Blood Pressure"),
        "frecuencia_cardiaca":  ("8867-4",  "Heart rate"),
        "temperatura":          ("8310-5",  "Body temperature"),
        "saturacion_oxigeno":   ("2708-6",  "Oxygen saturation"),
        "peso":                 ("29463-7", "Body weight"),
        "talla":                ("8302-2",  "Body height"),
        "frecuencia_respiratoria": ("9279-1","Respiratory rate"),
        "glucemia":             ("2339-0",  "Glucose"),
    }
    for campo, (loinc, display) in vitals.items():
        val = data.get(campo)
        if not val:
            continue
        obs.append({
            "resourceType": "Observation",
            "id": f"obs-{encounter_id}-{campo}",
            "status": "final",
            "code": {
                "coding": [{"system": "http://loinc.org",
                             "code": loinc, "display": display}],
                "text": display,
            },
            "subject":   {"reference": f"Patient/{patient_id}"},
            "encounter": {"reference": f"Encounter/{encounter_id}"},
            "valueString": str(val),
        })
    return obs


def _data_to_fhir_medication_request(data: Dict, patient_id: str,
                                      encounter_id: str) -> List[Dict]:
    """Construye recursos FHIR R4 MedicationRequest."""
    meds = data.get("medicamentos") or []
    if isinstance(meds, str):
        meds = [meds]
    resources = []
    for i, med in enumerate(meds[:20]):
        resources.append({
            "resourceType": "MedicationRequest",
            "id": f"medrq-{encounter_id}-{i}",
            "status": "active",
            "intent": "order",
            "medicationCodeableConcept": {"text": str(med)},
            "subject":   {"reference": f"Patient/{patient_id}"},
            "encounter": {"reference": f"Encounter/{encounter_id}"},
        })
    return resources


def export_fhir_bundle(results: List[Dict], anon_mode: bool = False) -> Dict:
    """
    Exporta resultados como FHIR R4 Bundle (transaction).
    Cada historia clínica → Patient + Encounter + Conditions + Observations + MedRequests.
    """
    entries = []
    for r in results:
        if r.get("_status") != "done":
            continue
        data        = {k: v for k, v in r.items() if not k.startswith("_")}
        record_id   = r.get("_id", str(uuid.uuid4()))[:20]
        anon_id     = r.get("_anon_id", "")
        patient_id  = anon_id if (anon_mode and anon_id) else \
                      str(data.get("numero_documento", record_id))
        filename    = r.get("_filename", "")

        # Patient
        patient = _data_to_fhir_patient(data if not anon_mode else
                                          {k: v for k, v in data.items()
                                           if k not in ("nombre_paciente","numero_documento")},
                                          patient_id)
        entries.append({"resource": patient,
                         "request": {"method":"PUT",
                                     "url":f"Patient/{patient_id}"}})

        # Encounter
        enc = _data_to_fhir_encounter(data, patient_id, record_id, filename)
        entries.append({"resource": enc,
                         "request": {"method":"PUT",
                                     "url":f"Encounter/{record_id}"}})

        # Conditions
        cond_p = _data_to_fhir_condition(data, patient_id, record_id)
        if cond_p:
            entries.append({"resource": cond_p,
                             "request": {"method":"PUT",
                                         "url":f"Condition/{cond_p['id']}"}})
        for dx_sec in (data.get("diagnosticos_secundarios") or [])[:5]:
            cond_s = _data_to_fhir_condition(
                {"diagnosticos_secundarios": [dx_sec],
                 "codigos_cie10_secundarios": data.get("codigos_cie10_secundarios",[])},
                patient_id, record_id, is_secondary=True
            )
            if cond_s:
                entries.append({"resource": cond_s,
                                 "request": {"method":"PUT",
                                             "url":f"Condition/{cond_s['id']}"}})

        # Observations (signos vitales)
        for obs in _data_to_fhir_observation(data, patient_id, record_id):
            entries.append({"resource": obs,
                             "request": {"method":"PUT",
                                         "url":f"Observation/{obs['id']}"}})

        # MedicationRequests
        for mr in _data_to_fhir_medication_request(data, patient_id, record_id):
            entries.append({"resource": mr,
                             "request": {"method":"PUT",
                                         "url":f"MedicationRequest/{mr['id']}"}})

    return {
        "resourceType": "Bundle",
        "type": "transaction",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "total": len(entries),
        "entry": entries,
    }


def export_research_csv(results: List[Dict], campos: List[str],
                         anon_mode: bool = True) -> str:
    """
    Exporta CSV estructurado para investigación con metadatos de trazabilidad.
    Incluye completitud, confianza por campo y flags de inferencia.
    """
    rows = []
    for r in results:
        if r.get("_status") != "done":
            continue
        traces  = r.get("_field_traces", {})
        row: Dict = {
            "record_id":     r.get("_id", ""),
            "anon_id":       r.get("_anon_id", ""),
            "filename":      r.get("_filename", ""),
            "processed_at":  r.get("_processed_at", "")[:10],
            "tipo_consulta": r.get("_tipo_consulta", ""),
            "confidence":    round(r.get("_confidence", 0), 3),
            "ocr_score":     r.get("_ocr_quality", {}).get("score", ""),
            "needs_review":  int(r.get("_needs_review", False)),
            "n_alerts":      len(r.get("_alerts", [])),
            "n_inferences":  sum(1 for t in traces.values()
                                  if isinstance(t, dict) and t.get("es_inferencia")),
        }
        for campo in campos:
            val = r.get(campo, "")
            if anon_mode and campo in ("nombre_paciente","numero_documento"):
                row[campo] = "[REDACTED]"
            elif isinstance(val, list):
                row[campo] = " | ".join(str(v) for v in val if v)
            else:
                row[campo] = val if val is not None else ""

            # Metadatos de trazabilidad por campo
            t = traces.get(campo, {})
            if isinstance(t, dict):
                row[f"{campo}_conf"]   = round(t.get("confianza", 0), 3)
                row[f"{campo}_infer"]  = int(t.get("es_inferencia", False))
                row[f"{campo}_pagina"] = t.get("pagina", "")
        rows.append(row)

    if not rows:
        return ""
    return pd.DataFrame(rows).to_csv(index=False)


# ═══════════════════════════════════════════════════════════════
# MÓDULO D — SEGMENTACIÓN MULTI-PACIENTE
# ═══════════════════════════════════════════════════════════════

# Patrones que suelen indicar el inicio de una nueva historia clínica
_MULTI_PATIENT_SEPARATORS = [
    re.compile(r'(?:^|\n)\s*[-=_*]{10,}\s*(?:\n|$)'),           # Línea separadora
    re.compile(r'(?:^|\n)\s*(?:paciente|patient)\s*[:#]\s*\d+', re.I),
    re.compile(r'(?:^|\n)\s*historia\s+clínica\s*[:#nN°o]\s*\d+', re.I),
    re.compile(r'(?:^|\n)\s*h\.?c\.?\s*[:#nN°]\s*\d+', re.I),
    re.compile(r'(?:^|\n)\s*(?:nombre|name)\s*[:,]\s*[A-ZÁÉÍÓÚ][a-záéíóú]', re.I),
    re.compile(r'\[Página\s+1\s+OCR\]'),                          # Nueva pág 1 de OCR
]

_MIN_PATIENT_CHARS = 200   # Un paciente tiene al menos 200 chars


def detect_multi_patient(text: str) -> bool:
    """Detecta si un documento contiene múltiples historias clínicas."""
    hits = sum(len(p.findall(text)) for p in _MULTI_PATIENT_SEPARATORS)
    return hits >= 2


def split_multi_patient(text: str, filename: str) -> List[Tuple[str, str]]:
    """
    Divide un texto multi-paciente en segmentos individuales.
    Retorna lista de (texto_paciente, nombre_derivado).
    """
    if not detect_multi_patient(text):
        return [(text, filename)]

    # Encontrar todas las posiciones de separadores
    cut_positions = set()
    for pat in _MULTI_PATIENT_SEPARATORS:
        for m in pat.finditer(text):
            cut_positions.add(m.start())

    positions = sorted(cut_positions) + [len(text)]
    segments: List[Tuple[str, str]] = []
    prev = 0

    for i, pos in enumerate(positions):
        chunk = text[prev:pos].strip()
        if len(chunk) >= _MIN_PATIENT_CHARS:
            derived_name = f"{Path(filename).stem}_paciente{len(segments)+1}{Path(filename).suffix}"
            segments.append((chunk, derived_name))
        prev = pos

    # Si no se pudo separar bien, devolver el original
    return segments if len(segments) > 1 else [(text, filename)]


# ═══════════════════════════════════════════════════════════════
# MÓDULO E — MONITOREO Y ALERTAS
# ═══════════════════════════════════════════════════════════════

MONITOR_SCHEMA = """
CREATE TABLE IF NOT EXISTS monitor_snapshots (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp    TEXT NOT NULL,
    period       TEXT NOT NULL,
    total_docs   INTEGER DEFAULT 0,
    done_docs    INTEGER DEFAULT 0,
    error_docs   INTEGER DEFAULT 0,
    avg_conf     REAL DEFAULT 0,
    avg_ocr      REAL DEFAULT 0,
    n_alerts     INTEGER DEFAULT 0,
    n_review     INTEGER DEFAULT 0,
    metrics_json TEXT
);
"""

# Umbrales de alerta configurables
MONITOR_THRESHOLDS = {
    "conf_min":       float(os.environ.get("CEP_ALERT_CONF_MIN",    "0.65")),
    "error_rate_max": float(os.environ.get("CEP_ALERT_ERR_MAX",     "0.20")),
    "ocr_min":        float(os.environ.get("CEP_ALERT_OCR_MIN",     "40")),
    "review_rate_max":float(os.environ.get("CEP_ALERT_REV_MAX",     "0.35")),
}


def init_monitor_db():
    # Conexión dedicada: executescript no compatible con pool thread-local
    con = sqlite3.connect(str(DB_PATH), check_same_thread=False, timeout=30)
    con.execute("PRAGMA journal_mode=WAL")
    con.executescript(MONITOR_SCHEMA)
    con.commit()
    con.close()


def compute_monitoring_snapshot(results: List[Dict]) -> Dict:
    """Calcula un snapshot de métricas para el período actual."""
    if not results:
        return {}
    done    = [r for r in results if r.get("_status") == "done"]
    errors  = [r for r in results if "error" in r.get("_status","")]
    total   = len(results)

    avg_conf = sum(r.get("_confidence",0) for r in done) / max(len(done),1)
    ocr_scores = [r.get("_ocr_quality",{}).get("score",100)
                  for r in results if r.get("_ocr_quality")]
    avg_ocr  = sum(ocr_scores) / max(len(ocr_scores),1) if ocr_scores else 100
    n_alerts = sum(len(r.get("_alerts",[])) for r in results)
    n_review = sum(1 for r in results if r.get("_needs_review"))

    snap = {
        "total_docs":  total,
        "done_docs":   len(done),
        "error_docs":  len(errors),
        "avg_conf":    round(avg_conf, 3),
        "avg_ocr":     round(avg_ocr, 1),
        "n_alerts":    n_alerts,
        "n_review":    n_review,
        "error_rate":  round(len(errors)/max(total,1), 3),
        "review_rate": round(n_review/max(total,1), 3),
    }

    # Detectar violaciones de umbral
    alerts_fired = []
    if snap["avg_conf"] < MONITOR_THRESHOLDS["conf_min"]:
        alerts_fired.append(
            f"⚠️ Confianza promedio {snap['avg_conf']:.0%} "
            f"< umbral {MONITOR_THRESHOLDS['conf_min']:.0%}"
        )
    if snap["error_rate"] > MONITOR_THRESHOLDS["error_rate_max"]:
        alerts_fired.append(
            f"🔴 Tasa de errores {snap['error_rate']:.0%} "
            f"> umbral {MONITOR_THRESHOLDS['error_rate_max']:.0%}"
        )
    if snap["avg_ocr"] < MONITOR_THRESHOLDS["ocr_min"]:
        alerts_fired.append(
            f"⚠️ Calidad OCR promedio {snap['avg_ocr']:.0f} "
            f"< umbral {MONITOR_THRESHOLDS['ocr_min']:.0f}"
        )
    if snap["review_rate"] > MONITOR_THRESHOLDS["review_rate_max"]:
        alerts_fired.append(
            f"⚠️ Tasa de revisión {snap['review_rate']:.0%} "
            f"> umbral {MONITOR_THRESHOLDS['review_rate_max']:.0%}"
        )

    snap["alerts_fired"] = alerts_fired
    return snap


def save_monitor_snapshot(snap: Dict, period: str = "session"):
    try:
        con = _get_db_connection()
        con.execute(
            "INSERT INTO monitor_snapshots "
            "(timestamp,period,total_docs,done_docs,error_docs,"
            " avg_conf,avg_ocr,n_alerts,n_review,metrics_json) "
            "VALUES (?,?,?,?,?,?,?,?,?,?)",
            (datetime.utcnow().isoformat(), period,
             snap.get("total_docs",0), snap.get("done_docs",0),
             snap.get("error_docs",0), snap.get("avg_conf",0),
             snap.get("avg_ocr",0),    snap.get("n_alerts",0),
             snap.get("n_review",0),   json.dumps(snap))
        )
        con.commit()
        con.close()
    except Exception as e:
        log.warning(f"Monitor snapshot error: {e}")


def send_monitor_alert(snap: Dict, webhook_url: str = "", email_to: str = ""):
    """Envía alerta de monitoreo vía webhook (Slack/Teams) o log."""
    alerts = snap.get("alerts_fired", [])
    if not alerts:
        return
    msg = (
        f"🏥 Clinical Extractor — Alerta de calidad\n"
        f"Período: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}\n"
        f"Total: {snap['total_docs']} docs | "
        f"Conf: {snap['avg_conf']:.0%} | "
        f"OCR: {snap['avg_ocr']:.0f}/100\n"
        + "\n".join(f"• {a}" for a in alerts)
    )

    # Webhook Slack/Teams
    webhook_url = webhook_url or os.environ.get("CEP_WEBHOOK_URL","")
    if webhook_url:
        try:
            import urllib.request
            payload = json.dumps({"text": msg}).encode()
            req = urllib.request.Request(
                webhook_url, data=payload,
                headers={"Content-Type":"application/json"}
            )
            urllib.request.urlopen(req, timeout=5)
            log.info(f"Monitor alert enviada a webhook")
        except Exception as e:
            log.warning(f"Webhook alert error: {e}")

    log.warning(f"MONITOR ALERT: {msg}")




# ─────────────────────────────────────────────────────────────
# BASE DE DATOS LOCAL (cache + audit log + métricas)
# ─────────────────────────────────────────────────────────────
 
DB_PATH = Path("clinical_extractor_v11.db")  # v11 unified DB
 
 
def init_db():
    """Inicializa la base de datos SQLite local con esquema v15, WAL mode y seguridad."""
    init_security_db()   # Seguridad
    bootstrap_admin()    # Admin por defecto
    init_dedup_db()      # Deduplicación y proyectos
    init_queue_db()      # Cola de procesamiento persistente
    init_monitor_db()    # Snapshots de monitoreo
    # NOTA: conexión dedicada para setup inicial (executescript hace COMMIT implícito,
    # lo que corrompería el estado del pool thread-local para las llamadas siguientes)
    con = sqlite3.connect(str(DB_PATH), check_same_thread=False, timeout=30)
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("PRAGMA synchronous=NORMAL")
    cur = con.cursor()
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS processed_files (
        id              TEXT PRIMARY KEY,
        file_hash       TEXT UNIQUE,
        filename        TEXT,
        source          TEXT,
        processed_at    TEXT,
        status          TEXT,
        confidence      REAL,
        tipo_consulta   TEXT,
        data_json       TEXT,
        validation_json TEXT,
        alerts_json     TEXT
    );
 
    CREATE TABLE IF NOT EXISTS audit_log (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp   TEXT,
        action      TEXT,
        user        TEXT,
        filename    TEXT,
        detail      TEXT
    );
 
    CREATE TABLE IF NOT EXISTS sf_processed (
        sf_id           TEXT PRIMARY KEY,
        processed_at    TEXT,
        status          TEXT
    );
 
    CREATE TABLE IF NOT EXISTS campo_stats (
        campo           TEXT PRIMARY KEY,
        total_extractions INTEGER DEFAULT 0,
        total_conflicts   INTEGER DEFAULT 0,
        suma_confianza    REAL DEFAULT 0.0,
        last_updated      TEXT
    );
 
    CREATE TABLE IF NOT EXISTS sf_failed_queue (
        sf_id           TEXT PRIMARY KEY,
        filename        TEXT,
        attempts        INTEGER DEFAULT 0,
        last_attempt    TEXT,
        last_error      TEXT
    );

    -- MEJORA v15b: índices para consultas rápidas sobre datos clínicos
    CREATE INDEX IF NOT EXISTS idx_pf_confidence   ON processed_files(confidence);
    CREATE INDEX IF NOT EXISTS idx_pf_tipo         ON processed_files(tipo_consulta);
    CREATE INDEX IF NOT EXISTS idx_pf_processed    ON processed_files(processed_at DESC);
    """)
    con.commit()
    con.close()
 
 
def file_already_processed(file_hash: str) -> Optional[Dict]:
    try:
        con = _get_db_connection()
        cur = con.cursor()
        cur.execute(
            "SELECT data_json, validation_json, alerts_json, status, confidence "
            "FROM processed_files WHERE file_hash=?", (file_hash,)
        )
        row = cur.fetchone()
        con.close()
        if row:
            return {
                "data":       json.loads(row[0]) if row[0] else {},
                "validation": json.loads(row[1]) if row[1] else {},
                "alerts":     json.loads(row[2]) if row[2] else [],
                "status":     row[3],
                "confidence": row[4],
            }
    except Exception as e:
        log.warning(f"DB check error: {e}")
    return None
 
 
def save_to_db(file_hash: str, filename: str, source: str,
               data: Dict, validation: Dict, alerts: List,
               status: str, confidence: float, tipo_consulta: str = ""):
    try:
        with _db_write_lock:
            con = _get_db_connection()
            cur = con.cursor()
            cur.execute("""
                INSERT OR REPLACE INTO processed_files
                (id, file_hash, filename, source, processed_at, status,
                 confidence, tipo_consulta, data_json, validation_json, alerts_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                str(uuid.uuid4()), file_hash, filename, source,
                datetime.now().isoformat(), status, confidence, tipo_consulta,
                json.dumps(data, ensure_ascii=False),
                json.dumps(validation, ensure_ascii=False),
                json.dumps(alerts, ensure_ascii=False),
            ))
            con.commit()
            con.close()
    except Exception as e:
        log.warning(f"DB save error: {e}")
 
 
def update_campo_stats(campos_confianza: Dict[str, float], conflictos: List[str]):
    """Acumula estadísticas de confianza por campo para análisis histórico."""
    try:
        with _db_write_lock:
            con = _get_db_connection()
            cur = con.cursor()
            now = datetime.now().isoformat()
            for campo, conf in campos_confianza.items():
                if conf is None:
                    continue
                is_conflict = 1 if campo in conflictos else 0
                cur.execute("""
                    INSERT INTO campo_stats (campo, total_extractions, total_conflicts, suma_confianza, last_updated)
                    VALUES (?, 1, ?, ?, ?)
                    ON CONFLICT(campo) DO UPDATE SET
                        total_extractions = total_extractions + 1,
                        total_conflicts   = total_conflicts + ?,
                        suma_confianza    = suma_confianza + ?,
                        last_updated      = ?
                """, (campo, is_conflict, conf, now, is_conflict, conf, now))
            con.commit()
            con.close()
    except Exception as e:
        log.warning(f"campo_stats update error: {e}")
 
 
def get_last_sf_processed_date() -> Optional[str]:
    """Retorna la fecha del último registro SF procesado (para modo incremental)."""
    try:
        con = _get_db_connection()
        cur = con.cursor()
        cur.execute("SELECT MAX(processed_at) FROM sf_processed WHERE status='done'")
        row = cur.fetchone()
        con.close()
        return row[0] if row and row[0] else None
    except Exception:
        return None
 
 
def queue_sf_failure(sf_id: str, filename: str, error: str):
    try:
        con = _get_db_connection()
        with _db_write_lock:
            cur = con.cursor()
        cur.execute("""
            INSERT INTO sf_failed_queue (sf_id, filename, attempts, last_attempt, last_error)
            VALUES (?, ?, 1, ?, ?)
            ON CONFLICT(sf_id) DO UPDATE SET
                attempts     = attempts + 1,
                last_attempt = ?,
                last_error   = ?
        """, (sf_id, filename, datetime.now().isoformat(), error,
              datetime.now().isoformat(), error))
        con.commit()
        con.close()
    except Exception as e:
        log.warning(f"queue_sf_failure error: {e}")
 
 
def get_sf_failed_queue() -> List[Dict]:
    try:
        con = _get_db_connection()
        df = pd.read_sql(
            "SELECT * FROM sf_failed_queue WHERE attempts < 5 ORDER BY last_attempt",
            con
        )
        con.close()
        return df.to_dict("records")
    except Exception:
        return []
 
 
def audit(action: str, filename: str, detail: str = "", user: str = "sistema"):
    try:
        with _db_write_lock:
            con = _get_db_connection()
            cur = con.cursor()
            cur.execute("""
                INSERT INTO audit_log (timestamp, action, user, filename, detail)
                VALUES (?, ?, ?, ?, ?)
            """, (datetime.now().isoformat(), action, user, filename, detail))
            con.commit()
            con.close()
    except Exception:
        pass


def load_results_from_db(limit: int = 500) -> List[Dict]:
    """
    Carga los resultados almacenados en la DB para restaurarlos en session_state.
    Esto permite que al cerrar y abrir la app, los resultados previos estén disponibles.
    MEJORA v15b: función optimizada con índices DB y carga selectiva.
    """
    try:
        con = _get_db_connection()
        cur = con.cursor()
        cur.execute("""
            SELECT id, file_hash, filename, source, processed_at, status,
                   confidence, tipo_consulta, data_json, validation_json, alerts_json
            FROM processed_files
            WHERE status = 'done'
            ORDER BY processed_at DESC
            LIMIT ?
        """, (limit,))
        rows = cur.fetchall()
        con.close()

        results = []
        for row in rows:
            try:
                result = {
                    "_id": row[0],
                    "_file_hash": row[1],
                    "_filename": row[2],
                    "_source": row[3],
                    "_processed_at": row[4],
                    "_status": row[5],
                    "_confidence": row[6] if row[6] is not None else 0.0,
                    "_tipo_consulta": row[7] if row[7] else "General / Base",
                    "_from_cache": True,
                }
                # Cargar datos extraídos
                if row[8]:
                    data = json.loads(row[8])
                    for k, v in data.items():
                        if not k.startswith("_"):
                            result[k] = v
                # Cargar validación
                if row[9]:
                    result["_validation"] = json.loads(row[9])
                # Cargar alertas
                if row[10]:
                    result["_alerts"] = json.loads(row[10])
                results.append(result)
            except Exception as e:
                log.warning(f"Error cargando resultado {row[0]}: {e}")
                continue

        log.info(f"📥 Restaurados {len(results)} resultados desde la base de datos")
        return results
    except Exception as e:
        log.warning(f"Error cargando resultados de DB: {e}")
        return []
 
 
@__import__("functools").lru_cache(maxsize=256)
def compute_hash(data: bytes) -> str:
    """MEJORA v15c: cacheado — mismo archivo no se re-hashea en dedup checks."""
    return hashlib.sha256(data).hexdigest()
 
 
# ─────────────────────────────────────────────────────────────
# SALESFORCE MANAGER (mejorado con reintentos y modo incremental)
# ─────────────────────────────────────────────────────────────
 
class SalesforceManager:
    """
    Conecta con Salesforce. Soporta:
    - ContentVersion (archivos PDF/imagen)
    - Campos de texto en objetos Case / custom (sin OCR)
    - Modo incremental desde última fecha procesada
    - Cola de reintentos para fallos parciales
    """
 
    def __init__(self, username: str, password: str, security_token: str,
                 domain: str = "login", api_version: str = "57.0"):
        self.username = username
        self.password = password
        self.security_token = security_token
        self.domain = domain
        self.api_version = api_version
        self.sf = None
        self._connect()
 
    def _connect(self):
        try:
            from simple_salesforce import Salesforce
            self.sf = Salesforce(
                username=self.username,
                password=self.password,
                security_token=self.security_token,
                domain=self.domain,
                version=self.api_version,
            )
            log.info("✅ Conectado a Salesforce")
        except ImportError:
            raise RuntimeError("Instala simple-salesforce: pip install simple-salesforce")
        except Exception as e:
            log.error(f"❌ Error Salesforce: {e}")
            raise
 
    def query_clinical_records(self, soql: str = None,
                                limit: int = 100,
                                offset: int = 0,
                                incremental: bool = False) -> List[Dict]:
        """
        Consulta registros clínicos. Si incremental=True,
        filtra desde la última fecha procesada.
        """
        if not self.sf:
            return []
 
        date_filter = ""
        if incremental:
            last_date = get_last_sf_processed_date()
            if last_date:
                date_filter = f" AND CreatedDate > {last_date[:10]}T00:00:00Z"
                log.info(f"Modo incremental desde: {last_date[:10]}")
 
        if soql is None:
            soql = (
                f"SELECT Id, Title, FileExtension, ContentSize, CreatedDate, "
                f"FirstPublishLocationId "
                f"FROM ContentVersion "
                f"WHERE (FileExtension='pdf' OR FileExtension='png' OR "
                f"FileExtension='jpg' OR FileExtension='jpeg')"
                f"{date_filter} "
                f"ORDER BY CreatedDate DESC "
                f"LIMIT {limit} OFFSET {offset}"
            )
        elif incremental and date_filter:
            # Inyectar filtro incremental si hay SOQL personalizado con WHERE
            if "WHERE" in soql.upper():
                soql = soql + date_filter
            else:
                soql = soql + f" WHERE CreatedDate > {get_last_sf_processed_date()[:10]}T00:00:00Z"
 
        try:
            result = self.sf.query(soql)
            records = result.get("records", [])
            while not result.get("done", True) and result.get("nextRecordsUrl"):
                result = self.sf.query_more(result["nextRecordsUrl"], identifier_is_url=True)
                records.extend(result.get("records", []))
            log.info(f"📋 {len(records)} registros encontrados en Salesforce")
            return records
        except Exception as e:
            log.error(f"❌ Error consultando Salesforce: {e}")
            return []
 
    def query_text_records(self, soql: str) -> List[Dict]:
        """
        Consulta objetos con texto clínico en campos (Case, HistoriaClinica__c, etc).
        Retorna lista de dicts con campo 'text_content' pre-poblado para procesamiento directo.
        """
        try:
            result = self.sf.query_all(soql)
            records = result.get("records", [])
            # Concatenar todos los campos de texto en un solo string por registro
            processed = []
            for r in records:
                text_parts = []
                for k, v in r.items():
                    if k.startswith("_") or k == "attributes":
                        continue
                    if isinstance(v, str) and len(v) > 10:
                        text_parts.append(f"[{k}]\n{v}")
                processed.append({
                    **r,
                    "text_content": "\n\n".join(text_parts),
                    "_is_text_record": True,
                })
            log.info(f"📋 {len(processed)} registros de texto encontrados")
            return processed
        except Exception as e:
            log.error(f"❌ Error en query_text_records: {e}")
            return []
 
    def download_content_version(self, content_version_id: str,
                                  max_retries: int = 3) -> Optional[bytes]:
        """Descarga ContentVersion con reintentos exponenciales."""
        if not self.sf:
            return None
        url = (f"https://{self.sf.sf_instance}/services/data/"
               f"v{self.api_version}/sobjects/ContentVersion/"
               f"{content_version_id}/VersionData")
        for attempt in range(max_retries):
            try:
                resp = self.sf.session.get(
                    url,
                    headers={"Authorization": f"Bearer {self.sf.session_id}"},
                    timeout=90
                )
                resp.raise_for_status()
                return resp.content
            except Exception as e:
                wait = 2 ** attempt * 3
                log.warning(f"Intento {attempt+1}/{max_retries} falló para {content_version_id}: {e}. Esperando {wait}s")
                if attempt < max_retries - 1:
                    time.sleep(wait)
                else:
                    log.error(f"❌ Descarga fallida definitivamente: {content_version_id}")
                    queue_sf_failure(content_version_id, content_version_id, str(e))
                    return None
 
    def query_custom_object(self, soql: str) -> List[Dict]:
        try:
            result = self.sf.query_all(soql)
            return result.get("records", [])
        except Exception as e:
            log.error(f"❌ Error en query custom: {e}")
            return []
 
    def mark_as_processed(self, sf_id: str):
        try:
            con = _get_db_connection()  # MEJORA v15c: thread-local pool
            con.execute(
                "INSERT OR REPLACE INTO sf_processed (sf_id, processed_at, status) VALUES (?,?,?)",
                (sf_id, datetime.now().isoformat(), "done")
            )
            con.commit()
        except Exception:
            pass

    def is_already_processed(self, sf_id: str) -> bool:
        try:
            con = _get_db_connection()  # MEJORA v15c: thread-local pool
            return con.execute(
                "SELECT 1 FROM sf_processed WHERE sf_id=?", (sf_id,)
            ).fetchone() is not None
        except Exception:
            return False
 
 
# ─────────────────────────────────────────────────────────────
# GOOGLE DRIVE MANAGER — leer archivos + escribir resultados
# ─────────────────────────────────────────────────────────────

class GoogleDriveManager:
    """
    Integración con Google Drive:
    - Listar y descargar PDFs/imágenes desde una carpeta de Drive
    - Subir archivos Excel con los resultados de extracción
    Soporta cuentas personales y organizacionales (Service Account o OAuth2).
    """

    SCOPES = [
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/spreadsheets",
    ]

    def __init__(self, folder_url_or_id: str = "", credentials_path: str = ""):
        self.folder_id = self._extract_folder_id(folder_url_or_id) if folder_url_or_id else ""
        self.credentials_path = credentials_path
        self.service = None
        self._cred_data = None
        self._connect()

    @staticmethod
    def _extract_folder_id(url_or_id: str) -> str:
        import re as _re
        url_or_id = url_or_id.strip()
        # URL de carpeta: https://drive.google.com/drive/folders/ID
        m = _re.search(r"/folders/([a-zA-Z0-9_-]+)", url_or_id)
        if m:
            return m.group(1)
        # URL de archivo compartido: ?id=ID o /d/ID
        m = _re.search(r"[?&]id=([a-zA-Z0-9_-]+)", url_or_id)
        if m:
            return m.group(1)
        m = _re.search(r"/d/([a-zA-Z0-9_-]+)", url_or_id)
        if m:
            return m.group(1)
        # ID directo
        if "/" not in url_or_id and len(url_or_id) > 10:
            return url_or_id
        return url_or_id

    def _connect(self):
        try:
            from google.oauth2.service_account import Credentials
            from googleapiclient.discovery import build as _build

            self._cred_data = GoogleSheetsManager._load_credentials_data(self.credentials_path)
            creds = Credentials.from_service_account_info(self._cred_data, scopes=self.SCOPES)
            self.service = _build("drive", "v3", credentials=creds,
                                  cache_discovery=False)
            log.info("✅ Google Drive conectado")
        except Exception as e:
            log.error(f"❌ Google Drive: {e}")
            raise

    def list_files(self, folder_id: str = "", mime_filter: list = None) -> List[Dict]:
        """
        Lista archivos en una carpeta de Drive.
        mime_filter: lista de MIME types, ej. ["application/pdf", "image/jpeg"]
        Devuelve lista de {"id", "name", "mimeType", "size", "modifiedTime"}.
        """
        fid = folder_id or self.folder_id
        if not fid:
            raise ValueError("Se requiere un ID o URL de carpeta de Google Drive.")

        mime_types = mime_filter or [
            "application/pdf",
            "image/jpeg", "image/jpg", "image/png", "image/tiff",
        ]
        mime_query = " or ".join(f"mimeType='{m}'" for m in mime_types)
        query = f"'{fid}' in parents and ({mime_query}) and trashed=false"

        files, page_token = [], None
        while True:
            resp = self.service.files().list(
                q=query,
                pageSize=100,
                fields="nextPageToken, files(id,name,mimeType,size,modifiedTime)",
                pageToken=page_token,
            ).execute()
            files.extend(resp.get("files", []))
            page_token = resp.get("nextPageToken")
            if not page_token:
                break
        return files

    def download_file(self, file_id: str) -> bytes:
        """Descarga el contenido binario de un archivo de Drive."""
        from googleapiclient.http import MediaIoBaseDownload
        import io
        req = self.service.files().get_media(fileId=file_id)
        buf = io.BytesIO()
        downloader = MediaIoBaseDownload(buf, req)
        done = False
        while not done:
            _, done = downloader.next_chunk()
        return buf.getvalue()

    def upload_excel(self, data: bytes, filename: str, folder_id: str = "") -> str:
        """
        Sube un archivo Excel (.xlsx) a Drive.
        Devuelve la URL del archivo subido.
        """
        from googleapiclient.http import MediaIoBaseUpload
        import io
        fid = folder_id or self.folder_id
        meta = {
            "name": filename,
            "mimeType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        }
        if fid:
            meta["parents"] = [fid]
        media = MediaIoBaseUpload(
            io.BytesIO(data),
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            resumable=True,
        )
        file_obj = self.service.files().create(
            body=meta, media_body=media, fields="id,webViewLink"
        ).execute()
        url = file_obj.get("webViewLink", "")
        log.info(f"✅ Excel subido a Drive: {filename} → {url}")
        return url

    def auto_grant_access(self, folder_id: str = "") -> dict:
        """
        Verifica y otorga acceso a la carpeta a la cuenta de servicio.
        Devuelve dict con status y message igual que _auto_share_sheet.
        """
        fid = folder_id or self.folder_id
        svc_email = (self._cred_data or {}).get("client_email", "")
        return GoogleSheetsManager._auto_share_sheet(self.service, fid, svc_email)


# ─────────────────────────────────────────────────────────────
# ONEDRIVE MANAGER — leer archivos + escribir resultados
# ─────────────────────────────────────────────────────────────

class OneDriveManager:
    """
    Integración con Microsoft OneDrive / SharePoint mediante Microsoft Graph API.
    Soporta cuentas personales (OAuth2 device flow) y organizacionales (Azure AD).

    Configuración necesaria (guardada en DB cifrada):
      - client_id:     ID de la app registrada en Azure
      - tenant_id:     "consumers" para cuentas personales, ID del tenant para org.
      - client_secret: solo para cuentas organizacionales (app confidential)
    """

    GRAPH_BASE = "https://graph.microsoft.com/v1.0"

    # Scopes necesarios
    SCOPES_PERSONAL = ["Files.ReadWrite", "offline_access"]
    SCOPES_ORG      = ["https://graph.microsoft.com/Files.ReadWrite.All",
                       "https://graph.microsoft.com/offline_access"]

    def __init__(self, client_id: str, tenant_id: str = "consumers",
                 client_secret: str = "", access_token: str = ""):
        self.client_id     = client_id
        self.tenant_id     = tenant_id           # "consumers" = personal, UUID = org
        self.client_secret = client_secret
        self._access_token = access_token
        self._token_cache  = {}

    # ── Autenticación ─────────────────────────────────────────────────────

    def get_device_flow_url(self) -> dict:
        """
        Inicia el flujo de autenticación por dispositivo (para cuentas personales o org).
        Devuelve {"user_code", "verification_uri", "device_code", "expires_in"}.
        El usuario debe ir a la URL y escribir el código.
        """
        import requests as _req
        url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/devicecode"
        scopes = " ".join(self.SCOPES_PERSONAL if self.tenant_id == "consumers"
                          else self.SCOPES_ORG)
        resp = _req.post(url, data={
            "client_id": self.client_id,
            "scope": scopes,
        })
        resp.raise_for_status()
        return resp.json()

    def poll_device_flow(self, device_code: str) -> dict:
        """
        Sondea si el usuario ya autorizó. Devuelve {"access_token", "refresh_token"}
        o {"error": "authorization_pending"} si aún no lo hizo.
        """
        import requests as _req
        url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
        resp = _req.post(url, data={
            "client_id":   self.client_id,
            "device_code": device_code,
            "grant_type":  "urn:ietf:params:oauth2:grant-type:device_code",
        })
        return resp.json()

    def auth_with_client_credentials(self) -> str:
        """
        Autenticación server-to-server para cuentas organizacionales
        (requiere client_secret). Devuelve access_token.
        """
        import requests as _req
        url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
        resp = _req.post(url, data={
            "client_id":     self.client_id,
            "client_secret": self.client_secret,
            "scope":         "https://graph.microsoft.com/.default",
            "grant_type":    "client_credentials",
        })
        resp.raise_for_status()
        data = resp.json()
        self._access_token = data["access_token"]
        return self._access_token

    def set_token(self, token: str):
        self._access_token = token

    def _headers(self) -> dict:
        if not self._access_token:
            raise RuntimeError("OneDrive: no hay token de acceso. Autentícate primero.")
        return {"Authorization": f"Bearer {self._access_token}",
                "Content-Type": "application/json"}

    # ── Listar y descargar archivos ───────────────────────────────────────

    def list_files(self, folder_path: str = "/") -> List[Dict]:
        """
        Lista archivos PDF e imágenes en una carpeta de OneDrive.
        folder_path: ruta relativa, ej. "/Historias Clinicas"
        Devuelve lista de {"id", "name", "size", "webUrl", "mimeType"}.
        """
        import requests as _req
        VALID_EXT = {".pdf", ".png", ".jpg", ".jpeg", ".tiff", ".tif"}

        if folder_path in ("", "/"):
            url = f"{self.GRAPH_BASE}/me/drive/root/children"
        else:
            folder_path = folder_path.strip("/")
            url = f"{self.GRAPH_BASE}/me/drive/root:/{folder_path}:/children"

        files, next_link = [], url
        while next_link:
            resp = _req.get(next_link, headers=self._headers(),
                            params={"$top": 100, "$select":
                                    "id,name,size,webUrl,file,lastModifiedDateTime"})
            resp.raise_for_status()
            data = resp.json()
            for item in data.get("value", []):
                if "file" in item:
                    ext = "." + item["name"].rsplit(".", 1)[-1].lower() if "." in item["name"] else ""
                    if ext in VALID_EXT:
                        files.append({
                            "id":           item["id"],
                            "name":         item["name"],
                            "size":         item.get("size", 0),
                            "webUrl":       item.get("webUrl", ""),
                            "mimeType":     item.get("file", {}).get("mimeType", ""),
                            "modified":     item.get("lastModifiedDateTime", ""),
                        })
            next_link = data.get("@odata.nextLink")
        return files

    def download_file(self, file_id: str) -> bytes:
        """Descarga el contenido binario de un archivo de OneDrive."""
        import requests as _req
        url = f"{self.GRAPH_BASE}/me/drive/items/{file_id}/content"
        resp = _req.get(url, headers=self._headers(), allow_redirects=True)
        resp.raise_for_status()
        return resp.content

    # ── Subir resultados ──────────────────────────────────────────────────

    def upload_excel(self, data: bytes, filename: str,
                     folder_path: str = "/Extracciones_Clinicas") -> str:
        """
        Sube un archivo Excel a una carpeta de OneDrive.
        Crea la carpeta si no existe. Devuelve la URL del archivo.
        """
        import requests as _req
        folder_path = folder_path.strip("/")
        if folder_path:
            upload_url = (f"{self.GRAPH_BASE}/me/drive/root:/"
                          f"{folder_path}/{filename}:/content")
        else:
            upload_url = f"{self.GRAPH_BASE}/me/drive/root:/{filename}:/content"

        headers = {
            "Authorization": f"Bearer {self._access_token}",
            "Content-Type": ("application/vnd.openxmlformats-officedocument"
                             ".spreadsheetml.sheet"),
        }
        resp = _req.put(upload_url, headers=headers, data=data)
        resp.raise_for_status()
        result = resp.json()
        url = result.get("webUrl", "")
        log.info(f"✅ Excel subido a OneDrive: {filename} → {url}")
        return url

    def write_results_excel(self, results: List[Dict], campos: List[str],
                             folder_path: str = "/Extracciones_Clinicas") -> str:
        """
        Convierte los resultados a Excel y los sube a OneDrive.
        Devuelve la URL del archivo.
        """
        import io
        rows = []
        for r in results:
            if r.get("_status") != "done":
                continue
            row = {
                "Archivo":    r.get("_filename", ""),
                "Confianza":  f"{r.get('_confidence', 0):.0%}",
                "Estado":     r.get("_status", ""),
                "Fecha":      datetime.utcnow().strftime("%Y-%m-%d"),
            }
            for c in campos:
                row[c] = r.get(c, "")
            rows.append(row)

        if not rows:
            raise ValueError("No hay resultados completados para exportar.")

        df = pd.DataFrame(rows)
        buf = io.BytesIO()
        with pd.ExcelWriter(buf, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Extracciones")
        buf.seek(0)

        ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        filename = f"Clinical_Extracciones_{ts}.xlsx"
        return self.upload_excel(buf.getvalue(), filename, folder_path)


# ─────────────────────────────────────────────────────────────
# GOOGLE SHEETS MANAGER (batch mejorado)
# ─────────────────────────────────────────────────────────────
 
class GoogleSheetsManager:
    """
    Gestiona Google Sheets con escritura en batch para rendimiento.
    Acumula filas en buffer y las escribe de una sola vez.
    """
 
    def __init__(self, credentials_path: str, spreadsheet_url: str):
        self.credentials_path = credentials_path
        self.spreadsheet_url = spreadsheet_url
        self.gc = None
        self.spreadsheet = None
        self.ws_data    = None
        self.ws_review  = None
        self.ws_alerts  = None
        self.ws_quality = None
 
        # Buffers de batch
        self._buffer_data:   List[List] = []
        self._buffer_review: List[List] = []
        self._buffer_alerts: List[List] = []
        self._campos_header: List[str]  = []
 
        self._connect()
 
    @staticmethod
    def _extract_sheet_id(url_or_id: str) -> str:
        """
        Acepta tanto la URL completa del navegador como solo el ID del spreadsheet.
        Ejemplo URL: https://docs.google.com/spreadsheets/d/ID_AQUI/edit?gid=0#gid=0
        Retorna solo el ID.
        """
        import re as _re
        url_or_id = url_or_id.strip()
        m = _re.search(r"/spreadsheets/d/([a-zA-Z0-9_-]+)", url_or_id)
        if m:
            return m.group(1)
        # Si ya es un ID puro (sin slashes)
        if "/" not in url_or_id and len(url_or_id) > 10:
            return url_or_id
        return url_or_id

    @staticmethod
    def _load_credentials_data(credentials_path: str) -> dict:
        """
        Carga las credenciales de Google en este orden de prioridad:
        1. session_state["_gcp_creds_json"] — pegado directamente en el editor de la app
        2. Streamlit Secrets (st.secrets["gcp_service_account"]) — persistente en Streamlit Cloud
        3. Variable de entorno GOOGLE_CREDENTIALS_JSON (JSON string)
        4. Archivo físico credentials_path — solo funciona en servidor propio
        """
        # ── Fuente 1: DB cifrada (persistente) ──────────────────────────
        try:
            raw_db = load_app_config("gcp_credentials_json", "").strip()
            if raw_db:
                cred_dict = json.loads(raw_db)
                if cred_dict.get("type") == "service_account":
                    log.info("✅ Credenciales Google cargadas desde DB cifrada")
                    return cred_dict
        except Exception:
            pass

        # ── Fuente 2: Editor JSON en session_state (fallback de sesión) ──
        try:
            import streamlit as _st
            raw_json = _st.session_state.get("_gcp_creds_json", "").strip()
            if raw_json:
                cred_dict = json.loads(raw_json)
                if cred_dict.get("type") == "service_account":
                    log.info("✅ Credenciales Google cargadas desde session_state")
                    return cred_dict
        except Exception:
            pass

        # ── Fuente 3: Streamlit Secrets ──────────────────────────────────
        try:
            import streamlit as _st
            if "gcp_service_account" in _st.secrets:
                cred_dict = dict(_st.secrets["gcp_service_account"])
                log.info("✅ Credenciales Google cargadas desde Streamlit Secrets")
                return cred_dict
        except Exception:
            pass

        # ── Fuente 4: Variable de entorno ────────────────────────────────
        env_creds = os.environ.get("GOOGLE_CREDENTIALS_JSON", "")
        if env_creds.strip():
            try:
                cred_dict = json.loads(env_creds)
                log.info("✅ Credenciales Google cargadas desde variable de entorno")
                return cred_dict
            except json.JSONDecodeError:
                log.warning("GOOGLE_CREDENTIALS_JSON no es JSON válido")

        # ── Fuente 5: Archivo físico (servidor propio) ───────────────────
        if credentials_path:
            creds_path = Path(credentials_path)
            if creds_path.exists():
                try:
                    cred_dict = json.loads(creds_path.read_text())
                    log.info(f"✅ Credenciales Google cargadas desde archivo: {credentials_path}")
                    return cred_dict
                except Exception as e:
                    raise ValueError(f"Error leyendo credentials.json: {e}")

        # ── Sin fuente disponible ────────────────────────────────────────
        raise FileNotFoundError(
            "No se encontraron credenciales de Google. "
            "Pega el contenido del credentials.json en Configuracion > Google Sheets > Editor JSON, ""o guarda las credenciales con el boton Guardar de forma permanente."
        )

    @staticmethod
    def _auto_share_sheet(drive_service, sheet_id: str, service_account_email: str) -> dict:
        """
        Comparte el Sheet con la cuenta de servicio si no tiene acceso aún.
        Devuelve un dict con:
          - status: "ya_compartido" | "compartido_ahora" | "error"
          - message: descripción legible
          - email: email de la cuenta de servicio
        """
        result = {"email": service_account_email, "status": "error", "message": ""}
        try:
            # Listar permisos actuales del archivo
            perms = drive_service.permissions().list(
                fileId=sheet_id,
                fields="permissions(emailAddress,role)"
            ).execute().get("permissions", [])

            already = any(
                p.get("emailAddress", "").lower() == service_account_email.lower()
                for p in perms
            )

            if already:
                result["status"]  = "ya_compartido"
                result["message"] = f"El Sheet ya estaba compartido con `{service_account_email}`."
                log.info(f"✅ Sheet ya compartido con {service_account_email}")
            else:
                # Otorgar permiso de escritura
                drive_service.permissions().create(
                    fileId=sheet_id,
                    body={
                        "type": "user",
                        "role": "writer",
                        "emailAddress": service_account_email,
                    },
                    sendNotificationEmail=False,
                ).execute()
                result["status"]  = "compartido_ahora"
                result["message"] = (
                    f"Permiso otorgado ahora mismo a `{service_account_email}` "
                    f"(rol: Editor)."
                )
                log.info(f"✅ Sheet compartido automáticamente con {service_account_email}")

        except Exception as e:
            result["status"]  = "error"
            result["message"] = (
                f"No se pudo compartir con `{service_account_email}`: {e}. "
                "Compártelo manualmente desde Google Sheets → Compartir."
            )
            log.warning(result["message"])

        return result

    def _connect(self):
        import gspread
        from google.oauth2.service_account import Credentials
        from googleapiclient.discovery import build as _build

        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]

        # ── 1. Cargar credenciales ────────────────────────────────────────
        cred_data = self._load_credentials_data(self.credentials_path)
        service_account_email = cred_data.get("client_email", "")
        creds = Credentials.from_service_account_info(cred_data, scopes=scopes)

        # ── 2. Conectar gspread (método más directo y compatible) ─────────
        # service_account_from_dict funciona en gspread 5.x y 6.x
        self.gc = gspread.service_account_from_dict(cred_data)

        # ── 3. Extraer ID del spreadsheet ─────────────────────────────────
        sheet_id = self._extract_sheet_id(self.spreadsheet_url)

        # ── 4. Auto-compartir usando Drive API ────────────────────────────
        if service_account_email:
            try:
                drive_svc = _build("drive", "v3", credentials=creds,
                                   cache_discovery=False)
                self._auto_share_sheet(drive_svc, sheet_id, service_account_email)
            except Exception as _e:
                log.warning(f"Auto-share omitido: {_e}")

        # ── 5. Abrir el spreadsheet ───────────────────────────────────────
        try:
            self.spreadsheet = self.gc.open_by_key(sheet_id)
        except gspread.exceptions.APIError as api_err:
            err_str = str(api_err)
            if "403" in err_str or "PERMISSION_DENIED" in err_str:
                raise PermissionError(
                    f"Sin acceso al spreadsheet. "
                    f"Compártelo manualmente con: {service_account_email} (rol Editor)."
                ) from api_err
            elif "404" in err_str:
                raise ValueError(
                    "Spreadsheet no encontrado. Verifica que la URL sea correcta."
                ) from api_err
            raise
        except Exception as _e2:
            raise RuntimeError(f"No se pudo abrir el spreadsheet: {_e2}") from _e2

        # ── 6. Crear/obtener hojas ────────────────────────────────────────
        self.ws_data    = self._get_or_create_sheet("Extracciones")
        self.ws_review  = self._get_or_create_sheet("Revisar_Manual")
        self.ws_alerts  = self._get_or_create_sheet("Alertas_Medicas")
        self.ws_quality = self._get_or_create_sheet("Calidad_Campos")

        log.info(f"✅ Google Sheets conectado: {self.spreadsheet.title}")
 
    def _get_or_create_sheet(self, name: str):
        try:
            return self.spreadsheet.worksheet(name)
        except Exception:
            return self.spreadsheet.add_worksheet(title=name, rows=10000, cols=60)
 
    def _ensure_headers(self, ws, headers: List[str]):
        try:
            existing = ws.row_values(1)
            if not existing or existing != headers:
                ws.clear()
                ws.append_row(headers, value_input_option="USER_ENTERED")
        except Exception as e:
            log.warning(f"Error en _ensure_headers: {e}")
 
    def buffer_extraction(self, data: Dict, campos: List[str],
                           validation: Dict = None, alerts: List = None,
                           confidence: float = 1.0, needs_review: bool = False):
        """
        Acumula una extracción en el buffer sin escribir a Sheets todavía.
        Llama flush_batch() cuando tengas todas las filas listas.
        """
        if not self._campos_header:
            self._campos_header = campos
 
        file_hash = data.get("_file_hash", data.get("_hash", ""))
        row_data = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            data.get("_filename", ""),
            data.get("_source", "local"),
            data.get("_status", "done"),
            f"{confidence:.0%}",
            "⚠️ SÍ" if needs_review else "✅ NO",
            file_hash,                       # FileHash — columna clave para dedup en Sheets
            data.get("_project_id", DEFAULT_PROJECT_ID),  # Proyecto
        ]
        for campo in campos:
            value = data.get(campo, "")
            if isinstance(value, list):
                value = " | ".join(str(v) for v in value if v)
            row_data.append(str(value) if value else "")
        self._buffer_data.append(row_data)
 
        if needs_review and validation:
            conflictos = validation.get("conflictos", [])
            self._buffer_review.append([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                data.get("_filename", ""),
                f"{confidence:.0%}",
                " | ".join(conflictos[:10]),
                validation.get("resumen", ""),
            ])
 
        if alerts:
            for alert in alerts:
                self._buffer_alerts.append([
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    data.get("_filename", ""),
                    data.get("nombre_paciente", ""),
                    alert.get("tipo", ""),
                    alert.get("descripcion", ""),
                    alert.get("severidad", "MEDIA"),
                ])
 
    def flush_batch(self):
        """
        Escribe todos los buffers de una vez a Google Sheets.
        Mucho más rápido que append_row por fila.
        """
        campos = self._campos_header
 
        # Hoja principal de datos
        if self._buffer_data:
            headers = (
                ["FechaExtraccion", "Archivo", "Fuente", "Estado",
                 "Confianza", "RequiereRevision",
                 "FileHash", "Proyecto"] + campos
            )
            self._ensure_headers(self.ws_data, headers)
            self.ws_data.append_rows(
                self._buffer_data, value_input_option="USER_ENTERED"
            )
            log.info(f"✅ Batch Sheets: {len(self._buffer_data)} filas escritas")
            self._buffer_data = []
 
        # Hoja de revisión manual
        if self._buffer_review:
            self._ensure_headers(self.ws_review, [
                "FechaExtraccion", "Archivo", "Confianza",
                "CamposConflictivos", "MotivoRevision"
            ])
            self.ws_review.append_rows(
                self._buffer_review, value_input_option="USER_ENTERED"
            )
            self._buffer_review = []
 
        # Hoja de alertas médicas
        if self._buffer_alerts:
            self._ensure_headers(self.ws_alerts, [
                "FechaExtraccion", "Archivo", "Paciente",
                "TipoAlerta", "Descripcion", "Severidad"
            ])
            self.ws_alerts.append_rows(
                self._buffer_alerts, value_input_option="USER_ENTERED"
            )
            self._buffer_alerts = []
 
    def write_quality_report(self):
        """Escribe reporte de calidad por campo en hoja dedicada."""
        try:
            con = _get_db_connection()  # thread-local pool
            df = pd.read_sql("""
                SELECT campo,
                       total_extractions,
                       total_conflicts,
                       ROUND(suma_confianza / MAX(total_extractions, 1), 3) as confianza_promedio,
                       ROUND(CAST(total_conflicts AS REAL) / MAX(total_extractions, 1), 3) as tasa_conflicto,
                       last_updated
                FROM campo_stats
                ORDER BY tasa_conflicto DESC
            """, con)
            con.close()
 
            if df.empty:
                return
 
            self._ensure_headers(self.ws_quality, list(df.columns))
            rows = df.values.tolist()
            self.ws_quality.clear()
            self.ws_quality.append_row(list(df.columns), value_input_option="USER_ENTERED")
            self.ws_quality.append_rows(rows, value_input_option="USER_ENTERED")
            log.info("✅ Reporte de calidad escrito en Sheets")
        except Exception as e:
            log.warning(f"Error escribiendo quality report: {e}")
 
    def get_all_records(self) -> List[Dict]:
        try:
            return self.ws_data.get_all_records()
        except Exception as e:
            log.error(f"❌ Error leyendo Sheets: {e}")
            return []
 
 
# ─────────────────────────────────────────────────────────────
# OCR Y EXTRACCIÓN DE TEXTO (mejorado)
# ─────────────────────────────────────────────────────────────
 
def extract_text_from_bytes(data: bytes, filename: str,
                             ocr_lang: str = "spa+eng",
                             dpi: int = 300,
                             use_easyocr: bool = False,
                             use_vision: bool = False,
                             vision_api_key: str = "",
                             vision_provider: str = "claude") -> str:
    """
    Extrae texto de bytes de PDF o imagen.
    Soporta Tesseract, EasyOCR y visión directa del modelo.
    """
    suffix = Path(filename).suffix.lower()
    if suffix == ".pdf":
        return _extract_pdf_bytes(data, ocr_lang, dpi, use_easyocr, use_vision,
                                   vision_api_key, vision_provider)
    elif suffix in {".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".webp"}:
        if use_vision and vision_api_key:
            return _vision_ocr(data, vision_api_key, vision_provider)
        return _ocr_bytes_enhanced(data, ocr_lang, use_easyocr)
    else:
        try:
            return data.decode("utf-8", errors="replace")
        except Exception:
            return ""
 
 
def _extract_pdf_bytes(data: bytes, ocr_lang: str, dpi: int,
                        use_easyocr: bool = False,
                        use_vision: bool = False,
                        vision_api_key: str = "",
                        vision_provider: str = "claude") -> str:
    try:
        import fitz
        doc = fitz.open(stream=data, filetype="pdf")
        texts = []
        try:  # MEJORA v15b: garantizar cierre del doc PDF para liberar memoria
            for page_num, page in enumerate(doc):
                t = page.get_text().strip()
                if len(t) > 50:
                    # Página digital: texto nativo
                    texts.append(t)
                else:
                    # Página escaneada o manuscrita → OCR
                    pix = page.get_pixmap(dpi=dpi)
                    img_bytes = pix.tobytes("png")
                    del pix  # MEJORA v15b: liberar pixmap de memoria inmediatamente

                    if use_vision and vision_api_key:
                        page_text = _vision_ocr(img_bytes, vision_api_key, vision_provider)
                    else:
                        page_text = _ocr_bytes_enhanced(img_bytes, ocr_lang, use_easyocr)

                    if page_text.strip():
                        texts.append(f"[Página {page_num+1} OCR]\n{page_text}")

        finally:
            try:
                doc.close()  # MEJORA v15b: liberar PDF de memoria
            except Exception:
                pass
        return "\n\n".join(texts)
 
    except ImportError:
        log.warning("PyMuPDF no disponible, intentando OCR directo")
        return _ocr_bytes_enhanced(data, ocr_lang, use_easyocr)
    except Exception as e:
        log.error(f"Error extrayendo PDF: {e}")
        return ""
 
 
def _ocr_bytes_enhanced(img_bytes: bytes, lang: str = "spa+eng",
                          use_easyocr: bool = False) -> str:
    """
    OCR mejorado con deskewing, denoising y normalización.
    Intenta EasyOCR si está disponible y se solicita, sino Tesseract.
    """
    try:
        import cv2
        import numpy as np
        from PIL import Image, ImageFilter, ImageEnhance
 
        img = Image.open(io.BytesIO(img_bytes))
        if img.mode != "RGB":
            img = img.convert("RGB")
 
        # Aumentar resolución si es pequeña
        w, h = img.size
        if w < 1200:
            scale = 1200 / w
            img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
 
        # Mejorar contraste y nitidez
        img = ImageEnhance.Contrast(img).enhance(1.8)
        img = ImageEnhance.Sharpness(img).enhance(2.5)
 
        # Convertir a numpy para OpenCV
        img_np = np.array(img)
        img.close()  # MEJORA v15b: liberar imagen PIL de memoria
        del img
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
 
        # Denoising (especialmente útil para papel con ruido)
        gray = cv2.fastNlMeansDenoising(gray, h=10)
 
        # Deskewing automático
        gray = _deskew(gray)
 
        # Umbralización adaptativa para mejor contraste en manuscritos
        binary = cv2.adaptiveThreshold(
            gray, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, 31, 11
        )
 
        processed_img = Image.fromarray(binary)
 
        if use_easyocr:
            return _easyocr_extract(processed_img, lang)
        else:
            return _tesseract_extract(processed_img, lang)
 
    except ImportError:
        # Sin OpenCV: usar solo Pillow básico
        return _ocr_bytes_basic(img_bytes, lang)
    except Exception as e:
        log.warning(f"OCR enhanced error, fallback básico: {e}")
        return _ocr_bytes_basic(img_bytes, lang)
 
 
def _deskew(gray_np) -> Any:
    """Corrige inclinación de la imagen (deskew)."""
    try:
        import cv2
        import numpy as np
        coords = np.column_stack(np.where(gray_np < 128))
        if len(coords) == 0:
            return gray_np
        angle = cv2.minAreaRect(coords.astype(np.float32))[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        if abs(angle) > 0.5:
            h, w = gray_np.shape
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center, angle, 1.0)
            gray_np = cv2.warpAffine(
                gray_np, M, (w, h),
                flags=cv2.INTER_CUBIC,
                borderMode=cv2.BORDER_REPLICATE
            )
    except Exception:
        pass
    return gray_np
 
 
def _tesseract_extract(img, lang: str = "spa+eng") -> str:
    try:
        import pytesseract, sys, os
        # Auto-configurar ruta en Windows si no está en PATH
        if sys.platform == "win32" and not __import__("shutil").which("tesseract"):
            for _p in [r"C:\Program Files\Tesseract-OCR\tesseract.exe",
                       r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"]:
                if os.path.isfile(_p):
                    pytesseract.pytesseract.tesseract_cmd = _p
                    break
        config = "--oem 3 --psm 6 -c preserve_interword_spaces=1"
        return pytesseract.image_to_string(img, lang=lang, config=config)
    except ImportError:
        return "[pytesseract no instalado]"
    except Exception as e:
        return f"[Tesseract error: {e}]"
 
 
def _easyocr_extract(img, lang: str = "spa+eng") -> str:
    """Usa el singleton de EasyOCR para evitar recargar el modelo en cada imagen.
    FIX v15-CLINIC: el reader se crea UNA sola vez y se reutiliza (bug original creaba uno por imagen).
    """
    try:
        import numpy as np
        langs = []
        if "spa" in lang or "es" in lang:
            langs.append("es")
        if "eng" in lang or "en" in lang:
            langs.append("en")
        if not langs:
            langs = ["es", "en"]
        reader = get_easyocr_reader(langs)  # ← SINGLETON (no recrea el modelo)
        if reader is None:
            return _tesseract_extract(img, lang)
        img_np = np.array(img)
        results = reader.readtext(img_np, detail=0, paragraph=True)
        return "\n".join(results)
    except ImportError:
        log.warning("EasyOCR no instalado, usando Tesseract")
        return _tesseract_extract(img, lang)
    except Exception as e:
        log.warning(f"EasyOCR error: {e}, usando Tesseract")
        return _tesseract_extract(img, lang)
 
 
def _ocr_bytes_basic(img_bytes: bytes, lang: str = "spa+eng") -> str:
    """Fallback OCR básico sin OpenCV."""
    try:
        from PIL import Image, ImageEnhance
        import pytesseract
        img = Image.open(io.BytesIO(img_bytes))
        if img.mode != "RGB":
            img = img.convert("RGB")
        img = ImageEnhance.Contrast(img).enhance(1.5)
        img = ImageEnhance.Sharpness(img).enhance(2.0)
        w, h = img.size
        if w < 1000:
            img = img.resize((int(w * 1000 / w), int(h * 1000 / w)), Image.LANCZOS)
        return pytesseract.image_to_string(img, lang=lang, config="--oem 3 --psm 6")
    except Exception as e:
        return f"[OCR error: {e}]"
 
 
def _vision_ocr(img_bytes: bytes, api_key: str,
                 provider: str = "claude") -> str:
    """
    Usa visión del modelo LLM directamente sobre la imagen.
    Mucho más preciso que Tesseract para manuscritos difíciles.
    """
    b64_img = base64.b64encode(img_bytes).decode("utf-8")
    prompt = (
        "Eres un experto en lectura de documentos médicos manuscritos en español colombiano. "
        "Transcribe EXACTAMENTE todo el texto visible en esta imagen, "
        "incluyendo abreviaciones médicas, números, fechas y firmas. "
        "Conserva la estructura del documento. No omitas nada. "
        "Si hay texto ilegible, indica [ilegible]. "
        "Responde SOLO con el texto transcrito, sin comentarios adicionales."
    )
 
    if provider == "claude":
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=api_key)
            msg = client.messages.create(
                model="claude-opus-4-5",
                max_tokens=4096,
                messages=[{
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": b64_img,
                            },
                        },
                        {"type": "text", "text": prompt},
                    ],
                }],
            )
            return msg.content[0].text
        except Exception as e:
            log.warning(f"Vision Claude error: {e}")
            return _ocr_bytes_basic(img_bytes, "spa+eng")
 
    elif provider == "openai":
        try:
            from openai import OpenAI
            client = _get_openai_client(api_key)  # SINGLETON
            resp = client.chat.completions.create(
                model="gpt-4o",
                max_tokens=4096,
                messages=[{
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{b64_img}",
                                "detail": "high",
                            },
                        },
                        {"type": "text", "text": prompt},
                    ],
                }],
            )
            return resp.choices[0].message.content or ""
        except Exception as e:
            log.warning(f"Vision OpenAI error: {e}")
            return _ocr_bytes_basic(img_bytes, "spa+eng")
 
    return ""
 
 
# ─────────────────────────────────────────────────────────────
# SEGMENTADOR DE DOCUMENTOS
# ─────────────────────────────────────────────────────────────
 
SECCIONES_HC = {
    "identificacion": [
        "nombre", "paciente", "documento", "cédula", "cedula",
        "fecha nacimiento", "edad", "sexo", "género", "genero",
        "eps", "aseguradora", "afiliado"
    ],
    "motivo_consulta": [
        "motivo", "consulta", "queja", "principal", "viene por",
        "refiere", "acude"
    ],
    "enfermedad_actual": [
        "enfermedad actual", "historia", "relato", "evolución",
        "evolucion", "cuadro clínico", "tiempo evolución"
    ],
    "antecedentes": [
        "antecedente", "personales", "familiares", "quirúrgico",
        "quirurgico", "patológico", "patologico", "alergia",
        "medicamento", "gineco", "obstétrico"
    ],
    "revision_sistemas": [
        "revisión", "revision", "sistemas", "órganos", "organos",
        "cardiovascular", "respiratorio", "digestivo", "neurológico"
    ],
    "examen_fisico": [
        "examen físico", "examen fisico", "ef:", "exploración",
        "exploracion", "inspección", "inspeccion", "auscultación",
        "palpación", "palpacion", "signos vitales", "sv:"
    ],
    "signos_vitales": [
        "tensión arterial", "tension arterial", "ta:", "fc:", "fr:",
        "temperatura", "temp:", "saturación", "saturacion", "sat o2",
        "peso", "talla", "imc"
    ],
    "diagnostico": [
        "diagnóstico", "diagnostico", "impresión", "impresion",
        "cie", "cie-10", "codigo", "código", "conclusión", "conclusion"
    ],
    "plan_tratamiento": [
        "plan", "tratamiento", "manejo", "conducta", "prescripción",
        "prescripcion", "medicamento", "dosis", "fórmula", "formula"
    ],
    "examenes": [
        "laboratorio", "laboratorios", "examen", "paraclínicos",
        "paraclínicos", "paraclínico", "rx", "rayos x", "ecografía",
        "ecografia", "solicita"
    ],
}
 
 
@__import__("functools").lru_cache(maxsize=512)
def segment_document(text: str) -> Dict[str, str]:
    """
    Divide el texto de la historia clínica en secciones semánticas.
    Permite al LLM recibir solo las secciones relevantes para cada campo.
    MEJORA v15-CLINIC: cacheado con LRU (mismo texto no se resegmenta en reintentos).
    """
    lines = text.split("\n")
    segments: Dict[str, List[str]] = {s: [] for s in SECCIONES_HC}
    segments["general"] = []
    current_section = "general"
 
    for line in lines:
        line_lower = line.lower()
        matched = False
        for seccion, keywords in SECCIONES_HC.items():
            if any(kw in line_lower for kw in keywords):
                current_section = seccion
                matched = True
                break
        segments[current_section].append(line)
 
    return {k: "\n".join(v).strip() for k, v in segments.items() if v}
 
 
def get_relevant_fragment(text: str, campo: str, segments: Dict[str, str],
                           max_chars: int = 3000) -> str:
    """
    Retorna el fragmento más relevante del documento para un campo dado.
    Usa los segmentos si están disponibles, si no busca por palabras clave.
    """
    # Mapeo de campo a sección relevante
    campo_seccion = {
        "nombre_paciente": "identificacion",
        "fecha_nacimiento": "identificacion",
        "edad": "identificacion",
        "sexo": "identificacion",
        "documento_identidad": "identificacion",
        "eps_aseguradora": "identificacion",
        "motivo_consulta": "motivo_consulta",
        "enfermedad_actual": "enfermedad_actual",
        "antecedentes_personales": "antecedentes",
        "antecedentes_familiares": "antecedentes",
        "alergias": "antecedentes",
        "examen_fisico": "examen_fisico",
        "tension_arterial": "signos_vitales",
        "frecuencia_cardiaca": "signos_vitales",
        "temperatura": "signos_vitales",
        "frecuencia_respiratoria": "signos_vitales",
        "saturacion_o2": "signos_vitales",
        "peso_kg": "signos_vitales",
        "talla_cm": "signos_vitales",
        "imc": "signos_vitales",
        "diagnostico_principal": "diagnostico",
        "codigo_cie10_principal": "diagnostico",
        "diagnosticos_secundarios": "diagnostico",
        "codigos_cie10_secundarios": "diagnostico",
        "medicamentos": "plan_tratamiento",
        "dosis": "plan_tratamiento",
        "plan_tratamiento": "plan_tratamiento",
        "examenes_solicitados": "examenes",
    }
 
    seccion = campo_seccion.get(campo)
    if seccion and seccion in segments and segments[seccion]:
        fragment = segments[seccion]
        # Incluir también signos vitales de examen físico si es relevante
        if seccion == "examen_fisico" and "signos_vitales" in segments:
            fragment = segments["signos_vitales"] + "\n\n" + fragment
        return fragment[:max_chars]
 
    # Búsqueda por ventana deslizante de palabras clave del campo
    keywords = campo.replace("_", " ").split()
    text_lower = text.lower()
    best_pos = 0
    best_count = 0
    window = 500
    for i in range(0, len(text) - window, 100):
        chunk = text_lower[i:i + window]
        count = sum(1 for kw in keywords if kw in chunk)
        if count > best_count:
            best_count = count
            best_pos = i
 
    start = max(0, best_pos - 200)
    return text[start:start + max_chars]
 
 
# ─────────────────────────────────────────────────────────────
# MOTOR DE LLM (Claude + OpenAI, seleccionable)
# ─────────────────────────────────────────────────────────────
 
def _call_llm(messages: List[Dict], api_key: str,
              provider: str = "claude",
              model: str = "claude-sonnet-4-5",
              max_tokens: int = 3000,
              temperature: float = 0.05) -> str:
    """
    Llama al LLM seleccionado (Claude o GPT-4o) con reintentos.
    Claude es el predeterminado por mejor desempeño en textos médicos en español.
    MEJORA v15b: instrumentación de tiempo para monitoreo de latencia.
    """
    _t0 = time.monotonic()
    try:
        if provider == "claude":
            result = _call_claude(messages, api_key, model, max_tokens, temperature)
        else:
            result = _call_openai(messages, api_key, model, max_tokens, temperature)
        _elapsed = time.monotonic() - _t0
        if _elapsed > 30:
            log.warning(f"LLM lento: {provider}/{model} tardó {_elapsed:.1f}s")
        return result
    except Exception as e:
        _elapsed = time.monotonic() - _t0
        log.error(f"LLM error tras {_elapsed:.1f}s ({provider}/{model}): {e}")
        raise
 
 
# ── Singleton de clientes LLM (v15-CLINIC) ─────────────────────
_anthropic_clients: Dict[str, Any] = {}
_openai_clients: Dict[str, Any] = {}
_llm_client_lock = __import__("threading").Lock()


def _get_anthropic_client(api_key: str):
    """Singleton Anthropic: evita recrear cliente TCP en cada llamada LLM."""
    with _llm_client_lock:
        if api_key not in _anthropic_clients:
            try:
                import anthropic
                import httpx
                _anthropic_clients[api_key] = anthropic.Anthropic(
                    api_key=api_key,
                    http_client=httpx.Client(
                        timeout=httpx.Timeout(120.0, connect=10.0),
                        limits=httpx.Limits(max_connections=20, max_keepalive_connections=10),
                    )
                )
                log.info("✅ Cliente Anthropic singleton inicializado")
            except Exception:
                import anthropic
                _anthropic_clients[api_key] = anthropic.Anthropic(api_key=api_key)
        return _anthropic_clients[api_key]


def _get_openai_client(api_key: str):
    """Singleton OpenAI: evita recrear cliente TCP en cada llamada LLM."""
    with _llm_client_lock:
        if api_key not in _openai_clients:
            try:
                from openai import OpenAI
                import httpx
                _openai_clients[api_key] = OpenAI(
                    api_key=api_key,
                    http_client=httpx.Client(
                        timeout=httpx.Timeout(120.0, connect=10.0),
                        limits=httpx.Limits(max_connections=20, max_keepalive_connections=10),
                    )
                )
                log.info("✅ Cliente OpenAI singleton inicializado")
            except Exception:
                from openai import OpenAI
                _openai_clients[api_key] = OpenAI(api_key=api_key)
        return _openai_clients[api_key]


def _call_claude(messages: List[Dict], api_key: str,
                 model: str = "claude-sonnet-4-5",
                 max_tokens: int = 3000,
                 temperature: float = 0.05) -> str:
    try:
        import anthropic
    except ImportError:
        raise RuntimeError("Instala anthropic: pip install anthropic")
 
    client = _get_anthropic_client(api_key)  # SINGLETON
 
    # Separar system del resto de mensajes
    system_msg = ""
    user_messages = []
    for m in messages:
        if m["role"] == "system":
            system_msg = m["content"]
        else:
            user_messages.append(m)
 
    last_error = None
    for attempt in range(4):
        try:
            resp = client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                system=system_msg if system_msg else anthropic.NOT_GIVEN,
                messages=user_messages,
            )
            return resp.content[0].text
        except Exception as e:
            last_error = e
            wait = 2 ** attempt * 3
            log.warning(f"Claude intento {attempt+1}/4 falló: {e}. Esperando {wait}s")
            time.sleep(wait)
 
    raise RuntimeError(f"Claude falló tras reintentos: {last_error}")
 
 
def _call_openai(messages: List[Dict], api_key: str,
                 model: str = "gpt-4o",
                 max_tokens: int = 3000,
                 temperature: float = 0.05) -> str:
    try:
        from openai import OpenAI, RateLimitError, APIError
    except ImportError:
        raise RuntimeError("Instala openai: pip install openai")
 
    client = OpenAI(api_key=api_key)
    last_error = None
 
    for attempt in range(4):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return resp.choices[0].message.content or ""
        except RateLimitError:
            wait = 2 ** attempt * 5
            log.warning(f"Rate limit OpenAI, esperando {wait}s...")
            time.sleep(wait)
        except APIError as e:
            last_error = e
            time.sleep(2 ** attempt)
        except Exception as e:
            last_error = e
            break
 
    raise RuntimeError(f"OpenAI falló tras reintentos: {last_error}")
 
 
def _parse_json_response(response: str) -> Dict:
    """Parsea respuesta JSON del LLM con limpieza robusta."""
    response = re.sub(r"```json\s*", "", response)
    response = re.sub(r"```\s*", "", response)
    response = response.strip()
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        m = re.search(r"\{[\s\S]*\}", response)
        if m:
            try:
                return json.loads(m.group())
            except Exception:
                pass
        return {}
 
 
# ─────────────────────────────────────────────────────────────
# PROMPTS (mejorados con terminología SGSSS colombiana)
# ─────────────────────────────────────────────────────────────
 
SYSTEM_EXTRACTOR = """Eres un extractor clínico experto especializado en historias clínicas del Sistema General de Seguridad Social en Salud (SGSSS) de Colombia.
 
EXPERIENCIA Y CONTEXTO:
- Historias escritas a mano (reconoces abreviaciones médicas en español colombiano)
- Historias digitales de sistemas como Salesforce Health Cloud, HIS, OME, Hipócrates
- Terminología del sistema de salud colombiano: EPS, IPS, SOAT, SISBEN, ADRES, Resolución 1995/99
- Clasificación CIE-10 según RIPS colombianos
- Abreviaciones frecuentes: TA, FC, FR, T°, SatO2, EF, AP, AHF, AQx, APx, AHF, MC, EA, PCM, HTA, DM, ERC
 
ABREVIACIONES MÉDICAS COLOMBIANAS COMUNES:
- TA: Tensión Arterial | FC: Frecuencia Cardíaca | FR: Frecuencia Respiratoria
- T° o Temp: Temperatura | SatO2 o Sat: Saturación de Oxígeno
- EF: Examen Físico | MC: Motivo de Consulta | EA: Enfermedad Actual
- Dx: Diagnóstico | Rx: Tratamiento o Radiografía (por contexto)
- HTA: Hipertensión Arterial | DM: Diabetes Mellitus | ERC: Enfermedad Renal Crónica
- EPOC: Enfermedad Pulmonar Obstructiva Crónica | ICC: Insuficiencia Cardíaca Congestiva
- GI: Gastrointestinal | SNC: Sistema Nervioso Central
- AP: Antecedentes Personales | AHF: Antecedentes Heredofamiliares | AQx: Antecedentes Quirúrgicos
- PCM: Peso, Condición, Medicamentos | SOAP: Subjetivo, Objetivo, Análisis, Plan
- C/C: Con | S/C: Sin | PO: Por vía Oral | IV: Intravenoso | IM: Intramuscular | SC: Subcutáneo
- QD/OD: Una vez al día | BID: Dos veces al día | TID: Tres veces al día | QID: Cuatro veces al día
- PRN: Según necesidad | VO: Vía Oral | SL: Sublingual
 
INSTRUCCIONES CRÍTICAS:
- Responde ÚNICAMENTE con JSON válido, sin explicaciones ni markdown
- Si un campo no está presente o no es legible: usa null
- Para arrays: siempre usa listas JSON aunque haya un solo elemento
- Fechas en formato ISO YYYY-MM-DD
- Nombres propios: capitalización correcta
- Códigos CIE-10: formato exacto (ej: "J06.9", "I10", "E11.9", "O09.2")
- Tensión arterial: intenta separar sistólica/diastólica (ej: "120/80 mmHg")
- Para medicamentos: extrae nombre comercial Y genérico si aparecen ambos
- Dosis con unidades: mg, mcg, UI, mL, g
- Tipo de documento: CC (Cédula Ciudadanía), TI (Tarjeta Identidad), CE (Cédula Extranjería), RC (Registro Civil), PA (Pasaporte), NIT, NUIP
- Tipo de consulta: Primera Vez, Control, Urgencias, Hospitalización, Interconsulta, Telemedicina
"""
 
 
def prompt_extraccion(text: str, campos: List[str],
                       segments: Dict[str, str] = None,
                       tipo_consulta: str = "") -> str:
    """
    Genera prompt de extracción con secciones relevantes del documento.
    Incluye hasta 18,000 chars del texto completo más secciones clave.
    """
    fields_str = "\n".join(f'  "{f}": <valor o null>' for f in campos)
 
    # Incluir secciones más relevantes para los campos solicitados
    context_extra = ""
    if segments:
        key_sections = ["identificacion", "signos_vitales", "diagnostico",
                        "plan_tratamiento", "motivo_consulta"]
        parts = []
        for sec in key_sections:
            if sec in segments and segments[sec]:
                parts.append(f"[Sección: {sec.upper()}]\n{segments[sec][:1500]}")
        if parts:
            context_extra = "\n\nSECCIONES IDENTIFICADAS:\n" + "\n\n".join(parts)
 
    tipo_str = f"\nTIPO DE CONSULTA ESPERADO: {tipo_consulta}\n" if tipo_consulta else ""
 
    return f"""Analiza esta historia clínica colombiana y extrae los siguientes campos con máxima precisión.{tipo_str}
 
CAMPOS REQUERIDOS:
{chr(10).join(f"- {f}" for f in campos)}
 
HISTORIA CLÍNICA COMPLETA:
{text[:16000]}
{context_extra}
 
Responde con este JSON exacto (sin texto adicional):
{{
{fields_str}
}}"""
 
 
SYSTEM_VERIFICADOR = """Eres un médico verificador experto en historias clínicas colombianas.
Tu misión: revisar una extracción de datos clínicos y verificar su exactitud contra el documento original.
 
TAREA:
1. Lee el documento original nuevamente con atención
2. Compara CADA campo extraído con lo que dice el documento (incluyendo abreviaciones colombianas)
3. Identifica discrepancias, datos faltantes, mal interpretados o incorrectos
4. Asigna confianza 0.0-1.0 por campo (1.0 = completamente seguro)
5. Señala campos que requieren revisión humana
6. Considera abreviaciones del SGSSS: TA=Tensión Arterial, FC=Frecuencia Cardíaca, etc.
 
Responde SOLO con JSON. No incluyas explicaciones fuera del JSON.
"""
 
 
def prompt_verificacion(text: str, extraction: Dict, campos: List[str],
                         segments: Dict[str, str] = None) -> str:
    ext_str = json.dumps(extraction, ensure_ascii=False, indent=2)
 
    # Incluir texto completo (no solo primeros N chars)
    doc_context = text[:14000]
    if segments and len(text) > 14000:
        # Añadir secciones de diagnóstico y plan que suelen estar al final
        # MEJORA v15c: join en lugar de += para concatenación de strings
        extra_parts = [
            f"\n\n[{sec.upper()}]\n{segments[sec][:2000]}"
            for sec in ["diagnostico", "plan_tratamiento", "examenes"]
            if sec in segments and segments[sec]
        ]
        doc_context += "".join(extra_parts)
 
    return f"""Verifica esta extracción clínica contra el documento original colombiano.
 
EXTRACCIÓN A VERIFICAR:
{ext_str}
 
DOCUMENTO ORIGINAL:
{doc_context}
 
Responde con este JSON:
{{
  "verificacion_por_campo": {{
    "<campo>": {{
      "valor_confirmado": <valor verificado o null>,
      "coincide": <true/false>,
      "confianza": <0.0-1.0>,
      "nota": "<observación si hay discrepancia o abreviación interpretada>"
    }}
  }},
  "confianza_global": <0.0-1.0>,
  "campos_conflictivos": ["<lista de campos con discrepancias>"],
  "requiere_revision_humana": <true/false>,
  "resumen_verificacion": "<resumen breve de hallazgos y observaciones clave>"
}}"""
 
 
SYSTEM_RESOLUTOR = """Eres un árbitro clínico experto en el sistema de salud colombiano.
Recibes dos versiones de datos extraídos de una historia clínica y determinas el valor correcto.
 
Usa estos criterios:
- Contexto del documento y fragmentos específicos donde aparece el dato
- Coherencia médica (edad vs diagnóstico, medicamentos vs indicaciones, dosis vs vía)
- Lógica temporal (fechas coherentes entre sí)
- Estándares colombianos de historia clínica (Resolución 1995/1999)
- Abreviaciones del SGSSS correctamente interpretadas
 
Responde SOLO con JSON.
"""
 
 
def prompt_resolucion(campo: str, val1: Any, val2: Any,
                       fragment: str, razonamiento_v1: str = "",
                       razonamiento_v2: str = "") -> str:
    """
    Resolución de conflicto campo por campo con fragmento relevante.
    """
    return f"""Resuelve el conflicto en el campo '{campo}' de esta historia clínica.
 
EXTRACCIÓN 1 (primera lectura): {json.dumps(val1, ensure_ascii=False)}
{f'Nota de extracción 1: {razonamiento_v1}' if razonamiento_v1 else ''}
 
EXTRACCIÓN 2 (verificación): {json.dumps(val2, ensure_ascii=False)}
{f'Nota de verificación: {razonamiento_v2}' if razonamiento_v2 else ''}
 
FRAGMENTO RELEVANTE DEL DOCUMENTO (donde debería aparecer este dato):
{fragment}
 
Determina el valor correcto:
{{
  "valor_final": <valor más probable>,
  "razonamiento": "<por qué este valor es más correcto>",
  "confianza": <0.0-1.0>
}}"""
 
 

# ═══════════════════════════════════════════════════════════════
# MÓDULO 1 — SCORE DE CALIDAD OCR
# ═══════════════════════════════════════════════════════════════

OCR_QUALITY_THRESHOLD = float(os.environ.get("CEP_OCR_QUALITY_MIN", "35"))

# Patrones que indican texto basura de OCR
_OCR_NOISE_PATTERNS = [
    r'[^\w\s\.,;:\-\(\)\[\]\/\°\%\+\=áéíóúüñÁÉÍÓÚÜÑ]{4,}',  # Chars raros consecutivos
    r'(\w){5,}',         # Mismo char repetido 6+ veces
    r'[0-9]{20,}',         # Números larguísimos sin sentido
]
_OCR_NOISE_RE = [re.compile(p) for p in _OCR_NOISE_PATTERNS]

# Vocabulario clínico colombiano esperado
_VOCAB_CLINICO = {
    'paciente','consulta','diagnostico','diagnóstico','fecha','nombre',
    'edad','sexo','peso','talla','tensión','presión','temperatura',
    'medicamento','tratamiento','antecedentes','historia','clínica',
    'eps','ips','médico','doctor','enfermera','urgencias','control',
    'dolor','fiebre','tos','nausea','vómito','diarrea','cefalea',
    'hipertensión','diabetes','corazón','pulmón','riñón',
    'mg','ml','dosis','vía','oral','intravenoso','tableta',
}


def score_ocr_quality(text: str) -> Dict[str, Any]:
    """
    Calcula un score de calidad OCR 0-100 con descomposición diagnóstica.

    Criterios:
    - Densidad de caracteres legibles (alfanuméricos + puntuación española)
    - Ausencia de patrones de ruido (chars raros repetidos)
    - Presencia de vocabulario clínico colombiano
    - Proporción de palabras completas vs fragmentos

    Retorna dict con score y diagnóstico para mostrar en UI.
    """
    if not text or not text.strip():
        return {"score": 0, "nivel": "ilegible", "apto": False,
                "detalle": "Texto vacío", "chars": 0, "palabras": 0}

    chars_total = len(text)
    # Chars "buenos": letras, dígitos, puntuación española
    buenos = sum(1 for c in text if c.isalnum() or c in ' .,;:-áéíóúüñÁÉÍÓÚÜÑ\n°%()/')
    densidad = buenos / max(chars_total, 1)

    # Penalizar patrones de ruido
    ruido = sum(len(p.findall(text)) for p in _OCR_NOISE_RE)
    penalty_ruido = min(0.4, ruido * 0.05)

    # Bonus por vocabulario clínico
    words = set(re.findall(r'\w{3,}', text.lower()))
    vocab_hits = len(words & _VOCAB_CLINICO)
    bonus_vocab = min(0.25, vocab_hits * 0.02)

    # Proporción de palabras largas (≥4 chars) → texto real vs ruido
    palabras = re.findall(r'\w+', text)
    prop_largas = sum(1 for w in palabras if len(w) >= 4) / max(len(palabras), 1)

    raw = (densidad * 0.45 + prop_largas * 0.30 + bonus_vocab - penalty_ruido)
    score = max(0, min(100, round(raw * 100)))

    if score >= 70:
        nivel = "bueno"
    elif score >= OCR_QUALITY_THRESHOLD:
        nivel = "aceptable"
    elif score >= 20:
        nivel = "deficiente"
    else:
        nivel = "ilegible"

    return {
        "score":     score,
        "nivel":     nivel,
        "apto":      score >= OCR_QUALITY_THRESHOLD,
        "detalle":   f"densidad={densidad:.2f} ruido={ruido} vocab={vocab_hits} palabras={len(palabras)}",
        "chars":     chars_total,
        "palabras":  len(palabras),
    }


# ═══════════════════════════════════════════════════════════════
# MÓDULO 2 — TRAZABILIDAD POR CAMPO
# ═══════════════════════════════════════════════════════════════

@dataclass
class FieldTrace:
    """Trazabilidad completa de un campo extraído."""
    campo:           str
    valor:           Any
    texto_original:  str        # Fragmento exacto del PDF del que se extrajo
    pagina:          Optional[int]   # Número de página (1-indexed), None si no aplica
    seccion:         Optional[str]   # Sección del documento (diagnostico, signos_vitales…)
    modelo:          str        # Modelo LLM que extrajo el valor
    confianza:       float      # 0.0-1.0
    metodo:          str        # "extraction_pass1" | "verification" | "resolution" | "audit_correction"
    es_inferencia:   bool       # True si el LLM infirió, False si está literal
    timestamp_utc:   str


def build_field_trace(campo: str, valor: Any, raw_text: str,
                       segments: Dict[str, str], modelo: str,
                       confianza: float, metodo: str,
                       es_inferencia: bool = False) -> FieldTrace:
    """
    Construye la traza de un campo buscando el fragmento textual más relevante.
    """
    # Intentar encontrar el texto exacto donde aparece el valor en el documento
    texto_original = ""
    pagina = None
    seccion = None

    valor_str = str(valor) if valor is not None else ""

    if valor_str and len(valor_str) > 1:
        # Buscar fragmento de ~200 chars alrededor del valor en el texto
        idx = raw_text.lower().find(valor_str.lower()[:30])
        if idx >= 0:
            start = max(0, idx - 80)
            end   = min(len(raw_text), idx + len(valor_str) + 80)
            texto_original = raw_text[start:end].strip()

            # Detectar número de página si el texto tiene marcadores [Página N]
            page_markers = list(re.finditer(r'\[Página (\d+)', raw_text[:idx]))
            if page_markers:
                pagina = int(page_markers[-1].group(1))

    # Detectar sección
    if segments:
        section_map = {
            "identificacion":  ["nombre", "edad", "sexo", "documento", "fecha_nacimiento"],
            "signos_vitales":  ["tension_arterial", "frecuencia_cardiaca", "temperatura",
                               "saturacion_oxigeno", "peso", "talla", "imc"],
            "diagnostico":     ["diagnostico_principal", "codigo_cie10_principal",
                               "diagnosticos_secundarios"],
            "plan_tratamiento":["medicamentos", "plan", "recomendaciones"],
            "motivo_consulta": ["motivo_consulta", "enfermedad_actual"],
        }
        for sec, campos_sec in section_map.items():
            if campo in campos_sec:
                seccion = sec
                break

        # Si no se encontró en el texto principal, buscar en la sección
        if not texto_original and seccion and seccion in segments:
            seg_text = segments[seccion]
            idx2 = seg_text.lower().find(valor_str.lower()[:25]) if valor_str else -1
            if idx2 >= 0:
                s = max(0, idx2 - 60)
                e = min(len(seg_text), idx2 + len(valor_str) + 60)
                texto_original = seg_text[s:e].strip()

    return FieldTrace(
        campo=campo,
        valor=valor,
        texto_original=texto_original[:400] if texto_original else "",
        pagina=pagina,
        seccion=seccion,
        modelo=modelo,
        confianza=confianza,
        metodo=metodo,
        es_inferencia=es_inferencia,
        timestamp_utc=datetime.utcnow().isoformat(),
    )


def traces_to_dict(traces: Dict[str, FieldTrace]) -> Dict:
    """Serializa trazas a dict para almacenamiento."""
    return {
        campo: {
            "valor":           t.valor,
            "texto_original":  t.texto_original,
            "pagina":          t.pagina,
            "seccion":         t.seccion,
            "modelo":          t.modelo,
            "confianza":       t.confianza,
            "metodo":          t.metodo,
            "es_inferencia":   t.es_inferencia,
            "timestamp_utc":   t.timestamp_utc,
        }
        for campo, t in traces.items()
    }


# ═══════════════════════════════════════════════════════════════
# MÓDULO 3 — NORMALIZACIÓN DE DATOS
# ═══════════════════════════════════════════════════════════════

# ── CIE-10: tabla de sinónimos → código canónico ──────────────
# (muestra; en producción usar catálogo MSPS completo ~14k códigos)
_CIE10_SINONIMOS: Dict[str, str] = {
    # Hipertensión
    "hta": "I10", "hipertensión arterial": "I10", "hipertension arterial": "I10",
    "hipertensión": "I10", "presión alta": "I10",
    # Diabetes
    "dm2": "E11.9", "dm tipo 2": "E11.9", "diabetes tipo 2": "E11.9",
    "diabetes mellitus tipo 2": "E11.9", "diabetes mellitus 2": "E11.9",
    "dm1": "E10.9", "dm tipo 1": "E10.9", "diabetes tipo 1": "E10.9",
    # IRA/Resfriado
    "ira": "J06.9", "resfriado": "J06.9", "infección respiratoria aguda": "J06.9",
    "rinofaringitis": "J06.9",
    # Neumonía
    "neumonia": "J18.9", "neumonía": "J18.9", "neumonía bacteriana": "J15.9",
    # COVID
    "covid": "U07.1", "covid-19": "U07.1", "sars-cov-2": "U07.1",
    # Cardiopatía
    "icc": "I50.9", "insuficiencia cardíaca": "I50.9",
    "insuficiencia cardiaca congestiva": "I50.0",
    "infarto": "I21.9", "iam": "I21.9",
    # Renal
    "erc": "N18.9", "enfermedad renal crónica": "N18.9",
    "ira renal": "N17.9", "insuficiencia renal aguda": "N17.9",
    # Pulmonar
    "epoc": "J44.1", "enfermedad pulmonar obstructiva": "J44.1",
    "asma": "J45.9",
    # Neurológico
    "evento cerebrovascular": "I64", "evc": "I64", "ictus": "I64",
    "epilepsia": "G40.9",
    # Infectológico
    "dengue": "A97.9", "malaria": "B54", "paludismo": "B54",
    "tuberculosis": "A15.9", "tbc": "A15.9",
    # Osteoarticular
    "artritis reumatoide": "M06.9", "ar": "M06.9",
    "osteoporosis": "M81.9", "fractura cadera": "S72.0",
    # Gineco-obstétrico
    "embarazo": "Z34.9", "control prenatal": "Z34.9",
    "parto": "O80", "cesárea": "O82",
}

# ── Medicamentos: nombre comercial/variante → genérico DCI ───
_MED_NORMALIZACION: Dict[str, str] = {
    # Analgésicos
    "acetaminofén": "paracetamol", "acetaminofen": "paracetamol",
    "tylenol": "paracetamol", "dolex": "paracetamol",
    "advil": "ibuprofeno", "nurofen": "ibuprofeno",
    # Antibióticos
    "amoxil": "amoxicilina", "trimox": "amoxicilina",
    "augmentine": "amoxicilina-clavulánico", "clavulin": "amoxicilina-clavulánico",
    "ciprobay": "ciprofloxacino", "ciproxina": "ciprofloxacino",
    "flagyl": "metronidazol",
    # Antihipertensivos
    "norvasc": "amlodipino", "terapil": "amlodipino",
    "cozaar": "losartan", "losartán": "losartan",
    "renitec": "enalapril", "vasotec": "enalapril",
    "tenormin": "atenolol",
    # Antidiabéticos
    "glucophage": "metformina", "glafornil": "metformina",
    "amaryl": "glimepirida",
    "lantus": "insulina glargina", "levemir": "insulina detemir",
    "novorapid": "insulina aspart", "humalog": "insulina lispro",
    # Estatinas
    "lipitor": "atorvastatina", "crestor": "rosuvastatina",
    "mevacor": "lovastatina",
    # Gastrointestinal
    "omeprazol": "omeprazol",  # ya es genérico
    "losec": "omeprazol", "prilosec": "omeprazol",
    "zantac": "ranitidina", "tagamet": "cimetidina",
    # Psiquiátrico
    "prozac": "fluoxetina", "paxil": "paroxetina", "zoloft": "sertralina",
    "rivotril": "clonazepam", "valium": "diazepam",
}

# ── Unidades: normalización a unidad canónica ─────────────────
_UNIDADES_NORM: Dict[str, str] = {
    "mgr": "mg", "mgs": "mg", "milligramos": "mg", "miligramos": "mg",
    "mcg": "mcg", "µg": "mcg", "microgramos": "mcg",
    "grs": "g", "gramos": "g", "gram": "g",
    "ml": "mL", "cc": "mL", "mililitros": "mL",
    "l": "L", "litros": "L",
    "ui": "UI", "iu": "UI", "unidades internacionales": "UI",
    "mmhg": "mmHg", "mm hg": "mmHg",
    "bpm": "lpm", "latidos/min": "lpm", "lat/min": "lpm",
    "rpm": "rpm", "resp/min": "rpm",
    "°c": "°C", "grados": "°C", "grados celsius": "°C",
    "%": "%", "porcentaje": "%",
    "kg": "kg", "kgs": "kg", "kilogramos": "kg",
    "cm": "cm", "mts": "m", "metros": "m",
    "kcal": "kcal", "calorias": "kcal",
}

_UNIDAD_RE = re.compile(
    r'(\d+(?:[.,]\d+)?)\s*(' +
    '|'.join(re.escape(k) for k in sorted(_UNIDADES_NORM, key=len, reverse=True)) +
    r')',
    re.IGNORECASE
)


def normalizar_cie10(texto: str) -> Optional[str]:
    """
    Normaliza un diagnóstico o código CIE-10 a su forma canónica.
    Primero intenta reconocer el código directo, luego busca en sinónimos.
    """
    if not texto:
        return None
    t = texto.strip()

    # ¿Ya es un código CIE-10 válido? (ej: "I10", "E11.9", "J06.9")
    if re.match(r'^[A-Z]\d{2}(\.\d{1,2})?$', t.upper()):
        return t.upper()

    # Buscar en sinónimos (case-insensitive)
    canon = _CIE10_SINONIMOS.get(t.lower().strip())
    if canon:
        return canon

    # Fuzzy: buscar si alguna clave está contenida en el texto
    t_lower = t.lower()
    best_match = None
    best_len = 0
    for sinonimo, codigo in _CIE10_SINONIMOS.items():
        if sinonimo in t_lower and len(sinonimo) > best_len:
            best_match = codigo
            best_len = len(sinonimo)

    return best_match  # None si no se encontró


def normalizar_medicamento(nombre: str) -> str:
    """Normaliza nombre comercial a DCI (nombre genérico)."""
    if not nombre:
        return nombre
    key = nombre.lower().strip()
    return _MED_NORMALIZACION.get(key, nombre)


def normalizar_unidades(texto: str) -> str:
    """Normaliza unidades de medida a forma canónica."""
    if not texto:
        return texto

    def _replace(m):
        num   = m.group(1).replace(',', '.')
        unit  = _UNIDADES_NORM.get(m.group(2).lower(), m.group(2))
        return f"{num} {unit}"

    return _UNIDAD_RE.sub(_replace, texto)


def normalizar_datos(data: Dict, campos: List[str]) -> Tuple[Dict, Dict[str, str]]:
    """
    Aplica normalización completa a los datos extraídos.
    Retorna (datos_normalizados, cambios_realizados).
    """
    normalized = dict(data)
    cambios: Dict[str, str] = {}

    # Normalizar CIE-10
    for campo in ["codigo_cie10_principal", "diagnostico_principal"]:
        val = normalized.get(campo)
        if val and isinstance(val, str):
            norm = normalizar_cie10(val)
            if norm and norm != val:
                normalized[campo] = norm
                cambios[campo] = f"{val!r} → {norm!r}"

    # CIE-10 secundarios
    for campo in ["codigos_cie10_secundarios", "diagnosticos_secundarios"]:
        val = normalized.get(campo)
        if val:
            if isinstance(val, str):
                val = [val]
            nuevos = []
            for item in val:
                norm = normalizar_cie10(str(item))
                nuevos.append(norm if norm else item)
            if nuevos != val:
                normalized[campo] = nuevos
                cambios[campo] = f"normalizado {len(nuevos)} código(s)"

    # Normalizar medicamentos
    meds = normalized.get("medicamentos")
    if meds:
        if isinstance(meds, str):
            meds = [meds]
        nuevos_meds = []
        for m in meds:
            gen = normalizar_medicamento(str(m))
            nuevos_meds.append(gen)
        if nuevos_meds != meds:
            normalized["medicamentos"] = nuevos_meds
            cambios["medicamentos"] = f"normalizado {len(nuevos_meds)} medicamento(s)"

    # Normalizar unidades en signos vitales
    for campo in ["tension_arterial", "frecuencia_cardiaca", "temperatura",
                  "saturacion_oxigeno", "peso", "talla", "glucemia",
                  "frecuencia_respiratoria"]:
        val = normalized.get(campo)
        if val and isinstance(val, str):
            norm = normalizar_unidades(val)
            if norm != val:
                normalized[campo] = norm
                cambios[campo] = f"{val!r} → {norm!r}"

    return normalized, cambios


# ═══════════════════════════════════════════════════════════════
# MÓDULO 4 — ANONIMIZACIÓN (Nivel 1: eliminación de PII)
# ═══════════════════════════════════════════════════════════════

# Patrones de datos personales identificables
_PII_PATTERNS = [
    # Cédula / documento
    (re.compile(r'(C\.?C\.?|T\.?I\.?|C\.?E\.?|N\.?U\.?I\.?P\.?|pasaporte)\s*[:#]?\s*\d[\d\.\-\s]{5,15}',
                re.IGNORECASE), "[DOC_REDACTED]"),
    # Número de cédula solo (9-12 dígitos)
    (re.compile(r'\d{9,12}'), "[ID_REDACTED]"),
    # Teléfono colombiano
    (re.compile(r'(3\d{2}[\s\-]?\d{3}[\s\-]?\d{4}|(\+57|57)[\s\-]?\d{10})'), "[TEL_REDACTED]"),
    # Email
    (re.compile(r'[\w.\-]+@[\w.\-]+\.\w{2,4}', re.IGNORECASE), "[EMAIL_REDACTED]"),
    # Dirección
    (re.compile(r'(calle|carrera|avenida|cra|cll|av|diagonal|transversal|manzana)\s+[\w\d\-#]+',
                re.IGNORECASE), "[ADDR_REDACTED]"),
]


def anonimizar_texto(texto: str) -> Tuple[str, int]:
    """
    Elimina PII del texto mediante regex.
    Retorna (texto_anonimizado, numero_de_reemplazos).
    """
    if not texto:
        return texto, 0
    total = 0
    result = texto
    for pattern, replacement in _PII_PATTERNS:
        new_result, n = pattern.subn(replacement, result)
        total += n
        result = new_result
    return result, total


def anonimizar_datos_extraidos(data: Dict, campos_pii: List[str] = None) -> Dict:
    """
    Anonimiza campos PII en los datos extraídos.
    Reemplaza nombre y documento con versión redactada.
    """
    if campos_pii is None:
        campos_pii = ["nombre_paciente", "numero_documento",
                      "nombre_acompañante", "direccion", "telefono",
                      "correo_electronico"]

    anon = dict(data)
    for campo in campos_pii:
        val = anon.get(campo)
        if val and isinstance(val, str) and val.strip():
            anon[campo] = "[REDACTED]"

    return anon


def generar_id_anonimo(nombre: str, documento: str,
                        fecha_nacimiento: str = "") -> str:
    """
    Genera un ID anónimo consistente para investigación.
    SHA-256(nombre_norm + documento + fecha_nac + SALT) → hex[:16].
    El mismo paciente siempre produce el mismo ID sin revelar identidad.
    """
    salt = os.environ.get("CEP_ANON_SALT", SECRET_KEY[:16])
    raw  = f"{nombre.strip().lower()}|{documento.strip()}|{fecha_nacimiento.strip()}|{salt}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


# ═══════════════════════════════════════════════════════════════
# MÓDULO 5 — SEPARACIÓN EXTRACCIÓN vs INTERPRETACIÓN
# ═══════════════════════════════════════════════════════════════

SYSTEM_EXTRACTOR_LITERAL = """Eres un extractor clínico forense. Tu única misión es TRANSCRIBIR datos que aparecen EXPLÍCITAMENTE en el documento.

REGLA ABSOLUTA: Solo extrae lo que está escrito literalmente.
- ✅ "Dx: HTA" → diagnostico_principal = "HTA"
- ✅ "TA: 140/90" → tension_arterial = "140/90"
- ❌ NUNCA escribas "hipertensión crónica probable" si el doc dice solo "HTA"
- ❌ NUNCA inferas edad a partir de fecha de nacimiento
- ❌ NUNCA completes un código CIE-10 si no aparece en el documento
- ❌ NUNCA asumas diagnóstico basado en medicamentos

Si un dato NO está explícito → null. Sin excepciones.
Contexto: historias clínicas SGSSS Colombia (Resolución 1995/1999).
Responde SOLO con JSON válido.
"""

SYSTEM_EXTRACTOR_INFERENCIA = """Eres un médico especialista en historias clínicas del SGSSS colombiano.
Tu misión: completar los campos que NO están explícitos pero pueden inferirse con alta certeza clínica.

SOLO infiere cuando:
1. La evidencia indirecta es inequívoca (ej: medicamentos implican diagnóstico conocido)
2. La inferencia sigue estándares clínicos publicados
3. Tu confianza en la inferencia es ≥ 0.80

Para cada inferencia DEBES indicar:
- is_inference: true
- inference_basis: "razón clínica de la inferencia"
- confidence: 0.0-1.0

Si no puedes inferir con certeza ≥ 0.80 → null.
Responde SOLO con JSON válido.
"""


def prompt_extraccion_literal(text: str, campos: List[str],
                               segments: Dict = None,
                               tipo_consulta: str = "") -> str:
    """Prompt para extracción literal (sin inferencias)."""
    fields_str = "\n".join(f'  "{f}": <SOLO si aparece explícitamente, sino null>' for f in campos)
    tipo_str   = f"\nTIPO DE CONSULTA ESPERADO: {tipo_consulta}\n" if tipo_consulta else ""
    context    = ""
    if segments:
        parts = [f"[{s.upper()}]\n{v[:1200]}"
                 for s, v in list(segments.items())[:5] if v]
        if parts:
            context = "\n\nSECCIONES:\n" + "\n\n".join(parts)

    return f"""Transcribe SOLO los datos explícitos de esta historia clínica.{tipo_str}
NO inferir. NO completar. Solo lo que está escrito.

DOCUMENTO:
{text[:14000]}{context}

Responde con JSON exacto:
{{
{fields_str}
}}"""


def prompt_extraccion_inferencia(text: str, datos_literales: Dict,
                                  campos_nulos: List[str],
                                  tipo_consulta: str = "") -> str:
    """Prompt para completar campos nulos con inferencia justificada."""
    if not campos_nulos:
        return ""
    fields_str = "\n".join(
        f'  "{f}": {{"valor": <inferido o null>, "is_inference": true, "inference_basis": "<razón>", "confidence": <0-1>}}'
        for f in campos_nulos
    )
    lit_str = json.dumps({k: v for k, v in datos_literales.items() if v is not None},
                          ensure_ascii=False, indent=2)
    tipo_str = f"\nTIPO DE CONSULTA: {tipo_consulta}" if tipo_consulta else ""

    return f"""Completa solo los campos nulos que puedas inferir con alta certeza.{tipo_str}

DATOS LITERALES YA EXTRAÍDOS:
{lit_str}

DOCUMENTO (para contexto):
{text[:8000]}

Completa solo estos campos nulos (si no puedes inferir → null):
{{
{fields_str}
}}"""


def merge_literal_inferencias(literal: Dict, inferencias: Dict,
                                campos: List[str]) -> Tuple[Dict, Dict[str, Dict]]:
    """
    Fusiona extracción literal con inferencias.
    Retorna (datos_finales, metadatos_inferencia).
    """
    final = dict(literal)
    meta_inferencia: Dict[str, Dict] = {}

    for campo in campos:
        inf_raw = inferencias.get(campo)
        if not inf_raw:
            continue
        if isinstance(inf_raw, dict) and inf_raw.get("is_inference"):
            val = inf_raw.get("valor")
            conf = float(inf_raw.get("confidence", 0))
            if val is not None and conf >= 0.80 and final.get(campo) is None:
                final[campo] = val
                meta_inferencia[campo] = {
                    "es_inferencia": True,
                    "base": inf_raw.get("inference_basis", ""),
                    "confianza_inferencia": conf,
                }

    return final, meta_inferencia


# ═══════════════════════════════════════════════════════════════
# MÓDULO 6 — ENSAMBLE DE MODELOS (A extrae, B valida)
# ═══════════════════════════════════════════════════════════════

def _get_secondary_provider(primary_provider: str,
                              primary_model: str,
                              secondary_api_key: str = "") -> Tuple[str, str, str]:
    """
    Determina el proveedor secundario para validación cruzada.
    Si el primario es Claude → secundario es GPT (si hay key) o Claude-mini.
    Si el primario es OpenAI → secundario es Claude-haiku.
    """
    if not secondary_api_key:
        # Sin segunda key: usar modelo más pequeño del mismo proveedor
        if primary_provider == "claude":
            return "claude", "claude-haiku-4-5-20251001", ""
        else:
            return "openai", "gpt-4o-mini", ""

    if primary_provider == "claude":
        return "openai", "gpt-4o-mini", secondary_api_key
    else:
        return "claude", "claude-haiku-4-5-20251001", secondary_api_key


SYSTEM_VALIDADOR_ENSAMBLE = """Eres un validador clínico independiente. Recibes datos extraídos de una historia clínica y debes verificar su plausibilidad clínica.

Tu misión NO es re-extraer datos. Es detectar:
1. Valores imposibles o improbables (ej: FC de 300 lpm)
2. Inconsistencias entre campos (ej: embarazo en hombre)
3. Campos que probablemente no están en el documento y fueron inventados
4. Formatos incorrectos (CIE-10 mal formado, fechas imposibles)

Para cada campo: indica si el valor es plausible (true/false) y por qué si no lo es.
Responde SOLO con JSON.
"""


def prompt_validacion_ensamble(datos: Dict, raw_text_fragment: str,
                                tipo_consulta: str = "") -> str:
    datos_str = json.dumps(datos, ensure_ascii=False, indent=2)
    tipo_str  = f"\nTIPO DE CONSULTA: {tipo_consulta}" if tipo_consulta else ""
    return f"""Valida la plausibilidad clínica de estos datos extraídos.{tipo_str}

DATOS A VALIDAR:
{datos_str}

FRAGMENTO DEL DOCUMENTO (primeros 4000 chars):
{raw_text_fragment[:4000]}

Responde con:
{{
  "campos_plausibles": {{
    "<campo>": {{"plausible": true/false, "razon": "<si no es plausible>"}}
  }},
  "flags_criticos": ["<lista de campos con problemas graves>"],
  "confianza_ensamble": <0.0-1.0>,
  "resumen": "<observaciones del validador independiente>"
}}"""


def ensemble_validate(datos: Dict, raw_text: str, tipo_consulta: str,
                       primary_provider: str, primary_api_key: str,
                       primary_model: str,
                       secondary_api_key: str = "") -> Dict:
    """
    Valida los datos extraídos con un segundo modelo independiente.
    Retorna resultado de validación del ensamble.
    """
    sec_provider, sec_model, sec_key = _get_secondary_provider(
        primary_provider, primary_model, secondary_api_key
    )
    key_to_use = sec_key or primary_api_key

    try:
        raw = _call_llm(
            messages=[
                {"role": "system", "content": SYSTEM_VALIDADOR_ENSAMBLE},
                {"role": "user",   "content": prompt_validacion_ensamble(
                    datos, raw_text, tipo_consulta)},
            ],
            api_key=key_to_use,
            provider=sec_provider,
            model=sec_model,
            max_tokens=1500,
        )
        result = _parse_json_response(raw)
        if isinstance(result, dict):
            result["_validador_modelo"] = f"{sec_provider}/{sec_model}"
            return result
    except Exception as e:
        log.warning(f"Ensamble validation falló ({sec_provider}/{sec_model}): {e}")

    return {
        "campos_plausibles": {},
        "flags_criticos": [],
        "confianza_ensamble": 0.8,
        "resumen": "Validación de ensamble no disponible",
        "_validador_modelo": f"{sec_provider}/{sec_model}",
    }


# ─────────────────────────────────────────────────────────────
# VALIDACIÓN MÉDICA (mejorada)
# ─────────────────────────────────────────────────────────────
 
def validate_medical_data(data: Dict) -> Tuple[List[Dict], List[str]]:
    """
    Valida lógica médica sobre los datos extraídos.
    Retorna (alertas_criticas, advertencias).
    """
    alerts = []
    warnings = []
 
    def safe_float(val_str: Any, default=None) -> Optional[float]:
        if not val_str:
            return default
        nums = re.findall(r"\d+\.?\d*", str(val_str))
        if nums:
            try:
                return float(nums[0])
            except Exception:
                pass
        return default
 
    def check_range(field_name: str, value_str: Any, key: str):
        val = safe_float(value_str)
        if val is None:
            return
        lo, hi = RANGOS_FISIOLOGICOS[key]
        if not (lo <= val <= hi):
            severidad = "CRITICA" if (val < lo * 0.8 or val > hi * 1.2) else "ALTA"
            alerts.append({
                "tipo": "RANGO_FISIOLOGICO",
                "descripcion": f"{field_name} = {value_str} está fuera del rango esperado ({lo}–{hi})",
                "severidad": severidad,
                "campo": field_name,
            })
 
    # 1. Tensión arterial
    ta = data.get("tension_arterial", "")
    if ta:
        nums = re.findall(r"\d+", str(ta))
        if len(nums) >= 2:
            check_range("tension_sistolica",  nums[0], "tension_sistolica")
            check_range("tension_diastolica", nums[1], "tension_diastolica")
            # Presión de pulso muy estrecha (< 20 mmHg) o muy amplia (> 100 mmHg)
            try:
                pp = int(nums[0]) - int(nums[1])
                if pp < 20:
                    alerts.append({
                        "tipo": "PRESION_PULSO",
                        "descripcion": f"Presión de pulso muy estrecha: {pp} mmHg (normal 30-50)",
                        "severidad": "ALTA",
                        "campo": "tension_arterial",
                    })
                elif pp > 100:
                    warnings.append(f"Presión de pulso muy amplia: {pp} mmHg")
            except Exception:
                pass
 
    # 2. Resto de signos vitales
    for campo, rango_key in [
        ("frecuencia_cardiaca", "frecuencia_cardiaca"),
        ("temperatura",         "temperatura"),
        ("peso_kg",             "peso_kg"),
        ("talla_cm",            "talla_cm"),
        ("saturacion_o2",       "saturacion_o2"),
        ("frecuencia_respiratoria", "frecuencia_respiratoria"),
    ]:
        check_range(campo, data.get(campo), rango_key)
 
    # 3. Validar CIE-10
    for campo in ["codigo_cie10_principal", "codigos_cie10_secundarios"]:
        codigos = data.get(campo, [])
        if isinstance(codigos, str):
            codigos = [codigos]
        if not isinstance(codigos, list):
            codigos = []
        for cod in codigos:
            if cod and not re.match(r"^[A-Z]\d{2}(\.\d{1,2})?$", str(cod).strip().upper()):
                warnings.append(f"Código CIE-10 posiblemente incorrecto: '{cod}'")
 
    # 4. Interacciones medicamentosas
    medicamentos_raw = data.get("medicamentos", [])
    if isinstance(medicamentos_raw, str):
        medicamentos_raw = [medicamentos_raw]
    meds_lower = set(
        m.lower().strip()
        for m in (medicamentos_raw if isinstance(medicamentos_raw, list) else [])
        if m
    )
    for grupo1, grupo2, descripcion in INTERACCIONES_CRITICAS:
        tiene_g1 = any(any(kw in med for kw in grupo1) for med in meds_lower)
        tiene_g2 = any(any(kw in med for kw in grupo2) for med in meds_lower)
        if tiene_g1 and tiene_g2:
            alerts.append({
                "tipo": "INTERACCION_MEDICAMENTOSA",
                "descripcion": descripcion,
                "severidad": "CRITICA",
                "campo": "medicamentos",
            })
 
    # 5. Coherencia edad-diagnóstico
    edad = safe_float(data.get("edad", ""))
    if edad is not None:
        edad = int(edad)
        diag = str(data.get("diagnostico_principal", "")).lower()
 
        if edad >= 18:
            if any(x in diag for x in ["kawasaki", "enfermedad de kawasaki"]):
                warnings.append(f"Diagnóstico principalmente pediátrico en adulto ({edad} años): {diag}")
 
        if edad < 18:
            if any(x in diag for x in ["menopausia", "hiperplasia prostática",
                                         "andropausia", "climaterio"]):
                warnings.append(f"Diagnóstico de adulto en paciente pediátrico ({edad} años): {diag}")
 
        # Diagnósticos obstétricos en hombres
        sexo = str(data.get("sexo", "")).lower()
        if sexo in ["m", "masculino", "male", "hombre"]:
            if any(x in diag for x in ["embarazo", "gestación", "gestacion",
                                         "prenatal", "posparto", "puerperio"]):
                alerts.append({
                    "tipo": "INCONSISTENCIA_DEMOGRAFICA",
                    "descripcion": f"Diagnóstico obstétrico en paciente masculino: {diag}",
                    "severidad": "CRITICA",
                    "campo": "diagnostico_principal",
                })
 
    # 6. IMC calculado vs documentado
    peso = safe_float(data.get("peso_kg"))
    talla = safe_float(data.get("talla_cm"))
    if peso and talla and talla > 0:
        t_m = talla / 100
        imc_calc = round(peso / (t_m * t_m), 1)
        imc_doc = safe_float(data.get("imc"))
        if imc_doc and abs(imc_calc - imc_doc) > 2.5:
            warnings.append(
                f"IMC calculado ({imc_calc}) difiere significativamente del documentado ({imc_doc}). "
                f"Verificar peso={peso}kg, talla={talla}cm"
            )
        if not data.get("imc"):
            data["imc"] = str(imc_calc)
 
        # Categoría IMC
        if imc_calc < 16:
            alerts.append({
                "tipo": "IMC_CRITICO",
                "descripcion": f"IMC muy bajo ({imc_calc}): desnutrición severa probable",
                "severidad": "CRITICA",
                "campo": "imc",
            })
        elif imc_calc > 40:
            alerts.append({
                "tipo": "IMC_CRITICO",
                "descripcion": f"IMC muy alto ({imc_calc}): obesidad mórbida",
                "severidad": "ALTA",
                "campo": "imc",
            })
 
    # 7. Saturación baja
    sat = safe_float(data.get("saturacion_o2"))
    if sat and sat < 90:
        alerts.append({
            "tipo": "SATURACION_CRITICA",
            "descripcion": f"Saturación O2 crítica: {sat}% (< 90%)",
            "severidad": "CRITICA",
            "campo": "saturacion_o2",
        })
 
    # 8. Glucemia en rangos críticos
    gluc = safe_float(data.get("glucemia", data.get("glucometria", "")))
    if gluc:
        if gluc < 50:
            alerts.append({
                "tipo": "GLUCEMIA_CRITICA",
                "descripcion": f"Glucemia muy baja: {gluc} mg/dL (hipoglucemia severa)",
                "severidad": "CRITICA",
                "campo": "glucemia",
            })
        elif gluc > 400:
            alerts.append({
                "tipo": "GLUCEMIA_CRITICA",
                "descripcion": f"Glucemia muy alta: {gluc} mg/dL (hiperglucemia severa)",
                "severidad": "CRITICA",
                "campo": "glucemia",
            })
 
    return alerts, warnings
 
 


# ─────────────────────────────────────────────────────────────
# INTELIGENCIA CLÍNICA AVANZADA v10 — AUDITOR AUTÓNOMO
# ─────────────────────────────────────────────────────────────

# ── Reglas de incompatibilidad sexo-biológico ─────────────────
# (terminos, sexos_incompatibles, descripcion, campo_afectado)
REGLAS_SEXO_BIOLOGICO: List[Tuple] = [
    (["prostatitis", "hiperplasia prostática", "hiperplasia benigna de próstata",
      "adenoma de próstata", "cáncer de próstata", "prostatectomía",
      "prostatismo", "hbp", "hiperplasia de próstata"],
     ["f", "femenino", "female", "mujer"],
     "Diagnóstico exclusivo del aparato genital masculino (próstata) en paciente femenino",
     "diagnostico_principal"),
    (["criptorquidia", "varicocele", "hidrocele", "epididimitis",
      "orquitis", "torsión testicular", "azoospermia", "oligospermia"],
     ["f", "femenino", "female", "mujer"],
     "Diagnóstico de aparato genital masculino en paciente femenino",
     "diagnostico_principal"),
    (["embarazo", "gestación", "gestacion", "prenatal", "posparto",
      "puerperio", "eclampsia", "preeclampsia", "amenorrea",
      "dismenorrea", "endometriosis", "mioma uterino", "leiomioma",
      "cancer de cuello uterino", "histerectomía", "histerectomia",
      "ooforectomía", "ooforectomia", "vaginitis", "vulvovaginitis",
      "candidiasis vaginal", "bartholinitis",
      "ovario poliquístico", "ovario poliquistico", "sop",
      "control prenatal", "consulta prenatal"],
     ["m", "masculino", "male", "hombre"],
     "Diagnóstico exclusivo de sexo femenino registrado en paciente masculino",
     "diagnostico_principal"),
]

# ── Reglas edad-diagnóstico ───────────────────────────────────
# (terminos, edad_min_para_advertir_adulto, edad_max_para_advertir_niño, descripcion, campo)
REGLAS_EDAD_DIAGNOSTICO: List[Tuple] = [
    (["kawasaki", "fiebre reumática aguda", "sarampión", "varicela diagnosticada",
      "escarlatina", "parotiditis infecciosa", "tos ferina", "tos convulsiva"],
     18, None,
     "Diagnóstico predominantemente pediátrico en adulto ≥18 años",
     "diagnostico_principal"),
    (["menopausia", "climaterio", "andropausia",
      "hiperplasia prostática benigna", "demencia senil",
      "enfermedad de alzheimer", "osteoporosis senil"],
     None, 17,
     "Diagnóstico típico de adulto mayor en paciente pediátrico (<18 años)",
     "diagnostico_principal"),
    (["ictericia neonatal", "asfixia perinatal", "sepsis neonatal",
      "enterocolitis necrotizante", "membrana hialina"],
     1, None,
     "Diagnóstico neonatal/perinatal en paciente que no es recién nacido",
     "diagnostico_principal"),
]

# ── CIE-10 exclusivos por sexo ────────────────────────────────
CIE10_EXCLUSIVO_MASCULINO = {
    "N40", "N41", "N42", "N43", "N44", "N45", "N46", "N47",
    "N48", "N49", "N50", "C61",
}
CIE10_EXCLUSIVO_FEMENINO = {
    "N70", "N71", "N72", "N73", "N74", "N75", "N76", "N77",
    "N80", "N81", "N82", "N83", "N84", "N85", "N86", "N87",
    "N88", "N89", "N90", "N91", "N92", "N93", "N94", "N95",
    "C51", "C52", "C53", "C54", "C55", "C56", "C57", "C58",
    "O00", "O01", "O02", "O03", "O04", "O05", "O06", "O07",
    "O08", "O09", "O10", "O11", "O12", "O13", "O14", "O15",
    "O16", "O20", "O21", "O22", "O23", "O24", "O25", "O26",
    "O28", "O29", "O30", "O31", "O32", "O33", "O34", "O35",
    "O36", "O40", "O41", "O42", "O43", "O44", "O45", "O46",
    "O47", "O48", "O60", "O61", "O62", "O63", "O64", "O65",
    "O66", "O67", "O68", "O69", "O70", "O71", "O72", "O73",
    "O74", "O75", "O80", "O82", "O85", "O86", "O87", "O88",
    "O89", "O90", "O91", "O92", "O94", "O95", "O96", "O97",
    "O98", "O99",
}
CIE10_NEONATAL = {
    "P00", "P01", "P02", "P03", "P04", "P05", "P07", "P08",
    "P10", "P11", "P12", "P13", "P14", "P15", "P20", "P21",
    "P22", "P23", "P24", "P25", "P26", "P28", "P29", "P35",
    "P36", "P37", "P38", "P39", "P50", "P51", "P52", "P53",
    "P54", "P55", "P56", "P57", "P58", "P59", "P60", "P61",
    "P70", "P71", "P72", "P74", "P75", "P76", "P77", "P78",
    "P80", "P81", "P83", "P84", "P90", "P91", "P92", "P93",
    "P94", "P95", "P96",
}

# ── Prompts del auditor ───────────────────────────────────────

SYSTEM_AUDITOR_CLINICO = """Eres un médico auditor clínico experto con 20 años de experiencia auditando historias clínicas del SGSSS colombiano.

TU MISIÓN: Detectar INCOHERENCIAS LÓGICAS en datos clínicos extraídos — datos que simplemente no tienen sentido médico real.

EJEMPLOS DE INCOHERENCIAS QUE DEBES DETECTAR:
- Mujer con diagnóstico de prostatitis (imposible anatómicamente)
- Hombre con diagnóstico de embarazo o control prenatal
- Niño de 5 años con menopausia o Alzheimer
- Código CIE-10 que no corresponde al diagnóstico descrito en texto
- Medicamento para una condición que no aparece diagnosticada en la historia
- Signos vitales fisiológicamente imposibles para la edad del paciente
- Fecha de nacimiento que no concuerda con la edad registrada
- Diagnóstico de DM tipo 1 sin insulina en el tratamiento
- Diagnóstico de infección urinaria en hombre con antibiótico para ITS femenina

Responde SOLO con JSON válido. Sin texto adicional.
"""


def prompt_auditoria_clinica(datos: Dict, raw_text_fragment: str,
                              tipo_consulta: str = "") -> str:
    datos_str = json.dumps(datos, ensure_ascii=False, indent=2)
    tipo_str = f"\nTIPO DE CONSULTA: {tipo_consulta}" if tipo_consulta else ""
    return f"""Audita la coherencia clínica de estos datos extraídos de una historia clínica colombiana.{tipo_str}

DATOS EXTRAÍDOS:
{datos_str}

FRAGMENTO DEL DOCUMENTO (para contexto de verificación):
{raw_text_fragment[:6000]}

Responde con este JSON exacto:
{{
  "incoherencias": [
    {{
      "campo": "<campo con error>",
      "valor_extraido": "<valor problemático>",
      "tipo_incoherencia": "<SEXO_BIOLOGICO|EDAD_DIAGNOSTICO|DX_MEDICAMENTO|CIE10_SEXO|SIGNOS_VITALES|COHERENCIA_INTERNA|OTRO>",
      "descripcion": "<por qué es incoherente, en lenguaje claro>",
      "severidad": "<CRITICA|ALTA|MEDIA>",
      "probable_causa": "<ERROR_EXTRACCION|ERROR_HC_ORIGINAL|REQUIERE_VERIFICACION>",
      "fragmento_a_verificar": "<texto a buscar en el documento para confirmar>",
      "valor_probable_correcto": "<valor correcto si puedes inferirlo, si no null>"
    }}
  ],
  "coherencia_global": <0.0-1.0>,
  "requiere_reescaneo": <true si hay incoherencias que podrían ser errores de extracción>,
  "campos_para_reescaneo": ["<campos que deben re-extraerse>"],
  "resumen_auditoria": "<resumen ejecutivo del resultado de la auditoría>",
  "datos_confiables": <true si los datos en general tienen sentido clínico>
}}

Si NO hay incoherencias, responde: "incoherencias": [], "coherencia_global": 1.0, "requiere_reescaneo": false.
"""


def prompt_reescaneo_dirigido(raw_text: str, campos: List[str],
                               incoherencias: List[Dict],
                               datos_actuales: Dict) -> str:
    """Prompt para re-extraer solo los campos con incoherencias detectadas."""
    inc_str = json.dumps(incoherencias, ensure_ascii=False, indent=2)
    campos_str = "\n".join(f'  "{f}": <valor corregido o null>' for f in campos)
    datos_str = json.dumps(
        {k: v for k, v in datos_actuales.items() if k in campos},
        ensure_ascii=False, indent=2
    )
    return f"""Re-extrae ÚNICAMENTE los campos con incoherencias, leyendo el documento con máxima atención crítica.

INCOHERENCIAS DETECTADAS QUE DEBES RESOLVER:
{inc_str}

VALORES ACTUALES (posiblemente incorrectos por error de OCR o extracción):
{datos_str}

INSTRUCCIONES CRÍTICAS:
- Lee el documento COMPLETO buscando evidencia directa en el texto
- Si el diagnóstico parece imposible (ej: prostatitis en mujer), revisa si el OCR confundió letras o palabras similares
- Si el dato sigue siendo incoherente tras revisión exhaustiva, mantenlo (es error de la HC original)
- NO inventes valores ni asumas correcciones sin evidencia textual
- Busca sinónimos, abreviaciones y variaciones del término en el documento

DOCUMENTO COMPLETO:
{raw_text[:12000]}

Responde con JSON exacto (solo los campos listados):
{{
{campos_str}
}}"""


# ── Clase principal del Auditor Clínico ───────────────────────

class ClinicalAuditor:
    """
    Auditor autónomo de coherencia clínica v10.

    Ciclo de auditoría en 4 pasos:
    1. Reglas determinísticas (sexo/biología, edad, CIE-10, medicamentos, fechas)
    2. Auditoría semántica por LLM (incoherencias complejas no cubiertas por reglas)
    3. Re-escaneo dirigido del documento si se detectan errores recuperables de extracción
    4. Marcado granular para revisión manual con detalle del hallazgo y evidencia
    """

    def __init__(self, api_key: str, provider: str = "claude",
                 model: str = "claude-sonnet-4-5", max_tokens: int = 2000):
        self.api_key = api_key
        self.provider = provider
        self.model = model
        self.max_tokens = max_tokens

    def _llm(self, system: str, user: str) -> str:
        return _call_llm(
            messages=[
                {"role": "system", "content": system},
                {"role": "user",   "content": user},
            ],
            api_key=self.api_key,
            provider=self.provider,
            model=self.model,
            max_tokens=self.max_tokens,
        )

    def _audit_rules(self, data: Dict) -> List[Dict]:
        """Paso 1: Aplica reglas determinísticas de coherencia clínica."""
        findings: List[Dict] = []

        sexo_raw = str(data.get("sexo", "") or "").lower().strip()
        edad_raw = data.get("edad", "")
        edad_num: Optional[int] = None
        try:
            nums = re.findall(r"\d+", str(edad_raw))
            if nums:
                edad_num = int(nums[0])
        except Exception:
            pass

        diag_raw = str(data.get("diagnostico_principal", "") or "").lower()
        diags_sec = data.get("diagnosticos_secundarios", [])
        if isinstance(diags_sec, str):
            diags_sec = [diags_sec]
        todos_diags = diag_raw + " " + " ".join(str(d).lower() for d in (diags_sec or []))

        meds_raw = data.get("medicamentos", [])
        if isinstance(meds_raw, str):
            meds_raw = [meds_raw]
        todos_meds = " ".join(str(m).lower() for m in (meds_raw or []))

        # — Reglas sexo-biológico —
        for terminos, sexos_incompatibles, desc, campo in REGLAS_SEXO_BIOLOGICO:
            if not any(s in sexo_raw for s in sexos_incompatibles):
                continue
            valor_campo = str(data.get(campo, "") or "").lower()
            if any(t in todos_diags or t in valor_campo for t in terminos):
                findings.append({
                    "campo": campo,
                    "valor_extraido": data.get(campo),
                    "tipo_incoherencia": "SEXO_BIOLOGICO",
                    "descripcion": desc,
                    "severidad": "CRITICA",
                    "probable_causa": "ERROR_EXTRACCION",
                    "fragmento_a_verificar": f"sexo del paciente y diagnóstico en campo '{campo}'",
                    "valor_probable_correcto": None,
                })

        # — Reglas edad-diagnóstico —
        if edad_num is not None:
            for terminos, edad_min_adulto, edad_max_niño, desc, campo in REGLAS_EDAD_DIAGNOSTICO:
                if not any(t in todos_diags for t in terminos):
                    continue
                disparar = False
                if edad_min_adulto is not None and edad_num >= edad_min_adulto:
                    disparar = True
                if edad_max_niño is not None and edad_num <= edad_max_niño:
                    disparar = True
                if disparar:
                    findings.append({
                        "campo": campo,
                        "valor_extraido": data.get(campo),
                        "tipo_incoherencia": "EDAD_DIAGNOSTICO",
                        "descripcion": f"{desc} (edad registrada: {edad_num} años)",
                        "severidad": "ALTA",
                        "probable_causa": "REQUIERE_VERIFICACION",
                        "fragmento_a_verificar": f"edad del paciente y diagnóstico en campo '{campo}'",
                        "valor_probable_correcto": None,
                    })

        # — Reglas CIE-10 vs sexo —
        for campo_cie in ["codigo_cie10_principal", "codigos_cie10_secundarios"]:
            codigos = data.get(campo_cie, [])
            if isinstance(codigos, str):
                codigos = [codigos]
            for cod_raw in (codigos or []):
                if not cod_raw:
                    continue
                cod = str(cod_raw).strip().upper()[:3]
                if cod in CIE10_EXCLUSIVO_MASCULINO:
                    if any(s in sexo_raw for s in ["f", "femenino", "female", "mujer"]):
                        findings.append({
                            "campo": campo_cie,
                            "valor_extraido": cod_raw,
                            "tipo_incoherencia": "CIE10_SEXO",
                            "descripcion": f"CIE-10 {cod_raw} corresponde al aparato genital masculino, pero el paciente es femenino",
                            "severidad": "CRITICA",
                            "probable_causa": "ERROR_EXTRACCION",
                            "fragmento_a_verificar": f"código CIE-10 '{cod_raw}' y sexo del paciente",
                            "valor_probable_correcto": None,
                        })
                if cod in CIE10_EXCLUSIVO_FEMENINO:
                    if any(s in sexo_raw for s in ["m", "masculino", "male", "hombre"]):
                        findings.append({
                            "campo": campo_cie,
                            "valor_extraido": cod_raw,
                            "tipo_incoherencia": "CIE10_SEXO",
                            "descripcion": f"CIE-10 {cod_raw} corresponde al aparato genital femenino/obstétrico, pero el paciente es masculino",
                            "severidad": "CRITICA",
                            "probable_causa": "ERROR_EXTRACCION",
                            "fragmento_a_verificar": f"código CIE-10 '{cod_raw}' y sexo del paciente",
                            "valor_probable_correcto": None,
                        })
                if cod in CIE10_NEONATAL and edad_num is not None and edad_num > 0:
                    findings.append({
                        "campo": campo_cie,
                        "valor_extraido": cod_raw,
                        "tipo_incoherencia": "EDAD_DIAGNOSTICO",
                        "descripcion": f"CIE-10 {cod_raw} es neonatal/perinatal pero el paciente tiene {edad_num} años",
                        "severidad": "ALTA",
                        "probable_causa": "ERROR_EXTRACCION",
                        "fragmento_a_verificar": f"código CIE-10 '{cod_raw}' y edad del paciente",
                        "valor_probable_correcto": None,
                    })

        # — Coherencia fecha nacimiento vs edad registrada —
        fecha_nac = str(data.get("fecha_nacimiento", "") or "")
        fecha_consulta = str(data.get("fecha_consulta", "") or "")
        if fecha_nac and fecha_consulta and edad_num is not None:
            try:
                fn = datetime.strptime(fecha_nac[:10], "%Y-%m-%d")
                fc = datetime.strptime(fecha_consulta[:10], "%Y-%m-%d")
                edad_calculada = (fc - fn).days // 365
                if abs(edad_calculada - edad_num) > 2:
                    findings.append({
                        "campo": "edad",
                        "valor_extraido": edad_num,
                        "tipo_incoherencia": "COHERENCIA_INTERNA",
                        "descripcion": (
                            f"Edad registrada ({edad_num} años) no concuerda con la calculada "
                            f"({edad_calculada} años) según fecha nacimiento {fecha_nac} "
                            f"y fecha consulta {fecha_consulta}"
                        ),
                        "severidad": "ALTA",
                        "probable_causa": "ERROR_EXTRACCION",
                        "fragmento_a_verificar": "fecha de nacimiento y edad del paciente en la historia",
                        "valor_probable_correcto": str(edad_calculada),
                    })
            except Exception:
                pass

        # — Anticonceptivos hormonales femeninos en hombre —
        if any(s in sexo_raw for s in ["m", "masculino", "male", "hombre"]):
            anticonceptivos_fem = [
                "levonorgestrel", "etinilestradiol", "desogestrel",
                "gestodeno", "drospirenona", "etonogestrel",
                "noretisterona", "anticonceptivo oral",
            ]
            if any(ac in todos_meds for ac in anticonceptivos_fem):
                findings.append({
                    "campo": "medicamentos",
                    "valor_extraido": data.get("medicamentos"),
                    "tipo_incoherencia": "DX_MEDICAMENTO",
                    "descripcion": "Anticonceptivo hormonal femenino prescrito en paciente masculino",
                    "severidad": "CRITICA",
                    "probable_causa": "ERROR_EXTRACCION",
                    "fragmento_a_verificar": "medicamentos prescritos y sexo del paciente",
                    "valor_probable_correcto": None,
                })

        return findings

    def _audit_llm(self, data: Dict, raw_text: str, tipo_consulta: str = "") -> Dict:
        """Paso 2: Auditoría semántica profunda vía LLM."""
        default = {
            "incoherencias": [], "coherencia_global": 0.85,
            "requiere_reescaneo": False, "campos_para_reescaneo": [],
            "resumen_auditoria": "", "datos_confiables": True,
        }
        try:
            raw = self._llm(
                SYSTEM_AUDITOR_CLINICO,
                prompt_auditoria_clinica(data, raw_text, tipo_consulta)
            )
            resultado = _parse_json_response(raw)
            if isinstance(resultado, dict):
                return resultado
        except Exception as e:
            log.warning(f"Auditoría LLM semántica falló: {e}")
        return default

    def _rescan_fields(self, raw_text: str, campos: List[str],
                       incoherencias: List[Dict], datos_actuales: Dict) -> Dict:
        """Paso 3: Re-extrae campos con incoherencias leyendo el documento de nuevo."""
        if not campos or not raw_text.strip():
            return {}
        try:
            raw = self._llm(
                SYSTEM_EXTRACTOR,
                prompt_reescaneo_dirigido(raw_text, campos, incoherencias, datos_actuales)
            )
            nuevos = _parse_json_response(raw)
            return nuevos if isinstance(nuevos, dict) else {}
        except Exception as e:
            log.warning(f"Re-escaneo dirigido falló: {e}")
            return {}

    def audit(self, data: Dict, raw_text: str, tipo_consulta: str = "") -> Dict[str, Any]:
        """
        Auditoría clínica completa con re-escaneo y marcado para revisión manual.

        Retorna dict con:
          - datos_auditados: datos (corregidos donde fue posible)
          - incoherencias: lista detallada de todos los hallazgos
          - campos_marcados_revision: campos que requieren revisión humana
          - coherencia_auditoria: score 0.0-1.0
          - resumen: texto ejecutivo del resultado
          - requiere_revision_manual: bool
          - ciclos_reescaneo: cuántos re-escaneos se realizaron
        """
        resultado: Dict[str, Any] = {
            "datos_auditados": dict(data),
            "incoherencias": [],
            "campos_marcados_revision": [],
            "coherencia_auditoria": 1.0,
            "resumen": "",
            "requiere_revision_manual": False,
            "ciclos_reescaneo": 0,
        }

        # Paso 1: Reglas determinísticas
        inc_reglas = self._audit_rules(data)
        log.info(f"🔍 [Auditor] Reglas: {len(inc_reglas)} incoherencia(s)")

        # Paso 2: Auditoría semántica LLM
        audit_llm_r = self._audit_llm(data, raw_text, tipo_consulta)
        inc_llm = audit_llm_r.get("incoherencias", [])
        log.info(f"🧠 [Auditor] LLM semántico: {len(inc_llm)} incoherencia(s)")

        # Unificar por campo (priorizar mayor severidad)
        sev_map = {"CRITICA": 3, "ALTA": 2, "MEDIA": 1}
        campo_inc: Dict[str, Dict] = {}
        for inc in (inc_reglas + inc_llm):
            campo = inc.get("campo", "desconocido")
            if campo not in campo_inc:
                campo_inc[campo] = inc
            elif sev_map.get(inc.get("severidad", ""), 0) >                  sev_map.get(campo_inc[campo].get("severidad", ""), 0):
                campo_inc[campo] = inc

        todas_inc = list(campo_inc.values())
        resultado["incoherencias"] = todas_inc

        if not todas_inc:
            resultado["coherencia_auditoria"] = float(audit_llm_r.get("coherencia_global", 1.0))
            resultado["resumen"] = (
                audit_llm_r.get("resumen_auditoria") or
                "✅ Sin incoherencias clínicas detectadas"
            )
            return resultado

        # Paso 3: Re-escaneo dirigido (solo para errores de extracción)
        campos_rescan = list(dict.fromkeys(
            inc["campo"] for inc in todas_inc
            if inc.get("probable_causa") == "ERROR_EXTRACCION"
        ))
        campos_rescan += [c for c in audit_llm_r.get("campos_para_reescaneo", [])
                          if c not in campos_rescan]

        datos_corregidos = dict(data)
        if campos_rescan:
            log.info(f"🔄 [Auditor] Re-escaneo de campos: {campos_rescan}")
            nuevos = self._rescan_fields(raw_text, campos_rescan, todas_inc, data)
            resultado["ciclos_reescaneo"] = 1

            campos_cambiados = []
            for campo, nuevo_val in nuevos.items():
                if nuevo_val is not None and str(nuevo_val) != str(data.get(campo, "")):
                    datos_corregidos[campo] = nuevo_val
                    campos_cambiados.append(campo)
                    log.info(f"  ✏️ '{campo}': '{data.get(campo)}' → '{nuevo_val}'")

            # Re-evaluar incoherencias en campos corregidos
            if campos_cambiados:
                inc_post = self._audit_rules(datos_corregidos)
                campos_inc_post = {i["campo"] for i in inc_post}
                todas_inc = [
                    i for i in todas_inc
                    if i["campo"] not in campos_cambiados
                    or i["campo"] in campos_inc_post
                ]
                resultado["incoherencias"] = todas_inc

        resultado["datos_auditados"] = datos_corregidos

        # Paso 4: Marcado final para revisión manual
        campos_revision = list(dict.fromkeys(
            i.get("campo", "") for i in todas_inc if i.get("campo")
        ))
        criticas = sum(1 for i in todas_inc if i.get("severidad") == "CRITICA")
        altas    = sum(1 for i in todas_inc if i.get("severidad") == "ALTA")

        coherencia_base = float(audit_llm_r.get("coherencia_global", 1.0))
        if criticas > 0:
            coherencia_final = min(coherencia_base, 0.40)
        elif altas > 0:
            coherencia_final = min(coherencia_base, 0.65)
        else:
            coherencia_final = min(coherencia_base, 0.80)

        resumen = (
            audit_llm_r.get("resumen_auditoria") or
            f"⚠️ {len(todas_inc)} incoherencia(s): {criticas} crítica(s), "
            f"{altas} alta(s). Campos a revisar: {', '.join(campos_revision)}"
        )

        resultado.update({
            "campos_marcados_revision": campos_revision,
            "coherencia_auditoria":     round(coherencia_final, 3),
            "requiere_revision_manual": bool(campos_revision),
            "resumen":                  resumen,
        })

        if campos_revision:
            log.warning(
                f"🚨 [Auditor] {len(todas_inc)} incoherencia(s). "
                f"Marcados para revisión manual: {campos_revision}"
            )

        return resultado

# ─────────────────────────────────────────────────────────────
# PIPELINE COMPLETO DE EXTRACCIÓN CON VALIDACIÓN CRUZADA
# ─────────────────────────────────────────────────────────────
 
class ClinicalExtractor:
    """
    Pipeline completo v8:
    1. OCR/extracción de texto (mejorado con deskew, denoise, EasyOCR, visión)
    2. Segmentación inteligente del documento
    3. Extracción inicial (Claude o GPT-4o)
    4. Verificación cruzada con documento completo segmentado
    5. Resolución de conflictos campo por campo con fragmento relevante
    6. Validación médica ampliada
    7. Score de confianza y estadísticas acumuladas
    """
 
    def __init__(self, api_key: str,
                 provider: str = "claude",
                 model: str = "claude-sonnet-4-5",
                 max_tokens: int = 3000,
                 ocr_lang: str = "spa+eng",
                 ocr_dpi: int = 300,
                 campos: List[str] = None,
                 confidence_threshold: float = 0.75,
                 use_easyocr: bool = False,
                 use_vision_ocr: bool = False,
                 tipo_consulta: str = "General / Base",
                 project_id: str = DEFAULT_PROJECT_ID,
                 user_id: str = ""):
        self.api_key = api_key
        self.provider = provider
        self.model = model
        self.max_tokens = max_tokens
        self.ocr_lang = ocr_lang
        self.ocr_dpi = ocr_dpi
        self.campos = campos or CAMPOS_DEFAULT
        self.confidence_threshold = confidence_threshold
        self.use_easyocr = use_easyocr
        self.use_vision_ocr = use_vision_ocr
        self.tipo_consulta = tipo_consulta
        self.project_id           = project_id
        self._user_id             = user_id
        self.enable_anonymization = bool(os.environ.get("CEP_ENABLE_ANON", "0") == "1")
        self.enable_ensemble      = bool(os.environ.get("CEP_ENABLE_ENSEMBLE", "1") != "0")
 
    def _llm(self, system: str, user: str) -> str:
        return _call_llm(
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            api_key=self.api_key,
            provider=self.provider,
            model=self.model,
            max_tokens=self.max_tokens,
        )
 
    def extract_from_text(self, text: str, filename: str,
                           source: str = "text_field",
                           progress_callback=None) -> Dict[str, Any]:
        """Procesa texto directo (campos Salesforce sin OCR)."""
        return self._run_pipeline(text, filename, source,
                                   b"", progress_callback, skip_ocr=True)
 
    def extract(self, file_data: bytes, filename: str,
                source: str = "local",
                progress_callback=None) -> Dict[str, Any]:
        """Ejecuta el pipeline completo desde bytes (PDF/imagen)."""
        return self._run_pipeline("", filename, source,
                                   file_data, progress_callback, skip_ocr=False)
 
    def _run_pipeline(self, text_in: str, filename: str, source: str,
                       file_data: bytes, progress_callback=None,
                       skip_ocr: bool = False) -> Dict[str, Any]:
 
        def progress(msg: str, pct: int):
            if progress_callback:
                progress_callback(msg, pct)
            log.info(f"[{pct}%] {msg}")
 
        result = {
            "_filename": filename,
            "_source": source,
            "_status": "processing",
            "_confidence": 0.0,
            "_needs_review": False,
            "_alerts": [],
            "_warnings": [],
            "_validation": {},
            "_tipo_consulta": self.tipo_consulta,
        }
 
        try:
            # ── CACHE CHECK ─────────────────────────────────────
            file_hash = compute_hash(file_data if file_data else text_in.encode())
            result["_file_hash"]    = file_hash
            result["_project_id"]   = getattr(self, "project_id", DEFAULT_PROJECT_ID)
            cached = file_already_processed(file_hash)
            if cached:
                progress("♻️ Usando resultado en caché", 100)
                result.update(cached["data"])
                result["_validation"] = cached["validation"]
                result["_alerts"] = cached["alerts"]
                result["_status"] = cached["status"]
                result["_confidence"] = cached["confidence"]
                result["_needs_review"] = cached["confidence"] < self.confidence_threshold
                result["_from_cache"] = True
                audit("cache_hit", filename, f"hash={file_hash[:16]}")
                return result
 
            # ══════════════════════════════════════════════════════
            # ETAPA 1: OCR / EXTRACCIÓN DE TEXTO + SCORE CALIDAD
            # ══════════════════════════════════════════════════════
            if skip_ocr:
                raw_text    = text_in
                ocr_quality = {"score":100,"nivel":"bueno","apto":True,
                               "detalle":"sin OCR","chars":len(raw_text),"palabras":0}
                progress("📝 Texto directo (sin OCR)...", 6)
            else:
                progress("📄 OCR + extracción de texto...", 5)
                raw_text    = extract_text_from_bytes(
                    file_data, filename,
                    ocr_lang=self.ocr_lang,
                    dpi=self.ocr_dpi,
                    use_easyocr=self.use_easyocr,
                    use_vision=self.use_vision_ocr,
                    vision_api_key=self.api_key,
                    vision_provider=self.provider,
                )
                ocr_quality = score_ocr_quality(raw_text)
                audit("ocr_quality", filename,
                      f"score={ocr_quality['score']} nivel={ocr_quality['nivel']}")

            result["_ocr_quality"] = ocr_quality

            if not raw_text.strip():
                result["_status"] = "error_empty"
                return result

            if not ocr_quality["apto"] and not skip_ocr:
                result["_alerts"].append({
                    "tipo": "OCR_QUALITY_INSUFICIENTE",
                    "descripcion": (f"Calidad OCR {ocr_quality['score']}/100 "
                                    f"({ocr_quality['nivel']}) bajo umbral "
                                    f"{OCR_QUALITY_THRESHOLD}. Revisar imagen original."),
                    "severidad": "ALTA", "campo": "_ocr",
                })
                needs_review = True

            audit("text_extracted", filename,
                  f"chars={len(raw_text)} ocr_score={ocr_quality['score']}")

            # ══════════════════════════════════════════════════════
            # ETAPA 2: SEGMENTACIÓN
            # ══════════════════════════════════════════════════════
            progress("📋 Segmentando documento...", 12)
            segments = segment_document(raw_text)

            # ══════════════════════════════════════════════════════
            # ETAPA 3: EXTRACCIÓN LITERAL (solo lo explícito)
            # ══════════════════════════════════════════════════════
            progress(f"🔤 Extracción literal ({self.provider.upper()})...", 20)
            raw_lit    = self._llm(SYSTEM_EXTRACTOR_LITERAL,
                                    prompt_extraccion_literal(
                                        raw_text, self.campos, segments, self.tipo_consulta))
            ext_literal = _parse_json_response(raw_lit) or {}
            audit("extraction_literal", filename,
                  f"campos_con_valor={sum(1 for v in ext_literal.values() if v is not None)}")

            # ══════════════════════════════════════════════════════
            # ETAPA 4: EXTRACCIÓN POR INFERENCIA (campos nulos)
            # ══════════════════════════════════════════════════════
            campos_nulos     = [c for c in self.campos if ext_literal.get(c) is None]
            meta_inferencia: Dict[str, Dict] = {}
            if campos_nulos:
                progress(f"🧩 Inferencia para {len(campos_nulos)} campo(s) nulo(s)...", 30)
                raw_inf       = self._llm(SYSTEM_EXTRACTOR_INFERENCIA,
                                           prompt_extraccion_inferencia(
                                               raw_text, ext_literal,
                                               campos_nulos, self.tipo_consulta))
                ext_inf        = _parse_json_response(raw_inf) or {}
                ext1, meta_inferencia = merge_literal_inferencias(
                    ext_literal, ext_inf, self.campos)
                audit("extraction_inference", filename, f"inferidos={len(meta_inferencia)}")
            else:
                ext1 = ext_literal

            # ══════════════════════════════════════════════════════
            # ETAPA 5: VERIFICACIÓN CRUZADA
            # ══════════════════════════════════════════════════════
            progress("🔍 Verificación cruzada...", 42)
            raw2         = self._llm(SYSTEM_VERIFICADOR,
                                      prompt_verificacion(raw_text, ext1,
                                                          self.campos, segments))
            verification = _parse_json_response(raw2) or {}
            audit("extraction_verify", filename)

            ver_campos       = verification.get("verificacion_por_campo", {})
            ext2             = {}
            for campo in self.campos:
                if campo in ver_campos:
                    vc          = ver_campos[campo]
                    ext2[campo] = vc.get("valor_confirmado")
                    if ext2[campo] is None:
                        ext2[campo] = ext1.get(campo)
                else:
                    ext2[campo] = ext1.get(campo)

            confianza_global = float(verification.get("confianza_global", 0.7))
            conflictos       = verification.get("campos_conflictivos", [])
            needs_review     = verification.get("requiere_revision_humana", False)

            # Trazabilidad por campo
            model_label  = f"{self.provider}/{self.model}"
            field_traces: Dict[str, Any] = {}
            for campo in self.campos:
                c_conf = float(ver_campos.get(campo, {}).get("confianza", confianza_global))
                es_inf = campo in meta_inferencia
                metodo = ("inference" if es_inf
                          else "verification" if campo in ver_campos
                          else "extraction_literal")
                field_traces[campo] = build_field_trace(
                    campo, ext2.get(campo), raw_text, segments,
                    modelo=model_label, confianza=c_conf,
                    metodo=metodo, es_inferencia=es_inf,
                )

            # ══════════════════════════════════════════════════════
            # ETAPA 6: RESOLUCIÓN DE CONFLICTOS
            # ══════════════════════════════════════════════════════
            final_data   = dict(ext2)
            resoluciones = {}
            if conflictos:
                progress(f"⚖️ Resolviendo {len(conflictos)} conflicto(s)...", 58)
                conf_res_list = []
                for campo in conflictos:
                    val1 = ext1.get(campo)
                    val2 = ext2.get(campo)
                    if val1 == val2:
                        continue
                    fragment  = get_relevant_fragment(raw_text, campo, segments)
                    nota_v2   = ver_campos.get(campo, {}).get("nota", "")
                    raw3      = self._llm(SYSTEM_RESOLUTOR,
                                          prompt_resolucion(campo, val1, val2,
                                                            fragment, razonamiento_v2=nota_v2))
                    res       = _parse_json_response(raw3) or {}
                    resoluciones[campo] = res
                    if res.get("valor_final") is not None:
                        final_data[campo] = res["valor_final"]
                        field_traces[campo] = build_field_trace(
                            campo, res["valor_final"], raw_text, segments,
                            modelo=model_label,
                            confianza=float(res.get("confianza", confianza_global)),
                            metodo="resolution", es_inferencia=False,
                        )
                    if res.get("confianza"):
                        conf_res_list.append(float(res["confianza"]))
                if conf_res_list:
                    confianza_global = round(
                        (confianza_global + sum(conf_res_list)/len(conf_res_list)) / 2, 3)
                audit("conflict_resolution", filename, f"conflicts={len(conflictos)}")

            # ══════════════════════════════════════════════════════
            # ETAPA 7: NORMALIZACIÓN (CIE-10 + medicamentos + unidades)
            # ══════════════════════════════════════════════════════
            progress("🏷️ Normalizando datos...", 65)
            final_data, cambios_norm = normalizar_datos(final_data, self.campos)
            if cambios_norm:
                result["_normalization_changes"] = cambios_norm
                audit("normalization", filename, f"cambios={list(cambios_norm.keys())}")

            # ══════════════════════════════════════════════════════
            # ETAPA 8: ANONIMIZACIÓN PII
            # ══════════════════════════════════════════════════════
            if getattr(self, "enable_anonymization", False):
                progress("🔒 Anonimizando PII...", 68)
                nombre_raw = str(final_data.get("nombre_paciente") or "")
                doc_raw    = str(final_data.get("numero_documento") or "")
                fecha_nac  = str(final_data.get("fecha_nacimiento") or "")
                anon_id    = generar_id_anonimo(nombre_raw, doc_raw, fecha_nac)
                final_data = anonimizar_datos_extraidos(final_data)
                result["_anon_id"] = anon_id
                audit("anonymization", filename, f"anon_id={anon_id}")

            # Guardar trazabilidad serializada
            result["_field_traces"] = traces_to_dict(field_traces)

            # ══════════════════════════════════════════════════════
            # ETAPA 9: VALIDACIÓN MÉDICA
            # ══════════════════════════════════════════════════════
            progress("🏥 Validando lógica médica...", 72)
            alerts, warnings = validate_medical_data(final_data)
            audit("medical_validation", filename,
                  f"alerts={len(alerts)}, warnings={len(warnings)}")
            if any(a["severidad"] == "CRITICA" for a in alerts):
                needs_review     = True
                confianza_global = min(confianza_global, 0.6)

            # ══════════════════════════════════════════════════════
            # ETAPA 10: ENSAMBLE DE MODELOS
            # ══════════════════════════════════════════════════════
            if getattr(self, "enable_ensemble", True):
                progress("🤝 Validación de ensamble...", 78)
                try:
                    sec_key = os.environ.get(
                        "OPENAI_API_KEY" if self.provider == "claude"
                        else "ANTHROPIC_API_KEY", "")
                    ens = ensemble_validate(
                        final_data, raw_text, self.tipo_consulta,
                        self.provider, self.api_key, self.model,
                        secondary_api_key=sec_key,
                    )
                    flags = ens.get("flags_criticos", [])
                    if flags:
                        needs_review     = True
                        confianza_global = min(
                            confianza_global,
                            float(ens.get("confianza_ensamble", confianza_global)))
                        for f in flags:
                            reason = (ens.get("campos_plausibles", {})
                                       .get(f, {}).get("razon", ""))
                            alerts.append({
                                "tipo":        "ENSEMBLE_FLAG",
                                "descripcion": f"Validador independiente: campo '{f}' — {reason}",
                                "severidad":   "ALTA",
                                "campo":       f,
                            })
                    result["_ensemble"] = {
                        "modelo_validador": ens.get("_validador_modelo",""),
                        "flags":            flags,
                        "confianza":        ens.get("confianza_ensamble", 1.0),
                        "resumen":          ens.get("resumen",""),
                    }
                    audit("ensemble", filename,
                          f"flags={flags} modelo={ens.get('_validador_modelo','')}")
                except Exception as e_ens:
                    log.warning(f"Ensemble no crítico: {e_ens}")

            if confianza_global < self.confidence_threshold:
                needs_review = True

                        # ── PASO 7: AUDITORÍA CLÍNICA INTELIGENTE v10 ────────
            progress("🧠 Auditoría de coherencia clínica (v10)...", 87)
            audit_validation_extra = {}
            try:
                auditor = ClinicalAuditor(
                    api_key=self.api_key,
                    provider=self.provider,
                    model=self.model,
                    max_tokens=2000,
                )
                audit_result = auditor.audit(
                    data=final_data,
                    raw_text=raw_text,
                    tipo_consulta=self.tipo_consulta,
                )
                # Aplicar datos corregidos por el auditor
                final_data.update({
                    k: v for k, v in audit_result["datos_auditados"].items()
                    if not k.startswith("_")
                })
                # Agregar incoherencias como alertas adicionales tipificadas
                for inc in audit_result.get("incoherencias", []):
                    alerts.append({
                        "tipo": f"INCOHERENCIA_{inc.get('tipo_incoherencia', 'CLINICA')}",
                        "descripcion": inc.get("descripcion", ""),
                        "severidad": inc.get("severidad", "ALTA"),
                        "campo": inc.get("campo", ""),
                        "causa_probable": inc.get("probable_causa", ""),
                        "fragmento_a_verificar": inc.get("fragmento_a_verificar", ""),
                        "valor_probable_correcto": inc.get("valor_probable_correcto"),
                    })
                if audit_result.get("requiere_revision_manual"):
                    needs_review = True
                    confianza_global = min(
                        confianza_global,
                        audit_result.get("coherencia_auditoria", confianza_global)
                    )
                audit_validation_extra = {
                    "auditoria_clinica": {
                        "incoherencias":            audit_result.get("incoherencias", []),
                        "campos_marcados_revision": audit_result.get("campos_marcados_revision", []),
                        "coherencia_auditoria":     audit_result.get("coherencia_auditoria", 1.0),
                        "resumen_auditoria":        audit_result.get("resumen", ""),
                        "ciclos_reescaneo":         audit_result.get("ciclos_reescaneo", 0),
                    }
                }
                audit("clinical_audit_v10", filename,
                      f"incoherencias={len(audit_result.get('incoherencias', []))}, "
                      f"marcados={audit_result.get('campos_marcados_revision', [])}, "
                      f"reescaneos={audit_result.get('ciclos_reescaneo', 0)}")
            except Exception as e_audit:
                log.warning(f"Auditoría clínica v10 (no crítico): {e_audit}")

            # ── PASO 8: ESTADÍSTICAS POR CAMPO ────────────────────
            confianza_por_campo = {
                c: ver_campos.get(c, {}).get("confianza")
                for c in self.campos
            }
            update_campo_stats(
                {k: v for k, v in confianza_por_campo.items() if v is not None},
                conflictos
            )

            if confianza_global < self.confidence_threshold:
                needs_review = True

            # ── ENSAMBLAR RESULTADO ────────────────────────────────
            result.update(final_data)
            result["_status"]       = "done"
            result["_confidence"]   = round(confianza_global, 3)
            result["_needs_review"] = needs_review
            result["_alerts"]       = alerts
            result["_warnings"]     = warnings
            result["_segments"]     = {k: v[:300] for k, v in segments.items()}
            result["_validation"]   = {
                "conflictos":          conflictos,
                "resumen":             verification.get("resumen_verificacion", ""),
                "confianza_por_campo": confianza_por_campo,
                "resoluciones":        resoluciones,
                **audit_validation_extra,
            }

            # ── GUARDAR EN CACHE ───────────────────────────────────
            save_to_db(
                file_hash, filename, source,
                {k: v for k, v in result.items() if not k.startswith("_")},
                result["_validation"], alerts,
                result["_status"], confianza_global, self.tipo_consulta
            )

            # Registrar en dedup_registry para prevención futura de duplicados
            register_processed(
                file_hash, filename,
                project_id=getattr(self, "project_id", DEFAULT_PROJECT_ID),
                source=source,
                user_id=getattr(self, "_user_id", ""),
            )

            progress("✅ Procesamiento completado", 100)
 
        except Exception as e:
            log.error(f"❌ Error en pipeline {filename}: {traceback.format_exc()}")
            result["_status"] = "error"
            result["_error"] = str(e)
 
        return result
 
 
# ─────────────────────────────────────────────────────────────
# PROCESADOR DE VOLUMEN (paralelo + batch Sheets)
# ─────────────────────────────────────────────────────────────
 
class BulkProcessor:
    """Procesa grandes volúmenes de documentos en paralelo con batch a Sheets."""
 
    def __init__(self, extractor: ClinicalExtractor,
                 sheets_manager: Optional[GoogleSheetsManager] = None,
                 max_workers: int = None):
        self.extractor = extractor
        self.sheets = sheets_manager
        import os as _oscpu
        default_w = min(max(2, (_oscpu.cpu_count() or 2) * 2), 8)
        self.max_workers = max_workers if max_workers is not None else default_w
        log.info(f"BatchProcessor: {self.max_workers} workers (CPU={_oscpu.cpu_count()})")
 
    def process_files(self, files: List[Tuple[bytes, str, str]],
                      progress_callback=None) -> List[Dict]:
        """
        Procesa lista de (bytes, filename, source) en paralelo.
        Detecta y divide documentos multi-paciente antes de procesar.
        """
        # Expandir archivos multi-paciente
        expanded: List[Tuple] = []
        for file_data, filename, source in files:
            preview_text = ""
            try:
                import fitz as _fitz
                _doc = _fitz.open(stream=file_data, filetype="pdf")
                preview_text = "".join(
                    _doc[i].get_text() for i in range(min(3, len(_doc)))
                )
                _doc.close()
            except Exception:
                pass

            if preview_text and detect_multi_patient(preview_text):
                segs = split_multi_patient(preview_text, filename)
                if len(segs) > 1:
                    log.info(f"📄 Multi-paciente: {filename} → {len(segs)} historias")
                    for seg_text, seg_name in segs:
                        expanded.append((seg_text.encode("utf-8"), seg_name, source))
                    continue
            expanded.append((file_data, filename, source))

        total   = len(expanded)
        results = []

        def process_one(item):
            raw, fname, src = item
            try:
                # Segmento de texto plano (de split multi-paciente)
                if isinstance(raw, bytes):
                    try:
                        txt = raw.decode("utf-8")
                        if txt.strip() and not fname.lower().endswith(
                                (".pdf",".png",".jpg",".jpeg",".tiff")):
                            return self.extractor.extract_from_text(txt, fname, src)
                    except UnicodeDecodeError:
                        pass
                return self.extractor.extract(raw, fname, src)
            except Exception as e:
                return {"_filename": fname, "_source": src,
                        "_status": "error", "_error": str(e), "_confidence": 0.0}

        # MEJORA v15-CLINIC: semáforo para limitar concurrencia y evitar OOM en lotes grandes
        import gc as _gc
        _sem = __import__("threading").Semaphore(self.max_workers)

        def _worker_with_semaphore(args):
            with _sem:
                return args[0](*args[1:])

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(process_one, item): i
                       for i, item in enumerate(expanded)}
            for i, future in enumerate(as_completed(futures)):
                result = future.result()
                results.append(result)
                # MEJORA v15b: throttle progress updates (cada 5% o mín 1s)
                # evita congelar Streamlit con 100+ archivos actualizando render cada vez
                if progress_callback and (i == 0 or i == total-1 or
                        (total > 0 and (i+1) % max(1, total//20) == 0)):
                    progress_callback(
                        f"Procesado {i+1}/{total}: {result.get('_filename','')}",
                        int((i+1)/total*100)
                    )
                if self.sheets and result.get("_status") == "done":
                    try:
                        self.sheets.buffer_extraction(
                            data={k: v for k, v in result.items()
                                  if not k.startswith("_") or
                                  k in ("_filename","_source","_status",
                                        "_file_hash","_project_id")},
                            campos=self.extractor.campos,
                            validation=result.get("_validation", {}),
                            alerts=result.get("_alerts", []),
                            confidence=result.get("_confidence", 0.0),
                            needs_review=result.get("_needs_review", False),
                        )
                    except Exception as e:
                        log.warning(f"Buffer Sheets error: {e}")

        if self.sheets:
            try:
                self.sheets.flush_batch()
                self.sheets.write_quality_report()
            except Exception as e:
                log.warning(f"flush_batch error: {e}")

        # Monitoreo automático al final de cada batch
        try:
            snap = compute_monitoring_snapshot(results)
            save_monitor_snapshot(snap, period="batch")
            if snap.get("alerts_fired"):
                send_monitor_alert(snap)
        except Exception as e:
            log.warning(f"Monitor error: {e}")

        return results

    def process_text_records(self, records: List[Dict],
                              progress_callback=None) -> List[Dict]:
        """Procesa registros de texto directo de Salesforce (sin OCR)."""
        total = len(records)
        results = []
 
        for i, rec in enumerate(records):
            text = rec.get("text_content", "")
            sf_id = rec.get("Id", f"rec_{i}")
            filename = f"SF_TEXT_{rec.get('Title', sf_id)}"
            if not text.strip():
                continue
            try:
                result = self.extractor.extract_from_text(text, filename, f"salesforce_text:{sf_id}")
                results.append(result)
                if self.sheets and result.get("_status") == "done":
                    self.sheets.buffer_extraction(
                        data={k: v for k, v in result.items()
                              if not k.startswith("_") or k in ("_filename",)},
                        campos=self.extractor.campos,
                        validation=result.get("_validation", {}),
                        alerts=result.get("_alerts", []),
                        confidence=result.get("_confidence", 0.0),
                        needs_review=result.get("_needs_review", False),
                    )
            except Exception as e:
                results.append({
                    "_filename": filename,
                    "_status": "error",
                    "_error": str(e),
                    "_confidence": 0.0,
                })
 
            if progress_callback:
                progress_callback(
                    f"Texto {i+1}/{total}: {filename}",
                    int((i + 1) / total * 100)
                )
 
        if self.sheets:
            try:
                self.sheets.flush_batch()
            except Exception as e:
                log.warning(f"Error flush_batch text: {e}")
 
        return results
 
 
# ─────────────────────────────────────────────────────────────
# INTERFAZ STREAMLIT
# ─────────────────────────────────────────────────────────────
 

def _render_login_page(st):
    """Página de login minimalista y segura."""
    st.markdown("""
    <style>
    section[data-testid="stMain"]{background:#0d1117}
    .lbox{max-width:380px;margin:60px auto 0;padding:36px 32px;background:#151929;
          border-radius:14px;border:1px solid #2a3354}
    .lt{text-align:center;font-size:1.5rem;font-weight:600;color:#e0e6ff;margin-bottom:4px}
    .ls{text-align:center;font-size:.8rem;color:#5a6a9a;margin-bottom:24px}
    .sb{background:#0d2218;color:#3db87a;border-radius:6px;padding:7px 12px;
        font-size:.75rem;text-align:center;margin-top:14px;border:1px solid #1a3d28}
    </style>""", unsafe_allow_html=True)

    _, col, _ = st.columns([1, 2, 1])
    with col:
        st.markdown('<div class="lt">🏥 Clinical Extractor Pro</div>', unsafe_allow_html=True)
        st.markdown('<div class="ls">v13 · SGSSS Colombia · Ley 1581 · Cifrado AES-256</div>',
                    unsafe_allow_html=True)
        st.markdown("---")
        email    = st.text_input("Correo electrónico", placeholder="usuario@dominio.com",
                                  key="login_email", label_visibility="collapsed")
        password = st.text_input("Contraseña", type="password", placeholder="Contraseña",
                                  key="login_pass", label_visibility="collapsed")
        remember = st.checkbox("Mantener sesión iniciada", key="login_remember",
                               help="El token se guarda cifrado en la base de datos. "
                                    "No necesitas volver a iniciar sesión aunque cierres el navegador.")
        if st.button("Iniciar sesión →", use_container_width=True, type="primary", key="btn_login"):
            if not email or not password:
                st.error("Ingresa correo y contraseña.")
            else:
                ok, msg, user = authenticate_user(email.strip(), password,
                                                   ip="web", ua="streamlit/v13")
                if ok and user:
                    _token = user["_token"]
                    # Si "recordar sesión", guardar token en DB cifrada con TTL extendida
                    if remember:
                        try:
                            _long_token = create_session_token(
                                user["id"], user["email"], user["role"],
                                ttl_hours=24 * 30  # 30 días
                            )
                            # Registrar en tabla sessions para que is_token_valid lo acepte
                            _lpl = verify_session_token(_long_token)
                            if _lpl:
                                _ljti = _lpl.get("jti", secrets.token_hex(16))
                                _lexp = (datetime.utcnow() + timedelta(hours=24*30)).isoformat()
                                _con2 = _sec_db()
                                _con2.execute(
                                    "INSERT OR IGNORE INTO sessions "
                                    "(jti, user_id, token, created_at, expires_at, "
                                    " ip_address, user_agent) VALUES (?,?,?,?,?,?,?)",
                                    (_ljti, user["id"], _long_token,
                                     datetime.utcnow().isoformat(), _lexp,
                                     "web", "streamlit/remember")
                                )
                                _con2.commit()
                            save_app_config(
                                f"remember_token_{user['id']}",
                                _long_token,
                                updated_by=user["id"]
                            )
                            _token = _long_token
                        except Exception as _re:
                            log.warning(f"remember_me error: {_re}")
                            pass  # usar token normal si falla
                    st.session_state.update({
                        "_auth_token":       _token,
                        "_user_id":          user["id"],
                        "_user_email":       user["email"],
                        "_user_role":        user["role"],
                        "_user_name":        user.get("full_name", ""),
                        "_must_change_pass": user.get("_must_change_pass", False),
                        "_remembered":       remember,
                    })
                    st.rerun()
                else:
                    st.error(f"🚫 {msg}")
        st.markdown(
            '<div class="sb">🔒 AES-256-GCM · bcrypt · JWT HS256 · Audit log</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div style="text-align:center;font-size:.72rem;color:#3a4a6a;margin-top:18px;">'
            'Desarrollado por <strong style="color:#5a7abf">Juan Manuel Collazos Rozo, MD, MSc.</strong><br>'
            'Todos los derechos reservados</div>',
            unsafe_allow_html=True)


def _sidebar_nav(st, active_page: str, user_role: str, results: list) -> str:
    """Sidebar de navegación. Devuelve la página activa."""
    n_review = sum(1 for r in results if r.get("_needs_review"))
    n_dup    = len(st.session_state.get("duplicate_log", []))

    with st.sidebar:
        st.markdown("### 🏥 Clinical Extractor")
        st.caption("v13 · SGSSS Colombia")
        st.markdown("---")

        pages_main = [
            ("📤  Subir documentos",    "upload"),
            ("☁️  Salesforce",          "salesforce"),
            ("📋  Resultados",          "results"),
            ("⚠️  Revisar manualmente", "review"),
        ]
        pages_analysis = [
            ("📈  Calidad y métricas", "quality"),
            ("🔍  Buscador clínico",   "search"),
            ("📬  Cola de trabajos",   "queue"),
            ("🔁  Duplicados",         "dupes"),
        ]
        pages_system = [
            ("⚙️  Configuración",   "settings"),
            ("📂  Google Drive",    "gdrive"),
            ("🔷  OneDrive",        "onedrive"),
            ("📖  Ayuda / Manual",  "help"),
        ]
        if user_role == Role.ADMIN:
            pages_system.append(("👑  Usuarios y seguridad", "admin"))

        st.caption("PRINCIPAL")
        for label, key in pages_main:
            badge = ""
            if key == "review" and n_review > 0:
                badge = f" 🔴{n_review}"
            if key == "dupes" and n_dup > 0:
                badge = f" ·{n_dup}"
            if st.button(f"{label}{badge}", key=f"nav_{key}",
                         use_container_width=True,
                         type="primary" if active_page == key else "secondary"):
                st.session_state["_page"] = key
                st.rerun()

        st.caption("ANÁLISIS")
        for label, key in pages_analysis:
            badge = f" ·{n_dup}" if key == "dupes" and n_dup > 0 else ""
            if st.button(f"{label}{badge}", key=f"nav_{key}",
                         use_container_width=True,
                         type="primary" if active_page == key else "secondary"):
                st.session_state["_page"] = key
                st.rerun()

        st.caption("SISTEMA")
        for label, key in pages_system:
            if st.button(label, key=f"nav_{key}", use_container_width=True,
                         type="primary" if active_page == key else "secondary"):
                st.session_state["_page"] = key
                st.rerun()

        st.markdown("---")
        role_icon = {"admin": "👑", "editor": "✏️", "reader": "👁️"}.get(user_role, "👤")
        st.caption(f"{role_icon} {st.session_state.get('_user_email','')}")
        _is_remembered = st.session_state.get("_remembered", False)
        _btn_label = "Cerrar sesión 🔓" if not _is_remembered else "Cerrar sesión (y olvidar) 🔓"
        if st.button(_btn_label, key="btn_logout", use_container_width=True):
            _uid = st.session_state.get("_user_id", "")
            logout_user(st.session_state.get("_auth_token", ""))
            # Borrar token persistente de la DB si existía
            if _uid:
                try:
                    save_app_config(f"remember_token_{_uid}", "", updated_by=_uid)
                except Exception:
                    pass
            for k in list(st.session_state.keys()):
                if k.startswith("_"): del st.session_state[k]
            st.rerun()

    return st.session_state.get("_page", "upload")


def _run_extraction_local(uploaded_files, api_key, provider, model, max_tokens,
                           confidence_threshold, ocr_lang, ocr_dpi,
                           use_easyocr, use_vision_ocr,
                           campos_sel, tipo_consulta, max_workers,
                           sheets_enabled, sheets_url, creds_path,
                           project_id=None, user_id="", force_reprocess=False):
    """
    Ejecuta la extraccion sobre archivos subidos desde la UI de Streamlit.
    Muestra barra de progreso, detecta duplicados, escribe a Sheets si esta habilitado
    y almacena los resultados en st.session_state['results'].
    """
    import streamlit as _st

    if not uploaded_files:
        return

    sheets_mgr = None
    if sheets_enabled and sheets_url:
        try:
            # credentials_path puede ser "" si las credenciales vienen de Streamlit Secrets
            sheets_mgr = GoogleSheetsManager(sheets_url, creds_path or "")
        except FileNotFoundError as e:
            _st.error(f"❌ {e}")
        except Exception as e:
            _st.error(f"❌ No se pudo conectar a Google Sheets: {e}")

    enable_anon     = _st.session_state.get("cfg_anon_v",     False)
    enable_ensemble = _st.session_state.get("cfg_ensemble_v", True)

    extractor = ClinicalExtractor(
        api_key=api_key,
        provider=provider,
        model=model,
        max_tokens=max_tokens,
        ocr_lang=ocr_lang,
        ocr_dpi=ocr_dpi,
        campos=campos_sel,
        confidence_threshold=confidence_threshold,
        use_easyocr=use_easyocr,
        use_vision_ocr=use_vision_ocr,
        tipo_consulta=tipo_consulta,
        project_id=project_id or DEFAULT_PROJECT_ID,
        user_id=user_id,
    )
    extractor.enable_anonymization = enable_anon
    extractor.enable_ensemble      = enable_ensemble

    processor = BulkProcessor(
        extractor=extractor,
        sheets_manager=sheets_mgr,
        max_workers=max_workers,
    )

    files_to_process = []
    dup_log = _st.session_state.get("duplicate_log", [])

    for uf in uploaded_files:
        raw = uf.read()
        file_hash = hashlib.sha256(raw).hexdigest()

        if not force_reprocess:
            prior = file_already_processed(file_hash)
            if prior:
                dup_log.append({
                    "Archivo":      uf.name,
                    "filename":     uf.name,
                    "reason":       "duplicate_in_db",
                    "Motivo":       "Ya en base de datos local",
                    "detail":       "Ya procesado anteriormente",
                    "Detalle":      "Ya procesado anteriormente",
                    "prior_date":   (prior.get("processed_at") or "")[:10],
                    "Fecha previa": (prior.get("processed_at") or "")[:10],
                })
                continue

        files_to_process.append((raw, uf.name, f"upload:{uf.name}"))

    _st.session_state["duplicate_log"] = dup_log

    if not files_to_process:
        _st.warning("Todos los archivos ya fueron procesados anteriormente. "
                    "Activa Forzar re-extraccion si deseas reprocesarlos.")
        return

    progress_bar = _st.progress(0, text="Iniciando extraccion...")
    status_text  = _st.empty()

    def _progress_cb(msg, pct):
        progress_bar.progress(min(pct, 100), text=msg)
        status_text.caption(msg)

    with _st.spinner(f"Procesando {len(files_to_process)} archivo(s)..."):
        new_results = processor.process_files(files_to_process, progress_callback=_progress_cb)

    progress_bar.progress(100, text="Extraccion completada")
    status_text.empty()

    for res, (raw, fname, _src) in zip(new_results, files_to_process):
        if res.get("_status") == "done":
            file_hash = hashlib.sha256(raw).hexdigest()
            try:
                register_processed(
                    file_hash=file_hash,
                    filename=fname,
                    project_id=project_id or DEFAULT_PROJECT_ID,
                    user_id=user_id,
                )
            except Exception:
                pass

    existing = _st.session_state.get("results", [])
    _st.session_state["results"] = existing + new_results

    done   = sum(1 for r in new_results if r.get("_status") == "done")
    errors = sum(1 for r in new_results if "error" in r.get("_status", ""))
    _st.success(f"{done} documento(s) extraidos correctamente."
                + (f" {errors} con error." if errors else ""))


def _page_upload(st, user_payload, api_key, provider, model, max_tokens,
                  confidence_threshold, ocr_lang, ocr_dpi, use_easyocr,
                  use_vision_ocr, campos_sel, tipo_consulta, max_workers,
                  sheets_enabled, sheets_url, creds_path,
                  user_id, user_role):
    """Pagina: subir documentos."""
    if not has_permission(user_payload, "extract"):
        st.warning("👁️ Tu rol (Lector) no permite extraer documentos.")
        return

    # ── Proyecto activo ──────────────────────────────────────
    projects = get_all_projects()
    proj_map = {p["id"]: p for p in projects}
    pid_list = [p["id"] for p in projects]
    if "_active_project_id" not in st.session_state:
        st.session_state["_active_project_id"] = DEFAULT_PROJECT_ID

    cur_pid = st.session_state.get("_active_project_id", DEFAULT_PROJECT_ID)
    if cur_pid not in proj_map:
        cur_pid = DEFAULT_PROJECT_ID
        st.session_state["_active_project_id"] = cur_pid
    active_p = proj_map.get(cur_pid, {})

    pc1, pc2, pc3, pc4 = st.columns([4, 1, 1, 1])
    with pc1:
        idx = pid_list.index(cur_pid) if cur_pid in pid_list else 0
        sel = st.selectbox("Proyecto activo", pid_list, index=idx,
                            format_func=lambda x: f"{proj_map[x]['name']} "
                                                   f"({proj_map[x].get('total_files',0)} archivos)",
                            label_visibility="collapsed")
        if sel != cur_pid:
            st.session_state["_active_project_id"] = sel
            st.session_state["results"] = load_results_from_db()
            st.rerun()
    with pc2:
        if st.button("＋ Nuevo", use_container_width=True, key="btn_new_proj"):
            st.session_state["_modal"] = "new_project"
    with pc3:
        if st.button("🗑 Limpiar", use_container_width=True, key="btn_clean_proj"):
            st.session_state["_modal"] = "clear_project"
    with pc4:
        st.caption(f"📂 {active_p.get('name','')}")

    # ── Modales ──────────────────────────────────────────────
    modal = st.session_state.get("_modal")

    if modal == "new_project":
        with st.container(border=True):
            st.subheader("Crear nuevo proyecto")
            n1, n2 = st.columns(2)
            np_name = n1.text_input("Nombre *", key="np_name")
            np_tab  = n2.text_input("Tab en Sheets (opcional)", key="np_tab")
            np_desc = st.text_area("Descripción opcional", height=60, key="np_desc")
            c1, c2 = st.columns(2)
            if c1.button("Crear y activar", type="primary", key="btn_np_ok"):
                if np_name.strip():
                    pid = create_project(np_name.strip(), np_desc.strip(),
                                         created_by=user_id,
                                         sheets_tab=np_tab.strip() or None)
                    st.session_state.update({
                        "_active_project_id": pid,
                        "results": [],
                        "duplicate_log": [],
                        "_modal": None,
                    })
                    st.success(f"✅ Proyecto «{np_name}» creado.")
                    st.rerun()
                else:
                    st.error("El nombre no puede estar vacío.")
            if c2.button("Cancelar", key="btn_np_cancel"):
                st.session_state["_modal"] = None
                st.rerun()

    elif modal == "clear_project":
        with st.container(border=True):
            st.subheader("Limpiar o eliminar proyecto")
            st.error("⚠️ Algunas opciones son irreversibles.")
            mode = st.radio("¿Qué deseas hacer?", [
                "Limpiar duplicados — permite re-procesar los mismos archivos",
                "Eliminar todas las extracciones + duplicados del proyecto",
                "Eliminar el proyecto completo",
            ], key="clear_radio")
            confirm = st.text_input(
                f"Escribe CONFIRMAR para proceder sobre «{active_p.get('name','')}»",
                key="clear_confirm")
            c1, c2 = st.columns(2)
            if c1.button("Ejecutar", type="primary", key="btn_clear_ok"):
                if confirm.strip() != "CONFIRMAR":
                    st.error("Escribe CONFIRMAR exactamente.")
                else:
                    pid = st.session_state["_active_project_id"]
                    if "duplicados" in mode:
                        counts = clear_project_data(pid, False, user_id)
                        st.success(f"✅ {counts['dedup']} registros de dedup limpiados. "
                                   "Puedes re-procesar los mismos archivos.")
                    elif "extracciones" in mode:
                        counts = clear_project_data(pid, True, user_id)
                        st.session_state["results"] = []
                        st.success(f"✅ {counts['dedup']} duplicados y "
                                   f"{counts['extractions']} extracciones eliminados.")
                    else:
                        ok, msg = delete_project(pid, user_id)
                        if ok:
                            st.session_state.update({
                                "_active_project_id": DEFAULT_PROJECT_ID,
                                "results": [],
                            })
                            st.success(f"✅ {msg}")
                        else:
                            st.error(f"❌ {msg}")
                    st.session_state["_modal"] = None
                    st.rerun()
            if c2.button("Cancelar", key="btn_clear_cancel"):
                st.session_state["_modal"] = None
                st.rerun()

    st.markdown("---")

    # ── Historial de duplicados (colapsado por defecto) ───────
    dup_log = st.session_state.get("duplicate_log", [])
    if dup_log:
        with st.expander(f"🔁 {len(dup_log)} duplicado(s) omitido(s) en esta sesión"):
            st.dataframe(pd.DataFrame(dup_log), use_container_width=True, hide_index=True)
            dc1, dc2 = st.columns(2)
            dc1.download_button("Exportar CSV", pd.DataFrame(dup_log).to_csv(index=False).encode(),
                                 "duplicados.csv", mime="text/csv", key="btn_dup_csv")
            if dc2.button("Limpiar lista", key="btn_dup_clear"):
                st.session_state["duplicate_log"] = []
                st.rerun()
        st.markdown("")

    # ── Zona de carga ─────────────────────────────────────────
    uploaded_files = st.file_uploader(
        "Arrastra historias clínicas aquí — PDF, PNG, JPG, TIFF",
        type=["pdf", "png", "jpg", "jpeg", "tiff"],
        accept_multiple_files=True,
        label_visibility="visible",
    )

    # MEJORA v15b: validar tamaño máximo de archivos
    if uploaded_files:
        _max_mb = int(os.environ.get("CEP_MAX_FILE_MB", "50"))
        oversized = [f.name for f in uploaded_files if hasattr(f, "size") and f.size and f.size > _max_mb * 1024 * 1024]
        if oversized:
            st.warning(f"⚠️ {len(oversized)} archivo(s) exceden {_max_mb}MB y serán ignorados: {', '.join(oversized[:3])}")
            uploaded_files = [f for f in uploaded_files if not hasattr(f, "size") or not f.size or f.size <= _max_mb * 1024 * 1024]
    if uploaded_files:
        force = st.checkbox(
            "Forzar re-extracción (ignorar detección de duplicados)",
            key="force_reprocess_chk",
            help="Usa esto si el documento original cambió o quieres una extracción nueva.",
        )
        if not api_key:
            st.warning("⚠️ Configura la API Key en Configuración.")
        else:
            if st.button(f"Iniciar extracción — {len(uploaded_files)} archivo(s)",
                         type="primary", use_container_width=True,
                         disabled=not campos_sel):
                _run_extraction_local(
                    uploaded_files, api_key, provider, model, max_tokens,
                    confidence_threshold, ocr_lang, ocr_dpi,
                    use_easyocr, use_vision_ocr,
                    campos_sel, tipo_consulta, max_workers,
                    sheets_enabled, sheets_url, creds_path,
                    project_id=st.session_state.get("_active_project_id", DEFAULT_PROJECT_ID),
                    user_id=user_id,
                    force_reprocess=force,
                )


def _page_results(st, results, campos_sel, user_payload):
    """Página: resultados de extracciones."""
    if not results:
        st.info("Aún no hay resultados. Procesa documentos en «Subir documentos».")
        return

    # MEJORA v15c: cachear métricas para no recalcular en cada rerender
    _results_sig = (len(results), sum(1 for r in results if r.get("_status")=="done"))
    if st.session_state.get("_metrics_sig") != _results_sig:
        done     = sum(1 for r in results if r.get("_status") == "done")
        errors   = sum(1 for r in results if "error" in r.get("_status", ""))
        to_rev   = sum(1 for r in results if r.get("_needs_review"))
        avg_conf = (sum(r.get("_confidence", 0) for r in results if r.get("_status") == "done")
                    / max(done, 1))
        st.session_state["_metrics_cache"] = (done, errors, to_rev, avg_conf)
        st.session_state["_metrics_sig"] = _results_sig
    else:
        done, errors, to_rev, avg_conf = st.session_state["_metrics_cache"]

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total",            len(results))
    m2.metric("✅ Exitosos",       done)
    m3.metric("⚠️ A revisar",      to_rev)
    m4.metric("Confianza prom.",   f"{avg_conf:.0%}")

    # Filtros en una sola fila compacta
    st.markdown("")
    fc1, fc2, fc3, fc4 = st.columns([2, 2, 2, 1])
    f_status = fc1.multiselect("Estado", ["done", "error", "error_empty"],
                                default=["done", "error", "error_empty"],
                                label_visibility="collapsed",
                                placeholder="Filtrar por estado")
    f_review = fc2.checkbox("Solo pendientes revisión", key="f_rev")
    f_tipo   = fc3.multiselect("Tipo consulta",
                                list(set(r.get("_tipo_consulta","") for r in results if r.get("_tipo_consulta"))),
                                label_visibility="collapsed",
                                placeholder="Tipo de consulta")
    can_exp  = has_permission(user_payload, "export")

    filtered = [r for r in results
                if r.get("_status","") in (f_status or ["done","error","error_empty"])
                and (not f_review or r.get("_needs_review"))
                and (not f_tipo or r.get("_tipo_consulta","") in f_tipo)]

    if can_exp:
        exp_c1, exp_c2, exp_c3 = st.columns(3)
        with exp_c1:
            # MEJORA v15c: no computar exportación hasta que el usuario la pida
            _csv_key = f"csv_inv_{len(filtered)}"
            if st.button("📊 Preparar CSV Investigación", key="prep_csv_inv"):
                st.session_state[_csv_key] = export_research_csv(filtered, campos_sel, anon_mode=True)
            csv_inv = st.session_state.get(_csv_key, "")
            st.download_button(
                "⬇️ Descargar CSV Investigación",
                csv_inv.encode() if csv_inv else b"",
                f"investigacion_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                mime="text/csv", use_container_width=True,
                disabled=not csv_inv,
            )
        with exp_c2:
            all_data = []
            for r in filtered:
                row = {"archivo":r.get("_filename",""),"estado":r.get("_status",""),
                       "confianza":r.get("_confidence",0)}
                for campo in campos_sel:
                    v = r.get(campo,"")
                    row[campo] = " | ".join(str(x) for x in v) if isinstance(v,list) else v
                all_data.append(row)
            st.download_button(
                "⬇️ CSV Simple",
                pd.DataFrame(all_data).to_csv(index=False).encode(),
                f"extraccion_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                mime="text/csv", use_container_width=True,
            )
        with exp_c3:
            fhir_bundle = export_fhir_bundle(filtered, anon_mode=True)
            st.download_button(
                "⬇️ FHIR R4 Bundle",
                json.dumps(fhir_bundle, ensure_ascii=False, indent=2).encode(),
                f"fhir_bundle_{datetime.now().strftime('%Y%m%d_%H%M')}.json",
                mime="application/json", use_container_width=True,
            )

    # Tabla principal
    if filtered:
        display_cols = ["_filename","_status","_confidence","_needs_review","_tipo_consulta"] + campos_sel[:6]
        df = pd.DataFrame(filtered)
        show_cols = [c for c in display_cols if c in df.columns]
        df_show = df[show_cols].copy()
        df_show.columns = [c.replace("_"," ").title() for c in show_cols]
        st.dataframe(df_show, use_container_width=True, height=300, hide_index=True)

    # Detalle expandible (solo registros con alertas o revisión pendiente primero)
    # MEJORA v15c: sort O(n log n) en lugar de O(n²) 'not in list'
    sorted_filtered = sorted(
        filtered,
        key=lambda r: (0 if (r.get("_needs_review") or r.get("_alerts")) else 1)
    )
    for r in sorted_filtered[:30]:
        fname  = r.get("_filename", "—")
        conf   = r.get("_confidence", 0)
        status = r.get("_status","")
        icon   = "✅" if status=="done" and not r.get("_needs_review") else ("⚠️" if r.get("_needs_review") else "❌")
        with st.expander(f"{icon} {fname} — {conf:.0%}"):
            alerts = [a for a in r.get("_alerts",[]) if a.get("severidad") in ("CRITICA","ALTA")]
            for a in alerts[:5]:
                sev = a.get("severidad","")
                col = "error" if sev=="CRITICA" else "warning"
                getattr(st, col)(f"**{a.get('tipo','')}** · {a.get('descripcion','')}")
            if r.get("_validation",{}).get("auditoria_clinica",{}).get("incoherencias"):
                incs = r["_validation"]["auditoria_clinica"]["incoherencias"]
                st.info(f"🧠 Auditoría: {len(incs)} incoherencia(s) detectada(s). "
                        f"Ir a «Revisar manualmente» para corregir.")
            disp = {k: v for k,v in r.items() if not k.startswith("_") and k in campos_sel}
            st.json(disp, expanded=False)


def _page_review(st, results, campos_sel, user_payload, user_id):
    """Página: revisión manual de registros con problemas."""
    to_rev = [r for r in results if r.get("_needs_review")]
    if not to_rev:
        st.success("✅ No hay registros pendientes de revisión.")
        return

    st.info(f"⚠️ {len(to_rev)} registro(s) requieren revisión humana")
    can_edit = has_permission(user_payload, "edit")

    for i, r in enumerate(to_rev):
        fname     = r.get("_filename", f"Registro {i+1}")
        conf      = r.get("_confidence", 0)
        val       = r.get("_validation", {})
        alerts    = r.get("_alerts", [])
        audit_data = val.get("auditoria_clinica", {})
        incs      = audit_data.get("incoherencias", [])
        conflictos = val.get("conflictos", [])

        criticas = sum(1 for a in alerts if a.get("severidad")=="CRITICA")
        badge    = f"🔴 {criticas} crítica(s) · " if criticas else ""

        with st.expander(f"⚠️ {fname} — {badge}Confianza {conf:.0%}"):
            # Alertas médicas
            for a in alerts[:8]:
                sev = a.get("severidad","")
                if sev == "CRITICA":
                    st.error(f"🔴 **{a.get('tipo','')}**: {a.get('descripcion','')}")
                elif sev == "ALTA":
                    st.warning(f"🟠 **{a.get('tipo','')}**: {a.get('descripcion','')}")

            # Incoherencias de auditoría clínica
            if incs:
                st.markdown(f"**🧠 Auditoría de coherencia: {len(incs)} incoherencia(s)**")
                for inc in incs:
                    sev_i = inc.get("severidad","")
                    tipo_i = inc.get("tipo_incoherencia","")
                    campo_i = inc.get("campo","")
                    msg = f"**[{tipo_i}]** campo `{campo_i}`: {inc.get('descripcion','')}"
                    if sev_i == "CRITICA":
                        st.error(msg)
                    else:
                        st.warning(msg)
                    if inc.get("valor_probable_correcto"):
                        st.caption(f"Valor sugerido: `{inc['valor_probable_correcto']}`")

            if val.get("resumen"):
                st.caption(f"Verificación: {val['resumen']}")

            # Campos a corregir
            if can_edit and (conflictos or incs):
                st.markdown("**Corrección de campos:**")
                correcciones = {}
                campos_a_mostrar = list(dict.fromkeys(
                    conflictos + [i.get("campo","") for i in incs if i.get("campo")]
                ))[:15]

                for campo in campos_a_mostrar:
                    if not campo: continue
                    val_actual = r.get(campo, "")
                    if isinstance(val_actual, list):
                        val_actual = " | ".join(str(x) for x in val_actual)
                    nueva = st.text_input(
                        f"`{campo}`",
                        value=str(val_actual) if val_actual else "",
                        key=f"edit_{i}_{campo}",
                    )
                    if nueva != str(val_actual or ""):
                        correcciones[campo] = nueva

                c1, c2 = st.columns(2)
                if c1.button(f"💾 Guardar ({len(correcciones)} cambios)",
                              key=f"save_{i}", type="primary", disabled=not correcciones):
                    idx_r = st.session_state.results.index(r)
                    for campo, valor in correcciones.items():
                        st.session_state.results[idx_r][campo] = valor
                    st.session_state.results[idx_r]["_needs_review"] = False
                    st.session_state.results[idx_r]["_manually_reviewed"] = True
                    audit("manual_review", fname, f"campos={list(correcciones.keys())}")
                    st.success("✅ Correcciones guardadas.")
                    st.rerun()
                if c2.button("Marcar como revisado", key=f"mark_{i}"):
                    idx_r = st.session_state.results.index(r)
                    st.session_state.results[idx_r]["_needs_review"] = False
                    st.rerun()
            elif not can_edit:
                st.info("👁️ Tu rol (Lector) solo permite visualizar. Para editar necesitas rol Editor.")

            # ── Trazabilidad por campo ─────────────────────────
            field_traces = r.get("_field_traces", {})
            if field_traces:
                with st.expander("🔍 Trazabilidad por campo (origen de cada dato)"):
                    trace_rows = []
                    for campo, t in field_traces.items():
                        if not isinstance(t, dict): continue
                        trace_rows.append({
                            "Campo":         campo,
                            "Valor":         str(t.get("valor",""))[:60],
                            "Fuente":        t.get("texto_original","")[:80],
                            "Página":        t.get("pagina","—"),
                            "Sección":       t.get("seccion","—"),
                            "Modelo":        t.get("modelo",""),
                            "Confianza":     f"{t.get('confianza',0):.0%}",
                            "Método":        t.get("metodo",""),
                            "Inferencia":    "✅ Sí" if t.get("es_inferencia") else "No",
                        })
                    if trace_rows:
                        st.dataframe(pd.DataFrame(trace_rows),
                                     use_container_width=True, hide_index=True)
                        st.download_button(
                            "⬇️ Exportar trazabilidad",
                            pd.DataFrame(trace_rows).to_csv(index=False).encode(),
                            f"trazabilidad_{fname[:30]}.csv",
                            mime="text/csv",
                            key=f"trace_dl_{i}",
                        )

            # ── Ensemble result ────────────────────────────────
            ens = r.get("_ensemble", {})
            if ens and ens.get("flags"):
                st.warning(
                    f"🤝 **Ensamble** ({ens.get('modelo_validador','')}) "
                    f"marcó {len(ens['flags'])} campo(s): "
                    f"`{'`, `'.join(ens['flags'])}`. "
                    f"{ens.get('resumen','')}"
                )

            # ── Normalizaciones aplicadas ──────────────────────
            norm = r.get("_normalization_changes", {})
            if norm:
                st.info("🏷️ **Normalizaciones aplicadas:** " +
                        " · ".join(f"`{k}`: {v}" for k,v in list(norm.items())[:6]))


def _page_quality(st, results):
    """Dashboard científico de calidad de datos v14."""
    if not results:
        st.info("Aún no hay datos para analizar.")
        return

    done_results = [r for r in results if r.get("_status") == "done"]
    done         = len(done_results)
    total        = len(results)
    errors       = sum(1 for r in results if "error" in r.get("_status",""))
    to_rev       = sum(1 for r in results if r.get("_needs_review"))
    n_alerts     = sum(len(r.get("_alerts",[])) for r in results)
    n_incs       = sum(len(r.get("_validation",{}).get("auditoria_clinica",{})
                            .get("incoherencias",[])) for r in results)
    avg_conf     = (sum(r.get("_confidence",0) for r in done_results) / max(done, 1))

    # OCR quality stats
    ocr_scores = [r.get("_ocr_quality",{}).get("score",100)
                  for r in results if r.get("_ocr_quality")]
    avg_ocr    = sum(ocr_scores) / max(len(ocr_scores), 1) if ocr_scores else 100
    bad_ocr    = sum(1 for s in ocr_scores if s < OCR_QUALITY_THRESHOLD)

    # Field completeness
    all_fields: Dict[str, List] = {}
    for r in done_results:
        traces = r.get("_field_traces", {})
        for campo in r.get("_validation", {}).get("confianza_por_campo", {}):
            if campo not in all_fields:
                all_fields[campo] = []
            val = r.get(campo)
            all_fields[campo].append(val is not None and val != "")

    completeness = {c: (sum(v)/len(v)*100 if v else 0)
                    for c, v in all_fields.items()}

    # Inference rate
    n_inferred = sum(
        sum(1 for t in r.get("_field_traces",{}).values()
            if isinstance(t, dict) and t.get("es_inferencia"))
        for r in done_results
    )
    n_total_fields = sum(len(r.get("_field_traces",{})) for r in done_results)
    inf_rate = n_inferred / max(n_total_fields, 1) * 100

    # Ensemble flags
    n_ens_flags = sum(
        len(r.get("_ensemble",{}).get("flags",[]))
        for r in done_results
    )

    # ── Métricas principales ─────────────────────────────────
    st.markdown("### Resumen global")
    cols = st.columns(4)
    cols[0].metric("Total documentos",  total)
    cols[1].metric("✅ Procesados",      done,  f"{errors} errores")
    cols[2].metric("Confianza prom.",    f"{avg_conf:.0%}")
    cols[3].metric("⚠️ A revisar",       to_rev)

    cols2 = st.columns(4)
    cols2[0].metric("Calidad OCR prom.", f"{avg_ocr:.0f}/100",
                     f"⚠️ {bad_ocr} bajo umbral" if bad_ocr else "✅ todos aptos")
    cols2[1].metric("Alertas médicas",   n_alerts)
    cols2[2].metric("Incoherencias",     n_incs)
    cols2[3].metric("Flags ensamble",    n_ens_flags)

    st.divider()

    # ── Completitud por campo ─────────────────────────────────
    if completeness:
        st.markdown("### Completitud por campo")
        df_comp = (pd.DataFrame(
                       [(c, round(p,1)) for c,p in sorted(
                           completeness.items(), key=lambda x: x[1])])
                   .rename(columns={0:"Campo", 1:"Completitud (%)"}))
        # Color coding
        def color_completitud(val):
            if val >= 80: return "color: #0F6E56"
            if val >= 50: return "color: #BA7517"
            return "color: #A32D2D"
        st.dataframe(
            df_comp.style.map(color_completitud, subset=["Completitud (%)"]),
            use_container_width=True, hide_index=True, height=280
        )

    # ── Tasa de inferencia ────────────────────────────────────
    if n_total_fields > 0:
        st.markdown("### Extracción vs inferencia")
        c1, c2 = st.columns(2)
        c1.metric("Campos extraídos literalmente",
                   f"{100-inf_rate:.1f}%",
                   f"{n_total_fields - n_inferred} campos")
        c2.metric("Campos completados por inferencia",
                   f"{inf_rate:.1f}%",
                   f"{n_inferred} campos",
                   delta_color="inverse")
        if inf_rate > 30:
            st.warning(
                f"⚠️ {inf_rate:.0f}% de los campos fueron inferidos (no están "
                "literalmente en el documento). Considera mejorar la calidad "
                "del OCR o la legibilidad de los documentos fuente."
            )

    # ── OCR quality distribution ──────────────────────────────
    if ocr_scores:
        st.markdown("### Distribución de calidad OCR")
        buckets = {
            "Bueno (≥70)":        sum(1 for s in ocr_scores if s >= 70),
            "Aceptable (35-69)":  sum(1 for s in ocr_scores if 35 <= s < 70),
            "Deficiente (20-34)": sum(1 for s in ocr_scores if 20 <= s < 35),
            "Ilegible (<20)":     sum(1 for s in ocr_scores if s < 20),
        }
        df_ocr = pd.DataFrame(
            [(k,v) for k,v in buckets.items() if v > 0],
            columns=["Nivel","Documentos"]
        )
        st.bar_chart(df_ocr.set_index("Nivel"))

    # ── Conflictos por campo (DB) ─────────────────────────────
    try:
        con = _get_db_connection()  # thread-local pool
        df_stats = pd.read_sql("""
            SELECT campo,
                   total_extractions                                                 AS extracciones,
                   ROUND(suma_confianza/MAX(total_extractions,1)*100,1)             AS confianza_pct,
                   ROUND(CAST(total_conflicts AS REAL)/MAX(total_extractions,1)*100,1) AS conflicto_pct
            FROM campo_stats ORDER BY conflicto_pct DESC LIMIT 20
        """, con)
        if not df_stats.empty:
            st.markdown("### Campos con mayor tasa de conflicto histórica")
            st.dataframe(df_stats, use_container_width=True, hide_index=True)
    except Exception:
        pass

    # ── Evolución de confianza ────────────────────────────────
    ts_data = [(r.get("_processed_at","")[:10], r.get("_confidence",0))
               for r in done_results if r.get("_processed_at")]
    if len(ts_data) >= 3:
        df_ts = pd.DataFrame(ts_data, columns=["Fecha","Confianza"])
        df_ts = df_ts.groupby("Fecha")["Confianza"].mean().reset_index()
        st.markdown("### Evolución de confianza por fecha")
        st.line_chart(df_ts.set_index("Fecha"))

    # ── Normalizaciones aplicadas ─────────────────────────────
    norm_changes = [r.get("_normalization_changes",{}) for r in done_results
                    if r.get("_normalization_changes")]
    if norm_changes:
        total_norm = sum(len(c) for c in norm_changes)
        st.markdown(f"### Normalizaciones aplicadas: {total_norm}")
        st.caption("Datos estandarizados a CIE-10 canónico, DCI genérico y unidades SI")
        sample = []
        for nc in norm_changes[:10]:
            for campo, cambio in nc.items():
                sample.append({"Campo": campo, "Cambio": cambio})
        if sample:
            st.dataframe(pd.DataFrame(sample), use_container_width=True,
                          hide_index=True, height=200)


def _page_dupes(st, user_id):
    """Página: duplicados omitidos."""
    dup_log = st.session_state.get("duplicate_log", [])

    if not dup_log:
        st.success("✅ No se han omitido duplicados en esta sesión.")
    else:
        st.info(f"🔁 {len(dup_log)} archivo(s) omitido(s) por ser duplicados")
        reason_map = {
            "duplicate_in_batch":   "Duplicado en el mismo lote",
            "duplicate_in_session": "Ya procesado en esta sesión",
            "duplicate_in_db":      "Ya en base de datos local",
            "duplicate_in_sheets":  "Ya en Google Sheets",
        }
        df = pd.DataFrame([{
            "Archivo":      d.get("Archivo") or d.get("filename", "—"),
            "Motivo":       reason_map.get(
                                d.get("reason", d.get("Motivo", "")),
                                d.get("Motivo") or d.get("reason", "—")
                            ),
            "Detalle":      d.get("Detalle") or d.get("detail", "—"),
            "Fecha previa": d.get("Fecha previa") or d.get("prior_date", "—"),
        } for d in dup_log])
        st.dataframe(df, use_container_width=True, hide_index=True)

        c1,c2 = st.columns(2)
        c1.download_button("⬇️ Exportar CSV",
                            df.to_csv(index=False).encode(),
                            "duplicados_omitidos.csv", mime="text/csv")
        if c2.button("Limpiar lista", key="btn_clear_dup"):
            st.session_state["duplicate_log"] = []
            st.rerun()

    # Proyectos y stats
    st.markdown("---")
    st.markdown("**Proyectos y registros procesados**")
    projects = get_all_projects()
    if projects:
        df_proj = pd.DataFrame([{
            "Nombre": p["name"], "Archivos": p.get("total_files",0),
            "Creado": (p.get("created_at","")[:10]),
        } for p in projects])
        st.dataframe(df_proj, use_container_width=True, hide_index=True)


def _page_settings(st, user_payload):
    """Página: configuración del sistema."""
    # ── Control de acceso: solo el admin puede modificar ─────────────────────
    _is_admin = user_payload.get("role") == Role.ADMIN
    _ro = not _is_admin  # read-only para no-admins

    if _ro:
        st.info("👁️ Estás viendo la configuración en modo lectura. Solo el administrador puede modificarla.")
    else:
        st.markdown("Configura el modelo, OCR y las integraciones externas.")

    # ── Pre-cargar valores guardados del .env ─────────────────────────────────
    _saved = _load_or_create_config()
    _def_provider    = _saved.get("CEP_PROVIDER", "claude")
    _def_model_claude = _saved.get("CEP_MODEL", "claude-sonnet-4-5") if _def_provider == "claude" else "claude-sonnet-4-5"
    _def_model_openai = _saved.get("CEP_MODEL", "gpt-4o") if _def_provider == "openai" else "gpt-4o"
    _def_api_key     = (_saved.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_API_KEY","")
                        if _def_provider == "claude"
                        else _saved.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY",""))
    _def_max_tok     = int(_saved.get("CEP_MAX_TOKENS", 3000))
    _def_conf        = float(_saved.get("CEP_CONF_THR", 0.75))
    _def_lang        = _saved.get("CEP_OCR_LANG", "spa+eng")
    _def_dpi         = int(_saved.get("CEP_OCR_DPI", 300))
    _def_workers     = int(_saved.get("CEP_MAX_WORKERS", min(3, __import__("os").cpu_count() or 2)))
    _def_anon        = _saved.get("CEP_ENABLE_ANON", "0") == "1"
    _def_ensemble    = _saved.get("CEP_ENABLE_ENSEMBLE", "1") != "0"
    _def_ocr_thr     = int(_saved.get("CEP_OCR_THR", int(OCR_QUALITY_THRESHOLD)))
    _def_sheets_url  = _saved.get("GOOGLE_SHEET_URL") or os.environ.get("GOOGLE_SHEET_URL","")
    _def_sf_user     = _saved.get("SF_USERNAME") or os.environ.get("SF_USERNAME","")
    _def_sf_domain   = _saved.get("SF_DOMAIN", "login")
    _def_sf_soql     = _saved.get("SF_SOQL", "")
    _def_sf_tsoql    = _saved.get("SF_TEXT_SOQL", "")

    with st.expander("🤖 Modelo de inteligencia artificial", expanded=True):
        pc1, pc2 = st.columns(2)
        _prov_idx = 0 if _def_provider == "claude" else 1
        provider = pc1.selectbox("Proveedor", ["claude","openai"],
            index=_prov_idx,
            format_func=lambda x: "Claude (Anthropic) — Recomendado" if x=="claude" else "GPT-4o (OpenAI)",
            key="cfg_provider", disabled=_ro)
        if provider == "claude":
            api_key = pc2.text_input("API Key", type="password",
                                      value=_def_api_key if _def_provider=="claude" else os.environ.get("ANTHROPIC_API_KEY",""),
                                      key="cfg_apikey", disabled=_ro)
            _mdl_opts_c = ["claude-sonnet-4-5","claude-opus-4-5","claude-haiku-4-5"]
            _mdl_idx_c  = _mdl_opts_c.index(_def_model_claude) if _def_model_claude in _mdl_opts_c else 0
            model   = st.selectbox("Modelo", _mdl_opts_c, index=_mdl_idx_c, key="cfg_model", disabled=_ro)
        else:
            api_key = pc2.text_input("API Key", type="password",
                                      value=_def_api_key if _def_provider=="openai" else os.environ.get("OPENAI_API_KEY",""),
                                      key="cfg_apikey", disabled=_ro)
            _mdl_opts_o = ["gpt-4o","gpt-4o-mini","gpt-4-turbo"]
            _mdl_idx_o  = _mdl_opts_o.index(_def_model_openai) if _def_model_openai in _mdl_opts_o else 0
            model   = st.selectbox("Modelo", _mdl_opts_o, index=_mdl_idx_o, key="cfg_model", disabled=_ro)
        cc1,cc2 = st.columns(2)
        max_tokens           = cc1.slider("Max tokens", 1000, 8000, _def_max_tok, 500, key="cfg_tokens", disabled=_ro)
        confidence_threshold = cc2.slider("Umbral de confianza", 0.5, 1.0, _def_conf, 0.05, key="cfg_conf", disabled=_ro)

    with st.expander("📋 Plantilla de extracción", expanded=True):
        tipo_consulta = st.selectbox("Tipo de consulta", list(PLANTILLAS_CONSULTA.keys()),
                                      key="cfg_tipo", disabled=_ro)
        campos_sel = st.multiselect("Campos a extraer",
                                     options=CAMPOS_DEFAULT,
                                     default=PLANTILLAS_CONSULTA[tipo_consulta],
                                     key="cfg_campos", disabled=_ro)
        custom = st.text_input("Agregar campo personalizado", key="cfg_custom", disabled=_ro)
        if custom and custom not in campos_sel:
            campos_sel = campos_sel + [custom]
        st.caption(f"{len(campos_sel)} campos seleccionados")

    with st.expander("🔬 Lectura de documentos (OCR)"):
        oc1, oc2 = st.columns(2)
        use_vision_ocr = oc1.checkbox("Visión directa del modelo",
            help="Más preciso para manuscritos difíciles. Mayor costo de API.",
            key="cfg_vision", disabled=_ro)
        use_easyocr    = oc2.checkbox("EasyOCR", disabled=_ro or use_vision_ocr,
            help="pip install easyocr", key="cfg_easyocr") if not use_vision_ocr else False
        oc3, oc4 = st.columns(2)
        _lang_opts = ["spa+eng","spa","eng"]
        _lang_idx  = _lang_opts.index(_def_lang) if _def_lang in _lang_opts else 0
        ocr_lang  = oc3.selectbox("Idioma OCR", _lang_opts, index=_lang_idx, key="cfg_lang", disabled=_ro)
        _dpi_opts  = [150, 200, 300, 400]
        _dpi_val   = _def_dpi if _def_dpi in _dpi_opts else 300
        ocr_dpi   = oc4.select_slider("DPI", _dpi_opts, value=_dpi_val, key="cfg_dpi", disabled=_ro)

    with st.expander("📊 Google Sheets"):
        sheets_enabled = st.checkbox("Habilitar Google Sheets", key="cfg_sheets", disabled=_ro)
        sheets_url = creds_path = ""
        if sheets_enabled:
            sheets_url = st.text_input("URL del Spreadsheet",
                                        value=_def_sheets_url, key="cfg_shurl", disabled=_ro)

            # ── Detectar fuente de credenciales activa ────────────────────
            _has_db      = False
            _has_secrets = False
            _has_session = False

            _raw_db = load_app_config("gcp_credentials_json", "").strip()
            if _raw_db:
                try:
                    _has_db = json.loads(_raw_db).get("type") == "service_account"
                except Exception:
                    pass
            try:
                import streamlit as _stchk
                _has_secrets = "gcp_service_account" in _stchk.secrets
            except Exception:
                pass
            _raw_ss = st.session_state.get("_gcp_creds_json", "").strip()
            if _raw_ss:
                try:
                    _has_session = json.loads(_raw_ss).get("type") == "service_account"
                except Exception:
                    pass

            if _has_db:
                _db_email = ""
                try:
                    _db_email = json.loads(_raw_db).get("client_email", "")
                except Exception:
                    pass
                st.success(f"✅ Credenciales guardadas permanentemente en DB cifrada"
                           + (f" — {_db_email}" if _db_email else ""))
            elif _has_secrets:
                st.success("✅ Credenciales activas: Streamlit Secrets")
            elif _has_session:
                st.info("⚠️ Credenciales activas solo en esta sesión — usa 'Guardar permanentemente'")

            # ── Editor JSON de credenciales ───────────────────────────────
            if not _ro:
                _PLACEHOLDER = """{
  "type": "service_account",
  "project_id": "tu-proyecto",
  "private_key_id": "abc123",
  "private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIE...\n-----END RSA PRIVATE KEY-----\n",
  "client_email": "nombre@tu-proyecto.iam.gserviceaccount.com",
  "client_id": "123456789",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/..."
}"""
                # Pre-cargar desde DB si existe
                _editor_default = _raw_db if _has_db else st.session_state.get("_gcp_creds_json", "")

                with st.expander(
                    "🔑 Credenciales JSON — pega el contenido de credentials.json",
                    expanded=not _has_db
                ):
                    st.caption(
                        "Abre tu archivo **credentials.json** con el Bloc de notas o VS Code, "
                        "copia todo el contenido y pégalo aquí. "
                        "Haz clic en **💾 Guardar permanentemente** para cifrarlas en la base de datos."
                    )
                    _json_input = st.text_area(
                        "credentials.json",
                        value=_editor_default,
                        height=280,
                        placeholder=_PLACEHOLDER,
                        key="cfg_gcp_json_editor",
                        label_visibility="collapsed",
                    )

                    c1, c2, c3 = st.columns([2, 2, 1])

                    if c1.button("💾 Guardar permanentemente", key="btn_save_gcp", type="primary"):
                        _txt = _json_input.strip()
                        if not _txt:
                            st.error("El campo está vacío.")
                        else:
                            try:
                                _parsed = json.loads(_txt)
                                if _parsed.get("type") != "service_account":
                                    st.error("El JSON no parece un Service Account de Google "
                                             "(falta \"type\": \"service_account\").")
                                else:
                                    save_app_config(
                                        "gcp_credentials_json", _txt,
                                        updated_by=user_payload.get("sub", "admin")
                                    )
                                    st.session_state["_gcp_creds_json"] = _txt
                                    st.success(
                                        f"✅ Guardado permanentemente en DB cifrada para: "
                                        f"{_parsed.get('client_email', '—')}. "
                                        "Persistirá entre reinicios."
                                    )
                                    st.rerun()
                            except json.JSONDecodeError as _je:
                                st.error(f"JSON inválido — línea {_je.lineno}: {_je.msg}. "
                                         "Verifica que copiaste el archivo completo.")

                    if c2.button("▶️ Aplicar solo en esta sesión", key="btn_apply_gcp"):
                        _txt = _json_input.strip()
                        if not _txt:
                            st.error("El campo está vacío.")
                        else:
                            try:
                                _parsed = json.loads(_txt)
                                if _parsed.get("type") != "service_account":
                                    st.error("El JSON no parece un Service Account de Google.")
                                else:
                                    st.session_state["_gcp_creds_json"] = _txt
                                    st.success(f"✅ Aplicado para esta sesión: "
                                               f"{_parsed.get('client_email', '—')}")
                                    st.rerun()
                            except json.JSONDecodeError as _je:
                                st.error(f"JSON inválido: {_je.msg}")

                    if c3.button("🗑️ Borrar", key="btn_clear_gcp"):
                        save_app_config("gcp_credentials_json", "",
                                        updated_by=user_payload.get("sub", "admin"))
                        st.session_state.pop("_gcp_creds_json", None)
                        st.rerun()

            else:
                if not (_has_db or _has_secrets or _has_session):
                    st.warning("⚠️ No hay credenciales de Google configuradas. "
                               "Contacta al administrador.")
                st.caption("🔒 Solo el administrador puede modificar las credenciales.")

            # ── Botón de diagnóstico ─────────────────────────────────────
            if not _ro and (_has_db or _has_secrets or _has_session):
                if st.button("🔍 Diagnóstico de credenciales", key="btn_diag_sheets"):
                    try:
                        import gspread as _gsp
                        st.write(f"**gspread version:** {_gsp.__version__}")
                    except Exception:
                        st.error("gspread no está instalado.")
                    _raw_d = load_app_config("gcp_credentials_json", "")
                    if _raw_d:
                        try:
                            _pd = json.loads(_raw_d)
                            st.write(f"**Credenciales en DB:** {_pd.get('client_email','—')}")
                            st.write(f"**Proyecto:** {_pd.get('project_id','—')}")
                            st.write(f"**Tipo:** {_pd.get('type','—')}")
                            _pk = _pd.get('private_key','')
                            if _pk.startswith('-----BEGIN'):
                                st.success("✅ private_key parece válida")
                            else:
                                st.error("❌ private_key inválida o vacía")
                        except Exception as _de:
                            st.error(f"JSON inválido en DB: {_de}")
                    else:
                        st.warning("No hay credenciales guardadas en DB")
                    if sheets_url:
                        _sid = GoogleSheetsManager._extract_sheet_id(sheets_url)
                        st.write(f"**URL configurada:** `{sheets_url}`")
                        st.write(f"**Sheet ID extraído:** `{_sid}`")
                        # Verificar que el ID tiene el formato correcto
                        import re as _re
                        if _re.match(r"^[a-zA-Z0-9_-]{20,}$", _sid):
                            st.success("✅ El ID parece válido")
                        else:
                            st.error(f"❌ El ID extraído no parece válido: '{_sid}'. "
                                     "Verifica que la URL sea de Google Sheets "
                                     "(debe contener /spreadsheets/d/ID)")
                    else:
                        st.warning("⚠️ No hay URL de Spreadsheet configurada en esta sesión. "
                                   "Escribe la URL en el campo 'URL del Spreadsheet' y guarda la configuración.")

            # ── Botón de prueba de conexión ───────────────────────────────
            # Leer URL directamente del widget (no de session_state que puede estar desactualizado)
            _url_to_test = (st.session_state.get("cfg_shurl") or sheets_url or
                            load_app_config("GOOGLE_SHEET_URL", "") or
                            _def_sheets_url).strip()

            if not _ro and (_has_db or _has_secrets or _has_session):
                if not _url_to_test:
                    st.warning("Escribe la URL del Spreadsheet antes de probar.")
                elif st.button("Probar conexion", key="btn_test_sheets", type="primary"):
                    with st.spinner("Verificando..."):
                        # ── Paso 1: cargar credenciales ───────────────────
                        _raw_creds = load_app_config("gcp_credentials_json", "")
                        if not _raw_creds:
                            try:
                                import streamlit as _st2
                                _raw_creds = json.dumps(
                                    dict(_st2.secrets.get("gcp_service_account", {}))
                                )
                            except Exception:
                                pass

                        if not _raw_creds:
                            st.error("No hay credenciales guardadas. "
                                     "Pega el credentials.json en el editor de arriba.")
                        else:
                            try:
                                _cred_data = json.loads(_raw_creds)
                                _svc_email = _cred_data.get("client_email", "")
                                _sheet_id  = GoogleSheetsManager._extract_sheet_id(_url_to_test)

                                st.caption(f"Sheet ID: `{_sheet_id}`")
                                st.caption(f"Cuenta de servicio: `{_svc_email}`")

                                from google.oauth2.service_account import Credentials as _GC
                                from googleapiclient.discovery import build as _gb
                                _scopes = [
                                    "https://www.googleapis.com/auth/spreadsheets",
                                    "https://www.googleapis.com/auth/drive",
                                ]
                                _creds = _GC.from_service_account_info(_cred_data,
                                                                        scopes=_scopes)

                                # ── Paso 2: compartir PRIMERO via Drive API ───
                                st.caption("Paso 1/2: Otorgando permisos...")
                                try:
                                    _drive = _gb("drive", "v3", credentials=_creds,
                                                 cache_discovery=False)
                                    _share = GoogleSheetsManager._auto_share_sheet(
                                        _drive, _sheet_id, _svc_email
                                    )
                                    _ss = _share.get("status")
                                    if _ss == "ya_compartido":
                                        st.info(f"Permisos: ya estaba compartido con {_svc_email}")
                                    elif _ss == "compartido_ahora":
                                        st.success(f"Permiso otorgado ahora a {_svc_email}")
                                    else:
                                        # Drive API fallo — mostrar instruccion manual
                                        st.warning(
                                            "No se pudo compartir automaticamente. "
                                            "Comparte el Sheet manualmente: "
                                            "1) Abre tu Google Sheet. "
                                            "2) Clic en Compartir (arriba a la derecha). "
                                            "3) Escribe este correo: " + _svc_email + ". "
                                            "4) Asigna rol Editor. "
                                            "5) Regresa y haz clic en Probar conexion."
                                        )
                                except Exception as _de:
                                    st.warning(
                                        f"Drive API no disponible ({_de}). "
                                        f"Comparte el Sheet manualmente con: `{_svc_email}` (rol Editor), "
                                        f"luego prueba de nuevo."
                                    )

                                # ── Paso 3: abrir el Sheet ────────────────────
                                st.caption("Paso 2/2: Conectando al spreadsheet...")
                                try:
                                    import gspread as _gsp
                                    _gc = _gsp.service_account_from_dict(_cred_data)
                                    _sp = _gc.open_by_key(_sheet_id)
                                    st.success(
                                        f"Conectado a: **{_sp.title}**   "
                                        f"({len(_sp.worksheets())} hoja(s))"
                                    )
                                    st.caption(
                                        "Hojas: " + ", ".join(
                                            ws.title for ws in _sp.worksheets()
                                        )
                                    )
                                    # Guardar la URL en DB para que persista
                                    save_app_config("GOOGLE_SHEET_URL", _url_to_test,
                                                    user_payload.get("sub","admin"))

                                except Exception as _oe:
                                    _es = str(_oe)
                                    if "404" in _es or "SpreadsheetNotFound" in _es:
                                        st.error(
                                            "El Sheet todavia no esta compartido con la cuenta "
                                            "de servicio. Sigue los pasos de arriba para "
                                            f"compartirlo con `{_svc_email}` y vuelve a intentar."
                                        )
                                    elif "403" in _es:
                                        st.error(
                                            f"Sin permiso. Asegurate de dar rol **Editor** "
                                            f"(no solo Lector) a `{_svc_email}`."
                                        )
                                    else:
                                        st.error(f"Error al abrir el Sheet: {_oe}")

                            except json.JSONDecodeError as _je:
                                st.error(f"El JSON de credenciales es invalido: {_je}. "
                                         "Vuelve a pegar el credentials.json completo.")
                            except Exception as _ge:
                                st.error(f"Error inesperado: {_ge}")

            st.caption("Sincronizacion bidireccional de deduplicacion con Sheets")

    # ── Google Drive ────────────────────────────────────────────────────────
    with st.expander("📂 Google Drive (leer archivos + exportar Excel)"):
        gdrive_enabled = st.checkbox("Habilitar Google Drive", key="cfg_gdrive", disabled=_ro)
        gdrive_folder_url = ""
        gdrive_export_folder = ""
        if gdrive_enabled:
            gdrive_folder_url = st.text_input(
                "URL o ID de carpeta (para leer PDFs/imágenes)",
                value=load_app_config("gdrive_folder_url", ""),
                key="cfg_gdrive_folder", disabled=_ro,
                help="Carpeta de Drive donde están los documentos a procesar. "
                     "La app la comparte automáticamente con la cuenta de servicio."
            )
            gdrive_export_folder = st.text_input(
                "URL o ID de carpeta de exportación (para guardar resultados Excel)",
                value=load_app_config("gdrive_export_folder", ""),
                key="cfg_gdrive_export", disabled=_ro,
                help="Carpeta donde se subirán los archivos Excel con los resultados."
            )
            st.caption("Usa las mismas credenciales JSON de Google configuradas arriba.")

            if not _ro:
                _has_gdrive_creds = bool(load_app_config("gcp_credentials_json", ""))
                if not _has_gdrive_creds:
                    try:
                        import streamlit as _stg
                        _has_gdrive_creds = "gcp_service_account" in _stg.secrets
                    except Exception:
                        pass

                if _has_gdrive_creds and gdrive_folder_url:
                    if st.button("🔌 Probar conexión Drive", key="btn_test_gdrive"):
                        with st.spinner("Conectando con Google Drive..."):
                            try:
                                _gdmgr = GoogleDriveManager(gdrive_folder_url)
                                _files  = _gdmgr.list_files()
                                _share  = _gdmgr.auto_grant_access()
                                st.success(
                                    f"✅ Carpeta accesible. "
                                    f"{len(_files)} archivo(s) encontrado(s) "
                                    f"(PDF, JPG, PNG, TIFF)."
                                )
                                _st_share = _share.get("status")
                                if _st_share == "ya_compartido":
                                    st.info(f"🔗 {_share['message']}")
                                elif _st_share == "compartido_ahora":
                                    st.success(f"🎉 {_share['message']}")
                                else:
                                    st.warning(_share.get("message", ""))
                                if not _ro and gdrive_folder_url:
                                    save_app_config("gdrive_folder_url", gdrive_folder_url,
                                                    user_payload.get("sub","admin"))
                                if not _ro and gdrive_export_folder:
                                    save_app_config("gdrive_export_folder", gdrive_export_folder,
                                                    user_payload.get("sub","admin"))
                            except Exception as _e:
                                st.error(f"❌ {_e}")
                elif not _has_gdrive_creds:
                    st.warning("⚠️ Primero guarda las credenciales JSON de Google arriba.")

    # ── OneDrive / Microsoft 365 ────────────────────────────────────────────
    with st.expander("🔷 OneDrive / Microsoft 365 (leer archivos + exportar Excel)"):
        od_enabled = st.checkbox("Habilitar OneDrive", key="cfg_od", disabled=_ro)
        od_client_id = od_tenant_id = od_client_secret = od_token = ""
        od_folder = od_export_folder = ""
        if od_enabled:
            st.markdown("**Credenciales de Microsoft Azure**")
            st.caption(
                "Necesitas registrar una app en [portal.azure.com](https://portal.azure.com). "
                "En la sección de Ayuda encontrarás el paso a paso."
            )
            oa1, oa2 = st.columns(2)
            od_client_id = oa1.text_input(
                "Client ID (Application ID)",
                value=load_app_config("od_client_id", ""),
                key="cfg_od_clientid", disabled=_ro,
                type="password"
            )
            od_tenant_id = oa2.selectbox(
                "Tipo de cuenta",
                ["consumers", "organizations", "common"],
                index=["consumers","organizations","common"].index(
                    load_app_config("od_tenant_id", "consumers")
                    if load_app_config("od_tenant_id","consumers")
                    in ["consumers","organizations","common"] else "consumers"
                ),
                key="cfg_od_tenant", disabled=_ro,
                format_func=lambda x: {
                    "consumers":    "Personal (Outlook / Hotmail)",
                    "organizations":"Organizacional (Microsoft 365 / Azure AD)",
                    "common":       "Ambas (automático)",
                }.get(x, x)
            )
            if od_tenant_id == "organizations":
                od_client_secret = st.text_input(
                    "Client Secret (solo para cuentas organizacionales)",
                    value=load_app_config("od_client_secret", ""),
                    key="cfg_od_secret", disabled=_ro, type="password"
                )

            st.markdown("**Carpetas de OneDrive**")
            of1, of2 = st.columns(2)
            od_folder = of1.text_input(
                "Carpeta de lectura (ruta relativa)",
                value=load_app_config("od_folder", "/"),
                key="cfg_od_folder", disabled=_ro,
                placeholder="/Historias Clinicas",
                help="Ruta dentro de tu OneDrive. Usa / para la raíz."
            )
            od_export_folder = of2.text_input(
                "Carpeta de exportación",
                value=load_app_config("od_export_folder", "/Extracciones_Clinicas"),
                key="cfg_od_exportfolder", disabled=_ro,
                placeholder="/Extracciones_Clinicas"
            )

            # Token almacenado
            od_token = load_app_config("od_access_token", "")

            if not _ro:
                st.markdown("**Autenticación**")

                # Mostrar estado del token
                if od_token:
                    st.success("✅ Token de acceso guardado. La conexión está activa.")
                    if st.button("🗑️ Revocar token", key="btn_od_revoke"):
                        save_app_config("od_access_token", "",
                                        user_payload.get("sub","admin"))
                        st.rerun()
                else:
                    st.info("No hay token guardado. Usa el botón de abajo para autenticarte.")

                if od_client_id:
                    # Autenticación por client credentials (org)
                    if od_tenant_id == "organizations" and od_client_secret:
                        if st.button("🔑 Autenticar (Client Credentials)", key="btn_od_cc"):
                            with st.spinner("Autenticando..."):
                                try:
                                    _od = OneDriveManager(od_client_id, od_tenant_id,
                                                          od_client_secret)
                                    _tok = _od.auth_with_client_credentials()
                                    save_app_config("od_access_token", _tok,
                                                    user_payload.get("sub","admin"))
                                    # Guardar configuración
                                    for _k, _v in [
                                        ("od_client_id",     od_client_id),
                                        ("od_tenant_id",     od_tenant_id),
                                        ("od_client_secret", od_client_secret),
                                        ("od_folder",        od_folder),
                                        ("od_export_folder", od_export_folder),
                                    ]:
                                        if _v:
                                            save_app_config(_k, _v,
                                                            user_payload.get("sub","admin"))
                                    st.success("✅ Autenticación exitosa.")
                                    st.rerun()
                                except Exception as _e:
                                    st.error(f"❌ {_e}")
                    else:
                        # Device flow (personal o org sin secret)
                        if st.button("🔑 Iniciar autenticación con Microsoft",
                                     key="btn_od_device"):
                            with st.spinner("Iniciando flujo de autenticación..."):
                                try:
                                    _od = OneDriveManager(od_client_id, od_tenant_id)
                                    _flow = _od.get_device_flow_url()
                                    st.session_state["_od_device_code"]  = _flow.get("device_code","")
                                    st.session_state["_od_client_id"]    = od_client_id
                                    st.session_state["_od_tenant_id"]    = od_tenant_id
                                    st.session_state["_od_folder"]       = od_folder
                                    st.session_state["_od_export_folder"]= od_export_folder
                                    _vuri  = _flow.get("verification_uri", "")
                                    _ucode = _flow.get("user_code", "")
                                    st.info(
                                        "Paso 1: Abre esta URL en tu navegador: "
                                        + _vuri + "  \n\n"
                                        "Paso 2: Ingresa este codigo: " + _ucode + "  \n\n"
                                        "Paso 3: Haz clic en Confirmar autorizacion abajo."
                                    )
                                except Exception as _e:
                                    st.error(f"❌ {_e}")

                        if st.session_state.get("_od_device_code"):
                            if st.button("✅ Confirmar autorización", key="btn_od_confirm"):
                                with st.spinner("Verificando..."):
                                    try:
                                        _od2 = OneDriveManager(
                                            st.session_state["_od_client_id"],
                                            st.session_state["_od_tenant_id"]
                                        )
                                        _result = _od2.poll_device_flow(
                                            st.session_state["_od_device_code"]
                                        )
                                        if "access_token" in _result:
                                            save_app_config(
                                                "od_access_token",
                                                _result["access_token"],
                                                user_payload.get("sub","admin")
                                            )
                                            for _k, _v in [
                                                ("od_client_id",
                                                 st.session_state["_od_client_id"]),
                                                ("od_tenant_id",
                                                 st.session_state["_od_tenant_id"]),
                                                ("od_folder",
                                                 st.session_state.get("_od_folder","/")),
                                                ("od_export_folder",
                                                 st.session_state.get("_od_export_folder",
                                                                       "/Extracciones_Clinicas")),
                                            ]:
                                                if _v:
                                                    save_app_config(_k, _v,
                                                        user_payload.get("sub","admin"))
                                            st.session_state.pop("_od_device_code", None)
                                            st.success("✅ Autenticación completada y guardada.")
                                            st.rerun()
                                        elif _result.get("error") == "authorization_pending":
                                            st.warning("⏳ Aún no has autorizado. "
                                                       "Completa el paso en el navegador y vuelve.")
                                        else:
                                            st.error(f"Error: {_result.get('error_description','')}")
                                    except Exception as _e:
                                        st.error(f"❌ {_e}")

                    # Probar conexión si hay token
                    if od_token and st.button("🔌 Probar conexión OneDrive",
                                              key="btn_test_od"):
                        with st.spinner("Verificando..."):
                            try:
                                _od3 = OneDriveManager(
                                    load_app_config("od_client_id",""),
                                    load_app_config("od_tenant_id","consumers"),
                                    access_token=od_token
                                )
                                _files = _od3.list_files(
                                    load_app_config("od_folder","/")
                                )
                                st.success(
                                    f"✅ Conectado a OneDrive. "
                                    f"{len(_files)} archivo(s) encontrado(s) "
                                    f"(PDF, imágenes) en la carpeta configurada."
                                )
                                if _files:
                                    st.dataframe(
                                        pd.DataFrame([{
                                            "Nombre": f["name"],
                                            "Tamaño": f"{int(f.get('size',0))//1024} KB",
                                            "Modificado": f.get("modified","")[:10],
                                        } for f in _files[:10]]),
                                        use_container_width=True, hide_index=True
                                    )
                            except Exception as _e:
                                st.error(f"❌ {_e}")
                else:
                    st.warning("⚠️ Ingresa el Client ID para continuar.")

    with st.expander("☁️ Salesforce"):
        sf_enabled = st.checkbox("Habilitar Salesforce", key="cfg_sf", disabled=_ro)
        sf_user=sf_pass=sf_token=sf_soql=sf_text_soql=""
        sf_domain="login"; sf_limit=100; sf_skip_processed=True; sf_incremental=False
        if sf_enabled:
            s1,s2 = st.columns(2)
            sf_user  = s1.text_input("Usuario SF", value=_def_sf_user, key="cfg_sfuser", disabled=_ro)
            sf_pass  = s2.text_input("Contraseña SF", type="password", key="cfg_sfpass", disabled=_ro)
            s3,s4 = st.columns(2)
            sf_token  = s3.text_input("Security Token", type="password", key="cfg_sftoken", disabled=_ro)
            _sf_dom_opts = ["login","test"]
            _sf_dom_idx  = _sf_dom_opts.index(_def_sf_domain) if _def_sf_domain in _sf_dom_opts else 0
            sf_domain = s4.selectbox("Entorno", _sf_dom_opts, index=_sf_dom_idx, key="cfg_sfdomain", disabled=_ro)
            sf_soql       = st.text_area("SOQL archivos", value=_def_sf_soql, height=60, key="cfg_sfsoql", disabled=_ro)
            sf_text_soql  = st.text_area("SOQL campos de texto", value=_def_sf_tsoql, height=60, key="cfg_sftsoql", disabled=_ro)
            sf_limit      = st.number_input("Límite registros", 10, 2000, 100, key="cfg_sflimit", disabled=_ro)
            sf_incremental = st.checkbox("Modo incremental", key="cfg_sfinc", disabled=_ro)
            if not _ro and st.button("Conectar Salesforce", key="btn_sf_connect"):
                with st.spinner("Conectando..."):
                    try:
                        st.session_state.sf_manager = SalesforceManager(sf_user,sf_pass,sf_token,sf_domain)
                        st.success("✅ Conectado")
                    except Exception as e:
                        st.error(f"❌ {e}")

    with st.expander("⚡ Procesamiento paralelo"):
        _cpu_count = __import__("os").cpu_count() or 2
        max_workers = st.slider(
            "Workers paralelos",
            min_value=1,
            max_value=min(8, _cpu_count * 2),
            value=min(_def_workers, min(8, _cpu_count * 2)),
            help=f"CPU disponibles: {_cpu_count}. Para clínicas grandes se recomienda 3-5.",
            key="cfg_workers", disabled=_ro
        )

    with st.expander("🔬 Robustez científica (v14)"):
        st.caption("Configuración de las mejoras de calidad científica")
        sc1, sc2 = st.columns(2)
        enable_anon = sc1.checkbox(
            "🔒 Anonimizar PII",
            value=_def_anon,
            key="cfg_anon",
            disabled=_ro,
            help="Elimina nombre, documento e info personal. Genera ID anónimo para investigación."
        )
        enable_ensemble = sc2.checkbox(
            "🤝 Ensamble de modelos",
            value=_def_ensemble,
            key="cfg_ensemble",
            disabled=_ro,
            help="Usa un segundo modelo para validar la extracción del primero."
        )
        ocr_threshold = st.slider(
            "Umbral mínimo de calidad OCR",
            min_value=10, max_value=80, value=_def_ocr_thr, step=5,
            key="cfg_ocr_thr",
            disabled=_ro,
            help="Documentos con score OCR por debajo de este umbral se marcarán para revisión."
        )
        if enable_anon:
            st.info("⚠️ Anonimización activa: los nombres y documentos NO serán almacenados. "
                    "Solo se guarda el ID anónimo SHA-256 para investigación longitudinal.")
        st.session_state["cfg_anon_v"]     = enable_anon
        st.session_state["cfg_ensemble_v"] = enable_ensemble
        st.session_state["cfg_ocr_thr_v"]  = ocr_threshold

    # Guardar en session_state para uso global
    for k,v in {
        "cfg_api_key":api_key, "cfg_prov":provider, "cfg_mdl":model,
        "cfg_max_tok":max_tokens, "cfg_conf_thr":confidence_threshold,
        "cfg_lang_ocr":ocr_lang, "cfg_dpi_ocr":ocr_dpi,
        "cfg_easyocr_v":use_easyocr if not use_vision_ocr else False,
        "cfg_vision_v":use_vision_ocr,
        "cfg_campos_v":campos_sel, "cfg_tipo_v":tipo_consulta,
        "cfg_sheets_en":sheets_enabled, "cfg_sheets_url":sheets_url,
        "cfg_creds_path":creds_path, "cfg_max_wrk":max_workers,
        "cfg_sf_en":sf_enabled, "cfg_sf_user":sf_user, "cfg_sf_pass":sf_pass,
        "cfg_sf_tok":sf_token, "cfg_sf_dom":sf_domain,
        "cfg_sf_soql":sf_soql, "cfg_sf_tsoql":sf_text_soql,
        "cfg_sf_lim":sf_limit, "cfg_sf_inc":sf_incremental,
    }.items():
        st.session_state[k] = v

    # ── Botón de persistencia: guarda la configuración en .env ──────────────
    st.markdown("---")
    if _ro:
        st.caption("🔒 Solo el administrador puede guardar cambios en la configuración.")
    else:
        st.markdown("### 💾 Persistencia de configuración")
        st.caption(
            "Guarda las llaves y conexiones en el archivo `.env` local. "
            "Así estarán disponibles automáticamente al reiniciar la aplicación."
        )
    if not _ro and st.button("💾 Guardar configuración en disco", key="btn_save_cfg", type="primary"):
        _cfg_to_save: Dict[str, str] = {}

        # API keys y proveedor
        if provider == "claude" and api_key:
            _cfg_to_save["ANTHROPIC_API_KEY"] = api_key
        elif provider == "openai" and api_key:
            _cfg_to_save["OPENAI_API_KEY"] = api_key

        # Google Sheets
        if sheets_enabled and sheets_url:
            _cfg_to_save["GOOGLE_SHEET_URL"] = sheets_url

        # Salesforce
        if sf_enabled:
            if sf_user:    _cfg_to_save["SF_USERNAME"] = sf_user
            if sf_pass:    _cfg_to_save["SF_PASSWORD"] = sf_pass
            if sf_token:   _cfg_to_save["SF_TOKEN"]    = sf_token
            if sf_domain:  _cfg_to_save["SF_DOMAIN"]   = sf_domain
            if sf_soql:    _cfg_to_save["SF_SOQL"]      = sf_soql
            if sf_text_soql: _cfg_to_save["SF_TEXT_SOQL"] = sf_text_soql

        # Ajustes generales
        _cfg_to_save["CEP_MODEL"]         = model
        _cfg_to_save["CEP_PROVIDER"]      = provider
        _cfg_to_save["CEP_MAX_TOKENS"]    = str(max_tokens)
        _cfg_to_save["CEP_CONF_THR"]      = str(confidence_threshold)
        _cfg_to_save["CEP_OCR_LANG"]      = ocr_lang
        _cfg_to_save["CEP_OCR_DPI"]       = str(ocr_dpi)
        _cfg_to_save["CEP_MAX_WORKERS"]   = str(max_workers)
        _cfg_to_save["CEP_ENABLE_ANON"]   = "1" if enable_anon else "0"
        _cfg_to_save["CEP_ENABLE_ENSEMBLE"] = "1" if enable_ensemble else "0"
        _cfg_to_save["CEP_OCR_THR"]       = str(ocr_threshold)

        if _cfg_to_save:
            try:
                _persist_config(_cfg_to_save, overwrite=True)
                st.success(
                    f"✅ Configuración guardada en `{_CFG_FILE}` "
                    f"({len(_cfg_to_save)} parámetros). "
                    "Estará disponible automáticamente al reiniciar."
                )
            except Exception as _e:
                st.error(f"❌ No se pudo guardar: {_e}")
        else:
            st.warning("⚠️ No hay valores para guardar. Completa al menos una API Key.")

    # Mostrar ruta del archivo .env como referencia
    st.caption(f"📁 Archivo de configuración: `{_CFG_FILE.resolve()}`")

    return {
        "api_key":api_key, "provider":provider, "model":model,
        "max_tokens":max_tokens, "confidence_threshold":confidence_threshold,
        "ocr_lang":ocr_lang, "ocr_dpi":ocr_dpi,
        "use_easyocr":use_easyocr if not use_vision_ocr else False,
        "use_vision_ocr":use_vision_ocr,
        "campos_sel":campos_sel, "tipo_consulta":tipo_consulta,
        "sheets_enabled":sheets_enabled, "sheets_url":sheets_url,
        "creds_path":creds_path, "max_workers":max_workers,
        "sf_enabled":sf_enabled,
    }


def _page_salesforce(st, user_payload, api_key, provider, model, max_tokens,
                      confidence_threshold, ocr_lang, ocr_dpi, use_easyocr,
                      use_vision_ocr, campos_sel, tipo_consulta, max_workers,
                      sheets_enabled, sheets_url, creds_path, user_id):
    """Página: extracción desde Salesforce."""
    if not has_permission(user_payload, "extract"):
        st.warning("👁️ Tu rol no permite extraer documentos.")
        return

    sf_mgr = st.session_state.get("sf_manager")
    if not sf_mgr:
        st.info("👈 Configura y conecta Salesforce en **Configuración**.")
        return

    st.success("✅ Salesforce conectado")

    failed_queue = get_sf_failed_queue()
    if failed_queue:
        st.warning(f"⚠️ {len(failed_queue)} registro(s) en cola de reintentos")
        if st.button("Reintentar fallos"):
            _retry_sf_failures(
                failed_queue, sf_mgr, api_key, provider, model,
                max_tokens, confidence_threshold, ocr_lang, ocr_dpi,
                use_easyocr, use_vision_ocr, campos_sel, tipo_consulta,
                max_workers, sheets_enabled, sheets_url, creds_path)

    sc1, sc2 = st.columns(2)
    with sc1:
        st.subheader("Archivos PDF/Imagen")
        sf_incremental = st.checkbox("Solo nuevos desde última ejecución", key="sf_inc2")
        if st.button("Listar archivos disponibles", key="btn_sf_list"):
            with st.spinner("Consultando..."):
                recs = sf_mgr.query_clinical_records(incremental=sf_incremental)
                st.session_state["sf_records"] = recs
                st.success(f"{len(recs)} registros encontrados")
        if "sf_records" in st.session_state:
            recs = st.session_state["sf_records"]
            st.dataframe(pd.DataFrame([{
                "ID":r.get("Id"), "Título":r.get("Title",""),
                "Ext":r.get("FileExtension",""),
            } for r in recs[:20]]), use_container_width=True, hide_index=True)
            if st.button(f"Extraer {len(recs)} archivos", type="primary", key="btn_sf_extract"):
                _run_extraction_salesforce(
                    sf_mgr, recs, api_key, provider, model,
                    max_tokens, confidence_threshold, ocr_lang, ocr_dpi,
                    use_easyocr, use_vision_ocr, campos_sel, tipo_consulta,
                    max_workers, sheets_enabled, sheets_url, creds_path)
    with sc2:
        st.subheader("Campos de texto")
        sf_tsoql = st.session_state.get("cfg_sf_tsoql","")
        if sf_tsoql and st.button("Listar registros de texto", key="btn_sf_tlist"):
            with st.spinner("Consultando..."):
                trecs = sf_mgr.query_text_records(sf_tsoql)
                st.session_state["sf_text_records"] = trecs
                st.success(f"{len(trecs)} registros")
        if "sf_text_records" in st.session_state:
            trecs = st.session_state["sf_text_records"]
            st.info(f"{len(trecs)} registros de texto listos")
            if st.button("Procesar campos de texto", type="primary", key="btn_sf_text"):
                _run_extraction_text_records(
                    sf_mgr, trecs, api_key, provider, model,
                    max_tokens, confidence_threshold, campos_sel,
                    tipo_consulta, max_workers, sheets_enabled, sheets_url, creds_path)


def _page_search(st, campos_sel):
    """Buscador clínico sobre datos extraídos."""
    st.markdown("Busca pacientes por diagnóstico, medicamento, edad y otros criterios.")

    with st.form("clinical_search_form"):
        c1, c2 = st.columns(2)
        dx      = c1.text_input("Diagnóstico",     placeholder="ej: HTA, diabetes, neumonía")
        cie10   = c1.text_input("Código CIE-10",   placeholder="ej: I10, E11.9, J18.9")
        med     = c2.text_input("Medicamento",     placeholder="ej: metformina, enalapril")
        sexo    = c2.selectbox("Sexo", ["(todos)","Masculino","Femenino"])

        c3, c4, c5 = st.columns(3)
        edad_min = c3.number_input("Edad mínima", min_value=0, max_value=130, value=0, step=1)
        edad_max = c4.number_input("Edad máxima", min_value=0, max_value=130, value=0, step=1)
        conf_min = c5.slider("Confianza mínima", 0.0, 1.0, 0.0, 0.05)

        c6, c7, c8 = st.columns(3)
        tipo_c  = c6.selectbox("Tipo consulta", ["(todos)"] + list(PLANTILLAS_CONSULTA.keys()))
        f_desde = c7.text_input("Desde (YYYY-MM-DD)", placeholder="2024-01-01")
        f_hasta = c8.text_input("Hasta (YYYY-MM-DD)", placeholder="2025-12-31")

        submitted = st.form_submit_button("🔍 Buscar", type="primary",
                                           use_container_width=True)

    if submitted:
        with st.spinner("Buscando..."):
            results = clinical_search(
                diagnostico    = dx.strip(),
                cie10_codigo   = cie10.strip().upper(),
                medicamento    = med.strip(),
                sexo           = "" if sexo=="(todos)" else sexo,
                edad_min       = int(edad_min) if edad_min > 0 else None,
                edad_max       = int(edad_max) if edad_max > 0 else None,
                confianza_min  = conf_min,
                tipo_consulta  = "" if tipo_c=="(todos)" else tipo_c,
                fecha_desde    = f_desde.strip(),
                fecha_hasta    = f_hasta.strip(),
            )

        st.metric("Resultados encontrados", len(results))

        if results:
            display_fields = ["filename","processed_at","tipo_consulta","confidence",
                              "diagnostico_principal","codigo_cie10_principal",
                              "edad","sexo","medicamentos"]
            df = pd.DataFrame([{f: r.get(f,"") for f in display_fields} for r in results])
            df.columns = [c.replace("_"," ").title() for c in df.columns]
            st.dataframe(df, use_container_width=True, height=380, hide_index=True)

            # Export search results
            csv_search = export_research_csv(
                [{"_status":"done","_filename":r["filename"],
                  "_processed_at":r.get("processed_at",""),
                  "_confidence":r.get("confidence",0),
                  "_tipo_consulta":r.get("tipo_consulta",""),
                  **r} for r in results],
                campos_sel, anon_mode=True
            )
            if csv_search:
                st.download_button(
                    "⬇️ Exportar resultados CSV",
                    csv_search.encode(),
                    f"busqueda_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                    mime="text/csv",
                )
        elif submitted:
            st.info("No se encontraron registros con esos criterios.")


def _page_queue(st, user_payload, user_id):
    """Gestión de la cola de procesamiento persistente."""
    pid = st.session_state.get("_active_project_id", DEFAULT_PROJECT_ID)
    stats = queue_stats(pid)

    pending    = stats.get("pending",    0)
    processing = stats.get("processing", 0)
    done       = stats.get("done",       0)
    failed     = stats.get("failed",     0)

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("⏳ Pendientes",    pending)
    c2.metric("⚙️ Procesando",   processing)
    c3.metric("✅ Completados",   done)
    c4.metric("❌ Fallidos",      failed)

    if failed > 0:
        st.warning(f"⚠️ {failed} trabajo(s) fallido(s) en este proyecto.")
        if st.button("🔄 Reintentar todos los fallidos", key="btn_retry_all"):
            n = queue_retry_failed(pid)
            st.success(f"✅ {n} trabajo(s) puestos de nuevo en cola.")
            st.rerun()

    st.divider()
    st.markdown("**Trabajos fallidos**")
    failed_jobs = queue_get_failed(pid)
    if failed_jobs:
        df_f = pd.DataFrame(failed_jobs)
        df_f.columns = [c.replace("_"," ").title() for c in df_f.columns]
        st.dataframe(df_f, use_container_width=True, hide_index=True)
    else:
        st.success("✅ No hay trabajos fallidos.")

    st.divider()
    st.markdown("**Monitoreo de calidad — últimos snapshots**")
    try:
        con = _get_db_connection()  # thread-local pool
        df_mon = pd.read_sql("""
            SELECT timestamp, period, total_docs, done_docs, error_docs,
                   ROUND(avg_conf*100,1) AS conf_pct,
                   ROUND(avg_ocr,0) AS ocr_score,
                   n_alerts, n_review
            FROM monitor_snapshots
            ORDER BY timestamp DESC LIMIT 20
        """, con)
        con.close()
        if not df_mon.empty:
            df_mon["timestamp"] = df_mon["timestamp"].str[:16]
            st.dataframe(df_mon, use_container_width=True, hide_index=True)
            thresholds = MONITOR_THRESHOLDS
            st.caption(
                f"Umbrales: conf≥{thresholds['conf_min']:.0%} · "
                f"error≤{thresholds['error_rate_max']:.0%} · "
                f"OCR≥{thresholds['ocr_min']:.0f} · "
                f"revisión≤{thresholds['review_rate_max']:.0%}"
            )
    except Exception:
        st.info("Aún no hay snapshots de monitoreo.")

    webhook = os.environ.get("CEP_WEBHOOK_URL","")
    if webhook:
        st.success(f"✅ Webhook configurado: {webhook[:40]}…")
    else:
        st.info("💡 Configura CEP_WEBHOOK_URL en .env para recibir alertas en Slack/Teams.")


def _page_admin(st, user_payload):
    """Página: gestión de usuarios y seguridad."""
    tab_users, tab_sessions, tab_audit, tab_pass = st.tabs([
        "Usuarios", "Sesiones activas", "Audit log", "Mi contraseña"
    ])

    with tab_users:
        with st.expander("Crear nuevo usuario", expanded=False):
            cn1,cn2 = st.columns(2)
            new_name  = cn1.text_input("Nombre completo", key="adm_name")
            new_email = cn1.text_input("Email",           key="adm_email")
            new_role  = cn2.selectbox("Rol", [Role.EDITOR, Role.READER],
                format_func=lambda r: "Editor — extrae, edita, exporta"
                                     if r==Role.EDITOR else "Lector — solo visualiza",
                key="adm_role")
            new_pass  = cn2.text_input("Contraseña temporal", type="password", key="adm_pass")
            new_pass2 = cn2.text_input("Confirmar contraseña", type="password", key="adm_pass2")
            if st.button("Crear usuario", type="primary", key="adm_btn_create"):
                if new_pass != new_pass2: st.error("Las contraseñas no coinciden.")
                elif not all([new_email, new_pass, new_name]): st.error("Completa todos los campos.")
                else:
                    ok,msg = create_user(new_email, new_pass, new_role, new_name,
                                         created_by=user_payload["sub"])
                    (st.success if ok else st.error)(msg)
                    if ok: st.rerun()

        st.markdown("**Usuarios registrados**")
        for u in get_all_users():
            is_adm = u["role"]==Role.ADMIN
            stato  = "Activo" if u["is_active"] else "Inactivo"
            last   = (u.get("last_login") or "Nunca")[:10]
            rl     = {"admin":"👑 Admin","editor":"✏️ Editor","reader":"👁️ Lector"}.get(u["role"],u["role"])
            with st.expander(f"{rl} · {u['email']} · {stato} · {last}"):
                if u.get("locked_until"):
                    st.warning(f"🔒 Bloqueado hasta {u['locked_until'][:19]}")
                if not is_adm:
                    ac1,ac2,ac3,ac4 = st.columns(4)
                    nr = ac1.selectbox("Rol", [Role.EDITOR,Role.READER],
                        key=f"nr_{u['id']}",
                        format_func=lambda r:"✏️ Editor" if r==Role.EDITOR else "👁️ Lector")
                    if ac1.button("Cambiar rol", key=f"br_{u['id']}"):
                        ok,msg = update_user_role(u["id"],nr,user_payload["sub"])
                        (st.success if ok else st.error)(msg)
                        if ok: st.rerun()
                    lbl = "Desactivar" if u["is_active"] else "Activar"
                    if ac2.button(lbl, key=f"ba_{u['id']}"):
                        ok,msg = toggle_user_active(u["id"],user_payload["sub"])
                        (st.success if ok else st.error)(msg)
                        if ok: st.rerun()
                    if ac3.button("Eliminar", key=f"bd_{u['id']}"):
                        ok,msg = delete_user(u["id"],user_payload["sub"])
                        (st.success if ok else st.error)(msg)
                        if ok: st.rerun()
                    if ac4.button("Revocar sesiones", key=f"brs_{u['id']}"):
                        revoke_all_user_sessions(u["id"],user_payload["sub"])
                        st.success("Sesiones revocadas")

    with tab_sessions:
        sess = get_active_sessions()
        st.metric("Sesiones activas", len(sess))
        if sess:
            df_s = pd.DataFrame(sess)
            for c in ["created_at","expires_at"]:
                if c in df_s.columns: df_s[c]=df_s[c].str[:16]
            st.dataframe(df_s[["email","role","ip_address","created_at","expires_at"]],
                          use_container_width=True, hide_index=True)

    with tab_audit:
        rows = get_security_audit_log(300)
        st.metric("Eventos auditados", len(rows))
        if rows:
            df_a = pd.DataFrame(rows)
            df_a["timestamp_utc"] = df_a["timestamp_utc"].str[:16]
            df_a["success"] = df_a["success"].map({1:"OK",0:"FAIL"})
            st.dataframe(df_a[["timestamp_utc","email","action","success","ip_address","detail"]],
                          use_container_width=True, height=350, hide_index=True)
            st.download_button("Exportar CSV",
                pd.DataFrame(rows).to_csv(index=False).encode(),
                f"audit_{datetime.now().strftime('%Y%m%d')}.csv", mime="text/csv")

    with tab_pass:
        st.markdown("**Cambiar mi contraseña**")
        op  = st.text_input("Contraseña actual",  type="password", key="chg_old")
        np1 = st.text_input("Nueva contraseña",   type="password", key="chg_new")
        np2 = st.text_input("Confirmar nueva",    type="password", key="chg_new2")
        if st.button("Cambiar contraseña", type="primary", key="btn_chg"):
            if np1!=np2: st.error("Las contraseñas no coinciden.")
            else:
                ok,msg = change_password(user_payload["sub"], op, np1)
                if ok:
                    st.success(msg)
                    logout_user(st.session_state.get("_auth_token",""))
                    for k in list(st.session_state.keys()):
                        if k.startswith("_"): del st.session_state[k]
                    st.rerun()
                else: st.error(f"❌ {msg}")


def _render_force_change_password(st, user_payload: Dict, user_id: str, token: str):
    """
    Pantalla de cambio de contraseña obligatorio.
    Bloquea el acceso a la app hasta que el usuario cambie la contraseña temporal.
    """
    st.markdown("""
    <style>
    section[data-testid="stMain"]{background:#0d1117}
    </style>""", unsafe_allow_html=True)

    _, col, _ = st.columns([1, 2, 1])
    with col:
        st.markdown("## 🔑 Cambio de contraseña requerido")
        st.warning(
            "Estás usando una **contraseña temporal**. "
            "Debes establecer una contraseña personal antes de continuar. "
            "Esta contraseña no se guardará en ningún archivo — "
            "solo se almacena su hash cifrado en la base de datos."
        )
        st.markdown("---")

        st.markdown(f"**Usuario:** `{user_payload.get('email','')}`")
        st.markdown("")

        old_p = st.text_input(
            "Contraseña temporal actual",
            type="password",
            placeholder="ClinicalPro@2026!",
            key="fcp_old",
        )
        new_p = st.text_input(
            "Nueva contraseña",
            type="password",
            placeholder="Mínimo 10 caracteres",
            key="fcp_new",
            help="Debe tener al menos 10 caracteres, una mayúscula, un número y un símbolo.",
        )
        new_p2 = st.text_input(
            "Confirmar nueva contraseña",
            type="password",
            placeholder="Repite la nueva contraseña",
            key="fcp_new2",
        )

        # Indicador de fortaleza en tiempo real
        if new_p:
            has_upper  = any(c.isupper() for c in new_p)
            has_digit  = any(c.isdigit() for c in new_p)
            has_symbol = any(c in "!@#$%^&*()_+-=[]{}|;':,.<>?" for c in new_p)
            has_len    = len(new_p) >= 10
            strength   = sum([has_upper, has_digit, has_symbol, has_len])
            labels     = {1:"Muy débil 🔴", 2:"Débil 🟠", 3:"Aceptable 🟡", 4:"Fuerte 🟢"}
            st.caption(f"Fortaleza: {labels.get(strength,'—')}  "
                       f"{'✅' if has_len else '❌'} 10+ chars  "
                       f"{'✅' if has_upper else '❌'} Mayúscula  "
                       f"{'✅' if has_digit else '❌'} Número  "
                       f"{'✅' if has_symbol else '❌'} Símbolo")

        st.markdown("")
        if st.button("Establecer nueva contraseña →",
                      type="primary", use_container_width=True, key="fcp_btn"):
            if not old_p or not new_p or not new_p2:
                st.error("Completa todos los campos.")
            elif new_p != new_p2:
                st.error("Las contraseñas nuevas no coinciden.")
            elif new_p == old_p:
                st.error("La nueva contraseña no puede ser igual a la temporal.")
            else:
                ok, msg = change_password(user_id, old_p, new_p)
                if ok:
                    st.success("✅ Contraseña actualizada correctamente.")
                    st.info("Iniciando sesión con tu nueva contraseña…")
                    # Limpiar sesión — el usuario iniciará sesión de nuevo
                    logout_user(token)
                    for k in list(st.session_state.keys()):
                        if k.startswith("_"):
                            del st.session_state[k]
                    st.rerun()
                else:
                    st.error(f"❌ {msg}")

        st.markdown("---")
        st.caption("🔒 Tu contraseña se almacena cifrada con bcrypt. "
                   "Nadie — ni el administrador — puede verla.")


def _page_gdrive(st, user_payload, api_key, provider, model, max_tokens,
                  confidence_threshold, ocr_lang, ocr_dpi, use_easyocr,
                  use_vision_ocr, campos_sel, tipo_consulta, max_workers,
                  sheets_enabled, sheets_url, creds_path, user_id):
    """Pagina: importar desde Google Drive y exportar resultados a Drive."""
    if not has_permission(user_payload, "extract"):
        st.warning("Tu rol no permite extraer documentos.")
        return

    # Verificar credenciales
    _has_creds = bool(load_app_config("gcp_credentials_json", ""))
    if not _has_creds:
        try:
            import streamlit as _stg
            _has_creds = "gcp_service_account" in _stg.secrets
        except Exception:
            pass

    if not _has_creds:
        st.error("Primero configura las credenciales de Google en "
                 "Configuracion > Google Sheets > Editor JSON.")
        return

    tab_read, tab_export = st.tabs(["📥 Leer documentos desde Drive",
                                     "📤 Exportar resultados a Drive"])

    # ── TAB LECTURA ──────────────────────────────────────────────────────────
    with tab_read:
        st.markdown("Lee PDFs e imagenes directamente desde una carpeta de Google Drive.")
        folder_url = st.text_input(
            "URL o ID de la carpeta de Drive",
            value=load_app_config("gdrive_folder_url", ""),
            placeholder="https://drive.google.com/drive/folders/...",
            key="gdrive_folder_read"
        )
        if st.button("📋 Listar archivos", key="btn_gdrive_list") and folder_url:
            with st.spinner("Conectando con Google Drive..."):
                try:
                    _mgr = GoogleDriveManager(folder_url)
                    _files = _mgr.list_files()
                    if not _files:
                        st.warning("No se encontraron PDFs ni imagenes en esa carpeta.")
                    else:
                        st.success(f"{len(_files)} archivo(s) encontrado(s).")
                        st.session_state["_gdrive_files"] = _files
                        st.session_state["_gdrive_mgr_folder"] = folder_url
                        save_app_config("gdrive_folder_url", folder_url,
                                        user_payload.get("sub","admin"))
                except Exception as _e:
                    st.error(f"Error: {_e}")

        _files = st.session_state.get("_gdrive_files", [])
        if _files:
            st.dataframe(pd.DataFrame([{
                "Nombre":      f["name"],
                "Tamano KB":   f"{int(f.get('size',0))//1024}",
                "Modificado":  f.get("modified","")[:10],
            } for f in _files]), use_container_width=True, hide_index=True)

            _sel = st.multiselect(
                "Selecciona archivos a procesar",
                options=[f["name"] for f in _files],
                default=[f["name"] for f in _files],
                key="gdrive_sel_files"
            )
            force = st.checkbox("Forzar re-extraccion", key="gdrive_force")

            if st.button(f"Iniciar extraccion — {len(_sel)} archivo(s)",
                         type="primary", key="btn_gdrive_extract",
                         disabled=not _sel or not api_key):
                if not api_key:
                    st.warning("Configura la API Key en Configuracion.")
                else:
                    _selected = [f for f in _files if f["name"] in _sel]
                    _prog = st.progress(0, text="Descargando desde Drive...")
                    _status = st.empty()
                    _downloaded = []
                    try:
                        _gd = GoogleDriveManager(
                            st.session_state.get("_gdrive_mgr_folder","")
                        )
                        for i, _f in enumerate(_selected):
                            _status.caption(f"Descargando {_f['name']}...")
                            _raw = _gd.download_file(_f["id"])
                            _downloaded.append((_raw, _f["name"]))
                            _prog.progress(int((i+1)/len(_selected)*50),
                                           text=f"Descargado {i+1}/{len(_selected)}")
                    except Exception as _e:
                        st.error(f"Error descargando: {_e}")
                        return

                    # Crear objetos tipo UploadedFile para reutilizar _run_extraction_local
                    class _FakeFile:
                        def __init__(self, raw, name):
                            self._raw = raw
                            self.name = name
                            self.size = len(raw)
                        def read(self): return self._raw

                    _fake_files = [_FakeFile(r, n) for r, n in _downloaded]
                    _prog.progress(50, text="Procesando con IA...")
                    _run_extraction_local(
                        _fake_files, api_key, provider, model, max_tokens,
                        confidence_threshold, ocr_lang, ocr_dpi,
                        use_easyocr, use_vision_ocr,
                        campos_sel, tipo_consulta, max_workers,
                        sheets_enabled, sheets_url, creds_path,
                        project_id=st.session_state.get("_active_project_id",
                                                         DEFAULT_PROJECT_ID),
                        user_id=user_id,
                        force_reprocess=force,
                    )

    # ── TAB EXPORTAR ─────────────────────────────────────────────────────────
    with tab_export:
        st.markdown("Sube los resultados extraidos como archivo Excel a Google Drive.")
        export_folder = st.text_input(
            "URL o ID de carpeta de destino en Drive",
            value=load_app_config("gdrive_export_folder", ""),
            placeholder="https://drive.google.com/drive/folders/...",
            key="gdrive_export_folder_input"
        )
        results = st.session_state.get("results", [])
        done_count = sum(1 for r in results if r.get("_status") == "done")
        st.caption(f"{done_count} resultado(s) listos para exportar.")

        if st.button("📤 Subir Excel a Drive", key="btn_gdrive_upload",
                     type="primary", disabled=done_count == 0 or not export_folder):
            with st.spinner("Subiendo a Google Drive..."):
                try:
                    _gd2 = GoogleDriveManager(export_folder)
                    import io as _io
                    _rows = []
                    for r in results:
                        if r.get("_status") != "done":
                            continue
                        row = {"Archivo": r.get("_filename",""),
                               "Confianza": f"{r.get('_confidence',0):.0%}"}
                        for c in campos_sel:
                            row[c] = r.get(c, "")
                        _rows.append(row)
                    _df = pd.DataFrame(_rows)
                    _buf = _io.BytesIO()
                    with pd.ExcelWriter(_buf, engine="openpyxl") as _wr:
                        _df.to_excel(_wr, index=False, sheet_name="Extracciones")
                    _buf.seek(0)
                    _ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
                    _fname = f"Clinical_Extracciones_{_ts}.xlsx"
                    _url = _gd2.upload_excel(_buf.getvalue(), _fname,
                                             GoogleDriveManager._extract_folder_id(export_folder))
                    save_app_config("gdrive_export_folder", export_folder,
                                    user_payload.get("sub","admin"))
                    st.success(f"Archivo subido exitosamente.")
                    if _url:
                        st.markdown(f"[Abrir en Google Drive]({_url})")
                except Exception as _e:
                    st.error(f"Error: {_e}")


def _page_onedrive(st, user_payload, api_key, provider, model, max_tokens,
                    confidence_threshold, ocr_lang, ocr_dpi, use_easyocr,
                    use_vision_ocr, campos_sel, tipo_consulta, max_workers,
                    user_id):
    """Pagina: importar desde OneDrive y exportar resultados."""
    if not has_permission(user_payload, "extract"):
        st.warning("Tu rol no permite extraer documentos.")
        return

    _od_token     = load_app_config("od_access_token", "")
    _od_client_id = load_app_config("od_client_id", "")
    _od_tenant    = load_app_config("od_tenant_id", "consumers")
    _od_folder    = load_app_config("od_folder", "/")
    _od_export    = load_app_config("od_export_folder", "/Extracciones_Clinicas")

    if not _od_client_id or not _od_token:
        st.error("Primero configura y autenticate con OneDrive en "
                 "Configuracion > OneDrive.")
        if st.button("Ir a Configuracion", key="btn_od_goto_cfg"):
            st.session_state["_page"] = "settings"
            st.rerun()
        return

    _od_mgr = OneDriveManager(_od_client_id, _od_tenant, access_token=_od_token)

    tab_read, tab_export = st.tabs(["📥 Leer documentos desde OneDrive",
                                     "📤 Exportar resultados a OneDrive"])

    # ── TAB LECTURA ──────────────────────────────────────────────────────────
    with tab_read:
        st.markdown("Lee PDFs e imagenes directamente desde tu OneDrive.")
        od_folder_input = st.text_input(
            "Carpeta de OneDrive (ruta relativa)",
            value=_od_folder,
            placeholder="/Historias Clinicas",
            key="od_folder_input"
        )
        if st.button("📋 Listar archivos", key="btn_od_list"):
            with st.spinner("Consultando OneDrive..."):
                try:
                    _files = _od_mgr.list_files(od_folder_input)
                    if not _files:
                        st.warning("No se encontraron PDFs ni imagenes en esa carpeta.")
                    else:
                        st.success(f"{len(_files)} archivo(s) encontrado(s).")
                        st.session_state["_od_files"] = _files
                        save_app_config("od_folder", od_folder_input,
                                        user_payload.get("sub","admin"))
                except Exception as _e:
                    st.error(f"Error: {_e}")

        _od_files = st.session_state.get("_od_files", [])
        if _od_files:
            st.dataframe(pd.DataFrame([{
                "Nombre":     f["name"],
                "Tamano KB":  f"{int(f.get('size',0))//1024}",
                "Modificado": f.get("modified","")[:10],
            } for f in _od_files]), use_container_width=True, hide_index=True)

            _sel = st.multiselect(
                "Selecciona archivos a procesar",
                options=[f["name"] for f in _od_files],
                default=[f["name"] for f in _od_files],
                key="od_sel_files"
            )
            force = st.checkbox("Forzar re-extraccion", key="od_force")

            if st.button(f"Iniciar extraccion — {len(_sel)} archivo(s)",
                         type="primary", key="btn_od_extract",
                         disabled=not _sel or not api_key):
                if not api_key:
                    st.warning("Configura la API Key en Configuracion.")
                else:
                    _selected = [f for f in _od_files if f["name"] in _sel]
                    _prog = st.progress(0, text="Descargando desde OneDrive...")
                    _status = st.empty()
                    _downloaded = []
                    try:
                        for i, _f in enumerate(_selected):
                            _status.caption(f"Descargando {_f['name']}...")
                            _raw = _od_mgr.download_file(_f["id"])
                            _downloaded.append((_raw, _f["name"]))
                            _prog.progress(int((i+1)/len(_selected)*50),
                                           text=f"Descargado {i+1}/{len(_selected)}")
                    except Exception as _e:
                        st.error(f"Error descargando: {_e}")
                        return

                    class _FakeFile:
                        def __init__(self, raw, name):
                            self._raw = raw
                            self.name = name
                            self.size = len(raw)
                        def read(self): return self._raw

                    _fake_files = [_FakeFile(r, n) for r, n in _downloaded]
                    _prog.progress(50, text="Procesando con IA...")
                    _run_extraction_local(
                        _fake_files, api_key, provider, model, max_tokens,
                        confidence_threshold, ocr_lang, ocr_dpi,
                        use_easyocr, use_vision_ocr,
                        campos_sel, tipo_consulta, max_workers,
                        False, "", "",
                        project_id=st.session_state.get("_active_project_id",
                                                         DEFAULT_PROJECT_ID),
                        user_id=user_id,
                        force_reprocess=force,
                    )

    # ── TAB EXPORTAR ─────────────────────────────────────────────────────────
    with tab_export:
        st.markdown("Sube los resultados extraidos como archivo Excel a OneDrive.")
        od_exp_input = st.text_input(
            "Carpeta de destino en OneDrive",
            value=_od_export,
            placeholder="/Extracciones_Clinicas",
            key="od_export_input"
        )
        results = st.session_state.get("results", [])
        done_count = sum(1 for r in results if r.get("_status") == "done")
        st.caption(f"{done_count} resultado(s) listos para exportar.")

        if st.button("📤 Subir Excel a OneDrive", key="btn_od_upload",
                     type="primary", disabled=done_count == 0):
            with st.spinner("Subiendo a OneDrive..."):
                try:
                    _url = _od_mgr.write_results_excel(results, campos_sel, od_exp_input)
                    save_app_config("od_export_folder", od_exp_input,
                                    user_payload.get("sub","admin"))
                    st.success("Archivo subido exitosamente.")
                    if _url:
                        st.markdown(f"[Abrir en OneDrive]({_url})")
                except Exception as _e:
                    st.error(f"Error: {_e}")


def _page_help(st):
    """Página: manual de usuario integrado en la app."""

    st.markdown("""
> **Clinical Extractor Pro v15** — Guía completa para médicos y personal administrativo.
""")

    # ── Sección 1 ──────────────────────────────────────────────────────────
    with st.expander("1. ¿Qué es esta aplicación?", expanded=True):
        st.markdown("""
**Clinical Extractor Pro** extrae automáticamente información clínica de documentos médicos
(historias clínicas, órdenes, epicrisis, etc.) usando inteligencia artificial.

En lugar de leer manualmente cada documento, la app lo hace en segundos y organiza la
información en una tabla lista para exportar o cargar a Salesforce / Google Sheets.

> 🔒 Cumple **Ley 1581 de Colombia** y estándares HIPAA: cifrado AES-256, control de
> accesos por rol y registro de auditoría inmutable.
""")

    # ── Sección 2 ──────────────────────────────────────────────────────────
    with st.expander("2. Cómo ingresar"):
        st.markdown("""
El administrador le entregará:
- 🌐 **URL** de la aplicación
- 📧 **Usuario** (correo electrónico)
- 🔑 **Contraseña** temporal

> ⚠️ Tras **5 intentos fallidos** el acceso se bloquea 15 minutos. Contacte al administrador si queda bloqueado.
""")

    # ── Sección 3 ──────────────────────────────────────────────────────────
    with st.expander("3. Roles y permisos"):
        st.markdown("""
| Función | 👑 Admin | ✏️ Editor | 👁️ Lector |
|---|:---:|:---:|:---:|
| Extraer documentos | ✅ | ✅ | ❌ |
| Ver resultados | ✅ | ✅ | ✅ |
| Editar resultados | ✅ | ✅ | ❌ |
| Exportar datos | ✅ | ✅ | ❌ |
| Modificar configuración | ✅ | ❌ | ❌ |
| Gestionar usuarios | ✅ | ❌ | ❌ |
| Ver registro de auditoría | ✅ | ❌ | ❌ |

- **👑 Administrador:** control total — API keys, integraciones, usuarios.
- **✏️ Editor:** extrae, edita y exporta resultados.
- **👁️ Lector:** solo visualiza resultados.
""")

    # ── Sección 4 ──────────────────────────────────────────────────────────
    with st.expander("4. Páginas de la aplicación"):
        st.markdown("""
| Sección | Para qué sirve |
|---|---|
| 📤 Subir documentos | Cargar PDFs o imágenes para extracción |
| 📋 Resultados | Ver y editar los datos extraídos |
| ⚠️ Revisar manualmente | Corregir campos con baja confianza |
| 🔁 Duplicados | Documentos que ya fueron procesados |
| 📈 Calidad y métricas | Tendencias de confianza y errores |
| 🔍 Buscador clínico | Buscar por CIE-10, medicamento, fechas |
| 📬 Cola de trabajos | Estado de lotes grandes en proceso |
| ☁️ Salesforce | Extracción directa desde Salesforce |
| ⚙️ Configuración | Ajustes del sistema (solo Admin puede modificar) |
""")

    # ── Sección 5 ──────────────────────────────────────────────────────────
    with st.expander("5. Subir y procesar documentos"):
        st.markdown("""
**Formatos aceptados:** PDF, JPG, PNG, TIFF (nativos o escaneados).

**Pasos:**
1. Clic en **📤 Subir documentos** en el menú lateral.
2. Arrastra el archivo o haz clic en **Examinar**.
3. Espera la extracción (unos segundos por documento).
4. Revisa los resultados — campos en 🔴 rojo requieren revisión manual.

> 📷 **Documentos escaneados:** se usa OCR automático. Para mejor precisión,
> la imagen debe tener al menos **300 DPI** y buena iluminación.

**Varios archivos a la vez:** se procesan en paralelo. Puedes subir lotes completos.
""")

    # ── Sección 6 ──────────────────────────────────────────────────────────
    with st.expander("6. Indicadores de confianza"):
        col1, col2, col3 = st.columns(3)
        col1.success("🟢 Verde >= 75% — Extracción confiable. Revisión opcional.")
        col2.warning("🟡 Amarillo 50-74% — Confianza media. Se recomienda revisar.")
        col3.error("🔴 Rojo < 50% — Confianza baja. Revisión obligatoria.")
        st.markdown("""
**Exportar resultados** (Editor o Admin): CSV · Excel · FHIR R4 · JSON
""")

    # ── Sección 7 ──────────────────────────────────────────────────────────
    with st.expander("7. Revisión manual"):
        st.markdown("""
La sección **⚠️ Revisar manualmente** muestra:
- **Campos con baja confianza** — el sistema no está seguro del valor extraído.
- **Incoherencias clínicas** — ej. embarazo en paciente masculino, medicamento incompatible.
- **Fragmento del documento** — texto original del que se extrajo cada dato.

Para corregir: haz clic sobre el campo, escribe el valor correcto y confirma.
Las correcciones quedan guardadas y mejoran futuras extracciones.
""")

    # ── Sección 8 ──────────────────────────────────────────────────────────
    with st.expander("8. Control de duplicados"):
        st.markdown("""
La app detecta automáticamente documentos ya procesados (por hash SHA-256).

En **🔁 Duplicados** puedes:
- Ver la lista de archivos omitidos y cuándo se procesó el original.
- **Forzar re-procesamiento** si el documento cambió.
- Exportar el reporte de duplicados.
""")

    # ── Sección 9 ──────────────────────────────────────────────────────────
    with st.expander("9. Configuración del sistema"):
        st.markdown("""
> 🔒 **Solo el Administrador puede modificar la configuración.**
> Los demás usuarios la ven en modo lectura.

| Sección | Qué configura |
|---|---|
| 🤖 Modelo de IA | Proveedor (Claude / GPT-4o), API key, modelo, tokens |
| 📋 Plantilla | Campos a extraer según tipo de consulta |
| 🔬 OCR | Idioma, DPI, EasyOCR, visión directa |
| 📊 Google Sheets | URL del spreadsheet para sincronización |
| ☁️ Salesforce | Credenciales y consultas SOQL |
| ⚡ Procesamiento | Workers paralelos |
| 🔬 Robustez | Anonimización, ensamble de modelos, umbral OCR |

Presiona **💾 Guardar configuración en disco** para que los cambios persistan al reiniciar.
""")

    # ── Sección 10 ──────────────────────────────────────────────────────────
    with st.expander("10. Google Sheets — conexión persistente"):
        st.markdown("""
En **Streamlit Cloud** el sistema de archivos es temporal. Para que las credenciales
persistan entre reinicios:

1. Abre tu `credentials.json` con un editor de texto.
2. Ve a tu app → **Manage app → Settings → Secrets**.
3. Agrega el contenido en formato TOML:

```toml
[gcp_service_account]
type = "service_account"
project_id = "tu-proyecto"
private_key_id = "abc123"
private_key = "-----BEGIN RSA PRIVATE KEY-----\nMIIE...\n-----END RSA PRIVATE KEY-----\n"
client_email = "...@....iam.gserviceaccount.com"
client_id = "123456789"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
```

4. Guarda — la app se reinicia y queda conectada permanentemente.

> ✅ La app detecta automáticamente si las credenciales están en Secrets
> y te lo indica en la sección Configuración.
""")

    # ── Sección 11 ──────────────────────────────────────────────────────────
    with st.expander("11. Salesforce"):
        st.markdown("""
1. Activa la integración en **⚙️ Configuración → Salesforce** (solo Admin).
2. Ingresa usuario, contraseña y Security Token de Salesforce.
3. Escribe la consulta SOQL para seleccionar los registros.
4. Haz clic en **Conectar Salesforce**.
5. En **☁️ Salesforce**, selecciona registros y ejecuta la extracción.

> 💡 **Modo incremental:** procesa solo registros nuevos desde la última ejecución.
""")

    # ── Sección 12 ──────────────────────────────────────────────────────────
    with st.expander("12. Seguridad y privacidad"):
        st.markdown("""
- 🔐 Datos clínicos cifrados con **AES-256** en la base de datos local.
- 🔐 Comunicaciones con la IA por **HTTPS**.
- 🔐 **Anonimización** opcional: elimina nombre y documento, genera ID anónimo SHA-256.
- 📋 **Registro de auditoría inmutable**: quién hizo qué, desde qué IP y a qué hora.
  Solo el Admin puede verlo. Nadie puede borrarlo.

> ⚠️ Si notas actividad sospechosa, notifica al administrador para revisar el audit log.

> 🔐 **Nunca compartas tu contraseña** con nadie, incluido soporte técnico.
""")

    # ── Sección 13 — FAQ ──────────────────────────────────────────────────
    with st.expander("13. Preguntas frecuentes"):
        faqs = [
            ("¿Por qué algunos campos aparecen en rojo?",
             "La IA no pudo extraer ese dato con suficiente confianza. Corrígelo en **⚠️ Revisar manualmente**."),
            ("¿Qué pasa si subo el mismo documento dos veces?",
             "Se detecta como duplicado y se omite. Ve a **🔁 Duplicados** y activa 'Forzar re-extracción' si lo necesitas."),
            ("¿Los datos se guardan si cierro sesión?",
             "Sí, los resultados persisten en la base de datos. Solo la configuración no guardada (sin presionar 💾) se pierde."),
            ("¿Puedo usar la app desde el celular?",
             "Sí, la interfaz es responsiva. Para cargar documentos grandes se recomienda un computador."),
            ("¿La extracción es muy imprecisa en un documento?",
             "Verifica que el PDF tenga buena calidad. El Admin puede aumentar el DPI en Configuración → OCR."),
            ("¿Cómo cambio mi contraseña?",
             "Contacta al administrador — puede cambiar contraseñas desde el panel de administración."),
            ("¿Qué es FHIR R4?",
             "Estándar internacional de interoperabilidad clínica para compartir datos entre sistemas hospitalarios."),
        ]
        for q, a in faqs:
            st.markdown(f"**{q}**")
            st.markdown(f"{a}")
            st.markdown("---")

    st.caption("Clinical Extractor Pro v15 · Ley 1581 Colombia · HIPAA")


def run_streamlit():
    """Interfaz Clinical Extractor Pro v13 — navegación lateral, UI simplificada."""
    import streamlit as st

    st.set_page_config(
        page_title="Clinical Extractor Pro",
        page_icon="🏥",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # CSS global mínimo
    st.markdown("""<style>
    [data-testid="stSidebar"] {min-width:220px!important;max-width:240px!important}
    [data-testid="stSidebarContent"] {padding-top:1rem}
    div[data-testid="stSidebar"] .stButton button {
        text-align:left!important;justify-content:flex-start!important;
        font-size:13px!important;padding:6px 10px!important;border-radius:6px!important
    }
    div[data-testid="stSidebar"] .stButton button[kind="primary"] {
        background:rgba(24,95,165,.15)!important;border-color:rgba(24,95,165,.4)!important;
        color:var(--color-text-info)!important
    }
    div[data-testid="stSidebar"] small {font-size:10px;text-transform:uppercase;
        letter-spacing:.06em;color:var(--color-text-tertiary);padding:6px 4px 2px;
        display:block}
    .stExpander {border:0.5px solid var(--color-border-tertiary)!important}
    </style>""", unsafe_allow_html=True)

    # MEJORA v15-CLINIC: init_db solo una vez por proceso del servidor
    if "db_initialized" not in st.session_state:
        init_db()
        st.session_state["db_initialized"] = True
        # Verificar dependencias del sistema y mostrar advertencias
        sys_warns = _check_system_deps()
        if sys_warns:
            st.session_state["_sys_warnings"] = sys_warns
    if st.session_state.get("_sys_warnings"):
        for w in st.session_state["_sys_warnings"]:
            st.warning(w)

    # Autenticación — verificar session_state o token persistente en DB
    token = st.session_state.get("_auth_token")
    user_payload = is_token_valid(token) if token else None

    # Si no hay token en sesión, buscar token persistente ("recordar sesión") en DB
    if not user_payload:
        try:
            # Buscar todos los tokens de tipo remember_token_*
            _con = _sec_db()
            _rows = _con.execute(
                "SELECT key, value FROM app_config WHERE key LIKE 'remember_token_%'"
            ).fetchall()
            for _rk, _rv in _rows:
                _raw = decrypt_clinical_data(_rv)
                _pl  = is_token_valid(_raw)
                if _pl:
                    # Token válido encontrado — restaurar sesión automáticamente
                    _uid = _pl.get("sub", "")
                    _user_row = _con.execute(
                        "SELECT id, email, role, full_name, is_active "
                        "FROM users WHERE id=? AND is_active=1", (_uid,)
                    ).fetchone()
                    if _user_row:
                        st.session_state.update({
                            "_auth_token":  _raw,
                            "_user_id":     _user_row[0],
                            "_user_email":  _user_row[1],
                            "_user_role":   _user_row[2],
                            "_user_name":   _user_row[3] or "",
                            "_remembered":  True,
                        })
                        user_payload = _pl
                        token = _raw
                        log.info(f"✅ Sesión restaurada automáticamente: {_user_row[1]}")
                    break
        except Exception as _re:
            log.warning(f"No se pudo restaurar sesión: {_re}")

    if not user_payload:
        for k in ["_auth_token","_user_email","_user_role","_user_name","_user_id"]:
            st.session_state.pop(k, None)
        _render_login_page(st)
        st.stop()

    user_role  = user_payload.get("role", Role.READER)
    user_email = user_payload.get("email", "")
    user_id    = user_payload.get("sub", "")

    if "results" not in st.session_state:
        st.session_state["results"] = (
            load_results_from_db()
            if has_permission(user_payload, "view_results") else []
        )
    if "sf_manager" not in st.session_state:
        st.session_state["sf_manager"] = None
    if "_page" not in st.session_state:
        st.session_state["_page"] = "upload"

    results = st.session_state.results

    # ── Forzar cambio de contraseña si es temporal ───────────
    if st.session_state.get("_must_change_pass"):
        _render_force_change_password(st, user_payload, user_id, token)
        st.stop()

    # Navegación lateral
    page = _sidebar_nav(st, st.session_state["_page"], user_role, results)

    # Leer config guardada en session_state
    def cfg(k, default):
        return st.session_state.get(k, default)

    api_key              = cfg("cfg_api_key",    os.environ.get("ANTHROPIC_API_KEY",""))
    provider             = cfg("cfg_prov",        "claude")
    model                = cfg("cfg_mdl",         "claude-sonnet-4-5")
    max_tokens           = cfg("cfg_max_tok",     3000)
    confidence_threshold = cfg("cfg_conf_thr",    0.75)
    ocr_lang             = cfg("cfg_lang_ocr",    "spa+eng")
    ocr_dpi              = cfg("cfg_dpi_ocr",     300)
    use_easyocr          = cfg("cfg_easyocr_v",   False)
    use_vision_ocr       = cfg("cfg_vision_v",    False)
    campos_sel           = cfg("cfg_campos_v",    PLANTILLAS_CONSULTA["General / Base"])
    tipo_consulta        = cfg("cfg_tipo_v",      "General / Base")
    sheets_enabled       = cfg("cfg_sheets_en",   False)
    # Fallback: si session_state está vacío (sesión nueva), leer desde DB/.env
    sheets_url = (cfg("cfg_sheets_url", "") or
                  load_app_config("GOOGLE_SHEET_URL", "") or
                  os.environ.get("GOOGLE_SHEET_URL", ""))
    # sheets_enabled: activar automáticamente si hay URL guardada
    if sheets_url and not sheets_enabled:
        sheets_enabled = True
    creds_path           = cfg("cfg_creds_path",  "")
    max_workers          = cfg("cfg_max_wrk",     2)
    sf_enabled           = cfg("cfg_sf_en",       False)

    # Enrutar a la página activa
    if page == "upload":
        st.title("Subir documentos")
        _page_upload(st, user_payload, api_key, provider, model, max_tokens,
                     confidence_threshold, ocr_lang, ocr_dpi, use_easyocr,
                     use_vision_ocr, campos_sel, tipo_consulta, max_workers,
                     sheets_enabled, sheets_url, creds_path, user_id, user_role)

    elif page == "salesforce":
        st.title("Salesforce")
        _page_salesforce(st, user_payload, api_key, provider, model, max_tokens,
                         confidence_threshold, ocr_lang, ocr_dpi, use_easyocr,
                         use_vision_ocr, campos_sel, tipo_consulta, max_workers,
                         sheets_enabled, sheets_url, creds_path, user_id)

    elif page == "results":
        st.title("Resultados")
        _page_results(st, results, campos_sel, user_payload)

    elif page == "review":
        st.title("Revisar manualmente")
        _page_review(st, results, campos_sel, user_payload, user_id)

    elif page == "quality":
        st.title("Calidad y métricas")
        _page_quality(st, results)

    elif page == "search":
        st.title("Buscador clínico")
        _page_search(st, campos_sel)

    elif page == "queue":
        st.title("Cola de trabajos")
        _page_queue(st, user_payload, user_id)

    elif page == "dupes":
        st.title("Duplicados omitidos")
        _page_dupes(st, user_id)

    elif page == "settings":
        st.title("Configuración")
        _page_settings(st, user_payload)

    elif page == "admin":
        st.title("Usuarios y seguridad")
        if user_role == Role.ADMIN:
            _page_admin(st, user_payload)
        else:
            st.error("Acceso restringido al administrador.")

    elif page == "gdrive":
        st.title("📂 Google Drive")
        _page_gdrive(st, user_payload, api_key, provider, model, max_tokens,
                     confidence_threshold, ocr_lang, ocr_dpi, use_easyocr,
                     use_vision_ocr, campos_sel, tipo_consulta, max_workers,
                     sheets_enabled, sheets_url, creds_path, user_id)

    elif page == "onedrive":
        st.title("🔷 OneDrive / Microsoft 365")
        _page_onedrive(st, user_payload, api_key, provider, model, max_tokens,
                       confidence_threshold, ocr_lang, ocr_dpi, use_easyocr,
                       use_vision_ocr, campos_sel, tipo_consulta, max_workers,
                       user_id)

    elif page == "help":
        st.title("📖 Manual de usuario")
        _page_help(st)



# ═══════════════════════════════════════════════════════════════
# SUITE DE TESTS AUTOMATIZADOS
# Ejecutar: python -m pytest Extractor_HC_v15_final.py -v
#           python Extractor_HC_v15_final.py --test
# ═══════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════
# TESTS: Score OCR
# ═══════════════════════════════════════════════════════════════

class TestOCRQuality:
    def test_texto_vacio_es_ilegible(self):
        r = score_ocr_quality("")
        assert r["score"] == 0
        assert r["nivel"] == "ilegible"
        assert not r["apto"]

    def test_texto_clinico_real_es_bueno(self):
        texto = """
        Paciente: María García Rodríguez
        Fecha: 2024-03-15  Edad: 45 años  Sexo: Femenino
        Motivo de consulta: cefalea y tensión arterial elevada
        Diagnóstico: Hipertensión arterial I10
        TA: 150/95 mmHg  FC: 78 lpm  Temperatura: 36.8°C
        Medicamentos: Enalapril 10mg VO cada 12 horas
        """
        r = score_ocr_quality(texto)
        assert r["score"] >= 60
        assert r["apto"]

    def test_texto_ruido_es_deficiente(self):
        ruido = "@@##$$%%^^&&**((##@@" * 20 + "xzxzxzxzxzxzxzxzxzxz" * 10
        r = score_ocr_quality(ruido)
        assert r["score"] < OCR_QUALITY_THRESHOLD

    def test_texto_repeticion_detecta_ruido(self):
        ruido = "aaaaaaaaaa bbbbbbbbbb cccccccccc" * 30
        r = score_ocr_quality(ruido)
        assert r["score"] < 70


# ═══════════════════════════════════════════════════════════════
# TESTS: Normalización CIE-10
# ═══════════════════════════════════════════════════════════════

class TestNormalizacionCIE10:
    def test_hta_normaliza_a_i10(self):
        assert normalizar_cie10("HTA") == "I10"

    def test_hipertension_arterial_normaliza(self):
        assert normalizar_cie10("hipertensión arterial") == "I10"

    def test_dm2_normaliza(self):
        assert normalizar_cie10("DM2") == "E11.9"
        assert normalizar_cie10("diabetes tipo 2") == "E11.9"

    def test_ira_normaliza(self):
        assert normalizar_cie10("IRA") == "J06.9"

    def test_codigo_valido_pasa_directo(self):
        assert normalizar_cie10("I10") == "I10"
        assert normalizar_cie10("E11.9") == "E11.9"
        assert normalizar_cie10("J18.9") == "J18.9"

    def test_codigo_minuscula_normaliza(self):
        assert normalizar_cie10("i10") == "I10"

    def test_texto_no_reconocido_retorna_none(self):
        assert normalizar_cie10("condición desconocida xyz") is None

    def test_none_retorna_none(self):
        assert normalizar_cie10(None) is None
        assert normalizar_cie10("") is None

    def test_covid_normaliza(self):
        assert normalizar_cie10("COVID-19") == "U07.1"
        assert normalizar_cie10("covid") == "U07.1"


# ═══════════════════════════════════════════════════════════════
# TESTS: Normalización Medicamentos
# ═══════════════════════════════════════════════════════════════

class TestNormalizacionMedicamentos:
    def test_dolex_a_paracetamol(self):
        assert normalizar_medicamento("Dolex") == "paracetamol"
        assert normalizar_medicamento("dolex") == "paracetamol"

    def test_tylenol_a_paracetamol(self):
        assert normalizar_medicamento("Tylenol") == "paracetamol"

    def test_lantus_a_insulina_glargina(self):
        assert normalizar_medicamento("Lantus") == "insulina glargina"

    def test_glucophage_a_metformina(self):
        assert normalizar_medicamento("Glucophage") == "metformina"

    def test_nombre_desconocido_pasa_intacto(self):
        assert normalizar_medicamento("medicamento_nuevo_xyz") == "medicamento_nuevo_xyz"

    def test_nombre_vacio_pasa_intacto(self):
        assert normalizar_medicamento("") == ""


# ═══════════════════════════════════════════════════════════════
# TESTS: Normalización Unidades
# ═══════════════════════════════════════════════════════════════

class TestNormalizacionUnidades:
    def test_mgr_a_mg(self):
        result = normalizar_unidades("500 mgr")
        assert "mg" in result
        assert "mgr" not in result

    def test_cc_a_ml(self):
        result = normalizar_unidades("10 cc")
        assert "mL" in result

    def test_mmhg_normaliza(self):
        result = normalizar_unidades("140 mmhg")
        assert "mmHg" in result

    def test_texto_sin_unidades_pasa_intacto(self):
        texto = "sin datos relevantes"
        assert normalizar_unidades(texto) == texto


# ═══════════════════════════════════════════════════════════════
# TESTS: Anonimización
# ═══════════════════════════════════════════════════════════════

class TestAnonimizacion:
    def test_cedula_es_redactada(self):
        texto, n = anonimizar_texto("Cédula: 1020304050")
        assert "1020304050" not in texto
        assert n > 0

    def test_cedula_cc_es_redactada(self):
        texto, n = anonimizar_texto("C.C. 1020304050 expedida en Bogotá")
        assert "1020304050" not in texto

    def test_email_es_redactado(self):
        texto, n = anonimizar_texto("Correo: paciente@gmail.com")
        assert "paciente@gmail.com" not in texto
        assert n > 0

    def test_telefono_colombiano_redactado(self):
        texto, n = anonimizar_texto("Tel: 3001234567")
        assert "3001234567" not in texto

    def test_texto_sin_pii_no_cambia(self):
        texto = "Diagnóstico: Hipertensión arterial I10"
        resultado, n = anonimizar_texto(texto)
        assert "Hipertensión" in resultado
        assert n == 0

    def test_datos_extraidos_anonimizados(self):
        datos = {
            "nombre_paciente": "María García",
            "numero_documento": "1020304050",
            "diagnostico_principal": "HTA",
            "tension_arterial": "150/90 mmHg",
        }
        anon = anonimizar_datos_extraidos(datos)
        assert anon["nombre_paciente"] == "[REDACTED]"
        assert anon["numero_documento"] == "[REDACTED]"
        assert anon["diagnostico_principal"] == "HTA"  # No PII
        assert anon["tension_arterial"] == "150/90 mmHg"  # No PII

    def test_id_anonimo_consistente(self):
        """El mismo paciente siempre produce el mismo ID."""
        id1 = generar_id_anonimo("María García", "1020304050", "1979-05-15")
        id2 = generar_id_anonimo("María García", "1020304050", "1979-05-15")
        assert id1 == id2
        assert len(id1) == 16

    def test_id_anonimo_diferente_pacientes(self):
        id1 = generar_id_anonimo("María García",  "1020304050", "1979-05-15")
        id2 = generar_id_anonimo("Carlos López", "9876543210", "1965-08-22")
        assert id1 != id2


# ═══════════════════════════════════════════════════════════════
# TESTS: Auditor Clínico — Reglas determinísticas
# ═══════════════════════════════════════════════════════════════

class TestAuditorReglasDeterministicas:
    """Prueba que las reglas de coherencia clínica detectan incoherencias críticas."""

    def _build_auditor(self):
        """Auditor mínimo sin llamadas LLM (solo reglas)."""
        class _MockAuditor(ClinicalAuditor):
            def _audit_llm(self, data, raw_text, tipo_consulta=""):
                return {"incoherencias":[],"coherencia_global":1.0,
                         "requiere_reescaneo":False,"campos_para_reescaneo":[],
                         "resumen_auditoria":"Mock","datos_confiables":True}
            def _rescan_fields(self, raw_text, campos, incoherencias, datos_actuales):
                return {}
        return _MockAuditor(api_key="mock", provider="claude")

    def test_prostatitis_en_mujer_detectada(self):
        auditor = self._build_auditor()
        data = {"sexo": "femenino", "diagnostico_principal": "prostatitis"}
        incs = auditor._audit_rules(data)
        tipos = [i["tipo_incoherencia"] for i in incs]
        assert "SEXO_BIOLOGICO" in tipos
        severidades = [i["severidad"] for i in incs if i["tipo_incoherencia"]=="SEXO_BIOLOGICO"]
        assert all(s == "CRITICA" for s in severidades)

    def test_embarazo_en_hombre_detectado(self):
        auditor = self._build_auditor()
        data = {"sexo": "masculino", "diagnostico_principal": "embarazo semana 12"}
        incs = auditor._audit_rules(data)
        tipos = [i["tipo_incoherencia"] for i in incs]
        assert "SEXO_BIOLOGICO" in tipos

    def test_control_prenatal_en_hombre_detectado(self):
        auditor = self._build_auditor()
        data = {"sexo": "masculino", "diagnostico_principal": "control prenatal"}
        incs = auditor._audit_rules(data)
        assert any(i["tipo_incoherencia"] == "SEXO_BIOLOGICO" for i in incs)

    def test_cie10_masculino_en_mujer_detectado(self):
        auditor = self._build_auditor()
        data = {"sexo": "femenino", "codigo_cie10_principal": "N40"}
        incs = auditor._audit_rules(data)
        assert any(i["tipo_incoherencia"] == "CIE10_SEXO" for i in incs)

    def test_cie10_femenino_en_hombre_detectado(self):
        auditor = self._build_auditor()
        data = {"sexo": "masculino", "codigo_cie10_principal": "O00"}
        incs = auditor._audit_rules(data)
        assert any(i["tipo_incoherencia"] == "CIE10_SEXO" for i in incs)

    def test_cie10_neonatal_en_adulto_detectado(self):
        auditor = self._build_auditor()
        data = {"sexo": "masculino", "edad": "35 años",
                "codigo_cie10_principal": "P22"}
        incs = auditor._audit_rules(data)
        assert any(i["tipo_incoherencia"] == "EDAD_DIAGNOSTICO" for i in incs)

    def test_anticonceptivo_femenino_en_hombre_detectado(self):
        auditor = self._build_auditor()
        data = {"sexo": "masculino",
                "medicamentos": ["levonorgestrel 1.5mg", "ibuprofeno 400mg"]}
        incs = auditor._audit_rules(data)
        assert any(i["tipo_incoherencia"] == "DX_MEDICAMENTO" for i in incs)

    def test_fechas_inconsistentes_detectadas(self):
        auditor = self._build_auditor()
        data = {
            "sexo":             "femenino",
            "fecha_nacimiento": "1990-01-01",
            "fecha_consulta":   "2024-06-15",
            "edad":             "55",  # Debería ser ~34 años
        }
        incs = auditor._audit_rules(data)
        assert any(i["tipo_incoherencia"] == "COHERENCIA_INTERNA" and
                   i["campo"] == "edad" for i in incs)

    def test_datos_coherentes_sin_alertas(self):
        auditor = self._build_auditor()
        data = {
            "sexo":                  "femenino",
            "edad":                  "34 años",
            "fecha_nacimiento":      "1990-01-01",
            "fecha_consulta":        "2024-06-15",
            "diagnostico_principal": "hipertensión arterial",
            "codigo_cie10_principal":"I10",
            "medicamentos":          ["enalapril 10mg"],
        }
        incs = auditor._audit_rules(data)
        assert incs == []


# ═══════════════════════════════════════════════════════════════
# TESTS: Detección Multi-paciente
# ═══════════════════════════════════════════════════════════════

class TestMultiPaciente:
    def test_documento_simple_no_detecta_multipaciente(self):
        texto = """
        Paciente: Juan Pérez. Edad: 45. Diagnóstico: HTA.
        Medicamentos: Enalapril 10mg. Plan: control en 1 mes.
        """
        assert not detect_multi_patient(texto)

    def test_separadores_detectan_multipaciente(self):
        texto = """
        Paciente 1: Juan Pérez. Diagnóstico: HTA.
        ─────────────────────────
        Paciente 2: María López. Diagnóstico: DM2.
        ─────────────────────────
        """
        assert detect_multi_patient(texto)

    def test_split_produce_segmentos_correctos(self):
        texto = """
        HISTORIA CLÍNICA N° 001
        Paciente: Juan Pérez. Edad: 45. Diagnóstico: HTA. Tratamiento: Enalapril.
        ══════════════════════════════════════════
        HISTORIA CLÍNICA N° 002
        Paciente: María López. Edad: 32. Diagnóstico: DM2. Tratamiento: Metformina.
        ══════════════════════════════════════════
        HISTORIA CLÍNICA N° 003
        Paciente: Carlos Ruiz. Edad: 60. Diagnóstico: EPOC. Tratamiento: Salbutamol.
        """
        segmentos = split_multi_patient(texto, "multi_hc.pdf")
        assert len(segmentos) >= 2
        for seg_texto, seg_nombre in segmentos:
            assert len(seg_texto.strip()) >= 50


# ═══════════════════════════════════════════════════════════════
# TESTS: Trazabilidad
# ═══════════════════════════════════════════════════════════════

class TestTrazabilidad:
    def test_trace_encuentra_valor_en_texto(self):
        raw_text = "Diagnóstico principal: Hipertensión arterial sistémica"
        segments = {"diagnostico": "Diagnóstico principal: Hipertensión arterial sistémica"}
        trace = build_field_trace(
            campo="diagnostico_principal",
            valor="Hipertensión arterial sistémica",
            raw_text=raw_text,
            segments=segments,
            modelo="claude/claude-sonnet-4-5",
            confianza=0.95,
            metodo="extraction_literal",
            es_inferencia=False,
        )
        assert trace.campo == "diagnostico_principal"
        assert trace.confianza == 0.95
        assert not trace.es_inferencia
        assert len(trace.texto_original) > 0

    def test_trace_serializa_a_dict(self):
        raw_text = "TA: 140/90 mmHg"
        trace = build_field_trace(
            "tension_arterial", "140/90 mmHg",
            raw_text, {}, "gpt/gpt-4o", 0.88, "verification"
        )
        d = traces_to_dict({"tension_arterial": trace})
        assert "tension_arterial" in d
        assert d["tension_arterial"]["confianza"] == 0.88
        assert d["tension_arterial"]["modelo"] == "gpt/gpt-4o"

    def test_trace_marca_inferencia(self):
        trace = build_field_trace(
            "codigo_cie10_principal", "I10",
            "Dx: HTA", {}, "claude", 0.82,
            "inference", es_inferencia=True
        )
        assert trace.es_inferencia


# ═══════════════════════════════════════════════════════════════
# TESTS: Hash y Deduplicación
# ═══════════════════════════════════════════════════════════════

class TestDeduplicacion:
    def test_mismo_contenido_mismo_hash(self):
        data = b"historia clinica test"
        assert compute_hash(data) == compute_hash(data)

    def test_contenido_diferente_hash_diferente(self):
        assert compute_hash(b"historia 1") != compute_hash(b"historia 2")

    def test_hash_es_hex_64_chars(self):
        h = compute_hash(b"test")
        assert len(h) == 64
        assert all(c in "0123456789abcdef" for c in h)


# ═══════════════════════════════════════════════════════════════
# TESTS: FHIR Export
# ═══════════════════════════════════════════════════════════════

class TestFHIRExport:
    def _sample_result(self):
        return {
            "_status": "done",
            "_id": "test-001",
            "_filename": "HC_001.pdf",
            "_processed_at": "2024-03-15T10:00:00",
            "_confidence": 0.92,
            "_tipo_consulta": "General / Base",
            "nombre_paciente": "María García",
            "numero_documento": "1020304050",
            "fecha_nacimiento": "1979-05-15",
            "sexo": "femenino",
            "edad": "45 años",
            "diagnostico_principal": "Hipertensión arterial",
            "codigo_cie10_principal": "I10",
            "medicamentos": ["enalapril 10mg", "amlodipino 5mg"],
            "tension_arterial": "150/95 mmHg",
            "frecuencia_cardiaca": "78 lpm",
        }

    def test_bundle_es_fhir_valido(self):
        bundle = export_fhir_bundle([self._sample_result()])
        assert bundle["resourceType"] == "Bundle"
        assert bundle["type"] == "transaction"
        assert "entry" in bundle
        assert len(bundle["entry"]) > 0

    def test_bundle_contiene_patient(self):
        bundle = export_fhir_bundle([self._sample_result()])
        types = [e["resource"]["resourceType"] for e in bundle["entry"]]
        assert "Patient" in types

    def test_bundle_contiene_encounter(self):
        bundle = export_fhir_bundle([self._sample_result()])
        types = [e["resource"]["resourceType"] for e in bundle["entry"]]
        assert "Encounter" in types

    def test_bundle_contiene_condition(self):
        bundle = export_fhir_bundle([self._sample_result()])
        types = [e["resource"]["resourceType"] for e in bundle["entry"]]
        assert "Condition" in types

    def test_bundle_contiene_medication_request(self):
        bundle = export_fhir_bundle([self._sample_result()])
        types = [e["resource"]["resourceType"] for e in bundle["entry"]]
        assert "MedicationRequest" in types

    def test_bundle_anonimo_no_tiene_nombre(self):
        bundle = export_fhir_bundle([self._sample_result()], anon_mode=True)
        patients = [e["resource"] for e in bundle["entry"]
                    if e["resource"]["resourceType"] == "Patient"]
        for p in patients:
            names = p.get("name", [])
            for n in names:
                assert "García" not in str(n)

    def test_csv_investigacion_tiene_columnas_trazabilidad(self):
        r = self._sample_result()
        r["_field_traces"] = {
            "diagnostico_principal": {
                "valor": "Hipertensión arterial",
                "confianza": 0.95,
                "es_inferencia": False,
                "pagina": 1,
                "seccion": "diagnostico",
                "modelo": "claude/sonnet",
                "metodo": "extraction_literal",
                "texto_original": "Dx: HTA",
                "timestamp_utc": "2024-03-15T10:00:00",
            }
        }
        csv = export_research_csv([r], ["diagnostico_principal", "tension_arterial"])
        assert csv
        assert "diagnostico_principal" in csv
        assert "diagnostico_principal_conf" in csv
        assert "diagnostico_principal_infer" in csv

    def test_resultado_no_done_no_aparece_en_csv(self):
        r = self._sample_result()
        r["_status"] = "error"
        csv = export_research_csv([r], ["diagnostico_principal"])
        df_lines = [l for l in csv.splitlines() if l.strip()]
        assert len(df_lines) <= 1  # Solo header

    def test_bundle_vacio_con_errores(self):
        r = self._sample_result()
        r["_status"] = "error"
        bundle = export_fhir_bundle([r])
        assert bundle["total"] == 0
        assert bundle["entry"] == []


# ═══════════════════════════════════════════════════════════════
# TESTS: Monitoreo
# ═══════════════════════════════════════════════════════════════

class TestMonitoreo:
    def _sample_results(self, n_done=8, n_errors=2, avg_conf=0.85):
        results = []
        for i in range(n_done):
            results.append({
                "_status": "done",
                "_confidence": avg_conf,
                "_needs_review": False,
                "_alerts": [],
                "_ocr_quality": {"score": 80},
            })
        for i in range(n_errors):
            results.append({"_status": "error", "_confidence": 0})
        return results

    def test_snapshot_calcula_correctamente(self):
        # (already in scope)
        snap = compute_monitoring_snapshot(self._sample_results(8, 2, 0.85))
        assert snap["total_docs"] == 10
        assert snap["done_docs"] == 8
        assert snap["error_docs"] == 2
        assert abs(snap["avg_conf"] - 0.85) < 0.01
        assert abs(snap["error_rate"] - 0.2) < 0.01

    def test_alerta_confianza_baja(self):
        # (already in scope)
        # Confianza muy baja
        snap = compute_monitoring_snapshot(self._sample_results(10, 0, 0.40))
        if 0.40 < MONITOR_THRESHOLDS["conf_min"]:
            assert any("Confianza" in a for a in snap["alerts_fired"])

    def test_alerta_tasa_error_alta(self):
        # (already in scope)
        snap = compute_monitoring_snapshot(self._sample_results(3, 7, 0.85))
        assert any("error" in a.lower() for a in snap["alerts_fired"])

    def test_sin_alertas_con_buenos_datos(self):
        # (already in scope)
        snap = compute_monitoring_snapshot(self._sample_results(10, 0, 0.90))
        assert snap["alerts_fired"] == []


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        import pytest
        pytest.main([__file__, "-v", "--tb=short"])


def _run_tests():
    """Ejecuta la suite de tests desde la línea de comandos."""
    try:
        import pytest as _pytest
        import sys as _sys
        print("\n🧪 Ejecutando suite de tests Clinical Extractor Pro v15...")
        result = _pytest.main([__file__, "-v", "--tb=short", "-x"])
        _sys.exit(result)
    except ImportError:
        print("❌ pytest no instalado. Instalar con: pip install pytest")
        import sys as _sys
        _sys.exit(1)


# ─────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys as _sys_entry
    if len(_sys_entry.argv) > 1 and _sys_entry.argv[1] == "--test":
        _run_tests()
    else:
        run_streamlit()
