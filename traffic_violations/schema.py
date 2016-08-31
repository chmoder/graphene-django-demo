import graphene

import traffic_violations.violations.schema

class Query(traffic_violations.violations.schema.ViolationQuery):
    # use multiple inheritance to expose more
    # expose more than one Query
    pass

schema = graphene.Schema(name='Traffic Violations Schema')
schema.query = Query

