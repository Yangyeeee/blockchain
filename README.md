# blockchain
'--pwd',type=str, default='b7a875fc1ea228b9061041b7cec4bd3c52ab3ce2', help='hash'
'--mode', default=1, type=int, help='mode 1 one password mode 2 salted mode3 concatenated with space'
'--hint', type=str, default='', help='hint for mode 2'
'--multi', default=0, type=int, help='multi thread'


usage:

python hash.py --pwd=b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
time 0.00013279914856 try 16.0 find letmein

python hash.py --pwd=801cdea58224c921c21fd2b183ff28ffa910ce31
time 5.77836203575 try 999968.0 find vjhtrhsvdctcegth

python hash.py --pwd=ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 --mode=2 --hint=f0744d60dd500c92c0d37c16174cc58d3c4bdd8e
time 2.96422886848 try 546372.0 find hine harib

python hash.py --pwd=34302959e138917ce9339c0b30ec50e650ce6b40 --mode=3


multi thread:
python hash.py --pwd=b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 --multi=1

