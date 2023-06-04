from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

#retriving all the real_estate lisitngs as a list
def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings":listings
    }
    return render(request,"listings.html",context)


#retriving one real_estate lisitng
def listing_retrive(request,pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing":listing
    }
    return render(request,"listing.html",context)


#Create to accept new real estate lisitng
def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form":form
    }
    return render(request,"listing_create.html",context)


#Update an existing listing  
def listing_update(request,pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == "POST":
        form = ListingForm(request.POST,instance=listing,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form":form
    }
    return render(request,"listing_update.html",context)


#delete a exiting lisitng
def listing_delete(request,pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")