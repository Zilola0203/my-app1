import streamlit as st
import numpy as np
import pickle

# Trained modelni yuklash (modelni oldindan tayyorlab, pickle yordamida saqlagan bo'lishingiz kerak)
# Bu yerda model.pkl sizning tayyorlangan model faylingiz
with open('model.pkl', 'rb') as file:
     model = pickle.load(file)

# Streamlit interfeys yaratish

st.title("Stress Level Prediction")
st.write("Kiritilgan ma'lumotlar asosida stress darajasini aniqlash")

    # Input formalar
study_hours = st.number_input("Study Hours Per Day", min_value=0.0, max_value=24.0, value=4.0, step=0.5)
extracurricular_hours = st.number_input("Extracurricular Hours Per Day", min_value=0.0, max_value=24.0, value=2.0, step=0.5)
sleep_hours = st.number_input("Sleep Hours Per Day", min_value=0.0, max_value=24.0, value=8.0, step=0.5)
social_hours = st.number_input("Social Hours Per Day", min_value=0.0, max_value=24.0, value=3.0, step=0.5)
physical_activity_hours = st.number_input("Physical Activity Hours Per Day", min_value=0.0, max_value=24.0, value=1.0, step=0.5)
gpa = st.number_input("GPA", min_value=0.0, max_value=4.0, value=3.0, step=0.1)

    # Natijani ko'rsatish uchun tugma
if st.button("Predict Stress Level"):
        # Foydalanuvchi kiritgan ma'lumotlardan massiv yaratish
        inputs = np.array([[study_hours, extracurricular_hours, sleep_hours, social_hours, physical_activity_hours, gpa]])
        
        # Model yordamida bashorat qilish
        result = model.predict(inputs)[0]  # Natijani 0, 1 yoki 2 sifatida qaytaradi
        
        # Hozircha dummy model sifatida ishlatamiz
               
        # Natijani "low", "moderate", yoki "high" ga moslash
        stress_levels = {0: "low", 1: "moderate", 2: "high"}
        stress_level = stress_levels.get(result, "Unknown")

        st.write(f"Predicted Stress Level: {stress_level}")


