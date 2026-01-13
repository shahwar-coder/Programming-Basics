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
