'use strict';

const fs = require('fs');
const path = require('path');
const asts = require('synthetix/publish/deployed/mainnet/deployment');
const mkdirp = require('mkdirp');
const buildPath = path.join(__dirname, '..', 'artifacts', 'synthetix');
mkdirp.sync(buildPath);
fs.writeFileSync(path.join(buildPath, 'SynthetixDeployments.json'), JSON.stringify(asts, null, 2));
