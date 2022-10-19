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
        try:
            data=request.data
            listUserData=data["user_ids"].split(",")
            userProfileData=UserProfile.objects.filter(id__in=listUserData)

            created_debate=Debate.objects.create(topic_id=data["topic"])
            created_debate.users.set(userProfileData)    # added many to many field by using set method 
            # created_debate.users.add(userProfileData[0])   # adding single user object in many to many field 

            serializer=DebetSerializer(created_debate)

            return Response(serializer.data)

        except Exception as e:
            return Response({"message":str(e)})



    

    