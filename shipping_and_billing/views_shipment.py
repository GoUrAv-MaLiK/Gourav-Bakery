from django.http.response import HttpResponse
import shipping_and_billing
from django.shortcuts import render, redirect
from django.views import View
from .models import Shipping_detail 
from django.views.decorators.csrf import csrf_exempt
from paytm import Checksum

MERCHANT_KEY= '%Pj9XV91Tpc_267F';

# Create your views here.
def Shipping_and_billing(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        last_name=request.POST.get('last_name','')
        address=request.POST.get('address1','')+ " " + request.POST.get('address2','')
        email=request.POST.get('email','')
        state=request.POST.get('state','')
        zip=request.POST.get('zip','')
        mobile_number=request.POST.get('mobile_number','')
        item_json=request.POST.get('item_json')
        order=Shipping_detail(name=name,item_Json=item_json,address=address,    state=state,email=email,mobile_number=mobile_number,zip=zip) 
        order.save()
        thank=True
        id=order.order_id

        paytmParams = {

                'requestType': 'Payment',
                'MID': 'NvuQhy57403134872925',
                'ORDER_ID': str(order.order_id),
                'txnAmount': str(500),
                'custId': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'websiteName': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'callbackUrl':'http://127.0.0.1:8000/handlepayment/',

        }
        paytmParams['CHECKSUMHASH'] = Checksum.generateSignature(paytmParams, MERCHANT_KEY)
        print("generateSignature Returns:" + str(paytmParams))
        paytmChecksum = paytmParams['CHECKSUMHASH']
        isVerifySignature = Checksum.verifySignature(paytmParams, MERCHANT_KEY,paytmChecksum)
        if isVerifySignature:
	        print("Checksum Matched")
        else:
	        print("Checksum Mismatched")

        m='NvuQhy57403134872925'
        o=str(order.order_id)
        return render(request,'shipping_and_billing/paytm.html',{'paytmParams':paytmParams,
         'order': o,
         'mid' : m,
        })

    return render(request,'shipping_and_billing/shipment.html')

@csrf_exempt
def handlepayment(request):
    return HttpResponse('Done')
