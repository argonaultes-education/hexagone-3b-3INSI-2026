import http from 'k6/http';

export default function () {
  http.get('http://todoapi:3002');
}