def get_query(query=None):
    """Returns user input as query to search for or [a]dd, [q]uit"""
    while not query:
        query = input('Enter query string or [a]dd, [q]uit: ')
    return query


def get_record():
    """Returns user input as record to insert"""
    record=[]
    record.append(input('Firs name? '))
    record.append(input('Last name? '))
    record.append(input('Address? '))
    record.append(input('Phone? '))
    if not input('Add {}? [y]/[N]: '.format(record)) == 'y': record=[]
    return record
