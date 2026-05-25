import json

def validate_json(data):

    try:
        json.loads(data)
        return True

    except:
        return False
