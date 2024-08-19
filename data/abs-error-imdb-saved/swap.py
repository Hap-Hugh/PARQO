with open('./data/abs_error/ci-n.txt', 'r') as fp:
    lines = fp.readlines()
    data = [x.strip().split() for x in lines]
    swapped_data = [[i[1], i[0]] for i in data]
    with open('./data/abs_error/ci-n_new.txt', 'w') as fp:
        for i in swapped_data:
            i = str(i[0]) + " " + str(i[1])
            fp.write("%s\n" % i)
