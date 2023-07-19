siblings = ['Asya','Barke','Silim','Nadya','Ibthisam']
def chop(t):
    if len(t) >= 2:
        del t[0]
        del t[-1]
    return None

def middle(t):
    return t[1:-1]

theElite = middle(siblings)
print('using middle returning the middle names', theElite)
theElite1 =chop(siblings)
print('using chop with return none ', theElite1)
