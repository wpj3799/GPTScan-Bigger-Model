

  .oooooo.    ooooooooo.   ooooooooooooo  .oooooo..o                                 
 d8P'  `Y8b   `888   `Y88. 8'   888   `8 d8P'    `Y8                                 
888            888   .d88'      888      Y88bo.       .ooooo.   .oooo.   ooo. .oo.   
888            888ooo88P'       888       `"Y8888o.  d88' `"Y8 `P  )88b  `888P"Y88b  
888     ooooo  888              888           `"Y88b 888        .oP"888   888   888  
`88.    .88'   888              888      oo     .d8P 888   .o8 d8(  888   888   888  
 `Y8bood8P'   o888o            o888o     8""88888P'  `Y8bod8P' `Y888""8o o888o o888o                                                        


                                                                   

[18:37:24] Loaded 10 rules                                                                                                                                                                                       tasks.py:119
[12/08/24 18:37:24] INFO     CryticCompile: 'npx hardhat clean' running (wd: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0xb3654dc3d10ea7645f8319668e8f54d2574fbdc8_fantom)                   subprocess.py:41
[12/08/24 18:37:25] INFO     CryticCompile: 'npx hardhat clean --global' running (wd: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0xb3654dc3d10ea7645f8319668e8f54d2574fbdc8_fantom)          subprocess.py:41
[12/08/24 18:37:28] INFO     CryticCompile: 'npx hardhat compile --force' running (wd: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0xb3654dc3d10ea7645f8319668e8f54d2574fbdc8_fantom)         subprocess.py:41
[12/08/24 18:37:30] INFO     antlr4helper.callgraph: In whitelist: Address.isContract(address) returns(bool)                                                                                                  callgraph.py:21
╭──────────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have code statements that get or calculate LP token's value/price                                                                                                                                              │
│ deposit/mint/add the liquidity pool/amount/share                                                                                                                                                                          │
│ Code:                                                                                                                                                                                                                     │
│     function _mint(address account, uint256 amount) internal {                                                                                                                                                            │
│         require(account != address(0), "ERC20: mint to the zero address");                                                                                                                                                │
│                                                                                                                                                                                                                           │
│         _totalSupply += amount;                                                                                                                                                                                           │
│         balanceOf += amount;                                                                                                                                                                                              │
│         emit Transfer(address(0), account, amount);                                                                                                                                                                       │
│     }                                                                                                                                                                                                                     │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────────────────── Response ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                                         │
│     "1": "No",                                                                                                                                                                                                            │
│     "2": "No"                                                                                                                                                                                                             │
│ }                                                                                                                                                                                                                         │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have code statements that get or calculate LP token's value/price                                                                                                                                              │
│ deposit/mint/add the liquidity pool/amount/share                                                                                                                                                                          │
│ Code:                                                                                                                                                                                                                     │
│     function _burn(address account, uint256 amount) internal {                                                                                                                                                            │
│         require(account != address(0), "ERC20: burn from the zero address");                                                                                                                                              │
│                                                                                                                                                                                                                           │
│         balanceOf -= amount;                                                                                                                                                                                              │
│         _totalSupply -= amount;                                                                                                                                                                                           │
│         emit Transfer(account, address(0), amount);                                                                                                                                                                       │
│     }                                                                                                                                                                                                                     │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────────────────── Response ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                                         │
│     "1": "No",                                                                                                                                                                                                            │
│     "2": "No"                                                                                                                                                                                                             │
│ }                                                                                                                                                                                                                         │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have code statements that get or calculate LP token's value/price                                                                                                                                              │
│ deposit/mint/add the liquidity pool/amount/share                                                                                                                                                                          │
│ Code:                                                                                                                                                                                                                     │
│     function Swapout(uint256 amount, address bindaddr) public returns (bool) {                                                                                                                                            │
│         require(bindaddr != address(0), "bind address is the zero address");                                                                                                                                              │
│         _burn(msg.sender, amount);                                                                                                                                                                                        │
│         emit LogSwapout(msg.sender, bindaddr, amount);                                                                                                                                                                    │
│         return true;                                                                                                                                                                                                      │
│     }                                                                                                                                                                                                                     │
│     function _burn(address account, uint256 amount) internal {                                                                                                                                                            │
│         require(account != address(0), "ERC20: burn from the zero address");                                                                                                                                              │
│                                                                                                                                                                                                                           │
│         balanceOf -= amount;                                                                                                                                                                                              │
│         _totalSupply -= amount;                                                                                                                                                                                           │
│         emit Transfer(account, address(0), amount);                                                                                                                                                                       │
│     }                                                                                                                                                                                                                     │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────────────────── Response ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                                         │
│     "1": "No",                                                                                                                                                                                                            │
│     "2": "No"                                                                                                                                                                                                             │
│ }                                                                                                                                                                                                                         │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have code statements that get or calculate LP token's value/price                                                                                                                                              │
│ Code:                                                                                                                                                                                                                     │
│     function transferWithPermit(address target, address to, uint256 value, uint256 deadline, uint8 v, bytes32 r, bytes32 s) external returns (bool) {                                                                     │
│         require(block.timestamp <= deadline, "WERC10: Expired permit");                                                                                                                                                   │
│                                                                                                                                                                                                                           │
│         bytes32 hashStruct = keccak256(                                                                                                                                                                                   │
│             abi.encode(                                                                                                                                                                                                   │
│                 TRANSFER_TYPEHASH,                                                                                                                                                                                        │
│                 target,                                                                                                                                                                                                   │
│                 to,                                                                                                                                                                                                       │
│                 value,                                                                                                                                                                                                    │
│                 nonces++,                                                                                                                                                                                                 │
│                 deadline));                                                                                                                                                                                               │
│                                                                                                                                                                                                                           │
│         require(verifyEIP712(target, hashStruct, v, r, s) || verifyPersonalSign(target, hashStruct, v, r, s));                                                                                                            │
│                                                                                                                                                                                                                           │
│         require(to != address(0) || to != address(this));                                                                                                                                                                 │
│                                                                                                                                                                                                                           │
│         uint256 balance = balanceOf;                                                                                                                                                                                      │
│         require(balance >= value, "WERC10: transfer amount exceeds balance");                                                                                                                                             │
│                                                                                                                                                                                                                           │
│         balanceOf = balance - value;                                                                                                                                                                                      │
│         balanceOf += value;                                                                                                                                                                                               │
│         emit Transfer(target, to, value);                                                                                                                                                                                 │
│                                                                                                                                                                                                                           │
│         return true;                                                                                                                                                                                                      │
│     }                                                                                                                                                                                                                     │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────────────────── Response ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                                         │
│     "1": "No"                                                                                                                                                                                                             │
│ }                                                                                                                                                                                                                         │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have code statements that get or calculate LP token's value/price                                                                                                                                              │
│ Code:                                                                                                                                                                                                                     │
│     function transfer(address to, uint256 value) external override returns (bool) {                                                                                                                                       │
│         require(to != address(0) || to != address(this));                                                                                                                                                                 │
│         uint256 balance = balanceOf;                                                                                                                                                                                      │
│         require(balance >= value, "WERC10: transfer amount exceeds balance");                                                                                                                                             │
│                                                                                                                                                                                                                           │
│         balanceOf = balance - value;                                                                                                                                                                                      │
│         balanceOf += value;                                                                                                                                                                                               │
│         emit Transfer(msg.sender, to, value);                                                                                                                                                                             │
│                                                                                                                                                                                                                           │
│         return true;                                                                                                                                                                                                      │
│     }                                                                                                                                                                                                                     │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────────────────── Response ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                                         │
│     "1": "No"                                                                                                                                                                                                             │
│ }                                                                                                                                                                                                                         │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have code statements that get or calculate LP token's value/price                                                                                                                                              │
│ Code:                                                                                                                                                                                                                     │
│     function transferFrom(address from, address to, uint256 value) external override returns (bool) {                                                                                                                     │
│         require(to != address(0) || to != address(this));                                                                                                                                                                 │
│         if (from != msg.sender) {                                                                                                                                                                                         │
│             // _decreaseAllowance(from, msg.sender, value);                                                                                                                                                               │
│             uint256 allowed = allowance;                                                                                                                                                                                  │
│             if (allowed != type(uint256).max) {                                                                                                                                                                           │
│                 require(allowed >= value, "WERC10: request exceeds allowance");                                                                                                                                           │
│                 uint256 reduced = allowed - value;                                                                                                                                                                        │
│                 allowance = reduced;                                                                                                                                                                                      │
│                 emit Approval(from, msg.sender, reduced);                                                                                                                                                                 │
│             }                                                                                                                                                                                                             │
│         }                                                                                                                                                                                                                 │
│                                                                                                                                                                                                                           │
│         uint256 balance = balanceOf;                                                                                                                                                                                      │
│         require(balance >= value, "WERC10: transfer amount exceeds balance");                                                                                                                                             │
│                                                                                                                                                                                                                           │
│         balanceOf = balance - value;                                                                                                                                                                                      │
│         balanceOf += value;                                                                                                                                                                                               │
│         emit Transfer(from, to, value);                                                                                                                                                                                   │
│                                                                                                                                                                                                                           │
│         return true;                                                                                                                                                                                                      │
│     }                                                                                                                                                                                                                     │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────────────────── Response ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                                         │
│     "1": "No"                                                                                                                                                                                                             │
│ }                                                                                                                                                                                                                         │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have code statements that get or calculate LP token's value/price                                                                                                                                              │
│ Code:                                                                                                                                                                                                                     │
│     function transferAndCall(address to, uint value, bytes calldata data) external override returns (bool) {                                                                                                              │
│         require(to != address(0) || to != address(this));                                                                                                                                                                 │
│                                                                                                                                                                                                                           │
│         uint256 balance = balanceOf;                                                                                                                                                                                      │
│         require(balance >= value, "WERC10: transfer amount exceeds balance");                                                                                                                                             │
│                                                                                                                                                                                                                           │
│         balanceOf = balance - value;                                                                                                                                                                                      │
│         balanceOf += value;                                                                                                                                                                                               │
│         emit Transfer(msg.sender, to, value);                                                                                                                                                                             │
│                                                                                                                                                                                                                           │
│         return ITransferReceiver(to).onTokenTransfer(msg.sender, value, data);                                                                                                                                            │
│     }                                                                                                                                                                                                                     │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────────────────── Response ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                                         │
│     "1": "No"                                                                                                                                                                                                             │
│ }                                                                                                                                                                                                                         │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
                      Scan Results                       
┏━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Type ┃ Description ┃ Affected Files ┃ Analysis Report ┃
┡━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
└──────┴─────────────┴────────────────┴─────────────────┘
                  Summary                   
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Key                  ┃ Value             ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ Files                │ 1                 │
│ Contracts            │ 8                 │
│ Functions            │ 13                │
│ Lines of Code        │ 493               │
│ Used Time            │ 9.815748453140259 │
│ Estimated Cost (USD) │ 0.0027255         │
└──────────────────────┴───────────────────┘