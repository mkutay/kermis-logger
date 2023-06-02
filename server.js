const path = require("path");
const express = require("express");
const bodyParser = require("body-parser");
const fs = require('fs');
const cors = require('cors')

const app = express();

app.use(bodyParser.json());

app.use(cors({
  origin: '*'
}));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

app.post("/add", (req, res) => {
  const { bought, cost } = req.body;
  let sum = parseInt(a) + parseInt(b);
  let data;
  try {
    data = fs.readFileSync("./data.json");
  } catch (error) {
    console.error(error);
    throw error;
  }
  let jsn = JSON.parse(data);

  jsn["data"].push({"bought": bought, "cost": cost});

  data = JSON.stringify(jsn);
  try {
    fs.writeFileSync("data.json", data);
  } catch (error) {
    console.error(error);
    throw error;
  }
  res.send({
    result: sum,
  });
});

app.listen(5000, () => {
  console.log(`Server is running on port 5000.`);
});