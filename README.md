# album-engineers-webscraper
Hallwood started looking to sign engineers now and wanted to look for engineers that have worked new albums. Thus, I made a webscraper that (with the Jaxsta link to the album) will display the Engineer with the Album name following it. It will also organize it to cumulate the albums an engineer has worked on and display it in a list on the CSV file "final.csv". It is relatively simple and was made while I was still updating the original credits sheet, so it isn't as advanced. Most likely has hacks that I haven't realized just yet, such as maybe only working for the certain web format Jaxsta has, but it gives the result.

### My Messy Organization (Jaxsta Album Engineers)

1. check_repeat_names.py: this file organizes the engineers.csv data into the final.csv data set
2. csv_writer.py: this file is everything used to write the actual CSV files
3. webscrapper.py: this file is what runs the program and does the webscrapping
