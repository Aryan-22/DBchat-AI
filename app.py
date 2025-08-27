import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

st.set_page_config(page_title="Chat with SQL with DB")
st.title("DB_chat")

LOCAL_DB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"
radio_opt = ["Use SQLLite 3 Database - HERO.db","Connect to your SQL DataBase"]

selected_opt = st.sidebar.radio(label = "Choose the DB with which you want to chat",options= radio_opt)
if radio_opt.index(selected_opt) == 1:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("Provide My SQL Host")
    mysql_user = st.sidebar.text_input("MYSQL user")
    mysql_password = st.sidebar.text_input("MYSQL password",type = "password")
    mysql_db = st.sidebar.text_input("MySQL database")

else:
    db_uri = LOCAL_DB

api_key = st.sidebar.text_input(label = "GROQ API KEY",type = "password")
if not db_uri:
    st.info("Please enter database information and uri")

if not api_key:
    st.info("Please add the groq api key")

##LLM
llm = ChatGroq(api_key=api_key,model_name = "Llama-8b-8192",streaming=True)

@st.cache_resource(ttl = "2h")
def configure_db(db_uri,mysql_host = None,mysql_user = None,mysql_password = None,mysql_db = None):
    if db_uri == LOCAL_DB:
        db_file_path = (Path(__file__).parent / "student.db").absolute()
        print(db_file_path)
        creator = lambda: sqlite3.connect(f"file:{db_file_path}?mode=ro",uri = True)
        return SQLDatabase(create_engine("sqlite:///",creator= creator))
    
    elif db_uri == MYSQL:
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("Please  provide all MySQL connection details.")
            st.stop()
            return SQLDatabase(create_engine(f"mysql+mysqlconnector://{my_user}:{mysql_password}@{mysql_host}/{mysql_db}"))

if db_uri == MYSQL:
    db = configure_db(db_uri,mysql_host,mysql_user,mysql_password,mysql_db)
else:
    db = configure_db(db_uri)


#toolkit