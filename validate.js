const fs = require('fs');
const content = fs.readFileSync('k3_piket.html', 'utf8');
const start = content.indexOf('<script type="module">');
const end = content.lastIndexOf('</script>');
const scriptContent = content.substring(start + 22, end);
try {
  new Function(scriptContent);
  console.log('JavaScript syntax: VALID');
} catch(e) {
  console.log('Syntax error:', e.message);
  console.log('Line:', e.lineNumber);
}
