# if we wamt use VERBOL and DOTALL in one case, we should use IGNORECASE and |

import re

some_regex_value = re.compile("foo", re.I | re.DOTALL)

some_regex_value = re.compile("foo", re.I | re.DOTALL | re.VERBOSE)