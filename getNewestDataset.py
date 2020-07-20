#attempt obtain the newest dataset from the gov.uk site
#assume is titled 'Highways England road network - {d} {m} {y}
#{d} = single and double digit day of month
#{m} = month as a word
#{y} = 4 digit year

import urllib.request

def go():
    site = "https://data.gov.uk/dataset/5b3267d8-4307-4eef-a9af-3a4c28224694/planned-road-works-on-the-he-road-network"
    contents = urllib.request.urlopen(site).read()
    print(type(contents))
    contents = contents.decode("utf-8") 
    findfirst = "<a data-ga-event=\"download\" data-ga-format=\"CSV\" data-ga-publisher=\"highways-england\" class=\"govuk-link\" href=\""
    d = contents.find(findfirst)+len(findfirst)
    print(d)
    dd = contents[d:].find("\"") + d
    print(dd)
    thef = contents[d:dd]
    print(thef)

    #now download the xmlfile
    with urllib.request.urlopen(thef) as f:
             xml = f.read().decode('utf-8')
             print(xml)
             text_file = open(thef[thef.rfind("/")+1:], "w")
             text_file.write(xml)
             text_file.close()







go()
