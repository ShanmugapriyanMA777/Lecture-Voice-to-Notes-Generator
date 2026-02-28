import streamlit as st
import speech_recognition as sr

st.title("🎙 Lecture Voice-to-Notes Generator")

def simple_summarizer(text):
    sentences = text.split(".")
    summary = ". ".join(sentences[:3])
    return summary

uploaded_file = st.file_uploader("Upload Audio File (WAV format)", type=["wav"])

if uploaded_file is not None:
    recognizer = sr.Recognizer()

    with sr.AudioFile(uploaded_file) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)

        st.subheader("📄 Transcribed Text")
        st.write(text)

        if len(text) > 50:
            summary = simple_summarizer(text)

            st.subheader("📝 Summary")
            st.write(summary)
        else:
            st.warning("Text too short for summarization.")

    except Exception as e:
        st.error("Error processing audio file")
