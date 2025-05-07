const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const fetch = require("node-fetch");

const app = express();
app.use(cors());
app.use(bodyParser.json());

const OPENAI_KEY = "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"; // Replace with your actual OpenAI API key

app.post("/ask", async (req, res) => {
  try {
    const response = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${OPENAI_KEY}`
      },
      body: JSON.stringify({
        model: "gpt-4",
        messages: req.body.messages
      })
    });

    const data = await response.json();
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: "AI failed", details: err.message });
  }
});

app.listen(3000, () => {
  console.log("Proxy running on port 3000");
});
