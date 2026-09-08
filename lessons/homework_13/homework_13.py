class TestCase:
    def __init__(self, name, status="new", duration=None):
        self.name = name
        self.status = status
        self.duration = duration

    def can_run(self):
        return self.status == "new"

    def finish(self, result, duration):
        if not self.can_run():
            return False

        if result not in ("passed", "failed"):
            return False

        self.status = result
        self.duration = duration
        return True

    def is_slow(self):
        if self.duration is None:
            return None

        return self.duration >= 5


test_1 = TestCase("Login test")

test_2 = TestCase("Payment test")
test_2.finish("passed", 6)

test_3 = TestCase("Profile test")
test_3.finish("failed", 3)
test_3.finish("passed", 2)


print(test_1.name, test_1.can_run(), test_1.is_slow(), test_1.status)
print(test_2.name, test_2.can_run(), test_2.is_slow(), test_2.status)
print(test_3.name, test_3.can_run(), test_3.is_slow(), test_3.status)
