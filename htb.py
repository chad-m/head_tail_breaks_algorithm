# python implementation of the head/tail breaks algorithm 
# see >> http://arxiv.org/ftp/arxiv/papers/1209/1209.2801.pdf
def htb(data):
    data_mean = sum(data)/float(len(data))
    head = [i for i in data if i > data_mean]
    tail = [i for i in data if i < data_mean]
    print data_mean 
    while len(head) > 1 and len(head)/float(len(data)) < 0.40:
        return htb(head)
