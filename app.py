import streamlit as st
import pandas as pd

# --- NEW CODE: import and initialize data manager and login manager ---
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

data_manager = DataManager(       # initialize data manager
    fs_protocol='webdav',         # protocol for the filesystem, use webdav for switch drive
    fs_root_folder="Bakterienidentifikationsapp"  # folder on switch drive where the data is stored
    ) 
login_manager = LoginManager(data_manager) # handles user login and registration
login_manager.login_register()             # stops if not logged in
# --- END OF NEW CODE ---

# --- CODE UPDATE: load user data from data manager if not already present in session state --
if 'data_df' not in st.session_state:
    st.session_state['data_df'] = data_manager.load_user_data(
        'data.csv',                     # The file on switch drive where the data is stored
        initial_value=pd.DataFrame(),   # Initial value if the file does not exist
        parse_dates=['timestamp']       # Parse timestamp as datetime
    )
# --- END OF CODE UPDATE ---

pg_home = st.Page("views/home.py", title="Home")
pg_gram_pos = st.Page("views/Gram_positiv.py", title="Gram-positiv", default=True)
pg_gram_neg = st.Page("views/Gram_negativ.py", title="Gram-negativ")
pg_tests = st.Page("views/Testbeschreibung.py", title="Testbeschreibungen")
pg_lernen = st.Page("views/Lernen.py", title="Lernen")
pg_steckbriefe = st.Page("views/Steckbrief.py", title="Steckbriefe")

pg = st.navigation([pg_home, pg_gram_pos, pg_gram_neg, pg_tests, pg_lernen, pg_steckbriefe])
pg.run()