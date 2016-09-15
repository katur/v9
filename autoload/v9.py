import os
import sys
import vim


# Add v9lib to the Python path.
for p in vim.eval('&runtimepath').split(','):
    plugin_dir = os.path.join(p, 'autoload')
    if os.path.exists(os.path.join(plugin_dir, 't9lib')):
        if plugin_dir not in sys.path:
            sys.path.append(plugin_dir)
            break


from t9lib.t9 import init_t9_trie


print 'Initializing V9...'

trie = init_t9_trie()

print 'Done initializing V9.'
