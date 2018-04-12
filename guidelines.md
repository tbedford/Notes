# Technical writing style guide

## Overview

Some initial thoughts/pointers on a consistent writing style. This is
a starting point and is open for discussion.

## Examples of writing style guides

Microsoft Style for Technical Publications:

https://books.google.co.uk/books/about/The_Microsoft_Manual_of_Style_for_Techni.html

Magento:

http://devdocs.magento.com/guides/v2.0/contributor-guide/contributing_docs.html

Kubernetes:

https://kubernetes.io/docs/home/contribute/style-guide/


.NET:

https://github.com/dotnet/docs/blob/master/styleguide/voice-tone.md


## Style

### Present tense

Use present tense.

Future:

This command will start the server

Present:

This command starts the server.

### Active voice

Active:

You can register your account in the dashboard.

Passive:

Your account can be registered in the dashboard.

### Use simple and direct language

Clear, simple, directive (without sounding too bossy), conversational.

Avoid cautious/conditional language. For example:

Bad:
If you run the Nexmo CLI with no parameters you might see something!

Better:
If you run the Nexmo CLI a help message is displayed.

Avoid words like would, should, might and so on.

### Second person

You.

You can now click the dialog to display.

Avoid 'we'.

### US English

Use US spelling as per:

https://www.merriam-webster.com


### Avoid Latin phrases, slang, contractions

- Use for example, instead of e.g.
- Don't use words like 'crash', use 'error'. Use launch or start rather than 'fire up'.
- Don't use words like `don't`, use 'do not'. You will rather than you've.

### Tone

Tone can range from very casual to very formal (1 to 5) Nexmo should
be a 3 (open for discussion).

Example (probably a 2 or 3):

https://firebase.google.com/docs/ 

Example (probably a 3 or 4):

https://www.ibm.com/support/knowledgecenter/SSEPEK_11.0.0/intro/src/tpc/db2z_newuserroadmap.html

Other reading:

UX - specific but covers topics around voice, tone, style:

http://docs.alfresco.com/sites/docs.alfresco.com/files/public/docs_team/u2/Alfresco-Writing-Guide.pdf


### Headings

- Word case for document title
- Sentence case for section headings

### Bulleted lists

This is an example of a bulleted list:

- Precede a list with a sentence and a colon.
- Terminate each sentence in a list with a full stop.
- Use bulleted lists for lists.
- Use numbered lists for ordered sequences (procedures, tasks and so on).

### Codeblocks

- Specify coding language
- Break text before codeblock with colon, not period. Also, there should not be a space before the colon.

### Miscellaneous

- Try to explain to the reader *why* they need a particular feature and not just what the feature is.
- Clear, simple language is much easier to translate.
- Avoid jargon/idioms (for example: bring up a server, fire it up, behind the scenes) - reader's first language may not be English.
- Avoid 'we'.
- Mouse is clicked and keyboard is pressed. Avoid terms such as `hit`.
- "He or she" (use user/developer as appropriate)
- e.g. use 'for example' i.e. use 'that is etc. use 'and so on'.
- Filler words superfluous adjectives 'really', 'easily', 'it may be that', 'and that's it'.
- Avoid wasted words/phrase/slang - "this is really cool", "a supercool feature is...".
- Avoid judgements "You can easily..." (it might not be easy for the user/developer!)
- Avoid statements that predict the future, for example, "the next version will have super xxx feature..."
- Avoid time sensitive information (specify exact version (for example 1.1) rather than 'current version' - current version may change)

---
