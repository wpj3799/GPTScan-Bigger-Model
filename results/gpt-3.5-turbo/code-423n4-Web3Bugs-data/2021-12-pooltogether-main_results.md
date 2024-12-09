

  .oooooo.    ooooooooo.   ooooooooooooo  .oooooo..o                                 
 d8P'  `Y8b   `888   `Y88. 8'   888   `8 d8P'    `Y8                                 
888            888   .d88'      888      Y88bo.       .ooooo.   .oooo.   ooo. .oo.   
888            888ooo88P'       888       `"Y8888o.  d88' `"Y8 `P  )88b  `888P"Y88b  
888     ooooo  888              888           `"Y88b 888        .oP"888   888   888  
`88.    .88'   888              888      oo     .d8P 888   .o8 d8(  888   888   888  
 `Y8bood8P'   o888o            o888o     8""88888P'  `Y8bod8P' `Y888""8o o888o o888o                                                        


                                                                   

[19:25:21] Loaded 10 rules                                                                                                                                                                             tasks.py:119
[12/08/24 19:25:21] INFO     CryticCompile: 'npx hardhat clean' running (wd: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/datasets/code-423n4-Web3Bugs-data/2021-12-pooltogether-main)         subprocess.py:41
[12/08/24 19:25:23] INFO     CryticCompile: 'npx hardhat clean --global' running (wd:                                                                                                              subprocess.py:41
                             /home/owen/Documents/GitHub/GPTScan-Bigger-Model/datasets/code-423n4-Web3Bugs-data/2021-12-pooltogether-main)                                                                         
[12/08/24 19:25:25] INFO     CryticCompile: 'npx hardhat compile --force' running (wd:                                                                                                             subprocess.py:41
                             /home/owen/Documents/GitHub/GPTScan-Bigger-Model/datasets/code-423n4-Web3Bugs-data/2021-12-pooltogether-main)                                                                         
[19:25:26] Traceback (most recent call last):                                                                                                                                                          tasks.py:126
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
           /home/owen/Documents/GitHub/GPTScan-Bigger-Model/datasets/code-423n4-Web3Bugs-data/2021-12-pooltogether-main/artifacts/build-info is not a directory.                                                   
                                                                                                                                                                                                                   
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
           /home/owen/Documents/GitHub/GPTScan-Bigger-Model/datasets/code-423n4-Web3Bugs-data/2021-12-pooltogether-main/artifacts/build-info is not a directory.                                                   
                                                                                                                                                                                                                   
           Compile failed.                                                                                                                                                                             tasks.py:127
           Since the compilation is failed, some static analysis tool may not be enabled, which may cause lower precision and recall.                                                                  tasks.py:128
                      Scan Results                       
┏━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Type ┃ Description ┃ Affected Files ┃ Analysis Report ┃
┡━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
└──────┴─────────────┴────────────────┴─────────────────┘
                  Summary                   
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Key                  ┃ Value             ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ Files                │ 0                 │
│ Contracts            │ 0                 │
│ Functions            │ 0                 │
│ Lines of Code        │ 0                 │
│ Used Time            │ 5.822059154510498 │
│ Estimated Cost (USD) │ 0.0               │
└──────────────────────┴───────────────────┘
