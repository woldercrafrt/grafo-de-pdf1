import subprocess
import json
import os
import html

def extract_pdf_pages(start_page, end_page):
    cmd = ['pdftotext', '-f', str(start_page), '-l', str(end_page), 'RAMÍREZ IBARRA MARÍA EUGENIA.pdf', '-']
    res = subprocess.run(cmd, capture_output=True, text=True)
    raw = res.stdout
    # Clean page breaks and clean up text
    pages_raw = raw.split('\x0c')
    formatted_pages = []
    curr_page = start_page
    for p in pages_raw:
        clean = p.strip()
        if clean:
            # Escape HTML
            clean_escaped = html.escape(clean)
            # Format paragraphs
            paras = clean_escaped.split('\n\n')
            p_html = "".join([f"<p>{para.replace(chr(10), ' ')}</p>" for para in paras if para.strip()])
            formatted_pages.append(f"<div class='page-block'><span class='page-marker'>📄 Página {curr_page} del PDF original (Tesis UACM):</span>{p_html}</div>")
        curr_page += 1
    return "".join(formatted_pages)

# Mapping of nodes with their respective exact PDF pages
node_mappings = [
    # --- 1. NÚCLEO DE LA SALUD ---
    {
        "id": "SALUD_CHAPELA",
        "title": "Definición de Salud (Luz María Chapela)",
        "group": "salud",
        "color": "#2d6a4f",
        "badge": "Núcleo de la Salud",
        "pages": (104, 107),
        "links": ["OTTAWA_1986", "PS_EMANCIPATORIA", "PS_INSTITUCIONAL", "SUJETO_ETICO", "PROYECTO_VIDA"]
    },
    {
        "id": "OTTAWA_1986",
        "title": "Carta de Ottawa (1986) y Prerrequisitos de Salud",
        "group": "salud",
        "color": "#2d6a4f",
        "badge": "Núcleo de la Salud",
        "pages": (85, 89),
        "links": ["SALUD_CHAPELA", "PS_INSTITUCIONAL", "PS_EMANCIPATORIA", "TERRITORIO_IZTAPALAPA"]
    },
    {
        "id": "PS_EMANCIPATORIA",
        "title": "Promoción de la Salud Emancipatoria",
        "group": "salud",
        "color": "#2d6a4f",
        "badge": "Núcleo de la Salud",
        "pages": (101, 106),
        "links": ["SALUD_CHAPELA", "SUJETO_ETICO", "ESI_EMANCIPATORIA", "MMH_MENENDEZ"]
    },
    {
        "id": "PS_INSTITUCIONAL",
        "title": "Promoción de la Salud Institucional",
        "group": "salud",
        "color": "#2d6a4f",
        "badge": "Núcleo de la Salud",
        "pages": (190, 194),
        "links": ["OTTAWA_1986", "ESTILOS_VIDA", "CONDONERIA_FOLLETOS", "BARRERAS_CENTRO_SALUD"]
    },
    {
        "id": "ESTILOS_VIDA",
        "title": "Enfoque de Estilos de Vida y Culpabilización",
        "group": "salud",
        "color": "#2d6a4f",
        "badge": "Núcleo de la Salud",
        "pages": (96, 100),
        "links": ["PS_INSTITUCIONAL", "MMH_MENENDEZ", "TERRITORIO_IZTAPALAPA"]
    },
    {
        "id": "SUJETO_ETICO",
        "title": "El Adolescente como Sujeto Ético y Político",
        "group": "salud",
        "color": "#2d6a4f",
        "badge": "Núcleo de la Salud",
        "pages": (104, 107),
        "links": ["SALUD_CHAPELA", "PS_EMANCIPATORIA", "PROYECTO_VIDA", "DERECHOS_SEXUALES"]
    },
    {
        "id": "PROYECTO_VIDA",
        "title": "Proyecto de Vida y Soberanía Corporal",
        "group": "salud",
        "color": "#2d6a4f",
        "badge": "Núcleo de la Salud",
        "pages": (7, 10),
        "links": ["SALUD_CHAPELA", "SUJETO_ETICO", "ITS_EPIDEMIOLOGIA", "DERECHOS_SEXUALES"]
    },

    # --- 2. EL PROBLEMA DE LAS ITS ---
    {
        "id": "ITS_EPIDEMIOLOGIA",
        "title": "Epidemiología de las ITS en México",
        "group": "its",
        "color": "#9d0208",
        "badge": "Problema de las ITS",
        "pages": (32, 36),
        "links": ["ITS_VPH", "ITS_VIH", "ITS_BACTERIANAS", "VULNERABILIDAD_BIO", "CONDON_MITOS"]
    },
    {
        "id": "ITS_VPH",
        "title": "Virus del Papiloma Humano (VPH) y Cáncer",
        "group": "its",
        "color": "#9d0208",
        "badge": "Problema de las ITS",
        "pages": (32, 34),
        "links": ["ITS_EPIDEMIOLOGIA", "VULNERABILIDAD_BIO", "AISLAMIENTO_ATENCION"]
    },
    {
        "id": "ITS_VIH",
        "title": "VIH y SIDA: Epidemia y Estigma",
        "group": "its",
        "color": "#9d0208",
        "badge": "Problema de las ITS",
        "pages": (33, 36),
        "links": ["ITS_EPIDEMIOLOGIA", "ESTIGMA_PENA", "AISLAMIENTO_ATENCION"]
    },
    {
        "id": "ITS_BACTERIANAS",
        "title": "ITS Bacterianas: Sífilis, Gonorrea y Clamidia",
        "group": "its",
        "color": "#9d0208",
        "badge": "Problema de las ITS",
        "pages": (32, 35),
        "links": ["ITS_EPIDEMIOLOGIA", "AISLAMIENTO_ATENCION", "MMH_MENENDEZ"]
    },
    {
        "id": "VULNERABILIDAD_BIO",
        "title": "Vulnerabilidad Biopsicosocial en la Adolescencia",
        "group": "its",
        "color": "#9d0208",
        "badge": "Problema de las ITS",
        "pages": (31, 34),
        "links": ["ITS_EPIDEMIOLOGIA", "TERRITORIO_IZTAPALAPA", "GENERO_PODER", "PSICOLOGIA_EVOLUTIVA"]
    },
    {
        "id": "CONDON_MITOS",
        "title": "Mitos y Resistencia al Uso del Condón",
        "group": "its",
        "color": "#9d0208",
        "badge": "Problema de las ITS",
        "pages": (184, 187),
        "links": ["ITS_EPIDEMIOLOGIA", "GENERO_PODER", "CONDONERIA_FOLLETOS", "ESI_EMANCIPATORIA"]
    },
    {
        "id": "ESTIGMA_PENA",
        "title": "Estigma Social, Culpa y Vergüenza",
        "group": "its",
        "color": "#9d0208",
        "badge": "Problema de las ITS",
        "pages": (189, 192),
        "links": ["ITS_EPIDEMIOLOGIA", "AISLAMIENTO_ATENCION", "TABU_FAMILIAR", "RELACION_MEDICO_PACIENTE"]
    },
    {
        "id": "AISLAMIENTO_ATENCION",
        "title": "Aislamiento y Retraso en la Atención Médica",
        "group": "its",
        "color": "#9d0208",
        "badge": "Problema de las ITS",
        "pages": (166, 172),
        "links": ["ITS_EPIDEMIOLOGIA", "ESTIGMA_PENA", "BARRERAS_CENTRO_SALUD", "EXIGENCIA_TUTOR"]
    },

    # --- 3. ENTORNO DE LA MEDICINA (MMH) ---
    {
        "id": "MMH_MENENDEZ",
        "title": "Modelo Médico Hegemónico (Eduardo Menéndez)",
        "group": "medicina",
        "color": "#0077b6",
        "badge": "Entorno Médico",
        "pages": (90, 95),
        "links": ["RELACION_MEDICO_PACIENTE", "BARRERAS_CENTRO_SALUD", "DESPACHO_PACIENTES", "EXIGENCIA_TUTOR"]
    },
    {
        "id": "RELACION_MEDICO_PACIENTE",
        "title": "Relación Médico-Paciente Vertical y Juicio Moral",
        "group": "medicina",
        "color": "#0077b6",
        "badge": "Entorno Médico",
        "pages": (191, 195),
        "links": ["MMH_MENENDEZ", "EXIGENCIA_TUTOR", "ESTIGMA_PENA", "NOM_005"]
    },
    {
        "id": "BARRERAS_CENTRO_SALUD",
        "title": "Barreras Institucionales en el C.S. Maximiliano Ruíz",
        "group": "medicina",
        "color": "#0077b6",
        "badge": "Entorno Médico",
        "pages": (169, 173),
        "links": ["MMH_MENENDEZ", "DESPACHO_PACIENTES", "AISLAMIENTO_ATENCION"]
    },
    {
        "id": "EXIGENCIA_TUTOR",
        "title": "Exigencia Arbitraria de Tutor Adulto",
        "group": "medicina",
        "color": "#0077b6",
        "badge": "Entorno Médico",
        "pages": (209, 212),
        "links": ["NOM_005", "RELACION_MEDICO_PACIENTE", "AISLAMIENTO_ATENCION", "DERECHOS_SEXUALES"]
    },
    {
        "id": "NOM_005",
        "title": "Violación a la Norma Oficial NOM-005-SSA2-1993",
        "group": "medicina",
        "color": "#0077b6",
        "badge": "Entorno Médico",
        "pages": (209, 212),
        "links": ["EXIGENCIA_TUTOR", "DERECHOS_SEXUALES", "MMH_MENENDEZ"]
    },
    {
        "id": "CONDONERIA_FOLLETOS",
        "title": "Condonería y Reparto Pasivo de Folletos",
        "group": "medicina",
        "color": "#0077b6",
        "badge": "Entorno Médico",
        "pages": (172, 176),
        "links": ["PS_INSTITUCIONAL", "CONDON_MITOS", "ESI_EMANCIPATORIA"]
    },
    {
        "id": "DESPACHO_PACIENTES",
        "title": "Burocracia de 'Despacho' y Contabilidad",
        "group": "medicina",
        "color": "#0077b6",
        "badge": "Entorno Médico",
        "pages": (191, 194),
        "links": ["MMH_MENENDEZ", "BARRERAS_CENTRO_SALUD", "RELACION_MEDICO_PACIENTE"]
    },

    # --- 4. ENTORNO DE LA CIENCIA Y PARADIGMAS ---
    {
        "id": "PARADIGMAS_CIENCIA",
        "title": "Tensión de Paradigmas Científicos",
        "group": "ciencia",
        "color": "#7b2cbf",
        "badge": "Entorno de la Ciencia",
        "pages": (11, 14),
        "links": ["POSITIVISMO_BIOMEDICO", "CUALITATIVO_SOCIO", "METODOLOGIA_MIXTA"]
    },
    {
        "id": "POSITIVISMO_BIOMEDICO",
        "title": "Paradigma Positivista Biomédico",
        "group": "ciencia",
        "color": "#7b2cbf",
        "badge": "Entorno de la Ciencia",
        "pages": (15, 18),
        "links": ["PARADIGMAS_CIENCIA", "MMH_MENENDEZ", "ITS_EPIDEMIOLOGIA"]
    },
    {
        "id": "CUALITATIVO_SOCIO",
        "title": "Paradigma Cualitativo y Socio-Crítico",
        "group": "ciencia",
        "color": "#7b2cbf",
        "badge": "Entorno de la Ciencia",
        "pages": (11, 14),
        "links": ["PARADIGMAS_CIENCIA", "METODOLOGIA_MIXTA", "PS_EMANCIPATORIA"]
    },
    {
        "id": "ANTROPOLOGIA_SOCIOLOGIA",
        "title": "Aporte de la Antropología y Sociología",
        "group": "ciencia",
        "color": "#7b2cbf",
        "badge": "Entorno de la Ciencia",
        "pages": (20, 25),
        "links": ["CONSTRUCCION_SOCIAL", "GENERO_PODER", "PSICOLOGIA_EVOLUTIVA"]
    },
    {
        "id": "PSICOLOGIA_EVOLUTIVA",
        "title": "Psicología Evolutiva: Duelos y Construcción del Yo",
        "group": "ciencia",
        "color": "#7b2cbf",
        "badge": "Entorno de la Ciencia",
        "pages": (23, 27),
        "links": ["VULNERABILIDAD_BIO", "CONSTRUCCION_SOCIAL", "ANTROPOLOGIA_SOCIOLOGIA"]
    },
    {
        "id": "METODOLOGIA_MIXTA",
        "title": "Metodología Mixta del Estudio en C.S. T-III",
        "group": "ciencia",
        "color": "#7b2cbf",
        "badge": "Entorno de la Ciencia",
        "pages": (130, 136),
        "links": ["PARADIGMAS_CIENCIA", "CUALITATIVO_SOCIO", "ESI_EMANCIPATORIA"]
    },

    # --- 5. ENTORNO SOCIAL Y TERRITORIAL ---
    {
        "id": "CONSTRUCCION_SOCIAL",
        "title": "La Adolescencia como Construcción Social",
        "group": "social",
        "color": "#a68a56",
        "badge": "Entorno Social",
        "pages": (20, 24),
        "links": ["TERRITORIO_IZTAPALAPA", "ANTROPOLOGIA_SOCIOLOGIA", "GENERO_PODER"]
    },
    {
        "id": "TERRITORIO_IZTAPALAPA",
        "title": "Territorio, Demografía y Marginación en Iztapalapa",
        "group": "social",
        "color": "#a68a56",
        "badge": "Entorno Social",
        "pages": (110, 116),
        "links": ["CONSTRUCCION_SOCIAL", "VULNERABILIDAD_BIO", "BARRERAS_CENTRO_SALUD"]
    },
    {
        "id": "GENERO_PODER",
        "title": "Desigualdad de Género y Asimetría Sexual",
        "group": "social",
        "color": "#a68a56",
        "badge": "Entorno Social",
        "pages": (202, 206),
        "links": ["ITS_EPIDEMIOLOGIA", "CONDON_MITOS", "DERECHOS_SEXUALES"]
    },
    {
        "id": "TABU_FAMILIAR",
        "title": "Tabúes Familiares y Represión Doméstica",
        "group": "social",
        "color": "#a68a56",
        "badge": "Entorno Social",
        "pages": (184, 187),
        "links": ["ESTIGMA_PENA", "CONSTRUCCION_SOCIAL", "ESI_EMANCIPATORIA"]
    },
    {
        "id": "DERECHOS_SEXUALES",
        "title": "Derechos Sexuales y Reproductivos de las Juventudes",
        "group": "social",
        "color": "#a68a56",
        "badge": "Entorno Social",
        "pages": (194, 198),
        "links": ["NOM_005", "SUJETO_ETICO", "ESI_EMANCIPATORIA"]
    },
    {
        "id": "ESI_EMANCIPATORIA",
        "title": "Propuesta: Educación Sexual Integral y Emancipatoria",
        "group": "social",
        "color": "#a68a56",
        "badge": "Entorno Social",
        "pages": (209, 216),
        "links": ["PS_EMANCIPATORIA", "DERECHOS_SEXUALES", "ITS_EPIDEMIOLOGIA"]
    }
]

# Load existing summary text from create_dense_html.py or compile it
from create_dense_html import verbatim_enrichment, category_meta

dense_nodes_final = []
links_final = []

print("Extracting 100% verbatim pages from PDF and pairing with summaries...")

for node in node_mappings:
    nid = node["id"]
    p_start, p_end = node["pages"]
    
    # 1. Extract literal raw text from PDF
    literal_transcription = extract_pdf_pages(p_start, p_end)
    
    # 2. Get summary from verbatim_enrichment or generate
    summary_text = ""
    # Find corresponding file in notes
    for k, v in verbatim_enrichment.items():
        if nid.lower() in k.lower() or node["title"][:15].lower() in k.lower():
            summary_text = v
            break
    if not summary_text:
        summary_text = f"<div class='summary-box'><h3>Resumen Analítico del Concepto</h3><p>Este nodo sintetiza el análisis de <strong>{node['title']}</strong> en el marco de la investigación de María Eugenia Ramírez Ibarra, vinculando la práctica en el Centro de Salud T-III Dr. Maximiliano Ruíz Castañeda con los enfoques de Promoción de la Salud y prevención de ITS.</p></div>"

    dense_nodes_final.append({
        "id": nid,
        "title": node["title"],
        "group": node["group"],
        "badge": node["badge"],
        "color": node["color"],
        "pages": f"Págs. {p_start}-{p_end}",
        "transcrito_html": literal_transcription,
        "resumen_html": summary_text,
        "links": node["links"]
    })

    for link_id in node["links"]:
        links_final.append({"source": nid, "target": link_id})

print(f"Processed {len(dense_nodes_final)} dual-mode nodes.")

# Now write the dual-mode HTML application
html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Red Conceptual Dual: Salud, ITS y Educación Sexual (UACM)</title>
    <style>
        :root {
            --bg-main: #0a0e17;
            --bg-card: #131b2e;
            --bg-panel: #182239;
            --border-color: rgba(255, 255, 255, 0.14);
            --primary: #38bdf8;
            --primary-rgb: 56, 189, 248;
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
            --accent-gold: #f59e0b;
            --font-size-base: 14px;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        body { background: var(--bg-main); color: var(--text-main); overflow: hidden; width: 100vw; height: 100vh; position: fixed; }

        /* HEADER SUPERIOR CON SWITCH GLOBAL */
        header {
            position: absolute; top: 0; left: 0; right: 0; height: 68px;
            background: rgba(10, 14, 23, 0.96); backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border-color);
            display: flex; align-items: center; justify-content: space-between; padding: 0 16px; z-index: 100;
        }
        .header-title-box { display: flex; flex-direction: column; }
        .header-title { font-size: 14px; font-weight: 800; color: var(--primary); letter-spacing: 0.3px; }
        .header-subtitle { font-size: 11px; font-weight: 400; color: var(--text-muted); }

        /* SELECTOR GLOBAL DE MODO (TODO EL SISTEMA) */
        .global-mode-switcher {
            display: flex; background: #0f172a; border: 1px solid #334155; border-radius: 20px; padding: 2px;
        }
        .global-mode-btn {
            padding: 5px 12px; border-radius: 18px; font-size: 11px; font-weight: 700; cursor: pointer;
            border: none; background: transparent; color: #94a3b8; transition: 0.25s;
        }
        .global-mode-btn.active {
            background: var(--primary); color: #0a0e17; box-shadow: 0 2px 8px rgba(56, 189, 248, 0.4);
        }

        .search-container { position: relative; }
        .search-input {
            background: var(--bg-card); border: 1px solid #334155; color: #fff;
            padding: 6px 10px 6px 28px; border-radius: 20px; font-size: 12px; width: 120px;
            transition: width 0.3s ease; outline: none;
        }
        .search-input:focus { width: 180px; border-color: var(--primary); }
        .search-icon { position: absolute; left: 9px; top: 7px; color: #64748b; font-size: 11px; }

        /* BARRA DE FILTROS */
        .filter-bar {
            position: absolute; top: 74px; left: 10px; right: 10px;
            display: flex; gap: 6px; overflow-x: auto; padding-bottom: 4px; z-index: 90;
            scrollbar-width: none;
        }
        .filter-bar::-webkit-scrollbar { display: none; }
        .pill {
            padding: 5px 12px; border-radius: 14px; font-size: 11px; font-weight: 600;
            cursor: pointer; border: 1px solid var(--border-color);
            background: var(--bg-card); color: #cbd5e1; white-space: nowrap; transition: 0.2s;
        }
        .pill.active { background: var(--primary); color: #0a0e17; border-color: var(--primary); font-weight: 700; }
        .pill.salud { border-color: #2d6a4f; color: #80ed99; }
        .pill.its { border-color: #9d0208; color: #ffccd5; }
        .pill.medicina { border-color: #0077b6; color: #90e0ef; }
        .pill.ciencia { border-color: #7b2cbf; color: #e0aaff; }
        .pill.social { border-color: #a68a56; color: #ede0d4; }

        /* CANVAS */
        #graphCanvas { width: 100%; height: 100%; display: block; touch-action: none; }

        /* CONTROLES FLOTANTES */
        .controls {
            position: absolute; bottom: 20px; right: 16px; display: flex; flex-direction: column; gap: 8px; z-index: 90;
        }
        .btn-ctrl {
            width: 40px; height: 40px; border-radius: 50%; background: var(--bg-panel); color: #f8fafc;
            border: 1px solid var(--border-color); font-size: 16px; display: flex; align-items: center; justify-content: center;
            cursor: pointer; box-shadow: 0 4px 14px rgba(0,0,0,0.5); user-select: none;
        }
        .btn-ctrl:active { transform: scale(0.92); }

        .toggle-links-btn {
            position: absolute; bottom: 20px; left: 16px; z-index: 90;
            background: var(--bg-panel); border: 1px solid var(--border-color); color: #cbd5e1;
            font-size: 11px; font-weight: 600; padding: 8px 14px; border-radius: 20px;
            cursor: pointer; display: flex; align-items: center; gap: 6px; box-shadow: 0 4px 14px rgba(0,0,0,0.5);
        }
        .toggle-links-btn.active { border-color: var(--primary); color: var(--primary); background: #0f2744; }

        /* DRAWER MODAL DE LECTURA DUAL */
        .drawer {
            position: absolute; bottom: 0; left: 0; right: 0; max-height: 88vh;
            background: var(--bg-panel); border-top: 3px solid var(--primary); border-radius: 22px 22px 0 0;
            padding: 20px 20px 30px; overflow-y: auto; transform: translateY(105%); transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 -10px 40px rgba(0,0,0,0.85); z-index: 200;
        }
        .drawer.open { transform: translateY(0); }

        .drawer-top-bar {
            display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;
            border-bottom: 1px solid var(--border-color); padding-bottom: 12px;
        }
        .drawer-meta { display: flex; flex-direction: column; gap: 4px; }
        .drawer-badge {
            display: inline-block; padding: 4px 10px; border-radius: 12px; font-size: 10px; font-weight: 700;
            text-transform: uppercase; width: fit-content;
        }
        .drawer-title { font-size: 18px; font-weight: 800; color: #fff; line-height: 1.3; }
        .drawer-source-pages { font-size: 11px; color: var(--accent-gold); font-weight: 600; }

        .drawer-actions { display: flex; align-items: center; gap: 8px; }
        .btn-font {
            background: #0f172a; border: 1px solid #334155; color: #cbd5e1; width: 30px; height: 30px;
            border-radius: 6px; font-size: 12px; font-weight: bold; cursor: pointer; display: flex; align-items: center; justify-content: center;
        }
        .drawer-close {
            background: #0f172a; border: 1px solid #334155; font-size: 22px; color: #94a3b8;
            cursor: pointer; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center;
        }

        /* TABS INDIVIDUALES DENTRO DEL NODO (TRANSCRITO VS RESUMEN) */
        .node-mode-tabs {
            display: flex; gap: 8px; margin: 12px 0 16px; background: #0a0e17; padding: 4px; border-radius: 12px;
            border: 1px solid var(--border-color);
        }
        .tab-btn {
            flex: 1; padding: 8px 12px; border-radius: 8px; border: none; font-size: 12px; font-weight: 700;
            cursor: pointer; background: transparent; color: #94a3b8; transition: 0.2s; display: flex; align-items: center; justify-content: center; gap: 6px;
        }
        .tab-btn.active {
            background: #1e293b; color: #fff; border: 1px solid var(--primary); box-shadow: 0 2px 6px rgba(0,0,0,0.4);
        }
        .tab-btn.active.transcrito { color: var(--accent-gold); border-color: var(--accent-gold); }
        .tab-btn.active.resumen { color: var(--primary); border-color: var(--primary); }

        /* CONTENIDO DE TEXTO */
        .drawer-content { font-size: var(--font-size-base); line-height: 1.75; color: #e2e8f0; }
        .drawer-content p { margin-bottom: 12px; text-align: justify; }
        .drawer-content h3 { font-size: 15px; color: var(--primary); margin: 18px 0 8px; font-weight: 700; }
        .drawer-content ul, .drawer-content ol { margin-left: 20px; margin-bottom: 14px; }
        .drawer-content li { margin-bottom: 6px; }

        .page-block {
            background: rgba(10, 14, 23, 0.6); border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 10px; padding: 14px; margin-bottom: 16px; position: relative;
        }
        .page-marker {
            display: inline-block; background: #1e293b; color: var(--accent-gold); font-size: 10px; font-weight: 700;
            padding: 3px 8px; border-radius: 6px; margin-bottom: 10px; text-transform: uppercase;
        }

        .quote {
            background: rgba(10, 14, 23, 0.85); border-left: 4px solid var(--primary);
            padding: 12px 16px; border-radius: 0 10px 10px 0; font-size: 13px; font-style: italic;
            color: #cbd5e1; margin: 16px 0;
        }

        /* SECCIÓN OCULTA DE NODOS RELACIONADOS */
        .related-toggle-container {
            margin-top: 24px; padding-top: 16px; border-top: 1px solid var(--border-color);
        }
        .btn-toggle-related {
            width: 100%; background: #0a0e17; border: 1px solid #334155; color: var(--primary);
            padding: 11px 16px; border-radius: 12px; font-size: 13px; font-weight: 600;
            display: flex; align-items: center; justify-content: space-between; cursor: pointer; transition: 0.2s;
        }
        .btn-toggle-related:hover { background: #131b2e; border-color: var(--primary); }

        .related-nodes-panel {
            display: none; margin-top: 12px; flex-wrap: wrap; gap: 8px;
            background: #0a0e17; padding: 14px; border-radius: 12px; border: 1px solid #334155;
        }
        .related-nodes-panel.visible { display: flex; }
        .rel-node-chip {
            padding: 6px 12px; background: var(--bg-card); border: 1px solid #475569; border-radius: 16px;
            font-size: 11px; font-weight: 500; color: #f1f5f9; cursor: pointer; transition: 0.2s;
            display: flex; align-items: center; gap: 6px;
        }
        .rel-node-chip:hover { border-color: var(--primary); color: var(--primary); transform: translateY(-1px); }
        .rel-node-dot { width: 8px; height: 8px; border-radius: 50%; display: inline-block; }
    </style>
</head>
<body>

    <header>
        <div class="header-title-box">
            <span class="header-title">Red Conceptual: Salud e ITS</span>
            <span class="header-subtitle">Tesis UACM (M. E. Ramírez Ibarra)</span>
        </div>

        <!-- SWITCH GLOBAL DE MODO PARA TODO EL MAPA -->
        <div class="global-mode-switcher">
            <button id="btnGlobalTranscrito" class="global-mode-btn active" onclick="setGlobalMode('transcrito')">
                📖 Transcrito (Literal)
            </button>
            <button id="btnGlobalResumen" class="global-mode-btn" onclick="setGlobalMode('resumen')">
                💡 Resumen
            </button>
        </div>

        <div class="search-container">
            <span class="search-icon">🔍</span>
            <input type="text" id="searchInput" class="search-input" placeholder="Buscar...">
        </div>
    </header>

    <div class="filter-bar">
        <div class="pill active" onclick="filterCategory('todos', this)">Todos (34)</div>
        <div class="pill salud" onclick="filterCategory('salud', this)">1. Núcleo Salud</div>
        <div class="pill its" onclick="filterCategory('its', this)">2. Problema ITS</div>
        <div class="pill medicina" onclick="filterCategory('medicina', this)">3. Medicina (MMH)</div>
        <div class="pill ciencia" onclick="filterCategory('ciencia', this)">4. Paradigmas Ciencia</div>
        <div class="pill social" onclick="filterCategory('social', this)">5. Social & Territorial</div>
    </div>

    <canvas id="graphCanvas"></canvas>

    <button id="btnToggleLinks" class="toggle-links-btn" onclick="toggleGlobalLinks()">
        <span id="linkIcon">🔗</span> <span id="linkText">Ocultar Todas las Líneas</span>
    </button>

    <div class="controls">
        <button class="btn-ctrl" onclick="zoomIn()" title="Acercar">+</button>
        <button class="btn-ctrl" onclick="zoomOut()" title="Alejar">−</button>
        <button class="btn-ctrl" onclick="resetView()" title="Centrar">🎯</button>
    </div>

    <!-- DRAWER DE TEXTO DENSO Y LECTURA CON SELECTOR DUAL -->
    <div id="detailDrawer" class="drawer">
        <div class="drawer-top-bar">
            <div class="drawer-meta">
                <span id="drawerBadge" class="drawer-badge"></span>
                <h2 id="drawerTitle" class="drawer-title"></h2>
                <span id="drawerPages" class="drawer-source-pages"></span>
            </div>
            <div class="drawer-actions">
                <button class="btn-font" onclick="changeFontSize(-1)">A−</button>
                <button class="btn-font" onclick="changeFontSize(1)">A+</button>
                <button class="drawer-close" onclick="closeDrawer()">×</button>
            </div>
        </div>

        <!-- SELECTOR LOCAL PARA ESTE NODO EN PARTICULAR -->
        <div class="node-mode-tabs">
            <button id="tabTranscrito" class="tab-btn transcrito active" onclick="setNodeMode('transcrito')">
                📖 Transcrito Literal (Palabra por palabra del PDF)
            </button>
            <button id="tabResumen" class="tab-btn resumen" onclick="setNodeMode('resumen')">
                💡 Resumen Analítico
            </button>
        </div>

        <div id="drawerBody" class="drawer-content"></div>

        <!-- SECCIÓN DE NODOS RELACIONADOS (OCULTA POR DEFECTO A MENOS QUE SE ABRA) -->
        <div class="related-toggle-container">
            <button id="btnToggleRelated" class="btn-toggle-related" onclick="toggleRelatedPanel()">
                <span id="relatedBtnText">🔗 Ver Nodos Relacionados (0)</span>
                <span id="relatedArrow">▼</span>
            </button>
            <div id="relatedNodesPanel" class="related-nodes-panel"></div>
        </div>
    </div>

    <script>
        const rawNodes = __NODES_JSON__;
        const rawLinks = __LINKS_JSON__;

        const canvas = document.getElementById("graphCanvas");
        const ctx = canvas.getContext("2d");

        let width, height;
        function resize() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        }
        window.addEventListener("resize", resize);
        resize();

        // Node lookup map
        const nodeMap = {};
        rawNodes.forEach((n, idx) => {
            const angle = (idx / rawNodes.length) * Math.PI * 2;
            const dist = 180 + Math.random() * 220;
            n.x = width/2 + Math.cos(angle) * dist;
            n.y = height/2 + Math.sin(angle) * dist;
            n.vx = 0; n.vy = 0;
            n.radius = 16;
            nodeMap[n.id] = n;
        });

        const links = rawLinks.map(l => ({
            source: nodeMap[l.source],
            target: nodeMap[l.target]
        })).filter(l => l.source && l.target);

        // State variables
        let zoom = 1.0;
        let panX = 0, panY = 0;
        let activeFilter = 'todos';
        let selectedNode = null;
        let showRelatedOnCanvas = false;
        let showAllGlobalLinks = true;
        let fontSizeBase = 14;

        // Global and local view mode: 'transcrito' or 'resumen'
        let currentMode = 'transcrito';

        let draggedNode = null;
        let isTouching = false;
        let startDist = 0;
        let lastTouchX = 0, lastTouchY = 0;

        function simulate() {
            // Repulsion
            for (let i = 0; i < rawNodes.length; i++) {
                for (let j = i + 1; j < rawNodes.length; j++) {
                    const a = rawNodes[i];
                    const b = rawNodes[j];
                    const dx = b.x - a.x;
                    const dy = b.y - a.y;
                    const dist = Math.sqrt(dx*dx + dy*dy) || 1;
                    if (dist < 280) {
                        const force = (280 - dist) / 280 * 0.7;
                        const fx = (dx / dist) * force;
                        const fy = (dy / dist) * force;
                        a.vx -= fx; a.vy -= fy;
                        b.vx += fx; b.vy += fy;
                    }
                }
            }

            // Spring attraction
            links.forEach(l => {
                const dx = l.target.x - l.source.x;
                const dy = l.target.y - l.source.y;
                const dist = Math.sqrt(dx*dx + dy*dy) || 1;
                const force = (dist - 130) * 0.006;
                const fx = (dx / dist) * force;
                const fy = (dy / dist) * force;
                l.source.vx += fx; l.source.vy += fy;
                l.target.vx -= fx; l.target.vy -= fy;
            });

            // Center gravity & dampening
            rawNodes.forEach(n => {
                if (n !== draggedNode) {
                    n.vx += (width/2 - n.x) * 0.0006;
                    n.vy += (height/2 - n.y) * 0.0006;
                    n.x += n.vx;
                    n.y += n.vy;
                    n.vx *= 0.86;
                    n.vy *= 0.86;
                }
            });
        }

        function draw() {
            ctx.clearRect(0, 0, width, height);
            ctx.save();
            ctx.translate(panX, panY);
            ctx.scale(zoom, zoom);

            const connectedNodeIds = new Set();
            if (selectedNode) {
                links.forEach(l => {
                    if (l.source === selectedNode) connectedNodeIds.add(l.target.id);
                    if (l.target === selectedNode) connectedNodeIds.add(l.source.id);
                });
            }

            // Draw Links
            links.forEach(l => {
                const isSelectedEdge = selectedNode && (l.source === selectedNode || l.target === selectedNode);
                
                if (!showAllGlobalLinks && !isSelectedEdge) return;

                if (selectedNode) {
                    if (isSelectedEdge && showRelatedOnCanvas) {
                        ctx.lineWidth = 2.4;
                        ctx.strokeStyle = "rgba(56, 189, 248, 0.9)";
                    } else if (isSelectedEdge && !showRelatedOnCanvas) {
                        ctx.lineWidth = 0.8;
                        ctx.strokeStyle = "rgba(56, 189, 248, 0.2)";
                    } else {
                        ctx.lineWidth = 0.4;
                        ctx.strokeStyle = "rgba(51, 65, 85, 0.05)";
                    }
                } else {
                    const matches = (activeFilter === 'todos' || l.source.group === activeFilter || l.target.group === activeFilter);
                    ctx.lineWidth = matches ? 1.0 : 0.4;
                    ctx.strokeStyle = matches ? "rgba(148, 163, 184, 0.2)" : "rgba(51, 65, 85, 0.04)";
                }

                ctx.beginPath();
                ctx.moveTo(l.source.x, l.source.y);
                ctx.lineTo(l.target.x, l.target.y);
                ctx.stroke();
            });

            // Draw Nodes
            rawNodes.forEach(n => {
                const matchesFilter = (activeFilter === 'todos' || n.group === activeFilter);
                const isSel = (selectedNode === n);
                const isConnected = selectedNode && connectedNodeIds.has(n.id);

                ctx.save();
                ctx.beginPath();

                let radius = n.radius;
                if (isSel) radius += 6;
                else if (isConnected && showRelatedOnCanvas) radius += 3;

                ctx.arc(n.x, n.y, radius, 0, Math.PI * 2);

                if (selectedNode) {
                    if (isSel) {
                        ctx.fillStyle = n.color;
                        ctx.lineWidth = 3.5;
                        ctx.strokeStyle = "#38bdf8";
                    } else if (isConnected && showRelatedOnCanvas) {
                        ctx.fillStyle = n.color;
                        ctx.lineWidth = 2.5;
                        ctx.strokeStyle = "#ffffff";
                    } else if (isConnected && !showRelatedOnCanvas) {
                        ctx.fillStyle = n.color;
                        ctx.lineWidth = 1.0;
                        ctx.strokeStyle = "rgba(255, 255, 255, 0.4)";
                    } else {
                        ctx.fillStyle = "rgba(24, 34, 57, 0.4)";
                        ctx.lineWidth = 0.8;
                        ctx.strokeStyle = "rgba(71, 85, 105, 0.25)";
                    }
                } else {
                    ctx.fillStyle = matchesFilter ? n.color : "#1e293b";
                    ctx.lineWidth = matchesFilter ? 1.6 : 0.8;
                    ctx.strokeStyle = matchesFilter ? "#ffffff" : "#475569";
                }

                ctx.fill();
                ctx.stroke();

                // Node text label
                const showLabel = (zoom > 0.65 || isSel || (isConnected && showRelatedOnCanvas));
                if (showLabel) {
                    ctx.font = isSel ? "bold 13px sans-serif" : (isConnected && showRelatedOnCanvas ? "600 12px sans-serif" : "11px sans-serif");
                    ctx.fillStyle = isSel ? "#38bdf8" : (selectedNode && !isConnected ? "rgba(100, 116, 139, 0.35)" : "#f8fafc");
                    ctx.textAlign = "center";
                    const displayTitle = n.title.length > 22 ? n.title.slice(0, 20) + "..." : n.title;
                    ctx.fillText(displayTitle, n.x, n.y + radius + 14);
                }

                ctx.restore();
            });

            ctx.restore();
            simulate();
            requestAnimationFrame(draw);
        }
        requestAnimationFrame(draw);

        // Position & coordinate helpers
        function getPos(e) {
            const rect = canvas.getBoundingClientRect();
            const clientX = e.touches ? e.touches[0].clientX : e.clientX;
            const clientY = e.touches ? e.touches[0].clientY : e.clientY;
            return {
                x: (clientX - rect.left - panX) / zoom,
                y: (clientY - rect.top - panY) / zoom,
                rawX: clientX,
                rawY: clientY
            };
        }

        function findNodeAt(x, y) {
            for (let i = rawNodes.length - 1; i >= 0; i--) {
                const n = rawNodes[i];
                const dx = n.x - x;
                const dy = n.y - y;
                if (Math.sqrt(dx*dx + dy*dy) <= n.radius + 10) return n;
            }
            return null;
        }

        // Mouse Handlers
        let isDragging = false;
        let lastMouseX = 0, lastMouseY = 0;

        canvas.addEventListener("mousedown", e => {
            const pos = getPos(e);
            const n = findNodeAt(pos.x, pos.y);
            if (n) {
                draggedNode = n;
                selectNode(n);
            } else {
                isDragging = true;
                lastMouseX = e.clientX;
                lastMouseY = e.clientY;
            }
        });

        window.addEventListener("mousemove", e => {
            if (draggedNode) {
                const pos = getPos(e);
                draggedNode.x = pos.x;
                draggedNode.y = pos.y;
            } else if (isDragging) {
                panX += (e.clientX - lastMouseX);
                panY += (e.clientY - lastMouseY);
                lastMouseX = e.clientX;
                lastMouseY = e.clientY;
            }
        });

        window.addEventListener("mouseup", () => {
            draggedNode = null;
            isDragging = false;
        });

        // Touch Handlers
        canvas.addEventListener("touchstart", e => {
            if (e.touches.length === 1) {
                const pos = getPos(e);
                const n = findNodeAt(pos.x, pos.y);
                if (n) {
                    draggedNode = n;
                    selectNode(n);
                } else {
                    isTouching = true;
                    lastTouchX = e.touches[0].clientX;
                    lastTouchY = e.touches[0].clientY;
                }
            } else if (e.touches.length === 2) {
                draggedNode = null;
                isTouching = false;
                const dx = e.touches[0].clientX - e.touches[1].clientX;
                const dy = e.touches[0].clientY - e.touches[1].clientY;
                startDist = Math.sqrt(dx*dx + dy*dy);
            }
        }, { passive: false });

        canvas.addEventListener("touchmove", e => {
            e.preventDefault();
            if (draggedNode && e.touches.length === 1) {
                const pos = getPos(e);
                draggedNode.x = pos.x;
                draggedNode.y = pos.y;
            } else if (isTouching && e.touches.length === 1) {
                panX += (e.touches[0].clientX - lastTouchX);
                panY += (e.touches[0].clientY - lastTouchY);
                lastTouchX = e.touches[0].clientX;
                lastTouchY = e.touches[0].clientY;
            } else if (e.touches.length === 2) {
                const dx = e.touches[0].clientX - e.touches[1].clientX;
                const dy = e.touches[0].clientY - e.touches[1].clientY;
                const dist = Math.sqrt(dx*dx + dy*dy);
                const factor = dist / startDist;
                zoom = Math.min(Math.max(0.3, zoom * factor), 2.5);
                startDist = dist;
            }
        }, { passive: false });

        canvas.addEventListener("touchend", () => {
            draggedNode = null;
            isTouching = false;
        });

        function zoomIn() { zoom = Math.min(2.5, zoom * 1.25); }
        function zoomOut() { zoom = Math.max(0.3, zoom * 0.8); }
        function resetView() { zoom = 1.0; panX = 0; panY = 0; }

        function filterCategory(cat, el) {
            activeFilter = cat;
            document.querySelectorAll(".pill").forEach(p => p.classList.remove("active"));
            el.classList.add("active");
        }

        function toggleGlobalLinks() {
            showAllGlobalLinks = !showAllGlobalLinks;
            const btn = document.getElementById("btnToggleLinks");
            const txt = document.getElementById("linkText");
            if (showAllGlobalLinks) {
                btn.classList.remove("active");
                txt.innerText = "Ocultar Todas las Líneas";
            } else {
                btn.classList.add("active");
                txt.innerText = "Mostrar Todas las Líneas";
            }
        }

        // GLOBAL MODE (APLICA A TODO EL SISTEMA)
        function setGlobalMode(mode) {
            currentMode = mode;
            document.getElementById("btnGlobalTranscrito").classList.toggle("active", mode === 'transcrito');
            document.getElementById("btnGlobalResumen").classList.toggle("active", mode === 'resumen');
            if (selectedNode) {
                renderNodeContent();
            }
        }

        // LOCAL MODE (APLICA AL NODO ACTUAL)
        function setNodeMode(mode) {
            currentMode = mode;
            renderNodeContent();
        }

        function renderNodeContent() {
            if (!selectedNode) return;
            const isTranscrito = (currentMode === 'transcrito');
            document.getElementById("tabTranscrito").classList.toggle("active", isTranscrito);
            document.getElementById("tabResumen").classList.toggle("active", !isTranscrito);

            const body = document.getElementById("drawerBody");
            if (isTranscrito) {
                body.innerHTML = selectedNode.transcrito_html;
            } else {
                body.innerHTML = selectedNode.resumen_html;
            }
        }

        // Selection & Dense Reading Drawer
        function selectNode(n) {
            selectedNode = n;
            showRelatedOnCanvas = false;

            const drawer = document.getElementById("detailDrawer");
            const badge = document.getElementById("drawerBadge");
            badge.innerText = n.badge || n.group.toUpperCase();
            badge.style.background = n.color;
            badge.style.color = "#fff";

            document.getElementById("drawerTitle").innerText = n.title;
            document.getElementById("drawerPages").innerText = `Extracción del libro: ${n.pages}`;

            renderNodeContent();

            // Prepare related nodes panel (HIDDEN BY DEFAULT)
            const panel = document.getElementById("relatedNodesPanel");
            panel.classList.remove("visible");
            panel.innerHTML = "";

            const connectedNodes = [];
            links.forEach(l => {
                if (l.source === n) connectedNodes.push(l.target);
                else if (l.target === n) connectedNodes.push(l.source);
            });

            document.getElementById("relatedBtnText").innerText = `🔗 Ver Nodos Relacionados (${connectedNodes.length})`;
            document.getElementById("relatedArrow").innerText = "▼";

            connectedNodes.forEach(target => {
                const chip = document.createElement("div");
                chip.className = "rel-node-chip";
                chip.innerHTML = `<span class="rel-node-dot" style="background:${target.color}"></span> ${target.title}`;
                chip.onclick = () => {
                    selectNode(target);
                    panToNode(target);
                };
                panel.appendChild(chip);
            });

            drawer.classList.add("open");
        }

        function toggleRelatedPanel() {
            const panel = document.getElementById("relatedNodesPanel");
            const isVisible = panel.classList.contains("visible");
            if (isVisible) {
                panel.classList.remove("visible");
                document.getElementById("relatedArrow").innerText = "▼";
                showRelatedOnCanvas = false;
            } else {
                panel.classList.add("visible");
                document.getElementById("relatedArrow").innerText = "▲";
                showRelatedOnCanvas = true;
            }
        }

        function closeDrawer() {
            document.getElementById("detailDrawer").classList.remove("open");
            selectedNode = null;
            showRelatedOnCanvas = false;
        }

        function panToNode(n) {
            panX = width/2 - n.x * zoom;
            panY = height/2 - n.y * zoom;
        }

        function changeFontSize(delta) {
            fontSizeBase = Math.min(22, Math.max(12, fontSizeBase + delta));
            document.documentElement.style.setProperty('--font-size-base', fontSizeBase + 'px');
        }

        // Live Search
        document.getElementById("searchInput").addEventListener("input", e => {
            const q = e.target.value.toLowerCase().trim();
            if (!q) return;
            const match = rawNodes.find(n => n.title.toLowerCase().includes(q) || n.transcrito_html.toLowerCase().includes(q) || n.resumen_html.toLowerCase().includes(q));
            if (match) {
                selectNode(match);
                panToNode(match);
            }
        });
    </script>
</body>
</html>
"""

html_final = html_content.replace("__NODES_JSON__", json.dumps(dense_nodes_final, ensure_ascii=False)).replace("__LINKS_JSON__", json.dumps(links_final, ensure_ascii=False))

with open("Grafo_Interactivo_Salud_ITS.html", "w", encoding="utf-8") as f:
    f.write(html_final)

print("Dual-mode HTML app successfully written to Grafo_Interactivo_Salud_ITS.html!")
