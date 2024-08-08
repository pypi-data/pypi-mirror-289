from datetime import datetime

from ..payment import BasePayment
from garpix_order.services.robokassa import robokassa_service


class RobokassaPayment(BasePayment):
    class Meta:
        verbose_name = 'Платеж Robokassa'
        verbose_name_plural = 'Платежи Robokassa'

    def pay(self, data, auto=False):
        if self.status != BasePayment.PaymentStatus.CREATED:
            return False, 'Invoice already in process'
        self.pending()
        self.save()
        if self.amount == 0:
            msg = 'It is not possible to pay 0 amount'
            self.set_provider_data({'msg': msg})
            self.failed()
            self.save()
            return False, msg

        res, msg = robokassa_service.check_success_payment(self, data)
        if not res:
            self.set_provider_data({'msg': msg})
            self.failed()
            self.save()
            return False, msg
        self.succeeded()
        self.order.pay(self.amount)
        if auto:
            self.order.next_payment_date = self.order.recurring.get_next_payment_date()
        self.order.save()
        self.set_provider_data({'msg': 'Payment is successful'})
        self.save()
        return True

    def refund(self):
        self.set_provider_data({'msg': f'Payment is refunded {self.amount}'})
        self.refunded()
        self.save()

    def cancel(self):
        self.set_provider_data({'msg': 'Payment is canceled'})
        self.canceled()
        self.save()

    def generate_payment_link(self):
        return robokassa_service.generate_payment_link(self)
