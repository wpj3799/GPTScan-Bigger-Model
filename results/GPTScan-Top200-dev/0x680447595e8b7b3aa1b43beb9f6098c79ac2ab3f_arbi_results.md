

  .oooooo.    ooooooooo.   ooooooooooooo  .oooooo..o                                 
 d8P'  `Y8b   `888   `Y88. 8'   888   `8 d8P'    `Y8                                 
888            888   .d88'      888      Y88bo.       .ooooo.   .oooo.   ooo. .oo.   
888            888ooo88P'       888       `"Y8888o.  d88' `"Y8 `P  )88b  `888P"Y88b  
888     ooooo  888              888           `"Y88b 888        .oP"888   888   888  
`88.    .88'   888              888      oo     .d8P 888   .o8 d8(  888   888   888  
 `Y8bood8P'   o888o            o888o     8""88888P'  `Y8bod8P' `Y888""8o o888o o888o                                                        


                                                                   

[14:34:09] Loaded 10 rules                                                                                                                                                                                                                  tasks.py:119
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
           crytic_compile.platform.exceptions.InvalidCompilation: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0x680447595e8b7b3aa1b43beb9f6098c79ac2ab3f_arbi is a directory. Expected a Solidity file when not using a                  
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
           /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0x680447595e8b7b3aa1b43beb9f6098c79ac2ab3f_arbi is a directory. Expected a Solidity file when not using a compilation framework.                                                  
                                                                                                                                                                                                                                                        
           Compile failed.                                                                                                                                                                                                                  tasks.py:127
           Since the compilation is failed, some static analysis tool may not be enabled, which may cause lower precision and recall.                                                                                                       tasks.py:128
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
│ Contracts            │ 3                  │
│ Functions            │ 2                  │
│ Lines of Code        │ 56                 │
│ Used Time            │ 0.6080992221832275 │
│ Estimated Cost (USD) │ 0.0                │
└──────────────────────┴────────────────────┘
