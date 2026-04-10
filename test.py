class Bad:
    STATE = False

    def attack(self) -> str:
        return "boosted" if Bad.STATE else "normal"

    def transform(self) -> None:
        Bad.STATE = True   # BUG: writes to the class

    def revert(self) -> None:
        Bad.STATE = False  # BUG: writes to the class


def main() -> None:
    a = Bad()
    b = Bad()

    print("Static/class STATE bug demo")
    print("Before any transform:")
    print(" a.attack() ->", a.attack())
    print(" b.attack() ->", b.attack())

    a.transform()

    print("After calling a.transform():")
    print(" a.attack() ->", a.attack())
    print(" b.attack() ->", b.attack(), "(BUG: b changed too)")

    if b.attack() != "normal":
        print("Result: BUG REPRODUCED")
        print(
            "Reason: STATE is a class/static variable shared across all instances, "
            "so transforming 'a' also changes 'b'."
        )
    else:
        print("Result: OK (no shared state bug)")


if __name__ == "__main__":
    main()