import streamlit as st
import json
import os

JSON_FILE = "output.json"

# Load JSON into session_state if not already loaded
if "data" not in st.session_state:
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            st.session_state.data = json.load(f)
    else:
        st.session_state.data = []

if "index" not in st.session_state:
    st.session_state.index = 0

st.title("Arabic Medical Term Annotation")

# Current term
if len(st.session_state.data) == 0:
    st.warning("No terms found in JSON.")
    st.stop()

current_item = st.session_state.data[st.session_state.index]
st.subheader(f"Term {st.session_state.index + 1} / {len(st.session_state.data)}")
st.write(current_item["ArabicCommon"])

# Input for Darja
daja_annotation = st.text_input("Enter Darja translation:", current_item.get("Darja", ""))

# Save annotation directly into session_state AND write to output.json immediately
if st.button("Save Annotation"):
    st.session_state.data[st.session_state.index]["Darja"] = daja_annotation
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(st.session_state.data, f, ensure_ascii=False, indent=2)
    st.success("Annotation saved to output.json!")

# Navigation
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Previous") and st.session_state.index > 0:
        st.session_state.index -= 1
with col2:
    if st.button("Next") and st.session_state.index < len(st.session_state.data) - 1:
        st.session_state.index += 1
with col3:
    if st.button("Reset"):
        st.session_state.index = 0

# Download updated JSON (optional, same as the file)
st.download_button(
    "Download Updated JSON",
    data=json.dumps(st.session_state.data, ensure_ascii=False, indent=2),
    file_name="annotated_output.json",
    mime="application/json"
)
