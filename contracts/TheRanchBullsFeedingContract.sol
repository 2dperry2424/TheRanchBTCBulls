// SPDX-License-Identifier: MIT
pragma solidity 0.8.7;

/*    
🅣🅗🅔🅡🅐🅝🅒🅗_🅑🅤🅛🅛🅢_➋⓿➋➋
*/


import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";
import "@chainlink/contracts/src/v0.8/interfaces/KeeperCompatibleInterface.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import { IERC2981, IERC165 } from "@openzeppelin/contracts/interfaces/IERC2981.sol";


error Raffle__UpkeepNotNeeded (uint256 USDCRewardsForAddress, uint256 numPlayers, uint256 raffleMintState);
error Raffle__RaffleIsProcessing();
error Minting_ExceedsTotalBulls();
error Minting_ExceedsMintsPerTx();
error Minting_CantMintZero();
error Minting_PublicSaleNotLive();
error Contract_ContractPaused_CheckSocials();

contract TheRanchBullsFeedingContract is 
    ERC721Enumerable,
    IERC2981,
    Ownable,
    ReentrancyGuard {
    
    using Strings for uint256;
    using SafeERC20 for IERC20;
    using Counters for Counters.Counter;
    Counters.Counter private _tokenSupply;

    address public usdcTokenContract;
    address public TheRanchBullsMintAndReward;
    uint public usdcTokenDecimals = 6;

    // coreTeam Addresses
    address public coreTeam_1;

    // Minting 
    uint256 public mintingCost = 150;  // USDC.e
    uint public nftTotalCount = 10000;

    bool public publicSaleLive = false;
    bool public paused = true;

    mapping(address => uint) public userMintCount;  // How many bulls did an address mint


    // NFT INFO 
    string private _tokenBaseURI;
    string private baseURI;
    string private baseExtension = ".json";
 

   


    event fundAndRewardEvent(
            uint256 indexed _totalAmountDeposit,
            uint indexed _startingIndex,
            uint indexed _endingIndex
    );

  

    constructor(
        string memory _initBaseURI

    ) 
        ERC721("TheRanch_BTC_BULLS", "TRBB") {
        setBaseURI(_initBaseURI);  
    }


   // MINTING
    /**
     * @dev This is the function does the following things:
     * 0. Only works if the raffle is NOT PROCESSING, This only happens once a day for a small amount of time. 
     * 1. Allows users to mint new NFTs 1 - 10 per tx 
     * 2. Updates Mapping for their total count of mints
     * 3. Uses a referral/partners system to see who gets the referral bonus.
     * 4. Enters user into the daily raffle if they chose to do so. 
     * 5. If msg.sender elects to enter raffle, 95% goes to btcMinersFund, if they do not, 98% does. 
    */
    function mint(uint256 _tokenQuantity, bool _enterRaffle) public payable {
        if (paused) { revert Contract_ContractPaused_CheckSocials();}
        if (!publicSaleLive) { revert Minting_PublicSaleNotLive();}
        if (_tokenQuantity ==  0) { revert Minting_CantMintZero();}
        if (_tokenQuantity > 100) {revert Minting_ExceedsMintsPerTx();}
        if (_tokenSupply.current() + _tokenQuantity > nftTotalCount) {revert Minting_ExceedsTotalBulls();}


        IERC20 usdcToken = IERC20(usdcTokenContract);
        uint256 minting_cost_per_bull = mintingCost * 10 ** usdcTokenDecimals;
    
        uint256 totalTransactionCost = minting_cost_per_bull * _tokenQuantity;
        //require(msg.value == totalTransactionCost, "msg.value not equal to total minting transaction cost.");
        usdcToken.safeTransferFrom(msg.sender, address(this), (totalTransactionCost));

        for(uint256 i = 0; i < _tokenQuantity; i++) {
            _tokenSupply.increment();
            _safeMint(msg.sender, _tokenSupply.current());
        }

        //update the mint count for msg.sender
        userMintCount[msg.sender] += _tokenQuantity;
    }






     // Reward Conctract Interaction
    function transferUSDCToBullsMintandRewardContract(uint256 _amtToTransfer) internal {
        require(address(usdcTokenContract) != address(0), "ERROR: The minting token contract must be set first.");
        require(address(TheRanchBullsMintAndReward) != address(0), "ERROR: The Reward Contract must be set first.");
        IERC20 tokenContract = IERC20(usdcTokenContract);
        tokenContract.safeTransfer(TheRanchBullsMintAndReward, _amtToTransfer);

    }



    // Contract Funding / Withdrawing / Transferring
    function fund() public payable {}

    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    function withdrawToken(address _tokenContract, uint256 _amount) external onlyOwner {
        IERC20 tokenContract = IERC20(_tokenContract);
        tokenContract.safeTransfer(msg.sender, _amount);
    }




    /** Getter Functions */

    function getMintCountForAddress(address _address) public view returns (uint) {
        return userMintCount[_address];
    }


    function walletOfOwner(address _owner) public view returns (uint256[] memory) {
        uint256 ownerTokenCount = balanceOf(_owner);
        uint256[] memory tokenIds = new uint256[](ownerTokenCount);
        for (uint256 i; i < ownerTokenCount; i++) {
            tokenIds[i] = tokenOfOwnerByIndex(_owner, i);
        }
        return tokenIds;
    }

 

   // METADATA
    function _baseURI() internal view virtual override returns (string memory) {
        return baseURI;
    }

    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId),"ERC721Metadata: URI query for nonexistent token");
        string memory currentBaseURI = _baseURI();
        return bytes(currentBaseURI).length > 0 ? string(abi.encodePacked(currentBaseURI, tokenId.toString(), baseExtension)) : "";
    }

    // ERC165
    function supportsInterface(bytes4 interfaceId) public view override(ERC721Enumerable, IERC165) returns (bool) {
        return interfaceId == type(IERC2981).interfaceId || super.supportsInterface(interfaceId);
    }

    // IERC2981
    function royaltyInfo(uint256 _tokenId, uint256 _salePrice) external view override returns (address, uint256 royaltyAmount) {
        _tokenId; // silence solc warning
        royaltyAmount = _salePrice * 10 / 100;  // 10%
        return (coreTeam_1, royaltyAmount);
    }


    // Contract Control _ OnlyOwner
    function setBaseURI(string memory _newBaseURI) public onlyOwner {
            baseURI = _newBaseURI;
    }


    function setBaseExtension(string memory _newBaseExtension) external onlyOwner {
            baseExtension = _newBaseExtension;
    }


    function togglePublicSaleStatus() external onlyOwner {
        require(address(usdcTokenContract) != address(0), "ERROR: The usdcTokenContract address must be set prior to any minting");
        publicSaleLive = !publicSaleLive;
    }

    function togglePauseStatus() external onlyOwner {
        paused = !paused;
    }

    function setCoreTeam_1_Address(address _coreTeam_1) public onlyOwner {
        require(address(_coreTeam_1) != address(0), "ERROR: The coreTeam_1 address can't be address(0)");
        coreTeam_1 = _coreTeam_1;
    }


    function set_minting_price(uint _price) external onlyOwner {
        require(paused, "ERROR: CANT CHANGE PRICE IF CONTRACT IS NOT PAUSED");
        mintingCost = _price;
    }

    function setUsdcTokenAddress(address _address) public onlyOwner {
        require(address(_address ) != address(0), "ERROR: The USDC contract address can't be address(0)");
        usdcTokenContract = _address;
    }

    function setUsdcTokenDecimals(uint _decimals) public onlyOwner {
        usdcTokenDecimals = _decimals;
    }


    function setTheRanchBullsMintandRewardAddress(address _address) public onlyOwner {
        require(address(_address) != address(0), "ERROR: The mint and reward contract address can't be address(0)");
        TheRanchBullsMintAndReward = _address;
    }


}

