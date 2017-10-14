# Emacs key bindings

Work in progress...

Some test text this is some more text fdjkshfkjhskj fdjshfjkh
fjdshjkfhs hfdhskjfhkjsh

## Default bindings

### Moving

C-f     - forward character
C-b     - backward character
M-f     - forward word
M-b     - backward word
C-n     - forward line
M-n     - backward line
M-e     - forward sentence
M-a     - backward sentence
C-M-f   - forward expression
C-M-b   - backward expression
M-}     - forward paragraph
C-{     - backward paragraph
C-a     - start of line
C-e     - end of line
M->     - end of buffer     (should map C-up_arrow to end of buffer)
M-<     - start of buffer   (should map C-down_arrow to end of buffer)  

### Deleting

C-d     - delete forward
DEL     - delete backward
M-d     - delete word forward
M-DEL   - delete word backward
C-k     - delete to end of line
C-SPC C-a C-w - delete to start of line
M-k     - delete sentence forward
C-x DEL - delete sentence backward
C-M-k   - delete expression forward
C-M-DEL - delete expression backward

### Cut and paste

C-SPC   - mark point
C-w     - cut
M-w     - copy
C-y     - yank
M-y     - cycle yanked (do C-y first)

### Commands

C-g     - cancel command
C-x u   - undo
M-q     - reformat paragraph

### Scrolling

C-v     - scroll down
M-v     - scroll up
C-M-v   - scroll other window dwn

C-x 1   - single window on current buffer
C-x 2   - split window horizontally
C-x 3   - split window vertically

### CUA

C-c     - copy
C-v     - paste
C-z     - undo

## Custom

C-c l   - goto line (M-x goto-line)  
C-c t   - ansi-term
C-c h   - help

C-c up          - start of buffer
C-c down        - end of buffer

M-up            - start of buffer 
M-down          - end of buffer

C-c m           - invoke Make in current dorectory

C-c             - reserved for user use
FN-             - function keys (could be useful)

Compile ?
Reflow buffer?
Open always with split window?
Toggle between H and C file in current window
Toggle between H and C file in other window

---
