from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 1687)
assert_file_contents_hash_to(output_file, '76c107542d30738cec221c8918eaf4a388fabf569f12efc4a12c0c07871d19e7c7b6a510549ff0109e7f4c210c2696a01fc7f5dd475055537f809c1fb1fd76f3')
compute_code_for_file(output_file)
