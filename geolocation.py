import geoip2.database

reader = geoip2.database.Reader('./db.mmdb')


def handler(event, context):
    result = reader.country(event['requesterIp'])

    return {'country': result.country.iso_code}
