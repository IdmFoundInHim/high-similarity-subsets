try:
    input_filter(multiset_input)
except InputError as err:
    raise(err)
else:
    try:
        split_equally(multiset_input)
    except InputError:
        split_approximately(multiset_input)
