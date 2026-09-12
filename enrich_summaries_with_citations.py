import json
import re

# Dictionary of hyper-rich analytical summaries with citations for all 34 nodes
rich_summaries = {
    "SALUD_CHAPELA": """<div class="summary-card">
<h3>1. Concepto y Marco Teórico Central</h3>
<p>La investigación fundamenta su marco ontológico en la propuesta heterodoxa de la pedagoga e investigadora mexicana <strong>Luz María Chapela (2007)</strong>, rompiendo con el enfoque biomédico positivista que reduce la salud a una simple ausencia de enfermedad o a un estado pasivo:</p>
<blockquote class="quote">«La salud es la capacidad corporeizada de inventar futuros viables y alcanzables, permitiendo a los seres humanos considerarse como sujetos éticos capaces de construir conocimiento independientemente de los expertos o de las instituciones y, con base en ese conocimiento, dar significado, valor y sentido a su mundo y práctica» (Ramírez Ibarra, 2011, p. 2, 96).</blockquote>

<h3>2. Las 6 Capacidades Humanas Constitutivas</h3>
<p>Chapela plantea que la salud no se concibe fuera del cuerpo vivo y sintiente, en el cual se articulan seis capacidades humanas indisociables (p. 96-97):</p>
<ul>
  <li><strong>Capacidad de Razonamiento (Homo Sapiens):</strong> Discernir críticamente entre el autocuidado y el riesgo sin tutela ciega.</li>
  <li><strong>Capacidad de Imaginar y Jugar (Homo Ludens):</strong> Idear horizontes viables y proyectar alternativas frente a la adversidad.</li>
  <li><strong>Dimensión Erótica (Pulsión Afectiva):</strong> El placer, el deseo, la ternura y la afectividad como motores existenciales.</li>
  <li><strong>Capacidad de Trabajo (Homo Faber):</strong> Transformar el entorno material mediante la acción comunitaria.</li>
  <li><strong>Capacidad Política:</strong> Deliberar, disentir y ejercer soberanía sobre el propio cuerpo y destino.</li>
  <li><strong>Capacidad Económica:</strong> Movilizar capitales materiales y simbólicos (Pierre Bourdieu) para alcanzar los proyectos trazados.</li>
</ul>

<h3>3. Aplicación Crítica y Bioética en el Centro de Salud</h3>
<p>La autora demuestra que cuando el médico del Centro de Salud T-III regaña a los jóvenes o les exige tutores para darles condones, <strong>anula su capacidad política y erótica</strong>, dejándolos desamparados frente al VPH y al VIH al arrebatarles su condición de sujetos con agencia.</p>
</div>""",

    "OTTAWA_1986": """<div class="summary-card">
<h3>1. Marco Internacional y Declaración de Principios</h3>
<p>La tesis analiza las aportaciones de la <em>Primera Conferencia Internacional sobre la Promoción de la Salud</em> celebrada en Ottawa, Canadá (noviembre de 1986):</p>
<blockquote class="quote">«La promoción de la salud consiste en proporcionar a los pueblos los medios necesarios para mejorar su salud y ejercer un mayor control sobre la misma. Para alcanzar un estado adecuado de bienestar físico, mental y social, un individuo o grupo debe ser capaz de identificar y realizar sus aspiraciones, de satisfacer sus necesidades y de cambiar o adaptarse al medio ambiente» (Carta de Ottawa, citada en p. 80-81).</blockquote>

<h3>2. Los 7 Prerrequisitos Estructurales Indispensables (p. 81)</h3>
<p>La investigación resalta que la salud es inconcebible si el Estado no garantiza las condiciones materiales básicas:</p>
<ul>
  <li><strong>La Paz:</strong> Ausencia de violencia armada, policial o comunitaria.</li>
  <li><strong>La Educación:</strong> Formación crítica, laica y con equidad de género.</li>
  <li><strong>La Vivienda:</strong> Espacios habitacionales dignos con servicios urbanos.</li>
  <li><strong>La Alimentación:</strong> Seguridad nutricional para el desarrollo biológico.</li>
  <li><strong>La Renta / Ingreso:</strong> Salarios justos que erradiquen la precariedad extrema.</li>
  <li><strong>Un Ecosistema Estable:</strong> Sustentabilidad ambiental y agua potable.</li>
  <li><strong>La Justicia Social y la Equidad:</strong> Distribución justa de la riqueza y los servicios.</li>
</ul>

<h3>3. Contraste Crítico con la Realidad de Iztapalapa</h3>
<blockquote class="quote">«Cualquier mejora en la salud ha de basarse necesariamente en estos prerrequisitos fundamentales... Si no se garantizan la equidad y la justicia social, los programas de salud se reducen a dádivas asistenciales» (p. 81).</blockquote>
<p>En Iztapalapa, donde el 71% de los adolescentes depende económicamente de sus familias y el hacinamiento es severo, el discurso oficial de Ottawa queda convertido en mera retórica vacía.</p>
</div>""",

    "PS_EMANCIPATORIA": """<div class="summary-card">
<h3>1. El Paradigma Crítico de la UACM</h3>
<p>Frente a la medicina vertical tradicional, la autora defiende el enfoque pedagógico y epistemológico impulsado en la Licenciatura en Promoción de la Salud de la UACM:</p>
<blockquote class="quote">«La propuesta emancipatoria busca incorporar a la promoción de la salud el paradigma comprensivo... recuperando aportaciones de la sociología de la cultura, la educación popular de Paulo Freire y la bioética ciudadana. Su teoría destaca por considerar a los seres humanos como sujetos éticos capaces de construir conocimiento propio independientemente de los expertos o instituciones» (p. 2-4, 93).</blockquote>

<h3>2. Principios de Transformación Pedagógica</h3>
<ul>
  <li><strong>Superación de la Educación Bancaria:</strong> Rechaza que el médico deba 'depositar' órdenes técnicas en un paciente pasivo. Se privilegia la pedagogía de la pregunta y el diálogo de saberes.</li>
  <li><strong>Desmedicalización de la Sexualidad:</strong> La vida sexual no es un mero asunto bacteriológico o de control de natalidad; comprende afectividad, placer, derechos y vínculos éticos.</li>
  <li><strong>Construcción de Ciudadanía Sanitaria:</strong> Dotar a los adolescentes de herramientas cognitivas y jurídicas para exigir servicios cálidos y confidenciales (NOM-005).</li>
</ul>

<h3>3. Conclusión de la Investigación</h3>
<blockquote class="quote">«Considero que mediante prácticas de promoción de la salud emancipatoria se pueden revertir los problemas planteados inicialmente al permitir a los sujetos su autoconstrucción y la defensa de sus derechos en la atención de la salud» (Ramírez Ibarra, Conclusiones p. 201-202).</blockquote>
</div>""",

    "PS_INSTITUCIONAL": """<div class="summary-card">
<h3>1. Diagnóstico de la Práctica Institucional Real</h3>
<p>La autora, laboratorista y promotora en los centros de salud del D.F., realiza una disección crítica del quehacer cotidiano en el Centro de Salud T-III:</p>
<blockquote class="quote">«La educación sexual en el centro de salud se concentra en la entrega de material gráfico, condonería, campañas de higiene, control médico y pláticas informativas, todo con un enfoque de prescribir y controlar comportamientos y prácticas sexuales de los adolescentes... a estas acciones se les llama formalmente 'promoción de la salud', pero no reflejan un impacto positivo en su aprendizaje» (p. 182).</blockquote>

<h3>2. Los Tres Vicios de la Promoción Burocrática</h3>
<ul>
  <li><strong>La 'Condonería' como Trámite:</strong> Repartir preservativos para justificar metas estadísticas, sin capacitar en su colocación correcta, caducidad o negociación coital.</li>
  <li><strong>Saturación de Folletos (41% del material):</strong> El 23% de los adolescentes confiesa que jamás los lee y un 26% indica que nadie se los explicó.</li>
  <li><strong>Vigilancia Normatizadora:</strong> La institución asume un rol de policía moral que sanciona a las y los jóvenes que solicitan anticonceptivos.</li>
</ul>

<h3>3. Evidencia Empírica de la Desconexión</h3>
<blockquote class="quote">«Al indagar sobre si piden información en materia de educación sexual, los resultados muestran un 73% de adolescentes que NO piden información contra un escaso 27% que sí lo hace» (p. 158).</blockquote>
</div>""",

    "ESTILOS_VIDA": """<div class="summary-card">
<h3>1. La Cooptación Neoliberal del Concepto (Lalonde, 1974)</h3>
<p>En el Capítulo 3.3, la autora desenmascara cómo el campo biomédico distorsionó el concepto de estilos de vida:</p>
<blockquote class="quote">«El campo biomédico se apropió del concepto estilos de vida... convirtiéndolo en un objeto de consumo y culpabilizando a quienes no los adoptan. Las prácticas de promoción desde esta visión impulsan medidas para cambiar hábitos individuales (fumar, comer, beber), omitiendo que si el contexto socio-territorial es precario, la salud seguirá deteriorada» (p. 89-91).</blockquote>

<h3>2. Patógenos e Inmunógenos Conductuales (Matarazzo, 1984)</h3>
<ul>
  <li><strong>Patógenos conductuales:</strong> Comportamientos individuales clasificados como de riesgo (inicio sexual temprano, no usar condón, consumo de alcohol).</li>
  <li><strong>Inmunógenos conductuales:</strong> Conductas protectoras prescritas (abstinencia, uso regular del preservativo, visitas médicas).</li>
</ul>

<h3>3. La Culpabilización del Adolescente como Coartada Estatal</h3>
<blockquote class="quote">«Si un individuo adopta conductas saludables, pero su ambiente o contexto no es propicio, de poco le servirá su buena disposición, pues esto no le garantiza una salud favorable» (p. 91).</blockquote>
<p>Exigir 'conductas responsables' en colonias con desabasto de agua, deserción escolar y violencia territorial exime al Estado de su responsabilidad estructural.</p>
</div>""",

    "SUJETO_ETICO": """<div class="summary-card">
<h3>1. Desmontando el Estigma de la 'Inmadurez'</h3>
<p>La tesis denuncia el adultocentrismo que etiqueta al joven como un ser incompleto y peligroso:</p>
<blockquote class="quote">«A los y las adolescentes se les asigna o etiqueta con un rol de rebeldes, inmaduros e irresponsables... tanto es la repetición de este mensaje que el adolescente lo adopta. Sin embargo, desde la promoción heterodoxática se considera a los seres humanos como sujetos éticos capaces de construir conocimiento y dar sentido a su mundo» (p. 2, 15).</blockquote>

<h3>2. Pilares de la Condición Ética Juvenil</h3>
<ul>
  <li><strong>Autonomía y Consentimiento:</strong> Derecho a decir cuándo, cómo y con quién ejercer su sexualidad libre de coacción.</li>
  <li><strong>Capacidad Deliberativa:</strong> Poder interpelar al médico, elegir métodos anticonceptivos y recibir información científica veraz.</li>
  <li><strong>Ética del Cuidado Compartido:</strong> El uso del condón concebido no como una obligación impuesta, sino como un pacto de cuidado recíproco.</li>
</ul>

<h3>3. La Violación de la Condición de Sujeto en Consulta</h3>
<p>En el C.S. Maximiliano Ruíz, el <strong>58% de las adolescentes encuestadas reveló que fue el médico quien decidió e impuso su método anticonceptivo</strong>, despojándolas de su derecho al consentimiento informado.</p>
</div>""",

    "PROYECTO_VIDA": """<div class="summary-card">
<h3>1. La Salud como Condición y no como Fin</h3>
<p>La autora recupera la sociología francesa para articular la prevención con el horizonte de futuro:</p>
<blockquote class="quote">«Para los y las adolescentes preservar su salud es una condición y no una finalidad de la existencia. Insistiendo en ese punto, Hugues Lagrange escribe: 'sostenemos para los jóvenes una noción de riesgos que mezclan placeres y peligros, asociándolos no a las prácticas tomadas de manera aislada, sino a comportamientos, a conjuntos de actos no aislados'» (p. 29).</blockquote>

<h3>2. El Impacto Devastador de las ITS y el Embarazo No Planeado</h3>
<ul>
  <li><strong>366,000 embarazos no deseados anuales en México:</strong> Conducen a la deserción escolar masiva y a la reproducción de la pobreza en Iztapalapa.</li>
  <li><strong>VPH y Lesiones Precancerígenas:</strong> Amenaza a largo plazo que trunca la vida productiva de las mujeres jóvenes si no hay citología oportuna.</li>
</ul>
<blockquote class="quote">«La educación sexual integral impulsa las capacidades humanas en los y las adolescentes y permite una construcción de proyecto desde su propia experiencia» (p. 3).</blockquote>
</div>""",

    "ITS_EPIDEMIOLOGIA": """<div class="summary-card">
<h3>1. Magnitud Epidemiológica Alarmante (Capítulo 1.4)</h3>
<blockquote class="quote">«En muchos países del mundo las Infecciones de Transmisión Sexual (ITS) amenazan la salud y la vida... aproximadamente 685 mil personas se contagian con una de estas enfermedades cada día en el planeta. En México se presentan anualmente SIETE MILLONES de casos nuevos de Infecciones de Transmisión Sexual (ITS), impactando con gran fuerza en la juventud» (p. 25, 27).</blockquote>

<h3>2. Factores de la Crisis en Jóvenes Mexicanos</h3>
<ul>
  <li><strong>Edad Temprana de Inicio Sexual:</strong> 14.5 años en varones y 15.5 años en mujeres en el Distrito Federal (2008), habitualmente sin preservativo.</li>
  <li><strong>Más de 30 Patógenos:</strong> Virus (VIH, VPH, Herpes 2), bacterias (Treponema pallidum, Neisseria gonorrhoeae, Chlamydia), hongos y protozoarios.</li>
  <li><strong>La Trampa de la 'Monogamia Aparente':</strong> La creencia errónea de que un noviazgo formal protege de infecciones previas asintomáticas.</li>
</ul>

<h3>3. El Aborto y la Maternidad en Cifras</h3>
<blockquote class="quote">«En México se estiman 20 millones de partos al año, de los cuales alrededor de 500 mil corresponden a mujeres de entre 15 y 19 años... Los abortos se presentan 14 veces más en embarazadas adolescentes que en mayores de 20 años» (p. 30).</blockquote>
</div>""",

    "ITS_VPH": """<div class="summary-card">
<h3>1. Prevalencia y Peligro Oncogénico</h3>
<blockquote class="quote">«El Virus del Papiloma Humano (VPH) es una de las infecciones de mayor prevalencia en la adolescencia y se ha transformado en un grave problema dada su rápida propagación y su vinculación directa con el cáncer cérvico-uterino» (p. 24-25).</blockquote>

<h3>2. Vulnerabilidad Tisular y Clínica</h3>
<ul>
  <li><strong>Ectopia Fisiológica Cervical:</strong> La zona de transformación del cuello uterino en menores de 20 años es celularmente inmadura y muy vulnerable a cepas oncogénicas 16 y 18.</li>
  <li><strong>Curso Silencioso:</strong> Más del 80% de los contagios no presentan verrugas visibles ni dolor inicial.</li>
  <li><strong>Desconocimiento Generalizado:</strong> Los cuestionarios demostraron que los adolescentes ubican el SIDA, pero desconocen por completo qué es el VPH y el Papanicolaou.</li>
</ul>
</div>""",

    "ITS_VIH": """<div class="summary-card">
<h3>1. Vía de Transmisión Dominante</h3>
<blockquote class="quote">«En México, la epidemia del SIDA es principalmente por transmisión sexual, toda vez que representa el 90% de los casos... El SIDA es una enfermedad infecciosa causada por un virus denominado Virus de Inmunodeficiencia Humana (VIH)... dada la rapidez de su propagación y la fatal evolución en caso de no tratarse, es indispensable cortar la cadena de transmisión mediante el diagnóstico temprano» (p. 25-26).</blockquote>

<h3>2. Barreras Psicosociales</h3>
<ul>
  <li><strong>Sensación de Invulnerabilidad:</strong> 'Eso sólo le pasa a gente promiscua o drogadicta'.</li>
  <li><strong>Estigma Mortal:</strong> El miedo al rechazo familiar impide que los jóvenes soliciten pruebas rápidas serológicas.</li>
  <li><strong>Burocracia Intimidatoria:</strong> En el Centro de Salud T-III no hay módulos confidenciales cálidos para pruebas de VIH dirigidas a jóvenes.</li>
</ul>
</div>""",

    "ITS_BACTERIANAS": """<div class="summary-card">
<h3>1. Sífilis, Gonorrea y Clamidia en Jóvenes</h3>
<blockquote class="quote">«Tradicionalmente llamadas enfermedades venéreas, la gonorrea y la sífilis siguen registrando tasas elevadas en los adolescentes. Su falta de detección temprana y tratamiento adecuado provoca consecuencias irreversibles como la esterilidad y la enfermedad pélvica inflamatoria» (p. 26).</blockquote>

<h3>2. Secuelas Fisiopatológicas</h3>
<ul>
  <li><strong>Enfermedad Pélvica Inflamatoria (EPI):</strong> Gonococo y clamidia ascienden por el tracto femenino causando salpingitis y obstrucción tubaria bilateral irreversible.</li>
  <li><strong>El Engaño del Chancro Sifilítico:</strong> La úlcera genital primaria es indolora y cicatriza espontáneamente, haciendo creer al joven que sanó mientras la bacteria invade órganos vitales.</li>
  <li><strong>Automedicación:</strong> Por vergüenza de mostrar sus genitales al médico, recurren a remedios caseros o antibióticos mal recetados.</li>
</ul>
</div>""",

    "VULNERABILIDAD_BIO": """<div class="summary-card">
<h3>1. La Confluencia Biopsicosocial del Riesgo</h3>
<blockquote class="quote">«Las tasas desproporcionadamente elevadas en las ITS y los embarazos no deseados no se determinan únicamente a partir de problemas emocionales individuales, sino que involucran aspectos biológicos, sociales y culturales indisociables» (p. 24).</blockquote>

<h3>2. Tres Ejes de Vulnerabilidad</h3>
<ul>
  <li><strong>Biológico:</strong> Mucosa genital en desarrollo, mayor absorción tisular y susceptibilidad a microtraumas.</li>
  <li><strong>Psicológico:</strong> Labilidad emocional, búsqueda de identidad y presión del grupo de pares (Aberastury, 1992).</li>
  <li><strong>Económico y Territorial:</strong> El 71% de los adolescentes encuestados depende totalmente del dinero de sus padres en Iztapalapa, lo que coarta su acceso a insumos de salud privados.</li>
</ul>
</div>""",

    "CONDON_MITOS": """<div class="summary-card">
<h3>1. Resistencias Identificadas en los Talleres de Reflexión</h3>
<blockquote class="quote">«Ambos equipos de adolescentes coincidieron en tener información sobre sexualidad y valores, cuidarse de las enfermedades... sin embargo, los mitos sobre el condón siguen vigentes: que resta sensibilidad o placer, que se rompe fácil, o que proponerlo denota desconfianza o infidelidad hacia la pareja... si el varón se niega al condón, la mujer suele ceder para no perder la relación afectiva» (p. 176, 195).</blockquote>

<h3>2. Mitos Patriarcales Clave en Iztapalapa</h3>
<ul>
  <li><em>«Le quita la pasión al momento»:</em> Creencia de que planificar el cuidado rompe el romanticismo.</li>
  <li><em>«Si una mujer trae condones en la bolsa es porque es fácil»:</em> Sanción moral machista hacia la mujer precavida.</li>
  <li><em>«Si le pido condón a mi novio va a pensar que ando con otro»:</em> Chantaje emocional que anula la protección.</li>
</ul>
</div>""",

    "ESTIGMA_PENA": """<div class="summary-card">
<h3>1. El Control Panóptico en la Colonia</h3>
<blockquote class="quote">«Apenas empecé a venir porque antes me daba pena... en la colonia creen que si vas al centro de salud es porque vienes embarazada o con alguna enfermedad de transmisión sexual, así que prefieres aguantarte antes de que te vean entrar» (Adolescente entrevistada, p. 182).</blockquote>

<h3>2. Factores del Silencio</h3>
<ul>
  <li><strong>Vigilancia Vecinal:</strong> En Iztapalapa, ingresar al consultorio de planificación es objeto de chismes y rumores vecinales.</li>
  <li><strong>Vergüenza en Mostradores:</strong> Farmacias y ventanillas hospitalarias donde se atiende con miradas de reproche a los jóvenes.</li>
  <li><strong>Retraso Diagnóstico:</strong> Ocultar lesiones por meses hasta que el dolor o la inflamación se vuelven insoportables.</li>
</ul>
</div>""",

    "AISLAMIENTO_ATENCION": """<div class="summary-card">
<h3>1. Estadísticas Contundentes de la Encuesta (N=60, Capítulo 6)</h3>
<blockquote class="quote">«Al indagar sobre si solicitan información en materia de educación sexual, los resultados muestran un 73% de adolescentes que NO piden información contra un escaso 27% que sí lo hace... Además, el 70% no cuenta con ningún control médico regular en el centro» (p. 158-160).</blockquote>

<h3>2. Desamparo Institucional en Cifras</h3>
<ul>
  <li><strong>73%</strong> de adolescentes jamás pregunta sobre sexualidad ni ITS al médico.</li>
  <li><strong>70%</strong> carece de expediente o control médico regular (sólo acuden por vacunas o certificados escolares).</li>
  <li><strong>49%</strong> acude forzosamente acompañado de sus padres por exigencia médica, cancelando la privacidad.</li>
  <li><strong>48%</strong> espera entre 31 y 60 minutos, y un <strong>27% espera de 1 a 2 horas</strong> para ser atendido.</li>
</ul>
</div>""",

    "MMH_MENENDEZ": """<div class="summary-card">
<h3>1. La Definición Clásica de Eduardo Menéndez</h3>
<blockquote class="quote">«El Modelo Médico Hegemónico (MMH) se define como el conjunto de prácticas, saberes y teorías generadas por el desarrollo de lo que se conoce como medicina científica, el cual desde fines del siglo XVIII ha ido logrando dejar como subalternos al conjunto de prácticas, saberes e ideologías que dominaban en los conjuntos sociales... caracterizado por el biologicismo, la concepción ahistórica, el individualismo, la eficacia pragmática y la relación asimétrica y de dominación médico-paciente... donde el objeto de transformación será la enfermedad y no la salud» (p. 82-84).</blockquote>

<h3>2. Las Cuatro Funciones Estructurales del MMH</h3>
<ul>
  <li><strong>Curativa-Preventiva Aparente:</strong> La única legitimada socialmente, pero subordinada al fármaco.</li>
  <li><strong>Normatizadora:</strong> Establece qué conductas sexuales son 'decentes' o 'desviadas'.</li>
  <li><strong>Control Social:</strong> Vigilancia epidemiológica jerarquizada sobre cuerpos subordinados.</li>
  <li><strong>Reproducción Ideológica:</strong> Mantiene la superioridad del experto sobre el saber popular.</li>
</ul>
</div>""",

    "RELACION_MEDICO_PACIENTE": """<div class="summary-card">
<h3>1. El Trato de Regaño y Descalificación en Consulta</h3>
<blockquote class="quote">«La actitud del personal médico y de enfermería muchas veces es impositiva, indiferente o de regaño. Los adolescentes señalaron sentirse juzgados con frases como 'son muy jóvenes para aquello'... Una adolescente expresó: 'Me regañó el doctor la otra vez pero según él estuvo bien. Porque dice que si andamos de novios nos va a ir mal'» (p. 183-184).</blockquote>

<h3>2. Demandas Reales de los Jóvenes</h3>
<blockquote class="quote">«Los adolescentes demandaron de forma unánime: 'Que los médicos sean más amables, que brindaran confianza, que no nos regañen ni nos juzguen y que expliquen sin palabras difíciles'» (p. 182-183).</blockquote>
<p>El autoritarismo destruye el puente de confianza indispensable para que un joven revele conductas de riesgo de ITS.</p>
</div>""",

    "BARRERAS_CENTRO_SALUD": """<div class="summary-card">
<h3>1. Condiciones Físicas del C.S. Maximiliano Ruíz Castañeda</h3>
<blockquote class="quote">«El 48% de los adolescentes han esperado de 31 a 60 minutos para ser atendidos, mientras que el 27% ha tardado de una a dos horas, y un 5% más de dos horas... Asimismo, el 70% acude exclusivamente por trámites forzosos como certificados médicos y vacunas escolares» (p. 162).</blockquote>

<h3>2. Obstáculos Detectados</h3>
<ul>
  <li><strong>Horarios Matutinos Incompatibles:</strong> Los módulos de salud reproductiva operan en horarios escolares, excluyendo a estudiantes.</li>
  <li><strong>Cero Confidencialidad:</strong> Personal de intendencia, enfermería y otros pacientes entran y salen de los consultorios sin tocar la puerta durante la consulta.</li>
  <li><strong>Falta de Servicios Amigables:</strong> Carencia de un espacio exclusivo para jóvenes en el centro de salud.</li>
</ul>
</div>""",

    "EXIGENCIA_TUTOR": """<div class="summary-card">
<h3>1. La Práctica Ilegal de Condicionar la Consulta</h3>
<blockquote class="quote">«En primer lugar, algunos médicos no atienden a los y las adolescentes si éstos no van acompañados por un familiar o adulto que se haga responsable de ella o él, argumentando que es por seguridad personal, sintiéndose más confiados que otro adulto asuma la responsabilidad del adolescente. Esto viola su derecho de atención de acuerdo con la Norma Oficial Mexicana NOM-005-SSA2-1993» (Conclusiones, p. 201).</blockquote>

<h3>2. Consecuencias Destructivas</h3>
<ul>
  <li><strong>Miedo al Castigo Familiar:</strong> Ninguna joven pedirá condones ni tratamiento de ITS si tiene a su madre o padre al lado en el consultorio.</li>
  <li><strong>Expulsión de los más Vulnerables:</strong> Jóvenes huérfanos, expulsados de sus casas o en situación de calle quedan desamparados.</li>
  <li><strong>Proliferación de Cadenas de Contagio:</strong> El adolescente no tratado transmite la infección a sus parejas.</li>
</ul>
</div>""",

    "NOM_005": """<div class="summary-card">
<h3>1. El Sustento Jurídico Federal Violado en la Institución</h3>
<blockquote class="quote">«La Norma Oficial Mexicana de los Servicios de Planificación Familiar (NOM-005-SSA2-1993, publicada en su versión actualizada en el DOF el 21 de enero de 2004) establece que la planificación familiar es un derecho de toda persona, independientemente de su género, edad y estado social o legal. Señala que la consejería debe dar PARTICULAR ATENCIÓN a la población adolescente con absoluto respeto al derecho a decidir sobre su conducta sexual y al consentimiento informado» (p. 201).</blockquote>

<h3>2. Numeral 4.1.1 de la Norma:</h3>
<blockquote class="quote">«'Los servicios de planificación familiar deberán proporcionar información, orientación, consejería, selección, prescripción, contraindicaciones y aplicación de métodos de control de la fertilidad... prevención de infecciones de transmisión sexual... La prestación de los servicios deberá de otorgarse de una manera integral con calidad y calidez a toda la población'» (p. 201-202).</blockquote>
<p>La investigación califica la exigencia de tutor como un acto ilegal y una transgresión de derechos humanos.</p>
</div>""",

    "CONDONERIA_FOLLETOS": """<div class="summary-card">
<h3>1. El Espejismo de la Folletería Impresa</h3>
<blockquote class="quote">«El 41% de la información son folletos y trípticos, seguido de pláticas con 25%... sin embargo, el 23% de los adolescentes refiere que nunca lee el material impreso, el 26% afirma que no se lo explicaron y sólo al 12% le resolvió dudas... A estas acciones se les llama 'promoción de la salud', la condonería y entrega de pulseras alusivas, pero no reflejan ningún impacto positivo en el aprendizaje de los adolescentes» (p. 164-165, 182).</blockquote>

<h3>2. Razones de su Fracaso</h3>
<ul>
  <li><strong>Lenguaje Técnico Frío:</strong> Esquemas anatómicos que no responden a las dudas afectivas reales de los jóvenes.</li>
  <li><strong>Sustituto de la Escucha:</strong> El médico entrega el papel y despacha al paciente en tres minutos.</li>
  <li><strong>Desperdicio de Recursos:</strong> Folletos arrojados a la basura sin generar conciencia ni cambio de conducta.</li>
</ul>
</div>""",

    "DESPACHO_PACIENTES": """<div class="summary-card">
<h3>1. La Confesión del Personal Médico</h3>
<blockquote class="quote">«En el caso de la atención médica el personal refiere estar inmerso en sus tareas burocráticas de 'despachar' y contabilizar pacientes. Un médico señala al respecto: 'Nosotros tenemos que despachar y contabilizar pacientes... si al chavo le interesa saber más sobre sexualidad o adentrarse a lo que es pues entonces tendría que ir a una temática de grupo... Nosotros los médicos nos debemos dar cuenta que los tiempos han cambiado pero no nos actualizamos como debe de ser' (Médico Sergio, entrevista p. 184).»</blockquote>

<h3>2. La Lógica Fabril de las Cuotas</h3>
<p>La Secretaría de Salud evalúa el rendimiento por número de consultas (10 a 15 minutos por paciente), castigando el tiempo necesario para realizar una consejería bioética profunda sobre ITS.</p>
</div>""",

    "PARADIGMAS_CIENCIA": """<div class="summary-card">
<h3>1. El Epígrafe de Edgar Morin</h3>
<blockquote class="quote">«Nosotros pensamos que existe todavía un vasto sector de la ciencia social en el que no se está más que en las etapas taylorianas de la racionalización del trabajo intelectual y en el que el pleno de la personalidad no puede más que contribuir al rigor científico. El rigor del razonamiento es más importante que el del cálculo. El cuestionamiento es más importante que el cuestionario» (Edgar Morin, epígrafe p. 6).</blockquote>

<h3>2. La Tensión Epistémica Central</h3>
<ul>
  <li><strong>Positivismo Biologicista:</strong> Cuantifica casos y bacterias, pero ignora el significado social del afecto.</li>
  <li><strong>Pensamiento Complejo:</strong> Comprende que las prácticas sexuales adolescentes mezclan riesgos, placeres, desigualdad territorial y mandatos de género.</li>
</ul>
</div>""",

    "POSITIVISMO_BIOMEDICO": """<div class="summary-card">
<h3>1. Origen y Límites del Paradigma Biologicista</h3>
<blockquote class="quote">«El paradigma biologicista surge como resultado de diversos descubrimientos en esferas de la biología, en un contexto histórico en el cual la Medicina y otras ciencias necesitaban despojarse del oscurantismo de una época asistida por recursos religiosos... pero terminó despojando al sujeto de su subjetividad» (p. 7-8).</blockquote>

<h3>2. El Punto Ciego en la Prevención</h3>
<p>El positivismo cree erróneamente que mostrar estadísticas de mortalidad atemorizará al adolescente y lo forzará a usar condón, ignorando que la sexualidad humana se mueve por el deseo, el amor romántico y las relaciones de poder.</p>
</div>""",

    "CUALITATIVO_SOCIO": """<div class="summary-card">
<h3>1. Nombrar Palabras y Mirar Conductas</h3>
<blockquote class="quote">«La metodología planteada en la investigación parte del paradigma cualitativo, la cual da la oportunidad de nombrar 'palabras' y mirar 'conductas', teniendo como resultado una descripción transparente y una comprensión de las múltiples experiencias de los y las adolescentes que asisten al centro de salud» (p. 4).</blockquote>

<h3>2. Herramientas Hermenéuticas</h3>
<ul>
  <li><strong>Entrevistas a Fondo:</strong> Rescate del testimonio vivo de adolescentes y profesionales de salud.</li>
  <li><strong>Observación Participante:</strong> Registro del trato burocrático en salas de espera y consultorios.</li>
  <li><strong>Talleres de Reflexión:</strong> Espacio dialógico donde emergen los significados colectivos.</li>
</ul>
</div>""",

    "ANTROPOLOGIA_SOCIOLOGIA": """<div class="summary-card">
<h3>1. La Sexualidad como Disputa de Poder (Jeffrey Weeks)</h3>
<blockquote class="quote">«La opinión de Weeks (1983) es ilustrativa: 'La sexualidad no es una olla de vapor que debemos tapar porque nos puede destruir; tampoco es una fuerza vital que debemos liberar para salvar a nuestras civilizaciones. Más bien debemos cobrar conciencia de que la sexualidad es un resultado de distintas prácticas sociales que dan significado a las actividades humanas, de definiciones sociales y autodefiniciones, de luchas entre quienes tienen el poder para definir y reglamentar contra quienes se resisten. La sexualidad no es un hecho dado, es un producto de negociación, lucha y acción humanas'» (p. 16).</blockquote>

<h3>2. Berger y Luckmann</h3>
<p>Distingue entre la <strong>socialización primaria</strong> (represión y silencio familiar) y la <strong>socialización secundaria</strong> (el choque del adolescente con la escuela y la institución médica).</p>
</div>""",

    "PSICOLOGIA_EVOLUTIVA": """<div class="summary-card">
<h3>1. La Identidad en Conflicto (Aberastury y Blos)</h3>
<blockquote class="quote">«Armida Aberastury (1992) aplica el término adolescencia al período en que el joven atraviesa por desequilibrios e inestabilidades extremas para establecer su identidad... Peter Blos (1975) señala que se presenta un segundo periodo de individuación en el que hay un nuevo desarrollo del concepto de sí mismo a través del desamparo generado por la desidealización de los padres» (p. 7, 15).</blockquote>

<h3>2. Los Tres Duelos Fundamentales</h3>
<ol>
  <li>Duelo por el cuerpo infantil perdido.</li>
  <li>Duelo por el rol y la identidad de niño protegido.</li>
  <li>Duelo por la omnipotencia de las figuras parentales.</li>
</ol>
<p>El regaño médico intensifica la rebeldía del joven, alejándolo del autocuidado y empujándolo a prácticas de riesgo desafiantes.</p>
</div>""",

    "METODOLOGIA_MIXTA": """<div class="summary-card">
<h3>1. Triangulación Metodológica (Capítulo 5)</h3>
<blockquote class="quote">«El estudio es descriptivo porque especifica situaciones y eventos, describe las prácticas de promoción que el personal de salud ofrece a los adolescentes... Para recabar datos socio-demográficos se diseñó un cuestionario aplicado a 60 adolescentes dentro de la consulta médica, enfermería, trabajo social y sala de espera... complementado con entrevistas semiestructuradas y un grupo de reflexión que aportó una interacción rica de experiencias» (p. 5).</blockquote>

<h3>2. Fases de la Investigación</h3>
<ul>
  <li><strong>Fase Cuantitativa:</strong> Muestra representativa de 60 adolescentes (39% mujeres de 15-17 años, 28% de 18-19, 20% hombres de 18-19 y 13% de 15-17).</li>
  <li><strong>Fase Cualitativa:</strong> Entrevistas a médicos generales, enfermeras y trabajadoras sociales del centro.</li>
  <li><strong>Fase Participativa:</strong> 4 sesiones de taller dialógico donde se validó la propuesta emancipatoria.</li>
</ul>
</div>""",

    "CONSTRUCCION_SOCIAL": """<div class="summary-card">
<h3>1. Desnaturalización de la Adolescencia (Capítulo 1.2)</h3>
<blockquote class="quote">«La adolescencia es una construcción social... no todos los grupos humanos han vivido la adolescencia de la misma forma; está determinada por la inserción laboral, la clase y la cultura. A los adolescentes se les asigna o etiqueta con un rol de rebeldes e inmaduros... tanto es la repetición de este mensaje que el adolescente lo adopta» (p. 12, 15).</blockquote>

<h3>2. La Realidad Popular en Iztapalapa</h3>
<p>En sectores urbanos marginados, la supuesta 'moratoria social' para solo estudiar se rompe tempranamente por el trabajo informal, el embarazo precoz o el apoyo al sostenimiento del hogar.</p>
</div>""",

    "TERRITORIO_IZTAPALAPA": """<div class="summary-card">
<h3>1. Diagnóstico Sociodemográfico (Capítulos 4 y 6)</h3>
<blockquote class="quote">«La delegación Iztapalapa es la más poblada del Distrito Federal... caracterizada por contrastes socioeconómicos profundos, zonas de alta marginación, carencia histórica de servicios como agua potable y saturación en los centros de salud» (p. 102-116).</blockquote>

<h3>2. Radiografía de la Muestra Encuestada (N=60)</h3>
<ul>
  <li><strong>71% depende económicamente de sus familias</strong> (sólo 15% es autosuficiente).</li>
  <li><strong>82% vive en casa de sus progenitores</strong> en cuartos compartidos sin privacidad.</li>
  <li><strong>62% son estudiantes</strong>, 10% empleados, 10% estudia y trabaja, 10% desempleados.</li>
</ul>
<p>Las condiciones de precariedad material limitan radicalmente los márgenes de autonomía sexual de los adolescentes.</p>
</div>""",

    "GENERO_PODER": """<div class="summary-card">
<h3>1. La Doble Moral Patriarcal en la Juventud</h3>
<blockquote class="quote">«Los roles de género tradicionales colocan a las adolescentes en una posición de extrema vulnerabilidad... Si una mujer propone el uso del condón, su pareja masculina suele ofenderse, acusándola de infidelidad o catalogándola despectivamente como 'fácil'; mientras que al varón se le tolera y alienta el inicio precoz y la multiplicidad de parejas sin protección» (p. 195).</blockquote>

<h3>2. Consecuencia Sanitaria Directa</h3>
<p>La asimetría de poder hace que las mujeres jóvenes sean las víctimas predominantes del VPH y el VIH en relaciones de pareja aparentemente estables, ante el chantaje masculino: <em>'si me quisieras no me pedirías condón'</em>.</p>
</div>""",

    "TABU_FAMILIAR": """<div class="summary-card">
<h3>1. El Silencio Doméstico como Factor de Riesgo</h3>
<blockquote class="quote">«Sus padres no hablan sobre el tema de la sexualidad que sigue siendo un tabú, tanto madres como padres sienten pena de hablar de sexo de qué es y cómo se cuida. Esta reproducción cultural de la represión ha llevado a los adolescentes a iniciar su actividad sexual prematuramente sin conocimientos previos y sin elementos preventivos» (p. 177).</blockquote>

<h3>2. La Paradoja de la Prohibición</h3>
<p>Los padres prohíben hablar de sexo creyendo que así evitan el inicio erótico de sus hijos; el resultado empírico es el inicio en la clandestinidad, sin condones y con pánico a acudir al médico ante una ITS.</p>
</div>""",

    "DERECHOS_SEXUALES": """<div class="summary-card">
<h3>1. Reivindicación de los Derechos Sexuales como Derechos Humanos</h3>
<blockquote class="quote">«El campo de la salud sexual y los derechos sexuales de los y las adolescentes es todavía un campo marginal... Los adolescentes tienen derecho inalienable a la información laica, científica y oportuna, a la confidencialidad médica y al disfrute placentero y seguro de su sexualidad sin coerción ni violencia» (p. 6, 201).</blockquote>

<h3>2. Derechos Exigibles en Centros de Salud</h3>
<ol>
  <li>Derecho a la confidencialidad médica sin revelación a padres.</li>
  <li>Derecho a recibir métodos anticonceptivos y de barrera gratuitos sin tutor.</li>
  <li>Derecho al consentimiento informado y libre elección del método (NOM-005).</li>
  <li>Derecho a una vida libre de violencia y discriminación institucional.</li>
</ol>
</div>""",

    "ESI_EMANCIPATORIA": """<div class="summary-card">
<h3>1. La Propuesta Transformadora de Ramírez Ibarra (Conclusiones)</h3>
<blockquote class="quote">«Considero que mediante prácticas de promoción de la salud emancipatoria se pueden revertir los problemas planteados inicialmente al permitir a los sujetos su autoconstrucción y la defensa de sus derechos en la atención de la salud... La realización de esta investigación permite visibilizar el sentir de un grupo de población conceptualizada como 'adolescentes' (el otro)» (p. 6, 202).</blockquote>

<h3>2. Los Cuatro Ejes de Acción Inmediata</h3>
<ul>
  <li><strong>1. Talleres Dialógicos Horizontales:</strong> Sustituir la folletería y la charla magistral por talleres de reflexión entre pares.</li>
  <li><strong>2. Erradicación de la Exigencia de Tutor:</strong> Cumplimiento irrestricto de la NOM-005 para atender a cualquier joven que acuda solo.</li>
  <li><strong>3. Servicios Amigables con Horarios Vespertinos:</strong> Consultorios exclusivos y confidenciales para estudiantes de Iztapalapa.</li>
  <li><strong>4. Sensibilización Bioética del Personal de Salud:</strong> Desterrar el regaño, el juicio moral y la burocracia de 'despachar pacientes'.</li>
</ul>
</div>"""
}

# Update GRAFO_CON_BOTON_TRANSCRIPCION.html
for filepath in ["GRAFO_CON_BOTON_TRANSCRIPCION.html", "Grafo_Interactivo_Salud_ITS.html"]:
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    m = re.search(r'const rawNodes = (\[.*?\]);\n', html)
    if m:
        nodes = json.loads(m.group(1))
        updated_count = 0
        for n in nodes:
            nid = n["id"]
            if nid in rich_summaries:
                n["resumen_html"] = rich_summaries[nid]
                updated_count += 1

        # Replace in html
        new_nodes_json = json.dumps(nodes, ensure_ascii=False)
        html = html[:m.start(1)] + new_nodes_json + html[m.end(1):]

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"Successfully injected {updated_count} rich summaries into {filepath}!")
    else:
        print(f"Could not find rawNodes in {filepath}")

