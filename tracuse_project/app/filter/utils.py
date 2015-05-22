"""Filter helper functions"""

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
    Q_filter_rules = ["filter_set_user_rules", "filter_set_group_rules", "filter_set_type_rules"]
    for filter_rule in Q_filter_rules:
        if filter_rule in rules:
            datum_filter_rules[filter_rule] = rules[filter_rule]

    # Compile filter rules that return datum set
    # Return list of datum sets
    # (FilterRuleAssociation, FilterRuleElement)
    datum_sets = []
    set_filter_rules = ["filter_set_association_rules", "filter_set_element_rules"]
    for filter_rule in set_filter_rules:
        if filter_rule in rules:
            datum_set = compile_datum_set_rules(
                filter_rules=rules[filter_rule],
                datum_filter_rules=datum_filter_rules
            )
            datum_sets.append(datum_set)

    output = set.intersection(*datum_sets)

    return output
