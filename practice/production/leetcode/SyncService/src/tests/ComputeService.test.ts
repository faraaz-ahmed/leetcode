import { ComputeService } from '../ComputeService';
import { FileParser } from '../FileParser';

const computeService = new ComputeService();
// const response = await computeService.getTimestamp();

// computeService.getTimestamp().then((x: any) => {
// 	console.log('valueee', x);
// });
// computeService
// 	.saveTopics({ topics: [{ topicName: 'strings' }] })
// 	.then((x) => console.log(x))
// 	.catch((x) => console.log(x));

// computeService
// 	.getTopics()
// 	.then((x) => {
// 		if (Array.isArray(x)) {
// 			console.log(x.map((x) => x.topicName));
// 		}
// 	})
// 	.catch((x) => console.log(x));
computeService
	.saveProblem({
		problemId: new FileParser().getIdFromFileName('lc121.py'),
		problemName: 'lc121.py',
		topicName: 'strings',
		solution: 'my solution',
		userName: 'alex'
	})
	.then((response) => console.log(response))
	.catch((error) => console.log('error', error));

/**
 * Steps to build:

cd SyncUpdates
tsc
node ./dist/tests/ComputeService.test.js

 */
