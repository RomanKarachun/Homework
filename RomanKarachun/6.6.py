class Sun(object):
    __instance = None

    @staticmethod
    def inst():
        if Sun.__instance == None:
            Sun.__instance = Sun()
        return Sun.__instance

p = Sun.inst()
f = Sun.inst()
print(p is f)
