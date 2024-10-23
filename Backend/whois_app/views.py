from django.shortcuts import render
from django.http import JsonResponse
import json
import psycopg2
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from whois.settings import sendResponse, connectDB, disconnectDB


def getPerson(request):
            jsons = json.loads(request.body)
            pid=jsons['pid']
            action=jsons['action']
            con = connectDB()
            cur = con.cursor()





            query=f'''SELECT 
    json_build_object(
        'firstname', p.firstname,
        'lastname', p.lastname,
        'headline', p.headline,
        'address', p.address,
        'phone', p.phone,
        'email', null, -- Имэйл талбар байхгүй тул null байна
        'linkedin', p.linkedin,
        'github', p.github,
        'facebook', p.facebook,
        'city', p.city,
        'summary', p.summary
    ) AS person_details,
    json_agg(
        json_build_object(
            'degree', d.degree,
            'institution', e.institution,
            'location', e.location,
            'start_year', e.start_year,
            'graduation_year', e.graduation_year,
            'description', e.description
        )
    ) AS education,
    json_agg(
        json_build_object(
            'job_title', j.job_title,
            'company', ex.company,
            'location', ex.location,
            'start_date', ex.start_date,
            'end_date', ex.end_date,
            'responsibilities', ex.responsibilities
            )
    ) as experience
FROM 
    whois.t_person_details p
INNER JOIN 
    whois.t_education e 
ON 
    p.pid = e.pid
INNER JOIN
    whois.t_degree d 
ON
    e.did = d.did
INNER JOIN
    whois.t_experience ex
ON
    ex.pid = p.pid
INNER JOIN 
    whois.t_job j
ON  
    j.jid = ex.jid

    
    
WHERE 
    p.pid = {pid}  -- динамик pid ашиглана
GROUP BY 
    p.pid;  -- p.pid дээр групп хийж байна

;


                    '''

            cur.execute(query)
            columns = cur.description
            respRow = [{columns[index][0]:column for index, 
                column in enumerate(value)} for value in cur.fetchall()]

            print(f'----------------------------------------{respRow}')
            cur.close()
            disconnectDB(con)
            data = respRow
            result = sendResponse(200, data, action)
            return result

def cv_register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            fname = data['firstname']
            con = connectDB()
            cur = con.cursor()
            cur.execute(f'''insert into whois.t_person_details(firstname)
                            VALUES('{fname}')''')
            print('------------------------------------'+fname)
            cur.close()
            con.commit()
            disconnectDB()
            respRow = {'kakak': 'sa'}
            return sendResponse(200, respRow)
        except Exception as e:
            return e


@csrf_exempt
def home(request):
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
            elif action == "getPerson":
                result = getPerson(request)
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
