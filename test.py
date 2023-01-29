import re
sentence = 'we are humans'
matched = re.match('.*hu', sentence)
print(matched.group())
