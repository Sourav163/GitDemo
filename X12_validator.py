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
