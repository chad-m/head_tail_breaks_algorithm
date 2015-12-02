// JavaScript implementation of the head/tail breaks algorithm.
// see >> http://arxiv.org/ftp/arxiv/papers/1209/1209.2801.pdf

function htb(data) {
    var data_mean = data.reduce(function(a, b){return a + b})/data.length;
    var head = data.filter(function(d){return d > data_mean});
    var tail = data.filter(function(d){return d < data_mean});
    console.log(data_mean);
    while (head.length > 1) {
        return htb(head);
    };
}
