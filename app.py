import flet as ft

RESPUESTAS = {
    "hola": "¡Hola! ¿En qué puedo ayudarte hoy?",
    "horario": "Las clases son de 7:00 am a 12:00 pm (Jornada Matutina) y de 1:00 pm a 6:10 pm (Jornada Vespertina).",
    "ubicación": "Estamos ubicados en Santa Rita, Copán, Honduras.",
    "director": "El director es el Lic. Carlos Manuel Chinchilla.",
    "teléfono": "Nuestro número es +504 9734-6370.",
    "correo": "Puedes escribirnos a Insuca@insuca.edu.hn",
    "becas": "Sí, contamos con programas de becas académicas y deportivas.",
    "inscripción": "El proceso de inscripción comienza en enero.",
    "requisitos": "Debes presentar partida de nacimiento, certificado de estudios y 4 fotos tamaño carnet.",
    "matrícula": "La matrícula es gratis.",
    "documentos": "Debes entregar fotocopia de identidad y boletín.",
    "ingreso": "El ingreso se evalúa mediante entrevista y prueba escrita.",
    "carreras": "Ofrecemos informática, contaduría y bachillerato en ciencias.",
    "inicio": "El año escolar inicia en febrero.",
    "finaliza": "El año escolar finaliza en noviembre.",
    "vacaciones": "El calendario escolar incluye vacaciones de medio año y otras fechas específicas.",
    "clases": "Las clases se imparten de forma presencial y virtual.",
    "plataforma": "Usamos Google Classroom para compartir clases y tareas.",
    "aula virtual": "Los estudiantes pueden ingresar al aula virtual desde cualquier dispositivo con internet.",
    "plataforma comunicacion": "Tenemos una plataforma en línea para informar sobre eventos y avisos importantes.",
    "wifi": "El instituto ofrece acceso gratuito a internet en todas las áreas, incluyendo aulas y zonas comunes.",
    "computación": "Las aulas tienen acceso a computadoras modernas.",
    "uniforme": "El uniforme es camisa blanca y pantalón azul.",
    "transporte": "No ofrecemos transporte escolar actualmente.",
    "cafetería": "La cafetería está abierta durante ambos turnos.",
    "comedor": "Hay opción de almuerzo para los alumnos en jornada extendida, con menú semanal.",
    "receso": "Hay un receso de 30 minutos entre clases.",
    "biblioteca": "La biblioteca está abierta de 8:00 am a 4:00 pm.",
    "deportes": "Organizamos competencias deportivas donde los estudiantes pueden participar.",
    "actividades": "Tenemos deportes, clubes de lectura y concursos dentro del instituto.",
    "actividades extraescolares": "Ofrecemos actividades fuera del horario como talleres, cursos y excursiones educativas.",
    "salidas extracurriculares": "Contamos con programas de excursiones para enriquecer la experiencia educativa.",
    "eventos": "Publicamos nuestros eventos académicos y escolares en nuestra página de Facebook.",
    "eventos familiares": "Organizamos celebraciones familiares como el Día de la Madre y otras actividades especiales.",
    "evaluaciones": "Se realizan evaluaciones periódicas y al final de cada parcial.",
    "notas": "Las notas pueden consultarse en línea o presencialmente.",
    "tareas": "Los docentes asignan tareas regularmente a través de Google Classroom.",
    "seguimiento académico": "Realizamos seguimiento a estudiantes con bajo rendimiento y les ofrecemos apoyo.",
    "tutorias": "Ofrecemos tutorías personalizadas para mejorar el rendimiento académico.",
    "mensualidad": "La mensualidad es de L. 100.",
    "pago": "Los pagos se realizan en efectivo o por transferencia.",
    "graduación": "La graduación se realiza en noviembre.",
    "título": "Al finalizar tu carrera se te entrega un título técnico avalado por la Secretaría de Educación.",
    "servicio": "Los alumnos de último año deben realizar horas de servicio social como requisito de graduación.",
    "prácticas": "Los estudiantes de último año deben realizar prácticas profesionales como parte de su formación.",
    "cursos": "Ofrecemos cursos de reforzamiento durante las vacaciones.",
    "materiales": "Al inicio del año se entrega una lista de materiales. Además, el instituto proporciona guías, libros y herramientas según la carrera.",
    "materiales adicionales": "También brindamos materiales educativos complementarios según el área de estudio.",
    "orientación vocacional": "Los estudiantes reciben charlas y asesoría sobre carreras y decisiones académicas.",
    "enfermería": "Tenemos personal capacitado para atender emergencias básicas.",
    "seguridad": "Contamos con vigilancia durante la entrada y salida de los estudiantes.",
    "asistencia": "La asistencia se registra a diario y se reporta en caso de inasistencias frecuentes.",
    "salida_temprana": "Las salidas anticipadas solo se permiten con autorización de los padres.",
    "facebook": "Síguenos como Instituto Superación Cashapa en Facebook.",
    "instagram": "En Instagram somos Instituto Superación Cashapa.",
    "enfermedades": "Si su hijo presenta síntomas de enfermedad, por favor no lo envíe al centro educativo",
    "celular": "El uso del celular está permitido únicamente con fines educativos y bajo supervisión del docente.",
    "formacion_docente": "Nuestros docentes reciben capacitaciones constantes en metodologías y tecnología educativa.",
    "dudas materia": "Los estudiantes pueden consultar dudas con sus docentes dentro o fuera del horario de clase, según disponibilidad.",
    "evaluación docentes": "Realizamos evaluaciones a los docentes cada periodo para mejorar la calidad educativa.",
    "soy nuevo": "Ofrecemos orientación especial para estudiantes de nuevo ingreso durante sus primeras semanas, cuenta con nuestro apoyo.",
    "ayuda":"Estoy aquí para ayudarte. ¿Qué necesitas saber?",
    "gracias": "¡De nada! Estoy para servirte.",
    "adiós": "¡Hasta pronto!",
    
}


def main(page: ft.Page):
    page.title = "InsuBot - Asistente Virtual"
    page.window_width = 400
    page.window_height = 600
    page.window_resizable = False
    page.bgcolor = ft.Colors.BLACK
    page.theme_mode = ft.ThemeMode.DARK

    chat_area = ft.ListView(
        expand=True,
        spacing=10,
        padding=10,
        auto_scroll=True,
    )

    input_box = ft.TextField(
        label="Escribe tu mensaje",
        hint_text="Ejmp. ¿Cuál es el horario de clases?",
        text_style=ft.TextStyle(color="#FFFFFF"),         
        hint_style=ft.TextStyle(color="#BDBDBD"),         
        bgcolor="#1E1E1E",                                
        border_color="#2979FF",                           
        focused_border_color="#2979FF",                   
        cursor_color="#2979FF",                           
        autofocus=True,
        expand=True,
        on_submit=lambda e: send_message(e)
    )

    send_button = ft.ElevatedButton(
        "Enviar",
        on_click=lambda e: send_message(),
        style=ft.ButtonStyle(
            bgcolor="#2979FF",        
            color="#FFFFFF",          
            padding=20,
        )
    )
    input_row = ft.Row(
        controls=[input_box, send_button],
        alignment=ft.MainAxisAlignment.CENTER
    )

    def add_bubble(message, sender):
        if sender == "user":
            bubble = ft.Container(
                content=ft.Text(message, color=ft.Colors.WHITE),
                bgcolor="#2979FF",
                padding=10,
                border_radius=10,
                alignment=ft.alignment.center_right,
                margin=ft.margin.only(left=50),
            )
        else:
            bubble = ft.Container(
                content=ft.Text(message, color=ft.Colors.BLACK),
                bgcolor="#F5F5F5",
                padding=10,
                border_radius=10,
                alignment=ft.alignment.center_left,
                margin=ft.margin.only(right=50),
            )
        chat_area.controls.append(bubble)
        page.update()
    
    def send_message():
        user_message = input_box.value.strip()
        if not user_message:
            return

        add_bubble(user_message, "user")

        user_message_lower = user_message.lower()
        response = next((value for key, value in RESPUESTAS.items() if key in user_message_lower),
                        "Lo siento, no entendí la pregunta. ¿Puedes reformularla?")
        add_bubble(response, "bot")
        input_box.value = ""
        page.update()

    page.add(chat_area, input_row)

ft.app(target=main, view=ft.WEB_BROWSER)
