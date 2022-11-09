from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Debate,UserProfile,DebateList
from .serializer import DebetSerializer,DebateListSerializer

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



class readDebateList (APIView):
    def get(self,request):
        try:
            getAllDebateList=DebateList.objects.filter(is_approved=True,is_deleted=False)
            if getAllDebateList.exists():
                serializerData=DebateListSerializer(getAllDebateList,many=True)
                return Response(serializerData.data,status=status.HTTP_200_OK)

            return Response({"message":"Data Not Available"})

        except Exception as e:
            return Response({"exception":str(e)},status=status.HTTP_400_BAD_REQUEST)



class PostNewDebate(APIView):
    def post(self,request):
        try:
            data=request.data
            debateTopic=data.get("debateTopic")
            debateDescription=data.get("debateDescription")

            if not debateTopic or not debateDescription :
                return Response ({"message":"Key Mising"},status=status.HTTP_200_OK)
                

            createDebate=DebateList.objects.create(DebateTopic=debateTopic,description=debateDescription)
            serilizer=DebateListSerializer(createDebate)
            return Response(serilizer.data,status=status.HTTP_200_OK)


        except Exception as e :
            return Response({"exception":str(e)},status=status.HTTP_400_BAD_REQUEST)
