

  .oooooo.    ooooooooo.   ooooooooooooo  .oooooo..o                                 
 d8P'  `Y8b   `888   `Y88. 8'   888   `8 d8P'    `Y8                                 
888            888   .d88'      888      Y88bo.       .ooooo.   .oooo.   ooo. .oo.   
888            888ooo88P'       888       `"Y8888o.  d88' `"Y8 `P  )88b  `888P"Y88b  
888     ooooo  888              888           `"Y88b 888        .oP"888   888   888  
`88.    .88'   888              888      oo     .d8P 888   .o8 d8(  888   888   888  
 `Y8bood8P'   o888o            o888o     8""88888P'  `Y8bod8P' `Y888""8o o888o o888o                                                        


                                                                   

[14:25:31] Loaded 10 rules                                                                                                                                                                                                                  tasks.py:119
           Traceback (most recent call last):                                                                                                                                                                                               tasks.py:126
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/falcon/falcon.py", line 90, in __init__                                                                                                          
               crytic_compile = CryticCompile(target, **kwargs)                                                                                                                                                                                         
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/crytic_compile/crytic_compile.py", line 131, in __init__                                                                                         
               self._compile(**kwargs)                                                                                                                                                                                                                  
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/crytic_compile/crytic_compile.py", line 553, in _compile                                                                                         
               self._platform.compile(self, **kwargs)                                                                                                                                                                                                   
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/crytic_compile/platform/solc.py", line 149, in compile                                                                                           
               targets_json = _get_targets_json(compilation_unit, self._target, **kwargs)                                                                                                                                                               
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/crytic_compile/platform/solc.py", line 278, in _get_targets_json                                                                                 
               return _run_solc(                                                                                                                                                                                                                        
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/crytic_compile/platform/solc.py", line 483, in _run_solc                                                                                         
               raise InvalidCompilation(                                                                                                                                                                                                                
           crytic_compile.platform.exceptions.InvalidCompilation: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0x152649ea73beab28c5b49b26eb48f7ead6d4c898_eth is a directory. Expected a Solidity file when not using a                   
           compilation framework.                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                        
           During handling of the above exception, another exception occurred:                                                                                                                                                                          
                                                                                                                                                                                                                                                        
           Traceback (most recent call last):                                                                                                                                                                                                           
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/src/tasks.py", line 124, in simple_cli                                                                                                                                              
               falcon_instance = compile_project(source_dir)                                                                                                                                                                                            
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/src/tasks.py", line 103, in compile_project                                                                                                                                         
               return falcon.Falcon(abs_path)                                                                                                                                                                                                           
             File "/home/owen/Documents/GitHub/GPTScan-Bigger-Model/.venv/lib/python3.10/site-packages/falcon/falcon.py", line 94, in __init__                                                                                                          
               raise FalconError(f"Invalid compilation: \n{str(e)}")                                                                                                                                                                                    
           falcon.exceptions.FalconError: Invalid compilation:                                                                                                                                                                                          
           /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0x152649ea73beab28c5b49b26eb48f7ead6d4c898_eth is a directory. Expected a Solidity file when not using a compilation framework.                                                   
                                                                                                                                                                                                                                                        
           Compile failed.                                                                                                                                                                                                                  tasks.py:127
           Since the compilation is failed, some static analysis tool may not be enabled, which may cause lower precision and recall.                                                                                                       tasks.py:128
[12/08/24 14:25:32] INFO     antlr4helper.callgraph: In whitelist: Ownable._transferOwnership(address) returns()                                                                                                                         callgraph.py:21
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ──────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have inside code statements that update/accrue interest/exchange rate,                                                                                                                                                                    │
│ Code:                                                                                                                                                                                                                                                │
│     function _ld2sd(uint _amount) internal virtual view returns (uint64) {                                                                                                                                                                           │
│         uint amountSD = _amount / _ld2sdRate();                                                                                                                                                                                                      │
│         require(amountSD <= type(uint64).max, "OFTCore: amountSD overflow");                                                                                                                                                                         │
│         return uint64(amountSD);                                                                                                                                                                                                                     │
│     }                                                                                                                                                                                                                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── Response ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {"1": "No"}                                                                                                                                                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
                      Scan Results                       
┏━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Type ┃ Description ┃ Affected Files ┃ Analysis Report ┃
┡━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
└──────┴─────────────┴────────────────┴─────────────────┘
                     Summary                     
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Key                  ┃ Value                  ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Files                │ 18                     │
│ Contracts            │ 18                     │
│ Functions            │ 38                     │
│ Lines of Code        │ 1790                   │
│ Used Time            │ 1.4735784530639648     │
│ Estimated Cost (USD) │ 0.00027600000000000004 │
└──────────────────────┴────────────────────────┘