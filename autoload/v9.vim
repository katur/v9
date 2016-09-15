if !has('python')
  finish
endif

pyfile v9.py

function! V9(digits)
python << endpython

import vim
print trie.get_words(vim.eval('a:digits'))

endpython
endfunction
