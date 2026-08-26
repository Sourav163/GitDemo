from pathlib import Path
from pyx12 import x12n_document
from pyx12.params import params
from pyx12.error_handler import errh_null


def validate_x12(path: str):
    edi = Path(path).read_text(encoding="utf-8")

    p = params()
    errors = errh_null()

    result = x12n_document.x12n_document(
        p,
        edi,
        errors,
    )

    return result


result = validate_x12("claim.edi")
print(result)



import pyx12
import inspect
from pyx12 import x12n_document

print(pyx12.__version__)
print(inspect.signature(x12n_document.x12n_document))



from io import StringIO

from pyx12 import x12n_document
from pyx12.params import params
from pyx12.error_handler import errh_null


edi = open("claim.edi", "r", encoding="utf-8").read()

p = params()
err_handler = errh_null()

fd_edi = StringIO(edi)
fd_html = StringIO()

result = x12n_document.x12n_document(
    p,
    fd_edi,
    err_handler,
    fd_html,
)

print(result)
