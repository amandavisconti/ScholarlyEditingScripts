"""
TITLE: TUstepscrub.py
Assembled by: Amanda Visconti (literaturegeek.com)
CREATED: September 29, 2013
CREDIT: For the encoding replacement code, this script is based on Eli Courtwright's answer to the StackOverflow question "Python - Way to recursively find and replace string in text files" (http://goo.gl/enn4ho).

LICENSING: Completely free for reuse of any type. Credit to all parties involved appreciated but not required.

PURPOSE: To remove format encoding and line numbering from a directory of .txt files, creating a clean reading text that can also be used for text analysis (e.g. with Juxta).

DIRECTIONS:
1. These directions assume you have, on your desktop, a folder named TUstepscrub containing both TUstepscrub.py and a folder of your .txt file(s) to be scrubbed named "TUstepfiles". These directions also assume Mac usage (non-Mac users may need to install Python and substitute their command-line program for the Mac terminal).
2. Open your command-line program (Applications/Utilities/Terminal). Navigate to the text-file folder by typing
	cd Desktop/TUstepscrub
and hitting enter.
3. Type
	python TUstepscrub.py
and hit enter.

ENCODING INCLUDED and CUSTOMIZING THIS SCRIPT:
This script was developed against the encoded Ulysses reading text edited by Hans Walter Gabler; it removes all of the format encodings I could locate in those files. It may not remove encoding that does not appear in the Ulysses files, but you can easily customize this script to remove additional encodings by reading the code comments farther below.

SPECIFIC THINGS REMOVED BY THIS SCRIPT:
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
"""

# Import Python library for operating system dependent functionality
import os

# Indicate what you want to replace encodings with
# Current script indicates nothing, which makes the replacement just a deletion
replacement = ""

# Inside the quotation marks, indicate the folder containing the files to search and replace. Path is relative to Desktop/TUstepscrub.
for dname, dirs, files in os.walk("TUstepfiles"):
    for fname in files:
        fpath = os.path.join(dname, fname)
        with open(fpath) as f:
            s = f.read()

# Tell the script the encodings to look for and delete. Certainly some way to do this more compactly when I have the time; right now we're going through each file in the folder for one encoding to delete at a time. Make sure to order encodings using the same symbols (e.g. $$$, $$, and $ from largest to smallest so that they are correctly substituted.

# Delete (replace with empty) this encoding: $$$
        s = s.replace("$$$", replacement)
        with open(fpath, "w") as f:
            f.write(s)
# Delete (replace with empty) this encoding: $$
        s = s.replace("$$", replacement)
        with open(fpath, "w") as f:
            f.write(s)
# Delete (replace with empty) this encoding: $ --
        s = s.replace("$ --", replacement)
        with open(fpath, "w") as f:
            f.write(s)
# Delete (replace with empty) this encoding: @@ }
        s = s.replace("@@ }", replacement)
        with open(fpath, "w") as f:
            f.write(s)
# Delete (replace with empty) this encoding: @@}
        s = s.replace("@@}", replacement)
        with open(fpath, "w") as f:
            f.write(s)
# Delete (replace with empty) this encoding: {
        s = s.replace("{", replacement)
        with open(fpath, "w") as f:
            f.write(s)
# Delete (replace with empty) this encoding: +++
        s = s.replace("+++", replacement)
        with open(fpath, "w") as f:
            f.write(s)
# Delete (replace with empty) this encoding: &:
        s = s.replace("&:", replacement)
        with open(fpath, "w") as f:
            f.write(s)
# Delete (replace with empty) this encoding: **
        s = s.replace("**", replacement)
        with open(fpath, "w") as f:
            f.write(s)
# Delete (replace with empty) this encoding: $
        s = s.replace("$", replacement)
        with open(fpath, "w") as f:
            f.write(s)
# Delete (replace with empty) this encoding: {
        s = s.replace("{", replacement)
        with open(fpath, "w") as f:
            f.write(s)
# Delete (replace with empty) this encoding: }
        s = s.replace("}", replacement)
        with open(fpath, "w") as f:
            f.write(s)
# Delete (replace with empty) this encoding: _
        s = s.replace("}", replacement)
        with open(fpath, "w") as f:
            f.write(s)
            
# To remove an additional encoding, remove the triple-quotation-marks from before and after the five lines of code immediately below, and replace the word _replacethisword_ with the encoding you want removed (keep the quotation marks that are currently around "replacethisword")
"""
        s = s.replace("replacethisword", replacement)
        with open(fpath, "w") as f:
            f.write(s)
"""

print "Success! The format encodings indicated in the script have been removed from your text files. \nYou'll still need to remove any line-numbering from the files. Currently, I only have a script set up to remove line-numbering and print the results into this window, so you'll need to copy and paste the results you'll see in a moment into a new text file. \nTo strip line numbers, type 'python numberremoval.py TUstepfiles/'filename.txt'' below, replacing 'filename.txt' with a filename from /TUstepscrub/Tustepfiles (keeping the single quotes around the filename so the code can handle the spaces and parantheses in the file name) and then pressing enter. \nYou'll need to do this for each file. \nFor the first file, the command you should enter would be python numberremoval.py TUstepfiles/'U-G (01).txt'"

# Line numbering removal: still need to add this. For now, use another utility such as the code the printed instructions above directs you to use (preferred option), or the tool at http://www.gonnalearn.com/code/remove_line_numbers_from_code.htm (this seems to use a PHP script which tries to recognize the format of the line numbering and remove it; I've noticed it is sometimes removing letters/words from the beginning of lines, especially from "Sirens", so you'll want to carefully proofread or locate another tool.)