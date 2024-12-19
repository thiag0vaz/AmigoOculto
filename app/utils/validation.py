from app.exceptions.validation_exception import ValidationException

def validate_request_data(schema, data):
    """
    Valida os dados da requisição usando um schema Marshmallow.

    Args:
        schema: Um schema Marshmallow para validação.
        data: Dados da requisição.

    Returns:
        dict: Dados validados.

    Raises:
        ValidationException: Se a validação falhar.
    """
    errors = schema.validate(data)
    if errors:
        raise ValidationException(errors=errors)
    return schema.load(data)
