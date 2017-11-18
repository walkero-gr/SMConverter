# SMConverter
SMConverter helps you to convert the session file of the Firefox addon [Session Manager by Michael Kraft](https://addons.mozilla.org/en-US/firefox/addon/session-manager/ "Session Manager") to a plain txt file.

The script is written in python, so you must have it installed in your system. The script opens the session file in read only mode, so it won't overwrite it, unless you give the same file name in the same path. **So take care**.

If the user doesn't provide an output file, then the new created file will have the same name with input file, adding the '**_export**' text at the end. In this new file you will find all the URLs, seperated by line change.

If you want to import these URLs to Firefox or Chrome, you can use an import addon, like the tabs2txt ([Firefox](https://addons.mozilla.org/en-US/firefox/addon/tabs2txt/ "tabs2txt for Firefox"), [Chrome](https://chrome.google.com/webstore/detail/tabs2txt/jaobckfgmoejmffgmlllfohadijkicgf "tabs2txt for Chrome")). Also you may use an addon to close all the duplicate tabs, like [FoxyTab](https://addons.mozilla.org/en-US/firefox/addon/foxytab/). 

## Usage
Open a terminal and run the script using 
```bash
python smconverter.py [options]
```

#### Options
```bash
-h              Shows the help text and these options
-v|--verbose    Returns more info in the output
-i|--ifile      The input file from Session Manager
-o|--ofile      The output file with the list of the url.
                CAUTION: Currently the script overrides the file, if it exists
```
