from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Property


def home(request):
    featured = Property.objects.filter(featured=True).order_by("-updated_at")[:6]
    return render(request, "pages/home.html", {"featured": featured})


def listings_page(request):
    qs = Property.objects.all().order_by("-updated_at")

    q = request.GET.get("q", "").strip()
    location = request.GET.get("location", "").strip()
    ptype = request.GET.get("type", "").strip()
    min_beds = request.GET.get("beds", "").strip()
    min_price = request.GET.get("min_price", "").strip()
    max_price = request.GET.get("max_price", "").strip()

    if q:
        qs = qs.filter(title__icontains=q) | qs.filter(location__icontains=q)

    if location:
        qs = qs.filter(location__icontains=location)

    if ptype:
        qs = qs.filter(property_type=ptype)

    if min_beds.isdigit():
        qs = qs.filter(bedrooms__gte=int(min_beds))

    if min_price.isdigit():
        qs = qs.filter(price__gte=int(min_price))

    if max_price.isdigit():
        qs = qs.filter(price__lte=int(max_price))

    paginator = Paginator(qs, 9)  # 9 per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    locations = Property.objects.values_list("location", flat=True).distinct().order_by("location")

    paginator = Paginator(qs, 9)  # 9 per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    context = {
        "properties": page_obj,
        "locations": locations,
        "filters": {
            "q": q,
            "location": location,
            "type": ptype,
            "beds": min_beds,
            "min_price": min_price,
            "max_price": max_price,
        }
    }
    return render(request, "listings/listings.html", context)


def listing_detail(request, slug):
    property_obj = get_object_or_404(Property, slug=slug)
    return render(request, "listings/detail.html", {"property": property_obj})


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, "pages/contact.html")
