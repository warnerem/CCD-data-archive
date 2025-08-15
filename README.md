# CCD-data-archive

The UMD Observatory has several classes that have collected data on various targets over the years. This project is to make that
data available publically.

Prior work was done by Julianna Reese, CPS-SDU student 2020-21
(Elizabeth: emails are in 
label:work-scholars-2020-21-data_archive  and in 
label:work-observatory-research-data-archive  )

SDU Data Archive (https://docs.google.com/spreadsheets/d/1dNfbGlGUQyahnOnTGAttpAUslrAX1JT_BJZCRbYG-nQ/edit?usp=sharing) my spreadsheet where I was keeping track of our datasets, like which ones had been uploaded, etc. 



I have updated the files to recreate the UMD Astronomy Open House research page, which now pulls data directly from the updated Google Spreadsheet.

To test this locally, you will need to be able to run Python and JavaScript.

Run the importSheet.py script. This will fetch the data from the Google Sheet and populate a local database file named data.db.

Next, run the Flask application by executing app.py. This will start a local web server.

Open a web browser and navigate to the local address provided in your terminal. The main page (template.html) should load automatically.

You should now see the webpage populated with the data from the spreadsheet.

Important: For the webpage to display correctly, you must download the "web" folder and rename it to "openhouse". This ensures that all the links to CSS and other assets are correct.

Please note that this is a work in progress, and aspects of the project may change.

Future Works:

Right now, we are using the HTML in the web/7research file titled templateREAL.html. While this way of doing things is good, it is not ideal. Ideally, having a database backend would be great. Some of the implementation for this could be found in the other template files in the web/7research folder. We would want a backend database as this would both make load times faster as well as make future debugging easier. This is something to look into in the future. The code that I had working with the python files importSheet.py and app.py is made for SQLite and would download the CSV, turn it into a DB, and then turn the DB into a JSON file to be used by the JavaScript. Ideally, if we could get rid of JavaScript from the webpage, that would be great, as some people might not have enabled JavaScript, so the webpage might not function for them without it. Fixing this issue would help with accessibility on the webpage.
