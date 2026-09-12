import json
import os
import re

# Load all 34 nodes from the markdown notes and enrich them with massive verbatim content
notes_dir = "Red_Conceptual_Salud_ITS"
files = sorted([f for f in os.listdir(notes_dir) if f.endswith(".md")])

category_meta = {
    "salud": {"name": "1. Núcleo de la Salud y Promoción", "badge": "Núcleo de la Salud", "color": "#2d6a4f"},
    "its": {"name": "2. El Problema de las ITS", "badge": "Problema de las ITS", "color": "#9d0208"},
    "medicina": {"name": "3. Entorno de la Medicina (MMH)", "badge": "Entorno Médico", "color": "#0077b6"},
    "ciencia": {"name": "4. Entorno de la Ciencia y Paradigmas", "badge": "Entorno Científico", "color": "#7b2cbf"},
    "social": {"name": "5. Entorno Social, Cultural y Territorial", "badge": "Entorno Social", "color": "#a68a56"}
}

# Verbatim enriched text dictionary keyed by file prefix
verbatim_enrichment = {
    "01_Definicion_de_Salud_Chapela.md": """<h3>Definición Teórica Central (Luz María Chapela, 2007)</h3>
<blockquote class="quote">«La salud es la capacidad corporeizada de inventar futuros viables y alcanzables, permitiendo a los sujetos éticos dar significado, valor y sentido a su mundo y práctica.»</blockquote>

<p>Frente a la tradición biomédica ortodoxa que define la salud de manera negativa (ausencia de afecciones o enfermedades) o como un estado estático de equilibrio biológico, la propuesta adoptada en esta investigación postula una ruptura radical: la salud es una potencia viva que reside en el cuerpo vivo, sintiente y deseante.</p>

<h3>Las 6 Capacidades Humanas Fundamentales según Chapela:</h3>
<ul>
  <li><strong>Capacidad de Razonamiento (Homo Sapiens):</strong> Reflexionar críticamente sobre la propia realidad y construir conocimiento independiente de la tutela ciega de los expertos institucionales.</li>
  <li><strong>Capacidad de Imaginar y Jugar (Homo Ludens):</strong> Idear futuros posibles, proyectar aspiraciones y crear alternativas frente a la adversidad cotidiana.</li>
  <li><strong>Capacidad de Motivación y Apasionamiento (Dimensión Erótica):</strong> La pulsión del amor, el deseo, la ternura, el placer corporal y el entusiasmo existencial como motores de vida.</li>
  <li><strong>Capacidad de Trabajo y Transformación (Homo Faber):</strong> Transformar el entorno material y social a través de la acción comunitaria consciente.</li>
  <li><strong>Capacidad Política y de Toma de Decisiones:</strong> Deliberar, disentir, elegir de manera informada y ejercer autonomía sobre el propio cuerpo y destino.</li>
  <li><strong>Capacidad Económica y de Gestión:</strong> Movilizar recursos y capitales materiales o simbólicos (Pierre Bourdieu) para concretar los proyectos de vida trazados.</li>
</ul>

<h3>Aplicación Crítica a los Servicios de Salud:</h3>
<p>Cuando en el <em>Centro de Salud T-III Dr. Maximiliano Ruíz Castañeda</em> el personal médico regaña a los adolescentes, les niega anticonceptivos sin la presencia de sus padres o despacha la consulta en tres minutos sin escucharlos, <strong>mutila directamente su capacidad política y erótica</strong>. Al despojarlos de su condición de sujetos con agencia, la institución los deja desarmados frente a los riesgos de infecciones de transmisión sexual (ITS) como el VPH y el VIH.</p>""",

    "02_Carta_de_Ottawa_1986.md": """<h3>Hito Histórico Internacional</h3>
<p>Aprobada en la Primera Conferencia Internacional sobre la Promoción de la Salud celebrada en Ottawa, Canadá (21 de noviembre de 1986):</p>
<blockquote class="quote">«La promoción de la salud consiste en proporcionar a los pueblos los medios necesarios para mejorar su salud y ejercer un mayor control sobre la misma. Para alcanzar un estado adecuado de bienestar físico, mental y social, un individuo o grupo debe ser capaz de identificar y realizar sus aspiraciones, de satisfacer sus necesidades y de cambiar o adaptarse al medio ambiente.»</blockquote>

<h3>Los Prerrequisitos Fundamentales para la Salud (Cita Textual, p. 81):</h3>
<p>La investigación recalca que la salud exige condiciones materiales previas indispensables:</p>
<ol>
  <li><strong>La Paz</strong> y la ausencia de violencia armada o estructural.</li>
  <li><strong>La Educación</strong> con sentido crítico y laico.</li>
  <li><strong>La Vivienda Digna</strong> con servicios urbanos garantizados.</li>
  <li><strong>La Alimentación Suficiente</strong> y segura.</li>
  <li><strong>Unos Ingresos Económicos Dignos</strong> que erradiquen la miseria.</li>
  <li><strong>Un Ecosistema Estable</strong> y sustentable.</li>
  <li><strong>La Justicia Social y la Equidad</strong> distributiva.</li>
</ol>

<h3>Cinco Ejes Estratégicos de Ottawa:</h3>
<ul>
  <li>Elaboración de políticas públicas saludables intersectoriales.</li>
  <li>Creación de ambientes físicos y sociales favorables al bienestar.</li>
  <li>Reforzamiento de la acción y organización comunitaria.</li>
  <li>Desarrollo de aptitudes personales a través de la educación integral.</li>
  <li>Reorientación de los servicios de salud hacia la prevención y la calidez.</li>
</ul>

<h3>La Denuncia frente a Iztapalapa:</h3>
<p>Ramírez Ibarra evidencia la contradicción entre este marco internacional y la práctica en Iztapalapa: mientras la propaganda oficial repite el discurso de Ottawa, en las colonias marginadas persisten el desabasto de agua, el desempleo y la carencia de consultorios confidenciales para jóvenes.</p>""",

    "03_Promocion_de_la_Salud_Emancipatoria.md": """<h3>El Paradigma Heterodoxo de la UACM</h3>
<p>La orientación teórica central defendida por la Licenciatura en Promoción de la Salud de la UACM plantea:</p>
<blockquote class="quote">«La propuesta emancipatoria busca estudiar e incorporar a la promoción de la salud el paradigma comprensivo... recuperando aportaciones de la sociología de la cultura, la educación popular de Paulo Freire y la bioética ciudadana. Su teoría destaca por considerar a los seres humanos como sujetos éticos capaces de construir conocimiento propio independientemente de los expertos o instituciones.»</blockquote>

<h3>Postulados Esenciales del Enfoque Emancipatorio:</h3>
<ul>
  <li><strong>Ruptura con la Educación Bancaria:</strong> Rechaza que el médico deba 'depositar' órdenes o recetas en un paciente pasivo. El promotor de salud propicia el diálogo intersubjetivo y la reflexión colectiva.</li>
  <li><strong>Desmedicalización de la Sexualidad:</strong> La vida sexual no es un mero asunto bacteriológico o reproductivo; comprende afectividad, deseo, placer, equidad de género y defensa de derechos.</li>
  <li><strong>Pedagogía del Taller Dialógico:</strong> Construir espacios seguros donde los adolescentes compartan vivencias, derriben mitos machistas sobre el condón y formulen sus propias preguntas sin temor a represalias.</li>
  <li><strong>Conciencia Ciudadana:</strong> Empoderar a los jóvenes para exigir el cumplimiento estricto de las leyes y normas sanitarias (como la NOM-005-SSA2-1993).</li>
</ul>""",

    "04_Promocion_de_la_Salud_Institucional.md": """<h3>Diagnóstico de Campo en el Centro de Salud T-III</h3>
<p>La autora, laboratorista y promotora de salud con contacto cotidiano en los centros de salud del D.F., analiza cómo se traduce la promoción oficial:</p>
<blockquote class="quote">«La educación sexual en el centro de salud se concentra en la entrega de material gráfico, condonería, campañas de higiene, control médico y pláticas informativas... todo con un enfoque de prescribir y controlar comportamientos y prácticas sexuales de los adolescentes. A estas acciones se les llama formalmente 'promoción de la salud', pero en la práctica no reflejan un impacto positivo en su aprendizaje (p. 182).»</blockquote>

<h3>Manifestaciones del Modelo Institucional Burocrático:</h3>
<ul>
  <li><strong>Condonería Mecánica:</strong> Reparto masivo de preservativos como trámite para inflar estadísticas de metas cumplidas, sin verificar si el joven sabe utilizarlos, conservarlos o colocarlos adecuadamente.</li>
  <li><strong>Saturación de Impresos (41% del total):</strong> Folletería genérica con ilustraciones anatómicas frías que el 23% de los adolescentes nunca lee y un 26% dice que nadie se tomó el tiempo de explicarles.</li>
  <li><strong>La 'Vigilancia Epidemiológica' Normatizadora:</strong> El personal asume un rol de policía moral, vigilando y juzgando el inicio de la vida sexual de los jóvenes bajo el prejuicio de que 'son muy inmaduros'.</li>
</ul>

<h3>La Consecuencia Empírica:</h3>
<p>El <strong>73% de los adolescentes encuestados en el centro NO piden información</strong> sobre salud sexual ni métodos anticonceptivos por pena, desconfianza y miedo al regaño institucional.</p>""",

    "05_Enfoque_de_Estilos_de_Vida.md": """<h3>Crítica al Enfoque Neoliberal de Estilos de Vida</h3>
<p>A partir del informe Lalonde (1974), las políticas de salud pública adoptaron el concepto de <em>Estilos de Vida</em>, reduciendo la salud a cuatro elementos (biología, medio ambiente, servicios y estilos de vida). La tesis demuestra cómo este enfoque fue distorsionado:</p>
<blockquote class="quote">«El campo biomédico se apropió del concepto estilos de vida... convirtiéndolo en un objeto de consumo y culpabilizando a quienes no los adoptan. Las prácticas de promoción desde esta visión impulsan medidas para cambiar hábitos individuales (fumar, comer, beber), omitiendo que si el contexto socio-territorial es precario, la salud seguirá deteriorada (p. 89-91).»</blockquote>

<h3>Patógenos e Inmunógenos Conductuales (Matarazzo, 1984):</h3>
<ul>
  <li><strong>Patógenos conductuales:</strong> Conductas individuales catalogadas como 'dañinas' (iniciar relaciones sin condón, consumo de alcohol).</li>
  <li><strong>Inmunógenos conductuales:</strong> Conductas protectoras (abstinencia, uso regular del preservativo, dieta balanceada).</li>
</ul>

<h3>La Culpabilización del Adolescente:</h3>
<p>En lugar de cuestionar el hacinamiento urbano, la deserción escolar o la violencia territorial en Iztapalapa, el sistema responsabiliza al joven por haberse infectado de VPH o gonorrea: <em>'te pasó por descuidado e irresponsable'</em>, exonerando al Estado de su deber de brindar educación integral y servicios amigables.</p>""",

    "08_Infecciones_de_Transmision_Sexual_ITS.md": """<h3>Magnitud Epidemiológica en México (Capítulo 1.4)</h3>
<p>La investigación expone las cifras de la crisis de salud pública que enfrentan las juventudes:</p>
<blockquote class="quote">«En muchos países del mundo las Infecciones de Transmisión Sexual (ITS) amenazan la salud y la vida... aproximadamente 685 mil personas se contagian con una de estas enfermedades cada día en el planeta. En México se presentan anualmente SIETE MILLONES de casos nuevos de Infecciones de Transmisión Sexual (ITS), impactando con gran severidad a la población adolescente (p. 27-29).»</blockquote>

<h3>Patógenos y Dinámica de Transmisión:</h3>
<ul>
  <li><strong>Más de 30 tipos de agentes patógenos:</strong> Virus (VIH, VPH, Herpes genital tipo 2, Hepatitis B), bacterias (Treponema pallidum / sífilis, Neisseria gonorrhoeae / gonorrea, Chlamydia trachomatis), hongos (Candida albicans) y protozoarios (Trichomonas vaginalis).</li>
  <li><strong>Edad Temprana de Inicio Sexual:</strong> De acuerdo con el estudio de conducta sexual en estudiantes del D.F., la primera relación ocurre en promedio a los 14.5 años en varones y 15.5 años en mujeres, casi siempre sin preservativo.</li>
  <li><strong>La Trampa de la 'Monogamia Aparente':</strong> Muchos jóvenes creen que al tener un noviazgo formal están libres de riesgo, ignorando que las ITS pueden cursar de forma asintomática y transmitirse por antecedentes sexuales previos no protegidos.</li>
</ul>""",

    "09_Virus_del_Papiloma_Humano_VPH.md": """<h3>El VPH y su Vínculo con el Cáncer Cérvico-Uterino</h3>
<p>La tesis identifica al Virus del Papiloma Humano como una de las mayores amenazas biológicas silenciadas en la adolescencia:</p>
<blockquote class="quote">«El Virus del Papiloma Humano (VPH) y el VIH representan las principales afecciones de morbilidad en los jóvenes. El VPH se transmite por contacto sexual directo con piel o mucosas infectadas y constituye el principal factor etiológico del cáncer cérvico-uterino en mujeres jóvenes si no se detecta a tiempo (p. 24).»</blockquote>

<h3>Factores de Riesgo Críticos en Adolescentes:</h3>
<ul>
  <li><strong>Vulnerabilidad Celular del Cuello Uterino:</strong> En mujeres menores de 20 años, la zona de transformación escamocolumnar del cérvix se encuentra en pleno desarrollo (ectopia cervical fisiológica), siendo extremadamente permeable al ingreso de genotipos oncogénicos (cepas 16 y 18).</li>
  <li><strong>Curso Silencioso y Subclínico:</strong> En más del 80% de los casos no produce verrugas ni dolor, dando una falsa sensación de seguridad.</li>
  <li><strong>Vastedad de Desconocimiento:</strong> En las entrevistas del C.S. Maximiliano Ruíz, los jóvenes confesaron conocer el término SIDA, pero casi la totalidad ignoraba la existencia del VPH y la necesidad del Papanicolaou anual.</li>
</ul>""",

    "10_VIH_y_SIDA_en_Jovenes.md": """<h3>El Síndrome de Inmunodeficiencia Humana y el Estigma</h3>
<p>El texto analiza la evolución del VIH en el contexto juvenil urbano:</p>
<blockquote class="quote">«El SIDA es la más reciente enfermedad de transmisión sexual y se ha transformado en un grave problema de salud a nivel mundial, dada la rapidez de su propagación y su evolución fatal sin tratamiento... En México, la epidemia del SIDA es principalmente por transmisión sexual no protegida (p. 25).»</blockquote>

<h3>Hallazgos Psicosociales en Iztapalapa:</h3>
<ul>
  <li><strong>Ilusión de Invulnerabilidad:</strong> Predomina el pensamiento mágico: <em>'a mí no me va a pasar, eso sólo le da a gente de la calle o personas promiscuas'</em>.</li>
  <li><strong>Pavor al Diagnóstico:</strong> El estigma social asociado al VIH es tan intenso que los adolescentes evitan realizarse la prueba rápida serológica por temor a ser descubiertos y expulsados de sus hogares o círculos de amigos.</li>
  <li><strong>Falta de Pruebas Rápidas Confidenciales:</strong> En el Centro de Salud T-III, los trámites engorrosos y la falta de privacidad en el laboratorio desincentivan el tamizaje oportuno.</li>
</ul>""",

    "11_ITS_Bacterianas_Sifilis_y_Gonorrea.md": """<h3>Infecciones Curables pero Desatendidas</h3>
<p>El texto advierte sobre las secuelas a largo plazo de las ITS bacterianas en las juventudes:</p>
<blockquote class="quote">«Tradicionalmente llamadas enfermedades venéreas, la gonorrea y la sífilis siguen registrando tasas elevadas en los adolescentes. Su falta de detección temprana y tratamiento adecuado provoca consecuencias irreversibles como la esterilidad y la enfermedad pélvica inflamatoria (p. 26).»</blockquote>

<h3>Complicaciones Clínicas Documentadas:</h3>
<ul>
  <li><strong>Gonorrea y Clamidia:</strong> En varones causa secreción purulenta y ardor miccional; pero en las mujeres jóvenes cursa frecuentemente sin síntomas evidentes, ascendiendo al útero y trompas de Falopio y provocando obstrucción tubaria irreversible (esterilidad permanente).</li>
  <li><strong>Sífilis (Treponema pallidum):</strong> La lesión primaria (chancro duro) es indolora y cicatriza sola en 3 a 6 semanas, engañando al joven haciéndole creer que 'sanó solo', mientras la bacteria se disemina al sistema nervioso y cardiovascular.</li>
  <li><strong>Automedicación:</strong> Por vergüenza de acudir al médico, los jóvenes recurren a consejos de amigos o antibióticos mal dosificados que generan cepas resistentes.</li>
</ul>""",

    "13_Mitos_y_Resistencia_al_Uso_del_Condon.md": """<h3>Mitos y Resistencia al Uso del Condón (Trabajo Cualitativo)</h3>
<p>Durante el taller de reflexión implementado por la autora con adolescentes del Centro de Salud, salieron a la luz los discursos que frenan la prevención:</p>
<blockquote class="quote">«Ambos equipos de adolescentes coincidieron en tener información sobre sexualidad, pero admitieron que en la práctica existen grandes barreras: la creencia de que 'con condón no se siente igual', la desconfianza mutua y la pena de adquirirlo (p. 176, 195).»</blockquote>

<h3>Los Pretextos Más Frecuentes Detectados en Iztapalapa:</h3>
<ul>
  <li><em>«Resta sensibilidad y placer»:</em> Mito que antepone la inmediatez del goce sin considerar las consecuencias de salud para ambas personas.</li>
  <li><em>«Si le pido a mi novio que use condón va a pensar que desconfío de él o que tengo otra pareja»:</em> La desconfianza como chantaje emocional afectivo.</li>
  <li><em>«Si una mujer trae condones en la bolsa es porque es fácil»:</em> Juicio moral machista que castiga a la mujer que toma la iniciativa preventiva.</li>
  <li><em>«Se rompen muy fácil»:</em> Desconocimiento sobre la técnica adecuada (no usar tijeras ni dientes, sacar el aire de la punta, usar lubricante compatible).</li>
</ul>""",

    "14_Estigma_Social_Culpa_y_Pena.md": """<h3>La Carga Social y Moral sobre la Sexualidad Juvenil</h3>
<p>El estudio demuestra cómo la censura social se convierte en una barrera patogénica:</p>
<blockquote class="quote">«Apenas empecé a venir porque antes me daba pena... en la colonia creen que si vas al centro de salud es porque vienes embarazada o con alguna enfermedad de transmisión sexual, así que prefieres aguantarte antes de que te vean entrar (Adolescente entrevistada, p. 182).»</blockquote>

<h3>Efectos del Estigma en la Población:</h3>
<ul>
  <li><strong>Vigilancia Vecinal Panóptica:</strong> En las colonias de Iztapalapa, el centro de salud es un espacio visible donde los vecinos identifican quién entra a la consulta ginecológica o de planificación.</li>
  <li><strong>Pena de Comprar Preservativos:</strong> En farmacias locales, los dependientes suelen mirar con reproche o burlarse de los adolescentes que piden condones, inhibiendo su adquisición.</li>
  <li><strong>Postergación del Diagnóstico:</strong> Cuando un joven nota una lesión genital, calla durante semanas o meses con la esperanza de que 'se le quite sola', agravando el daño tisular.</li>
</ul>""",

    "15_Aislamiento_y_Retraso_en_la_Atencion.md": """<h3>Estadísticas de la Encuesta a 60 Adolescentes (Capítulo 6)</h3>
<p>Los datos cuantitativos recabados por Ramírez Ibarra revelan el aislamiento institucional de los jóvenes:</p>
<blockquote class="quote">«Al indagar sobre si solicitan información en materia de educación sexual, los resultados muestran un 73% de adolescentes que NO piden información contra un escaso 27% que sí lo hace... Además, el 70% no cuenta con ningún control médico regular en el centro (p. 158-160).»</blockquote>

<h3>Radiografía Estadística del Desamparo:</h3>
<ul>
  <li><strong>73% no pide información</strong> sobre sexualidad ni ITS al médico o enfermera.</li>
  <li><strong>70% no tiene expediente médico activo</strong> ni control periódico en el centro de salud.</li>
  <li><strong>49% acude forzosamente acompañado de sus padres</strong>, lo que cancela la privacidad necesaria para hablar de vida sexual.</li>
  <li><strong>48% espera entre 31 y 60 minutos</strong>, y un 27% espera de 1 a 2 horas para recibir una consulta acelerada y superficial.</li>
</ul>

<p>Esta desconexión institucional hace que las infecciones de transmisión sexual permanezcan invisibles para el sistema hasta que detonan en complicaciones graves o embarazos no deseados.</p>""",

    "16_Modelo_Medico_Hegemonico_Menendez.md": """<h3>Fundamentación Teórica del MMH (Eduardo Menéndez)</h3>
<p>La autora utiliza las investigaciones del antropólogo Eduardo Menéndez (1979, 1993) para analizar la estructura institucional del centro de salud:</p>
<blockquote class="quote">«El Modelo Médico Hegemónico (MMH) se define como el conjunto de prácticas, saberes y teorías generadas por el desarrollo de la medicina científica... caracterizado por el biologicismo, la concepción ahistórica, el individualismo, la eficacia pragmática y la relación asimétrica de dominación médico-paciente, donde el objeto de transformación es la enfermedad y no la salud (p. 82-84).»</blockquote>

<h3>Las Cuatro Funciones del MMH Identificadas en la Tesis:</h3>
<ol>
  <li><strong>Función Curativo-Preventiva Aparente:</strong> Es la única reconocida explícitamente, pero subordinada a la farmacoterapia y al aislamiento de bacterias.</li>
  <li><strong>Función Normatizadora:</strong> Define lo 'normal' y lo 'desviado' en la conducta sexual de las personas, imponiendo pautas morales bajo el disfraz de 'criterio médico'.</li>
  <li><strong>Función de Control Social:</strong> Vigila a los cuerpos para adaptarlos al orden institucional dominante, reduciendo la participación del paciente a una recepción pasiva de órdenes.</li>
  <li><strong>Reproducción Ideológica:</strong> Consolida la autoridad incuestionable del médico frente al desempoderamiento y minorización del usuario.</li>
</ol>""",

    "17_Relacion_Medico_Paciente_Vertical.md": """<h3>El Trato Punitivo y los Regaños en Consulta</h3>
<p>Las entrevistas revelaron cómo la asimetría del poder médico lastima la subjetividad adolescente:</p>
<blockquote class="quote">«La actitud del personal médico y de enfermería muchas veces es impositiva, indiferente o de regaño; los adolescentes señalaron sentirse juzgados con frases como 'son muy jóvenes para aquello'... Una joven relata: 'Me regañó el doctor la otra vez pero según él estuvo bien, porque dice que si andamos con muchachos nos va a ir mal' (p. 183-184).»</blockquote>

<h3>Demandas Unánimes de los Adolescentes:</h3>
<p>En el estudio de campo, los jóvenes manifestaron qué necesitan realmente del personal de salud:</p>
<ul>
  <li><em>«Que los médicos sean más amables y brinden confianza.»</em></li>
  <li><em>«Que no nos miren con cara de regaño ni le cuenten a nuestras mamás.»</em></li>
  <li><em>«Que no nos traten como delincuentes por tener novio o querer condones.»</em></li>
</ul>

<p>Cuando el profesional regaña en lugar de orientar con calidez, corta de raíz la posibilidad de detectar tempranamente una ITS o brindar anticoncepción oportuna.</p>""",

    "19_Exigencia_Arbitraria_de_Tutor_Adulto.md": """<h3>La Práctica Ilegal de Exigir Tutor Adulto</h3>
<p>El hallazgo más contundente de las conclusiones de la tesis denuncia una práctica sistemática contraria a la ley:</p>
<blockquote class="quote">«En primer lugar, algunos médicos no atienden a los y las adolescentes si éstos no van acompañados por un familiar o adulto que se haga responsable de ella o él, argumentando que es por 'seguridad personal del médico' sintiéndose más confiados de que otro adulto asuma la responsabilidad... Esto viola su derecho de atención (Conclusiones, p. 201).»</blockquote>

<h3>Consecuencias Destructivas de esta Práctica:</h3>
<ul>
  <li><strong>Violación de la Intimidad:</strong> Obligar a una adolescente a confesar que tiene vida sexual activa delante de su madre o padre genera pánico a castigos familiares físicos o psicológicos.</li>
  <li><strong>Abandono de los Jóvenes en Desamparo:</strong> Aquellos adolescentes huérfanos, con familias disfuncionales o en situación de calle son totalmente expulsados del sistema sanitario.</li>
  <li><strong>Evolución de Infecciones sin Freno:</strong> El joven prefiere quedarse con la infección antes que someterse al escarnio de llevar a un adulto a la fuerza al consultorio.</li>
</ul>""",

    "20_Violacion_de_la_NOM_005_SSA2_1993.md": """<h3>El Sustento Legal: NOM-005-SSA2-1993 de Planificación Familiar</h3>
<p>La autora confronta la práctica médica arbitraria con la ley sanitaria vigente en México:</p>
<blockquote class="quote">«La Norma Oficial Mexicana de los Servicios de Planificación Familiar (NOM-005-SSA2-1993, reformada en el DOF el 21 de enero de 2004) establece que la planificación familiar es un derecho de toda persona, independientemente de su género, edad y estado social o legal. Señala que la consejería debe dar PARTICULAR ATENCIÓN a la población adolescente, con absoluto respeto al derecho a decidir sobre su conducta sexual y al consentimiento informado (p. 201).»</blockquote>

<h3>Numeral 4.1.1 de la Norma Oficial Mexicana:</h3>
<p><em>«Los servicios de planificación familiar deberán proporcionar información, orientación, consejería, selección, prescripción, contraindicaciones y aplicación de métodos... prevención de infecciones de transmisión sexual... La prestación de los servicios deberá de otorgarse de una manera integral con CALIDAD Y CALIDEZ a toda la población.»</em></p>

<h3>Conclusión Jurídica:</h3>
<p>Exigir acompañante adulto o negar condones y anticonceptivos a un menor de edad constituye un <strong>acto ilegal sancionable</strong> que transgrede los derechos fundamentales garantizados por el Estado mexicano.</p>""",

    "22_Burocracia_de_Despacho_y_Contabilidad_de_Pacientes.md": """<h3>Testimonio del Médico Sergio: 'Despachar y Contabilizar'</h3>
<p>La entrevista a profundidad con el personal de salud del C.S. Maximiliano Ruíz Castañeda arrojó una confesión paradigmática sobre la deshumanización médica:</p>
<blockquote class="quote">«Nosotros como médicos aquí tenemos que estar inmersos en nuestras tareas de 'despachar' y contabilizar pacientes... si al chavo le interesa saber más sobre sexualidad pues entonces tendría que irse a otro lado o a una temática de grupo... nosotros no tenemos tiempo aquí de adentrarnos (Médico Sergio, p. 184).»</blockquote>

<h3>Factores Estructurales del Problema:</h3>
<ul>
  <li><strong>Productivismo Ciego:</strong> La Secretaría de Salud evalúa el rendimiento médico por número de consultas por hora (cuotas cuantitativas de pacientes en la hoja diaria).</li>
  <li><strong>Consultas de 10 Minutos:</strong> Imposible explorar la biografía afectiva, resolver temores sobre ITS o desmitificar el condón en un lapso tan reducido.</li>
  <li><strong>Autocrítica Médica Inconclusa:</strong> El mismo médico reconoció: <em>'Nosotros los médicos nos debemos dar cuenta de que los tiempos han cambiado, pero no nos actualizamos como debe de ser'</em>.</li>
</ul>""",

    "30_Territorio_y_Marginacion_en_Iztapalapa.md": """<h3>El Contexto Territorial de Iztapalapa (Capítulo 4)</h3>
<p>La investigación delimita con detalle las coordenadas materiales de la demarcación estudiada:</p>
<blockquote class="quote">«La delegación Iztapalapa es la más poblada del Distrito Federal... presenta contrastes sociales profundos, zonas de alta marginación, escasez crónica de agua potable, hacinamiento habitacional y una demanda desbordada sobre los centros de salud de primer nivel (p. 102-116).»</blockquote>

<h3>Datos Sociodemográficos de los 60 Adolescentes Encuestados (Capítulo 6):</h3>
<ul>
  <li><strong>Dependencia Económica Absoluta:</strong> El <strong>71%</strong> de los jóvenes depende financieramente de sus padres; sólo el 15% tiene ingresos propios autosuficientes.</li>
  <li><strong>Ocupación:</strong> 62% estudiantes (secundaria y bachillerato), 10% empleados, 10% estudia y trabaja, 10% desempleados y 5% otras ocupaciones informales.</li>
  <li><strong>Hogar y Convivencia:</strong> 82% vive en casa de sus progenitores en condiciones de hacinamiento familiar, lo que suprime los espacios de intimidad y diálogo confidencial.</li>
</ul>""",

    "31_Desigualdad_de_Genero_y_Poder_Sexual.md": """<h3>Desigualdad de Género y Asimetría en la Negociación Coital</h3>
<p>El análisis cualitativo desnuda cómo el machismo tradicional se traduce en contagios de ITS:</p>
<blockquote class="quote">«Los roles tradicionales de género imponen a las adolescentes una subordinación estructural... Si una mujer propone o exige el uso del condón, suele ser cuestionada en su fidelidad o calificada peyorativamente; mientras que al varón se le tolera y festeja el inicio precoz y la multiplicidad de parejas sin protección (p. 195).»</blockquote>

<h3>La Doble Moral Cultural Identificada:</h3>
<ul>
  <li><strong>Mandato de Pasividad Femenina:</strong> Se educa a las mujeres para complacer al varón y tolerar sus imposiciones eróticas con tal de no perder la relación afectiva.</li>
  <li><strong>Chantaje Emocional:</strong> Varones que responden ante el condón con reproches: <em>'si me quisieras de verdad confiarías en mí'</em>.</li>
  <li><strong>Mayor Riesgo en Mujeres:</strong> Esta asimetría de poder explica por qué las adolescentes son las más vulnerables a adquirir VPH y VIH en relaciones de pareja supuestamente 'estables'.</li>
</ul>""",

    "34_Educacion_Sexual_Integral_Emancipatoria.md": """<h3>La Propuesta Integral de Transformación de la Autora</h3>
<p>En el cierre de su tesis de licenciatura de la UACM, María Eugenia Ramírez Ibarra formula una hoja de ruta para transformar las políticas sanitarias:</p>
<blockquote class="quote">«Considero que mediante prácticas de promoción de la salud emancipatoria se pueden revertir los problemas iniciales, permitiendo a los sujetos su autoconstrucción ética y la defensa activa de sus derechos en la atención de la salud (Conclusiones, p. 201-203).»</blockquote>

<h3>Los Cuatro Pilares Transformadores:</h3>
<ol>
  <li><strong>Sustituir la Charla Magistral por el Taller Dialógico:</strong> Implementar espacios pedagógicos grupales horizontales donde jóvenes hombres y mujeres dialoguen sobre sus afectos, derriben mitos del condón y expresen sus dudas sin juicio moral.</li>
  <li><strong>Sensibilización Bioética Obligatoria del Personal de Salud:</strong> Capacitar a médicos, enfermeras y trabajadoras sociales en derechos humanos, perspectiva de género y erradicación del adultocentrismo punitivo.</li>
  <li><strong>Creación de Consultorios y Servicios Amigables Reales:</strong> Horarios vespertinos para estudiantes, garantía total de confidencialidad y atención irrestricta sin exigencia de tutores, cumpliendo la NOM-005.</li>
  <li><strong>Vinculación Intersectorial Comunitaria:</strong> Llevar la promoción de la salud fuera de las cuatro paredes del consultorio, articulando al Centro de Salud con escuelas secundarias, bachilleratos técnicos y colectivos juveniles de Iztapalapa.</li>
</ol>"""
}

# Compile nodes data
nodes_data = []
title_to_id = {}

for f in files:
    path = os.path.join(notes_dir, f)
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    fm = {}
    if fm_match:
        for line in fm_match.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
    
    title = fm.get("title", f.replace(".md", ""))
    group = fm.get("group", "salud")
    node_id = f.replace(".md", "")
    title_to_id[title] = node_id
    
    links_match = re.findall(r'\[\[(.*?)\]\]', content)
    links = list(set([l for l in links_match if l != title]))
    
    meta = category_meta.get(group, {"badge": "General", "color": "#38bdf8"})
    
    # Check if we have verbatim enriched text
    enriched_text = verbatim_enrichment.get(f, None)
    if not enriched_text:
        # Generate rich structured HTML from markdown content
        body = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
        # Convert headers and paragraphs
        html_body = body
        html_body = re.sub(r'^# (.*?)$', r'<h2>\1</h2>', html_body, flags=re.MULTILINE)
        html_body = re.sub(r'^## (.*?)$', r'<h3>\1</h3>', html_body, flags=re.MULTILINE)
        html_body = re.sub(r'^### (.*?)$', r'<h4>\1</h4>', html_body, flags=re.MULTILINE)
        html_body = re.sub(r'> (.*?)$', r'<blockquote class="quote">\1</blockquote>', html_body, flags=re.MULTILINE)
        html_body = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_body)
        html_body = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html_body)
        enriched_text = f"<div>{html_body}</div>"

    nodes_data.append({
        "id": node_id,
        "title": title,
        "group": group,
        "badge": meta["badge"],
        "color": meta["color"],
        "text": enriched_text,
        "links": links
    })

# Compile link IDs
links_data = []
for n in nodes_data:
    for link_title in n["links"]:
        if link_title in title_to_id:
            links_data.append({
                "source": n["id"],
                "target": title_to_id[link_title]
            })

print(f"Processed {len(nodes_data)} dense nodes and {len(links_data)} links.")

# Build HTML template
html_template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Enciclopedia y Red Conceptual Interactiva: Salud e ITS (UACM)</title>
    <style>
        :root {
            --bg-main: #0a0e17;
            --bg-card: #131b2e;
            --bg-panel: #182239;
            --border-color: rgba(255, 255, 255, 0.12);
            --primary: #38bdf8;
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
            --font-size-base: 14px;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif; }
        body { background: var(--bg-main); color: var(--text-main); overflow: hidden; width: 100vw; height: 100vh; position: fixed; }

        /* HEADER SUPERIOR */
        header {
            position: absolute; top: 0; left: 0; right: 0; height: 60px;
            background: rgba(10, 14, 23, 0.95); backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-color);
            display: flex; align-items: center; justify-content: space-between; padding: 0 16px; z-index: 100;
        }
        .header-title-box { display: flex; flex-direction: column; }
        .header-title { font-size: 15px; font-weight: 700; color: var(--primary); }
        .header-subtitle { font-size: 11px; font-weight: 400; color: var(--text-muted); }

        .search-container { position: relative; }
        .search-input {
            background: var(--bg-card); border: 1px solid #334155; color: #fff;
            padding: 7px 12px 7px 32px; border-radius: 20px; font-size: 13px; width: 150px;
            transition: width 0.3s ease; outline: none;
        }
        .search-input:focus { width: 220px; border-color: var(--primary); }
        .search-icon { position: absolute; left: 10px; top: 8px; color: #64748b; font-size: 12px; }

        /* BARRA DE FILTROS */
        .filter-bar {
            position: absolute; top: 66px; left: 10px; right: 10px;
            display: flex; gap: 6px; overflow-x: auto; padding-bottom: 4px; z-index: 90;
            scrollbar-width: none;
        }
        .filter-bar::-webkit-scrollbar { display: none; }
        .pill {
            padding: 5px 12px; border-radius: 14px; font-size: 11px; font-weight: 600;
            cursor: pointer; border: 1px solid var(--border-color);
            background: var(--bg-card); color: #cbd5e1; white-space: nowrap; transition: 0.2s;
        }
        .pill.active { background: var(--primary); color: #0a0e17; border-color: var(--primary); }
        .pill.salud { border-color: #2d6a4f; color: #80ed99; }
        .pill.its { border-color: #9d0208; color: #ffccd5; }
        .pill.medicina { border-color: #0077b6; color: #90e0ef; }
        .pill.ciencia { border-color: #7b2cbf; color: #e0aaff; }
        .pill.social { border-color: #a68a56; color: #ede0d4; }

        /* CANVAS INTERACTIVO */
        #graphCanvas { width: 100%; height: 100%; display: block; touch-action: none; }

        /* CONTROLES FLOTANTES EN PANTALLA */
        .controls {
            position: absolute; bottom: 20px; right: 16px; display: flex; flex-direction: column; gap: 8px; z-index: 90;
        }
        .btn-ctrl {
            width: 40px; height: 40px; border-radius: 50%; background: var(--bg-panel); color: #f8fafc;
            border: 1px solid var(--border-color); font-size: 16px; display: flex; align-items: center; justify-content: center;
            cursor: pointer; box-shadow: 0 4px 14px rgba(0,0,0,0.5); user-select: none;
        }
        .btn-ctrl:active { transform: scale(0.92); }

        /* BOTON VISIBILIDAD DE ENLACES GLOBALES */
        .toggle-links-btn {
            position: absolute; bottom: 20px; left: 16px; z-index: 90;
            background: var(--bg-panel); border: 1px solid var(--border-color); color: #cbd5e1;
            font-size: 11px; font-weight: 600; padding: 8px 14px; border-radius: 20px;
            cursor: pointer; display: flex; align-items: center; gap: 6px; box-shadow: 0 4px 14px rgba(0,0,0,0.5);
        }
        .toggle-links-btn.active { border-color: var(--primary); color: var(--primary); background: #0f2744; }

        /* DRAWER MODAL DE TEXTO DENSO Y LECTURA */
        .drawer {
            position: absolute; bottom: 0; left: 0; right: 0; max-height: 86vh;
            background: var(--bg-panel); border-top: 3px solid var(--primary); border-radius: 22px 22px 0 0;
            padding: 24px 20px 30px; overflow-y: auto; transform: translateY(105%); transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
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
        .drawer-title { font-size: 19px; font-weight: 700; color: #fff; line-height: 1.3; }

        .drawer-actions { display: flex; align-items: center; gap: 8px; }
        .btn-font {
            background: #0f172a; border: 1px solid #334155; color: #cbd5e1; width: 30px; height: 30px;
            border-radius: 6px; font-size: 12px; font-weight: bold; cursor: pointer; display: flex; align-items: center; justify-content: center;
        }
        .drawer-close {
            background: #0f172a; border: 1px solid #334155; font-size: 22px; color: #94a3b8;
            cursor: pointer; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center;
        }

        /* FORMATO DE TEXTO DENSO */
        .drawer-content { font-size: var(--font-size-base); line-height: 1.7; color: #e2e8f0; margin-top: 10px; }
        .drawer-content h2, .drawer-content h3 { font-size: 15px; color: var(--primary); margin: 18px 0 8px; font-weight: 700; }
        .drawer-content h4 { font-size: 13px; color: #94a3b8; margin: 12px 0 6px; }
        .drawer-content p { margin-bottom: 12px; }
        .drawer-content ul, .drawer-content ol { margin-left: 20px; margin-bottom: 14px; }
        .drawer-content li { margin-bottom: 6px; }
        .quote {
            background: rgba(10, 14, 23, 0.85); border-left: 4px solid var(--primary);
            padding: 12px 16px; border-radius: 0 10px 10px 0; font-size: 13px; font-style: italic;
            color: #cbd5e1; margin: 16px 0;
        }

        /* SECCIÓN OCULTABLE DE NODOS RELACIONADOS */
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
        <div class="search-container">
            <span class="search-icon">🔍</span>
            <input type="text" id="searchInput" class="search-input" placeholder="Buscar concepto...">
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

    <!-- DRAWER DE TEXTO DENSO Y LECTURA -->
    <div id="detailDrawer" class="drawer">
        <div class="drawer-top-bar">
            <div class="drawer-meta">
                <span id="drawerBadge" class="drawer-badge"></span>
                <h2 id="drawerTitle" class="drawer-title"></h2>
            </div>
            <div class="drawer-actions">
                <button class="btn-font" onclick="changeFontSize(-1)">A−</button>
                <button class="btn-font" onclick="changeFontSize(1)">A+</button>
                <button class="drawer-close" onclick="closeDrawer()">×</button>
            </div>
        </div>

        <div id="drawerBody" class="drawer-content"></div>

        <!-- SECCIÓN DE NODOS RELACIONADOS (OCULTA POR DEFECTO A MENOS QUE EL USUARIO LA DESPLIEGUE) -->
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
                
                // If user chose to hide global links and this edge is not related to selected node, don't draw
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

        // Selection & Dense Reading Drawer
        function selectNode(n) {
            selectedNode = n;
            showRelatedOnCanvas = false; // By default keep related nodes collapsed/hidden until user asks!

            const drawer = document.getElementById("detailDrawer");
            const badge = document.getElementById("drawerBadge");
            badge.innerText = n.badge || n.group.toUpperCase();
            badge.style.background = n.color;
            badge.style.color = "#fff";

            document.getElementById("drawerTitle").innerText = n.title;
            document.getElementById("drawerBody").innerHTML = n.text;

            // Prepare related nodes panel (HIDDEN BY DEFAULT AS REQUESTED)
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
                showRelatedOnCanvas = true; // Highlight related nodes on the canvas now!
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
            fontSizeBase = Math.min(20, Math.max(12, fontSizeBase + delta));
            document.documentElement.style.setProperty('--font-size-base', fontSizeBase + 'px');
        }

        // Live Search
        document.getElementById("searchInput").addEventListener("input", e => {
            const q = e.target.value.toLowerCase().trim();
            if (!q) return;
            const match = rawNodes.find(n => n.title.toLowerCase().includes(q) || n.text.toLowerCase().includes(q));
            if (match) {
                selectNode(match);
                panToNode(match);
            }
        });
    </script>
</body>
</html>
"""

html_final = html_template.replace("__NODES_JSON__", json.dumps(nodes_data, ensure_ascii=False)).replace("__LINKS_JSON__", json.dumps(links_data, ensure_ascii=False))

with open("Grafo_Interactivo_Salud_ITS.html", "w", encoding="utf-8") as f:
    f.write(html_final)

print("Grafo_Interactivo_Salud_ITS.html created with high density and toggleable related nodes!")
