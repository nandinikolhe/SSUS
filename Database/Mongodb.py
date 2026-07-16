from pymongo import MongoClient

try:
    MONGO_URI="mongodb+srv://nandinikolhe7803_db_user:GB4s2XzHJWHWBTYc@cluster0.cbl7z9e.mongodb.net/?appName=Cluster0"
    
    client= MongoClient(MONGO_URI)
    
    client.admin.command("ping")
    db=client["SSUS"]
    
    students_collection= db["students"]
    marks_collection= db["marks"]
    attendance_collection= db["attendance"]
    bmi_collection=db["bmi_reports"]
    
    print("MongoDB Connected Sucessfully")
    
except Exception as e:
    print("MongoDB Error:", e)