

  .oooooo.    ooooooooo.   ooooooooooooo  .oooooo..o                                 
 d8P'  `Y8b   `888   `Y88. 8'   888   `8 d8P'    `Y8                                 
888            888   .d88'      888      Y88bo.       .ooooo.   .oooo.   ooo. .oo.   
888            888ooo88P'       888       `"Y8888o.  d88' `"Y8 `P  )88b  `888P"Y88b  
888     ooooo  888              888           `"Y88b 888        .oP"888   888   888  
`88.    .88'   888              888      oo     .d8P 888   .o8 d8(  888   888   888  
 `Y8bood8P'   o888o            o888o     8""88888P'  `Y8bod8P' `Y888""8o o888o o888o                                                        


                                                                   

[18:12:24] Loaded 10 rules                                                                                                                                                                             tasks.py:119
[12/08/24 18:12:24] INFO     CryticCompile: 'npx hardhat clean' running (wd: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0x25d887ce7a35172c62febfd67a1856f20faebb00_bsc)            subprocess.py:41
[12/08/24 18:12:26] INFO     CryticCompile: 'npx hardhat clean --global' running (wd: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0x25d887ce7a35172c62febfd67a1856f20faebb00_bsc)   subprocess.py:41
[12/08/24 18:12:29] INFO     CryticCompile: 'npx hardhat compile --force' running (wd: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0x25d887ce7a35172c62febfd67a1856f20faebb00_bsc)  subprocess.py:41
[18:12:30] Traceback (most recent call last):                                                                                                                                                          tasks.py:126
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
           /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0x25d887ce7a35172c62febfd67a1856f20faebb00_bsc/artifacts/build-info is not a directory.                                                      
                                                                                                                                                                                                                   
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
           /home/owen/Documents/GitHub/GPTScan-Bigger-Model/eval_data/0x25d887ce7a35172c62febfd67a1856f20faebb00_bsc/artifacts/build-info is not a directory.                                                      
                                                                                                                                                                                                                   
           Compile failed.                                                                                                                                                                             tasks.py:127
           Since the compilation is failed, some static analysis tool may not be enabled, which may cause lower precision and recall.                                                                  tasks.py:128
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have inside code statements that update/accrue interest/exchange rate,                                                                                                                               │
│ Code:                                                                                                                                                                                                           │
│     function _ld2sd(uint _amount) internal virtual view returns (uint64) {                                                                                                                                      │
│         uint amountSD = _amount / _ld2sdRate();                                                                                                                                                                 │
│         require(amountSD <= type(uint64).max, "OFTCore: amountSD overflow");                                                                                                                                    │
│         return uint64(amountSD);                                                                                                                                                                                │
│     }                                                                                                                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│     "1": "No"                                                                                                                                                                                                   │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
                      Scan Results                       
┏━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Type ┃ Description ┃ Affected Files ┃ Analysis Report ┃
┡━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
└──────┴─────────────┴────────────────┴─────────────────┘
                  Summary                  
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Key                  ┃ Value            ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ Files                │ 15               │
│ Contracts            │ 15               │
│ Functions            │ 36               │
│ Lines of Code        │ 1449             │
│ Used Time            │ 8.60348129272461 │
│ Estimated Cost (USD) │ 0.000282         │
└──────────────────────┴──────────────────┘
