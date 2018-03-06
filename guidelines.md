# Technical writing style guide

Some initial thoughts/pointers. This is a starting point and is open
for discussion.

## Overview

My suggestion would be to obtain an existing style guide (such as
Microsoft Style for Technical Publications) and then tailor it to
Nexmo's needs. A subset would be sufficient.

https://books.google.co.uk/books/about/The_Microsoft_Manual_of_Style_for_Techni.html

Other examples:

http://devdocs.magento.com/guides/v2.0/contributor-guide/contributing_docs.html

Another good example:

https://kubernetes.io/docs/home/contribute/style-guide/

Of particular note:

- Use present tense
- Use active voice
- Use simple and direct language
- Address the reader as "you"
- Avoid latin phrases
- Avoid statements that predict the future e.g. "the next version will have super xxx feature..."
- Avoid time sensitive information (specify exact version (e.g. 1.1) rather than 'current version' - current version may change)


## Present tense

Use present tense.

Future:

This command will start the server

Present:

This command starts the server.


## Second person

You.

You can now click the dialog to display.

Avoid 'we'.

## Language

Clear, simple, directive (without sounding too bossy).

Avoid cautious/conditional language. For example:

Bad:
If you run the Nexmo CLI with no parameters you might see something!

Better:
If you run the Nexmo CLI a help message is displayed.

Avoid words like would, should, might and so on.

## US English

Use US spelling as per:

https://www.merriam-webster.com

## Tone

Tome can range from very casual to very formal (1 to 5) Nexmo should be a 3 (open for discussion). 

Example (probably a 2 or 3):

https://firebase.google.com/docs/ 

Example (probably a 3 or 4):

https://www.ibm.com/support/knowledgecenter/SSEPEK_11.0.0/intro/src/tpc/db2z_newuserroadmap.html

Other reading:

UX - specific but covers topics around voice, tone, style:

http://docs.alfresco.com/sites/docs.alfresco.com/files/public/docs_team/u2/Alfresco-Writing-Guide.pdf


## Active voice

Active:

You can register your account in the dashboard.

Passive:

Your account can be registered in the dashboard.

## UX

Maybe beyond scope but good background reading:

https://uxdesign.cc/how-to-make-ux-writing-a-thing-in-your-org-2b802576b702

Consider UX copy.

## Headings

- Word case for document title
- Sentence case for section headings

## Bulleted lists

- Terminate each sentence in a bulleted list with a full stop.
- 

## Miscellaneous

- Clear, simple language is much easier to translate
- Avoid jargon/idioms (e.g. bring up a server, fire it up, behind the scenes) - reader's first language may not be English
- Avoid 'we'
- Mouse is clicked
- Keyboard is pressed (not hit, avoid "hot any key to continue")
- "He or she" (use user/developer as appropriate)
- e.g. use for example i.e. use that is etc. and so on.
- Filler words
- Contractions e.g. don't should be do not.
- Avoid wasted words/phrase/slang - "this is really cool", "a supercool feature is...".
- Avoid judgements "You can easily..." (it might not be easy for the user/developer!)

