from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 7033)
assert_lines_match_regex(output_file, r'[-A-Za-z ]+\((=|[+-]\d+)\)')
assert_file_contents_hash_to(output_file, 'f8fd53d13bc248958645ad0889b040a394a33404027166ee036a3fa3d98856a28379d6d53a47e7e3489698850c494011010dbe1562b70ebd800bb19f03cb19b1')
compute_code_for_file(output_file)
