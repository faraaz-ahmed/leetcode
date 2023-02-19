import { hostName } from "./Constants";

const axios = require('axios');

// Make a request for a user with a given ID
const HttpRequest = (method: string, url: string, payload?: any, headers?: string): any => {
    axios[method](`${hostName}${url}`, payload)
            .then((response) => {
                return response;
            })
            .catch((error) => {
                return error;
            });
    return 'bad method';
};

// Want to use async/await? Add the `async` keyword to your outer function/method.
async function saveTimestamp() {
  try {
    const timestampPayload = {
        timestampName: 'commit',
        timestampContent: 'sampleTimestampContent3',
        timestamp: 'sampleTimestamp3'
    };
    const response = await HttpRequest('put', 'timestamp/save', timestampPayload);
    console.log(response);
  } catch (error) {
    console.error(error);
  }
};

async function getTimestamp() {
    try {
        const response = await HttpRequest('get', 'timestamp/getByTimestampName?timestampName=commit');
        console.log(response);
    } catch (error) {
        console.error(error);
    }
};

// saveTimestamp();
getTimestamp();
