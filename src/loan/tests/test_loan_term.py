from datetime import timedelta
from unittest.mock import MagicMock

from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from common.business import get_now
from common.test_utils import AuthenticationUtils
from constant_core.business import ConstantCoreBusiness
from loan.constants import LOAN_APPLICATION_STATUS
from loan.factories import LoanApplicationFactory, LoanMemberFactory, LoanMemberApplicationFactory, \
    LoanTermFactory, LoanTermNotificationFactory


class ListLoanTermTests(APITestCase):
    def setUp(self):
        self.auth_utils = AuthenticationUtils(self.client)
        self.auth_utils.user_login()

        LoanTermFactory.create_batch(10)

    def test_list(self):
        url = reverse('loan:loanterm-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 0)

    def test_user_list(self):
        url = reverse('loan:loanterm-list')
        member = LoanMemberFactory(user_id=1)
        app = LoanApplicationFactory()
        mem_app = LoanMemberApplicationFactory(application=app, member=member, main=True)
        loan_term = LoanTermFactory(loan_applicant=mem_app, pay_date=get_now() + timedelta(days=2))
        LoanTermNotificationFactory(loan_term=loan_term)
        LoanTermNotificationFactory(loan_term=loan_term)

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 1)


class LoanTermTests(APITestCase):
    def setUp(self):
        self.auth_utils = AuthenticationUtils(self.client)
        self.auth_utils.user_login()

        ConstantCoreBusiness.transfer = MagicMock(return_value=None)

        self.member = LoanMemberFactory(user_id=1)
        app = LoanApplicationFactory(status=LOAN_APPLICATION_STATUS.approved)
        mem_app = LoanMemberApplicationFactory(application=app, member=self.member, main=True)
        self.loan_term = LoanTermFactory(loan_applicant=mem_app, pay_date=get_now() + timedelta(days=2))

    def test_pay(self):
        url = reverse('loan:loanterm-pay', args=[self.loan_term.pk])
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        ConstantCoreBusiness.transfer.assert_called_once_with(self.member.user_id,
                                                              settings.CONSTANT_USER_ID,
                                                              self.loan_term.total_amount)
