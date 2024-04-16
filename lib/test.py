from dotenv import load_dotenv
import os
from flask import Flask
from supabase import create_client
from jwt_functions import create_token , decode_jwt
from flask import request
load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)
app = Flask(__name__)

class Student:
    start = "student"

    @app.post(f"/{start}/log_in")
    def log_in():
        
        # get data from body
        ST_ID =  request.form["ST_ID"]
        Password =  request.form["Password"]
        response = supabase.table("Student").select("*").eq("ST_ID", ST_ID).eq("Password", Password).execute().data

        # check if user exist
        if len(response)==0:
            return  {"Message":"خطا في كلمة المرور أو رقم الطالب"}
        
        data = response[0]
        
        # create jwt token
        token  = create_token(data["ST_ID"],data["F_Name"], data["L_Name"])
        
        # return jwt token to user
        return {"token":token, "first_Name":data["F_Name"] ,"last_Name":data["L_Name"] , "Student_ID": data["ST_ID"] }
        
    
    @app.get(f"/{start}/Home")
    def Home():
        token = request.headers["token"]
        try:
            user = decode_jwt(token)
        except Exception as e:
            return{"Message":"token not found"}

        id = user["user_ID"]
        
        response = supabase.table("Belong").select("Section(SEC_ID, Course(Course_Name,Course_ID))").eq("ST_ID",id).execute().data

        return response

    @app.get(f"/{start}/Course/<Course_ID>")
    def course(Course_ID):
        token = request.headers["token"]
        try:
            user = decode_jwt(token)
        except Exception as e:
            return{"Message":"token not found"}
        id = user["user_ID"]

        response = supabase.table("Attendance_Record")\
            .select(" date , Lecture!inner(LEC_ID , Section!inner(Course!inner(Course_ID)))")\
                .eq("Lecture.Section.Course.Course_ID" , Course_ID)\
                    .eq("ST_ID" , id).execute().data

        return response

    @app.get(f"/{start}/profile")
    def profile():
        token = request.headers["token"]
        try:
            user = decode_jwt(token)
        except Exception as e:
            return{"Message":"token not found"}
        id = user["user_ID"]

        response = supabase.table("Student").select("F_Name , L_Name , Email , Phone_Number").eq("ST_ID",id).execute().data
        return response

class Educator:
    start = "Educator"
    
    @app.post(f"/{start}/log_in")
    def Educator_log_in():
        EDU_ID =  request.form["EDU_ID"]
        Password =  request.form["Password"]
        response = supabase.table("Educator").select("*").eq("EDU_ID", EDU_ID).eq("Password", Password).execute().data

        if len(response)==0:
            return  {"Message":"خطا في كلمة المرور أو رقم المحاضر"}
        
        data = response[0]
        
        token  = create_token(data["EDU_ID"],data["F_Name"], data["L_Name"])
        return {"token":token, "first_Name":data["F_Name"] ,"last_Name":data["L_Name"] , "Educator_ID": data["EDU_ID"] }
        
    @app.get(f"/{start}/Home")
    def Educator_Home():
        token = request.headers["token"]
        try:
            user = decode_jwt(token)
        except Exception as e:
            return{"Message":"token not found"}

        id = user["user_ID"]
        response = supabase.table("Section").select("SEC_ID, Course(Course_Name,Course_ID)").eq("EDU_ID",id).execute().data
        return response

    @app.get(f"/{start}/Course/<Course_ID>")
    def Educator_course(Course_ID):
        token = request.headers["token"]
        try:
            user = decode_jwt(token)
        except Exception as e:
            return{"Message":"token not found"}
        id = user["user_ID"]
        date = request.args.get("date")
        if (date): 
            response = supabase.table("Attendance_Record")\
                .select("Student(ST_ID , F_Name , L_Name) , date \
                    , Time,  Lecture!inner(LEC_ID , Section!inner(Course!inner(Course_ID)))")\
                        .eq("Lecture.Section.Course.Course_ID" , Course_ID)\
                            .eq("Lecture.Section.EDU_ID" , id).eq("date" , date).execute().data
            return response

        response = supabase.table("Attendance_Record").\
            select("Student(ST_ID , F_Name , L_Name) , Time , Lecture!inner(LEC_ID , Section!inner(Course!inner(Course_ID)))")\
                .eq("Lecture.Section.Course.Course_ID" , Course_ID)\
                    .eq("Lecture.Section.EDU_ID" , id).execute().data

        return response

    @app.get(f"/{start}/profile")
    def Educator_profile():
        token = request.headers["token"]
        try:
            user = decode_jwt(token)
        except Exception as e:
            return{"Message":"token not found"}
        id = user["user_ID"]

        response = supabase.table("Educator").select("F_Name , L_Name , Email , Phone_Number , Status").eq("EDU_ID",id).execute().data
        return response
    @app.post(f"/{start}/Change_Status")
    def Change_Status(): 
        token = request.headers["token"]
        try:
            user = decode_jwt(token)
        except Exception as e:
            return{"Message":"token not found"}

        id = user["user_ID"]
        Status = request.args["Status"]
        data = supabase.table('Educator').update({'Status': Status}).eq("EDU_ID", id).execute().data
        return {"Message":"تم التغيير"}


if(__name__ == "__main__"):
    app.run(port=2000)