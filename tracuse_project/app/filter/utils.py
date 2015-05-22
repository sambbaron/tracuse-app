"""Filter helper functions"""
from django.db.models import Q

from app.datum.models import DatumObject

Q_FILTER_RULES = ["filter_set_user_rules",
                  "filter_set_group_rules",
                  "filter_set_type_rules"
                  ]
SET_FILTER_RULES = ["filter_set_association_rules",
                    "filter_set_element_rules",
                    "filter_set_data_type_rules"
                    ]


def compile_Q_objects(datum_filter_rules, lookup_prefix=None):
    """Compile datum filter rules and sets of rules
    using Q objects and conditionals

    Arguments:
        datum_filter_rules: Collection of filter rule objects
            dictionary of rule lists
            (FilterRuleGroup & FilterRuleType)
        lookup_prefix (string):
            lookup path to datum_object

    Return:
        Q object
    """
    output = Q()

    first_set = True
    for rule_set in datum_filter_rules.values():

        rule_set_Q_filter = Q()
        first_rule = True
        for rule in rule_set:
            Q_object = rule.Q_object(lookup_prefix)
            if first_rule:
                rule_set_Q_filter = Q_object
                first_rule = False
            else:
                rule_set_Q_filter.add(Q_object, rule.conditional)

        if first_set:
            output = rule_set_Q_filter
            first_set = False
        else:
            output.add(rule_set_Q_filter, "AND")

    return output


def compile_datum_set_rules(filter_rules, datum_filter_rules):
    """Compile filter rules using datum set and conditionals

    Arguments:
        filter_rules: Filter rule objects that output datum sets
            (FilterRuleAssociation & FilterRuleElement)
        datum_filter_rules: Collection of filter rule objects
            dictionary of rule lists
            (datum_group & datum_type)

    Return:
        Set of datum_object_ids
    """
    output = set()

    first_rule = True
    for filter_rule in filter_rules:
        datum_set = filter_rule.get_datum_set(datum_filter_rules)
        if first_rule:
            output = datum_set
            first_rule = False
        else:
            if filter_rule.conditional == "AND":
                output = output.intersection(datum_set)
            else:
                output = output.union(datum_set)

    return output


def run_filter_from_dict(**rules):
    """Apply filter rules and return list of datum_object_ids

    Arguments:
        Key: filter rule group name
            example: "filter_set_group_rules"
        Value: list of FilterRule object instances

    Returns:
        List of datum_object_ids
    """
    output = set()

    # Compile filter rules that return Q object
    # Return dictionary to be passed to filter rules that return datum sets
    # (FilterRuleUser, FilterRuleGroup, FilterRuleType)
    datum_filter_rules = {}
    for filter_rule in Q_FILTER_RULES:
        if filter_rule in rules:
            datum_filter_rules[filter_rule] = rules[filter_rule]

    # Compile filter rules that return datum set
    # Return list of datum sets
    # (FilterRuleAssociation, FilterRuleElement)
    datum_sets = []
    for filter_rule in SET_FILTER_RULES:
        if filter_rule in rules:
            datum_set = compile_datum_set_rules(
                filter_rules=rules[filter_rule],
                datum_filter_rules=datum_filter_rules
            )
            datum_sets.append(datum_set)

    if datum_sets:
        output = set.intersection(*datum_sets)
    else:
        # If no filter datum set output, then apply datum_filter on all datums
        datum_filter = compile_Q_objects(datum_filter_rules)
        output = DatumObject.objects.filter(datum_filter).values_list("datum_object_id", flat=True)

    return output
