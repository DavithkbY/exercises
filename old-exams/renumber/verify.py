from verilib import *

output_file = 'output.txt'

assert_linecount(output_file, 13765)
assert_file_contents_hash_to(output_file, '45903ee689dfc4c4f5a7ebef65bb28e1e9e6964f98c9893cd0934dabe04cbca8ad75486f4b33ea0c9595ae389b06af28cfac86d893aaf69162c39b64e3ccd57c')
compute_code_for_file(output_file)
