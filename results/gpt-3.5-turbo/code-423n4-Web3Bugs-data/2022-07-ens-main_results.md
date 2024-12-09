

  .oooooo.    ooooooooo.   ooooooooooooo  .oooooo..o                                 
 d8P'  `Y8b   `888   `Y88. 8'   888   `8 d8P'    `Y8                                 
888            888   .d88'      888      Y88bo.       .ooooo.   .oooo.   ooo. .oo.   
888            888ooo88P'       888       `"Y8888o.  d88' `"Y8 `P  )88b  `888P"Y88b  
888     ooooo  888              888           `"Y88b 888        .oP"888   888   888  
`88.    .88'   888              888      oo     .d8P 888   .o8 d8(  888   888   888  
 `Y8bood8P'   o888o            o888o     8""88888P'  `Y8bod8P' `Y888""8o o888o o888o                                                        


                                                                   

[20:04:07] Loaded 10 rules                                                                                                                                                                             tasks.py:119
[12/08/24 20:04:07] INFO     CryticCompile: 'npx hardhat clean' running (wd: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/datasets/code-423n4-Web3Bugs-data/2022-07-ens-main)                  subprocess.py:41
[12/08/24 20:04:09] ERROR    CryticCompile: 'npx' returned non-zero exit code 1                                                                                                                    subprocess.py:60
                    ERROR    CryticCompile: Need to install the following packages:                                                                                                                subprocess.py:66
                             stdout: hardhat@2.22.17                                                                                                                                                               
                             stdout: Ok to proceed? (y)                                                                                                                                                            
                    ERROR    CryticCompile: npm error Invalid Version:                                                                                                                             subprocess.py:68
                             stderr: npm error A complete log of this run can be found in: /home/owen/.npm/_logs/2024-12-09T03_04_07_910Z-debug-0.log                                                              
                    INFO     CryticCompile: 'npx hardhat clean --global' running (wd: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/datasets/code-423n4-Web3Bugs-data/2022-07-ens-main)         subprocess.py:41
[12/08/24 20:04:50] ERROR    CryticCompile: 'npx' returned non-zero exit code 1                                                                                                                    subprocess.py:60
                    ERROR    CryticCompile: Need to install the following packages:                                                                                                                subprocess.py:66
                             stdout: hardhat@2.22.17                                                                                                                                                               
                             stdout: Ok to proceed? (y)                                                                                                                                                            
                    ERROR    CryticCompile: npm error Invalid Version:                                                                                                                             subprocess.py:68
                             stderr: npm error A complete log of this run can be found in: /home/owen/.npm/_logs/2024-12-09T03_04_09_393Z-debug-0.log                                                              
[12/08/24 20:04:51] INFO     CryticCompile: Problem executing hardhat: npm warn exec The following package was not found and will be installed: hardhat@2.22.17                                      hardhat.py:327
                             npm error Invalid Version:                                                                                                                                                            
                             npm error A complete log of this run can be found in: /home/owen/.npm/_logs/2024-12-09T03_04_50_486Z-debug-0.log                                                                      
                                                                                                                                                                                                                   
                    INFO     CryticCompile: 'npx hardhat compile --force' running (wd: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/datasets/code-423n4-Web3Bugs-data/2022-07-ens-main)        subprocess.py:41
[12/08/24 20:04:52] ERROR    CryticCompile: 'npx' returned non-zero exit code 1                                                                                                                    subprocess.py:60
                    ERROR    CryticCompile: Need to install the following packages:                                                                                                                subprocess.py:66
                             stdout: hardhat@2.22.17                                                                                                                                                               
                             stdout: Ok to proceed? (y)                                                                                                                                                            
                    ERROR    CryticCompile: npm error Invalid Version:                                                                                                                             subprocess.py:68
                             stderr: npm error A complete log of this run can be found in: /home/owen/.npm/_logs/2024-12-09T03_04_51_591Z-debug-0.log                                                              
[20:04:52] Traceback (most recent call last):                                                                                                                                                          tasks.py:126
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/falcon/falcon.py", line 90, in __init__                                                                     
               crytic_compile = CryticCompile(target, **kwargs)                                                                                                                                                    
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/crytic_compile/crytic_compile.py", line 131, in __init__                                                    
               self._compile(**kwargs)                                                                                                                                                                             
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/crytic_compile/crytic_compile.py", line 553, in _compile                                                    
               self._platform.compile(self, **kwargs)                                                                                                                                                              
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/crytic_compile/platform/hardhat.py", line 183, in compile                                                   
               hardhat_like_parsing(crytic_compile, self._target, build_directory, hardhat_working_dir)                                                                                                            
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/crytic_compile/platform/hardhat.py", line 52, in hardhat_like_parsing                                       
               raise InvalidCompilation(txt)                                                                                                                                                                       
           crytic_compile.platform.exceptions.InvalidCompilation: Compilation failed. Can you run build command?                                                                                                   
           /home/owen/Documents/GitHub/GPTScan-Bigger-Model/datasets/code-423n4-Web3Bugs-data/2022-07-ens-main/artifacts/build-info is not a directory.                                                            
                                                                                                                                                                                                                   
           During handling of the above exception, another exception occurred:                                                                                                                                     
                                                                                                                                                                                                                   
           Traceback (most recent call last):                                                                                                                                                                      
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/src/tasks.py", line 124, in simple_cli                                                                                                         
               falcon_instance = compile_project(source_dir)                                                                                                                                                       
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/src/tasks.py", line 103, in compile_project                                                                                                    
               return falcon.Falcon(abs_path)                                                                                                                                                                      
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/falcon/falcon.py", line 94, in __init__                                                                     
               raise FalconError(f"Invalid compilation: \n{str(e)}")                                                                                                                                               
           falcon.exceptions.FalconError: Invalid compilation:                                                                                                                                                     
           Compilation failed. Can you run build command?                                                                                                                                                          
           /home/owen/Documents/GitHub/GPTScan-Bigger-Model/datasets/code-423n4-Web3Bugs-data/2022-07-ens-main/artifacts/build-info is not a directory.                                                            
                                                                                                                                                                                                                   
           Compile failed.                                                                                                                                                                             tasks.py:127
           Since the compilation is failed, some static analysis tool may not be enabled, which may cause lower precision and recall.                                                                  tasks.py:128
[12/08/24 20:04:54] INFO     antlr4helper.callgraph: In whitelist: SafeMath.sub(uint,uint) returns(uint)                                                                                            callgraph.py:21
                    INFO     antlr4helper.callgraph: In whitelist: SafeMath.add(uint,uint) returns(uint)                                                                                            callgraph.py:21
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have inside code statements that update/accrue interest/exchange rate,                                                                                                                               │
│ Code:                                                                                                                                                                                                           │
│     function setDNSRecords(bytes32 node, bytes calldata data) virtual external authorised(node) {                                                                                                               │
│         uint16 resource = 0;                                                                                                                                                                                    │
│         uint256 offset = 0;                                                                                                                                                                                     │
│         bytes memory name;                                                                                                                                                                                      │
│         bytes memory value;                                                                                                                                                                                     │
│         bytes32 nameHash;                                                                                                                                                                                       │
│         // Iterate over the data to add the resource records                                                                                                                                                    │
│         for (RRUtils.RRIterator memory iter = data.iterateRRs(0); !iter.done(); iter.next()) {                                                                                                                  │
│             if (resource == 0) {                                                                                                                                                                                │
│                 resource = iter.dnstype;                                                                                                                                                                        │
│                 name = iter.name();                                                                                                                                                                             │
│                 nameHash = keccak256(abi.encodePacked(name));                                                                                                                                                   │
│                 value = bytes(iter.rdata());                                                                                                                                                                    │
│             } else {                                                                                                                                                                                            │
│                 bytes memory newName = iter.name();                                                                                                                                                             │
│                 if (resource != iter.dnstype || !name.equals(newName)) {                                                                                                                                        │
│                     setDNSRRSet(node, name, resource, data, offset, iter.offset - offset, value.length == 0);                                                                                                   │
│                     resource = iter.dnstype;                                                                                                                                                                    │
│                     offset = iter.offset;                                                                                                                                                                       │
│                     name = newName;                                                                                                                                                                             │
│                     nameHash = keccak256(name);                                                                                                                                                                 │
│                     value = bytes(iter.rdata());                                                                                                                                                                │
│                 }                                                                                                                                                                                               │
│             }                                                                                                                                                                                                   │
│         }                                                                                                                                                                                                       │
│         if (name.length > 0) {                                                                                                                                                                                  │
│             setDNSRRSet(node, name, resource, data, offset, data.length - offset, value.length == 0);                                                                                                           │
│         }                                                                                                                                                                                                       │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│     "1": "No"                                                                                                                                                                                                   │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have inside code statements that update/accrue interest/exchange rate,                                                                                                                               │
│ Code:                                                                                                                                                                                                           │
│     function validateRRs(RRUtils.SignedSet memory rrset, uint16 typecovered) internal pure returns (bytes memory name) {                                                                                        │
│         // Iterate over all the RRs                                                                                                                                                                             │
│         for (RRUtils.RRIterator memory iter = rrset.rrs(); !iter.done(); iter.next()) {                                                                                                                         │
│             // We only support class IN (Internet)                                                                                                                                                              │
│             if(iter.class != DNSCLASS_IN) {                                                                                                                                                                     │
│                 revert InvalidClass(iter.class);                                                                                                                                                                │
│             }                                                                                                                                                                                                   │
│                                                                                                                                                                                                                 │
│             if(name.length == 0) {                                                                                                                                                                              │
│                 name = iter.name();                                                                                                                                                                             │
│             } else {                                                                                                                                                                                            │
│                 // Name must be the same on all RRs. We do things this way to avoid copying the name                                                                                                            │
│                 // repeatedly.                                                                                                                                                                                  │
│                 if(name.length != iter.data.nameLength(iter.offset)                                                                                                                                             │
│                     || !name.equals(0, iter.data, iter.offset, name.length))                                                                                                                                    │
│                 {                                                                                                                                                                                               │
│                     revert InvalidRRSet();                                                                                                                                                                      │
│                 }                                                                                                                                                                                               │
│             }                                                                                                                                                                                                   │
│                                                                                                                                                                                                                 │
│             // o  The RRSIG RR's Type Covered field MUST equal the RRset's type.                                                                                                                                │
│             if(iter.dnstype != typecovered) {                                                                                                                                                                   │
│                 revert SignatureTypeMismatch(iter.dnstype, typecovered);                                                                                                                                        │
│             }                                                                                                                                                                                                   │
│         }                                                                                                                                                                                                       │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│     "1": "No"                                                                                                                                                                                                   │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have inside code statements that update/accrue interest/exchange rate,                                                                                                                               │
│ Code:                                                                                                                                                                                                           │
│     function verifySignature(bytes memory name, RRUtils.SignedSet memory rrset, RRSetWithSignature memory data, bytes memory proof) internal view {                                                             │
│         // o  The RRSIG RR's Signer's Name field MUST be the name of the zone                                                                                                                                   │
│         //    that contains the RRset.                                                                                                                                                                          │
│         if(rrset.signerName.length > name.length                                                                                                                                                                │
│             || !rrset.signerName.equals(0, name, name.length - rrset.signerName.length))                                                                                                                        │
│         {                                                                                                                                                                                                       │
│             revert InvalidSignerName(name, rrset.signerName);                                                                                                                                                   │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         RRUtils.RRIterator memory proofRR = proof.iterateRRs(0);                                                                                                                                                │
│         // Check the proof                                                                                                                                                                                      │
│         if (proofRR.dnstype == DNSTYPE_DS) {                                                                                                                                                                    │
│             verifyWithDS(rrset, data, proofRR);                                                                                                                                                                 │
│         } else if (proofRR.dnstype == DNSTYPE_DNSKEY) {                                                                                                                                                         │
│             verifyWithKnownKey(rrset, data, proofRR);                                                                                                                                                           │
│         } else {                                                                                                                                                                                                │
│             revert InvalidProofType(proofRR.dnstype);                                                                                                                                                           │
│         }                                                                                                                                                                                                       │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│     "1": "No"                                                                                                                                                                                                   │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have inside code statements that update/accrue interest/exchange rate,                                                                                                                               │
│ Code:                                                                                                                                                                                                           │
│     function _premium(string memory name, uint expires, uint /*duration*/) override internal view returns(uint) {                                                                                               │
│         expires = expires.add(GRACE_PERIOD);                                                                                                                                                                    │
│         if(expires > block.timestamp) {                                                                                                                                                                         │
│             // No premium for renewals                                                                                                                                                                          │
│             return 0;                                                                                                                                                                                           │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         // Calculate the discount off the maximum premium                                                                                                                                                       │
│         uint discount = premiumDecreaseRate.mul(block.timestamp.sub(expires));                                                                                                                                  │
│                                                                                                                                                                                                                 │
│         // If we've run out the premium period, return 0.                                                                                                                                                       │
│         if(discount > initialPremium) {                                                                                                                                                                         │
│             return 0;                                                                                                                                                                                           │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         return initialPremium - discount;                                                                                                                                                                       │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│     "1": "No"                                                                                                                                                                                                   │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have inside code statements that update/accrue interest/exchange rate,                                                                                                                               │
│ Code:                                                                                                                                                                                                           │
│     function timeUntilPremium(uint expires, uint amount) external view returns(uint) {                                                                                                                          │
│         amount = weiToAttoUSD(amount);                                                                                                                                                                          │
│         require(amount <= initialPremium);                                                                                                                                                                      │
│                                                                                                                                                                                                                 │
│         expires = expires.add(GRACE_PERIOD);                                                                                                                                                                    │
│                                                                                                                                                                                                                 │
│         uint discount = initialPremium.sub(amount);                                                                                                                                                             │
│         uint duration = discount.div(premiumDecreaseRate);                                                                                                                                                      │
│         return expires.add(duration);                                                                                                                                                                           │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│     "1": "No"                                                                                                                                                                                                   │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: add or check approval via require/if statements before the token transfer,                                                                                                                           │
│ Code:                                                                                                                                                                                                           │
│     function wrapETH2LD(                                                                                                                                                                                        │
│         string calldata label,                                                                                                                                                                                  │
│         address wrappedOwner,                                                                                                                                                                                   │
│         uint32 fuses,                                                                                                                                                                                           │
│         uint64 expiry,                                                                                                                                                                                          │
│         address resolver                                                                                                                                                                                        │
│     ) public override returns (uint64) {                                                                                                                                                                        │
│         uint256 tokenId = uint256(keccak256(bytes(label)));                                                                                                                                                     │
│         address registrant = registrar.ownerOf(tokenId);                                                                                                                                                        │
│         if (                                                                                                                                                                                                    │
│             registrant != msg.sender &&                                                                                                                                                                         │
│             !isApprovedForAll(registrant, msg.sender) &&                                                                                                                                                        │
│             !registrar.isApprovedForAll(registrant, msg.sender)                                                                                                                                                 │
│         ) {                                                                                                                                                                                                     │
│             revert Unauthorised(                                                                                                                                                                                │
│                 _makeNode(ETH_NODE, bytes32(tokenId)),                                                                                                                                                          │
│                 msg.sender                                                                                                                                                                                      │
│             );                                                                                                                                                                                                  │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         // transfer the token from the user to this contract                                                                                                                                                    │
│         registrar.transferFrom(registrant, address(this), tokenId);                                                                                                                                             │
│                                                                                                                                                                                                                 │
│         // transfer the ens record back to the new owner (this contract)                                                                                                                                        │
│         registrar.reclaim(tokenId, address(this));                                                                                                                                                              │
│                                                                                                                                                                                                                 │
│         return _wrapETH2LD(label, wrappedOwner, fuses, expiry, resolver);                                                                                                                                       │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│     "1": "Yes"                                                                                                                                                                                                  │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────── Single Choice Scenario ─────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: add or check approval via require/if statements before the token transfer, and there is no clear/reset of the approval when the transfer finishes its main branch or encounters exceptions           │
│ Code:                                                                                                                                                                                                           │
│     function wrapETH2LD(                                                                                                                                                                                        │
│         string calldata label,                                                                                                                                                                                  │
│         address wrappedOwner,                                                                                                                                                                                   │
│         uint32 fuses,                                                                                                                                                                                           │
│         uint64 expiry,                                                                                                                                                                                          │
│         address resolver                                                                                                                                                                                        │
│     ) public override returns (uint64) {                                                                                                                                                                        │
│         uint256 tokenId = uint256(keccak256(bytes(label)));                                                                                                                                                     │
│         address registrant = registrar.ownerOf(tokenId);                                                                                                                                                        │
│         if (                                                                                                                                                                                                    │
│             registrant != msg.sender &&                                                                                                                                                                         │
│             !isApprovedForAll(registrant, msg.sender) &&                                                                                                                                                        │
│             !registrar.isApprovedForAll(registrant, msg.sender)                                                                                                                                                 │
│         ) {                                                                                                                                                                                                     │
│             revert Unauthorised(                                                                                                                                                                                │
│                 _makeNode(ETH_NODE, bytes32(tokenId)),                                                                                                                                                          │
│                 msg.sender                                                                                                                                                                                      │
│             );                                                                                                                                                                                                  │
│         }                                                                                                                                                                                                       │
│                                                                                                                                                                                                                 │
│         // transfer the token from the user to this contract                                                                                                                                                    │
│         registrar.transferFrom(registrant, address(this), tokenId);                                                                                                                                             │
│                                                                                                                                                                                                                 │
│         // transfer the ens record back to the new owner (this contract)                                                                                                                                        │
│         registrar.reclaim(tokenId, address(this));                                                                                                                                                              │
│                                                                                                                                                                                                                 │
│         return _wrapETH2LD(label, wrappedOwner, fuses, expiry, resolver);                                                                                                                                       │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ No                                                                                                                                                                                                              │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: add or check approval via require/if statements before the token transfer,                                                                                                                           │
│ Code:                                                                                                                                                                                                           │
│     function wrapETH2LD(                                                                                                                                                                                        │
│         string calldata label,                                                                                                                                                                                  │
│         address wrappedOwner,                                                                                                                                                                                   │
│         uint32 fuses,                                                                                                                                                                                           │
│         uint64 expiry,                                                                                                                                                                                          │
│         address resolver                                                                                                                                                                                        │
│     ) public {                                                                                                                                                                                                  │
│         uint256 tokenId = uint256(keccak256(bytes(label)));                                                                                                                                                     │
│         address registrant = registrar.ownerOf(tokenId);                                                                                                                                                        │
│         registrar.transferFrom(registrant, address(this), tokenId);                                                                                                                                             │
│         registrar.reclaim(tokenId, address(this));                                                                                                                                                              │
│         require(                                                                                                                                                                                                │
│             registrant == msg.sender ||                                                                                                                                                                         │
│                 registrar.isApprovedForAll(registrant, msg.sender),                                                                                                                                             │
│             "Unauthorised"                                                                                                                                                                                      │
│         );                                                                                                                                                                                                      │
│         emit WrapETH2LD(label, wrappedOwner, fuses, expiry, resolver);                                                                                                                                          │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│     "1": "Yes"                                                                                                                                                                                                  │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────── Single Choice Scenario ─────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: add or check approval via require/if statements before the token transfer, and there is no clear/reset of the approval when the transfer finishes its main branch or encounters exceptions           │
│ Code:                                                                                                                                                                                                           │
│     function wrapETH2LD(                                                                                                                                                                                        │
│         string calldata label,                                                                                                                                                                                  │
│         address wrappedOwner,                                                                                                                                                                                   │
│         uint32 fuses,                                                                                                                                                                                           │
│         uint64 expiry,                                                                                                                                                                                          │
│         address resolver                                                                                                                                                                                        │
│     ) public {                                                                                                                                                                                                  │
│         uint256 tokenId = uint256(keccak256(bytes(label)));                                                                                                                                                     │
│         address registrant = registrar.ownerOf(tokenId);                                                                                                                                                        │
│         registrar.transferFrom(registrant, address(this), tokenId);                                                                                                                                             │
│         registrar.reclaim(tokenId, address(this));                                                                                                                                                              │
│         require(                                                                                                                                                                                                │
│             registrant == msg.sender ||                                                                                                                                                                         │
│                 registrar.isApprovedForAll(registrant, msg.sender),                                                                                                                                             │
│             "Unauthorised"                                                                                                                                                                                      │
│         );                                                                                                                                                                                                      │
│         emit WrapETH2LD(label, wrappedOwner, fuses, expiry, resolver);                                                                                                                                          │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ No                                                                                                                                                                                                              │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have inside code statements that update/accrue interest/exchange rate,                                                                                                                               │
│ Code:                                                                                                                                                                                                           │
│   function testIterateRRs() public pure {                                                                                                                                                                       │
│     // a. IN A 3600 127.0.0.1                                                                                                                                                                                   │
│     // b.a. IN A 3600 192.168.1.1                                                                                                                                                                               │
│     bytes memory rrs = hex'0161000001000100000e1000047400000101620161000001000100000e100004c0a80101';                                                                                                           │
│     bytes[2] memory names = ;                                                                                                                                                                                   │
│     bytes[2] memory rdatas = ;                                                                                                                                                                                  │
│     uint i = 0;                                                                                                                                                                                                 │
│     for(RRUtils.RRIterator memory iter = rrs.iterateRRs(0); !iter.done(); iter.next()) {                                                                                                                        │
│       require(uint(iter.dnstype) == 1, "Type matches");                                                                                                                                                         │
│       require(uint(iter.class) == 1, "Class matches");                                                                                                                                                          │
│       require(uint(iter.ttl) == 3600, "TTL matches");                                                                                                                                                           │
│       require(keccak256(iter.name()) == keccak256(names), "Name matches");                                                                                                                                      │
│       require(keccak256(iter.rdata()) == keccak256(rdatas), "Rdata matches");                                                                                                                                   │
│       i++;                                                                                                                                                                                                      │
│     }                                                                                                                                                                                                           │
│     require(i == 2, "Expected 2 records");                                                                                                                                                                      │
│   }                                                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│   "1": "No"                                                                                                                                                                                                     │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
                      Scan Results                       
┏━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Type ┃ Description ┃ Affected Files ┃ Analysis Report ┃
┡━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
└──────┴─────────────┴────────────────┴─────────────────┘
                  Summary                   
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Key                  ┃ Value             ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ Files                │ 87                │
│ Contracts            │ 90                │
│ Functions            │ 124               │
│ Lines of Code        │ 6435              │
│ Used Time            │ 51.69023633003235 │
│ Estimated Cost (USD) │ 0.0046795         │
└──────────────────────┴───────────────────┘
