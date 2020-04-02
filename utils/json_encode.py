import rlp,json
class JsonEncoder(json.JSONEncoder):
    def default(self, field):
        if isinstance(field, datetime.datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field, datetime.date):
            return field.strftime('%Y-%m-%d')
        if isinstance(field, Decimal):
            return float(field)
        if isinstance(field,bytes):
            return rlp.hex_encode(field)
        return json.JSONEncoder.default(self, field)