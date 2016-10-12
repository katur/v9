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


let g:fakemo = 'Bla'

function! v9#GetMonth(findstart, base)
	if a:findstart
		" locate the start of the word
		let line = getline('.')
		let start = col('.') - 1
		while start > 0 && line[start - 1] =~ '\a'
			let start -= 1
		endwhile
		return start
	else
		echo a:base

		" Find months matching a:base
		let res = []
		for m in split(g:fakemo . " Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec")
			if m =~ '^' . a:base
				call add(res, m)
			endif
		endfor
		return res
	endif
endfunction

" :set completefunc
set completefunc=v9#GetMonth
