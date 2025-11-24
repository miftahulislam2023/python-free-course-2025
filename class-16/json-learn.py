import json

# Python Object থেকে JSON String (Serialization)
data = {
    "name": "Abir", 
    "active": True,
    "score": None
}

json_string = json.dumps(data) 
print(json_string)

# JSON ফাইল থেকে Python Object (Deserialization)
with open("class-16/github-api-json.json", "r") as f:
    github = json.load(f)
    # এখন এটি সাধারণ ডিকশনারির মতো ব্যবহার করা যাবে
    # print(github)
    print(type(github))
