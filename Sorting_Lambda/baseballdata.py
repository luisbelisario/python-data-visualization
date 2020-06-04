import csv


def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    table = []
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(
            csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            table.append(row)
    return table


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(
            csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
    return table


MINIMUM_AB = 500


def batting_average(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the batting average as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return hits / at_bats
    else:
        return 0


def onbase_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the on-base percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    walks = float(batting_stats[info["walks"]])
    if at_bats >= MINIMUM_AB:
        return (hits + walks) / (at_bats + walks)
    else:
        return 0


def slugging_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the slugging percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    doubles = float(batting_stats[info["doubles"]])
    triples = float(batting_stats[info["triples"]])
    home_runs = float(batting_stats[info["homeruns"]])
    singles = hits - doubles - triples - home_runs
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return (singles + 2 * doubles + 3 * triples + 4 * home_runs) / at_bats
    else:
        return 0


def filter_by_year(statistics, year, yearid):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      year       - Year to filter by
      yearid     - Year ID field in statistics
    Outputs:
      Returns a list of batting statistics dictionaries that
      are from the input year.
    """
    year_list = []
    for row in statistics:
        if int(row[yearid]) == year:
            year_list.append(row)
    return year_list


def top_player_ids(info, statistics, formula, numplayers):
    """
    Inputs:
      info       - Baseball data information dictionary
      statistics - List of batting statistics dictionaries
      formula    - function that takes an info dictionary and a
                   batting statistics dictionary as input and
                   computes a compound statistic
      numplayers - Number of top players to return
    Outputs:
      Returns a list of tuples, player ID and compound statistic
      computed by formula, of the top numplayers players sorted in
      decreasing order of the computed statistic.
    """
    list1 = []
    list2 = []
    for row in statistics:
        id_player = row[info['playerid']]
        computed_stats = formula(info, row)
        tuple1 = tuple((id_player, computed_stats))
        list1.append(tuple1)

    list1.sort(key=lambda value: value[1], reverse=True)
    for tuple_id in list1:
        if numplayers > 0:
            list2.append(tuple(tuple_id))
            numplayers -= 1
        else:
            break
    return list2


def lookup_player_names(info, top_ids_and_stats):
    """
    Inputs:
      info              - Baseball data information dictionary
      top_ids_and_stats - list of tuples containing player IDs and
                          computed statistics
    Outputs:
      List of strings of the form "x.xxx --- FirstName LastName",
      where "x.xxx" is a string conversion of the float stat in
      the input and "FirstName LastName" is the name of the player
      corresponding to the player ID in the input.
    """
    list = []
    info_dict = read_csv_as_nested_dict(
        info['masterfile'], info['playerid'], info['separator'], info['quote'])
    for index in top_ids_and_stats:
        formatted_string = format(index[1], '.3f') + " --- {0} {1}".format(info_dict[index[0]][info['firstname']],
                                                                           info_dict[index[0]][info['lastname']])
        list.append(formatted_string)
    return list


def compute_top_stats_year(info, formula, numplayers, year):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
      year        - Year to filter by
    Outputs:
      Returns a list of strings for the top numplayers in the given year
      according to the given formula.
    """
    list1 = read_csv_as_list_dict(info['battingfile'],
                                  info['separator'],
                                  info['quote']
                                  )
    filtered_by_year = filter_by_year(list1,
                                      year,
                                      info['yearid'])
    top_players = top_player_ids(info, filtered_by_year, formula, numplayers)
    return lookup_player_names(info, top_players)


def aggregate_by_player_id(statistics, playerid, fields):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      playerid   - Player ID field name
      fields     - List of fields to aggregate
    Output:
      Returns a nested dictionary whose keys are player IDs and whose values
      are dictionaries of aggregated stats.  Only the fields from the fields
      input will be aggregated in the aggregated stats dictionaries.
    """
    dict1 = {}
    dict2 = {}
    for row in statistics:
        if row[playerid] not in dict1:
            dict2[playerid] = row[playerid]
            for field in fields:
                dict2[field] = int(row[field])
            dict1[row[playerid]] = dict(dict2)
        else:
            for field in fields:
                dict1[row[playerid]][field] += int(row[field])
    return dict1


def compute_top_stats_career(info, formula, numplayers):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
    """
    list_stats = []
    aggregated_stats = aggregate_by_player_id(read_csv_as_list_dict(info['battingfile'], info['separator'], info['quote']),
                                              info['playerid'],
                                              info['battingfields'])
    for value in aggregated_stats.values():
        list_stats.append(value)
    return lookup_player_names(info, top_player_ids(info, list_stats, formula, numplayers))


def test_baseball_statistics():
    """
    Simple testing code.
    """
    baseballdatainfo = {"masterfile": "Master_2016.csv",
                        "battingfile": "Batting_2016.csv",
                        "separator": ",",
                        "quote": '"',
                        "playerid": "playerID",
                        "firstname": "nameFirst",
                        "lastname": "nameLast",
                        "yearid": "yearID",
                        "atbats": "AB",
                        "hits": "H",
                        "doubles": "2B",
                        "triples": "3B",
                        "homeruns": "HR",
                        "walks": "BB",
                        "battingfields": ["AB", "H", "2B", "3B", "HR", "BB"]}

    print("Top 5 batting averages in 1923")
    top_batting_average_1923 = compute_top_stats_year(
        baseballdatainfo, batting_average, 5, 1923)
    for player in top_batting_average_1923:
        print(player)
    print("")

    print("Top 10 batting averages in 2010")
    top_batting_average_2010 = compute_top_stats_year(
        baseballdatainfo, batting_average, 10, 2010)
    for player in top_batting_average_2010:
        print(player)
    print("")

    print("Top 10 on-base percentage in 2010")
    top_onbase_2010 = compute_top_stats_year(
        baseballdatainfo, onbase_percentage, 10, 2010)
    for player in top_onbase_2010:
        print(player)
    print("")

    print("Top 10 slugging percentage in 2010")
    top_slugging_2010 = compute_top_stats_year(
        baseballdatainfo, slugging_percentage, 10, 2010)
    for player in top_slugging_2010:
        print(player)
    print("")

    # You can also use lambdas for the formula
    #  This one computes onbase plus slugging percentage
    print("Top 10 OPS in 2010")
    top_ops_2010 = compute_top_stats_year(baseballdatainfo,
                                          lambda info, stats: (onbase_percentage(info, stats) +
                                                               slugging_percentage(info, stats)),
                                          10, 2010)
    for player in top_ops_2010:
        print(player)
    print("")

    print("Top 20 career batting averages")
    top_batting_average_career = compute_top_stats_career(
        baseballdatainfo, batting_average, 20)
    for player in top_batting_average_career:
        print(player)
    print("")


# Make sure the following call to test_baseball_statistics is
# commented out when submitting to OwlTest/CourseraTest.

# test_baseball_statistics()
