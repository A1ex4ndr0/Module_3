calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()
def is_contains(string, list_to_search):
    count_calls()
    k = False
    for i in list_to_search:
        if string.upper() == i.upper():
            k = True
            break
        else:
            k = False
    return k

print(string_info('Alexander'))
print(string_info('Nikolaevich'))
print(string_info('Barabolya'))
print(is_contains('Alex', ['PAlec', 'aLeX', 'alexia']))
print(is_contains('pin', ['pincode', 'KraPiva', 'PiPin']))
print(is_contains('soVA', ['SovA', 'roSOVAnie', 'Sovok']))
print(calls)