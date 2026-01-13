'''
Q1. What is the purpose of the json module in Python?
A.
The json module is used to convert data between Python objects and JSON format.
It enables safe data exchange between systems, especially in backend APIs.
'''
# Example:
# Python dict → JSON string
# json.dumps({"id": 1, "name": "Rahul"})
#
# JSON string → Python dict
# json.loads('{"id": 1, "name": "Rahul"}')


'''
Q2. What is the difference between json.loads() and json.load()?
A.
json.loads() parses JSON from a STRING,
while json.load() parses JSON from a FILE.
'''
# Example:
# json.loads('{"a": 1}')        # from string
#
# with open("data.json") as f:
#     json.load(f)              # from file


'''
Q3. What is the difference between json.dumps() and json.dump()?
A.
json.dumps() converts a Python object into a JSON STRING,
while json.dump() writes JSON directly into a FILE.
'''
# Example:
# s = json.dumps({"x": 10})
#
# with open("out.json", "w") as f:
#     json.dump({"x": 10}, f)


'''
Q4. Why is json.dumps() commonly used in backend APIs?
A.
Because APIs must send responses as JSON text over the network.
json.dumps() serializes Python data into JSON format for transmission.
'''
# Example:
# response = {"status": "ok", "data": [1, 2, 3]}
# return json.dumps(response)   # API response body


'''
Q5. What happens if json.dumps() encounters a non-JSON type?
A.
json.dumps() raises a TypeError because JSON supports only limited data types.
Custom serialization is required for unsupported types like datetime.
'''
# Example:
# json.dumps({"time": datetime.now()})   # ❌ TypeError
#
# json.dumps({"time": datetime.now()}, default=str)  # ✅ works


'''
Q6. What is the difference between a Python dict and JSON?
A.
A dict is an in-memory Python data structure,
while JSON is a text-based data format used for storage and communication.
'''
# Example:
# data = {"a": 1}               # Python dict
# json_text = json.dumps(data)  # JSON string
# back_to_dict = json.loads(json_text)


# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================


'''
Q1. Why is JSON the default data format in REST APIs and microservices?
A.
Because JSON is language-independent, lightweight, human-readable,
and natively supported by almost all backend and frontend systems.
'''
# Example:
# Client sends:
# POST /api/user
# Body: {"id": 1, "name": "Rahul"}
#
# Server:
# data = json.loads(request_body)


'''
Q2. Why should indent be avoided in production API responses?
A.
Because indentation increases payload size and network cost.
In production, compact JSON improves performance.
'''
# Example:
# ❌ Development (readable)
# json.dumps(data, indent=4)
#
# ✅ Production (compact)
# json.dumps(data, separators=(",", ":"))


'''
Q3. Why is sort_keys=True important for caching and testing?
A.
It ensures deterministic JSON output, which is critical for:
- cache keys
- snapshot tests
- hashing
'''
# Example:
# json.dumps({"b": 2, "a": 1}, sort_keys=True)
# Output: {"a":1,"b":2}


'''
Q4. Why is validating incoming JSON mandatory in backend systems?
A.
Because incoming JSON is untrusted user input.
Without validation, it can cause crashes, security issues, or corrupted data.
'''
# Example:
# payload = json.loads(request_body)
# if "id" not in payload:
#     raise ValueError("Invalid request")


'''
Q5. How does JSON serialization relate to ML / AI systems?
A.
ML systems exchange data (features, predictions, embeddings)
using JSON between services, models, and pipelines.
'''
# Example:
# Model output sent as JSON:
# json.dumps({
#   "embedding": [0.12, 0.98, -0.33],
#   "confidence": 0.91
# })


'''
Q6. Why is json.dumps(default=str) commonly used but risky?
A.
It prevents crashes by converting unknown objects to strings,
but it may silently hide bugs or lose semantic meaning.
'''
# Example:
# json.dumps({"time": datetime.now()}, default=str)
# Output: {"time": "2026-01-07 21:15:00.123456"}
# ⚠️ Better: explicit ISO format for APIs
