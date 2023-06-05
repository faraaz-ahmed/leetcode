export const HOSTNAME = 'http://localhost:8080';
export const IGNORE_FOLDERS = [
	'.git',
	'.idea',
	'node_modules',
	'CodeJam2022QualificationRound',
	'atcoder',
	'codejam1B2022',
	'SyncService'
];
export const AXIOS_CONSTANTS = {
	GET_TIMESTAMP: {
		method: 'get',
		url: `${HOSTNAME}/timestamp/getByTimestampName?timestampName=commit`
	},
	SAVE_COMMIT_TIMESTAMP: { method: 'put', url: `${HOSTNAME}/timestamp/save` },
	SAVE_PROBLEM: { method: 'post', url: `${HOSTNAME}/problem/save` },
	GET_TOPICS: { method: 'get', url: `${HOSTNAME}/topic/getAll` },
	SAVE_TOPICS: { method: 'post', url: `${HOSTNAME}/topic/saveAll` }
};
