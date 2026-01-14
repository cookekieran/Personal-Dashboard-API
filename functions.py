def get_news():
    news_list = []
    data = response.json()
    articles = data['news']['articles']

    for article in articles:
        news_dict = {
            "source": article['source']['name'],
            "author": article['author'],
            "url": article['url'],
            "title": article['title'],
            "publish time": datetime.fromisoformat(article['publishedAt'])
        }
        news_list.append(news_dict)

    # sort by date published (newest first)
    news_list.sort(key=lambda x: x["publish time"], reverse=True)

    return news_list


def get_fred():
    data_dict = {}
    all_dates = set()
    raw_json = response.json()
    macro_data = raw_json["macro"]

    for data in macro_data.values():
        for obs in data["observations"]:
            all_dates.add(obs["date"])

    all_dates = sorted(all_dates)
    date_index = {date: i for i, date in enumerate(all_dates)}
    
    data_dict["date"] = pd.to_datetime(all_dates)

    for macro_metric in macro_data.keys():
        data_dict[macro_metric] = [None] * len(all_dates) # intalise null
        observations = macro_data[macro_metric]["observations"]

        for obs in observations:
            idx = date_index[obs["date"]]
            value = obs["value"]
            data_dict[macro_metric][idx] = pd.to_numeric(value, errors = "coerce")
    
    df = pd.DataFrame(data_dict)

    return df