"""
data = 데이터 불러오고
"""
from sqlalchemy import create_engine, text
from pandasql import sqldf
import pandas as pd
from utils.database import engine

def get_institution(institution:str):
    query = """
    SELECT *
    FROM institution_table
    WHERE institution = :institution
    """
    with engine.connect() as con:
        res = con.execute(text(query),{"institution": institution})
        rows = res.fetchall()
    return [dict(row._mapping) for row in rows]
