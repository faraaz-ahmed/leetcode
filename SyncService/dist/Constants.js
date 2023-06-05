"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.AXIOS_CONSTANTS = exports.IGNORE_FOLDERS = exports.HOSTNAME = void 0;
exports.HOSTNAME = 'http://localhost:8080';
exports.IGNORE_FOLDERS = [
    '.git',
    '.idea',
    'node_modules',
    'CodeJam2022QualificationRound',
    'atcoder',
    'codejam1B2022',
    'SyncService'
];
exports.AXIOS_CONSTANTS = {
    GET_TIMESTAMP: {
        method: 'get',
        url: `${exports.HOSTNAME}/timestamp/getByTimestampName?timestampName=commit`
    },
    SAVE_COMMIT_TIMESTAMP: { method: 'put', url: `${exports.HOSTNAME}/timestamp/save` },
    SAVE_PROBLEM: { method: 'post', url: `${exports.HOSTNAME}/problem/save` },
    GET_TOPICS: { method: 'get', url: `${exports.HOSTNAME}/topic/getAll` },
    SAVE_TOPICS: { method: 'post', url: `${exports.HOSTNAME}/topic/saveAll` }
};
//# sourceMappingURL=Constants.js.map