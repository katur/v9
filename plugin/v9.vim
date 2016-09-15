" Exit if plugin already loaded or compatible mode set
if exists('g:loaded_V9') || &cp
  finish
endif

let g:loaded_V9 = 1


" Save cpo
let s:keepcpo = &cpo
set cpo&vim



" Restore cpo
let &cpo= s:keepcpo
unlet s:keepcpo
