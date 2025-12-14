from aqt import mw


def get_config():
    config = mw.addonManager.getConfig(__name__)
    if 'field_memory' not in config:
        config['field_memory'] = {}
    return config


def save_field_memory(model_id, expression_field, reading_field):
    if model_id is None:
        return

    model = mw.col.models.get(model_id)
    if not model:
        return

    model_name = model['name']
    config = get_config()
    config['field_memory'][model_name] = {
        'expression_field': expression_field,
        'reading_field': reading_field if reading_field else ''
    }
    mw.addonManager.writeConfig(__name__, config)


def get_field_memory(model_id):
    if model_id is None:
        return None

    model = mw.col.models.get(model_id)
    if not model:
        return None

    model_name = model['name']
    config = get_config()
    return config.get('field_memory', {}).get(model_name)


def get_default_fields():
    config = get_config()
    return (
        config.get('default_expression_field', ''),
        config.get('default_reading_field', '')
    )
