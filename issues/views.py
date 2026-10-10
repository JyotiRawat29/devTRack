from django.shortcuts import render

# Create your views here.
from issues.models import Reporter,Issue, CriticalIssue, LowPriorityIssue
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
from typing import override
from django.http import JsonResponse   

ISSUE_FILE_PATH = "issues/files/issues.json"
REPORTER_FILE_PATH = "issues/files/reporters.json"

class ReporterView(APIView):
    def __get_all_reporters(self):
        with open(REPORTER_FILE_PATH, "r") as file:
            return json.loads(file.read())
    @override
    def get(self,request):
        report_id = request.GET.get('id')
        reporters = self.__get_all_reporters()
        if report_id is not None:
            try:
                report_id = int(report_id)
            except ValueError:
                return JsonResponse({"error": "id must be an integer"}, status=400)
            for repo in reporters:
                if report_id == repo["id"]:
                    return JsonResponse(repo,status=200)
            return JsonResponse({"error": "Reporter not found"}, status=404)
        return Response(reporters)
    @override
    def post(self, request):
        data = request.data
        reports = self.__get_all_reporters()
        repo =  {
            "id": len(reports)+1,
            "email": data["email"],
            "name": data["name"],
            "team": data["team"]        
        }
        with open(REPORTER_FILE_PATH,"w") as file :
            reports.append(repo)
            json.dump(reports,file, indent = 4)
        return JsonResponse(repo, status=status.HTTP_201_CREATED)


class IssueView(APIView):
    def __get_all_issues(self): #private method
        with open(ISSUE_FILE_PATH,"r")as file:
            return json.loads(file.read())
    @override
    def post(self, request):
        data = request.data
        if data['priority'] == 'critical':
            issue = CriticalIssue(**data)
        elif data['priority'] == 'low':
            issue = LowPriorityIssue(**data)
        else:
            issue = Issue(**data)
        issue.validate()
        response_data = issue.to_dict()
        response_data['message'] = issue.describe()
        tasks = self.__get_all_issues()
        print("response_data", response_data)
        with open(ISSUE_FILE_PATH,"w") as file :
             tasks.append(response_data)
             json.dump(tasks,file, indent = 4)
        return JsonResponse(response_data, status=201)

    @override
    def get(self,request):
        issue_status = request.GET.get('status')
        issue_id = request.GET.get('id')
        issues = self.__get_all_issues()
        
        if issue_id is not None:
            try:
                issue_id = int(issue_id)
            except:
                raise ValueError({"error": "id value not valid integer"}, status=400)
            for issue in issues:
                if issue["id"] == issue_id:
                    return JsonResponse(issue, status=200)
            return JsonResponse({"error": "Issue not found"}, status=404)
        
        if issue_status is not None:
            matching_issues = [issue for issue in issues if issue["status"] == issue_status]
            if not matching_issues:
                return JsonResponse({"error": "No issues found with that status"},status=404)
            return JsonResponse({"issues": matching_issues}, status=200)
        return (Response(issues))
                
 

