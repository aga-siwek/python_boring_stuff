# . match any charakter

import re
at_regex = re.compile(r".at")
mol = at_regex.findall("The cat in the hat sat on the flat mat")
print(mol)