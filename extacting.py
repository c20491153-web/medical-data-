# import json

# # Load the whole JSON file
# with open("processed_common.json", "r", encoding="utf-8") as f:
#     data = json.load(f)

# # Write each object on one line
# with open("output.json", "w", encoding="utf-8") as f:
#     for obj in data:
#         f.write(json.dumps(obj, ensure_ascii=False))
#         f.write(",\n")
import streamlit as st
import json
import os

# File paths
JSON_FILE = r"C:/Users/ayadi/Desktop/medical tems/output.json"

UPDATED_FILE = "output_annotated.json"

# Load JSON data
if os.path.exists(UPDATED_FILE):
    with open(UPDATED_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

# Initialize session state
if "index" not in st.session_state:
    st.session_state.index = 0

# Current term
if st.session_state.index < len(data):
    current_item = data[st.session_state.index]
    st.write(f"**Arabic term:** {current_item['ArabicCommon']}")
    
    # Input for Darja translation
    darja_input = st.text_input("Enter Darja term", key=st.session_state.index)
    
    # Button to save and go to next
    if st.button("Save & Next"):
        data[st.session_state.index]["Darja"] = darja_input
        st.session_state.index += 1
        # Save updated JSON
        with open(UPDATED_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        st.experimental_rerun()
else:
    st.success("All terms annotated!")
    st.write("You can download the annotated file below:")
    st.download_button(
        "Download JSON",
        json.dumps(data, ensure_ascii=False, indent=2),
        file_name="output_annotated.json",
        mime="application/json"
    )
