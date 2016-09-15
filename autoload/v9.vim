if !has('python')
  finish
endif

if !exists('loaded_v9_py')
  let s:plugin_path = escape(expand('<sfile>:p:h'), '\')
  exe 'pyfile ' . s:plugin_path . '/v9.py'
  let g:loaded_v9_py = 1
endif


function! v9#V9(digits)
python << endpython

import vim
print trie.get_words(vim.eval('a:digits'))

endpython
endfunction
