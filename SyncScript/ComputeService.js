"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
exports.__esModule = true;
var Constants_1 = require("./Constants");
var axios = require('axios');
// Make a request for a user with a given ID
var HttpRequest = function (method, url, payload, headers) {
    console.log(method, method == 'put');
    axios[method]("".concat(Constants_1.hostName).concat(url), payload)
        .then(function (response) {
        console.log('ok?', response);
        return response;
    })["catch"](function (error) {
        return error;
    });
    // if (method == 'get') {
    //     axios.get(`${hostName}${url}`, payload)
    //         .then((response) => {
    //             return response;
    //         })
    //         .catch((error) => {
    //             return error;
    //         });
    // } else if (method == 'post') {
    //     axios.post(`${hostName}${url}`, payload)
    //         .then((response) => {
    //             return response;
    //         })
    //         .catch((error) => {
    //             return error;
    //         });
    // } else if (method == 'put') {
    //     console.log('ch1');
    //     axios.put(`${hostName}${url}`, payload)
    //         .then((response) => {
    //             console.log(response)
    //             return response;
    //         })
    //         .catch((error) => {
    //             return error;
    //         });
    // } else if (method == 'delete') {
    //     axios.delete(`${hostName}${url}`, payload)
    //         .then((response) => {
    //             return response;
    //         })
    //         .catch((error) => {
    //             return error;
    //         });
    // }
    return 'bad method';
};
// Want to use async/await? Add the `async` keyword to your outer function/method.
function saveTimestamp() {
    return __awaiter(this, void 0, void 0, function () {
        var timestampPayload, response, error_1;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    _a.trys.push([0, 2, , 3]);
                    timestampPayload = {
                        timestampName: 'commit',
                        timestampContent: 'sampleTimestampContent3',
                        timestamp: 'sampleTimestamp3'
                    };
                    return [4 /*yield*/, HttpRequest('put', 'timestamp/save', timestampPayload)];
                case 1:
                    response = _a.sent();
                    console.log(response);
                    return [3 /*break*/, 3];
                case 2:
                    error_1 = _a.sent();
                    console.error(error_1);
                    return [3 /*break*/, 3];
                case 3: return [2 /*return*/];
            }
        });
    });
}
;
function getTimestamp() {
    return __awaiter(this, void 0, void 0, function () {
        var response, error_2;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    _a.trys.push([0, 2, , 3]);
                    return [4 /*yield*/, HttpRequest('get', 'timestamp/getByTimestampName?timestampName=content')];
                case 1:
                    response = _a.sent();
                    console.log(response);
                    return [3 /*break*/, 3];
                case 2:
                    error_2 = _a.sent();
                    console.error(error_2);
                    return [3 /*break*/, 3];
                case 3: return [2 /*return*/];
            }
        });
    });
}
;
// saveTimestamp();
getTimestamp();
