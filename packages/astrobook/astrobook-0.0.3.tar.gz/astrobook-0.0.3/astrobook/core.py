import pandas as pd
from requests import request
from io import StringIO

APIs = {
    'simbad': 'https://simbad.u-strasbg.fr/simbad/sim-tap/sync?request=doQuery&lang=adql&query=',
    'vizier': 'http://tapvizier.u-strasbg.fr/TAPVizieR/tap/sync?request=doQuery&lang=adql&query=',
    'gaia': 'https://gea.esac.esa.int/tap-server/tap/sync?request=doQuery&lang=adql&query=',
    'irsa': 'https://irsa.ipac.caltech.edu/TAP/sync?QUERY=',
    'sdss':  'http://skyserver.sdss.org/dr16/en/tools/search/x_sql.aspx?cmd=',
    'sdss13': 'http://skyserver.sdss.org/dr13/en/tools/search/x_sql.aspx?cmd=',
    'sdss16': 'http://skyserver.sdss.org/dr16/en/tools/search/x_sql.aspx?cmd=',
    'sdss17': 'https://skyserver.sdss.org/dr17/SkyServerWS/SearchTools/SqlSearch?cmd=',
    'sdss18': 'https://skyserver.sdss.org/dr18/SkyServerWS/SearchTools/SqlSearch?cmd=',
    }


def sql2df(script, api):
    if api.lower() in APIs.keys():
        api = APIs[api]
    script = ' '.join(script.strip().split('\n'))
    url = api + script.replace(' ', '%20') + '&format=csv'
    res = request('GET', url).content.decode('utf-8')
    if len(res) > 0:
        if res.split('\n')[0][0] == '#':
            res = '\n'.join(res.split('\n')[1:])
    else:
        raise Exception('Invalid URL!')
    return pd.read_csv(StringIO(res))
