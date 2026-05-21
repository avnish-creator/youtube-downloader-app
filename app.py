import streamlit as st
import yt_dlp
import os

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AvnishLab Downloader",
    page_icon="🎥",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
    color: white;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #38BDF8;
}

.subtitle {
    text-align: center;
    color: #CBD5E1;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
    "<div class='title'>🎥 AvnishLab Downloader</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Professional YouTube Video Downloader</div>",
    unsafe_allow_html=True
)

# ---------------- INPUT ----------------

url = st.text_input("Enter YouTube Video URL")

# ---------------- DOWNLOAD ----------------

if st.button("⬇ Download Video"):

    if url:

        with st.spinner("Downloading Video..."):

            try:

                output_path = "downloads"

                os.makedirs(output_path, exist_ok=True)

                ydl_opts = {
                                'outtmpl': f'{output_path}/%(title)s.%(ext)s',
                                'format': 'best',
                                'quiet': True,
                                'nocheckcertificate': True,
                                'ignoreerrors': False,
                                'no_warnings': True,
                                'http_headers': {
                                    'User-Agent': 'Mozilla/5.0'
                                }
                            }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)

                    filename = ydl.prepare_filename(info)

                st.success("Download Completed Successfully!")

                with open(filename, "rb") as file:
                    st.download_button(
                        label="📥 Download File",
                        data=file,
                        file_name=os.path.basename(filename),
                        mime="video/mp4"
                    )

            except Exception as e:
                st.error(str(e))

    else:
        st.warning("Please enter a YouTube URL")

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
    "<center>Powered by Avnish Ojha 🚀</center>",
    unsafe_allow_html=True
)