import random, string

def get_rua():
	return f"Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S{random.randrange(100, 9999)}/{random.randrange(100, 9999)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.randrange(1, 9)}; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/{random.randrange(1, 9)}.{random.randrange(1, 9)} Mobile WVGA SMM-MMS/1.2.0 OPN-B"