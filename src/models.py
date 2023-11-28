from datetime import datetime


class Operation:
    def __init__(self, pk, date, state, operation_amount, description, from_, to):
        self.pk = pk
        self.date = self.covert_date(date)
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = self.covert_payment(from_)
        self.to = self.covert_payment(to)

    def covert_date(self, date):
        iso_date = datetime.fromisoformat(date)
        str_date = datetime.strftime(iso_date, "%d.%m.%Y")
        return datetime.strptime(str_date, "%d.%m.%Y")

    def covert_payment(self, info_payment):
        if info_payment:
            info_list = info_payment.split()
            if info_payment.startswith("Счет"):
                num_payment = info_list.pop()
                num_payment = f"**{num_payment[-4:]}"
                info_list.append(num_payment)
            else:
                num_payment = info_list.pop()
                num_payment = f"{num_payment[:6] + ' ** **** ' + num_payment[-4:]}"
                info_list.append(num_payment)
            return " ".join(info_list)
        return ""

    def __str__(self):
        return (f"{datetime.strftime(self.date, '%d.%m.%Y')} {self.description}\n"
                f"{self.from_} -> {self.to}\n"
                f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}")
