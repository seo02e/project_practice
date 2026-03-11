from fastapi import status, Path, Body
from fastapi.responses import JSONResponse
from services.post import get_institution
from services.post import get_institution_info
from services.post import get_avg_salary
from services.post import get_hiring
from services.post import get_ratio
from services.post import get_health 
from services.post import get_risk
# from services.post import get_quik

def get_dashboard_controller(institution:str):
    try:
        inst = get_institution(institution)
        inst_info = get_institution_info(institution)
        avg_sal = get_avg_salary(institution)
        hiring = get_hiring(institution)
        ratio = get_ratio(institution)
        health = get_health(institution)
        risk = get_risk(institution)
        #quik = get_quik(institution)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "조회 성공",
                "data": {
                    "institution": inst,
                    "institution_info": inst_info,
                    "avg_salary": avg_sal,
                    "hiring": hiring,
                    "ratio": ratio,
                    "health": health,
                    "risk": risk
                }
            })
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": "조회 실패",
                "error": str(e)
            }
        )

