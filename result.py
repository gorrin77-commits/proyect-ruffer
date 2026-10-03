from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from config import *

class FinalWindow(QWidget):
    def __init__(self, age, p1, p2, p3):
        super().__init__()
        
        # --- 1. GUARDAR LOS DATOS QUE VIENEN DE LA OTRA VENTANA ---
        self.age = age
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        # --- 2. CONFIGURACIÓN BÁSICA DE LA VENTANA ---
        self.setWindowTitle(TXT_RESULT_TITLE)
        self.resize(WIN_WIDTH, WIN_HEIGHT)
        self.move(WIN_X, WIN_Y)

        # --- 3. CÁLCULOS (Llamamos a las funciones de abajo) ---
        rufier_index = self.calculate_rufier()
        performance_text = self.evaluate_performance(rufier_index)

        # --- 4. CREACIÓN DE LOS TEXTOS EN PANTALLA (LABELS) ---
        # Juntamos el texto de tus constantes con los resultados calculados
        self.lbl_index = QLabel(f"{TXT_INDEX}{rufier_index}")
        self.lbl_performance = QLabel(f"{TXT_WORKOUT}{performance_text}")

        # --- 5. DISEÑO VERTICAL (LAYOUT) Y ACOMODAR ELEMENTOS ---
        self.main_layout = QVBoxLayout()
        
        # Añadimos los textos y los centramos en la pantalla
        self.main_layout.addWidget(self.lbl_index, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.lbl_performance, alignment=Qt.AlignCenter)
        
        # Le decimos a la ventana que use este diseño vertical
        self.setLayout(self.main_layout)

        # --- 6. MOSTRAR LA VENTANA ---
        self.show()


    # --- FUNCIONES DE LÓGICA Y MATEMÁTICAS ---

    # Fórmula matemática para calcular el índice de Rufier
    def calculate_rufier(self):
        resultado = (4 * (self.p1 + self.p2 + self.p3) - 200) / 10
        return resultado

    # Sistema de condiciones (if/elif) para evaluar la condición física según la edad
    def evaluate_performance(self, index):
        # Si es demasiado pequeño
        if self.age < 7:
            return "No hay datos para menores de 7 años"
        
        # Mayores de edad y adolescentes de 15 años o más
        if self.age >= 15:
            if index >= 15: return "Bajo"
            elif index >= 11: return "Satisfactorio"
            elif index >= 6: return "Promedio"
            elif index >= 0.5: return "Por encima del promedio"
            else: return "Alto"
            
        # Jóvenes de 13 y 14 años
        elif self.age >= 13:
            if index >= 16.5: return "Bajo"
            elif index >= 12.5: return "Satisfactorio"
            elif index >= 7.5: return "Promedio"
            elif index >= 2: return "Por encima del promedio"
            else: return "Alto"
            
        # Niños de 11 y 12 años
        elif self.age >= 11:
            if index >= 18: return "Bajo"
            elif index >= 14: return "Satisfactorio"
            elif index >= 9: return "Promedio"
            elif index >= 3.5: return "Por encima del promedio"
            else: return "Alto"
            
        # Niños de 9 y 10 años
        elif self.age >= 9:
            if index >= 19.5: return "Bajo"
            elif index >= 15.5: return "Satisfactorio"
            elif index >= 10.5: return "Promedio"
            elif index >= 5: return "Por encima del promedio"
            else: return "Alto"
            
        # Niños de 7 y 8 años
        else: 
            if index >= 21: return "Bajo"
            elif index >= 17: return "Satisfactorio"
            elif index >= 12: return "Promedio"
            elif index >= 6.5: return "Por encima del promedio"
            else: return "Alto"
