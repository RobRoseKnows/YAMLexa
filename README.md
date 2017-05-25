# alexa-tools
This is just a dump of tools/scripts I've made to use while developing alexa skills. You're welcome to add to it if you want.  

When you add a new tool, please add documentation in the README for what it does and how to use it.

# Tools
## convertToJSON.py
This is a tool I built that takes a list of slot items and converts them into the new slot format used by the new Intent Builder. To use it, create a file with slot items separated by line breaks. The file should be in plaintext and should have no file type as per the usual conventions found for Slot Types in the Alexa Skills Kit examples. Then run the script, passing in the name of the file. 

You'll get a JSON object that you then paste into the code editor in the types array.
