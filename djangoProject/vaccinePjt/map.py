import pandas as pd
import datetime
import numpy as np
import plotly.express as px
import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls


def mapping():

    df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv", 
                    usecols = ["location","iso_code","date","total_vaccinations"])

    df = df[df["location"] != "World"]

    df.fillna(method="ffill",inplace=True)

    df.reset_index(drop=True,inplace=True)

    str_min_date = df["date"].min()


    df["date"] = df["date"].apply(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d"))

    min_date = df["date"].min()
    max_date = df["date"].max()

    country_list = list(dict.fromkeys(zip(df["location"],df["iso_code"])))

    for i in country_list:

        date_temp = min_date
        country_df = df[df["location"]==i[0]]
        country_min = country_df["date"].min()
        country_max = country_df["date"].max()
        vaccine_max = int(country_df[df["date"]==country_max]["total_vaccinations"])

        while date_temp <= max_date:
            if date_temp < country_min:
                df.loc[len(df)] = [i[0],i[1],date_temp,0]
            elif date_temp > country_max:
                df.loc[len(df)] = [i[0],i[1],date_temp, vaccine_max]
            else:
                if date_temp not in country_df["date"].unique():
                    df.loc[len(df)] = [i[0],i[1],date_temp, np.nan]

            date_temp += datetime.timedelta(days=1)

    df.fillna(method="ffill",inplace=True)
    df.reset_index(drop=True,inplace=True)

    df = df.sort_values(by=["location","date"]).reset_index(drop=True)

    people = df[df["date"]==max_date]["total_vaccinations"].sum()
    country = len(df["location"].unique())
    
    days = (max_date - min_date).days
    ppd = round(int(people)/int(days),1)


    df["date"] = df["date"].apply(lambda x: str(x)[:10])


    fig = px.scatter_geo(df, locations="iso_code", locationmode="ISO-3",
                         size="total_vaccinations", 
                         hover_name="location",
                         animation_frame="date",
                         animation_group="location",
                         range_color=[833471,833471],
                          width=1200, height=900)
    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 10
    fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 10
    fig.update_layout({
        "plot_bgcolor": "rgba(0,0,0,0)",
        "paper_bgcolor": "rgba(0,0,0,0)"
    })
    fig.update_layout(geo=dict(bgcolor= 'rgba(0,0,0,0)'))

    username = 'sue-bin' # your username
    api_key = 'A9iEh0PmfbcEmki2cptp' # your api key - go to profile > settings > regenerate key
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

    a = py.plot(fig, filename = 'tempp', auto_open=False)

    iframe = tls.get_embed(a, height = "100%")

    return str_min_date, iframe, people, country, ppd
