import streamlit as st

st.set_page_config(page_title="Bakterienidentifikation", page_icon="🦠")

pg_home = st.Page("views/home.py", title="Home")
pg_gram_pos = st.Page("views/Gram_positiv.py", title="Gram-positiv", default=True)
pg_gram_neg = st.Page("views/Gram_negativ.py", title="Gram-negativ")
pg_tests = st.Page("views/Testbeschreibung.py", title="Testbeschreibungen")
pg_lernen = st.Page("views/Lernen.py", title="Lernen")
pg_steckbriefe = st.Page("views/Steckbrief.py", title="Steckbriefe")

pg = st.navigation([pg_home, pg_gram_pos, pg_gram_neg, pg_tests, pg_lernen, pg_steckbriefe])
pg.run()
