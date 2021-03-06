# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from InvenTree.forms import HelperForm

from .models import Company


class EditCompanyForm(HelperForm):

    class Meta:
        model = Company
        fields = [
            'name',
            'description',
            'website',
            'address',
            'phone',
            'email',
            'contact',
            'image',
            'is_customer',
            'is_supplier',
            'notes'
        ]


class CompanyImageForm(HelperForm):

    class Meta:
        model = Company
        fields = [
            'image'
        ]