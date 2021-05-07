import json
from django.shortcuts import render
from datetime import datetime
import requests
now = datetime.now()



# Create your views here.
# api_key= '16000001c1b6ba6e216778b178995cd094afc373'
# trafficapi_url = 'https://bin.mapletrack.com/aaa.php?page=Stats&ts_id=21&date=12&group1=287&group2=288&group3=1&date_s=2021-05-06&date_e=2021-05-06&timezone=-5:00&api_key=16000001c1b6ba6e216778b178995cd094afc373'

# plugrush='https://admin.plugrush.com/api/v2/campaigns?email=dinoevolution%40gmail.com&hash=5cb82c7cf82d2a12a33c117fcba9178d65f9ca13ab9726ccaa49f634f074d684&timestamp=1620360612'

def revenue_data():
    res = requests.get('https://bin.mapletrack.com/aaa.php?page=Stats&ts_id=21&date=12&group1=287&group2=282&group3=1&date_s=2021-05-06&date_e=2021-05-06&timezone=-5:00&api_key=16000001c1b6ba6e216778b178995cd094afc373')
    response = res.content.decode('utf8').replace("","")
    data = json.loads(response)
    s = json.dumps(data, indent=4,sort_keys=True)
    return data

# def plugrushapi():
#     res = requests.get('https://admin.plugrush.com/api/v2/stats/advertiser/websites?email=dinoevolution%40gmail.com&hash=b50f4dc32eabed086149dde5b9c8722f65005487aff7be234756f5406d4e030c&timestamp=1620372608&campaigns=%7840119&limit=0&offset=0&fbclid=IwAR1_VVkz7qetiWGq_TjR_6j2Uu29MPQjMbNjgQ1HW4P51dg9lEOYD09m7jQ')
#     response = res.content.decode('utf8').replace("","")
#     data = json.loads(response)
#     print(data)
#     s = json.dumps(data, indent=4,sort_keys=True)
#     return data    

def home(request):   
    data_traffic =revenue_data()
    # data_plugrush = plugrushapi()

    # revenue = []
    # r = len(data.revenue)
    # print(r)
    # for i in range(0,r):
    #     a = data.revenue
    #     revenue.append(a)
    # cost = data.cost
    # print(revenue)
    context={
        'data_traffic': data_traffic
    }
    return render(request, 'network/home.html',context)
