import http from 'k6/http';
import {check} from 'k6';

export default function () {
    for (let id = 0 ; id < `${__ENV.NB_LOOPS}`; id++) {
      const res = http.get('http://todoapi:3002/${id}');
      check(res, {
        'is status 200': (r) => r.status === 200
      })

      check(res, {
        'contains some text': (r) => r.body.includes('it works from')
      })
    }
}