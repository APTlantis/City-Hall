const fs = require("fs");
const source = fs.readFileSync(process.argv[2] || "spec/tokens/BlueSlate.Tokens.toml", "utf8");
const entries = [...source.matchAll(/^\[palette\.([^\]]+)]\r?\nhex = "(#[0-9A-F]{6})"\r?\noklch = "oklch\(([0-9.]+) ([0-9.]+) ([0-9.]+)\)"/gim)];
if (entries.length < 20) throw new Error("Could not read the expected palette entries.");
const linear = (channel) => { const value = channel / 255; return value <= 0.04045 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4; };
const oklch = (hex) => {
  const rgb = [1, 3, 5].map((index) => linear(parseInt(hex.slice(index, index + 2), 16)));
  const l = Math.cbrt(0.4122214708 * rgb[0] + 0.5363325363 * rgb[1] + 0.0514459929 * rgb[2]);
  const m = Math.cbrt(0.2119034982 * rgb[0] + 0.6806995451 * rgb[1] + 0.1073969566 * rgb[2]);
  const s = Math.cbrt(0.0883024619 * rgb[0] + 0.2817188376 * rgb[1] + 0.6299787005 * rgb[2]);
  const L = 0.2104542553 * l + 0.793617785 * m - 0.0040720468 * s;
  const a = 1.9779984951 * l - 2.428592205 * m + 0.4505937099 * s;
  const b = 0.0259040371 * l + 0.7827717662 * m - 0.808675766 * s;
  return [L, Math.hypot(a, b), (Math.atan2(b, a) * 180 / Math.PI + 360) % 360];
};
for (const [, name, hex, L, C, H] of entries) {
  const actual = oklch(hex), expected = [Number(L), Number(C), Number(H)];
  if (actual.some((value, index) => Math.abs(value - expected[index]) > 0.00055)) throw new Error(`Conversion drift for ${name}: ${hex}`);
}
console.log(`Verified exact sRGB-to-OKLCH conversion for ${entries.length} palette tokens.`);
