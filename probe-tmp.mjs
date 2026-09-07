import sharp from 'sharp'
import { readdirSync, statSync } from 'fs'
const dir = process.argv[2]
for (const f of readdirSync(dir).sort()) {
  const m = await sharp(dir + '/' + f).metadata()
  const kb = Math.round(statSync(dir + '/' + f).size / 1024)
  console.log(`${f}: ${m.width}x${m.height} (${kb}KB)`)
}
