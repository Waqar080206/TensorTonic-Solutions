def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    mapping = {value: i for i, value in enumerate(ordering)}
    return [mapping[value] for value in values]