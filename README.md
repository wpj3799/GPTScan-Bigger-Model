# GPTScan_Bigger_Model<br />
Version 2 of the GPTScan project by Sun et al.<br />
REF: [https://github.com/GPTScan/GPTScan](https://github.com/GPTScan/GPTScan)<br />

## Description

Using ChatGPT for logic vulnerability detection.

## How to Use

1. Install dependencies,

- Usable only in UNIX environment (Tested in Ubuntu 24.0.1 LTS)
- Requires Python 3.10+ `apt-get install python3`
- Requires Java 11+ `apt-get install default-jre`
- Requires Node.js/nvm 0.40+ [https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating)
- Requires solc 0.8+ `add-apt-repository ppa:ethereum/Ethereum & apt update & apt-get install solc`
- Install Python dependencies: `pip install -r requirements.txt`

2. GPTScan Usage

Update `src/config.py` with the:
- GPT_API_KEY
- GPT_Model_Version

Move Solidity files to a usable directory following the directory structure provided by MetaTrustLabs/GPTScan-Top200 where each .sol file is in its own folder within the SOURCECODE_DIRECTORY. i.e /data/0x000000/test.sol where /data is SOURCECODE_DIRECTORY.
NOTE: First run may be slow due to hardhat configuration and Solidity compilation.

```shell
./run_gptscan.sh /SOURCECODE_DIRECTORY
```

3. Check the output

The output results are located in each file’s directory:<br />
- Analysis output: `/data/0x000000/gptscan_output.json`<br />
- Metadata output: `/data/0x000000/gptscan_output.metadata.json`<br />
- GPTScan stdout: `/data/0x000000/gptscan_results.md`<br />

An example run of GPTScan on a Smart Contract HardHat project has been provided in the `example_data_source` directory. Utilize this output as a reference.<br />


## Supported Project Types

Currently supported project types include:
- Single file, i.e., a single `.sol` file
- Multi-file, i.e., a directory with multiple `.sol` files, without any other external dependencies
- Hardhat projects

## Dataset

Dataset used to evaluate GPTScan in the paper, are the following:<br />
1. Web3Bugs: [https://github.com/MetaTrustLabs/GPTScan-Web3Bugs](https://github.com/MetaTrustLabs/GPTScan-Web3Bugs) For some reason MetaTrustLabs does not include the Solidity files, get them from here [https://github.com/code-423n4](https://github.com/code-423n4)<br />
2. DefiHacks: [https://github.com/MetaTrustLabs/GPTScan-DefiHacks](https://github.com/MetaTrustLabs/GPTScan-DefiHacks) For some reason MetaTrustLabs does not include the Solidity files, get them from here: [https://github.com/SunWeb3Sec/DeFiHackLabs](https://github.com/SunWeb3Sec/DeFiHackLabs) or its fork: [https://github.com/skyonedot/DeFiHackLabs](https://github.com/skyonedot/DeFiHackLabs)<br />
3. Top200: [https://github.com/MetaTrustLabs/GPTScan-Top200](https://github.com/MetaTrustLabs/GPTScan-Top200)<br />

## Credits
Rochester Institute of Technology<br />
Golisano College of Computer Science and Information Technology<br />
Department of Cybersecurity<br />
CSEC 795 : Advanced Software Security<br />
