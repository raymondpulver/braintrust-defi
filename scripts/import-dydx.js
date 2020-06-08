'use strict';

const mkdirp = require('mkdirp')
const path = require('path');
const bluebird = require('bluebird');
const ncp = bluebird.promisify(require('ncp').ncp);
const glob = bluebird.promisify(require('glob'));

(async () => {
  const buildPath = path.join(__dirname, '..', 'artifacts', 'dydx');
  await mkdirp(buildPath);
  const { dir: dydxBuildPath } = path.parse(require.resolve('@dydxprotocol/perpetual/dist/build/contracts/PerpetualV1'));
  await Promise.all((await glob(path.join(dydxBuildPath, '*.json'))).map(async (v) => {
    const { base } = path.parse(v);
    await ncp(v, path.join(buildPath, base));
  }));
})().catch((err) => console.error(err));
