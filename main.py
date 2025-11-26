from fastapi import FastAPI,UploadFile,File
import uvicorn
import csv
from apliceision import Soldier
import sqlite3
app = FastAPI()
result = []
@app.post("/assignWithCsv")
def get_file(file: UploadFile = File()):
    if not "csv" in file.content_type:
        return {"msg": f"content_type: `{file.content_type}` not allowed!"}
with open('Hayal_No_Status.csv', 'r', encoding='utf-8') as file:
    reader =  csv.DictReader(file)
    for rows in reader:
     
        print(rows)
        soldier = Soldier(rows["soder_nomber"],rows["first_name"], rows["last_name"], rows["gender"], rows["city"], rows["distance"])
        result.append(soldier)
    
           
            

    
                     
    if __name__ == "__main__":
        uvicorn.run(app)
          