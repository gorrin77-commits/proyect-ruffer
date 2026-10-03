from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit
from config import * 
from result import FinalWindow

class TestWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # --- 1. CONFIGURACIÓN BÁSICA DE LA VENTANA ---
        self.setWindowTitle(TXT_TEST_TITLE)
        self.resize(WIN_WIDTH, WIN_HEIGHT)
        self.move(WIN_X, WIN_Y)

        # --- 2. CREACIÓN DE LOS ENTEROS Y ELEMENTOS GRÁFICOS ---
        # Datos del usuario
        self.lbl_name = QLabel("Introduce tu nombre completo:")
        self.line_name = QLineEdit("Nombre")
        self.lbl_age = QLabel(TXT_AGE)
        self.line_age = QLineEdit("0")
        
        # Prueba 1
        self.lbl_test1 = QLabel(TXT_TEST1)
        self.btn_test1 = QPushButton(TXT_START_TEST1)
        self.line_p1 = QLineEdit("0")
        
        # Prueba 2
        self.lbl_test2 = QLabel(TXT_TEST2)
        self.btn_test2 = QPushButton(TXT_START_TEST2)
        self.line_p2 = QLineEdit("0")
        
        # Prueba 3
        self.lbl_test3 = QLabel(TXT_TEST3)
        self.btn_test3 = QPushButton(TXT_START_TEST3)
        self.line_p3 = QLineEdit("0")
        
        # Botón final para enviar
        self.btn_submit = QPushButton(TXT_SEND_RESULTS)

        # El texto gigante del cronómetro
        self.lbl_timer = QLabel("00:00:00")
        self.lbl_timer.setStyleSheet("font-size: 42px; font-weight: bold;")

        # --- 3. AJUSTAR TAMAÑOS ---
        input_width = 300
        self.line_name.setMaximumWidth(input_width)
        self.line_age.setMaximumWidth(input_width)
        self.line_p1.setMaximumWidth(input_width)
        self.line_p2.setMaximumWidth(input_width)
        self.line_p3.setMaximumWidth(input_width)
        self.btn_test1.setMaximumWidth(input_width)
        self.btn_test2.setMaximumWidth(input_width)
        self.btn_test3.setMaximumWidth(input_width)

        # --- 4. CREAR LAS LÍNEAS DE DISEÑO (LAYOUTS) Y ACOMODAR TODO ---
        self.h_line = QHBoxLayout()  # Línea principal horizontal
        self.l_line = QVBoxLayout()  # Columna izquierda (Formulario)
        self.r_line = QVBoxLayout()  # Columna derecha (Cronómetro)

        # Añadir cosas a la columna izquierda una por una
        self.l_line.addWidget(self.lbl_name)
        self.l_line.addWidget(self.line_name)
        self.l_line.addWidget(self.lbl_age)
        self.l_line.addWidget(self.line_age)
        self.l_line.addWidget(self.lbl_test1)
        self.l_line.addWidget(self.btn_test1)
        self.l_line.addWidget(self.line_p1)
        self.l_line.addWidget(self.lbl_test2)
        self.l_line.addWidget(self.btn_test2)
        self.l_line.addWidget(self.line_p2)
        self.l_line.addWidget(self.lbl_test3)
        self.l_line.addWidget(self.btn_test3)
        self.l_line.addWidget(self.line_p3)
        self.l_line.addWidget(self.btn_submit, alignment=Qt.AlignLeft)

        # Añadir el cronómetro centrado en la columna derecha usando espacios vacíos (Stretch)
        self.r_line.addStretch() 
        self.r_line.addWidget(self.lbl_timer, alignment=Qt.AlignCenter)
        self.r_line.addStretch() 

        # Juntar las dos columnas en la línea principal
        self.h_line.addLayout(self.l_line, stretch=3)
        self.h_line.addLayout(self.r_line, stretch=1)
        self.setLayout(self.h_line)

        # --- 5. CONFIGURACIÓN DEL TEMPORIZADOR INTERNO ---
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_event) # Conectar con la función que resta segundos
        self.time_counter = 0
        self.current_test = 0

        # --- 6. CONECTAR LOS BOTONES A SUS ACCIONES ---
        self.btn_test1.clicked.connect(self.start_test1)
        self.btn_test2.clicked.connect(self.start_test2)
        self.btn_test3.clicked.connect(self.start_test3)
        self.btn_submit.clicked.connect(self.next_click)

        # Mostrar la ventana al terminar de armar todo
        self.show()

    # --- ACCIONES DE LOS BOTONES ---

    def start_test1(self):
        self.current_test = 1
        self.time_counter = 15
        self.lbl_timer.setText("00:00:15")
        self.timer.start(1000) # Activar para que cuente cada 1 segundo (1000 milisegundos)

    def start_test2(self):
        self.current_test = 2
        self.time_counter = 45
        self.lbl_timer.setText("00:00:45")
        self.timer.start(1000)

    def start_test3(self):
        self.current_test = 3
        self.time_counter = 60
        self.lbl_timer.setText("00:01:00")
        self.timer.start(1000)

    # Lo que pasa cada vez que pasa un segundo en el cronómetro
    def timer_event(self):
        self.time_counter -= 1
        time = QTime(0, 0, 0).addSecs(self.time_counter)
        self.lbl_timer.setText(time.toString("hh:mm:ss"))
        
        # Lógica especial de colores solo para la prueba 3
        if self.current_test == 3:
            if self.time_counter <= 15:
                self.lbl_timer.setStyleSheet("font-size: 42px; font-weight: bold; color: green;")
            else:
                self.lbl_timer.setStyleSheet("font-size: 42px; font-weight: bold; color: black;")
                
        # Si el tiempo llega a cero, detener el reloj
        if self.time_counter == 0:
            self.timer.stop()
            self.lbl_timer.setStyleSheet("font-size: 42px; font-weight: bold; color: black;")

    # Botón para ir a la ventana de resultados
    def next_click(self):
        try:
            # Convertir los textos a números enteros
            age = int(self.line_age.text())
            p1 = int(self.line_p1.text())
            p2 = int(self.line_p2.text())
            p3 = int(self.line_p3.text())
        except ValueError:
            # Si el usuario escribió letras o dejó vacío, poner todo en cero para que no explote el programa
            age, p1, p2, p3 = 0, 0, 0, 0
            
        self.hide() # Esconder esta ventana
        self.final_win = FinalWindow(age, p1, p2, p3) # Abrir la siguiente