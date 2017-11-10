
import re

# ISO-8601 YYYY-MM-DD
# MM 01 to 12
# DD 01 to 31
# But actually it's a bit more complicated than that as we won;t necessarily spot
# invalid dates such as 2017-19-39

str = "This 2017-12-01 string contains a date 2017-11-08 but can we find it?"

result = re.sub (r'(\d\d\d\d-[0-1][0-9]-[0-3][0-9])', r'<span class="date">\1</span>', str) 

print (result)
