import streamlit as st

st.set_page_config(page_title="Bakterienidentifikation", page_icon="🦠")

pg_home = st.Page("views/home.py", title="Home")
pg_gram_pos = st.Page("views/unterseite_a.py", title="Gram-positiv", default=True)
pg_gram_neg = st.Page("views/unterseite_b.py", title="Gram-negativ")
pg_tests = st.Page("views/unterseite_c.py", title="Testbeschreibungen")
pg_lernen = st.Page("views/unterseite_d.py", title="Lernen")

pg = st.navigation([pg_home, pg_gram_pos, pg_gram_neg, pg_tests, pg_lernen])
pg.run()
