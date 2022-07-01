const express = require("express");
const db = require("better-sqlite3")("db.sqlite3");
const app = express();

app.use(express.json());

app.post("/api/flag", (req, res) => {
	const username = req.body.username;
	const password = req.body.password;
	if (typeof username !== "string") {
		res.status(400);
		res.end();
		return;
	}
	if (typeof password !== "string") {
		res.status(400);
		res.end();
		return;
	}

	let result;
	try {
		result = db
			.prepare(
				`SELECT * FROM users
            WHERE username = '${username}'
            AND password = '${password}';`
			)
			.get();
	} catch (error) {
		res.json({ success: false, error: "There was a problem." });
		res.end();
		return;
	}

	if (result) {
		res.json({ success: true, flag: process.env.FLAG });
		res.end();
		return;
	}

	res.json({ success: false, error: "Incorrect username or password." });
});

app.use(express.static("/app/public"));
app.listen(process.env.PORT || 3000);

db.prepare(
	`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT);`
).run();
db.prepare(
	`INSERT INTO
    users (username, password)
    VALUES ('${process.env.USERNAME}', '${process.env.PASSWORD}');`
).run();
