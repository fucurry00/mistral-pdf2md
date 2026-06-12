import {
	InMemoryFilesystem,
	InMemorySnapshotStore,
	Patch,
	Patcher,
	formatHashlineHeader,
	formatNumberedLines,
} from "@oh-my-pi/hashline";

type Command = "describe" | "apply";

interface RequestPayload {
	command: Command;
	path: string;
	text: string;
	patch?: string;
}

function fail(message: string): never {
	console.error(message);
	process.exit(1);
}

async function readPayload(): Promise<RequestPayload> {
	const raw = await new Response(Bun.stdin.stream()).text();
	if (raw.trim().length === 0) fail("Missing JSON payload on stdin");
	const payload = JSON.parse(raw) as Partial<RequestPayload>;
	if (payload.command !== "describe" && payload.command !== "apply") {
		fail("Invalid command. Expected 'describe' or 'apply'.");
	}
	if (typeof payload.path !== "string" || payload.path.length === 0) {
		fail("Missing path");
	}
	if (typeof payload.text !== "string") {
		fail("Missing text");
	}
	return payload as RequestPayload;
}

const payload = await readPayload();
const fs = new InMemoryFilesystem([[payload.path, payload.text]]);
const snapshots = new InMemorySnapshotStore();
const tag = snapshots.record(payload.path, payload.text);

if (payload.command === "describe") {
	console.log(
		JSON.stringify({
			path: payload.path,
			tag,
			header: formatHashlineHeader(payload.path, tag),
			numberedText: formatNumberedLines(payload.text),
		}),
	);
	process.exit(0);
}

if (typeof payload.patch !== "string" || payload.patch.trim().length === 0) {
	fail("Missing patch");
}

const patcher = new Patcher({ fs, snapshots });
const result = await patcher.apply(Patch.parse(payload.patch));
const text = await fs.readText(payload.path);

console.log(
	JSON.stringify({
		path: payload.path,
		text,
		sections: result.sections.map(section => ({
			path: section.path,
			op: section.op,
			fileHash: section.fileHash,
			header: section.header,
			firstChangedLine: section.firstChangedLine,
			warnings: section.warnings,
		})),
	}),
);
