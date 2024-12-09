

  .oooooo.    ooooooooo.   ooooooooooooo  .oooooo..o                                 
 d8P'  `Y8b   `888   `Y88. 8'   888   `8 d8P'    `Y8                                 
888            888   .d88'      888      Y88bo.       .ooooo.   .oooo.   ooo. .oo.   
888            888ooo88P'       888       `"Y8888o.  d88' `"Y8 `P  )88b  `888P"Y88b  
888     ooooo  888              888           `"Y88b 888        .oP"888   888   888  
`88.    .88'   888              888      oo     .d8P 888   .o8 d8(  888   888   888  
 `Y8bood8P'   o888o            o888o     8""88888P'  `Y8bod8P' `Y888""8o o888o o888o                                                        


                                                                   

[18:11:16] Loaded 10 rules                                                                                                                                                                             tasks.py:119
[12/08/24 18:11:16] INFO     CryticCompile: 'npx hardhat clean' running (wd: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0x1f9840a85d5af5bf1d1762f925bdaddc4201f984_eth)            subprocess.py:41
[12/08/24 18:11:18] INFO     CryticCompile: 'npx hardhat clean --global' running (wd: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0x1f9840a85d5af5bf1d1762f925bdaddc4201f984_eth)   subprocess.py:41
[12/08/24 18:11:21] INFO     CryticCompile: 'npx hardhat compile --force' running (wd: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0x1f9840a85d5af5bf1d1762f925bdaddc4201f984_eth)  subprocess.py:41
[12/08/24 18:11:25] INFO     antlr4helper.callgraph: In whitelist: SafeMath.add(uint,uint) returns(uint)                                                                                            callgraph.py:21
                    INFO     antlr4helper.callgraph: In whitelist: SafeMath.sub(uint,uint,string) returns(uint)                                                                                     callgraph.py:21
                    INFO     antlr4helper.callgraph: In whitelist: SafeMath.div(uint,uint,string) returns(uint)                                                                                     callgraph.py:21
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have code statements that get or calculate LP token's value/price                                                                                                                                    │
│ deposit/mint/add the liquidity pool/amount/share                                                                                                                                                                │
│ Code:                                                                                                                                                                                                           │
│     function mint(address dst, uint rawAmount) external {                                                                                                                                                       │
│         require(msg.sender == minter, "Uni::mint: only the minter can mint");                                                                                                                                   │
│         require(block.timestamp >= mintingAllowedAfter, "Uni::mint: minting not allowed yet");                                                                                                                  │
│         require(dst != address(0), "Uni::mint: cannot transfer to the zero address");                                                                                                                           │
│                                                                                                                                                                                                                 │
│         // record the mint                                                                                                                                                                                      │
│         mintingAllowedAfter = SafeMath.add(block.timestamp, minimumTimeBetweenMints);                                                                                                                           │
│                                                                                                                                                                                                                 │
│         // mint the amount                                                                                                                                                                                      │
│         uint96 amount = safe96(rawAmount, "Uni::mint: amount exceeds 96 bits");                                                                                                                                 │
│         require(amount <= SafeMath.div(SafeMath.mul(totalSupply, mintCap), 100), "Uni::mint: exceeded mint cap");                                                                                               │
│         totalSupply = safe96(SafeMath.add(totalSupply, amount), "Uni::mint: totalSupply exceeds 96 bits");                                                                                                      │
│                                                                                                                                                                                                                 │
│         // transfer the amount to the recipient                                                                                                                                                                 │
│         balances = add96(balances, amount, "Uni::mint: transfer amount overflows");                                                                                                                             │
│         emit Transfer(address(0), dst, amount);                                                                                                                                                                 │
│                                                                                                                                                                                                                 │
│         // move delegates                                                                                                                                                                                       │
│         _moveDelegates(address(0), delegates, amount);                                                                                                                                                          │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│     "1": "No",                                                                                                                                                                                                  │
│     "2": "Yes"                                                                                                                                                                                                  │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────── Single Choice Scenario ─────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: deposit/mint/add the liquidity pool/amount/share and set the total share to the number of first deposit when the supply/liquidity is 0                                                               │
│ Code:                                                                                                                                                                                                           │
│     function mint(address dst, uint rawAmount) external {                                                                                                                                                       │
│         require(msg.sender == minter, "Uni::mint: only the minter can mint");                                                                                                                                   │
│         require(block.timestamp >= mintingAllowedAfter, "Uni::mint: minting not allowed yet");                                                                                                                  │
│         require(dst != address(0), "Uni::mint: cannot transfer to the zero address");                                                                                                                           │
│                                                                                                                                                                                                                 │
│         // record the mint                                                                                                                                                                                      │
│         mintingAllowedAfter = SafeMath.add(block.timestamp, minimumTimeBetweenMints);                                                                                                                           │
│                                                                                                                                                                                                                 │
│         // mint the amount                                                                                                                                                                                      │
│         uint96 amount = safe96(rawAmount, "Uni::mint: amount exceeds 96 bits");                                                                                                                                 │
│         require(amount <= SafeMath.div(SafeMath.mul(totalSupply, mintCap), 100), "Uni::mint: exceeded mint cap");                                                                                               │
│         totalSupply = safe96(SafeMath.add(totalSupply, amount), "Uni::mint: totalSupply exceeds 96 bits");                                                                                                      │
│                                                                                                                                                                                                                 │
│         // transfer the amount to the recipient                                                                                                                                                                 │
│         balances = add96(balances, amount, "Uni::mint: transfer amount overflows");                                                                                                                             │
│         emit Transfer(address(0), dst, amount);                                                                                                                                                                 │
│                                                                                                                                                                                                                 │
│         // move delegates                                                                                                                                                                                       │
│         _moveDelegates(address(0), delegates, amount);                                                                                                                                                          │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ No                                                                                                                                                                                                              │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: involve transfering token from an address different from message sender                                                                                                                              │
│ Code:                                                                                                                                                                                                           │
│     function transfer(address dst, uint rawAmount) external returns (bool) {                                                                                                                                    │
│         uint96 amount = safe96(rawAmount, "Uni::transfer: amount exceeds 96 bits");                                                                                                                             │
│         _transferTokens(msg.sender, dst, amount);                                                                                                                                                               │
│         return true;                                                                                                                                                                                            │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│     "1": "Yes"                                                                                                                                                                                                  │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────── Single Choice Scenario ─────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: involve transfering token from an address different from message sender and there is no check of allowance/approval from the address owner                                                           │
│ Code:                                                                                                                                                                                                           │
│     function transfer(address dst, uint rawAmount) external returns (bool) {                                                                                                                                    │
│         uint96 amount = safe96(rawAmount, "Uni::transfer: amount exceeds 96 bits");                                                                                                                             │
│         _transferTokens(msg.sender, dst, amount);                                                                                                                                                               │
│         return true;                                                                                                                                                                                            │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ No                                                                                                                                                                                                              │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have inside code statements that invoke user checkpoint,                                                                                                                                             │
│ Code:                                                                                                                                                                                                           │
│     function getPriorVotes(address account, uint blockNumber) public view returns (uint96) {                                                                                                                    │
│         require(blockNumber < block.number, "Uni::getPriorVotes: not yet determined");                                                                                                                          │
│                                                                                                                                                                                                                 │
│         uint32 nCheckpoints = numCheckpoints;                                                                                                                                                                   │
│         if (nCheckpoints == 0) {                                                                                                                                                                                │
│             return 0;                                                                                                                                                                                           │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         // First check most recent balance                                                                                                                                                                      │
│         if (checkpoints.fromBlock <= blockNumber) {                                                                                                                                                             │
│             return checkpoints.votes;                                                                                                                                                                           │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         // Next check implicit zero balance                                                                                                                                                                     │
│         if (checkpoints[0].fromBlock > blockNumber) {                                                                                                                                                           │
│             return 0;                                                                                                                                                                                           │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         uint32 lower = 0;                                                                                                                                                                                       │
│         uint32 upper = nCheckpoints - 1;                                                                                                                                                                        │
│         while (upper > lower) {                                                                                                                                                                                 │
│             uint32 center = upper - (upper - lower) / 2; // ceil, avoiding overflow                                                                                                                             │
│             Checkpoint memory cp = checkpoints;                                                                                                                                                                 │
│             if (cp.fromBlock == blockNumber) {                                                                                                                                                                  │
│                 return cp.votes;                                                                                                                                                                                │
│             } else if (cp.fromBlock < blockNumber) {                                                                                                                                                            │
│                 lower = center;                                                                                                                                                                                 │
│             } else {                                                                                                                                                                                            │
│                 upper = center - 1;                                                                                                                                                                             │
│             }                                                                                                                                                                                                   │
│         }                                                                                                                                                                                                       │
│         return checkpoints.votes;                                                                                                                                                                               │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│     "1": "Yes"                                                                                                                                                                                                  │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────── Single Choice Scenario ─────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have inside code statements that invoke user checkpoint, and have inside code statements that calculate/assigns/distribute the balance/share/stake/fee/loan/reward                                   │
│ Code:                                                                                                                                                                                                           │
│     function getPriorVotes(address account, uint blockNumber) public view returns (uint96) {                                                                                                                    │
│         require(blockNumber < block.number, "Uni::getPriorVotes: not yet determined");                                                                                                                          │
│                                                                                                                                                                                                                 │
│         uint32 nCheckpoints = numCheckpoints;                                                                                                                                                                   │
│         if (nCheckpoints == 0) {                                                                                                                                                                                │
│             return 0;                                                                                                                                                                                           │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         // First check most recent balance                                                                                                                                                                      │
│         if (checkpoints.fromBlock <= blockNumber) {                                                                                                                                                             │
│             return checkpoints.votes;                                                                                                                                                                           │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         // Next check implicit zero balance                                                                                                                                                                     │
│         if (checkpoints[0].fromBlock > blockNumber) {                                                                                                                                                           │
│             return 0;                                                                                                                                                                                           │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         uint32 lower = 0;                                                                                                                                                                                       │
│         uint32 upper = nCheckpoints - 1;                                                                                                                                                                        │
│         while (upper > lower) {                                                                                                                                                                                 │
│             uint32 center = upper - (upper - lower) / 2; // ceil, avoiding overflow                                                                                                                             │
│             Checkpoint memory cp = checkpoints;                                                                                                                                                                 │
│             if (cp.fromBlock == blockNumber) {                                                                                                                                                                  │
│                 return cp.votes;                                                                                                                                                                                │
│             } else if (cp.fromBlock < blockNumber) {                                                                                                                                                            │
│                 lower = center;                                                                                                                                                                                 │
│             } else {                                                                                                                                                                                            │
│                 upper = center - 1;                                                                                                                                                                             │
│             }                                                                                                                                                                                                   │
│         }                                                                                                                                                                                                       │
│         return checkpoints.votes;                                                                                                                                                                               │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Yes                                                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have inside code statements that invoke user checkpoint,                                                                                                                                             │
│ Code:                                                                                                                                                                                                           │
│     function _moveDelegates(address srcRep, address dstRep, uint96 amount) internal {                                                                                                                           │
│         if (srcRep != dstRep && amount > 0) {                                                                                                                                                                   │
│             if (srcRep != address(0)) {                                                                                                                                                                         │
│                 uint32 srcRepNum = numCheckpoints;                                                                                                                                                              │
│                 uint96 srcRepOld = srcRepNum > 0 ? checkpoints.votes : 0;                                                                                                                                       │
│                 uint96 srcRepNew = sub96(srcRepOld, amount, "Uni::_moveVotes: vote amount underflows");                                                                                                         │
│                 _writeCheckpoint(srcRep, srcRepNum, srcRepOld, srcRepNew);                                                                                                                                      │
│             }                                                                                                                                                                                                   │
│                                                                                                                                                                                                                 │
│             if (dstRep != address(0)) {                                                                                                                                                                         │
│                 uint32 dstRepNum = numCheckpoints;                                                                                                                                                              │
│                 uint96 dstRepOld = dstRepNum > 0 ? checkpoints.votes : 0;                                                                                                                                       │
│                 uint96 dstRepNew = add96(dstRepOld, amount, "Uni::_moveVotes: vote amount overflows");                                                                                                          │
│                 _writeCheckpoint(dstRep, dstRepNum, dstRepOld, dstRepNew);                                                                                                                                      │
│             }                                                                                                                                                                                                   │
│         }                                                                                                                                                                                                       │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│     "1": "Yes"                                                                                                                                                                                                  │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────── Single Choice Scenario ─────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have inside code statements that invoke user checkpoint, and have inside code statements that calculate/assigns/distribute the balance/share/stake/fee/loan/reward                                   │
│ Code:                                                                                                                                                                                                           │
│     function _moveDelegates(address srcRep, address dstRep, uint96 amount) internal {                                                                                                                           │
│         if (srcRep != dstRep && amount > 0) {                                                                                                                                                                   │
│             if (srcRep != address(0)) {                                                                                                                                                                         │
│                 uint32 srcRepNum = numCheckpoints;                                                                                                                                                              │
│                 uint96 srcRepOld = srcRepNum > 0 ? checkpoints.votes : 0;                                                                                                                                       │
│                 uint96 srcRepNew = sub96(srcRepOld, amount, "Uni::_moveVotes: vote amount underflows");                                                                                                         │
│                 _writeCheckpoint(srcRep, srcRepNum, srcRepOld, srcRepNew);                                                                                                                                      │
│             }                                                                                                                                                                                                   │
│                                                                                                                                                                                                                 │
│             if (dstRep != address(0)) {                                                                                                                                                                         │
│                 uint32 dstRepNum = numCheckpoints;                                                                                                                                                              │
│                 uint96 dstRepOld = dstRepNum > 0 ? checkpoints.votes : 0;                                                                                                                                       │
│                 uint96 dstRepNew = add96(dstRepOld, amount, "Uni::_moveVotes: vote amount overflows");                                                                                                          │
│                 _writeCheckpoint(dstRep, dstRepNum, dstRepOld, dstRepNew);                                                                                                                                      │
│             }                                                                                                                                                                                                   │
│         }                                                                                                                                                                                                       │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Yes                                                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have inside code statements that invoke user checkpoint,                                                                                                                                             │
│ Code:                                                                                                                                                                                                           │
│     function _writeCheckpoint(address delegatee, uint32 nCheckpoints, uint96 oldVotes, uint96 newVotes) internal {                                                                                              │
│       uint32 blockNumber = safe32(block.number, "Uni::_writeCheckpoint: block number exceeds 32 bits");                                                                                                         │
│                                                                                                                                                                                                                 │
│       if (nCheckpoints > 0 && checkpoints.fromBlock == blockNumber) {                                                                                                                                           │
│           checkpoints.votes = newVotes;                                                                                                                                                                         │
│       } else {                                                                                                                                                                                                  │
│           checkpoints = Checkpoint(blockNumber, newVotes);                                                                                                                                                      │
│           numCheckpoints = nCheckpoints + 1;                                                                                                                                                                    │
│       }                                                                                                                                                                                                         │
│                                                                                                                                                                                                                 │
│       emit DelegateVotesChanged(delegatee, oldVotes, newVotes);                                                                                                                                                 │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│     "1": "No"                                                                                                                                                                                                   │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────── Current Step ──────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: In the given code, which inside code statement is the first statement to invoke user checkpoint? Answer only ZERO or ONE statement, cover the code with backquotes.                                  │
│ Code:                                                                                                                                                                                                           │
│     function getPriorVotes(address account, uint blockNumber) public view returns (uint96) {                                                                                                                    │
│         require(blockNumber < block.number, "Uni::getPriorVotes: not yet determined");                                                                                                                          │
│                                                                                                                                                                                                                 │
│         uint32 nCheckpoints = numCheckpoints;                                                                                                                                                                   │
│         if (nCheckpoints == 0) {                                                                                                                                                                                │
│             return 0;                                                                                                                                                                                           │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         // First check most recent balance                                                                                                                                                                      │
│         if (checkpoints.fromBlock <= blockNumber) {                                                                                                                                                             │
│             return checkpoints.votes;                                                                                                                                                                           │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         // Next check implicit zero balance                                                                                                                                                                     │
│         if (checkpoints[0].fromBlock > blockNumber) {                                                                                                                                                           │
│             return 0;                                                                                                                                                                                           │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         uint32 lower = 0;                                                                                                                                                                                       │
│         uint32 upper = nCheckpoints - 1;                                                                                                                                                                        │
│         while (upper > lower) {                                                                                                                                                                                 │
│             uint32 center = upper - (upper - lower) / 2; // ceil, avoiding overflow                                                                                                                             │
│             Checkpoint memory cp = checkpoints;                                                                                                                                                                 │
│             if (cp.fromBlock == blockNumber) {                                                                                                                                                                  │
│                 return cp.votes;                                                                                                                                                                                │
│             } else if (cp.fromBlock < blockNumber) {                                                                                                                                                            │
│                 lower = center;                                                                                                                                                                                 │
│             } else {                                                                                                                                                                                            │
│                 upper = center - 1;                                                                                                                                                                             │
│             }                                                                                                                                                                                                   │
│         }                                                                                                                                                                                                       │
│         return checkpoints.votes;                                                                                                                                                                               │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ The first statement to invoke user checkpoint is `checkpoints.fromBlock <= blockNumber`.                                                                                                                        │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
   order_first_b    
┏━━━━━━━━━━┳━━━━━━━┓
┃ Argument ┃ Value ┃
┡━━━━━━━━━━╇━━━━━━━┩
│ arg[0]   │ []    │
│ arg[1]   │ []    │
└──────────┴───────┘
╭───────────────────────────────────────────────────────────────────────────────────────────────── Current Step ──────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: In the given code, which inside code statement is the first statement to invoke user checkpoint? Answer only ZERO or ONE statement, cover the code with backquotes.                                  │
│ Code:                                                                                                                                                                                                           │
│     function _moveDelegates(address srcRep, address dstRep, uint96 amount) internal {                                                                                                                           │
│         if (srcRep != dstRep && amount > 0) {                                                                                                                                                                   │
│             if (srcRep != address(0)) {                                                                                                                                                                         │
│                 uint32 srcRepNum = numCheckpoints;                                                                                                                                                              │
│                 uint96 srcRepOld = srcRepNum > 0 ? checkpoints.votes : 0;                                                                                                                                       │
│                 uint96 srcRepNew = sub96(srcRepOld, amount, "Uni::_moveVotes: vote amount underflows");                                                                                                         │
│                 _writeCheckpoint(srcRep, srcRepNum, srcRepOld, srcRepNew);                                                                                                                                      │
│             }                                                                                                                                                                                                   │
│                                                                                                                                                                                                                 │
│             if (dstRep != address(0)) {                                                                                                                                                                         │
│                 uint32 dstRepNum = numCheckpoints;                                                                                                                                                              │
│                 uint96 dstRepOld = dstRepNum > 0 ? checkpoints.votes : 0;                                                                                                                                       │
│                 uint96 dstRepNew = add96(dstRepOld, amount, "Uni::_moveVotes: vote amount overflows");                                                                                                          │
│                 _writeCheckpoint(dstRep, dstRepNum, dstRepOld, dstRepNew);                                                                                                                                      │
│             }                                                                                                                                                                                                   │
│         }                                                                                                                                                                                                       │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ `_writeCheckpoint(dstRep, dstRepNum, dstRepOld, dstRepNew);`                                                                                                                                                    │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭───────────────────────────────────────────────────────────────────────────────────────────────── Current Step ──────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: In the given code, which inside code statement is the first statement to calculate/assign/distribute the balance/share/stake/fee/loan/reward? Answer only ZERO or ONE statement, cover the code with │
│ backquotes.                                                                                                                                                                                                     │
│ Code:                                                                                                                                                                                                           │
│     function _moveDelegates(address srcRep, address dstRep, uint96 amount) internal {                                                                                                                           │
│         if (srcRep != dstRep && amount > 0) {                                                                                                                                                                   │
│             if (srcRep != address(0)) {                                                                                                                                                                         │
│                 uint32 srcRepNum = numCheckpoints;                                                                                                                                                              │
│                 uint96 srcRepOld = srcRepNum > 0 ? checkpoints.votes : 0;                                                                                                                                       │
│                 uint96 srcRepNew = sub96(srcRepOld, amount, "Uni::_moveVotes: vote amount underflows");                                                                                                         │
│                 _writeCheckpoint(srcRep, srcRepNum, srcRepOld, srcRepNew);                                                                                                                                      │
│             }                                                                                                                                                                                                   │
│                                                                                                                                                                                                                 │
│             if (dstRep != address(0)) {                                                                                                                                                                         │
│                 uint32 dstRepNum = numCheckpoints;                                                                                                                                                              │
│                 uint96 dstRepOld = dstRepNum > 0 ? checkpoints.votes : 0;                                                                                                                                       │
│                 uint96 dstRepNew = add96(dstRepOld, amount, "Uni::_moveVotes: vote amount overflows");                                                                                                          │
│                 _writeCheckpoint(dstRep, dstRepNum, dstRepOld, dstRepNew);                                                                                                                                      │
│             }                                                                                                                                                                                                   │
│         }                                                                                                                                                                                                       │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ `_writeCheckpoint(dstRep, dstRepNum, dstRepOld, dstRepNew);`                                                                                                                                                    │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
                               order_first_b                               
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Argument ┃ Value                                                        ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ arg[0]   │ []                                                           │
│ arg[1]   │ [_writeCheckpoint(dstRep, dstRepNum, dstRepOld, dstRepNew);] │
└──────────┴──────────────────────────────────────────────────────────────┘
                      Scan Results                       
┏━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Type ┃ Description ┃ Affected Files ┃ Analysis Report ┃
┡━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
└──────┴─────────────┴────────────────┴─────────────────┘
                   Summary                   
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃ Key                  ┃ Value              ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ Files                │ 1                  │
│ Contracts            │ 2                  │
│ Functions            │ 16                 │
│ Lines of Code        │ 582                │
│ Used Time            │ 14.794493436813354 │
│ Estimated Cost (USD) │ 0.0060195          │
└──────────────────────┴────────────────────┘
