#author info
__author__ = "Jakub Mareš"
__copyright__ = "Copyright 2020, Jakub Mareš"
__contact__ = "instagram: @kubamari"

#výpočet Fibonacciho sekvence
def fib(n):
	if n <= 1:
		return n
	else:
		return(fib(n-1) + fib(n-2))

nterms = 0
print("\nDěkuju za stažení programu pro výpočet Fibonacciho sekvence")
print("\nKolik hodnot z Fibonacciho sekvence chcete zobrazit? \n(Při hodnoteě větší jak 50 dochází k výraznému zpomalení!)\n")
nterms = int(input())

if nterms <= 0:
	print("Zadejte prosím kladnou hodnotu")
else:
	print("\nFibonacciho sekvence\n")
	print("Začátek\n")
	for i in range(nterms):
		print(fib(i))

print("\nKonec")