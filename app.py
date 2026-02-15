import sqlite3 
from langchain_openai import ChatOpenAI 
import streamlit as st 
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.messages import SystemMessage , HumanMessage ,AIMessage 
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableLambda , RunnableParallel , RunnableBranch
import os
from dotenv import load_dotenv 
import pandas as pd 
load_dotenv()

llm = ChatOpenAI(model="gpt-5-mini")

con = sqlite3.connect("database.db" , check_same_thread=False)
cursor = con.cursor() 

st.title("AI-SQL Database Assistant")
st.write("Ask any question related to data base and if you want to quit type either quit or exit ")

user = st.text_input("Ask a question: ")

if user :
    if user.lower() in ["quit","exit"]:
        st.stop()
    template = ChatPromptTemplate.from_messages([
        ("system","You are a SQLite expert. Convert user question into a valid SQLite SQL query. Only return the SQL query. The table name is 'orders'."),
        ("human","{user}")
    ])

    chain = template | llm | StrOutputParser() 
    sql_query  = chain.invoke({"user":user})

    st.subheader("Generated SQL Query:")
    st.code(sql_query) 

    try :
        cursor.execute(sql_query)
        rows =cursor.fetchall()
        st.subheader("Query Result:")

        if rows :
            coulumn_names = [docs[0] for docs in cursor.description] 
            df = pd.DataFrame(rows , columns = coulumn_names)
            st.dataframe(df)
        else:
            st.write("No results found.")
    except Exception as e:
        st.write("Error executing SQL query: ", e)