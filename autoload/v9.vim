" Exit if this vim is not compatible with python
if !has('python')
  finish
endif


" Initialize V9
if !exists('g:initialized_V9')
  let s:plugin_path = escape(expand('<sfile>:p:h'), '\')
  exe 'pyfile ' . s:plugin_path . '/v9.py'
  let g:initialized_V9 = 1
endif


" Do V9 algorithm on string of digits. To run in normal mode -
" :call v9#V9('222783')
function! v9#V9(digits)
python << endpython

import vim
print trie.get_words(vim.eval('a:digits'))

endpython
endfunction
