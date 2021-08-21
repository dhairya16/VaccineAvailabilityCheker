from django.shortcuts import render
import requests
import re

# Create your views here.
def index(request):

	vaccine_data = None

	if request.method == 'POST':
		data = request.POST

		date = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', data['date'])
		pin = data['pin']

		result = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}'.format(pin, date))
		vaccine_data = result.json()

	context = {
		"vaccine_data": vaccine_data,
	}

	return render(request, 'index.html', context)