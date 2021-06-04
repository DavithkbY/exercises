from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 111156)
assert_file_contents_hash_to(output_file, '00e69ce76108ea2c7d324948f22b8170cafb3d41b7ebefc02c0941a60863cae7ea598d8d9c22650f0b8a83b63cba24d6ad6355c6d25f447afde7812cf4276d0c')
compute_code_for_file(output_file)
