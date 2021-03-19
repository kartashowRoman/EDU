def solution(n):
    ### YOUR SOLUTION ###

    a = "   _~_   "
    b = "  (o o)  "
    c = r" /  V  \ "
    d = "/(  _  )\\"
    e = "  ^^ ^^  "
    penguin = a*n+"\n"+b*n+"\n"+c*n+"\n"+d*n+"\n"+e*n
    if n == 0:
    	penguin = ''
    return penguin
