from fastapi import status, Path, Body
from fastapi.responses import JSONResponse
from services.post import get_institution as get_institution_service


def get_institution_controller(institution:str = Path):
    try:
        result = get_institution_service(institution)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "조회 성공",
                "data": result
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": "조회 실패",
                "error": str(e)
            }
        )
