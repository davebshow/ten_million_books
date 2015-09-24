import pandas as pd
from fuzzywuzzy import fuzz


def group_by_dist_basic(csvfile, col):
    csv = pd.read_csv(csvfile).fillna("")
    output = []
    for x in range(len(csv)):
        token = csv.ix[x][col]
        if token:
            results = []
            results.append(token)
            csv.ix[x][col] = ""
            for y in range(len(csv)):
                token2 = csv.ix[y][col]
                if token2:
                    dist = fuzz.ratio(token, token2)
                    if dist >= 80:
                        results.append(token2)
                        csv.ix[y][col] = ""
            output.append(pd.Series(results))
    return output


def group_by_dist(csvfile, col, col2):
    csv = pd.read_csv(csvfile).fillna("")
    output = []
    for x in range(len(csv)):
        token = csv.ix[x][col]
        if token:
            ref_token = csv.ix[x][col2]
            results = []
            results.append((x, token))
            csv.ix[x][col] = ""
            for y in range(len(csv)):
                token2 = csv.ix[y][col]
                if token2:
                    ref_token2 = csv.ix[y][col2]
                    if ref_token == ref_token2:
                        dist = fuzz.ratio(token, token2)
                        if dist >= 80:
                            results.append((y, token2))
                            csv.ix[y][col] = ""
            output.append(pd.Series(results))
    return output


def assign(csv, output):
    pass
