import requests_


def get_v1_speakers():
    r = requests_.get('http://127.0.0.1:9871/api/v1/speakers', params={
        'org_pub_id': 'a',
        'test': 1
    })

    print(r.status_code)
    print(r.url)
    print(r.status_text)
    print(r.content)
    print(r.encoding)
    print(r.text)
    resp_json = r.json()

    if 'error' in resp_json and resp_json['error'] != '':
        return resp_json['error']

    print(resp_json)


def get_v0_speakers():
    r = requests_.get('http://127.0.0.1:9871/api/v0/speakers', headers={
        'X-Api-Key': 'O76Vc3N1Gkq8akJIeZIfFvDswEJahlIw3UQ26X4vauM=',
    })

    print(r.status_code)
    print(r.url)
    print(r.status_text)
    print(r.content)
    print(r.encoding)
    print(r.text)
    resp_json = r.json()

    if 'error' in resp_json and resp_json['error'] != '':
        return resp_json['error']

    print(resp_json)


def delete_v1_speakers():
    r = requests_.delete('http://127.0.0.1:9871/api/v1/speaker', params={
        'org_pub_id': 'a',
        'speaker': 'seungminyoon'
    })

    print(r.status_code)
    print(r.url)
    print(r.status_text)
    print(r.content)
    print(r.encoding)
    print(r.text)
    resp_json = r.json()

    if 'error' in resp_json and resp_json['error'] != '':
        return resp_json['error']

    print(resp_json)


def delete_v0_speakers():
    r = requests_.delete('http://127.0.0.1:9871/api/v0/speaker', params={
        'speaker': 'smyoon'
    }, headers={
        'X-Api-Key': 'O76Vc3N1Gkq8akJIeZIfFvDswEJahlIw3UQ26X4vauM=',
    })

    print(r.status_code)
    print(r.url)
    print(r.status_text)
    print(r.content)
    print(r.encoding)
    print(r.text)
    resp_json = r.json()

    if 'error' in resp_json and resp_json['error'] != '':
        return resp_json['error']

    print(resp_json)


def post_v0_speaker_recognition():
    r = requests_.delete('http://127.0.0.1:9871/api/v0/speaker', params={
        'speaker': 'smyoon'
    }, headers={
        'X-Api-Key': 'O76Vc3N1Gkq8akJIeZIfFvDswEJahlIw3UQ26X4vauM=',
    })

    print(r.status_code)
    print(r.url)
    print(r.status_text)
    print(r.content)
    print(r.encoding)
    print(r.text)
    resp_json = r.json()

    if 'error' in resp_json and resp_json['error'] != '':
        return resp_json['error']

    print(resp_json)


def main():
    # get_v1_speakers()
    # get_v0_speakers()
    #
    # delete_v1_speakers()
    # delete_v0_speakers()

    # post_v1_speaker_recognition()
    # post_v0_speaker_recognition()

    # pass

    a = requests_.post('http://127.0.0.1:9871/api/v0/speaker/recognition', data={
        'a': 'b'
    }, headers={
        'X-Api-Key': 'O76Vc3N1Gkq8akJIeZIfFvDswEJahlIw3UQ26X4vauM='
    })
    print(a)


if __name__ == '__main__':
    main()
