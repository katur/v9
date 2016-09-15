if !has('python')
  finish
endif

let s:plugin_path = escape(expand('<sfile>:p:h'), '\')
exe 'pyfile ' . s:plugin_path . '/v9.py'

function! V9(digits)
python << endpython

import vim
print trie.get_words(vim.eval('a:digits'))

endpython
endfunction
