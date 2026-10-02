#!/usr/bin/env node
// Minimal language-agnostic-style SESM extraction example in JavaScript.

const fs = require("fs");

function extractSesm(svgText) {
  const match = svgText.match(/<metadata\b[^>]*\bid=["']sesm["'][^>]*>([\s\S]*?)<\/metadata>/i);
  if (!match) {
    throw new Error("No <metadata id=\"sesm\"> block found.");
  }
  const raw = match[1].replace(/^<!\[CDATA\[/, "").replace(/\]\]>$/, "").trim();
  return JSON.parse(raw);
}

if (require.main === module) {
  const file = process.argv[2];
  if (!file) {
    console.error("usage: node SESM/examples/extract-sesm.js <svg>");
    process.exit(2);
  }
  const data = extractSesm(fs.readFileSync(file, "utf8"));
  console.log(JSON.stringify({ status: "ok", sesm_version: data.sesm_version, asset: data.asset || null }, null, 2));
}

module.exports = { extractSesm };
