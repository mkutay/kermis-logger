const path = require("path");
const express = require("express");
const bodyParser = require("body-parser");
const fs = require('fs');

const app = express();

app.use(bodyParser.json());

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

app.post("/add", (req, res) => {
  const { a, b } = req.body;
  let sum = parseInt(a) + parseInt(b);
  let jsn = {"data": []};
  console.log(sum);
  fs.readFile('./data.json', 'utf8', (error, data) => {
    if (error) {
      console.log(error);
      return;
    }
    jsn = JSON.parse(data);
  });
  jsn["data"].push({"a": a, "b": b, "sum": sum});
  fs.writeFile('./data.json', JSON.stringify(jsn), (error) => {
    if (error) {
      console.log("there has been an error");
      return;
    }
    console.log("success");
  })
  res.send({
    result: sum,
  });
});

app.listen(5000, () => {
  console.log(`Server is running on port 5000.`);
});
