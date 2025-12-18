from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Contact
# Create your views here.



def add_to_db(request):
	if request.method == "POST":
		name 	= request.POST.get("name")
		email 	= request.POST.get("email")
		phone_no= request.POST.get("phone_no")
		content 	= request.POST.get("content")

		cont = Contact(name=name, email=email, phone_no=phone_no, content=content)
		try:
			cont.full_clean()
			cont.save()
			messages.success(request, "Your Contacts had been Saved successfully!")
			return redirect("/#")
			
		except ValidationError as e:
			for field,errors in e.message_dict.items():
				for error in errors:
					messages.error(request, f"{field}: {error}", extra_tags='danger')
				return redirect("/#")
	messages.success(request, "Welcome to my Portfolio!")
	return render(request,"home.html")