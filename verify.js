const fs = require('fs');
const content = fs.readFileSync('k3_piket.html', 'utf8');
const match = content.match(/<script type="module">([\s\S]*?)<\/script>/);
if (match) {
    fs.writeFileSync('_check.js', match[1]);
    console.log('Extracted script: ' + match[1].length + ' chars');
} else {
    console.log('No module script found');
}
