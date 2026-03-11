"""
data = 데이터 불러오고
"""
from sqlalchemy import create_engine, text
from pandasql import sqldf
import pandas as pd
from utils.database import engine

def load_csv_to_table():
    df = pd.read_csv("data/institution_kpi_table.csv")
    df.to_sql("institution_table", engine, index=False, if_exists="replace")

def get_institution(institution:str):
    query = """
    SELECT * FROM df
    WHERE institution = :institution
    """
    with engine.connect() as con:
        res = con.execute(text(query),{"institution": institution})
        rows = res.fetchall()
    return [dict(row._mapping) for row in rows]