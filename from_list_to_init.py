def print_parameters(start_text, list_to_transform):
    print(start_text, end='')
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
    #print()
        
        
def values_assigment(start_text, list_to_transform):
    start_spases = len(start_text) - 15
    for index in range(len(list_to_transform)):
        print(' '*start_spases, end='')
        print('self.', list_to_transform[index], ' = ',
              list_to_transform[index], sep='')
        
        # print()
    
    

string_to_transform ='''
        switch_id,switch_name,rs_id,rs_name,
        cday,h0,h1,h2,h3,
        h4,h5,h6,h7,h8,
        h9,h10,h11,h12,h13,
        h14,h15,h16,h17,h18,h19,H20,h21,h22,h23
'''
list_to_transform = string_to_transform.split(',')
for index in range(len(list_to_transform)):
    list_to_transform[index] = list_to_transform[index].strip().rstrip().lower()
print(list_to_transform)

start_text = "    def __init__(self, "
print_parameters(start_text, list_to_transform)
values_assigment(start_text, list_to_transform)



    
