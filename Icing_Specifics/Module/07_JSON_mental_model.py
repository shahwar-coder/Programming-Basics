'''
Personal mental model:
- `s` , means string is involved.
- no `s`, file is involved not str
- load menas something we are bringing/loading in python setup so we would need python object here.
- dumps means we are taking something away from python setup so away from python object.

# -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x

- loads() -> str involved -> bringing to python setup -> "Json String to Python Object"
- dumps() -> str involved -> taking away from python setup -> "Python Object to Json String"
- load() -> file involved -> bringing to python setup -> "File to Python Object"
- dump() -> file involved -> taking away from python setup -> "Python Object to File"

- file is json file
'''

# JSON Mental Model (Quick Recall)

# ---- STRING vs FILE ----
# "s"  -> string
# no s -> file

# ---- json.loads() ----
# JSON STRING  -> Python object
# Use when data comes from:
#   - API response
#   - request body
#   - hardcoded JSON text

# ---- json.dumps() ----
# Python object -> JSON STRING
# Use when:
#   - sending data over network
#   - logging / printing JSON
#   - storing JSON in memory (not file)

# ---- json.load() ----
# JSON FILE -> Python object
# Use when:
#   - reading from .json file on disk

# ---- json.dump() ----
# Python object -> JSON FILE
# Use when:
#   - writing data to .json file

# ---- One-line memory hook ----
# loads  = load string
# dumps  = dump string
# load   = load file
# dump   = dump file
