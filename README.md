# PlannedRoadworks-Viewer
Viewer for planned roadworks based on data supplied fortnightly by Highways England.  
  
This is a map view showing the location of all the planned Roadworks. Clicking one of the Planned Road works will give further information.

## Get the newest dataset

download the latest dataset for planned roadworks from gov.uk site. https://data.gov.uk/dataset/5b3267d8-4307-4eef-a9af-3a4c28224694/planned-road-works-on-the-he-road-network . Place in the public folder of this project.  
  
 Alternatively run the experimental python script
 ```
 python3 getNewestDataset.py
 ```
 This will download to the same directory as the script, and should be copied to public folder of this project.
 
 ## Running

```
node theapp.js
```

starts the server with localport 3001,

## Using viewer

With node server running navigate to http://localhost:3001/planned-rw.html with web browser.

## Filtering
 It is possible to filter to only Planned roadworks active in next 2 weeks, using the select box on the top left of page.
