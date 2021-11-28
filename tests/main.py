import http
from typing import Optional

from squall import Path, Query, Squall
from squall.params import Num, Str

app = Squall()


@app.add_api("/api_route")
def non_operation():
    return {"message": "Hello World"}


def non_decorated_route():
    return {"message": "Hello World"}


app.add_api_route("/non_decorated_route", non_decorated_route)


@app.get("/text")
def get_text():
    return "Hello World"


@app.get("/path/{item_id}")
def get_id(item_id):
    return item_id


@app.get("/path/str/{item_id}")
def get_str_id(item_id: str):
    return item_id


@app.get("/path/int/{item_id}")
def get_int_id(item_id: int):
    return item_id


@app.get("/path/float/{item_id}")
def get_float_id(item_id: float):
    return item_id


@app.get("/path/param/{item_id}")
def get_path_param_id(item_id: Optional[str] = Path(None)):
    return item_id


@app.get("/path/param-required/{item_id}")
def get_path_param_required_id(item_id: str = Path(...)):
    return item_id


@app.get("/path/param-minlength/{item_id}")
def get_path_param_min_len(item_id: str = Path(..., valid=Str(min_len=3))):
    return item_id


@app.get("/path/param-maxlength/{item_id}")
def get_path_param_max_len(item_id: str = Path(..., valid=Str(max_len=3))):
    return item_id


@app.get("/path/param-min_maxlength/{item_id}")
def get_path_param_min_max_len(
    item_id: str = Path(..., valid=Str(max_len=3, min_len=2))
):
    return item_id


@app.get("/path/param-gt/{item_id}")
def get_path_param_gt(item_id: float = Path(..., valid=Num(gt=3))):
    return item_id


@app.get("/path/param-gt0/{item_id}")
def get_path_param_gt0(item_id: float = Path(..., valid=Num(gt=0))):
    return item_id


@app.get("/path/param-ge/{item_id}")
def get_path_param_ge(item_id: float = Path(..., valid=Num(ge=3))):
    return item_id


@app.get("/path/param-lt/{item_id}")
def get_path_param_lt(item_id: float = Path(..., valid=Num(lt=3))):
    return item_id


@app.get("/path/param-lt0/{item_id}")
def get_path_param_lt0(item_id: float = Path(..., valid=Num(lt=0))):
    return item_id


@app.get("/path/param-le/{item_id}")
def get_path_param_le(item_id: float = Path(..., valid=Num(le=3))):
    return item_id


@app.get("/path/param-lt-gt/{item_id}")
def get_path_param_lt_gt(item_id: float = Path(..., valid=Num(lt=3, gt=1))):
    return item_id


@app.get("/path/param-le-ge/{item_id}")
def get_path_param_le_ge(item_id: float = Path(..., valid=Num(le=3, ge=1))):
    return item_id


@app.get("/path/param-lt-int/{item_id}")
def get_path_param_lt_int(item_id: int = Path(..., valid=Num(lt=3))):
    return item_id


@app.get("/path/param-gt-int/{item_id}")
def get_path_param_gt_int(item_id: int = Path(..., valid=Num(gt=3))):
    return item_id


@app.get("/path/param-le-int/{item_id}")
def get_path_param_le_int(item_id: int = Path(..., valid=Num(le=3))):
    return item_id


@app.get("/path/param-ge-int/{item_id}")
def get_path_param_ge_int(item_id: int = Path(..., valid=Num(ge=3))):
    return item_id


@app.get("/path/param-lt-gt-int/{item_id}")
def get_path_param_lt_gt_int(item_id: int = Path(..., valid=Num(lt=3, gt=1))):
    return item_id


@app.get("/path/param-le-ge-int/{item_id}")
def get_path_param_le_ge_int(item_id: int = Path(..., valid=Num(le=3, ge=1))):
    return item_id


@app.get("/query")
def get_query(query):
    return f"foo bar {query}"


@app.get("/query/optional")
def get_query_optional(query=None):
    if query is None:
        return "foo bar"
    return f"foo bar {query}"


@app.get("/query/int")
def get_query_type(query: int):
    return f"foo bar {query}"


@app.get("/query/int/optional")
def get_query_type_optional(query: Optional[int] = None):
    if query is None:
        return "foo bar"
    return f"foo bar {query}"


@app.get("/query/int/default")
def get_query_type_int_default(query: int = 10):
    return f"foo bar {query}"


@app.get("/query/param")
def get_query_param(query=Query(None)):
    if query is None:
        return "foo bar"
    return f"foo bar {query}"


@app.get("/query/param-required")
def get_query_param_required(query=Query(...)):
    return f"foo bar {query}"


@app.get("/query/param-required/int")
def get_query_param_required_type(query: int = Query(...)):
    return f"foo bar {query}"


@app.get("/enum-status-code", status_code=http.HTTPStatus.CREATED)
def get_enum_status_code():
    return "foo bar"
