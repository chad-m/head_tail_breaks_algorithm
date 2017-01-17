"""
Python implementation of the head/tail breaks algorithm.

Article reference: http://arxiv.org/ftp/arxiv/papers/1209/1209.2801.pdf


JavaScript Implementation for reference:

function htb(data) {
    var data_mean = data.reduce(function(a, b){return a + b})/data.length;
    var head = data.filter(function(d){return d > data_mean});
    console.log(data_mean);
    while (head.length > 1 && head.length/data.length < 0.40) {
        return htb(head);
    };
}

"""


def htb(data):
    """
    Function to compute the head/tail breaks algorithm on an array of data.

    Params:
    -------
    data: python list

    Returns:
    --------
    outp: python list - data representing a list of break points.
    """
    # test input
    assert len(data) > 0, "Input must not be empty."
    assert all(isinstance(_, int) or isinstance(_, float) for _ in data), "All input values must be numeric."

    outp = []  # array of break points

    def htb_inner(data):
        """
        Inner ht breaks function for recursivesly computing the break points.
        """
        data_length = float(len(data))
        data_mean = sum(data) / data_length
        head = [_ for _ in data if _ > data_mean]
        outp.append(data_mean)
        while len(head) > 1 and len(head) / data_length < 0.40:
            return htb_inner(head)
    htb_inner(data)
    return outp
