import pandas as pd
from eloqua_session import EloquaSession

session = EloquaSession()

df = pd.read_csv('trimmed-header-cdo.csv')

data = df.to_dict('records')

for record in data:
    for key in record.keys():
        try:
            record[key] = record[key].replace('\xa0', '')
        except AttributeError:
            pass

fields = []

for record in data:
    record_data = {
        "name": record["Custom Object Record Field"],
        "dataType": record['Field Data Type'].lower(),
        "displayType": record['Field type used'].lower()
    }

    if record_data['dataType'] == 'large text':
        record_data['dataType'] = 'largeText'
        record_data['displayType'] = 'textArea'

    if record_data['displayType'] == 'text area':
        record_data['displayType'] = 'textArea'

    if record_data['displayType'] == 'textbox':
        record_data['displayType'] = 'text'

    if not pd.isnull(record['Default Value']):
        record_data['defaultValue'] = record['Default Value']
    else:
        record_data['defaultValue'] = ''

    fields.append(record_data)


request_body = {
    "name": "Apps.Spam",
    "description": "",
    "fields": fields
}

response = session.post(
    url='/api/REST/2.0/assets/customObject', json=request_body)

print(response.status_code)
print(response.text)
