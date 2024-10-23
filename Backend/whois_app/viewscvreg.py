from django.shortcuts import render
from django.http import JsonResponse
import json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from whois.settings import sendResponse, connectDB, disconnectDB

def cv_register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            firstname = data["firstname"]
            lastname = data["lastname"]
            email = data["email"]
            phone = data["phone"]
            # personal_details

            institution = data["institution"]
            graduation_year = data["graduation_year"]
            # education

            degree = data["degree"]
            # degree

            skill = data["skill"]
            # skill

            proficiency = data["proficiency"]
            # proficiency

            company = data["company"]
            job_title = data["job_title"]
            start_date = data["start_date"]
            end_date = data["end_date"]
            # experience

            con = connectDB()
            cur = con.cursor()
            cur.execute(f'''insert into whois.t_person_details(firstname,lastname,email,phone,institution,degree,
                                                            graduation_year,skill,proficiency,company,job_title,start_date,end_date)
                            VALUES('{firstname}')''')
            print('------------------------------------'+fname)
            cur.close()
            con.commit()
            disconnectDB()
            return sendResponse(200, [])
        except Exception as e:
            return sendResponse(200, str(e))




@csrf_exempt
def cvreg(request):
    if request.method == "POST":
        try:
            jsons = json.loads(request.body)
        except json.JSONDecodeError:
            action = "wrong json"
            data = []
            result = sendResponse(404, data, action)
            return JsonResponse(json.loads(result))
        if 'action' in jsons:
            action = jsons['action']
            if action == "cv_register":
                result = cv_register(request)
                return JsonResponse(json.loads(result))
            else:
                action = "action not found"
                data = []
                result = sendResponse(404, data, action)
                return JsonResponse(json.loads(result))

        else:
            action = "no action"
            data = []
            result = sendResponse(404, data, action)
            return JsonResponse(json.loads(result))
    else:
        action = "method buruu"
        data = []
        result = sendResponse(405, data, action)
        return JsonResponse(json.loads(result))
