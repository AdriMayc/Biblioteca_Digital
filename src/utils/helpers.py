import inspect
import io
import sys

def call_and_capture(fn, *args, **kwargs):
    if fn is None:
        return None, "Função não encontrada."
    old_stdout = sys.stdout
    buf = io.StringIO()
    sys.stdout = buf
    try:
        result = fn(*args, **kwargs)
    except Exception as e:
        result = None
        print(f"Erro ao executar: {e}")
    sys.stdout = old_stdout
    printed = buf.getvalue()
    return result, printed

def safe_invoke(fn, from_fields):
    if fn is None:
        return None, "Função não disponível."
    sig = None
    try:
        sig = inspect.signature(fn)
    except Exception:
        return call_and_capture(fn)
    params = [p for p in sig.parameters.values() if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)]
    n = len(params)
    try:
        if n == 0:
            return call_and_capture(fn)
        else:
            args = []
            for i in range(n):
                if i < len(from_fields):
                    v = from_fields[i]
                    if isinstance(v, str) and v.isdigit():
                        args.append(int(v))
                    else:
                        args.append(v)
                else:
                    args.append(None)
            return call_and_capture(fn, *args)
    except TypeError as e:
        return None, f"TypeError: {e}"
    except Exception as e:
        return None, f"Erro: {e}"