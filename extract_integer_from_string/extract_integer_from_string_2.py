text = 'hello 10, fff90fff000fff 300 f150 12f'

# Get rid of non digit characters
tmp_list = [' ' if not i.isdigit() else i for i in text]
tmp_string = ''.join(tmp_list)

numbers = [int(number) for number in tmp_string.split()]

print('-' * 30)
print('Expected output:\n10 90 0 300 150 12')
print('-' * 30)

print(*numbers)
