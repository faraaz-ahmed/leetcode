import axios, { AxiosRequestConfig } from 'axios';
import { Timestamp } from '.';
import { AXIOS_CONSTANTS } from './Constants';
import { FileParser } from './FileParser';

// {"problemId":680,
// "problemName":"lc680.py",
// "topicName":"strings",
// "solution":"solution",
// "userName":"alex"
// }
export interface Problem {
	problemId: number;
	problemName: string;
	topicName: string;
	solution: string;
	userName: string;
}

export interface Topic {
	topicId?: number;
	topicName: string;
	problems?: any;
}

export interface Topics {
	topics: Topic[];
}

export class ComputeService {
	public async saveCommitTimestamp(commit: string): Promise<any> {
		const timestampPayload = {
			timestampName: 'commit',
			timestampContent: commit,
			timestamp: new Date().toJSON().toString()
		};
		return await axios({
			...AXIOS_CONSTANTS.SAVE_COMMIT_TIMESTAMP,
			data: timestampPayload
		})
			.then((response) => response?.data)
			.catch((error) => error);
	}

	public async getTimestamp(): Promise<Timestamp | string> {
		return await axios(AXIOS_CONSTANTS.GET_TIMESTAMP)
			.then((response) => response?.data)
			.catch((error) => error);
	}

	public async getTopics(): Promise<Topic[] | string> {
		return await axios(AXIOS_CONSTANTS.GET_TOPICS)
			.then((response) => response?.data)
			.catch((error) => error);
	}

	public async saveTopics(topics: Topics): Promise<string> {
		return await axios({ ...AXIOS_CONSTANTS.SAVE_TOPICS, data: topics })
			.then((response) => response?.data)
			.catch((error) => error);
	}

	public async saveProblem(problem: Problem): Promise<Problem | string> {
		/** 
         * 
        POST problem/save
        Description: Save problems for a user
        ```
        Request Payload:
        {
            problemId: 1,
            problemName: "test problemName",
            topic: "test topic",
            solution: "test solution",
            userId: "1"
        }
        ```
        */
		return await axios({
			...AXIOS_CONSTANTS.SAVE_PROBLEM,
			data: problem
		})
			.then((response) => response?.data)
			.catch((error) => error);
	}
}

/**
 * Steps to build:

cd SyncUpdates
tsc
node ./dist/ComputeService.js

 */
