class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def set_output(self, value):
        self.output = value

    def get_output(self):
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def get_pin_a(self):
        if self.pinA is None:
            return int(
                input(f"Enter Pin A input for gate {self.get_label()} -->"))
        else:
            return self.pinA.get_input_pin().get_output()


    def get_pin_b(self):
        if self.pinB is None:
            return int(input(f"Enter Pin B input for gate {self.get_label()} -->"))
        else:
            return self.pinB.get_input_pin().get_output()

    def set_next_pin(self, source):
        if self.pinA is None:
            self.pinA = source
        elif self.pinB is None:
            self.pinB = source
            self.set_output(self.perform_gate_logic())
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return int(input(f"Enter Pin input for gate {self.get_label()} -->"))
        else:
            return self.pin.get_input_pin().get_output()

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
            self.set_output(self.perform_gate_logic())
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class NandGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 0
        else:
            return 1


class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NorGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 0
        else:
            return 1


class XorGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == b:
            return 0
        else:
            return 1

class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin()
        if a == 1:
            return 0
        else:
            return 1


class Connector():
    def __init__(self, input_gate, output_gate):
        self.inputGate = input_gate
        self.outputGate = output_gate

        output_gate.set_next_pin(self)

    def get_input_pin(self):
        return self.inputGate

    def get_output_pin(self):
        return self.outputGate


class InputGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

    def set_value(self, value):
        self.set_output(value)

    def perform_gate_logic(self):
        return self.get_output()


# g1_1 = AndGate("G1")
# g1_2 = AndGate("G2")
# g1_3 = OrGate("G3")
# g1_4 = NotGate("G4")
#
# c1_1 = Connector(g1_1, g1_3)
# c1_2 = Connector(g1_2, g1_3)
# c1_3 = Connector(g1_3, g1_4)
#
# g2_1 = NandGate("G1")
# g2_2 = NandGate("G2")
# g2_3 = AndGate("G3")
#
# c2_1 = Connector(g2_1, g2_3)
# c2_2 = Connector(g2_2, g2_3)
#
# print(g1_4.get_output() == g2_3.get_output())

def half_adder(a_val, b_val):
    a = InputGate("A")
    b = InputGate("B")

    a.set_value(a_val)
    b.set_value(b_val)

    sum_gate = XorGate("SUM")
    carry_gate = AndGate("CARRY")

    Connector(a, sum_gate)
    Connector(b, sum_gate)
    Connector(a, carry_gate)
    Connector(b, carry_gate)

    sum_value = sum_gate.get_output()
    carry_value = carry_gate.get_output()

    return {"sum": sum_value, "carry": carry_value}


def adder(a_val, b_val, carry_val):
    firs_step = half_adder(a_val, b_val)
    second_step = half_adder(carry_val, firs_step["sum"])
    carry = firs_step["carry"] or second_step["carry"]

    return {"sum": second_step["sum"], "carry": carry}


def eight_bit_adder(a, b):
    step_carry = 0
    result = ''

    for i in range(7, -1, -1):
        step_result = adder(int(a[i]), int(b[i]), step_carry)
        result = str(step_result["sum"]) + result
        step_carry = step_result["carry"]

    return f"{result}{f" (carry_out = {step_carry})" if step_carry else ""}"


print(eight_bit_adder("01010101", "00110011"))
