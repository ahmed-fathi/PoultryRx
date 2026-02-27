const { readdirSync, statSync } = require('fs')
const { join } = require('path')

function findCss(dir) {
  const entries = readdirSync(dir)
  for (const e of entries) {
    const p = join(dir, e)
    const s = statSync(p)
    if (s.isDirectory()) {
      const found = findCss(p)
      if (found) return true
    } else if (p.endsWith('.css')) {
      console.error('Plain .css source found:', p)
      return true
    }
  }
  return false
}

const root = join(__dirname, '..', 'src')
try {
  if (findCss(root)) process.exit(1)
  console.log('No .css files found in src/')
} catch (err) {
  console.error(err)
  process.exit(2)
}
