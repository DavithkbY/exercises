from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 25298)
assert_file_contents_hash_to(output_file, '797507101dec2c241bc04420ba4fc2d83da49e22913314dfc94f3dfc591eaa9ff530ede35c6ea067630f06802f44e166fb5e229bf326bbd81d1704b782f2f90a')
compute_code_for_file(output_file)
