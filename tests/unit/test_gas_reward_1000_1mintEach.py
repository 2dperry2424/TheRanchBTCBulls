from curses import use_env
from curses.ascii import FF
from distutils import core
from unittest import mock
from pyrsistent import v
from scripts.helpful_scripts import get_account, get_contract, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMintReward, MockedTokens_USDC, MockedTokens_WBTC, network, config, MockV3Aggregator, accounts, exceptions, chain
from scripts.deploy_mintAndReward import deploy_contract
from scripts.deploy_v2mocks import deploy_v2mocks
from web3 import Web3
import time, pytest
import pprint
import math






def test_gas_1000_mints_rewards_and_maint():


    coinbase = accounts[10001]
    defender_wallet = accounts[10002]
    multisig = accounts[10003]

    btcMinersSafe = accounts[10006]
    hostingSafe = accounts[10007]


    person_1 = accounts[1]
    person_2 = accounts[2]
    person_3 = accounts[3]
    person_4 = accounts[4]
    person_5 = accounts[5]
    person_6 = accounts[6]
    person_7 = accounts[7]
    person_8 = accounts[8]
    person_9 = accounts[9]
    person_10 = accounts[10]
    person_11 = accounts[11]
    person_12 = accounts[12]
    person_13 = accounts[13]
    person_14 = accounts[14]
    person_15 = accounts[15]
    person_16 = accounts[16]
    person_17 = accounts[17]
    person_18 = accounts[18]
    person_19 = accounts[19]
    person_20 = accounts[20]
    person_21 = accounts[21]
    person_22 = accounts[22]
    person_23 = accounts[23]
    person_24 = accounts[24]
    person_25 = accounts[25]
    person_26 = accounts[26]
    person_27 = accounts[27]
    person_28 = accounts[28]
    person_29 = accounts[29]
    person_30 = accounts[30]

    person_31 = accounts[31]
    person_32 = accounts[32]
    person_33 = accounts[33]
    person_34 = accounts[34]
    person_35 = accounts[35]
    person_36 = accounts[36]
    person_37 = accounts[37]
    person_38 = accounts[38]
    person_39 = accounts[39]
    person_40 = accounts[40]

    person_41 = accounts[41]
    person_42 = accounts[42]
    person_43 = accounts[43]
    person_44 = accounts[44]
    person_45 = accounts[45]
    person_46 = accounts[46]
    person_47 = accounts[47]
    person_48 = accounts[48]
    person_49 = accounts[49]
    person_50 = accounts[50]

    person_51 = accounts[51]
    person_52 = accounts[52]
    person_53 = accounts[53]
    person_54 = accounts[54]
    person_55 = accounts[55]
    person_56 = accounts[56]
    person_57 = accounts[57]
    person_58 = accounts[58]
    person_59 = accounts[59]
    person_60 = accounts[60]
 
    person_61 = accounts[61]
    person_62 = accounts[62]
    person_63 = accounts[63]
    person_64 = accounts[64]
    person_65 = accounts[65]
    person_66 = accounts[66]
    person_67 = accounts[67]
    person_68 = accounts[68]
    person_69 = accounts[69]
    person_70 = accounts[70]

    person_71 = accounts[71]
    person_72 = accounts[72]
    person_73 = accounts[73]
    person_74 = accounts[74]
    person_75 = accounts[75]
    person_76 = accounts[76]
    person_77 = accounts[77]
    person_78 = accounts[78]
    person_79 = accounts[79]
    person_80 = accounts[80]

    person_81 = accounts[81]
    person_82 = accounts[82]
    person_83 = accounts[83]
    person_84 = accounts[84]
    person_85 = accounts[85]
    person_86 = accounts[86]
    person_87 = accounts[87]
    person_88 = accounts[88]
    person_89 = accounts[89]
    person_90 = accounts[90]

    person_91 = accounts[91]
    person_92 = accounts[92]
    person_93 = accounts[93]
    person_94 = accounts[94]
    person_95 = accounts[95]
    person_96 = accounts[96]
    person_97 = accounts[97]
    person_98 = accounts[98]
    person_99 = accounts[99]
    person_100 = accounts[100]
    person_101 = accounts[101]
    person_102 = accounts[102]
    person_103 = accounts[103]
    person_104 = accounts[104]
    person_105 = accounts[105]
    person_106 = accounts[106]
    person_107 = accounts[107]
    person_108 = accounts[108]
    person_109 = accounts[109]
    person_110 = accounts[110]
    person_111 = accounts[111]
    person_112 = accounts[112]
    person_113 = accounts[113]
    person_114 = accounts[114]
    person_115 = accounts[115]
    person_116 = accounts[116]
    person_117 = accounts[117]
    person_118 = accounts[118]
    person_119 = accounts[119]
    person_120 = accounts[120]
    person_121 = accounts[121]
    person_122 = accounts[122]
    person_123 = accounts[123]
    person_124 = accounts[124]
    person_125 = accounts[125]
    person_126 = accounts[126]
    person_127 = accounts[127]
    person_128 = accounts[128]
    person_129 = accounts[129]
    person_130 = accounts[130]
    person_131 = accounts[131]
    person_132 = accounts[132]
    person_133 = accounts[133]
    person_134 = accounts[134]
    person_135 = accounts[135]
    person_136 = accounts[136]
    person_137 = accounts[137]
    person_138 = accounts[138]
    person_139 = accounts[139]
    person_140 = accounts[140]
    person_141 = accounts[141]
    person_142 = accounts[142]
    person_143 = accounts[143]
    person_144 = accounts[144]
    person_145 = accounts[145]
    person_146 = accounts[146]
    person_147 = accounts[147]
    person_148 = accounts[148]
    person_149 = accounts[149]
    person_150 = accounts[150]
    person_151 = accounts[151]
    person_152 = accounts[152]
    person_153 = accounts[153]
    person_154 = accounts[154]
    person_155 = accounts[155]
    person_156 = accounts[156]
    person_157 = accounts[157]
    person_158 = accounts[158]
    person_159 = accounts[159]
    person_160 = accounts[160]
    person_161 = accounts[161]
    person_162 = accounts[162]
    person_163 = accounts[163]
    person_164 = accounts[164]
    person_165 = accounts[165]
    person_166 = accounts[166]
    person_167 = accounts[167]
    person_168 = accounts[168]
    person_169 = accounts[169]
    person_170 = accounts[170]
    person_171 = accounts[171]
    person_172 = accounts[172]
    person_173 = accounts[173]
    person_174 = accounts[174]
    person_175 = accounts[175]
    person_176 = accounts[176]
    person_177 = accounts[177]
    person_178 = accounts[178]
    person_179 = accounts[179]
    person_180 = accounts[180]
    person_181 = accounts[181]
    person_182 = accounts[182]
    person_183 = accounts[183]
    person_184 = accounts[184]
    person_185 = accounts[185]
    person_186 = accounts[186]
    person_187 = accounts[187]
    person_188 = accounts[188]
    person_189 = accounts[189]
    person_190 = accounts[190]
    person_191 = accounts[191]
    person_192 = accounts[192]
    person_193 = accounts[193]
    person_194 = accounts[194]
    person_195 = accounts[195]
    person_196 = accounts[196]
    person_197 = accounts[197]
    person_198 = accounts[198]
    person_199 = accounts[199]
    person_200 = accounts[200]
    person_201 = accounts[201]
    person_202 = accounts[202]
    person_203 = accounts[203]
    person_204 = accounts[204]
    person_205 = accounts[205]
    person_206 = accounts[206]
    person_207 = accounts[207]
    person_208 = accounts[208]
    person_209 = accounts[209]
    person_210 = accounts[210]
    person_211 = accounts[211]
    person_212 = accounts[212]
    person_213 = accounts[213]
    person_214 = accounts[214]
    person_215 = accounts[215]
    person_216 = accounts[216]
    person_217 = accounts[217]
    person_218 = accounts[218]
    person_219 = accounts[219]
    person_220 = accounts[220]
    person_221 = accounts[221]
    person_222 = accounts[222]
    person_223 = accounts[223]
    person_224 = accounts[224]
    person_225 = accounts[225]
    person_226 = accounts[226]
    person_227 = accounts[227]
    person_228 = accounts[228]
    person_229 = accounts[229]
    person_230 = accounts[230]
    person_231 = accounts[231]
    person_232 = accounts[232]
    person_233 = accounts[233]
    person_234 = accounts[234]
    person_235 = accounts[235]
    person_236 = accounts[236]
    person_237 = accounts[237]
    person_238 = accounts[238]
    person_239 = accounts[239]
    person_240 = accounts[240]
    person_241 = accounts[241]
    person_242 = accounts[242]
    person_243 = accounts[243]
    person_244 = accounts[244]
    person_245 = accounts[245]
    person_246 = accounts[246]
    person_247 = accounts[247]
    person_248 = accounts[248]
    person_249 = accounts[249]
    person_250 = accounts[250]
    person_251 = accounts[251]
    person_252 = accounts[252]
    person_253 = accounts[253]
    person_254 = accounts[254]
    person_255 = accounts[255]
    person_256 = accounts[256]
    person_257 = accounts[257]
    person_258 = accounts[258]
    person_259 = accounts[259]
    person_260 = accounts[260]
    person_261 = accounts[261]
    person_262 = accounts[262]
    person_263 = accounts[263]
    person_264 = accounts[264]
    person_265 = accounts[265]
    person_266 = accounts[266]
    person_267 = accounts[267]
    person_268 = accounts[268]
    person_269 = accounts[269]
    person_270 = accounts[270]
    person_271 = accounts[271]
    person_272 = accounts[272]
    person_273 = accounts[273]
    person_274 = accounts[274]
    person_275 = accounts[275]
    person_276 = accounts[276]
    person_277 = accounts[277]
    person_278 = accounts[278]
    person_279 = accounts[279]
    person_280 = accounts[280]
    person_281 = accounts[281]
    person_282 = accounts[282]
    person_283 = accounts[283]
    person_284 = accounts[284]
    person_285 = accounts[285]
    person_286 = accounts[286]
    person_287 = accounts[287]
    person_288 = accounts[288]
    person_289 = accounts[289]
    person_290 = accounts[290]
    person_291 = accounts[291]
    person_292 = accounts[292]
    person_293 = accounts[293]
    person_294 = accounts[294]
    person_295 = accounts[295]
    person_296 = accounts[296]
    person_297 = accounts[297]
    person_298 = accounts[298]
    person_299 = accounts[299]
    person_300 = accounts[300]
    person_301 = accounts[301]
    person_302 = accounts[302]
    person_303 = accounts[303]
    person_304 = accounts[304]
    person_305 = accounts[305]
    person_306 = accounts[306]
    person_307 = accounts[307]
    person_308 = accounts[308]
    person_309 = accounts[309]
    person_310 = accounts[310]
    person_311 = accounts[311]
    person_312 = accounts[312]
    person_313 = accounts[313]
    person_314 = accounts[314]
    person_315 = accounts[315]
    person_316 = accounts[316]
    person_317 = accounts[317]
    person_318 = accounts[318]
    person_319 = accounts[319]
    person_320 = accounts[320]
    person_321 = accounts[321]
    person_322 = accounts[322]
    person_323 = accounts[323]
    person_324 = accounts[324]
    person_325 = accounts[325]
    person_326 = accounts[326]
    person_327 = accounts[327]
    person_328 = accounts[328]
    person_329 = accounts[329]
    person_330 = accounts[330]
    person_331 = accounts[331]
    person_332 = accounts[332]
    person_333 = accounts[333]
    person_334 = accounts[334]
    person_335 = accounts[335]
    person_336 = accounts[336]
    person_337 = accounts[337]
    person_338 = accounts[338]
    person_339 = accounts[339]
    person_340 = accounts[340]
    person_341 = accounts[341]
    person_342 = accounts[342]
    person_343 = accounts[343]
    person_344 = accounts[344]
    person_345 = accounts[345]
    person_346 = accounts[346]
    person_347 = accounts[347]
    person_348 = accounts[348]
    person_349 = accounts[349]
    person_350 = accounts[350]
    person_351 = accounts[351]
    person_352 = accounts[352]
    person_353 = accounts[353]
    person_354 = accounts[354]
    person_355 = accounts[355]
    person_356 = accounts[356]
    person_357 = accounts[357]
    person_358 = accounts[358]
    person_359 = accounts[359]
    person_360 = accounts[360]
    person_361 = accounts[361]
    person_362 = accounts[362]
    person_363 = accounts[363]
    person_364 = accounts[364]
    person_365 = accounts[365]
    person_366 = accounts[366]
    person_367 = accounts[367]
    person_368 = accounts[368]
    person_369 = accounts[369]
    person_370 = accounts[370]
    person_371 = accounts[371]
    person_372 = accounts[372]
    person_373 = accounts[373]
    person_374 = accounts[374]
    person_375 = accounts[375]
    person_376 = accounts[376]
    person_377 = accounts[377]
    person_378 = accounts[378]
    person_379 = accounts[379]
    person_380 = accounts[380]
    person_381 = accounts[381]
    person_382 = accounts[382]
    person_383 = accounts[383]
    person_384 = accounts[384]
    person_385 = accounts[385]
    person_386 = accounts[386]
    person_387 = accounts[387]
    person_388 = accounts[388]
    person_389 = accounts[389]
    person_390 = accounts[390]
    person_391 = accounts[391]
    person_392 = accounts[392]
    person_393 = accounts[393]
    person_394 = accounts[394]
    person_395 = accounts[395]
    person_396 = accounts[396]
    person_397 = accounts[397]
    person_398 = accounts[398]
    person_399 = accounts[399]
    person_400 = accounts[400]
    person_401 = accounts[401]
    person_402 = accounts[402]
    person_403 = accounts[403]
    person_404 = accounts[404]
    person_405 = accounts[405]
    person_406 = accounts[406]
    person_407 = accounts[407]
    person_408 = accounts[408]
    person_409 = accounts[409]
    person_410 = accounts[410]
    person_411 = accounts[411]
    person_412 = accounts[412]
    person_413 = accounts[413]
    person_414 = accounts[414]
    person_415 = accounts[415]
    person_416 = accounts[416]
    person_417 = accounts[417]
    person_418 = accounts[418]
    person_419 = accounts[419]
    person_420 = accounts[420]
    person_421 = accounts[421]
    person_422 = accounts[422]
    person_423 = accounts[423]
    person_424 = accounts[424]
    person_425 = accounts[425]
    person_426 = accounts[426]
    person_427 = accounts[427]
    person_428 = accounts[428]
    person_429 = accounts[429]
    person_430 = accounts[430]
    person_431 = accounts[431]
    person_432 = accounts[432]
    person_433 = accounts[433]
    person_434 = accounts[434]
    person_435 = accounts[435]
    person_436 = accounts[436]
    person_437 = accounts[437]
    person_438 = accounts[438]
    person_439 = accounts[439]
    person_440 = accounts[440]
    person_441 = accounts[441]
    person_442 = accounts[442]
    person_443 = accounts[443]
    person_444 = accounts[444]
    person_445 = accounts[445]
    person_446 = accounts[446]
    person_447 = accounts[447]
    person_448 = accounts[448]
    person_449 = accounts[449]
    person_450 = accounts[450]
    person_451 = accounts[451]
    person_452 = accounts[452]
    person_453 = accounts[453]
    person_454 = accounts[454]
    person_455 = accounts[455]
    person_456 = accounts[456]
    person_457 = accounts[457]
    person_458 = accounts[458]
    person_459 = accounts[459]
    person_460 = accounts[460]
    person_461 = accounts[461]
    person_462 = accounts[462]
    person_463 = accounts[463]
    person_464 = accounts[464]
    person_465 = accounts[465]
    person_466 = accounts[466]
    person_467 = accounts[467]
    person_468 = accounts[468]
    person_469 = accounts[469]
    person_470 = accounts[470]
    person_471 = accounts[471]
    person_472 = accounts[472]
    person_473 = accounts[473]
    person_474 = accounts[474]
    person_475 = accounts[475]
    person_476 = accounts[476]
    person_477 = accounts[477]
    person_478 = accounts[478]
    person_479 = accounts[479]
    person_480 = accounts[480]
    person_481 = accounts[481]
    person_482 = accounts[482]
    person_483 = accounts[483]
    person_484 = accounts[484]
    person_485 = accounts[485]
    person_486 = accounts[486]
    person_487 = accounts[487]
    person_488 = accounts[488]
    person_489 = accounts[489]
    person_490 = accounts[490]
    person_491 = accounts[491]
    person_492 = accounts[492]
    person_493 = accounts[493]
    person_494 = accounts[494]
    person_495 = accounts[495]
    person_496 = accounts[496]
    person_497 = accounts[497]
    person_498 = accounts[498]
    person_499 = accounts[499]
    person_500 = accounts[500]
    person_501 = accounts[501]
    person_502 = accounts[502]
    person_503 = accounts[503]
    person_504 = accounts[504]
    person_505 = accounts[505]
    person_506 = accounts[506]
    person_507 = accounts[507]
    person_508 = accounts[508]
    person_509 = accounts[509]
    person_510 = accounts[510]
    person_511 = accounts[511]
    person_512 = accounts[512]
    person_513 = accounts[513]
    person_514 = accounts[514]
    person_515 = accounts[515]
    person_516 = accounts[516]
    person_517 = accounts[517]
    person_518 = accounts[518]
    person_519 = accounts[519]
    person_520 = accounts[520]
    person_521 = accounts[521]
    person_522 = accounts[522]
    person_523 = accounts[523]
    person_524 = accounts[524]
    person_525 = accounts[525]
    person_526 = accounts[526]
    person_527 = accounts[527]
    person_528 = accounts[528]
    person_529 = accounts[529]
    person_530 = accounts[530]
    person_531 = accounts[531]
    person_532 = accounts[532]
    person_533 = accounts[533]
    person_534 = accounts[534]
    person_535 = accounts[535]
    person_536 = accounts[536]
    person_537 = accounts[537]
    person_538 = accounts[538]
    person_539 = accounts[539]
    person_540 = accounts[540]
    person_541 = accounts[541]
    person_542 = accounts[542]
    person_543 = accounts[543]
    person_544 = accounts[544]
    person_545 = accounts[545]
    person_546 = accounts[546]
    person_547 = accounts[547]
    person_548 = accounts[548]
    person_549 = accounts[549]
    person_550 = accounts[550]
    person_551 = accounts[551]
    person_552 = accounts[552]
    person_553 = accounts[553]
    person_554 = accounts[554]
    person_555 = accounts[555]
    person_556 = accounts[556]
    person_557 = accounts[557]
    person_558 = accounts[558]
    person_559 = accounts[559]
    person_560 = accounts[560]
    person_561 = accounts[561]
    person_562 = accounts[562]
    person_563 = accounts[563]
    person_564 = accounts[564]
    person_565 = accounts[565]
    person_566 = accounts[566]
    person_567 = accounts[567]
    person_568 = accounts[568]
    person_569 = accounts[569]
    person_570 = accounts[570]
    person_571 = accounts[571]
    person_572 = accounts[572]
    person_573 = accounts[573]
    person_574 = accounts[574]
    person_575 = accounts[575]
    person_576 = accounts[576]
    person_577 = accounts[577]
    person_578 = accounts[578]
    person_579 = accounts[579]
    person_580 = accounts[580]
    person_581 = accounts[581]
    person_582 = accounts[582]
    person_583 = accounts[583]
    person_584 = accounts[584]
    person_585 = accounts[585]
    person_586 = accounts[586]
    person_587 = accounts[587]
    person_588 = accounts[588]
    person_589 = accounts[589]
    person_590 = accounts[590]
    person_591 = accounts[591]
    person_592 = accounts[592]
    person_593 = accounts[593]
    person_594 = accounts[594]
    person_595 = accounts[595]
    person_596 = accounts[596]
    person_597 = accounts[597]
    person_598 = accounts[598]
    person_599 = accounts[599]
    person_600 = accounts[600]
    person_601 = accounts[601]
    person_602 = accounts[602]
    person_603 = accounts[603]
    person_604 = accounts[604]
    person_605 = accounts[605]
    person_606 = accounts[606]
    person_607 = accounts[607]
    person_608 = accounts[608]
    person_609 = accounts[609]
    person_610 = accounts[610]
    person_611 = accounts[611]
    person_612 = accounts[612]
    person_613 = accounts[613]
    person_614 = accounts[614]
    person_615 = accounts[615]
    person_616 = accounts[616]
    person_617 = accounts[617]
    person_618 = accounts[618]
    person_619 = accounts[619]
    person_620 = accounts[620]
    person_621 = accounts[621]
    person_622 = accounts[622]
    person_623 = accounts[623]
    person_624 = accounts[624]
    person_625 = accounts[625]
    person_626 = accounts[626]
    person_627 = accounts[627]
    person_628 = accounts[628]
    person_629 = accounts[629]
    person_630 = accounts[630]
    person_631 = accounts[631]
    person_632 = accounts[632]
    person_633 = accounts[633]
    person_634 = accounts[634]
    person_635 = accounts[635]
    person_636 = accounts[636]
    person_637 = accounts[637]
    person_638 = accounts[638]
    person_639 = accounts[639]
    person_640 = accounts[640]
    person_641 = accounts[641]
    person_642 = accounts[642]
    person_643 = accounts[643]
    person_644 = accounts[644]
    person_645 = accounts[645]
    person_646 = accounts[646]
    person_647 = accounts[647]
    person_648 = accounts[648]
    person_649 = accounts[649]
    person_650 = accounts[650]
    person_651 = accounts[651]
    person_652 = accounts[652]
    person_653 = accounts[653]
    person_654 = accounts[654]
    person_655 = accounts[655]
    person_656 = accounts[656]
    person_657 = accounts[657]
    person_658 = accounts[658]
    person_659 = accounts[659]
    person_660 = accounts[660]
    person_661 = accounts[661]
    person_662 = accounts[662]
    person_663 = accounts[663]
    person_664 = accounts[664]
    person_665 = accounts[665]
    person_666 = accounts[666]
    person_667 = accounts[667]
    person_668 = accounts[668]
    person_669 = accounts[669]
    person_670 = accounts[670]
    person_671 = accounts[671]
    person_672 = accounts[672]
    person_673 = accounts[673]
    person_674 = accounts[674]
    person_675 = accounts[675]
    person_676 = accounts[676]
    person_677 = accounts[677]
    person_678 = accounts[678]
    person_679 = accounts[679]
    person_680 = accounts[680]
    person_681 = accounts[681]
    person_682 = accounts[682]
    person_683 = accounts[683]
    person_684 = accounts[684]
    person_685 = accounts[685]
    person_686 = accounts[686]
    person_687 = accounts[687]
    person_688 = accounts[688]
    person_689 = accounts[689]
    person_690 = accounts[690]
    person_691 = accounts[691]
    person_692 = accounts[692]
    person_693 = accounts[693]
    person_694 = accounts[694]
    person_695 = accounts[695]
    person_696 = accounts[696]
    person_697 = accounts[697]
    person_698 = accounts[698]
    person_699 = accounts[699]
    person_700 = accounts[700]
    person_701 = accounts[701]
    person_702 = accounts[702]
    person_703 = accounts[703]
    person_704 = accounts[704]
    person_705 = accounts[705]
    person_706 = accounts[706]
    person_707 = accounts[707]
    person_708 = accounts[708]
    person_709 = accounts[709]
    person_710 = accounts[710]
    person_711 = accounts[711]
    person_712 = accounts[712]
    person_713 = accounts[713]
    person_714 = accounts[714]
    person_715 = accounts[715]
    person_716 = accounts[716]
    person_717 = accounts[717]
    person_718 = accounts[718]
    person_719 = accounts[719]
    person_720 = accounts[720]
    person_721 = accounts[721]
    person_722 = accounts[722]
    person_723 = accounts[723]
    person_724 = accounts[724]
    person_725 = accounts[725]
    person_726 = accounts[726]
    person_727 = accounts[727]
    person_728 = accounts[728]
    person_729 = accounts[729]
    person_730 = accounts[730]
    person_731 = accounts[731]
    person_732 = accounts[732]
    person_733 = accounts[733]
    person_734 = accounts[734]
    person_735 = accounts[735]
    person_736 = accounts[736]
    person_737 = accounts[737]
    person_738 = accounts[738]
    person_739 = accounts[739]
    person_740 = accounts[740]
    person_741 = accounts[741]
    person_742 = accounts[742]
    person_743 = accounts[743]
    person_744 = accounts[744]
    person_745 = accounts[745]
    person_746 = accounts[746]
    person_747 = accounts[747]
    person_748 = accounts[748]
    person_749 = accounts[749]
    person_750 = accounts[750]
    person_751 = accounts[751]
    person_752 = accounts[752]
    person_753 = accounts[753]
    person_754 = accounts[754]
    person_755 = accounts[755]
    person_756 = accounts[756]
    person_757 = accounts[757]
    person_758 = accounts[758]
    person_759 = accounts[759]
    person_760 = accounts[760]
    person_761 = accounts[761]
    person_762 = accounts[762]
    person_763 = accounts[763]
    person_764 = accounts[764]
    person_765 = accounts[765]
    person_766 = accounts[766]
    person_767 = accounts[767]
    person_768 = accounts[768]
    person_769 = accounts[769]
    person_770 = accounts[770]
    person_771 = accounts[771]
    person_772 = accounts[772]
    person_773 = accounts[773]
    person_774 = accounts[774]
    person_775 = accounts[775]
    person_776 = accounts[776]
    person_777 = accounts[777]
    person_778 = accounts[778]
    person_779 = accounts[779]
    person_780 = accounts[780]
    person_781 = accounts[781]
    person_782 = accounts[782]
    person_783 = accounts[783]
    person_784 = accounts[784]
    person_785 = accounts[785]
    person_786 = accounts[786]
    person_787 = accounts[787]
    person_788 = accounts[788]
    person_789 = accounts[789]
    person_790 = accounts[790]
    person_791 = accounts[791]
    person_792 = accounts[792]
    person_793 = accounts[793]
    person_794 = accounts[794]
    person_795 = accounts[795]
    person_796 = accounts[796]
    person_797 = accounts[797]
    person_798 = accounts[798]
    person_799 = accounts[799]
    person_800 = accounts[800]
    person_801 = accounts[801]
    person_802 = accounts[802]
    person_803 = accounts[803]
    person_804 = accounts[804]
    person_805 = accounts[805]
    person_806 = accounts[806]
    person_807 = accounts[807]
    person_808 = accounts[808]
    person_809 = accounts[809]
    person_810 = accounts[810]
    person_811 = accounts[811]
    person_812 = accounts[812]
    person_813 = accounts[813]
    person_814 = accounts[814]
    person_815 = accounts[815]
    person_816 = accounts[816]
    person_817 = accounts[817]
    person_818 = accounts[818]
    person_819 = accounts[819]
    person_820 = accounts[820]
    person_821 = accounts[821]
    person_822 = accounts[822]
    person_823 = accounts[823]
    person_824 = accounts[824]
    person_825 = accounts[825]
    person_826 = accounts[826]
    person_827 = accounts[827]
    person_828 = accounts[828]
    person_829 = accounts[829]
    person_830 = accounts[830]
    person_831 = accounts[831]
    person_832 = accounts[832]
    person_833 = accounts[833]
    person_834 = accounts[834]
    person_835 = accounts[835]
    person_836 = accounts[836]
    person_837 = accounts[837]
    person_838 = accounts[838]
    person_839 = accounts[839]
    person_840 = accounts[840]
    person_841 = accounts[841]
    person_842 = accounts[842]
    person_843 = accounts[843]
    person_844 = accounts[844]
    person_845 = accounts[845]
    person_846 = accounts[846]
    person_847 = accounts[847]
    person_848 = accounts[848]
    person_849 = accounts[849]
    person_850 = accounts[850]
    person_851 = accounts[851]
    person_852 = accounts[852]
    person_853 = accounts[853]
    person_854 = accounts[854]
    person_855 = accounts[855]
    person_856 = accounts[856]
    person_857 = accounts[857]
    person_858 = accounts[858]
    person_859 = accounts[859]
    person_860 = accounts[860]
    person_861 = accounts[861]
    person_862 = accounts[862]
    person_863 = accounts[863]
    person_864 = accounts[864]
    person_865 = accounts[865]
    person_866 = accounts[866]
    person_867 = accounts[867]
    person_868 = accounts[868]
    person_869 = accounts[869]
    person_870 = accounts[870]
    person_871 = accounts[871]
    person_872 = accounts[872]
    person_873 = accounts[873]
    person_874 = accounts[874]
    person_875 = accounts[875]
    person_876 = accounts[876]
    person_877 = accounts[877]
    person_878 = accounts[878]
    person_879 = accounts[879]
    person_880 = accounts[880]
    person_881 = accounts[881]
    person_882 = accounts[882]
    person_883 = accounts[883]
    person_884 = accounts[884]
    person_885 = accounts[885]
    person_886 = accounts[886]
    person_887 = accounts[887]
    person_888 = accounts[888]
    person_889 = accounts[889]
    person_890 = accounts[890]
    person_891 = accounts[891]
    person_892 = accounts[892]
    person_893 = accounts[893]
    person_894 = accounts[894]
    person_895 = accounts[895]
    person_896 = accounts[896]
    person_897 = accounts[897]
    person_898 = accounts[898]
    person_899 = accounts[899]
    person_900 = accounts[900]
    person_901 = accounts[901]
    person_902 = accounts[902]
    person_903 = accounts[903]
    person_904 = accounts[904]
    person_905 = accounts[905]
    person_906 = accounts[906]
    person_907 = accounts[907]
    person_908 = accounts[908]
    person_909 = accounts[909]
    person_910 = accounts[910]
    person_911 = accounts[911]
    person_912 = accounts[912]
    person_913 = accounts[913]
    person_914 = accounts[914]
    person_915 = accounts[915]
    person_916 = accounts[916]
    person_917 = accounts[917]
    person_918 = accounts[918]
    person_919 = accounts[919]
    person_920 = accounts[920]
    person_921 = accounts[921]
    person_922 = accounts[922]
    person_923 = accounts[923]
    person_924 = accounts[924]
    person_925 = accounts[925]
    person_926 = accounts[926]
    person_927 = accounts[927]
    person_928 = accounts[928]
    person_929 = accounts[929]
    person_930 = accounts[930]
    person_931 = accounts[931]
    person_932 = accounts[932]
    person_933 = accounts[933]
    person_934 = accounts[934]
    person_935 = accounts[935]
    person_936 = accounts[936]
    person_937 = accounts[937]
    person_938 = accounts[938]
    person_939 = accounts[939]
    person_940 = accounts[940]
    person_941 = accounts[941]
    person_942 = accounts[942]
    person_943 = accounts[943]
    person_944 = accounts[944]
    person_945 = accounts[945]
    person_946 = accounts[946]
    person_947 = accounts[947]
    person_948 = accounts[948]
    person_949 = accounts[949]
    person_950 = accounts[950]
    person_951 = accounts[951]
    person_952 = accounts[952]
    person_953 = accounts[953]
    person_954 = accounts[954]
    person_955 = accounts[955]
    person_956 = accounts[956]
    person_957 = accounts[957]
    person_958 = accounts[958]
    person_959 = accounts[959]
    person_960 = accounts[960]
    person_961 = accounts[961]
    person_962 = accounts[962]
    person_963 = accounts[963]
    person_964 = accounts[964]
    person_965 = accounts[965]
    person_966 = accounts[966]
    person_967 = accounts[967]
    person_968 = accounts[968]
    person_969 = accounts[969]
    person_970 = accounts[970]
    person_971 = accounts[971]
    person_972 = accounts[972]
    person_973 = accounts[973]
    person_974 = accounts[974]
    person_975 = accounts[975]
    person_976 = accounts[976]
    person_977 = accounts[977]
    person_978 = accounts[978]
    person_979 = accounts[979]
    person_980 = accounts[980]
    person_981 = accounts[981]
    person_982 = accounts[982]
    person_983 = accounts[983]
    person_984 = accounts[984]
    person_985 = accounts[985]
    person_986 = accounts[986]
    person_987 = accounts[987]
    person_988 = accounts[988]
    person_989 = accounts[989]
    person_990 = accounts[990]
    person_991 = accounts[991]
    person_992 = accounts[992]
    person_993 = accounts[993]
    person_994 = accounts[994]
    person_995 = accounts[995]
    person_996 = accounts[996]
    person_997 = accounts[997]
    person_998 = accounts[998]
    person_999 = accounts[999]
    person_1000 = accounts[1000]





    TheRanchBullsMintAndReward = deploy_contract()
    deployer = TheRanchBullsMintAndReward.owner.call()

    coreTeam1 = TheRanchBullsMintAndReward.coreTeam_1.call()
    coreTeam2 = TheRanchBullsMintAndReward.coreTeam_2.call()


 
    ################################################################
    ## assert the deployer can transfer ownership of the contract ##
    ################################################################

    tx_transfer_ownership = TheRanchBullsMintAndReward.transferOwnership(multisig)
    print(tx_transfer_ownership.info())

    assert TheRanchBullsMintAndReward.owner.call() != deployer
    assert TheRanchBullsMintAndReward.owner.call() == multisig




    assert TheRanchBullsMintAndReward.paused.call() == True


    mocked_usdc = MockedTokens_USDC.deploy(1_000_000_000 * 10**6, {"from": coinbase})
    mocked_wbtc = MockedTokens_WBTC.deploy(10 * 10**8, {"from": multisig})

    TheRanchBullsMintAndReward.setUsdcTokenAddress(mocked_usdc,{"from": multisig})
    TheRanchBullsMintAndReward.setWbtcTokenAddress(mocked_wbtc,{"from": multisig})
    TheRanchBullsMintAndReward.setBaseURI("ipfs://aldkfjasdpofe", {"from": multisig})
    TheRanchBullsMintAndReward.setSafeAddresses(hostingSafe,btcMinersSafe,{"from": multisig})





    #########################################################
    ####       Transfer USDC  each person                ####
    #########################################################
    
    mocked_usdc.transfer(person_1, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_2, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_3, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_4, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_5, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_6, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_7, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_8, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_9, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_10, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_11, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_12, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_13, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_14, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_15, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_16, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_17, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_18, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_19, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_20, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_21, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_22, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_23, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_24, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_25, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_26, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_27, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_28, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_29, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_30, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_31, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_32, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_33, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_34, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_35, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_36, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_37, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_38, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_39, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_40, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_41, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_42, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_43, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_44, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_45, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_46, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_47, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_48, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_49, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_50, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_51, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_52, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_53, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_54, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_55, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_56, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_57, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_58, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_59, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_60, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_61, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_62, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_63, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_64, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_65, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_66, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_67, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_68, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_69, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_70, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_71, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_72, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_73, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_74, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_75, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_76, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_77, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_78, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_79, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_80, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_81, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_82, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_83, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_84, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_85, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_86, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_87, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_88, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_89, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_90, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_91, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_92, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_93, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_94, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_95, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_96, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_97, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_98, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_99, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_100, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_101, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_102, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_103, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_104, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_105, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_106, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_107, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_108, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_109, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_110, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_111, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_112, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_113, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_114, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_115, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_116, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_117, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_118, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_119, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_120, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_121, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_122, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_123, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_124, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_125, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_126, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_127, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_128, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_129, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_130, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_131, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_132, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_133, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_134, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_135, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_136, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_137, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_138, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_139, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_140, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_141, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_142, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_143, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_144, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_145, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_146, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_147, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_148, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_149, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_150, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_151, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_152, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_153, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_154, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_155, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_156, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_157, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_158, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_159, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_160, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_161, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_162, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_163, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_164, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_165, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_166, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_167, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_168, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_169, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_170, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_171, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_172, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_173, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_174, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_175, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_176, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_177, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_178, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_179, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_180, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_181, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_182, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_183, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_184, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_185, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_186, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_187, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_188, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_189, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_190, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_191, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_192, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_193, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_194, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_195, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_196, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_197, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_198, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_199, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_200, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_201, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_202, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_203, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_204, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_205, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_206, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_207, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_208, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_209, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_210, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_211, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_212, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_213, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_214, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_215, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_216, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_217, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_218, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_219, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_220, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_221, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_222, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_223, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_224, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_225, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_226, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_227, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_228, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_229, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_230, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_231, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_232, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_233, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_234, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_235, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_236, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_237, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_238, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_239, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_240, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_241, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_242, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_243, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_244, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_245, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_246, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_247, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_248, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_249, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_250, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_251, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_252, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_253, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_254, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_255, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_256, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_257, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_258, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_259, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_260, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_261, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_262, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_263, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_264, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_265, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_266, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_267, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_268, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_269, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_270, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_271, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_272, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_273, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_274, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_275, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_276, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_277, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_278, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_279, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_280, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_281, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_282, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_283, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_284, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_285, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_286, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_287, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_288, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_289, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_290, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_291, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_292, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_293, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_294, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_295, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_296, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_297, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_298, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_299, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_300, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_301, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_302, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_303, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_304, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_305, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_306, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_307, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_308, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_309, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_310, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_311, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_312, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_313, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_314, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_315, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_316, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_317, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_318, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_319, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_320, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_321, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_322, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_323, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_324, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_325, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_326, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_327, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_328, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_329, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_330, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_331, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_332, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_333, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_334, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_335, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_336, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_337, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_338, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_339, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_340, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_341, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_342, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_343, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_344, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_345, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_346, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_347, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_348, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_349, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_350, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_351, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_352, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_353, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_354, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_355, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_356, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_357, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_358, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_359, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_360, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_361, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_362, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_363, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_364, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_365, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_366, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_367, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_368, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_369, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_370, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_371, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_372, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_373, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_374, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_375, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_376, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_377, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_378, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_379, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_380, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_381, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_382, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_383, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_384, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_385, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_386, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_387, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_388, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_389, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_390, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_391, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_392, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_393, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_394, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_395, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_396, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_397, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_398, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_399, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_400, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_401, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_402, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_403, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_404, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_405, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_406, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_407, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_408, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_409, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_410, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_411, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_412, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_413, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_414, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_415, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_416, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_417, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_418, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_419, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_420, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_421, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_422, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_423, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_424, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_425, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_426, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_427, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_428, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_429, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_430, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_431, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_432, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_433, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_434, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_435, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_436, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_437, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_438, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_439, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_440, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_441, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_442, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_443, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_444, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_445, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_446, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_447, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_448, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_449, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_450, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_451, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_452, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_453, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_454, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_455, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_456, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_457, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_458, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_459, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_460, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_461, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_462, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_463, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_464, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_465, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_466, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_467, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_468, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_469, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_470, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_471, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_472, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_473, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_474, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_475, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_476, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_477, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_478, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_479, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_480, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_481, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_482, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_483, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_484, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_485, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_486, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_487, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_488, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_489, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_490, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_491, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_492, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_493, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_494, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_495, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_496, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_497, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_498, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_499, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_500, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_501, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_502, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_503, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_504, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_505, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_506, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_507, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_508, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_509, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_510, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_511, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_512, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_513, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_514, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_515, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_516, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_517, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_518, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_519, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_520, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_521, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_522, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_523, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_524, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_525, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_526, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_527, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_528, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_529, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_530, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_531, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_532, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_533, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_534, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_535, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_536, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_537, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_538, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_539, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_540, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_541, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_542, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_543, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_544, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_545, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_546, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_547, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_548, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_549, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_550, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_551, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_552, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_553, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_554, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_555, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_556, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_557, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_558, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_559, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_560, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_561, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_562, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_563, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_564, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_565, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_566, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_567, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_568, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_569, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_570, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_571, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_572, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_573, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_574, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_575, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_576, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_577, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_578, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_579, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_580, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_581, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_582, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_583, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_584, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_585, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_586, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_587, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_588, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_589, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_590, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_591, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_592, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_593, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_594, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_595, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_596, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_597, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_598, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_599, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_600, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_601, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_602, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_603, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_604, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_605, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_606, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_607, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_608, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_609, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_610, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_611, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_612, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_613, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_614, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_615, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_616, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_617, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_618, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_619, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_620, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_621, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_622, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_623, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_624, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_625, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_626, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_627, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_628, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_629, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_630, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_631, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_632, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_633, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_634, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_635, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_636, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_637, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_638, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_639, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_640, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_641, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_642, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_643, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_644, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_645, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_646, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_647, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_648, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_649, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_650, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_651, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_652, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_653, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_654, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_655, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_656, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_657, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_658, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_659, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_660, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_661, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_662, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_663, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_664, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_665, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_666, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_667, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_668, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_669, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_670, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_671, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_672, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_673, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_674, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_675, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_676, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_677, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_678, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_679, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_680, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_681, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_682, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_683, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_684, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_685, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_686, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_687, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_688, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_689, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_690, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_691, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_692, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_693, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_694, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_695, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_696, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_697, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_698, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_699, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_700, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_701, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_702, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_703, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_704, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_705, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_706, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_707, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_708, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_709, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_710, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_711, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_712, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_713, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_714, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_715, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_716, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_717, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_718, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_719, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_720, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_721, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_722, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_723, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_724, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_725, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_726, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_727, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_728, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_729, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_730, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_731, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_732, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_733, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_734, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_735, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_736, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_737, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_738, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_739, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_740, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_741, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_742, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_743, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_744, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_745, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_746, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_747, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_748, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_749, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_750, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_751, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_752, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_753, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_754, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_755, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_756, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_757, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_758, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_759, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_760, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_761, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_762, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_763, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_764, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_765, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_766, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_767, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_768, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_769, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_770, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_771, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_772, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_773, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_774, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_775, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_776, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_777, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_778, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_779, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_780, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_781, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_782, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_783, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_784, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_785, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_786, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_787, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_788, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_789, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_790, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_791, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_792, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_793, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_794, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_795, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_796, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_797, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_798, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_799, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_800, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_801, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_802, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_803, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_804, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_805, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_806, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_807, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_808, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_809, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_810, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_811, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_812, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_813, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_814, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_815, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_816, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_817, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_818, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_819, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_820, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_821, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_822, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_823, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_824, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_825, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_826, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_827, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_828, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_829, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_830, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_831, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_832, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_833, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_834, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_835, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_836, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_837, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_838, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_839, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_840, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_841, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_842, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_843, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_844, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_845, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_846, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_847, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_848, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_849, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_850, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_851, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_852, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_853, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_854, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_855, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_856, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_857, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_858, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_859, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_860, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_861, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_862, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_863, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_864, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_865, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_866, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_867, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_868, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_869, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_870, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_871, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_872, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_873, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_874, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_875, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_876, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_877, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_878, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_879, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_880, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_881, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_882, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_883, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_884, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_885, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_886, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_887, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_888, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_889, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_890, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_891, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_892, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_893, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_894, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_895, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_896, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_897, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_898, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_899, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_900, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_901, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_902, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_903, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_904, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_905, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_906, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_907, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_908, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_909, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_910, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_911, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_912, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_913, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_914, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_915, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_916, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_917, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_918, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_919, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_920, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_921, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_922, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_923, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_924, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_925, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_926, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_927, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_928, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_929, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_930, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_931, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_932, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_933, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_934, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_935, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_936, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_937, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_938, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_939, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_940, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_941, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_942, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_943, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_944, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_945, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_946, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_947, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_948, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_949, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_950, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_951, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_952, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_953, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_954, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_955, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_956, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_957, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_958, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_959, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_960, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_961, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_962, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_963, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_964, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_965, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_966, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_967, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_968, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_969, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_970, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_971, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_972, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_973, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_974, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_975, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_976, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_977, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_978, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_979, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_980, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_981, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_982, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_983, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_984, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_985, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_986, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_987, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_988, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_989, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_990, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_991, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_992, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_993, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_994, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_995, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_996, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_997, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_998, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_999, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_1000, 100_000 * 10**6, {"from": coinbase})

    print(f'########################## Transferred Done at 1000 person ##################################')





    change_pause_status = TheRanchBullsMintAndReward.setPauseStatus(False, {"from": multisig})
  
    #owner starts the public sale
    TheRanchBullsMintAndReward.togglePublicSaleStatus({"from": multisig})


   
    def price_needed(count):
        return (count * TheRanchBullsMintAndReward.mintingCost() * 10 ** 6)

 

    raffleEntryBool = True


    amt = 1
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_2})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_3})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_3, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_4})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_5})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_6})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_6, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_7})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_7, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_8})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_8, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_9})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_9, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_10})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_10, "value":  price_needed(amt)})
    
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_11})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_11, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_12})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_12, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_13})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_13, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_14})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_14, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_15})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_15, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_16})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_16, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_17})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_17, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_18})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_18, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_19})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_19, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_20})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_20, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_21})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_21, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_22})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_22, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_23})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_23, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_24})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_24, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_25})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_25, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_26})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_26, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_27})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_27, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_28})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_28, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_29})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_29, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_30})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_30, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_31})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_31, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_32})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_32, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_33})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_33, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_34})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_34, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_35})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_35, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_36})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_36, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_37})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_37, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_38})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_38, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_39})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_39, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_40})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_40, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_41})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_41, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_42})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_42, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_43})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_43, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_44})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_44, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_45})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_45, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_46})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_46, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_47})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_47, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_48})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_48, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_49})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_49, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_50})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_50, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_51})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_51, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_52})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_52, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_53})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_53, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_54})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_54, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_55})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_55, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_56})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_56, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_57})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_57, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_58})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_58, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_59})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_59, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_60})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_60, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_61})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_61, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_62})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_62, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_63})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_63, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_64})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_64, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_65})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_65, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_66})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_66, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_67})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_67, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_68})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_68, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_69})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_69, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_70})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_70, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_71})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_71, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_72})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_72, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_73})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_73, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_74})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_74, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_75})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_75, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_76})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_76, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_77})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_77, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_78})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_78, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_79})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_79, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_80})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_80, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_81})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_81, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_82})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_82, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_83})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_83, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_84})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_84, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_85})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_85, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_86})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_86, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_87})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_87, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_88})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_88, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_89})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_89, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_90})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_90, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_91})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_91, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_92})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_92, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_93})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_93, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_94})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_94, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_95})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_95, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_96})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_96, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_97})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_97, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_98})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_98, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_99})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_99, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_100})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_100, "value":  price_needed(amt)})






    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_101})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_101, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_102})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_102, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_103})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_103, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_104})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_104, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_105})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_105, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_106})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_106, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_107})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_107, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_108})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_108, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_109})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_109, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_110})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_110, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_111})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_111, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_112})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_112, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_113})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_113, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_114})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_114, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_115})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_115, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_116})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_116, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_117})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_117, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_118})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_118, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_119})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_119, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_120})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_120, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_121})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_121, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_122})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_122, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_123})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_123, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_124})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_124, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_125})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_125, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_126})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_126, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_127})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_127, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_128})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_128, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_129})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_129, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_130})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_130, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_131})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_131, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_132})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_132, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_133})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_133, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_134})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_134, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_135})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_135, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_136})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_136, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_137})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_137, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_138})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_138, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_139})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_139, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_140})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_140, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_141})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_141, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_142})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_142, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_143})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_143, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_144})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_144, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_145})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_145, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_146})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_146, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_147})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_147, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_148})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_148, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_149})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_149, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_150})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_150, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_151})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_151, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_152})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_152, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_153})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_153, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_154})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_154, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_155})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_155, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_156})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_156, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_157})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_157, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_158})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_158, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_159})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_159, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_160})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_160, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_161})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_161, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_162})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_162, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_163})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_163, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_164})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_164, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_165})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_165, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_166})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_166, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_167})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_167, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_168})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_168, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_169})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_169, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_170})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_170, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_171})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_171, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_172})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_172, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_173})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_173, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_174})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_174, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_175})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_175, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_176})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_176, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_177})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_177, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_178})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_178, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_179})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_179, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_180})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_180, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_181})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_181, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_182})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_182, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_183})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_183, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_184})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_184, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_185})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_185, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_186})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_186, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_187})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_187, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_188})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_188, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_189})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_189, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_190})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_190, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_191})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_191, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_192})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_192, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_193})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_193, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_194})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_194, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_195})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_195, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_196})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_196, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_197})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_197, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_198})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_198, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_199})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_199, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_200})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_200, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_201})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_201, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_202})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_202, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_203})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_203, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_204})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_204, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_205})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_205, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_206})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_206, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_207})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_207, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_208})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_208, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_209})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_209, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_210})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_210, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_211})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_211, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_212})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_212, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_213})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_213, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_214})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_214, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_215})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_215, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_216})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_216, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_217})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_217, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_218})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_218, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_219})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_219, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_220})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_220, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_221})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_221, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_222})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_222, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_223})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_223, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_224})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_224, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_225})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_225, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_226})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_226, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_227})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_227, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_228})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_228, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_229})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_229, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_230})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_230, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_231})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_231, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_232})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_232, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_233})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_233, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_234})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_234, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_235})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_235, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_236})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_236, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_237})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_237, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_238})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_238, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_239})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_239, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_240})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_240, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_241})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_241, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_242})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_242, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_243})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_243, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_244})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_244, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_245})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_245, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_246})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_246, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_247})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_247, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_248})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_248, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_249})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_249, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_250})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_250, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_251})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_251, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_252})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_252, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_253})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_253, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_254})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_254, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_255})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_255, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_256})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_256, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_257})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_257, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_258})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_258, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_259})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_259, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_260})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_260, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_261})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_261, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_262})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_262, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_263})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_263, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_264})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_264, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_265})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_265, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_266})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_266, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_267})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_267, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_268})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_268, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_269})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_269, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_270})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_270, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_271})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_271, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_272})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_272, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_273})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_273, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_274})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_274, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_275})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_275, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_276})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_276, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_277})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_277, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_278})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_278, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_279})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_279, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_280})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_280, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_281})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_281, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_282})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_282, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_283})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_283, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_284})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_284, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_285})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_285, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_286})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_286, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_287})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_287, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_288})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_288, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_289})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_289, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_290})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_290, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_291})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_291, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_292})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_292, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_293})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_293, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_294})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_294, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_295})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_295, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_296})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_296, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_297})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_297, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_298})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_298, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_299})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_299, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_300})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_300, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_301})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_301, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_302})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_302, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_303})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_303, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_304})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_304, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_305})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_305, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_306})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_306, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_307})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_307, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_308})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_308, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_309})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_309, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_310})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_310, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_311})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_311, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_312})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_312, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_313})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_313, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_314})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_314, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_315})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_315, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_316})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_316, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_317})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_317, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_318})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_318, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_319})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_319, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_320})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_320, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_321})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_321, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_322})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_322, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_323})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_323, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_324})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_324, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_325})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_325, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_326})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_326, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_327})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_327, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_328})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_328, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_329})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_329, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_330})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_330, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_331})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_331, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_332})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_332, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_333})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_333, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_334})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_334, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_335})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_335, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_336})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_336, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_337})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_337, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_338})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_338, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_339})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_339, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_340})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_340, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_341})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_341, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_342})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_342, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_343})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_343, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_344})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_344, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_345})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_345, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_346})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_346, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_347})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_347, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_348})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_348, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_349})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_349, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_350})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_350, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_351})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_351, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_352})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_352, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_353})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_353, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_354})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_354, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_355})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_355, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_356})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_356, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_357})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_357, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_358})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_358, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_359})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_359, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_360})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_360, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_361})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_361, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_362})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_362, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_363})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_363, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_364})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_364, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_365})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_365, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_366})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_366, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_367})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_367, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_368})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_368, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_369})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_369, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_370})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_370, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_371})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_371, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_372})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_372, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_373})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_373, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_374})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_374, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_375})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_375, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_376})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_376, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_377})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_377, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_378})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_378, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_379})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_379, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_380})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_380, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_381})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_381, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_382})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_382, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_383})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_383, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_384})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_384, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_385})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_385, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_386})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_386, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_387})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_387, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_388})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_388, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_389})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_389, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_390})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_390, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_391})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_391, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_392})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_392, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_393})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_393, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_394})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_394, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_395})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_395, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_396})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_396, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_397})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_397, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_398})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_398, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_399})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_399, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_400})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_400, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_401})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_401, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_402})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_402, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_403})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_403, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_404})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_404, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_405})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_405, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_406})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_406, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_407})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_407, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_408})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_408, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_409})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_409, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_410})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_410, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_411})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_411, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_412})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_412, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_413})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_413, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_414})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_414, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_415})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_415, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_416})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_416, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_417})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_417, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_418})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_418, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_419})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_419, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_420})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_420, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_421})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_421, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_422})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_422, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_423})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_423, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_424})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_424, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_425})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_425, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_426})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_426, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_427})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_427, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_428})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_428, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_429})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_429, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_430})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_430, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_431})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_431, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_432})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_432, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_433})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_433, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_434})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_434, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_435})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_435, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_436})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_436, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_437})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_437, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_438})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_438, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_439})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_439, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_440})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_440, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_441})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_441, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_442})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_442, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_443})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_443, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_444})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_444, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_445})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_445, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_446})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_446, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_447})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_447, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_448})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_448, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_449})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_449, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_450})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_450, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_451})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_451, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_452})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_452, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_453})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_453, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_454})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_454, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_455})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_455, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_456})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_456, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_457})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_457, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_458})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_458, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_459})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_459, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_460})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_460, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_461})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_461, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_462})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_462, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_463})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_463, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_464})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_464, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_465})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_465, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_466})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_466, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_467})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_467, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_468})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_468, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_469})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_469, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_470})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_470, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_471})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_471, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_472})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_472, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_473})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_473, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_474})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_474, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_475})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_475, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_476})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_476, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_477})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_477, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_478})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_478, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_479})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_479, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_480})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_480, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_481})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_481, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_482})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_482, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_483})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_483, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_484})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_484, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_485})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_485, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_486})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_486, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_487})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_487, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_488})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_488, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_489})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_489, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_490})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_490, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_491})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_491, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_492})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_492, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_493})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_493, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_494})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_494, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_495})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_495, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_496})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_496, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_497})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_497, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_498})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_498, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_499})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_499, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_500})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_500, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_501})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_501, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_502})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_502, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_503})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_503, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_504})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_504, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_505})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_505, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_506})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_506, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_507})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_507, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_508})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_508, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_509})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_509, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_510})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_510, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_511})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_511, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_512})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_512, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_513})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_513, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_514})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_514, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_515})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_515, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_516})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_516, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_517})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_517, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_518})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_518, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_519})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_519, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_520})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_520, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_521})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_521, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_522})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_522, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_523})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_523, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_524})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_524, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_525})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_525, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_526})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_526, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_527})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_527, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_528})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_528, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_529})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_529, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_530})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_530, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_531})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_531, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_532})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_532, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_533})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_533, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_534})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_534, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_535})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_535, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_536})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_536, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_537})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_537, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_538})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_538, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_539})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_539, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_540})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_540, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_541})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_541, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_542})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_542, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_543})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_543, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_544})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_544, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_545})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_545, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_546})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_546, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_547})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_547, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_548})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_548, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_549})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_549, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_550})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_550, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_551})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_551, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_552})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_552, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_553})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_553, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_554})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_554, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_555})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_555, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_556})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_556, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_557})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_557, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_558})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_558, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_559})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_559, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_560})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_560, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_561})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_561, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_562})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_562, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_563})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_563, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_564})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_564, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_565})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_565, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_566})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_566, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_567})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_567, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_568})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_568, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_569})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_569, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_570})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_570, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_571})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_571, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_572})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_572, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_573})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_573, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_574})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_574, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_575})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_575, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_576})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_576, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_577})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_577, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_578})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_578, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_579})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_579, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_580})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_580, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_581})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_581, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_582})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_582, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_583})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_583, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_584})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_584, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_585})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_585, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_586})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_586, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_587})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_587, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_588})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_588, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_589})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_589, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_590})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_590, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_591})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_591, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_592})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_592, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_593})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_593, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_594})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_594, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_595})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_595, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_596})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_596, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_597})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_597, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_598})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_598, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_599})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_599, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_600})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_600, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_601})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_601, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_602})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_602, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_603})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_603, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_604})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_604, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_605})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_605, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_606})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_606, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_607})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_607, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_608})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_608, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_609})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_609, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_610})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_610, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_611})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_611, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_612})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_612, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_613})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_613, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_614})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_614, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_615})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_615, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_616})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_616, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_617})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_617, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_618})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_618, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_619})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_619, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_620})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_620, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_621})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_621, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_622})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_622, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_623})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_623, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_624})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_624, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_625})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_625, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_626})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_626, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_627})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_627, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_628})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_628, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_629})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_629, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_630})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_630, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_631})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_631, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_632})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_632, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_633})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_633, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_634})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_634, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_635})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_635, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_636})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_636, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_637})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_637, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_638})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_638, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_639})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_639, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_640})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_640, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_641})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_641, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_642})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_642, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_643})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_643, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_644})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_644, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_645})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_645, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_646})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_646, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_647})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_647, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_648})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_648, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_649})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_649, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_650})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_650, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_651})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_651, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_652})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_652, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_653})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_653, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_654})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_654, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_655})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_655, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_656})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_656, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_657})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_657, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_658})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_658, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_659})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_659, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_660})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_660, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_661})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_661, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_662})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_662, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_663})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_663, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_664})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_664, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_665})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_665, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_666})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_666, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_667})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_667, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_668})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_668, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_669})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_669, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_670})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_670, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_671})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_671, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_672})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_672, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_673})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_673, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_674})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_674, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_675})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_675, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_676})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_676, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_677})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_677, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_678})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_678, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_679})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_679, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_680})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_680, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_681})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_681, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_682})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_682, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_683})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_683, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_684})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_684, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_685})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_685, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_686})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_686, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_687})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_687, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_688})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_688, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_689})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_689, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_690})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_690, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_691})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_691, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_692})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_692, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_693})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_693, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_694})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_694, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_695})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_695, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_696})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_696, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_697})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_697, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_698})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_698, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_699})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_699, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_700})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_700, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_701})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_701, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_702})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_702, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_703})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_703, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_704})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_704, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_705})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_705, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_706})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_706, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_707})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_707, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_708})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_708, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_709})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_709, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_710})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_710, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_711})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_711, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_712})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_712, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_713})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_713, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_714})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_714, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_715})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_715, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_716})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_716, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_717})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_717, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_718})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_718, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_719})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_719, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_720})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_720, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_721})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_721, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_722})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_722, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_723})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_723, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_724})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_724, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_725})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_725, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_726})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_726, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_727})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_727, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_728})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_728, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_729})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_729, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_730})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_730, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_731})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_731, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_732})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_732, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_733})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_733, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_734})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_734, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_735})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_735, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_736})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_736, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_737})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_737, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_738})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_738, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_739})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_739, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_740})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_740, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_741})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_741, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_742})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_742, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_743})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_743, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_744})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_744, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_745})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_745, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_746})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_746, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_747})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_747, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_748})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_748, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_749})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_749, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_750})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_750, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_751})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_751, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_752})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_752, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_753})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_753, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_754})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_754, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_755})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_755, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_756})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_756, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_757})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_757, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_758})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_758, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_759})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_759, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_760})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_760, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_761})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_761, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_762})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_762, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_763})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_763, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_764})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_764, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_765})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_765, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_766})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_766, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_767})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_767, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_768})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_768, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_769})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_769, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_770})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_770, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_771})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_771, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_772})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_772, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_773})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_773, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_774})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_774, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_775})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_775, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_776})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_776, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_777})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_777, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_778})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_778, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_779})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_779, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_780})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_780, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_781})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_781, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_782})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_782, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_783})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_783, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_784})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_784, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_785})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_785, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_786})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_786, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_787})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_787, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_788})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_788, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_789})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_789, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_790})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_790, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_791})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_791, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_792})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_792, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_793})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_793, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_794})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_794, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_795})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_795, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_796})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_796, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_797})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_797, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_798})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_798, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_799})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_799, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_800})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_800, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_801})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_801, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_802})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_802, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_803})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_803, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_804})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_804, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_805})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_805, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_806})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_806, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_807})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_807, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_808})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_808, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_809})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_809, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_810})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_810, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_811})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_811, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_812})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_812, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_813})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_813, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_814})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_814, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_815})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_815, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_816})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_816, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_817})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_817, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_818})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_818, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_819})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_819, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_820})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_820, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_821})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_821, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_822})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_822, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_823})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_823, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_824})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_824, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_825})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_825, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_826})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_826, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_827})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_827, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_828})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_828, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_829})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_829, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_830})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_830, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_831})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_831, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_832})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_832, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_833})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_833, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_834})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_834, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_835})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_835, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_836})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_836, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_837})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_837, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_838})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_838, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_839})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_839, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_840})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_840, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_841})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_841, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_842})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_842, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_843})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_843, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_844})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_844, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_845})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_845, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_846})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_846, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_847})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_847, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_848})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_848, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_849})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_849, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_850})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_850, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_851})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_851, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_852})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_852, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_853})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_853, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_854})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_854, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_855})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_855, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_856})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_856, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_857})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_857, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_858})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_858, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_859})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_859, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_860})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_860, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_861})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_861, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_862})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_862, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_863})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_863, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_864})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_864, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_865})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_865, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_866})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_866, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_867})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_867, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_868})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_868, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_869})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_869, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_870})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_870, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_871})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_871, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_872})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_872, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_873})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_873, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_874})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_874, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_875})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_875, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_876})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_876, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_877})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_877, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_878})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_878, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_879})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_879, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_880})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_880, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_881})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_881, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_882})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_882, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_883})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_883, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_884})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_884, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_885})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_885, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_886})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_886, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_887})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_887, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_888})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_888, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_889})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_889, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_890})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_890, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_891})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_891, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_892})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_892, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_893})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_893, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_894})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_894, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_895})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_895, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_896})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_896, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_897})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_897, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_898})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_898, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_899})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_899, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_900})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_900, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_901})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_901, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_902})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_902, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_903})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_903, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_904})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_904, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_905})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_905, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_906})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_906, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_907})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_907, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_908})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_908, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_909})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_909, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_910})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_910, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_911})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_911, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_912})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_912, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_913})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_913, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_914})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_914, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_915})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_915, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_916})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_916, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_917})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_917, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_918})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_918, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_919})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_919, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_920})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_920, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_921})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_921, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_922})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_922, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_923})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_923, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_924})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_924, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_925})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_925, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_926})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_926, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_927})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_927, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_928})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_928, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_929})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_929, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_930})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_930, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_931})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_931, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_932})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_932, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_933})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_933, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_934})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_934, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_935})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_935, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_936})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_936, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_937})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_937, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_938})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_938, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_939})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_939, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_940})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_940, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_941})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_941, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_942})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_942, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_943})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_943, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_944})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_944, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_945})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_945, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_946})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_946, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_947})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_947, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_948})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_948, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_949})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_949, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_950})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_950, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_951})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_951, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_952})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_952, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_953})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_953, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_954})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_954, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_955})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_955, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_956})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_956, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_957})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_957, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_958})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_958, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_959})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_959, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_960})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_960, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_961})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_961, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_962})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_962, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_963})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_963, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_964})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_964, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_965})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_965, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_966})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_966, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_967})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_967, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_968})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_968, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_969})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_969, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_970})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_970, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_971})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_971, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_972})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_972, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_973})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_973, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_974})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_974, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_975})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_975, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_976})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_976, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_977})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_977, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_978})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_978, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_979})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_979, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_980})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_980, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_981})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_981, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_982})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_982, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_983})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_983, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_984})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_984, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_985})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_985, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_986})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_986, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_987})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_987, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_988})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_988, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_989})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_989, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_990})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_990, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_991})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_991, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_992})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_992, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_993})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_993, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_994})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_994, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_995})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_995, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_996})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_996, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_997})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_997, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_998})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_998, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_999})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_999, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1000})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1000, "value":  price_needed(amt)})








    print(f'########################## Minting at 1000 person ##################################')



   


    print(f'Total Mints: {TheRanchBullsMintAndReward.totalSupply()}')
   


    
    print("#######################################################################################")
    print(f'\t\t\t\t\t BEFORE FUNDING AND UPDATING')
    print("#######################################################################################")
    print(f'coreTeam_1 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":coreTeam1})  }')
    print(f'coreTeam_2 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":coreTeam2})  }')
    print(f'person_1 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_1})  }')
    print(f'person_2 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_2})  }')
    print(f'person_3 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_3})  }')
    print(f'person_4 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_4})  }')
    print(f'person_5 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_5})  }')
    print(f'person_6 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_6})  }')
    print(f'person_7 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_7})  }')
    print(f'person_8 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_8})  }')
    print(f'person_9 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_9})  }')



    print("\n")


    print(f'coreTeam_1 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":coreTeam1})  }')
    print(f'coreTeam_2 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":coreTeam2})  }')
    print(f'person_1 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_1})  }')
    print(f'person_2 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_2})  }')
    print(f'person_3 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_3})  }')
    print(f'person_4 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_4})  }')
    print(f'person_5 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_5})  }')
    print(f'person_6 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_6})  }')
    print(f'person_7 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_7})  }')
    print(f'person_8 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_8})  }')
    print(f'person_9 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_9})  }')

    print("\n")

    print(f'coreTeam_1 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":coreTeam1})  }')
    print(f'coreTeam_2 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":coreTeam2})  }')
    print(f'person_1 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_1})  }')
    print(f'person_2 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_2})  }')
    print(f'person_3 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_3})  }')
    print(f'person_4 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_4})  }')
    print(f'person_5 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_5})  }')
    print(f'person_6 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_6})  }')
    print(f'person_7 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_7})  }')
    print(f'person_8 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_8})  }')
    print(f'person_9 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_9})  }')









    print(f'Wallet of person_1: {TheRanchBullsMintAndReward.walletOfOwner(person_1)}')
    print(f'Wallet of person_1: {TheRanchBullsMintAndReward.walletOfOwner(person_1)}') 
    print(f'Wallet of person_2: {TheRanchBullsMintAndReward.walletOfOwner(person_2)}') 
    print(f'Wallet of person_3: {TheRanchBullsMintAndReward.walletOfOwner(person_3)}')
    print(f'Wallet of person_4: {TheRanchBullsMintAndReward.walletOfOwner(person_4)}')
    print(f'Wallet of person_5: {TheRanchBullsMintAndReward.walletOfOwner(person_5)}')
    print(f'Wallet of person_6: {TheRanchBullsMintAndReward.walletOfOwner(person_6)}')
    print(f'Wallet of person_7: {TheRanchBullsMintAndReward.walletOfOwner(person_7)}')
    print(f'Wallet of person_8: {TheRanchBullsMintAndReward.walletOfOwner(person_8)}')
    print(f'Wallet of person_9: {TheRanchBullsMintAndReward.walletOfOwner(person_9)}')
    print(f'Wallet of person_10: {TheRanchBullsMintAndReward.walletOfOwner(person_10)}')
    print(f'Wallet of person_11: {TheRanchBullsMintAndReward.walletOfOwner(person_11)}')
    print(f'Wallet of person_12: {TheRanchBullsMintAndReward.walletOfOwner(person_12)}')
    print(f'Wallet of person_13: {TheRanchBullsMintAndReward.walletOfOwner(person_13)}')
    print(f'Wallet of person_14: {TheRanchBullsMintAndReward.walletOfOwner(person_14)}')
    print(f'Wallet of person_15: {TheRanchBullsMintAndReward.walletOfOwner(person_15)}')
    print(f'Wallet of person_16: {TheRanchBullsMintAndReward.walletOfOwner(person_16)}')
    print(f'Wallet of person_17: {TheRanchBullsMintAndReward.walletOfOwner(person_17)}')
    print(f'Wallet of person_18: {TheRanchBullsMintAndReward.walletOfOwner(person_18)}')
    print(f'Wallet of person_19: {TheRanchBullsMintAndReward.walletOfOwner(person_19)}')
    print(f'Wallet of person_20: {TheRanchBullsMintAndReward.walletOfOwner(person_20)}')
    print(f'Wallet of person_21: {TheRanchBullsMintAndReward.walletOfOwner(person_21)}')
    print(f'Wallet of person_22: {TheRanchBullsMintAndReward.walletOfOwner(person_22)}')
    print(f'Wallet of person_23: {TheRanchBullsMintAndReward.walletOfOwner(person_23)}')
    print(f'Wallet of person_24: {TheRanchBullsMintAndReward.walletOfOwner(person_24)}')
    print(f'Wallet of person_25: {TheRanchBullsMintAndReward.walletOfOwner(person_25)}')
    print(f'Wallet of person_26: {TheRanchBullsMintAndReward.walletOfOwner(person_26)}')
    print(f'Wallet of person_27: {TheRanchBullsMintAndReward.walletOfOwner(person_27)}')
    print(f'Wallet of person_28: {TheRanchBullsMintAndReward.walletOfOwner(person_28)}')
    print(f'Wallet of person_29: {TheRanchBullsMintAndReward.walletOfOwner(person_29)}')
    print(f'Wallet of person_30: {TheRanchBullsMintAndReward.walletOfOwner(person_30)}')










     #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #                                                                              ROUND 1                                                                                #
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################


    #################################################################
    ######### owner needs to set the stockyard information  ###########
    #################################################################

    tx_set_stockyard = TheRanchBullsMintAndReward.setStockYardInfo(1,0,1,1000, {"from": multisig})
   
    # tx_set_stockyard = TheRanchBullsMintAndReward.setStockYardInfo(2,0,16,30, {"from": multisig})

    print("\n")
    print(f'stockyard_0: {TheRanchBullsMintAndReward.stockyardInfo(0)}')
    print(f'stockyard_1: {TheRanchBullsMintAndReward.stockyardInfo(1)}')
    print(f'stockyard_2: {TheRanchBullsMintAndReward.stockyardInfo(2)}')
    print(f'stockyard_3: {TheRanchBullsMintAndReward.stockyardInfo(3)}')

    #################################################################
    ######### owner needs to send funds and set the pay per nft  ####
    #################################################################

    assert TheRanchBullsMintAndReward.payPerNftForTheMonth.call() == 0


    total_to_deposit = 1 * 10 ** 8 

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    fundAndSetPayPerNFT = TheRanchBullsMintAndReward.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0322',{"from": multisig})
    print(fundAndSetPayPerNFT.info())



    print(TheRanchBullsMintAndReward.payPerNftForTheMonth.call())

    expected_amt_per_nft = ((total_to_deposit * .90) / TheRanchBullsMintAndReward.totalSupply())
    assert TheRanchBullsMintAndReward.payPerNftForTheMonth.call() == expected_amt_per_nft



    ###########################################################
    ######### owner updates the maintenance fees variable ####
    ###########################################################

    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(12*10**6, {"from": multisig})   # 12 dollars in USDC.e for round 2
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 12*10**6

    #### set the defender wallet up to allow this ###
    TheRanchBullsMintAndReward.setDefenderRole(defender_wallet, True, {"from": multisig})


    ### call the readyToReward function to begin the rewarding process ###
    TheRanchBullsMintAndReward.setReadyToReward({"from": multisig})


    


    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################

    ### pause the contract ###
    TheRanchBullsMintAndReward.setPauseStatus(True, {"from": defender_wallet})

   



    assert TheRanchBullsMintAndReward.stockyardsThatHaveBeenRewardedCount.call() == 0


    #######################
    ###      REWARD     ###
    #######################

    ### check if we can reward the same stockyard twice or skip a stockyard on accident

 
    reward_tx = TheRanchBullsMintAndReward.rewardBulls(1,{"from": defender_wallet})
    print(reward_tx.info())

    # reward_tx = TheRanchBullsMintAndReward.rewardBulls(2,{"from": defender_wallet})
    # print(reward_tx.info())
    
    # reward_tx = TheRanchBullsMintAndReward.rewardBulls(3,{"from": defender_wallet})
    # print(reward_tx.info())

    # reward_tx = TheRanchBullsMintAndReward.rewardBulls(4,{"from": defender_wallet})
    # print(reward_tx.info())









    print("#######################################################################################")
    print(f'\t\t\t\t\t AFTER REWARDING')
    print("#######################################################################################")
    print(f'coreTeam_1 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":coreTeam1})  }')
    print(f'coreTeam_2 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":coreTeam2})  }')
    print(f'person_1 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_1})  }')
    print(f'person_2 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_2})  }')
    print(f'person_3 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_3})  }')
    print(f'person_4 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_4})  }')
    print(f'person_5 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_5})  }')
    print(f'person_6 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_6})  }')
    print(f'person_7 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_7})  }')
    print(f'person_8 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_8})  }')
    print(f'person_9 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_9})  }')



    print("\n")


    print(f'coreTeam_1 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":coreTeam1})  }')
    print(f'coreTeam_2 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":coreTeam2})  }')
    print(f'person_1 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_1})  }')
    print(f'person_2 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_2})  }')
    print(f'person_3 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_3})  }')
    print(f'person_4 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_4})  }')
    print(f'person_5 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_5})  }')
    print(f'person_6 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_6})  }')
    print(f'person_7 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_7})  }')
    print(f'person_8 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_8})  }')
    print(f'person_9 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_9})  }')

    print("\n")

    print(f'coreTeam_1 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":coreTeam1})  }')
    print(f'coreTeam_2 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":coreTeam2})  }')
    print(f'person_1 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_1})  }')
    print(f'person_2 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_2})  }')
    print(f'person_3 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_3})  }')
    print(f'person_4 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_4})  }')
    print(f'person_5 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_5})  }')
    print(f'person_6 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_6})  }')
    print(f'person_7 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_7})  }')
    print(f'person_8 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_8})  }')
    print(f'person_9 WBTC balance: {TheRanchBullsMintAndReward.getWbtctBalanceForTheOwner({"from":person_9})  }')























































    return





































































    ################################
    ###  UPDATE MAINTENANCE FEES ###
    ################################
 
    tx_update_fees = TheRanchBullsMintAndReward.updateMaintenanceFeesForTheMonth({"from": defender_wallet})
    print(tx_update_fees.info())


    finishing_identifier = tx_update_fees.events["MaintenanceFeeUpdatingEvent"]["sectionMessage"]

    assert 'STEP2DONE' in finishing_identifier


    ###############################
    ###  UPDATE MONTHS BEHIND   ###
    ################################

    tx_updateMonthsBehind = TheRanchBullsMintAndReward.updateMonthsBehindMaintenanceFeeDueDate({"from": defender_wallet})
    print(tx_updateMonthsBehind.info())

    finishing_identifier = tx_updateMonthsBehind.events["MaintenanceFeeEvent"]["sectionMessage"]

    assert 'STEP3DONE' in finishing_identifier



    tx_getLiquidityArrayLength = TheRanchBullsMintAndReward.getLiquidatedArrayLength({"from": defender_wallet})

    if tx_getLiquidityArrayLength < 1:
        print("Liquidation Not Needed")
        TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})
    else: 
        ############## LIQUIDATION #############
        print(f'Liquidation needed: Account to liquidate is __{tx_getLiquidityArrayLength}__')
        liquidation_event = TheRanchBullsMintAndReward.liquidateOutstandingAccounts({"from": multisig})
        print(liquidation_event.info())
        TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})



    ##########################
    ### ASSERT INFORMATION ###
    ##########################

    assert TheRanchBullsMintAndReward.paused.call() == False


    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1) == (12*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2) == (12*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_8) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_9) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_10) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_11) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_12) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_13) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_14) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_15) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_16) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_17) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_18) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_19) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_20) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_21) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_22) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_23) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_24) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_25) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_26) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_27) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_28) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_29) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_30) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_31) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_32) == 0


    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_8) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_9) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_10) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_11) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_12) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_13) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_14) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_15) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_16) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_17) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_18) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_19) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_20) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_21) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_22) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_23) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_24) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_25) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_26) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_27) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_28) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_29) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_30) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_31) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_32) == 0



    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_1}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_2}) == ((1*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_3}) == ((1*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_4}) == ((1*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_5}) == ((1*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_6}) == ((1*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_7}) == ((1*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_8}) == ((1*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_9}) == ((1*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_10}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_11}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_12}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_13}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_14}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_15}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_16}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_17}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_18}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_19}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_20}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_21}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_22}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_23}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_24}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_25}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_26}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_27}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_28}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_29}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_30}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_31}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_32}) == 0





    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #                                                                              ROUND 2                                                                                #
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################


    #################################################################
    ######### owner needs to send funds to the stockyard  ###########
    #################################################################

    amount_to_send = 1 * wbtc_decimals 
    print(f'money to approve : {amount_to_send}')
    total_to_deposit = amount_to_send

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    tx_fundBulls = TheRanchBullsMintAndReward.fundBulls(1,total_to_deposit, {"from": multisig})
    print(tx_fundBulls.info())





    amount_to_send = 1 * wbtc_decimals 
    print(f'money to approve : {amount_to_send}')
    total_to_deposit = amount_to_send

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    tx_fundBulls = TheRanchBullsMintAndReward.fundBulls(2,total_to_deposit, {"from": multisig})
    print(tx_fundBulls.info())


    
    assert tx_fundBulls.events["LoadedFundsIntoStockyard"]["amountDeposited"] == total_to_deposit

    print(tx_fundBulls.info())

  

    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(12*10**6, {"from": multisig})   # 12 dollars in USDC.e for round 2
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 12*10**6


    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################


    #######################
    ###      REWARD     ###
    #######################
    TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})

  
    fund_and_reward_tx = TheRanchBullsMintAndReward.rewardBulls(1,{"from": defender_wallet})
    print(fund_and_reward_tx.info())

    fund_and_reward_tx = TheRanchBullsMintAndReward.rewardBulls(2,{"from": defender_wallet})
    print(fund_and_reward_tx.info())


    ################################
    ###  UPDATE MAINTENANCE FEES ###
    ################################
 
    tx_update_fees = TheRanchBullsMintAndReward.updateMaintenanceFeesForTheMonth({"from": defender_wallet})
    print(tx_update_fees.info())


    finishing_identifier = tx_update_fees.events["MaintenanceFeeUpdatingEvent"]["sectionMessage"]

    assert 'STEP2DONE' in finishing_identifier


    ###############################
    ###  UPDATE MONTHS BEHIND   ###
    ################################

    tx_updateMonthsBehind = TheRanchBullsMintAndReward.updateMonthsBehindMaintenanceFeeDueDate({"from": defender_wallet})
    print(tx_updateMonthsBehind.info())

    finishing_identifier = tx_updateMonthsBehind.events["MaintenanceFeeEvent"]["sectionMessage"]

    assert 'STEP3DONE' in finishing_identifier



    tx_getLiquidityArrayLength = TheRanchBullsMintAndReward.getLiquidatedArrayLength({"from": defender_wallet})

    if tx_getLiquidityArrayLength < 1:
        print("Liquidation Not Needed")
        TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})
    else: 
        ############## LIQUIDATION #############
        print(f'Liquidation needed: Account to liquidate is __{tx_getLiquidityArrayLength}__')
        liquidation_event = TheRanchBullsMintAndReward.liquidateOutstandingAccounts({"from": multisig})
        print(liquidation_event.info())
        TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})



    ##########################
    ### ASSERT INFORMATION ###
    ##########################

    assert TheRanchBullsMintAndReward.paused.call() == False


    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1) == (24*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2) == (24*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_8) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_9) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_10) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_11) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_12) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_13) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_14) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_15) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_16) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_17) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_18) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_19) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_20) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_21) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_22) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_23) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_24) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_25) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_26) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_27) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_28) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_29) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_30) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_31) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_32) == 0


    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_8) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_9) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_10) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_11) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_12) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_13) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_14) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_15) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_16) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_17) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_18) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_19) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_20) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_21) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_22) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_23) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_24) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_25) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_26) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_27) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_28) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_29) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_30) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_31) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_32) == 0



    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_1}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_2}) == ((2*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_3}) == ((2*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_4}) == ((2*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_5}) == ((2*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_6}) == ((2*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_7}) == ((2*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_8}) == ((2*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_9}) == ((2*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_10}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_11}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_12}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_13}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_14}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_15}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_16}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_17}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_18}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_19}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_20}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_21}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_22}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_23}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_24}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_25}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_26}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_27}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_28}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_29}) == ((2*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_30}) == ((2*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_31}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_32}) == 0


    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #                                                                              ROUND 3                                                                                #
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################


    #################################################################
    ######### owner needs to send funds to the stockyard  ###########
    #################################################################

    amount_to_send = 1 * wbtc_decimals 
    print(f'money to approve : {amount_to_send}')
    total_to_deposit = amount_to_send

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    tx_fundBulls = TheRanchBullsMintAndReward.fundBulls(1,total_to_deposit, {"from": multisig})
    print(tx_fundBulls.info())





    amount_to_send = 1 * wbtc_decimals 
    print(f'money to approve : {amount_to_send}')
    total_to_deposit = amount_to_send

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    tx_fundBulls = TheRanchBullsMintAndReward.fundBulls(2,total_to_deposit, {"from": multisig})
    print(tx_fundBulls.info())


    
    assert tx_fundBulls.events["LoadedFundsIntoStockyard"]["amountDeposited"] == total_to_deposit

    print(tx_fundBulls.info())

  

    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(12*10**6, {"from": multisig})   # 12 dollars in USDC.e for round 2
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 12*10**6


    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################


    #######################
    ###      REWARD     ###
    #######################
    TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})

  
    fund_and_reward_tx = TheRanchBullsMintAndReward.rewardBulls(1,{"from": defender_wallet})
    print(fund_and_reward_tx.info())

    fund_and_reward_tx = TheRanchBullsMintAndReward.rewardBulls(2,{"from": defender_wallet})
    print(fund_and_reward_tx.info())


    ################################
    ###  UPDATE MAINTENANCE FEES ###
    ################################
 
    tx_update_fees = TheRanchBullsMintAndReward.updateMaintenanceFeesForTheMonth({"from": defender_wallet})
    print(tx_update_fees.info())


    finishing_identifier = tx_update_fees.events["MaintenanceFeeUpdatingEvent"]["sectionMessage"]

    assert 'STEP2DONE' in finishing_identifier


    ###############################
    ###  UPDATE MONTHS BEHIND   ###
    ################################

    tx_updateMonthsBehind = TheRanchBullsMintAndReward.updateMonthsBehindMaintenanceFeeDueDate({"from": defender_wallet})
    print(tx_updateMonthsBehind.info())

    finishing_identifier = tx_updateMonthsBehind.events["MaintenanceFeeEvent"]["sectionMessage"]

    assert 'STEP3DONE' in finishing_identifier



    tx_getLiquidityArrayLength = TheRanchBullsMintAndReward.getLiquidatedArrayLength({"from": defender_wallet})

    if tx_getLiquidityArrayLength < 1:
        print("Liquidation Not Needed")
        TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})
    else: 
        ############## LIQUIDATION #############
        print(f'Liquidation needed: Account to liquidate is __{tx_getLiquidityArrayLength}__')
        liquidation_event = TheRanchBullsMintAndReward.liquidateOutstandingAccounts({"from": multisig})
        print(liquidation_event.info())
        TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})


    ##########################
    ### ASSERT INFORMATION ###
    ##########################

    assert TheRanchBullsMintAndReward.paused.call() == False

    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1) == (36*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2) == (36*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_8) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_9) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_10) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_11) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_12) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_13) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_14) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_15) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_16) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_17) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_18) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_19) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_20) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_21) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_22) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_23) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_24) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_25) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_26) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_27) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_28) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_29) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_30) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_31) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_32) == 0


    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_8) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_9) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_10) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_11) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_12) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_13) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_14) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_15) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_16) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_17) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_18) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_19) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_20) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_21) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_22) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_23) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_24) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_25) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_26) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_27) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_28) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_29) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_30) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_31) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_32) == 0


    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_1}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_2}) == ((3*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_3}) == ((3*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_4}) == ((3*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_5}) == ((3*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_6}) == ((3*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_7}) == ((3*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_8}) == ((3*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_9}) == ((3*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_10}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_11}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_12}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_13}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_14}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_15}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_16}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_17}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_18}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_19}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_20}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_21}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_22}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_23}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_24}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_25}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_26}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_27}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_28}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_29}) == ((3*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_30}) == ((3*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_31}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_32}) == 0








    ################################################
    ##### Person 7 pays their maintenance fees #####
    ################################################
    
    usdc_rewards_7 = TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_7})
    maint_fees_7 = TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7)

    print(f'usdc person_7: {usdc_rewards_7}')
    print(f'maint_fees_person_7 {maint_fees_7}')

    if usdc_rewards_7 < maint_fees_7:
        amt_to_approve = maint_fees_7 - usdc_rewards_7
        mocked_usdc.approve(TheRanchBullsMintAndReward.address, amt_to_approve ,{"from":person_7})


    pay_maint_fees_person_7 = TheRanchBullsMintAndReward.payMaintanenceFees({"from": person_7})
    print(pay_maint_fees_person_7.info())

    assert pay_maint_fees_person_7.events["Transfer"]["value"] == maint_fees_7 - usdc_rewards_7






    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #                                                                              ROUND 4                                                                                #
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################



    #################################################################
    ######### owner needs to send funds to the stockyard  ###########
    #################################################################

    amount_to_send = 1 * wbtc_decimals 
    print(f'money to approve : {amount_to_send}')
    total_to_deposit = amount_to_send

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    tx_fundBulls = TheRanchBullsMintAndReward.fundBulls(1,total_to_deposit, {"from": multisig})
    print(tx_fundBulls.info())





    amount_to_send = 1 * wbtc_decimals 
    print(f'money to approve : {amount_to_send}')
    total_to_deposit = amount_to_send

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    tx_fundBulls = TheRanchBullsMintAndReward.fundBulls(2,total_to_deposit, {"from": multisig})
    print(tx_fundBulls.info())


    
    assert tx_fundBulls.events["LoadedFundsIntoStockyard"]["amountDeposited"] == total_to_deposit

    print(tx_fundBulls.info())

  

    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(12*10**6, {"from": multisig})   # 12 dollars in USDC.e for round 2
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 12*10**6


    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################


    #######################
    ###      REWARD     ###
    #######################
    TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})

  
    fund_and_reward_tx = TheRanchBullsMintAndReward.rewardBulls(1,{"from": defender_wallet})
    print(fund_and_reward_tx.info())

    fund_and_reward_tx = TheRanchBullsMintAndReward.rewardBulls(2,{"from": defender_wallet})
    print(fund_and_reward_tx.info())


    ################################
    ###  UPDATE MAINTENANCE FEES ###
    ################################
 
    tx_update_fees = TheRanchBullsMintAndReward.updateMaintenanceFeesForTheMonth({"from": defender_wallet})
    print(tx_update_fees.info())


    finishing_identifier = tx_update_fees.events["MaintenanceFeeUpdatingEvent"]["sectionMessage"]

    assert 'STEP2DONE' in finishing_identifier


    ###############################
    ###  UPDATE MONTHS BEHIND   ###
    ################################

    tx_updateMonthsBehind = TheRanchBullsMintAndReward.updateMonthsBehindMaintenanceFeeDueDate({"from": defender_wallet})
    print(tx_updateMonthsBehind.info())

    finishing_identifier = tx_updateMonthsBehind.events["MaintenanceFeeEvent"]["sectionMessage"]

    assert 'STEP3DONE' in finishing_identifier



    tx_getLiquidityArrayLength = TheRanchBullsMintAndReward.getLiquidatedArrayLength({"from": defender_wallet})

    if tx_getLiquidityArrayLength < 1:
        print("Liquidation Not Needed")
        TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})
    else: 
        ############## LIQUIDATION #############
        print(f'Liquidation needed: Account to liquidate is __{tx_getLiquidityArrayLength}__')
        liquidation_event = TheRanchBullsMintAndReward.liquidateOutstandingAccounts({"from": multisig})
        print(liquidation_event.info())
        TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})






    ##########################
    ### ASSERT INFORMATION ###
    ##########################

    assert TheRanchBullsMintAndReward.paused.call() == False

    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2) == 0  
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3) == 0  
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4) == 0  
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5) == 0  
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6) == 0  
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_8) == 0  
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_9) == 0  
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_10) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_11) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_12) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_13) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_14) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_15) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_16) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_17) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_18) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_19) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_20) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_21) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_22) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_23) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_24) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_25) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_26) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_27) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_28) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_29) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_30) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_31) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_32) == 0


    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2) == 0  
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3) == 0  
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4) == 0  
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5) == 0  
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6) == 0  
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7) == 1 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_8) == 0  
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_9) == 0  
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_10) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_11) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_12) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_13) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_14) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_15) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_16) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_17) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_18) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_19) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_20) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_21) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_22) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_23) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_24) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_25) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_26) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_27) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_28) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_29) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_30) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_31) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_32) == 0


    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_1}) == 0  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_2}) == 0  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_3}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_4}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_5}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_6}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_7}) == ((4*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_8}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_9}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_10}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_11}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_12}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_13}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_14}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_15}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_16}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_17}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_18}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_19}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_20}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_21}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_22}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_23}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_24}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_25}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_26}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_27}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_28}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_29}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_30}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_31}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_32}) == 0


