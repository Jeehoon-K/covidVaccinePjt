from django.shortcuts import render
import vaccinePjt.apps as apps

import vaccinePjt.pfizermodeling as pfm
import vaccinePjt.modernamodeling as mfm

# Create your views here.

def index(request):
    return render(request, 'vaccinePjt/index.html', {})

def select(request):
    return render(request, 'vaccinePjt/select.html', {})

def inputText(request):
    vaccineSelected = request.POST["vaccineSelector"]
    return render(request, 'vaccinePjt/input_text.html', {"vaccineSelected":vaccineSelected})

def result(request):
    vaccineSelected = request.POST["vaccineSelector"]
    textIn = request.POST["textReciever"]

    if vaccineSelected == "pfizer":
        result = pfm.Pfizer_qna(textIn)
    else:
        result = mfm.Moderna_qna(textIn)



    return render(request, 'vaccinePjt/result.html', {"vaccineSelected":vaccineSelected,"textIn":textIn,"result":result})


#def stationPage(request):
#    selected_date = request.POST["selectedDate"]
#    selected_route = request.POST["selectedRoute"]
#
#    df = pd.read_csv("test_web.csv")
#    df = df[df["date"]==selected_date]
#    station_names = list(df[df["bus_route_id"]==int(selected_route)]["station_name"].unique())
#    station_names.sort()

#    return render(request, 'blog/station.html',{"dateInfo":selected_date,"routeInfo":selected_route, "stationList": station_names})

