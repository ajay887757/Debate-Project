from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Debate,UserProfile
from .serializer import DebetSerializer

# Create your views here.


class debateInfo(APIView):
    def get(self,request):
        allData=Debate.objects.all()
        serializedData=DebetSerializer(allData,many=True)
        # alluserDataOfFirstObjects=allData[0].users.all()
        return Response(serializedData.data)

    def post(self,request):
        data=request.data
        listUserData=data["user_ids"].split(",")
        userProfileData=UserProfile.objects.filter(id__in=listUserData)

        created_debate=Debate.objects.create(topic_id=data["topic"])
        created_debate.users.set(userProfileData)    # added many field by using set method 

        return Response(data)



    

    