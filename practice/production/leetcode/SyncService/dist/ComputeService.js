"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ComputeService = void 0;
const axios_1 = require("axios");
const Constants_1 = require("./Constants");
class ComputeService {
    async saveCommitTimestamp(commit) {
        const timestampPayload = {
            timestampName: 'commit',
            timestampContent: commit,
            timestamp: new Date().toJSON().toString()
        };
        return await (0, axios_1.default)(Object.assign(Object.assign({}, Constants_1.AXIOS_CONSTANTS.SAVE_COMMIT_TIMESTAMP), { data: timestampPayload }))
            .then((response) => response === null || response === void 0 ? void 0 : response.data)
            .catch((error) => error);
    }
    async getTimestamp() {
        return await (0, axios_1.default)(Constants_1.AXIOS_CONSTANTS.GET_TIMESTAMP)
            .then((response) => response === null || response === void 0 ? void 0 : response.data)
            .catch((error) => error);
    }
    async getTopics() {
        return await (0, axios_1.default)(Constants_1.AXIOS_CONSTANTS.GET_TOPICS)
            .then((response) => response === null || response === void 0 ? void 0 : response.data)
            .catch((error) => error);
    }
    async saveTopics(topics) {
        return await (0, axios_1.default)(Object.assign(Object.assign({}, Constants_1.AXIOS_CONSTANTS.SAVE_TOPICS), { data: topics }))
            .then((response) => response === null || response === void 0 ? void 0 : response.data)
            .catch((error) => error);
    }
    async saveProblem(problem) {
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
        return await (0, axios_1.default)(Object.assign(Object.assign({}, Constants_1.AXIOS_CONSTANTS.SAVE_PROBLEM), { data: problem }))
            .then((response) => response === null || response === void 0 ? void 0 : response.data)
            .catch((error) => error);
    }
}
exports.ComputeService = ComputeService;
/**
 * Steps to build:

cd SyncUpdates
tsc
node ./dist/ComputeService.js

 */
//# sourceMappingURL=ComputeService.js.map