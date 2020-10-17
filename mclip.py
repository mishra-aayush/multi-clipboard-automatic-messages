# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 07:27:25 2020

Project: Multi-Clipboard Automatic Messages

@author: AAYUSH MISHRA
"""

text = {
'informal': 
"""
Dear XYZ,
Random Text Here.
Regards,
Aayush Mishra
""",
'formal':
"""
Respected XYZ,
Random Text Here.
Sincerely,
Aayush Mishra,
17ucs001
""",
'casual':
"""
What's good homie?
Random Text Here.
See you around,
Aayush
"""
}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Might be missing keyphrase')
    print('Usage: Python mclip.py [keyphrase]')
    sys.exit()

# 1st command line argument is keyphrase
keyphrase = sys.argv[1]

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print('Message for ' + keyphrase + ' copied!')
else:
    print('No such keyphrase exists')
