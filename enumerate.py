'''seq = ['one','two','three']
for i , element in enumerate(seq):
    seq[i] = '%d: %s' % (i,element)
print seq'''
seq = ["one","two","three"]
def f(pos,element):
    return "%d : %s" % (pos,element)
print [f(i,element) for i, element in enumerate(seq)]

