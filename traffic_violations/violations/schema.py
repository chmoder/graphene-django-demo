from graphene import relay, ObjectType
from graphene.contrib.django.filter import DjangoFilterConnectionField
from graphene.contrib.django.types import DjangoNode

from traffic_violations.violations.models import Violation

class ViolationNode(DjangoNode):
    class Meta:
        model = Violation
        filter_fields = {
            'description': ['exact', 'icontains', 'istartswith'],
            'date': ['exact', 'icontains'],
            'time': ['exact'],
        }
        filter_order_by = ['date']

class ViolationQuery(ObjectType):
    violation = relay.NodeField(ViolationNode)
    all_violations = DjangoFilterConnectionField(ViolationNode)

    class Meta:
        abstract = True
