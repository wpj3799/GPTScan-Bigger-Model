

  .oooooo.    ooooooooo.   ooooooooooooo  .oooooo..o                                 
 d8P'  `Y8b   `888   `Y88. 8'   888   `8 d8P'    `Y8                                 
888            888   .d88'      888      Y88bo.       .ooooo.   .oooo.   ooo. .oo.   
888            888ooo88P'       888       `"Y8888o.  d88' `"Y8 `P  )88b  `888P"Y88b  
888     ooooo  888              888           `"Y88b 888        .oP"888   888   888  
`88.    .88'   888              888      oo     .d8P 888   .o8 d8(  888   888   888  
 `Y8bood8P'   o888o            o888o     8""88888P'  `Y8bod8P' `Y888""8o o888o o888o                                                        


                                                                   

[19:39:54] Loaded 10 rules                                                                                                                                                                             tasks.py:119
[12/08/24 19:39:54] INFO     CryticCompile: 'npx hardhat clean' running (wd: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/datasets/code-423n4-Web3Bugs-data/2022-02-foundation-main)           subprocess.py:41
[12/08/24 19:39:56] ERROR    CryticCompile: 'npx' returned non-zero exit code 127                                                                                                                  subprocess.py:60
                    ERROR    CryticCompile: sh: 1: hardhat: not found                                                                                                                              subprocess.py:68
                    INFO     CryticCompile: 'npx hardhat clean --global' running (wd: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/datasets/code-423n4-Web3Bugs-data/2022-02-foundation-main)  subprocess.py:41
[12/08/24 19:39:58] ERROR    CryticCompile: 'npx' returned non-zero exit code 127                                                                                                                  subprocess.py:60
                    ERROR    CryticCompile: sh: 1: hardhat: not found                                                                                                                              subprocess.py:68
[12/08/24 19:39:59] INFO     CryticCompile: Problem executing hardhat: sh: 1: hardhat: not found                                                                                                     hardhat.py:327
                                                                                                                                                                                                                   
                    INFO     CryticCompile: 'npx hardhat compile --force' running (wd: /home/owen/Documents/GitHub/GPTScan-Bigger-Model/datasets/code-423n4-Web3Bugs-data/2022-02-foundation-main) subprocess.py:41
[12/08/24 19:40:01] ERROR    CryticCompile: 'npx' returned non-zero exit code 127                                                                                                                  subprocess.py:60
                    ERROR    CryticCompile: sh: 1: hardhat: not found                                                                                                                              subprocess.py:68
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: have inside code statements that update/accrue interest/exchange rate,                                                                                                                               │
│ Code:                                                                                                                                                                                                           │
│   function adminAccountMigration(                                                                                                                                                                               │
│     uint256[] calldata listedAuctionIds,                                                                                                                                                                        │
│     address originalAddress,                                                                                                                                                                                    │
│     address payable newAddress,                                                                                                                                                                                 │
│     bytes memory signature                                                                                                                                                                                      │
│   ) external onlyFoundationOperator {                                                                                                                                                                           │
│     // Validate the owner of the original account has approved this change.                                                                                                                                     │
│     originalAddress.requireAuthorizedAccountMigration(newAddress, signature);                                                                                                                                   │
│                                                                                                                                                                                                                 │
│     unchecked {                                                                                                                                                                                                 │
│       // The array length cannot overflow 256 bits.                                                                                                                                                             │
│       for (uint256 i = 0; i < listedAuctionIds.length; ++i) {                                                                                                                                                   │
│         uint256 auctionId = listedAuctionIds;                                                                                                                                                                   │
│         ReserveAuction storage auction = auctionIdToAuction;                                                                                                                                                    │
│         if (auction.seller != address(0)) {                                                                                                                                                                     │
│           // Only if the auction was found and not finalized before this transaction.                                                                                                                           │
│                                                                                                                                                                                                                 │
│           if (auction.seller != originalAddress) {                                                                                                                                                              │
│             // Confirm that the signature approval was the correct owner of this auction.                                                                                                                       │
│             revert NFTMarketReserveAuction_Cannot_Migrate_Non_Matching_Seller(auction.seller);                                                                                                                  │
│           }                                                                                                                                                                                                     │
│                                                                                                                                                                                                                 │
│           // Update the auction's seller address.                                                                                                                                                               │
│           auction.seller = newAddress;                                                                                                                                                                          │
│                                                                                                                                                                                                                 │
│           emit ReserveAuctionSellerMigrated(auctionId, originalAddress, newAddress);                                                                                                                            │
│         }                                                                                                                                                                                                       │
│       }                                                                                                                                                                                                         │
│     }                                                                                                                                                                                                           │
│   }                                                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│     "1": "No"                                                                                                                                                                                                   │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────── Multiple Choice Scenarios ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: add or check approval via require/if statements before the token transfer,                                                                                                                           │
│ Code:                                                                                                                                                                                                           │
│   function buyFromPrivateSaleFor(                                                                                                                                                                               │
│     IERC721 nftContract,                                                                                                                                                                                        │
│     uint256 tokenId,                                                                                                                                                                                            │
│     uint256 amount,                                                                                                                                                                                             │
│     uint256 deadline,                                                                                                                                                                                           │
│     uint8 v,                                                                                                                                                                                                    │
│     bytes32 r,                                                                                                                                                                                                  │
│     bytes32 s                                                                                                                                                                                                   │
│   ) public payable nonReentrant {                                                                                                                                                                               │
│     if (deadline < block.timestamp) {                                                                                                                                                                           │
│       // The signed message from the seller has expired.                                                                                                                                                        │
│       revert NFTMarketPrivateSale_Sale_Expired();                                                                                                                                                               │
│     } else if (deadline > block.timestamp + 2 days) {                                                                                                                                                           │
│       // Private sales typically expire in 24 hours, but 2 days is used here in order to ensure                                                                                                                 │
│       // that transactions do not fail due to a minor timezone error or similar during signing.                                                                                                                 │
│                                                                                                                                                                                                                 │
│       // This prevents malicious actors from requesting signatures that never expire.                                                                                                                           │
│       revert NFTMarketPrivateSale_Can_Be_Offered_For_24Hrs_Max();                                                                                                                                               │
│     }                                                                                                                                                                                                           │
│                                                                                                                                                                                                                 │
│     if (amount > msg.value) {                                                                                                                                                                                   │
│       // Withdraw additional ETH required from their available FETH balance.                                                                                                                                    │
│                                                                                                                                                                                                                 │
│       unchecked {                                                                                                                                                                                               │
│         // The if above ensures delta will not underflow                                                                                                                                                        │
│         uint256 delta = amount - msg.value;                                                                                                                                                                     │
│         feth.marketWithdrawFrom(msg.sender, delta);                                                                                                                                                             │
│       }                                                                                                                                                                                                         │
│     } else if (amount < msg.value) {                                                                                                                                                                            │
│       // The terms of the sale cannot change, so if too much ETH is sent then something went wrong.                                                                                                             │
│       revert NFTMarketPrivateSale_Too_Much_Value_Provided();                                                                                                                                                    │
│     }                                                                                                                                                                                                           │
│                                                                                                                                                                                                                 │
│     // The seller must have the NFT in their wallet when this function is called,                                                                                                                               │
│     // otherwise the signature verification below will fail.                                                                                                                                                    │
│     address payable seller = payable(nftContract.ownerOf(tokenId));                                                                                                                                             │
│                                                                                                                                                                                                                 │
│     // Scoping this block to avoid a stack too deep error                                                                                                                                                       │
│     {                                                                                                                                                                                                           │
│       bytes32 digest = keccak256(                                                                                                                                                                               │
│         abi.encodePacked(                                                                                                                                                                                       │
│           "\x19\x01",                                                                                                                                                                                           │
│           DOMAIN_SEPARATOR,                                                                                                                                                                                     │
│           keccak256(abi.encode(BUY_FROM_PRIVATE_SALE_TYPEHASH, nftContract, tokenId, msg.sender, amount, deadline))                                                                                             │
│         )                                                                                                                                                                                                       │
│       );                                                                                                                                                                                                        │
│                                                                                                                                                                                                                 │
│       // Revert if the signature is invalid, the terms are not as expected, or if the seller transferred the NFT.                                                                                               │
│       if (ecrecover(digest, v, r, s) != seller) {                                                                                                                                                               │
│         revert NFTMarketPrivateSale_Signature_Verification_Failed();                                                                                                                                            │
│       }                                                                                                                                                                                                         │
│     }                                                                                                                                                                                                           │
│                                                                                                                                                                                                                 │
│     // This should revert if the seller has not given the market contract approval.                                                                                                                             │
│     nftContract.transferFrom(seller, msg.sender, tokenId);                                                                                                                                                      │
│                                                                                                                                                                                                                 │
│     // Distribute revenue for this sale.                                                                                                                                                                        │
│     (uint256 f8nFee, uint256 creatorFee, uint256 ownerRev) = _distributeFunds(                                                                                                                                  │
│       address(nftContract),                                                                                                                                                                                     │
│       tokenId,                                                                                                                                                                                                  │
│       seller,                                                                                                                                                                                                   │
│       amount                                                                                                                                                                                                    │
│     );                                                                                                                                                                                                          │
│                                                                                                                                                                                                                 │
│     emit PrivateSaleFinalized(                                                                                                                                                                                  │
│       address(nftContract),                                                                                                                                                                                     │
│       tokenId,                                                                                                                                                                                                  │
│       seller,                                                                                                                                                                                                   │
│       msg.sender,                                                                                                                                                                                               │
│       f8nFee,                                                                                                                                                                                                   │
│       creatorFee,                                                                                                                                                                                               │
│       ownerRev,                                                                                                                                                                                                 │
│       deadline                                                                                                                                                                                                  │
│     );                                                                                                                                                                                                          │
│   }                                                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ {                                                                                                                                                                                                               │
│   "1": "Yes"                                                                                                                                                                                                    │
│ }                                                                                                                                                                                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────────────────────────────────────────────────────────────────── Single Choice Scenario ─────────────────────────────────────────────────────────────────────────────────────────────╮
│ Knowledge: add or check approval via require/if statements before the token transfer, and there is no clear/reset of the approval when the transfer finishes its main branch or encounters exceptions           │
│ Code:                                                                                                                                                                                                           │
│   function buyFromPrivateSaleFor(                                                                                                                                                                               │
│     IERC721 nftContract,                                                                                                                                                                                        │
│     uint256 tokenId,                                                                                                                                                                                            │
│     uint256 amount,                                                                                                                                                                                             │
│     uint256 deadline,                                                                                                                                                                                           │
│     uint8 v,                                                                                                                                                                                                    │
│     bytes32 r,                                                                                                                                                                                                  │
│     bytes32 s                                                                                                                                                                                                   │
│   ) public payable nonReentrant {                                                                                                                                                                               │
│     if (deadline < block.timestamp) {                                                                                                                                                                           │
│       // The signed message from the seller has expired.                                                                                                                                                        │
│       revert NFTMarketPrivateSale_Sale_Expired();                                                                                                                                                               │
│     } else if (deadline > block.timestamp + 2 days) {                                                                                                                                                           │
│       // Private sales typically expire in 24 hours, but 2 days is used here in order to ensure                                                                                                                 │
│       // that transactions do not fail due to a minor timezone error or similar during signing.                                                                                                                 │
│                                                                                                                                                                                                                 │
│       // This prevents malicious actors from requesting signatures that never expire.                                                                                                                           │
│       revert NFTMarketPrivateSale_Can_Be_Offered_For_24Hrs_Max();                                                                                                                                               │
│     }                                                                                                                                                                                                           │
│                                                                                                                                                                                                                 │
│     if (amount > msg.value) {                                                                                                                                                                                   │
│       // Withdraw additional ETH required from their available FETH balance.                                                                                                                                    │
│                                                                                                                                                                                                                 │
│       unchecked {                                                                                                                                                                                               │
│         // The if above ensures delta will not underflow                                                                                                                                                        │
│         uint256 delta = amount - msg.value;                                                                                                                                                                     │
│         feth.marketWithdrawFrom(msg.sender, delta);                                                                                                                                                             │
│       }                                                                                                                                                                                                         │
│     } else if (amount < msg.value) {                                                                                                                                                                            │
│       // The terms of the sale cannot change, so if too much ETH is sent then something went wrong.                                                                                                             │
│       revert NFTMarketPrivateSale_Too_Much_Value_Provided();                                                                                                                                                    │
│     }                                                                                                                                                                                                           │
│                                                                                                                                                                                                                 │
│     // The seller must have the NFT in their wallet when this function is called,                                                                                                                               │
│     // otherwise the signature verification below will fail.                                                                                                                                                    │
│     address payable seller = payable(nftContract.ownerOf(tokenId));                                                                                                                                             │
│                                                                                                                                                                                                                 │
│     // Scoping this block to avoid a stack too deep error                                                                                                                                                       │
│     {                                                                                                                                                                                                           │
│       bytes32 digest = keccak256(                                                                                                                                                                               │
│         abi.encodePacked(                                                                                                                                                                                       │
│           "\x19\x01",                                                                                                                                                                                           │
│           DOMAIN_SEPARATOR,                                                                                                                                                                                     │
│           keccak256(abi.encode(BUY_FROM_PRIVATE_SALE_TYPEHASH, nftContract, tokenId, msg.sender, amount, deadline))                                                                                             │
│         )                                                                                                                                                                                                       │
│       );                                                                                                                                                                                                        │
│                                                                                                                                                                                                                 │
│       // Revert if the signature is invalid, the terms are not as expected, or if the seller transferred the NFT.                                                                                               │
│       if (ecrecover(digest, v, r, s) != seller) {                                                                                                                                                               │
│         revert NFTMarketPrivateSale_Signature_Verification_Failed();                                                                                                                                            │
│       }                                                                                                                                                                                                         │
│     }                                                                                                                                                                                                           │
│                                                                                                                                                                                                                 │
│     // This should revert if the seller has not given the market contract approval.                                                                                                                             │
│     nftContract.transferFrom(seller, msg.sender, tokenId);                                                                                                                                                      │
│                                                                                                                                                                                                                 │
│     // Distribute revenue for this sale.                                                                                                                                                                        │
│     (uint256 f8nFee, uint256 creatorFee, uint256 ownerRev) = _distributeFunds(                                                                                                                                  │
│       address(nftContract),                                                                                                                                                                                     │
│       tokenId,                                                                                                                                                                                                  │
│       seller,                                                                                                                                                                                                   │
│       amount                                                                                                                                                                                                    │
│     );                                                                                                                                                                                                          │
│                                                                                                                                                                                                                 │
│     emit PrivateSaleFinalized(                                                                                                                                                                                  │
│       address(nftContract),                                                                                                                                                                                     │
│       tokenId,                                                                                                                                                                                                  │
│       seller,                                                                                                                                                                                                   │
│       msg.sender,                                                                                                                                                                                               │
│       f8nFee,                                                                                                                                                                                                   │
│       creatorFee,                                                                                                                                                                                               │
│       ownerRev,                                                                                                                                                                                                 │
│       deadline                                                                                                                                                                                                  │
│     );                                                                                                                                                                                                          │
│   }                                                                                                                                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─────────────────────────────────────────────────────────────────────────────────────────────────── Response ────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ No                                                                                                                                                                                                              │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
                      Scan Results                       
┏━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Type ┃ Description ┃ Affected Files ┃ Analysis Report ┃
┡━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
└──────┴─────────────┴────────────────┴─────────────────┘
                   Summary                   
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃ Key                  ┃ Value              ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ Files                │ 33                 │
│ Contracts            │ 33                 │
│ Functions            │ 58                 │
│ Lines of Code        │ 4392               │
│ Used Time            │ 14.644042730331421 │
│ Estimated Cost (USD) │ 0.002705           │
└──────────────────────┴────────────────────┘
