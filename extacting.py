import streamlit as st
import json

# Load JSON data
JSON_FILE = "output.json"
with open(JSON_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

st.title("Arabic Medical Term Annotation")

# Use session_state to keep track of current index
if "index" not in st.session_state:
    st.session_state.index = 0

# Show current ArabicCommon term
current_item = data[st.session_state.index]
st.subheader(f"Term {st.session_state.index + 1} / {len(data)}")
st.write(current_item["ArabicCommon"])

# Input for Darja annotation
daja_annotation = st.text_input("Enter Darja translation:", current_item.get("Darja", ""))

# Save annotation to session_state
if st.button("Save Annotation"):
    data[st.session_state.index]["Darja"] = daja_annotation
    st.success("Annotation saved!")

# Navigation buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Previous") and st.session_state.index > 0:
        st.session_state.index -= 1
with col2:
    if st.button("Next") and st.session_state.index < len(data) - 1:
        st.session_state.index += 1
with col3:
    if st.button("Reset"):
        st.session_state.index = 0

# Download updated JSON
st.download_button(
    "Download Updated JSON",
    data=json.dumps(data, ensure_ascii=False, indent=2),
    file_name="annotated_output.json",
    mime="application/json"
)
