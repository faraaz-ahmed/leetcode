const { readdir } = require('node:fs/promises');
const { join } = require('node:path/posix');

const BASE_DIR = '/';

const entryCounts = {
	dirs: 0n,
	files: 0n,
	symlinks: 0n,
	streams: 0n,
	blockdevs: 0n,
	chardevs: 0n,
	sockets: 0n,
	total: 0n
};
const spec = {
	'.DS_Store': [],
	'Icon\r': [],
	'desktop.ini': [],
	'Thumbs.db': [],
	'$RECYCLE.BIN': [],
	'.gitignore': []
};
const unreadable = [];
let outputlines = 0n;

walk(BASE_DIR).then(() => {
	console.log('Entries: ', entryCounts);
	console.log('Spec: ', spec);
	console.log('Unreadable: ', unreadable);
	console.log('Output: ', outputlines);
});

async function walk(path, depth = 1, layers = []) {
	if (depth === 1) /*// { console.log(BASE_DIR); /**/ outputlines++; //*/ }
	const entries = await readdir(path, { withFileTypes: true }).catch((err) => {
		unreadable.push(`${path} [${err.code}]`);
		logEntry(`[${err.code}]`, layers, true);
	});
	if (!entries) return;
	for (let i = 0; i < entries.length; i++) {
		const dirent = entries[i];
		const isLast = i === entries.length - 1;
		logEntry(dirent.name, layers, isLast);
		if (dirent.isDirectory())
			await walk(join(path, dirent.name), depth + 1, [...layers, !isLast]);
		if (dirent.name in spec) spec[dirent.name].push(join(path, dirent.name));
		if (dirent.isDirectory()) entryCounts.dirs++;
		else if (dirent.isFile()) entryCounts.files++;
		else if (dirent.isSymbolicLink()) entryCounts.symlinks++;
		else if (dirent.isFIFO()) entryCounts.streams++;
		else if (dirent.isBlockDevice()) entryCounts.blockdevs++;
		else if (dirent.isCharacterDevice()) entryCounts.chardevs++;
		else if (dirent.isSocket()) entryCounts.sockets++;
		entryCounts.total++;
	}
}

function logEntry(name, layers, isLast) {
	// console.log(`${layers.map((nested) => (nested ? "│" : " ") + " ".repeat(3)).join("")}${isLast ? "└" : "├"}── ${name}`);
	outputlines++;
}
