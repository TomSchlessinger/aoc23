"""part 1:
print(sum([int(t) for t in[(lambda x:x[0]+x[-1])(a) for a in [("".join(map(str,[int(j) for j in i if j.isdigit()]))*2) for i in open('1').read().split()]]]))"""

"""part 2:"""
print(sum([int(t) for t in[(lambda x:x[0]+x[-1])(a) for a in [("".join(map(str,[int(j) for j in i if j.isdigit()]))*2) for i in [i.replace("one","oneone").replace("two","twotwo").replace("three","threethree").replace("four","fourfour").replace("five","fivefive").replace("six","sixsix").replace("seven","sevenseven").replace("eight","eighteight").replace("nine","ninenine").replace("one","1").replace("two","2").replace("three","3").replace("four","4").replace("five","5").replace("six","6").replace("seven","7").replace("eight","8").replace("nine","9") for i in open('1').read().split()]]]]))
