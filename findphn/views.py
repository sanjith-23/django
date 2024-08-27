from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
import phonenumbers
from phonenumbers import timezone,carrier,geocoder
# Create your views here.

def findNumber(request):
    return render(request,'findNumber.html')

class FindNumberAPI(APIView):
    def post(self,request,*args, **kwargs):
        number=request.data.get('mobile_number')

        if not number:
            raise serializers.ValidationError("Mobile Number is Not Provide.")
        
        try:
            phone=phonenumbers.parse(number)
        except Exception as e:
            raise serializers.ValidationError("Please provide a valid Number.")
        
        if not phone:
            raise serializers.ValidationError("Please provide a valid Number.")
        
        tz=timezone.time_zones_for_number(phone)
        service_provider=carrier.name_for_valid_number(phone,'en')
        region=geocoder.description_for_valid_number(phone,'en')

        return Response({
            'country_code':phone.country_code,
            'mobile_number':phone.national_number,
            'timezone':tz,
            'service_provider':service_provider,
            'country':region,
        })
        

class FindPhoneNumberInText(APIView):
    def post(self,request,*args, **kwargs):
        mobile_numbers=[]
        user_text=request.data.get('find_number')

        for match in phonenumbers.PhoneNumberMatcher(user_text,''):
            mobile_numbers.append(phonenumbers.format_number(match.number,phonenumbers.PhoneNumberFormat.E164))
        return Response({
            'mobile_numbers':mobile_numbers,
        })