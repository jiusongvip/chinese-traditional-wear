import XLSX from 'xlsx'
import { readFileSync } from 'fs'
const wb = XLSX.read(readFileSync('C:/Users/jiusongPC11/Downloads/chinese-traditional-wear.com-Coverage-2026-09-08.xlsx'), { type: 'buffer' })
console.log('Sheets:', wb.SheetNames.join(' | '))
for (const name of wb.SheetNames) {
  const ws = wb.Sheets[name]
  const rows = XLSX.utils.sheet_to_json(ws, { header: 1, defval: '' })
  console.log(`\n===== ${name} (${rows.length} rows) =====`)
  const max = rows.length > 60 ? 60 : rows.length
  for (let i = 0; i < max; i++) console.log(rows[i].join(' | ').substring(0, 250))
  if (rows.length > 60) console.log(`... 还有 ${rows.length - 60} 行`)
}
