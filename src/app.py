import streamlit as st
import tempfile
import os

from main import analyze_file_with_ai


st.set_page_config(page_title="AI Log Analyzer", layout="centered")

st.title("🤖 AI Log Analyzer")
st.write("Upload any log, txt, csv, excel or json file to generate AI error report.")

uploaded_file = st.file_uploader(
    "Upload your file",
    type=["log", "txt", "csv", "xlsx", "json"]
)

if uploaded_file:
    file_ext = os.path.splitext(uploaded_file.name)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    if st.button("Analyze File"):
        with st.spinner("🔍 Analyzing file with AI..."):
            try:
                summary = analyze_file_with_ai(temp_path)

                st.success("✅ Analysis Completed")

                st.text_area("AI Summary Report", summary, height=300)

                os.makedirs("output", exist_ok=True)
                report_path = "output/ai_summary_report.txt"

                with open(report_path, "w", encoding="utf-8") as f:
                    f.write(summary)

                with open(report_path, "rb") as f:
                    st.download_button(
                        "⬇ Download Summary Report",
                        f,
                        file_name="ai_log_summary.txt",
                        mime="text/plain"
                    )

            except Exception as e:
                st.error(str(e))

    os.remove(temp_path)
