" Exit if plugin already loaded or compatible mode set
if exists("g:loaded_V9") || &cp
  finish
endif

let g:loaded_V9 = 1


" command! -nargs=1 V9 call v9#V9(<args>)
