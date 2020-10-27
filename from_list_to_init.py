def print_parameters(start_text, list_to_transform):
    print(start_text, "index=None, ", end='', sep='')
    index = 0
    while index < len(list_to_transform):
        out_index = index
        for inner_index in range(index, index + 3):
            if inner_index >= len(list_to_transform):
                continue
            print(list_to_transform[inner_index], '=None', sep='', end='')
            if inner_index != len(list_to_transform) - 1:
                print(',', end='')
            else:
                print('):', end='')
                index += 1
                continue
            if inner_index != out_index + 2:
                print(' ', end='')
            index += 1
        if index < len(list_to_transform):
            print('\n' + ' ' * (len(start_text) - 6), end='')
        else:
            print()


def values_assigment(start_text, list_to_transform):
    start_spases = len(start_text) - 15
    print(' '*start_spases, 'self.index = index', sep='')
    for index in range(len(list_to_transform)):
        print(' '*start_spases, end='')
        print('self.', list_to_transform[index], ' = ',
              list_to_transform[index], sep='')


def create_init(start_text, list_to_transform):
    print_parameters(start_text, list_to_transform)
    values_assigment(start_text, list_to_transform)


def create_file_read_function(file_place, name_of_records,
                              len_of_elements, class_name):
    print(f'\ndef read_{name_of_records}({name_of_records}_file_name):')
    print(f'    {name_of_records}_file = open({name_of_records}_file_name)',
    f'    {name_of_records}_lines = {name_of_records}_file.readlines()',
    f'    size_of_{name_of_records}_list = len({name_of_records}_lines)',
    f'    for index in range(size_of_{name_of_records}_list):',
    f'        {name_of_records}_lines[index] = (',
    f'               {name_of_records}_lines[index].rstrip())',
    f'    {name_of_records} = [None] * size_of_{name_of_records}_list',
    f'    in_{name_of_records}_list_index = 0',
    f'    out_{name_of_records}_list_index = 0',
    f'    while in_{name_of_records}_list_index < size_of_{name_of_records}_list:',
    f'        line_split = (',
    f'               {name_of_records}[in_{name_of_records}_list_index].split("\\t"))',
    f'        if line_split[-1] == "\\n":',
    f'            line_split.pop()',
    f'        print(in_{name_of_records}_list_index, "line_split =", line_split)',
    f'        if len(line_split) == {len_of_elements}:',
    f'            {name_of_records}[out_{name_of_records}_list_index] = (',
    f'                            {class_name}(out_{name_of_records}_list_index,',
    f'                            *line_split))',
    f'            in_{name_of_records}_list_index += 1',
    f'            out_{name_of_records}_list_index += 1',
    f'        else:',
    '            print(f"Error in line from file = {by_hours_records_file_name}",',
    '                  f"with index = {in_%s_list_index}",' % name_of_records,
    '                  f"with value {line_split}",',
    '                  f"wait for %d parameters",' % len_of_elements,
    '                  f"and got len(line_split)")',
    # here could be print into error log file
    f'            size_of_{name_of_records}_list -= 1',
    f'            in_{name_of_records}_list_index += 1',
    f'            {name_of_records}.pop()',
    f'    return {name_of_records}',
    sep='\n')


def create__str__function():
    print('\n    def __str__(self):')
    print('        \'\'\'',
          '        we return a string which almost looks like a list with str value',
          '        of every field in record',
          '        \'\'\'',
          '        list_of_values = [str((t)) for name, t in self.__dict__.items()',
          '                          if type(t).__name__ != "function" and',
          '                          not name.startswith("__")]',
          '        line_to_return = "[" + " , ".join(list_of_values) + "]"',
          '        return line_to_return',
          sep='\n')


'''
### TODO
we need to create a class with name camel_style
cause we use it in read function
'''
string_to_transform = '''
        switch_id,switch_name,rs_id,rs_name,
        cday,h0,h1,h2,h3,
        h4,h5,h6,h7,h8,
        h9,h10,h11,h12,h13,
        h14,h15,h16,h17,h18,h19,H20,h21,h22,h23
'''
start_text = "    def __init__(self, "
file_place = 'D:\\python\\double_dno\\by_hours\\mzts-3\\mzts_3_ama_all_time.txt'
name_of_records = 'by_hours_records'
class_name = ''.join(word.title() for word in name_of_records.split('_'))
print(f'class {class_name}:')
list_to_transform = string_to_transform.split(',')
len_of_elements = len(list_to_transform)
for index in range(len_of_elements):
    list_to_transform[index] = list_to_transform[index].strip().rstrip().lower()

# print(list_to_transform)

create_init(start_text, list_to_transform)

create_file_read_function(file_place, name_of_records, len_of_elements, class_name)

create__str__function()
