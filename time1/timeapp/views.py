from django.http import HttpResponse
from datetime import datetime,timedelta

def myfunc(request):
    ct = datetime.now()
    bt = ct-timedelta(hours=4)
    at = ct+timedelta(hours=4)

    response_content = (
        f"Current time is {ct}\n"
        f"Before time is {bt}\n"
        f"Ahead time is {at}\n"
    )
    return HttpResponse(response_content,content_type='text/plain')