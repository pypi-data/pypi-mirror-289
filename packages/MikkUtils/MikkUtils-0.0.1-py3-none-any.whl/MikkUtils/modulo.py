import json

def jsonc( lines : list[str] ):
    jsdata = ''
    for t, line in enumerate( lines ):
        line = line.strip()
        if line and line != '' and not line.startswith( '//' ):
            jsdata = f'{jsdata}\n{line}'
    return json.loads( jsdata )
