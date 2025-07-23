# Detección de Fraude en Transacciones con Machine Learning

Este proyecto implementa un modelo de Machine Learning para detectar transacciones fraudulentas basado en datos reales anonimizados. El objetivo es mostrar cómo un sistema automatizado puede ayudar a prevenir fraudes en pagos con tarjeta de crédito.

## Dataset

El conjunto de datos utilizado proviene de [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud), e incluye 284,807 transacciones hechas por titulares de tarjetas europeas en septiembre de 2013. 

- Contiene 492 transacciones fraudulentas.
- Las variables `V1` a `V28` provienen de una reducción de dimensionalidad (PCA) para proteger la privacidad.
- Se conservaron las columnas `Amount` y `Time`, que fueron escaladas con `StandardScaler` durante el preprocesamiento.

---

## Algoritmos Usados

Durante el desarrollo del modelo se probaron múltiples algoritmos. Finalmente, se eligió uno que dio un buen balance entre precisión y sensibilidad:

**Random Forest Classifier** (entrenado con datos balanceados)
-  Métricas evaluadas:
    - **Accuracy**
    - **Precision**
    - **Recall**
    - **F1-score**
    - **Curva ROC-AUC**

El modelo fue entrenado y probado íntegramente en un cuaderno de Jupyter Notebook (`.ipynb`), incluyendo todos los pasos de:

- Análisis exploratorio de datos.
- Preprocesamiento (escalado y balanceo con undersampling).
- Entrenamiento y validación cruzada.
- Evaluación con las métricas anteriores.

---

## 📈 Resultados

El modelo final logró un **buen desempeño**, con métricas balanceadas que permiten detectar la mayoría de fraudes con baja tasa de falsos positivos. Las métricas exactas obtenidas en el conjunto de prueba fueron:

- **Precision:** Alta, lo que significa pocos falsos positivos.
- **Recall:** Alta, lo que significa que detecta la mayoría de los fraudes.
- **F1-score:** Óptimo balance entre precisión y recall.
- **ROC-AUC:** Alto (>0.90), indicando un buen separador entre clases.

> Todas las métricas se calcularon utilizando librerías como `scikit-learn`, `pandas` y `matplotlib` durante las pruebas en Jupyter Notebook.

---

## Visualización Web con Streamlit

Para facilitar la predicción de nuevos casos sin necesidad de código, se implementó una interfaz web interactiva con Streamlit. Esta app permite ingresar los valores de V1 a V28, más el monto y el tiempo de la transacción, y visualizar al instante si se detecta fraude.

### Instrucciones para correr la aplicación

1. Clona el repositorio o descarga los archivos:
* modelo_de_fraude.pkl
* scaler_amount.pkl
* scaler_time.pkl
* app.py
* CUADERNO: project_ML.ipynb

Ejecuta la app con el siguiente comando:
`streamlit run app.py `
### Capturas de app en Streamlit
<img width="781" height="713" alt="Captura de pantalla 2025-07-22 183314" src="https://github.com/user-attachments/assets/cbafb785-a5c7-4630-bf14-0ca8a8c91d67" />
<img width="833" height="798" alt="Captura de pantalla 2025-07-22 183108" src="https://github.com/user-attachments/assets/aee24386-6605-402f-9aa8-de48349d6349" />

