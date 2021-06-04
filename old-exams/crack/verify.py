from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 100000)
assert_lines_match_regex(output_file, r'r\d{7} .*')
assert_file_contents_hash_to(output_file, '83be4a48745be6586e302803c095f0f6c07755b441eb88e0d10b0229e8e86ff0c54e4dd3095847aa98781adaf6c91496bc87560a2f5515755879487a370d1bfe')
compute_code_for_file(output_file)
