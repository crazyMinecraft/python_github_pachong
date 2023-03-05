import mysql.connector

# 连接数据库
mydb = mysql.connector.connect(
  host="保密",
  user="保密",
  password="保密",
  database="waston_1"
)

# 创建游标对象
mycursor = mydb.cursor()

# 数据列表
data_list = [
  (1, "https://github.com/lidofinance/lido-frontend-template,https://github.com/lidofinance/lido-oracle,https://github.com/lidofinance/aip,https://github.com/lidofinance/lido-council-daemon,https://github.com/lidofinance/polygon-validators-monitoring,https://github.com/lidofinance/lido-dao,https://github.com/lidofinance/lido-vesting-escrow,https://github.com/lidofinance/solana-docs,https://github.com/lidofinance/alerting-forta,https://github.com/lidofinance/lido-keys-api,https://github.com/lidofinance/validator-ejector,https://github.com/lidofinance/lido-subgraph,https://github.com/lidofinance/lido-nestjs-modules,https://github.com/lidofinance/dc4bc-conference-call,https://github.com/lidofinance/ui,https://github.com/lidofinance/reef-knot,https://github.com/lidofinance/dc4bc,https://github.com/lidofinance/depositor-bot,https://github.com/lidofinance/scripts,https://github.com/lidofinance/audits,https://github.com/lidofinance/conventional-changelog-action,https://github.com/lidofinance/github-pages-action,https://github.com/lidofinance/cosmos-sdk,https://github.com/lidofinance/lido-js-sdk,https://github.com/lidofinance/wallets-testing-modules,https://github.com/lidofinance/polygon-contracts,https://github.com/lidofinance/wasmd,https://github.com/lidofinance/ibc-go,https://github.com/lidofinance/distwallet-plaintext,https://github.com/lidofinance/terra-repositories,", "Lido"),
  (2, "https://github.com/maticnetwork/matic-docs,https://github.com/maticnetwork/polygon-cli,https://github.com/maticnetwork/matic.js,https://github.com/maticnetwork/bor,https://github.com/maticnetwork/avail-apps,https://github.com/maticnetwork/avail,https://github.com/maticnetwork/matic-cli,https://github.com/maticnetwork/avail-core,https://github.com/maticnetwork/avail-light,https://github.com/maticnetwork/proof-generation-api,https://github.com/maticnetwork/heimdall,https://github.com/maticnetwork/polygon-token-list,https://github.com/maticnetwork/pos-portal,https://github.com/maticnetwork/genesis-contracts,https://github.com/maticnetwork/Polygon-Improvement-Proposals,https://github.com/maticnetwork/mint-unity-sdk,https://github.com/maticnetwork/maticgasstation,https://github.com/maticnetwork/mint-backend,https://github.com/maticnetwork/erigon,https://github.com/maticnetwork/polyproto,https://github.com/maticnetwork/go-substrate-rpc-client,https://github.com/maticnetwork/contracts,https://github.com/maticnetwork/polygon-rosetta,https://github.com/maticnetwork/launch,https://github.com/maticnetwork/pos-plasma-tutorial,https://github.com/maticnetwork/avail_missed_blocks,https://github.com/maticnetwork/data-availability,https://github.com/maticnetwork/gaming-recipes,https://github.com/maticnetwork/node-ansible,https://github.com/maticnetwork/metamask-provider,", "maticnetwork"),
  (3, "https://github.com/makerdao/mips,https://github.com/makerdao/asset-registry,https://github.com/makerdao/governance-portal-v2,https://github.com/makerdao/spells-goerli,https://github.com/makerdao/community,https://github.com/makerdao/spells-mainnet,https://github.com/makerdao/dss-bridge,https://github.com/makerdao/endgame-docs,https://github.com/makerdao/governance-manual,https://github.com/makerdao/starknet-dss-bridge-tests,https://github.com/makerdao/multicall,https://github.com/makerdao/dss-kiln,https://github.com/makerdao/starknet-dss,https://github.com/makerdao/dss-direct-deposit,https://github.com/makerdao/starknet-spells-mainnet,https://github.com/makerdao/starknet-spells-goerli,https://github.com/makerdao/dss-teleport,https://github.com/makerdao/chainlog-ui,https://github.com/makerdao/go-ethereum,https://github.com/makerdao/exchange-callees,https://github.com/makerdao/xdomain,https://github.com/makerdao/makerdao-status,https://github.com/makerdao/gov-polling-db,https://github.com/makerdao/pe-checklists,https://github.com/makerdao/ilk-registry,https://github.com/makerdao/dss-test,https://github.com/makerdao/dss-simulation-scripts,https://github.com/makerdao/dss-flash,https://github.com/makerdao/starknet-teleport-keeper,https://github.com/makerdao/liquidations-portal,", "makerdao")
]

# 执行批量插入操作
sql = "INSERT INTO t_check_record (id, git_addr, name) VALUES (%s, %s, %s)"
mycursor.executemany(sql, data_list)

# 提交更改
mydb.commit()

print(mycursor.rowcount, "记录被插入")
