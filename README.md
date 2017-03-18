ScholarlyEditingScripts  
=======================

Scripts to help scholars and readers work with textual transcriptions and other digital files.  

# CREDIT:  
For the encoding replacement code (tustepscrub.py), this script is based on Eli Courtwright's answer to the StackOverflow question "Python - Way to recursively find and replace string in text files" (http://goo.gl/enn4ho). Numberremoval.py is currently wholly code created by someone else (viewable here, no author name: http://goo.gl/tePnrO); I need to adapt it to write to file instead of printing in terminal when I have the time.  

# LICENSING:  
Completely free for reuse of any type. Credit to all parties involved appreciated but not required.  

# PURPOSE:  
To remove format encoding and line numbering from a directory of .txt files, creating a clean reading text that can also be used for text analysis (e.g. with Juxta).  

# DIRECTIONS:   
1. These directions assume you have, on your desktop, a folder named TUstepscrub containing both TUstepscrub.py and a folder of your .txt file(s) to be scrubbed named "TUstepfiles". These directions also assume Mac usage (non-Mac users may need to install Python and substitute their command-line program for the Mac terminal).  
2. Open your command-line program (Applications/Utilities/Terminal). Navigate to the text-file folder by typing
	cd Desktop/TUstepscrub
and hitting enter.  
3. Type
	python TUstepscrub.py
and hit enter.  
4. When the script has completed, it will print instructions on how to remove the line numbering from these files.  

# FORMAT ENCODING INCLUDED and CUSTOMIZING THIS SCRIPT:  
This script was developed against the encoded Ulysses reading text edited by Hans Walter Gabler; it removes all of the format encodings I could locate in those files. It may not remove encoding that does not appear in the Ulysses files, but you can easily customize this script to remove additional encodings by reading the code comments farther below.  

# SPECIFIC THINGS REMOVED BY THIS SCRIPT:  
13 format encodings:    
$$$				(centering)    
$$				(new paragraph indent, i.e. pilcrow)    
$ --			(em dash and immediate dialogue)  
@@ } AND @@}	(begin italics)	  
{				(end italics)  
+++				(headings, e.g. Ulysses "Aeolus")  
&:				(encoding used in Ulysses "Sirens")  
**  
$   
{  
}  
_  
  
I still need to edit this script to remove line numbering of the style '001 | Text...'  
