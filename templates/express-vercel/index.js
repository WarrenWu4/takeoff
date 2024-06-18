import express from "express";

const app = express();

app.get("/", (req, res) => {
    res.send("Skill Issue :)))");
});

app.listen(5000, () => {
    console.log("Running on port 5000");
});

module.exports = app
