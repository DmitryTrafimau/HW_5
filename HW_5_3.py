NEGATIVE_ECONOMY = []


def no_regrets(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        vocab = {}
        if res < 0:
            a = {'name': f}
            b = {'args': args}
            c = {'kwargs': kwargs}
            vocab.update(a)
            vocab.update(b)
            vocab.update(c)
            NEGATIVE_ECONOMY.append(vocab)
            return 0
        else:
            return res
    return wrapper



@no_regrets
def calculate_water_economy(previos_consumption, new_consumption, extra_cost=0):
    return hash(
        repr(previos_consumption) +
        repr(new_consumption) +
        repr(extra_cost)) % 20 - 7

@no_regrets
def calculate_electricity_economy(load, *, rate, green_rate, **kw):
    return hash(repr(load) + repr(rate) + repr(green_rate) + repr(kw)) % 20 - 7


print(calculate_water_economy(45, 98))
print(calculate_electricity_economy(34, rate=43, green_rate=10))
print(NEGATIVE_ECONOMY)