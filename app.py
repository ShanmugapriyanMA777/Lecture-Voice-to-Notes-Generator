
import streamlit as st
import speech_recognition as sr
from transformers import pipeline

st.title("🎙 Lecture Voice-to-Notes Generator")

# Load summarizer model
summarizer = pipeline("summarization")

uploaded_file = st.file_uploader("Upload Audio File (WAV format)", type=["wav"])

if uploaded_file is not None:
    recognizer = sr.Recognizer()

    with sr.AudioFile(uploaded_file) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        st.subheader("📄 Transcribed Text")
        st.write(text)

        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)

        st.subheader("📝 Summary")
        st.write(summary[0]['summary_text'])

    except Exception as e:
        st.error("Error processing audio file")
