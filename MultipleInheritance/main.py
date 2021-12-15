class Human:
    alice = True

    def sleep(self):
        print("Człowiek śpi...")


class Mother(Human):
    def dance_talent(self):
        print("Tańczy...")


class Father(Human):
    def sport_talent(self):
        print("Tańczy...")


class Grandpa(Human):
    def fix_talent(self):
        print("Naprawia...")


class Child(Mother, Father, Grandpa):
    def cry(self):
        print("Płacze...")


child = Child()
child.cry()
child.fix_talent()
child.sport_talent()
child.dance_talent()
child.sleep()
