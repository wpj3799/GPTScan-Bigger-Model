

  .oooooo.    ooooooooo.   ooooooooooooo  .oooooo..o                                 
 d8P'  `Y8b   `888   `Y88. 8'   888   `8 d8P'    `Y8                                 
888            888   .d88'      888      Y88bo.       .ooooo.   .oooo.   ooo. .oo.   
888            888ooo88P'       888       `"Y8888o.  d88' `"Y8 `P  )88b  `888P"Y88b  
888     ooooo  888              888           `"Y88b 888        .oP"888   888   888  
`88.    .88'   888              888      oo     .d8P 888   .o8 d8(  888   888   888  
 `Y8bood8P'   o888o            o888o     8""88888P'  `Y8bod8P' `Y888""8o o888o o888o                                                        


                                                                   

[18:18:49] Loaded 10 rules                                                                                                                                                                             tasks.py:119
           Traceback (most recent call last):                                                                                                                                                          tasks.py:126
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/src/tasks.py", line 124, in simple_cli                                                                                                         
               falcon_instance = compile_project(source_dir)                                                                                                                                                       
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/src/tasks.py", line 103, in compile_project                                                                                                    
               return falcon.Falcon(abs_path)                                                                                                                                                                      
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/falcon/falcon.py", line 90, in __init__                                                                     
               crytic_compile = CryticCompile(target, **kwargs)                                                                                                                                                    
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/crytic_compile/crytic_compile.py", line 117, in __init__                                                    
               platform = self._init_platform(target, **kwargs)                                                                                                                                                    
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/crytic_compile/crytic_compile.py", line 531, in _init_platform                                              
               platform = next(                                                                                                                                                                                    
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/crytic_compile/crytic_compile.py", line 532, in <genexpr>                                                   
               (p(target) for p in platforms if p.is_supported(target, **kwargs)), None                                                                                                                            
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/crytic_compile/platform/waffle.py", line 255, in is_supported                                               
               package = json.load(file_desc)                                                                                                                                                                      
             File "/usr/lib/python3.10/json/__init__.py", line 293, in load                                                                                                                                        
               return loads(fp.read(),                                                                                                                                                                             
             File "/usr/lib/python3.10/json/__init__.py", line 346, in loads                                                                                                                                       
               return _default_decoder.decode(s)                                                                                                                                                                   
             File "/usr/lib/python3.10/json/decoder.py", line 337, in decode                                                                                                                                       
               obj, end = self.raw_decode(s, idx=_w(s, 0).end())                                                                                                                                                   
             File "/usr/lib/python3.10/json/decoder.py", line 355, in raw_decode                                                                                                                                   
               raise JSONDecodeError("Expecting value", s, err.value) from None                                                                                                                                    
           json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)                                                                                                                                 
                                                                                                                                                                                                                   
           Compile failed.                                                                                                                                                                             tasks.py:127
           Since the compilation is failed, some static analysis tool may not be enabled, which may cause lower precision and recall.                                                                  tasks.py:128
[12/08/24 18:18:50] INFO     antlr4helper.callgraph: In whitelist: SafeMath.sub(uint,uint,string) returns(uint)                                                                                     callgraph.py:21
                    INFO     antlr4helper.callgraph: In whitelist: SafeMath.div(uint,uint,string) returns(uint)                                                                                     callgraph.py:21
                    INFO     antlr4helper.callgraph: In whitelist: Ownable._transferOwnership(address) returns()                                                                                    callgraph.py:21
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have inside code statements that invoke user checkpoint,                                                                                                                                             │
│ Code:                                                                                                                                                                                                           │
│     function getPriorVotes(address account, uint256 blockNumber) public view returns (uint96) {                                                                                                                 │
│         require(blockNumber < block.number, "Not determined yet");                                                                                                                                              │
│                                                                                                                                                                                                                 │
│         uint32 nCheckpoints = numCheckpoints;                                                                                                                                                                   │
│         if (nCheckpoints == 0) {                                                                                                                                                                                │
│             return 0;                                                                                                                                                                                           │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         // First check most recent balance                                                                                                                                                                      │
│         if (checkpoints.fromBlock <= blockNumber) {                                                                                                                                                             │
│             return ceil96(checkpoints.votes);                                                                                                                                                                   │
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
│                 return ceil96(cp.votes);                                                                                                                                                                        │
│             } else if (cp.fromBlock < blockNumber) {                                                                                                                                                            │
│                 lower = center;                                                                                                                                                                                 │
│             } else {                                                                                                                                                                                            │
│                 upper = center - 1;                                                                                                                                                                             │
│             }                                                                                                                                                                                                   │
│         }                                                                                                                                                                                                       │
│         return ceil96(checkpoints.votes);                                                                                                                                                                       │
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
│     function getPriorVotes(address account, uint256 blockNumber) public view returns (uint96) {                                                                                                                 │
│         require(blockNumber < block.number, "Not determined yet");                                                                                                                                              │
│                                                                                                                                                                                                                 │
│         uint32 nCheckpoints = numCheckpoints;                                                                                                                                                                   │
│         if (nCheckpoints == 0) {                                                                                                                                                                                │
│             return 0;                                                                                                                                                                                           │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         // First check most recent balance                                                                                                                                                                      │
│         if (checkpoints.fromBlock <= blockNumber) {                                                                                                                                                             │
│             return ceil96(checkpoints.votes);                                                                                                                                                                   │
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
│                 return ceil96(cp.votes);                                                                                                                                                                        │
│             } else if (cp.fromBlock < blockNumber) {                                                                                                                                                            │
│                 lower = center;                                                                                                                                                                                 │
│             } else {                                                                                                                                                                                            │
│                 upper = center - 1;                                                                                                                                                                             │
│             }                                                                                                                                                                                                   │
│         }                                                                                                                                                                                                       │
│         return ceil96(checkpoints.votes);                                                                                                                                                                       │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Yes                                                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have code statements that get or calculate LP token's value/price                                                                                                                                    │
│ deposit/mint/add the liquidity pool/amount/share                                                                                                                                                                │
│ Code:                                                                                                                                                                                                           │
│     function _burn(address account, uint256 amount) internal {                                                                                                                                                  │
│         require(account != address(0), "Cannot burn from the zero address");                                                                                                                                    │
│                                                                                                                                                                                                                 │
│         _balances = _balances.sub(amount, "The burn amount exceeds balance");                                                                                                                                   │
│         _totalSupply = _totalSupply.sub(amount);                                                                                                                                                                │
│         emit Transfer(account, address(0), amount);                                                                                                                                                             │
│                                                                                                                                                                                                                 │
│         _moveDelegates(delegates, address(0), amount);                                                                                                                                                          │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│     "1": "No",                                                                                                                                                                                                  │
│     "2": "No"                                                                                                                                                                                                   │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have inside code statements that invoke user checkpoint,                                                                                                                                             │
│ Code:                                                                                                                                                                                                           │
│     function _moveDelegates(address srcRep, address dstRep, uint256 amount) internal {                                                                                                                          │
│         if (srcRep != dstRep && amount > 0) {                                                                                                                                                                   │
│             if (srcRep != address(0)) {                                                                                                                                                                         │
│                 uint32 srcRepNum = numCheckpoints;                                                                                                                                                              │
│                 uint256 srcRepOld = srcRepNum > 0 ? checkpoints.votes : 0;                                                                                                                                      │
│                 uint256 srcRepNew = srcRepOld.sub(amount, "The vote amount underflows");                                                                                                                        │
│                 _writeCheckpoint(srcRep, srcRepNum, srcRepOld, srcRepNew);                                                                                                                                      │
│             }                                                                                                                                                                                                   │
│                                                                                                                                                                                                                 │
│             if (dstRep != address(0)) {                                                                                                                                                                         │
│                 uint32 dstRepNum = numCheckpoints;                                                                                                                                                              │
│                 uint256 dstRepOld = dstRepNum > 0 ? checkpoints.votes : 0;                                                                                                                                      │
│                 uint256 dstRepNew = dstRepOld.add(amount, "The vote amount overflows");                                                                                                                         │
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
│     function _moveDelegates(address srcRep, address dstRep, uint256 amount) internal {                                                                                                                          │
│         if (srcRep != dstRep && amount > 0) {                                                                                                                                                                   │
│             if (srcRep != address(0)) {                                                                                                                                                                         │
│                 uint32 srcRepNum = numCheckpoints;                                                                                                                                                              │
│                 uint256 srcRepOld = srcRepNum > 0 ? checkpoints.votes : 0;                                                                                                                                      │
│                 uint256 srcRepNew = srcRepOld.sub(amount, "The vote amount underflows");                                                                                                                        │
│                 _writeCheckpoint(srcRep, srcRepNum, srcRepOld, srcRepNew);                                                                                                                                      │
│             }                                                                                                                                                                                                   │
│                                                                                                                                                                                                                 │
│             if (dstRep != address(0)) {                                                                                                                                                                         │
│                 uint32 dstRepNum = numCheckpoints;                                                                                                                                                              │
│                 uint256 dstRepOld = dstRepNum > 0 ? checkpoints.votes : 0;                                                                                                                                      │
│                 uint256 dstRepNew = dstRepOld.add(amount, "The vote amount overflows");                                                                                                                         │
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
│     function _writeCheckpoint(address delegatee, uint32 nCheckpoints, uint256 oldVotes, uint256 newVotes) internal {                                                                                            │
│       uint32 blockNumber = safe32(block.number, "The block number exceeds 32 bits");                                                                                                                            │
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
│     function getPriorVotes(address account, uint256 blockNumber) public view returns (uint96) {                                                                                                                 │
│         require(blockNumber < block.number, "Not determined yet");                                                                                                                                              │
│                                                                                                                                                                                                                 │
│         uint32 nCheckpoints = numCheckpoints;                                                                                                                                                                   │
│         if (nCheckpoints == 0) {                                                                                                                                                                                │
│             return 0;                                                                                                                                                                                           │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         // First check most recent balance                                                                                                                                                                      │
│         if (checkpoints.fromBlock <= blockNumber) {                                                                                                                                                             │
│             return ceil96(checkpoints.votes);                                                                                                                                                                   │
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
│                 return ceil96(cp.votes);                                                                                                                                                                        │
│             } else if (cp.fromBlock < blockNumber) {                                                                                                                                                            │
│                 lower = center;                                                                                                                                                                                 │
│             } else {                                                                                                                                                                                            │
│                 upper = center - 1;                                                                                                                                                                             │
│             }                                                                                                                                                                                                   │
│         }                                                                                                                                                                                                       │
│         return ceil96(checkpoints.votes);                                                                                                                                                                       │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ `checkpoints.fromBlock <= blockNumber`                                                                                                                                                                          │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
[12/08/24 18:18:55] ERROR    tasks: Static analysis failed: Invalid args                                                                                                                               tasks.py:258
                    ERROR    tasks: Current File: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0x47bead2563dcbf3bf2c9407fea4dc236faba485a_bsc/SXP.sol, current function: getPriorVotes,  tasks.py:260
                             current vul: wrong-order-checkpoint                                                                                                                                                   
                    ERROR    tasks: Traceback (most recent call last):                                                                                                                                 tasks.py:262
                               File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/src/tasks.py", line 254, in simple_cli                                                                                       
                                 res_1 = static_check.run_static_check(checker, args, function1, falcon_instance,                                                                                                  
                             UnboundLocalError: local variable 'falcon_instance' referenced before assignment                                                                                                      
                                                                                                                                                                                                                   
╭───────────────────────────────────────────────────────────────────────────────────────────────── Current Step ──────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: In the given code, which inside code statement is the first statement to invoke user checkpoint? Answer only ZERO or ONE statement, cover the code with backquotes.                                  │
│ Code:                                                                                                                                                                                                           │
│     function _moveDelegates(address srcRep, address dstRep, uint256 amount) internal {                                                                                                                          │
│         if (srcRep != dstRep && amount > 0) {                                                                                                                                                                   │
│             if (srcRep != address(0)) {                                                                                                                                                                         │
│                 uint32 srcRepNum = numCheckpoints;                                                                                                                                                              │
│                 uint256 srcRepOld = srcRepNum > 0 ? checkpoints.votes : 0;                                                                                                                                      │
│                 uint256 srcRepNew = srcRepOld.sub(amount, "The vote amount underflows");                                                                                                                        │
│                 _writeCheckpoint(srcRep, srcRepNum, srcRepOld, srcRepNew);                                                                                                                                      │
│             }                                                                                                                                                                                                   │
│                                                                                                                                                                                                                 │
│             if (dstRep != address(0)) {                                                                                                                                                                         │
│                 uint32 dstRepNum = numCheckpoints;                                                                                                                                                              │
│                 uint256 dstRepOld = dstRepNum > 0 ? checkpoints.votes : 0;                                                                                                                                      │
│                 uint256 dstRepNew = dstRepOld.add(amount, "The vote amount overflows");                                                                                                                         │
│                 _writeCheckpoint(dstRep, dstRepNum, dstRepOld, dstRepNew);                                                                                                                                      │
│             }                                                                                                                                                                                                   │
│         }                                                                                                                                                                                                       │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ `ONE statement`                                                                                                                                                                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
                    ERROR    tasks: Static analysis failed: Invalid args                                                                                                                               tasks.py:258
                    ERROR    tasks: Current File: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0x47bead2563dcbf3bf2c9407fea4dc236faba485a_bsc/SXP.sol, current function: _moveDelegates, tasks.py:260
                             current vul: wrong-order-checkpoint                                                                                                                                                   
                    ERROR    tasks: Traceback (most recent call last):                                                                                                                                 tasks.py:262
                               File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/src/tasks.py", line 254, in simple_cli                                                                                       
                                 res_1 = static_check.run_static_check(checker, args, function1, falcon_instance,                                                                                                  
                             UnboundLocalError: local variable 'falcon_instance' referenced before assignment                                                                                                      
                                                                                                                                                                                                                   
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
│ Functions            │ 12                │
│ Lines of Code        │ 805               │
│ Used Time            │ 6.284967422485352 │
│ Estimated Cost (USD) │ 0.004087          │
└──────────────────────┴───────────────────┘
