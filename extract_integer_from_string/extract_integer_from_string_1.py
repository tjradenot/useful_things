import re

text = 'hello 10, fff90fff000fff 300 f150 12f'

tmp_list = re.findall(r'\d+', text)
numbers = [int(number) for number in tmp_list]

print('-' * 30)
print('Expected output:\n10 90 0 300 150 12')
print('-' * 30)

print(*numbers)
