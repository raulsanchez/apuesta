from django.http import HttpResponse

def inicio(request):
	html = "<html><body>Example</body></html>"
	return HttpResponse(html)