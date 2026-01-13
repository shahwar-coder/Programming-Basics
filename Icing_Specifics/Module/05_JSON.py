# ============================================================
# json module in Python — Backend Expert Perspective
# ============================================================

import json

# JSON is the PRIMARY data format in backend systems:
# - REST APIs (request / response bodies)
# - Config files
# - Inter-service communication
# - Caching (Redis)
# - Logging structured data

# ============================================================
# 1. MOST FREQUENTLY USED METHODS (CORE 4)
# ============================================================

# 1️⃣ json.loads()  → JSON STRING → Python object
# Used when:
# - API receives JSON payload
# - Reading JSON from message queue
# - Reading JSON stored as text

json_string = '{"id": 1, "name": "Rahul", "active": true}'
data = json.loads(json_string)
# Result: dict

# ------------------------------------------------------------

# 2️⃣ json.dumps() → Python object → JSON STRING
# Used when:
# - Sending API response
# - Writing logs
# - Storing JSON in DB / cache

response = {
    "status": "success",
    "data": data
}

json_response = json.dumps(response)

# Common backend options:
json.dumps(response, ensure_ascii=False)
json.dumps(response, indent=2)
json.dumps(response, separators=(",", ":"))

# ------------------------------------------------------------

# 3️⃣ json.load()   → JSON FILE → Python object
# Used when:
# - Reading config files
# - Bootstrapping application settings

with open("config.json", "r") as f:
    config = json.load(f)

# ------------------------------------------------------------

# 4️⃣ json.dump()   → Python object → JSON FILE
# Used when:
# - Writing config
# - Exporting data
# - Creating snapshots

with open("output.json", "w") as f:
    json.dump(response, f, indent=2)


# ============================================================
# 2. BACKEND-CRITICAL OPTIONS (YOU MUST KNOW)
# ============================================================

# ------------------------------------------------------------
# indent → readability (logs, debugging)
json.dumps(response, indent=4)

# ------------------------------------------------------------
# ensure_ascii → unicode handling
json.dumps({"name": "शहवार"}, ensure_ascii=False)

# ------------------------------------------------------------
# separators → compact JSON (network optimization)
json.dumps(response, separators=(",", ":"))

# ------------------------------------------------------------
# sort_keys → deterministic output (testing, caching)
json.dumps(response, sort_keys=True)


# ============================================================
# 3. HANDLING NON-JSON TYPES (VERY IMPORTANT)
# ============================================================

from datetime import datetime

payload = {
    "user": "Rahul",
    "created_at": datetime.now()
}

# ❌ This will fail:
# json.dumps(payload)

# ✅ Solution 1: default serializer
def serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")

json.dumps(payload, default=serializer)

# ✅ Solution 2 (simpler, common)
json.dumps(payload, default=str)


# ============================================================
# 4. JSON ↔ PYTHON TYPE MAPPING (INTERVIEW FAVORITE)
# ============================================================

# JSON        → Python
# object      → dict
# array       → list
# string      → str
# number      → int / float
# true/false  → True / False
# null        → None


# ============================================================
# 5. VALIDATION & SAFETY (BACKEND REALITY)
# ============================================================

# NEVER trust incoming JSON blindly

def validate_user(data):
    required_keys = {"id", "name"}
    if not required_keys.issubset(data):
        raise ValueError("Invalid payload")

incoming = json.loads(json_string)
validate_user(incoming)


# ============================================================
# 6. JSON IN APIs (FastAPI / Django concept)
# ============================================================

"""
# Incoming request
payload = request.json()        # already parsed JSON → dict

# Outgoing response
return JsonResponse(payload)    # framework uses json.dumps internally
"""

# ============================================================
# 7. JSON vs dict (COMMON CONFUSION)
# ============================================================

# dict → in-memory Python structure
# JSON → text format for transport/storage

# json.dumps(dict) → JSON string
# json.loads(string) → dict


# ============================================================
# 8. PERFORMANCE & BEST PRACTICES
# ============================================================

# ✔ Use separators to reduce payload size
# ✔ Avoid indent in production APIs
# ✔ Serialize dates explicitly
# ✔ Validate input
# ✔ Log structured JSON
# ✔ Use sort_keys for caching & tests


# ============================================================
# 9. WHEN NOT TO USE json MODULE
# ============================================================

# - Heavy analytics → use pandas
# - Schema validation → use pydantic / marshmallow
# - Binary data → use base64 or other formats


# ============================================================
# 10. MENTAL MODEL (KEY TAKEAWAY)
# ============================================================

# json module is NOT about files.
# It is about:
# ✔ serialization (Python → JSON)
# ✔ deserialization (JSON → Python)
# ✔ safe data exchange between systems
