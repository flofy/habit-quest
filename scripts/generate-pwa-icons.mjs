#!/usr/bin/env node
/**
 * Génère les icônes PWA (PNG) de Habit Quest dans public/icons/.
 *
 * - Rendu logiciel sans dépendance : l'épée du thème est dessinée en
 *   géométries simples (polygone, rectangles arrondis, cercles), avec
 *   supersampling 4x4 pour l'anticrénelage.
 * - Encodage PNG manuel (RGBA 8 bits) + compression node:zlib.
 * - Lancé automatiquement avant "dev" et "build" (scripts npm "predev" /
 *   "prebuild") : les PNG ne sont jamais commités (cf. .gitignore).
 *
 * La même épée existe en vectoriel : public/icons/icon.svg.
 */
import { deflateSync } from "node:zlib";
import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// ---------- Palette (thème RPG, cf. src/app.css) ----------
const BG_TOP = [28, 47, 36]; // #1c2f24
const BG_MID = [19, 31, 24]; // #131f18
const BG_BOT = [13, 23, 17]; // #0d1711
const GOLD_TOP = [244, 205, 111]; // #f4cd6f
const GOLD_BOT = [217, 154, 43]; // #d99a2b
const BLADE_TOP = [242, 245, 236]; // #f2f5ec
const BLADE_BOT = [184, 196, 163]; // #b8c4a3
const GRIP_TOP = [107, 74, 38]; // #6b4a26
const GRIP_BOT = [58, 40, 18]; // #3a2812
const GEM = [143, 227, 160]; // #8fe3a0
const GEM_DARK = [79, 175, 98]; // #4faf62
const RING = [74, 107, 60]; // #4a6b3c

// Lame : pointe en haut, base sur la garde (repère unitaire, y vers le bas)
const BLADE_PTS = [
  [0.5, 0.115],
  [0.548, 0.245],
  [0.548, 0.585],
  [0.452, 0.585],
  [0.452, 0.245],
];

// ---------- Géométries ----------
const mix = (a, b, t) => [
  a[0] + (b[0] - a[0]) * t,
  a[1] + (b[1] - a[1]) * t,
  a[2] + (b[2] - a[2]) * t,
];
const clamp01 = (v) => (v < 0 ? 0 : v > 1 ? 1 : v);

const inRect = (x, y, x0, y0, x1, y1) => x >= x0 && x <= x1 && y >= y0 && y <= y1;
const inCircle = (x, y, cx, cy, r) => {
  const dx = x - cx;
  const dy = y - cy;
  return dx * dx + dy * dy <= r * r;
};
const inRoundRect = (x, y, cx, cy, hw, hh, r) => {
  const dx = Math.abs(x - cx) - (hw - r);
  const dy = Math.abs(y - cy) - (hh - r);
  if (dx <= 0 && dy <= 0) return true;
  return dx * dx + dy * dy <= r * r;
};
const inRing = (x, y, cx, cy, hw, hh, r, halfW) =>
  inRoundRect(x, y, cx, cy, hw, hh, r) &&
  !inRoundRect(x, y, cx, cy, hw - halfW, hh - halfW, Math.max(0.001, r - halfW));
const inPoly = (x, y, pts) => {
  let inside = false;
  for (let i = 0, j = pts.length - 1; i < pts.length; j = i++) {
    const [xi, yi] = pts[i];
    const [xj, yj] = pts[j];
    if ((yi > y) !== (yj > y) && x < ((xj - xi) * (y - yi)) / (yj - yi) + xi) {
      inside = !inside;
    }
  }
  return inside;
};

// Fond : même dégradé que le body du jeu + lueur bleutée en haut.
function bgAt(px, py) {
  const c =
    py < 0.45
      ? mix(BG_TOP, BG_MID, py / 0.45)
      : mix(BG_MID, BG_BOT, (py - 0.45) / 0.55);
  const g = Math.exp(-(((px - 0.5) ** 2) + (py + 0.35) ** 2) / 0.18);
  return mix(c, [74, 118, 168], 0.22 * g);
}

// Couleur au point (px, py) du carré unitaire. null = pixel transparent.
// "maskable" : fond plein carré (l'OS rogne les coins) et épée réduite à 90 %
// pour rester dans la zone sûre (cercle central de 80 %).
function paint(px, py, maskable) {
  const s = maskable ? 0.9 : 1;
  const x = 0.5 + (px - 0.5) / s;
  const y = 0.5 + (py - 0.5) / s;

  let color = maskable
    ? bgAt(px, py)
    : inRoundRect(px, py, 0.5, 0.5, 0.5, 0.5, 0.22)
      ? bgAt(px, py)
      : null;
  if (color === null) return null;

  // Halo émeraude derrière l'épée
  const halo = Math.hypot((px - 0.5) / 0.32, (py - 0.52) / 0.38);
  if (halo < 1) color = mix(color, GEM, 0.1 * (1 - halo));

  // Liseré de panneau (icônes standard uniquement)
  if (!maskable && inRing(px, py, 0.5, 0.5, 0.487, 0.487, 0.207, 0.008)) {
    return mix(color, RING, 0.85);
  }

  // Lame avec gouttière centrale
  if (inPoly(x, y, BLADE_PTS)) {
    let c = mix(BLADE_TOP, BLADE_BOT, clamp01((y - 0.115) / 0.47));
    if (inRect(x, y, 0.487, 0.27, 0.513, 0.55)) c = mix(c, [90, 104, 74], 0.45);
    return c;
  }

  // Garde dorée (barre + pommeaux latéraux)
  if (
    inRoundRect(x, y, 0.5, 0.615, 0.135, 0.033, 0.028) ||
    inCircle(x, y, 0.36, 0.615, 0.03) ||
    inCircle(x, y, 0.64, 0.615, 0.03)
  ) {
    return mix(GOLD_TOP, GOLD_BOT, clamp01((y - 0.582) / 0.066));
  }

  // Poignée de cuir avec lanières
  if (inRect(x, y, 0.472, 0.648, 0.528, 0.785)) {
    let c = mix(GRIP_TOP, GRIP_BOT, clamp01((y - 0.648) / 0.137));
    for (const wy of [0.685, 0.725, 0.765]) {
      if (inRect(x, y, 0.472, wy - 0.007, 0.528, wy + 0.007)) {
        c = mix(c, [0, 0, 0], 0.4);
      }
    }
    return c;
  }

  // Pommeau + gemme émeraude
  if (inCircle(x, y, 0.5, 0.845, 0.062)) {
    let c = mix(GOLD_TOP, GOLD_BOT, clamp01((y - 0.783) / 0.124));
    if (inCircle(x, y, 0.5, 0.845, 0.026)) {
      const d = Math.hypot(x - 0.5, y - 0.845);
      c = mix(GEM, GEM_DARK, clamp01((d - 0.012) / 0.014));
    }
    return c;
  }

  return color;
}

function renderIcon(size, maskable) {
  const SS = 4; // supersampling 4x4 par pixel
  const rgba = Buffer.alloc(size * size * 4);
  for (let py = 0; py < size; py++) {
    for (let px = 0; px < size; px++) {
      let r = 0;
      let g = 0;
      let b = 0;
      let covered = 0;
      for (let sy = 0; sy < SS; sy++) {
        for (let sx = 0; sx < SS; sx++) {
          const c = paint(
            (px + (sx + 0.5) / SS) / size,
            (py + (sy + 0.5) / SS) / size,
            maskable
          );
          if (c) {
            r += c[0];
            g += c[1];
            b += c[2];
            covered++;
          }
        }
      }
      const idx = (py * size + px) * 4;
      if (covered > 0) {
        rgba[idx] = Math.round(r / covered);
        rgba[idx + 1] = Math.round(g / covered);
        rgba[idx + 2] = Math.round(b / covered);
        rgba[idx + 3] = Math.round((covered / (SS * SS)) * 255);
      }
    }
  }
  return rgba;
}

// ---------- Encodage PNG ----------
const CRC_TABLE = (() => {
  const t = new Uint32Array(256);
  for (let n = 0; n < 256; n++) {
    let c = n;
    for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
    t[n] = c >>> 0;
  }
  return t;
})();

function crc32(bytes) {
  let c = 0xffffffff;
  for (let i = 0; i < bytes.length; i++) {
    c = CRC_TABLE[(c ^ bytes[i]) & 0xff] ^ (c >>> 8);
  }
  return (c ^ 0xffffffff) >>> 0;
}

function chunk(type, data) {
  const out = Buffer.alloc(12 + data.length);
  out.writeUInt32BE(data.length, 0);
  out.write(type, 4, "ascii");
  data.copy(out, 8);
  out.writeUInt32BE(crc32(out.subarray(4, 8 + data.length)), 8 + data.length);
  return out;
}

function encodePng(size, rgba) {
  const stride = size * 4;
  const raw = Buffer.alloc((stride + 1) * size);
  for (let y = 0; y < size; y++) {
    raw[y * (stride + 1)] = 0; // filtre "None"
    rgba.copy(raw, y * (stride + 1) + 1, y * stride, (y + 1) * stride);
  }
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(size, 0);
  ihdr.writeUInt32BE(size, 4);
  ihdr[8] = 8; // profondeur
  ihdr[9] = 6; // RGBA
  ihdr[10] = 0; // compression
  ihdr[11] = 0; // filtre
  ihdr[12] = 0; // entrelacement
  return Buffer.concat([
    Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]),
    chunk("IHDR", ihdr),
    chunk("IDAT", deflateSync(raw, { level: 9 })),
    chunk("IEND", Buffer.alloc(0)),
  ]);
}

// ---------- Génération ----------
const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const outDir = join(root, "public", "icons");

const SPECS = [
  { name: "icon-512.png", size: 512, maskable: false },
  { name: "icon-192.png", size: 192, maskable: false },
  { name: "icon-180.png", size: 180, maskable: false }, // apple-touch-icon
  { name: "maskable-512.png", size: 512, maskable: true },
  { name: "maskable-192.png", size: 192, maskable: true },
];

mkdirSync(outDir, { recursive: true });
for (const { name, size, maskable } of SPECS) {
  const png = encodePng(size, renderIcon(size, maskable));
  writeFileSync(join(outDir, name), png);
  console.log("  icône générée : public/icons/" + name + " (" + png.length + " octets)");
}
console.log("Icônes PWA générées dans public/icons/");
