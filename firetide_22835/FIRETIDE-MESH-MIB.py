# SNMP MIB module (FIRETIDE-MESH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/firetide_22835/FIRETIDE-MESH-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:02:57 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

firetideMesh = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 1)
)
if mibBuilder.loadTexts:
    firetideMesh.setRevisions(
        ("2006-02-16 23:00",
         "2005-09-12 10:00",
         "2005-05-02 17:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RadioProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("radio80211a", 1),
          ("radio80211b", 2),
          ("radio80211g", 3),
          ("radio8021149", 4),
          ("radiodisabled", 10))
    )



class LinkType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wireless", 1),
          ("ethernet", 2),
          ("other", 3))
    )



class VerifyOperation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("verifying", 2),
          ("consistent", 3),
          ("inconsistent", 4))
    )



class NetworkOperation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("force", 2),
          ("failure", 3),
          ("inprogress", 4),
          ("completed", 5))
    )



class CountryCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8,
              12,
              31,
              32,
              36,
              40,
              48,
              51,
              56,
              68,
              76,
              84,
              96,
              100,
              112,
              124,
              152,
              156,
              158,
              170,
              188,
              191,
              196,
              203,
              208,
              214,
              218,
              222,
              233,
              234,
              246,
              250,
              255,
              268,
              276,
              300,
              320,
              340,
              344,
              348,
              352,
              356,
              360,
              364,
              368,
              372,
              376,
              380,
              388,
              392,
              393,
              394,
              395,
              396,
              397,
              398,
              400,
              404,
              408,
              410,
              411,
              414,
              422,
              428,
              434,
              438,
              440,
              442,
              446,
              458,
              484,
              492,
              504,
              512,
              528,
              554,
              558,
              578,
              586,
              591,
              600,
              604,
              608,
              616,
              620,
              630,
              634,
              642,
              643,
              682,
              702,
              703,
              704,
              705,
              710,
              716,
              724,
              752,
              756,
              760,
              764,
              780,
              784,
              788,
              792,
              804,
              807,
              818,
              826,
              840,
              858,
              860,
              862,
              887)
        )
    )
    namedValues = NamedValues(
        *(("notInitilized", 0),
          ("albania", 8),
          ("algeria", 12),
          ("azerbaijan", 31),
          ("argentina", 32),
          ("australia", 36),
          ("austria", 40),
          ("bahrain", 48),
          ("armenia", 51),
          ("belgium", 56),
          ("bolivia", 68),
          ("brazil", 76),
          ("belize", 84),
          ("bruneiDarussalam", 96),
          ("bulgaria", 100),
          ("belarus", 112),
          ("canada", 124),
          ("chile", 152),
          ("china", 156),
          ("taiwan", 158),
          ("colombia", 170),
          ("costaRica", 188),
          ("croatia", 191),
          ("cyprus", 196),
          ("czech", 203),
          ("denmark", 208),
          ("dominicanRepublic", 214),
          ("ecuador", 218),
          ("elSalvador", 222),
          ("estonia", 233),
          ("faeroeIslands", 234),
          ("finland", 246),
          ("france", 250),
          ("france2", 255),
          ("georgia", 268),
          ("germany", 276),
          ("greece", 300),
          ("guatemala", 320),
          ("honduras", 340),
          ("hongKong", 344),
          ("hungary", 348),
          ("iceland", 352),
          ("india", 356),
          ("indonesia", 360),
          ("iran", 364),
          ("iraq", 368),
          ("ireland", 372),
          ("israel", 376),
          ("italy", 380),
          ("jamaica", 388),
          ("japan", 392),
          ("japan1", 393),
          ("japan2", 394),
          ("japan3", 395),
          ("japan4", 396),
          ("japan5", 397),
          ("kazakhstan", 398),
          ("jordan", 400),
          ("kenya", 404),
          ("koreaNorth", 408),
          ("koreaRoc", 410),
          ("koreaRoc2", 411),
          ("kuwait", 414),
          ("lebanon", 422),
          ("latvia", 428),
          ("libya", 434),
          ("liechtenstein", 438),
          ("lithuania", 440),
          ("luxembourg", 442),
          ("macau", 446),
          ("malaysia", 458),
          ("mexico", 484),
          ("monaco", 492),
          ("morocco", 504),
          ("oman", 512),
          ("netherlands", 528),
          ("newZealand", 554),
          ("nicaragua", 558),
          ("norway", 578),
          ("pakistan", 586),
          ("panama", 591),
          ("paraguay", 600),
          ("peru", 604),
          ("philippines", 608),
          ("poland", 616),
          ("portugal", 620),
          ("puertoRico", 630),
          ("qatar", 634),
          ("romania", 642),
          ("russia", 643),
          ("saudiArabia", 682),
          ("singapore", 702),
          ("slovakia", 703),
          ("vietNam", 704),
          ("slovenia", 705),
          ("southAfrica", 710),
          ("zimbabwe", 716),
          ("spain", 724),
          ("sweden", 752),
          ("switzerland", 756),
          ("syria", 760),
          ("thailand", 764),
          ("trinidadYTobago", 780),
          ("uae", 784),
          ("tunisia", 788),
          ("turkey", 792),
          ("ukraine", 804),
          ("macedonia", 807),
          ("egypt", 818),
          ("unitedKingdom", 826),
          ("unitedStates", 840),
          ("uruguay", 858),
          ("uzbekistan", 860),
          ("venezuela", 862),
          ("yemen", 887))
    )



class LinkRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("rate64Kbps", 0),
          ("rate128Kbps", 1),
          ("rate256Kbps", 2),
          ("rate512Kbps", 3),
          ("rate1Mbps", 4),
          ("rate1dot5Mbps", 5),
          ("rate2Mbps", 6),
          ("rate2dot25Mbps", 7),
          ("rate3Mbps", 8),
          ("rate4Mbps", 9),
          ("rate4dot5Mbps", 10),
          ("rate5dot5Mbps", 11),
          ("rate6Mbps", 12),
          ("rate8Mbps", 13),
          ("rate9Mbps", 14),
          ("rateEth10Mbps", 15),
          ("rate11Mbps", 16),
          ("rate12Mbps", 17),
          ("rate16Mbps", 18),
          ("rate18Mbps", 19),
          ("rate24Mbps", 20),
          ("rate27Mbps", 21),
          ("rate32Mbps", 22),
          ("rate36Mbps", 23),
          ("rate48Mbps", 24),
          ("rate54Mbps", 25),
          ("rate64Mbps", 26),
          ("rateEth100Mbps", 27))
    )



class RadioDataRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("radioDataRateUnknown", 0),
          ("radioDataRateAuto", 1),
          ("radioDataRate1M", 2),
          ("radioDataRate2M", 3),
          ("radioDataRate5dot5M", 4),
          ("radioDataRate6M", 5),
          ("radioDataRate11M", 6),
          ("radioDataRate12M", 7),
          ("radioDataRate18M", 8),
          ("radioDataRate24M", 9),
          ("radioDataRate36M", 10),
          ("radioDataRate48M", 11),
          ("radioDataRate54M", 12),
          ("radioDataRate108M", 13))
    )



# MIB Managed Objects in the order of their OIDs

_Firetide_ObjectIdentity = ObjectIdentity
firetide = _Firetide_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835)
)
_FiretideNetwork_ObjectIdentity = ObjectIdentity
firetideNetwork = _FiretideNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1)
)
_NumMesh_Type = Integer32
_NumMesh_Object = MibScalar
numMesh = _NumMesh_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 1),
    _NumMesh_Type()
)
numMesh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numMesh.setStatus("current")
_MeshConfigTable_Object = MibTable
meshConfigTable = _MeshConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2)
)
if mibBuilder.loadTexts:
    meshConfigTable.setStatus("current")
_MeshConfigEntry_Object = MibTableRow
meshConfigEntry = _MeshConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1)
)
meshConfigEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
)
if mibBuilder.loadTexts:
    meshConfigEntry.setStatus("current")


class _MeshIndex_Type(Integer32):
    """Custom type meshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MeshIndex_Type.__name__ = "Integer32"
_MeshIndex_Object = MibTableColumn
meshIndex = _MeshIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 1),
    _MeshIndex_Type()
)
meshIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    meshIndex.setStatus("current")
_MeshName_Type = DisplayString
_MeshName_Object = MibTableColumn
meshName = _MeshName_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 2),
    _MeshName_Type()
)
meshName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshName.setStatus("current")
_MeshNmsIp_Type = IpAddress
_MeshNmsIp_Object = MibTableColumn
meshNmsIp = _MeshNmsIp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 3),
    _MeshNmsIp_Type()
)
meshNmsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshNmsIp.setStatus("current")
_MeshNmsIpMask_Type = IpAddress
_MeshNmsIpMask_Object = MibTableColumn
meshNmsIpMask = _MeshNmsIpMask_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 4),
    _MeshNmsIpMask_Type()
)
meshNmsIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshNmsIpMask.setStatus("current")
_MeshNmsDefaultGateway_Type = IpAddress
_MeshNmsDefaultGateway_Object = MibTableColumn
meshNmsDefaultGateway = _MeshNmsDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 5),
    _MeshNmsDefaultGateway_Type()
)
meshNmsDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshNmsDefaultGateway.setStatus("current")


class _MeshStatsCollectInterval_Type(Integer32):
    """Custom type meshStatsCollectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 9999),
    )


_MeshStatsCollectInterval_Type.__name__ = "Integer32"
_MeshStatsCollectInterval_Object = MibTableColumn
meshStatsCollectInterval = _MeshStatsCollectInterval_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 6),
    _MeshStatsCollectInterval_Type()
)
meshStatsCollectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshStatsCollectInterval.setStatus("current")
_MeshNumNodes_Type = Integer32
_MeshNumNodes_Object = MibTableColumn
meshNumNodes = _MeshNumNodes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 7),
    _MeshNumNodes_Type()
)
meshNumNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meshNumNodes.setStatus("current")
_MeshNumNodesDown_Type = Integer32
_MeshNumNodesDown_Object = MibTableColumn
meshNumNodesDown = _MeshNumNodesDown_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 8),
    _MeshNumNodesDown_Type()
)
meshNumNodesDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meshNumNodesDown.setStatus("current")


class _MeshNumVlans_Type(Integer32):
    """Custom type meshNumVlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MeshNumVlans_Type.__name__ = "Integer32"
_MeshNumVlans_Object = MibTableColumn
meshNumVlans = _MeshNumVlans_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 9),
    _MeshNumVlans_Type()
)
meshNumVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meshNumVlans.setStatus("current")


class _MeshGatewayGroupConfiguredBitMap_Type(Integer32):
    """Custom type meshGatewayGroupConfiguredBitMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MeshGatewayGroupConfiguredBitMap_Type.__name__ = "Integer32"
_MeshGatewayGroupConfiguredBitMap_Object = MibTableColumn
meshGatewayGroupConfiguredBitMap = _MeshGatewayGroupConfiguredBitMap_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 10),
    _MeshGatewayGroupConfiguredBitMap_Type()
)
meshGatewayGroupConfiguredBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meshGatewayGroupConfiguredBitMap.setStatus("current")


class _MeshMacListSize_Type(Integer32):
    """Custom type meshMacListSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MeshMacListSize_Type.__name__ = "Integer32"
_MeshMacListSize_Object = MibTableColumn
meshMacListSize = _MeshMacListSize_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 11),
    _MeshMacListSize_Type()
)
meshMacListSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meshMacListSize.setStatus("current")


class _MeshMacFilterType_Type(Integer32):
    """Custom type meshMacFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_MeshMacFilterType_Type.__name__ = "Integer32"
_MeshMacFilterType_Object = MibTableColumn
meshMacFilterType = _MeshMacFilterType_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 12),
    _MeshMacFilterType_Type()
)
meshMacFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshMacFilterType.setStatus("current")
_MeshNeighborTableSize_Type = Integer32
_MeshNeighborTableSize_Object = MibTableColumn
meshNeighborTableSize = _MeshNeighborTableSize_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 13),
    _MeshNeighborTableSize_Type()
)
meshNeighborTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meshNeighborTableSize.setStatus("current")
_RebootMesh_Type = TruthValue
_RebootMesh_Object = MibTableColumn
rebootMesh = _RebootMesh_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 14),
    _RebootMesh_Type()
)
rebootMesh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootMesh.setStatus("current")


class _MeshConfigApply_Type(Integer32):
    """Custom type meshConfigApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("configChangeApplied", 1),
          ("applyErrorTryAgain", 2),
          ("applyPending", 3),
          ("applyInProgress", 4),
          ("rollbackConfig", 5),
          ("applyToMesh", 6),
          ("forceApplyToMesh", 7))
    )


_MeshConfigApply_Type.__name__ = "Integer32"
_MeshConfigApply_Object = MibTableColumn
meshConfigApply = _MeshConfigApply_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 15),
    _MeshConfigApply_Type()
)
meshConfigApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshConfigApply.setStatus("current")


class _ApplyErrorString_Type(DisplayString):
    """Custom type applyErrorString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApplyErrorString_Type.__name__ = "DisplayString"
_ApplyErrorString_Object = MibTableColumn
applyErrorString = _ApplyErrorString_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 16),
    _ApplyErrorString_Type()
)
applyErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applyErrorString.setStatus("current")


class _NewMeshIndex_Type(Integer32):
    """Custom type newMeshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NewMeshIndex_Type.__name__ = "Integer32"
_NewMeshIndex_Object = MibTableColumn
newMeshIndex = _NewMeshIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 17),
    _NewMeshIndex_Type()
)
newMeshIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newMeshIndex.setStatus("current")
_VerifyMeshwideConfig_Type = VerifyOperation
_VerifyMeshwideConfig_Object = MibTableColumn
verifyMeshwideConfig = _VerifyMeshwideConfig_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 18),
    _VerifyMeshwideConfig_Type()
)
verifyMeshwideConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    verifyMeshwideConfig.setStatus("current")
_MeshConfigComparison_Type = DisplayString
_MeshConfigComparison_Object = MibTableColumn
meshConfigComparison = _MeshConfigComparison_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 19),
    _MeshConfigComparison_Type()
)
meshConfigComparison.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meshConfigComparison.setStatus("current")
_VerifyRadioConfig_Type = VerifyOperation
_VerifyRadioConfig_Object = MibTableColumn
verifyRadioConfig = _VerifyRadioConfig_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 20),
    _VerifyRadioConfig_Type()
)
verifyRadioConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    verifyRadioConfig.setStatus("current")
_RadioConfigComparison_Type = DisplayString
_RadioConfigComparison_Object = MibTableColumn
radioConfigComparison = _RadioConfigComparison_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 21),
    _RadioConfigComparison_Type()
)
radioConfigComparison.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioConfigComparison.setStatus("current")


class _UpgradeMeshSoftware_Type(Integer32):
    """Custom type upgradeMeshSoftware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("upgradeAll", 1),
          ("upgradeForce", 2),
          ("upgradeFailed", 3),
          ("upgradeInProgress", 4),
          ("upgradeCompleted", 5),
          ("upgradeSelective", 6),
          ("upgradeCancel", 7))
    )


_UpgradeMeshSoftware_Type.__name__ = "Integer32"
_UpgradeMeshSoftware_Object = MibTableColumn
upgradeMeshSoftware = _UpgradeMeshSoftware_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 22),
    _UpgradeMeshSoftware_Type()
)
upgradeMeshSoftware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeMeshSoftware.setStatus("current")
_UpgradeSoftwarePath_Type = DisplayString
_UpgradeSoftwarePath_Object = MibTableColumn
upgradeSoftwarePath = _UpgradeSoftwarePath_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 23),
    _UpgradeSoftwarePath_Type()
)
upgradeSoftwarePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeSoftwarePath.setStatus("current")


class _UpgradeSoftwareCompletion_Type(Integer32):
    """Custom type upgradeSoftwareCompletion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpgradeSoftwareCompletion_Type.__name__ = "Integer32"
_UpgradeSoftwareCompletion_Object = MibTableColumn
upgradeSoftwareCompletion = _UpgradeSoftwareCompletion_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 24),
    _UpgradeSoftwareCompletion_Type()
)
upgradeSoftwareCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeSoftwareCompletion.setStatus("current")
_ImportMeshwideConfig_Type = NetworkOperation
_ImportMeshwideConfig_Object = MibTableColumn
importMeshwideConfig = _ImportMeshwideConfig_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 25),
    _ImportMeshwideConfig_Type()
)
importMeshwideConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    importMeshwideConfig.setStatus("current")
_ExportMeshwideConfig_Type = NetworkOperation
_ExportMeshwideConfig_Object = MibTableColumn
exportMeshwideConfig = _ExportMeshwideConfig_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 26),
    _ExportMeshwideConfig_Type()
)
exportMeshwideConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exportMeshwideConfig.setStatus("current")
_MeshConfigUpdateNodeIndex_Type = Integer32
_MeshConfigUpdateNodeIndex_Object = MibTableColumn
meshConfigUpdateNodeIndex = _MeshConfigUpdateNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 27),
    _MeshConfigUpdateNodeIndex_Type()
)
meshConfigUpdateNodeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshConfigUpdateNodeIndex.setStatus("current")
_MeshConfigUpdatePath_Type = DisplayString
_MeshConfigUpdatePath_Object = MibTableColumn
meshConfigUpdatePath = _MeshConfigUpdatePath_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 28),
    _MeshConfigUpdatePath_Type()
)
meshConfigUpdatePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshConfigUpdatePath.setStatus("current")
_MeshConfigSavedPasswd_Type = DisplayString
_MeshConfigSavedPasswd_Object = MibTableColumn
meshConfigSavedPasswd = _MeshConfigSavedPasswd_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 29),
    _MeshConfigSavedPasswd_Type()
)
meshConfigSavedPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshConfigSavedPasswd.setStatus("current")
_MeshConfigGwGrpNameToApply_Type = DisplayString
_MeshConfigGwGrpNameToApply_Object = MibTableColumn
meshConfigGwGrpNameToApply = _MeshConfigGwGrpNameToApply_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 30),
    _MeshConfigGwGrpNameToApply_Type()
)
meshConfigGwGrpNameToApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshConfigGwGrpNameToApply.setStatus("current")
_MeshConfigGwPrimary_Type = TruthValue
_MeshConfigGwPrimary_Object = MibTableColumn
meshConfigGwPrimary = _MeshConfigGwPrimary_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 31),
    _MeshConfigGwPrimary_Type()
)
meshConfigGwPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshConfigGwPrimary.setStatus("current")
_MeshConfigSavedUserName_Type = DisplayString
_MeshConfigSavedUserName_Object = MibTableColumn
meshConfigSavedUserName = _MeshConfigSavedUserName_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 32),
    _MeshConfigSavedUserName_Type()
)
meshConfigSavedUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshConfigSavedUserName.setStatus("current")
_MeshwidePriorityEnable_Type = TruthValue
_MeshwidePriorityEnable_Object = MibTableColumn
meshwidePriorityEnable = _MeshwidePriorityEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 33),
    _MeshwidePriorityEnable_Type()
)
meshwidePriorityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshwidePriorityEnable.setStatus("current")
_MeshwideCongestionControlEnable_Type = TruthValue
_MeshwideCongestionControlEnable_Object = MibTableColumn
meshwideCongestionControlEnable = _MeshwideCongestionControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 34),
    _MeshwideCongestionControlEnable_Type()
)
meshwideCongestionControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshwideCongestionControlEnable.setStatus("current")
_MeshReservedMacEnable_Type = TruthValue
_MeshReservedMacEnable_Object = MibTableColumn
meshReservedMacEnable = _MeshReservedMacEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 35),
    _MeshReservedMacEnable_Type()
)
meshReservedMacEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshReservedMacEnable.setStatus("current")
_MeshConfigEntryStatus_Type = RowStatus
_MeshConfigEntryStatus_Object = MibTableColumn
meshConfigEntryStatus = _MeshConfigEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 2, 1, 50),
    _MeshConfigEntryStatus_Type()
)
meshConfigEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    meshConfigEntryStatus.setStatus("current")
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 3)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 3, 1)
)
vlanEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "nodeIndex"),
    (0, "FIRETIDE-MESH-MIB", "portIndex"),
    (0, "FIRETIDE-MESH-MIB", "vlanNo"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")


class _VlanNo_Type(Integer32):
    """Custom type vlanNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4095),
    )


_VlanNo_Type.__name__ = "Integer32"
_VlanNo_Object = MibTableColumn
vlanNo = _VlanNo_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 3, 1, 1),
    _VlanNo_Type()
)
vlanNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanNo.setStatus("current")
_VlanTagged_Type = TruthValue
_VlanTagged_Object = MibTableColumn
vlanTagged = _VlanTagged_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 3, 1, 2),
    _VlanTagged_Type()
)
vlanTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTagged.setStatus("current")
_VlanStatus_Type = RowStatus
_VlanStatus_Object = MibTableColumn
vlanStatus = _VlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 3, 1, 10),
    _VlanStatus_Type()
)
vlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanStatus.setStatus("current")
_VlanTrunkTable_Object = MibTable
vlanTrunkTable = _VlanTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 4)
)
if mibBuilder.loadTexts:
    vlanTrunkTable.setStatus("current")
_VlanTrunkEntry_Object = MibTableRow
vlanTrunkEntry = _VlanTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 4, 1)
)
vlanTrunkEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "nodeIndex"),
)
if mibBuilder.loadTexts:
    vlanTrunkEntry.setStatus("current")
_VlanTrunkOnPort3_Type = TruthValue
_VlanTrunkOnPort3_Object = MibTableColumn
vlanTrunkOnPort3 = _VlanTrunkOnPort3_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 4, 1, 1),
    _VlanTrunkOnPort3_Type()
)
vlanTrunkOnPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkOnPort3.setStatus("current")
_VlanTrunkOnPort4_Type = TruthValue
_VlanTrunkOnPort4_Object = MibTableColumn
vlanTrunkOnPort4 = _VlanTrunkOnPort4_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 4, 1, 2),
    _VlanTrunkOnPort4_Type()
)
vlanTrunkOnPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkOnPort4.setStatus("current")


class _VlanTrunkMgmtVlanIdOnPort3_Type(Integer32):
    """Custom type vlanTrunkMgmtVlanIdOnPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_VlanTrunkMgmtVlanIdOnPort3_Type.__name__ = "Integer32"
_VlanTrunkMgmtVlanIdOnPort3_Object = MibTableColumn
vlanTrunkMgmtVlanIdOnPort3 = _VlanTrunkMgmtVlanIdOnPort3_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 4, 1, 3),
    _VlanTrunkMgmtVlanIdOnPort3_Type()
)
vlanTrunkMgmtVlanIdOnPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkMgmtVlanIdOnPort3.setStatus("current")


class _VlanTrunkMgmtVlanIdOnPort4_Type(Integer32):
    """Custom type vlanTrunkMgmtVlanIdOnPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_VlanTrunkMgmtVlanIdOnPort4_Type.__name__ = "Integer32"
_VlanTrunkMgmtVlanIdOnPort4_Object = MibTableColumn
vlanTrunkMgmtVlanIdOnPort4 = _VlanTrunkMgmtVlanIdOnPort4_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 4, 1, 4),
    _VlanTrunkMgmtVlanIdOnPort4_Type()
)
vlanTrunkMgmtVlanIdOnPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkMgmtVlanIdOnPort4.setStatus("current")
_VlanTrunkStatus_Type = RowStatus
_VlanTrunkStatus_Object = MibTableColumn
vlanTrunkStatus = _VlanTrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 4, 1, 10),
    _VlanTrunkStatus_Type()
)
vlanTrunkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkStatus.setStatus("current")
_MacListTable_Object = MibTable
macListTable = _MacListTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 5)
)
if mibBuilder.loadTexts:
    macListTable.setStatus("current")
_MacListEntry_Object = MibTableRow
macListEntry = _MacListEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 5, 1)
)
macListEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "macFilterMacAddress"),
)
if mibBuilder.loadTexts:
    macListEntry.setStatus("current")
_MacFilterMacAddress_Type = OctetString
_MacFilterMacAddress_Object = MibTableColumn
macFilterMacAddress = _MacFilterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 5, 1, 1),
    _MacFilterMacAddress_Type()
)
macFilterMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macFilterMacAddress.setStatus("current")
_MacFilterEntryStatus_Type = RowStatus
_MacFilterEntryStatus_Object = MibTableColumn
macFilterEntryStatus = _MacFilterEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 5, 1, 10),
    _MacFilterEntryStatus_Type()
)
macFilterEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macFilterEntryStatus.setStatus("current")
_BridgeGroupTable_Object = MibTable
bridgeGroupTable = _BridgeGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 6)
)
if mibBuilder.loadTexts:
    bridgeGroupTable.setStatus("current")
_BridgeGroupEntry_Object = MibTableRow
bridgeGroupEntry = _BridgeGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 6, 1)
)
bridgeGroupEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "bridgeGroupNo"),
)
if mibBuilder.loadTexts:
    bridgeGroupEntry.setStatus("current")


class _BridgeGroupNo_Type(Integer32):
    """Custom type bridgeGroupNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BridgeGroupNo_Type.__name__ = "Integer32"
_BridgeGroupNo_Object = MibTableColumn
bridgeGroupNo = _BridgeGroupNo_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 6, 1, 1),
    _BridgeGroupNo_Type()
)
bridgeGroupNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeGroupNo.setStatus("current")


class _BridgeGroupName_Type(DisplayString):
    """Custom type bridgeGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BridgeGroupName_Type.__name__ = "DisplayString"
_BridgeGroupName_Object = MibTableColumn
bridgeGroupName = _BridgeGroupName_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 6, 1, 2),
    _BridgeGroupName_Type()
)
bridgeGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupName.setStatus("current")


class _BridgeGroupRemoteMeshIndex_Type(Integer32):
    """Custom type bridgeGroupRemoteMeshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BridgeGroupRemoteMeshIndex_Type.__name__ = "Integer32"
_BridgeGroupRemoteMeshIndex_Object = MibTableColumn
bridgeGroupRemoteMeshIndex = _BridgeGroupRemoteMeshIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 6, 1, 3),
    _BridgeGroupRemoteMeshIndex_Type()
)
bridgeGroupRemoteMeshIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupRemoteMeshIndex.setStatus("current")


class _BridgeGroupNumIfs_Type(Integer32):
    """Custom type bridgeGroupNumIfs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BridgeGroupNumIfs_Type.__name__ = "Integer32"
_BridgeGroupNumIfs_Object = MibTableColumn
bridgeGroupNumIfs = _BridgeGroupNumIfs_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 6, 1, 4),
    _BridgeGroupNumIfs_Type()
)
bridgeGroupNumIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeGroupNumIfs.setStatus("current")


class _BridgeGroupAesFlag_Type(Integer32):
    """Custom type bridgeGroupAesFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("key128bit", 2),
          ("key256bit", 3))
    )


_BridgeGroupAesFlag_Type.__name__ = "Integer32"
_BridgeGroupAesFlag_Object = MibTableColumn
bridgeGroupAesFlag = _BridgeGroupAesFlag_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 6, 1, 5),
    _BridgeGroupAesFlag_Type()
)
bridgeGroupAesFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupAesFlag.setStatus("current")


class _BridgeGroupAesKey_Type(OctetString):
    """Custom type bridgeGroupAesKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
        ValueSizeConstraint(64, 64),
    )


_BridgeGroupAesKey_Type.__name__ = "OctetString"
_BridgeGroupAesKey_Object = MibTableColumn
bridgeGroupAesKey = _BridgeGroupAesKey_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 6, 1, 6),
    _BridgeGroupAesKey_Type()
)
bridgeGroupAesKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupAesKey.setStatus("current")
_BridgeGroupStatus_Type = RowStatus
_BridgeGroupStatus_Object = MibTableColumn
bridgeGroupStatus = _BridgeGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 6, 1, 10),
    _BridgeGroupStatus_Type()
)
bridgeGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeGroupStatus.setStatus("current")
_BridgeGroupIfTable_Object = MibTable
bridgeGroupIfTable = _BridgeGroupIfTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 7)
)
if mibBuilder.loadTexts:
    bridgeGroupIfTable.setStatus("current")
_BridgeGroupIfEntry_Object = MibTableRow
bridgeGroupIfEntry = _BridgeGroupIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 7, 1)
)
bridgeGroupIfEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "bridgeGroupNo"),
    (0, "FIRETIDE-MESH-MIB", "bridgeGroupIfNo"),
)
if mibBuilder.loadTexts:
    bridgeGroupIfEntry.setStatus("current")


class _BridgeGroupIfNo_Type(Integer32):
    """Custom type bridgeGroupIfNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BridgeGroupIfNo_Type.__name__ = "Integer32"
_BridgeGroupIfNo_Object = MibTableColumn
bridgeGroupIfNo = _BridgeGroupIfNo_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 7, 1, 1),
    _BridgeGroupIfNo_Type()
)
bridgeGroupIfNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bridgeGroupIfNo.setStatus("current")
_BridgeGroupIfNodeIndex_Type = Integer32
_BridgeGroupIfNodeIndex_Object = MibTableColumn
bridgeGroupIfNodeIndex = _BridgeGroupIfNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 7, 1, 2),
    _BridgeGroupIfNodeIndex_Type()
)
bridgeGroupIfNodeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupIfNodeIndex.setStatus("current")
_BridgeGroupIfIp_Type = IpAddress
_BridgeGroupIfIp_Object = MibTableColumn
bridgeGroupIfIp = _BridgeGroupIfIp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 7, 1, 3),
    _BridgeGroupIfIp_Type()
)
bridgeGroupIfIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupIfIp.setStatus("current")
_BridgeGroupIfIpMask_Type = IpAddress
_BridgeGroupIfIpMask_Object = MibTableColumn
bridgeGroupIfIpMask = _BridgeGroupIfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 7, 1, 4),
    _BridgeGroupIfIpMask_Type()
)
bridgeGroupIfIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupIfIpMask.setStatus("current")
_BridgeGroupIfDefaultGateway_Type = IpAddress
_BridgeGroupIfDefaultGateway_Object = MibTableColumn
bridgeGroupIfDefaultGateway = _BridgeGroupIfDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 7, 1, 5),
    _BridgeGroupIfDefaultGateway_Type()
)
bridgeGroupIfDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupIfDefaultGateway.setStatus("current")
_BridgeGroupIfRemoteIp_Type = IpAddress
_BridgeGroupIfRemoteIp_Object = MibTableColumn
bridgeGroupIfRemoteIp = _BridgeGroupIfRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 7, 1, 6),
    _BridgeGroupIfRemoteIp_Type()
)
bridgeGroupIfRemoteIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupIfRemoteIp.setStatus("current")


class _BridgeGroupIfPortIndex_Type(Integer32):
    """Custom type bridgeGroupIfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BridgeGroupIfPortIndex_Type.__name__ = "Integer32"
_BridgeGroupIfPortIndex_Object = MibTableColumn
bridgeGroupIfPortIndex = _BridgeGroupIfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 7, 1, 7),
    _BridgeGroupIfPortIndex_Type()
)
bridgeGroupIfPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupIfPortIndex.setStatus("current")
_BridgeGroupIfStatus_Type = RowStatus
_BridgeGroupIfStatus_Object = MibTableColumn
bridgeGroupIfStatus = _BridgeGroupIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 7, 1, 20),
    _BridgeGroupIfStatus_Type()
)
bridgeGroupIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeGroupIfStatus.setStatus("current")
_GatewayServerTable_Object = MibTable
gatewayServerTable = _GatewayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 8)
)
if mibBuilder.loadTexts:
    gatewayServerTable.setStatus("current")
_GatewayServerEntry_Object = MibTableRow
gatewayServerEntry = _GatewayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 8, 1)
)
gatewayServerEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "gatewayServerNo"),
)
if mibBuilder.loadTexts:
    gatewayServerEntry.setStatus("current")


class _GatewayServerNo_Type(Integer32):
    """Custom type gatewayServerNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_GatewayServerNo_Type.__name__ = "Integer32"
_GatewayServerNo_Object = MibTableColumn
gatewayServerNo = _GatewayServerNo_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 8, 1, 1),
    _GatewayServerNo_Type()
)
gatewayServerNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gatewayServerNo.setStatus("current")


class _GatewayServerName_Type(DisplayString):
    """Custom type gatewayServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GatewayServerName_Type.__name__ = "DisplayString"
_GatewayServerName_Object = MibTableColumn
gatewayServerName = _GatewayServerName_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 8, 1, 2),
    _GatewayServerName_Type()
)
gatewayServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayServerName.setStatus("current")
_GatewayServerPriNode_Type = Integer32
_GatewayServerPriNode_Object = MibTableColumn
gatewayServerPriNode = _GatewayServerPriNode_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 8, 1, 3),
    _GatewayServerPriNode_Type()
)
gatewayServerPriNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayServerPriNode.setStatus("current")


class _GatewayServerNumIfs_Type(Integer32):
    """Custom type gatewayServerNumIfs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_GatewayServerNumIfs_Type.__name__ = "Integer32"
_GatewayServerNumIfs_Object = MibTableColumn
gatewayServerNumIfs = _GatewayServerNumIfs_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 8, 1, 4),
    _GatewayServerNumIfs_Type()
)
gatewayServerNumIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayServerNumIfs.setStatus("current")


class _GatewayServerAesFlag_Type(Integer32):
    """Custom type gatewayServerAesFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("key128bit", 2),
          ("key256bit", 3))
    )


_GatewayServerAesFlag_Type.__name__ = "Integer32"
_GatewayServerAesFlag_Object = MibTableColumn
gatewayServerAesFlag = _GatewayServerAesFlag_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 8, 1, 5),
    _GatewayServerAesFlag_Type()
)
gatewayServerAesFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayServerAesFlag.setStatus("current")


class _GatewayServerAesKey_Type(OctetString):
    """Custom type gatewayServerAesKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
        ValueSizeConstraint(64, 64),
    )


_GatewayServerAesKey_Type.__name__ = "OctetString"
_GatewayServerAesKey_Object = MibTableColumn
gatewayServerAesKey = _GatewayServerAesKey_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 8, 1, 6),
    _GatewayServerAesKey_Type()
)
gatewayServerAesKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayServerAesKey.setStatus("current")
_GatewayServerSrvPriIfIp_Type = IpAddress
_GatewayServerSrvPriIfIp_Object = MibTableColumn
gatewayServerSrvPriIfIp = _GatewayServerSrvPriIfIp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 8, 1, 7),
    _GatewayServerSrvPriIfIp_Type()
)
gatewayServerSrvPriIfIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayServerSrvPriIfIp.setStatus("current")
_GatewayServerSrvIfIpMask_Type = IpAddress
_GatewayServerSrvIfIpMask_Object = MibTableColumn
gatewayServerSrvIfIpMask = _GatewayServerSrvIfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 8, 1, 8),
    _GatewayServerSrvIfIpMask_Type()
)
gatewayServerSrvIfIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayServerSrvIfIpMask.setStatus("current")
_GatewayServerSrvIfDefaultGateway_Type = IpAddress
_GatewayServerSrvIfDefaultGateway_Object = MibTableColumn
gatewayServerSrvIfDefaultGateway = _GatewayServerSrvIfDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 8, 1, 9),
    _GatewayServerSrvIfDefaultGateway_Type()
)
gatewayServerSrvIfDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayServerSrvIfDefaultGateway.setStatus("current")


class _GatewayServerSrvPortIndex_Type(Integer32):
    """Custom type gatewayServerSrvPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_GatewayServerSrvPortIndex_Type.__name__ = "Integer32"
_GatewayServerSrvPortIndex_Object = MibTableColumn
gatewayServerSrvPortIndex = _GatewayServerSrvPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 8, 1, 10),
    _GatewayServerSrvPortIndex_Type()
)
gatewayServerSrvPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayServerSrvPortIndex.setStatus("current")
_GatewayServerSrvRedundant_Type = TruthValue
_GatewayServerSrvRedundant_Object = MibTableColumn
gatewayServerSrvRedundant = _GatewayServerSrvRedundant_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 8, 1, 11),
    _GatewayServerSrvRedundant_Type()
)
gatewayServerSrvRedundant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayServerSrvRedundant.setStatus("current")
_GatewayServerSecNode_Type = Integer32
_GatewayServerSecNode_Object = MibTableColumn
gatewayServerSecNode = _GatewayServerSecNode_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 8, 1, 12),
    _GatewayServerSecNode_Type()
)
gatewayServerSecNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayServerSecNode.setStatus("current")
_GatewayServerSrvSecIfIp_Type = IpAddress
_GatewayServerSrvSecIfIp_Object = MibTableColumn
gatewayServerSrvSecIfIp = _GatewayServerSrvSecIfIp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 8, 1, 13),
    _GatewayServerSrvSecIfIp_Type()
)
gatewayServerSrvSecIfIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayServerSrvSecIfIp.setStatus("current")
_GatewayServerStatus_Type = RowStatus
_GatewayServerStatus_Object = MibTableColumn
gatewayServerStatus = _GatewayServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 8, 1, 20),
    _GatewayServerStatus_Type()
)
gatewayServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gatewayServerStatus.setStatus("current")
_GatewayServerIfTable_Object = MibTable
gatewayServerIfTable = _GatewayServerIfTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 9)
)
if mibBuilder.loadTexts:
    gatewayServerIfTable.setStatus("current")
_GatewayServerIfEntry_Object = MibTableRow
gatewayServerIfEntry = _GatewayServerIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 9, 1)
)
gatewayServerIfEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "gatewayServerNo"),
    (0, "FIRETIDE-MESH-MIB", "gatewayServerIfNo"),
)
if mibBuilder.loadTexts:
    gatewayServerIfEntry.setStatus("current")


class _GatewayServerIfNo_Type(Integer32):
    """Custom type gatewayServerIfNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_GatewayServerIfNo_Type.__name__ = "Integer32"
_GatewayServerIfNo_Object = MibTableColumn
gatewayServerIfNo = _GatewayServerIfNo_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 9, 1, 1),
    _GatewayServerIfNo_Type()
)
gatewayServerIfNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gatewayServerIfNo.setStatus("current")
_GatewayServerIfNodeIndex_Type = Integer32
_GatewayServerIfNodeIndex_Object = MibTableColumn
gatewayServerIfNodeIndex = _GatewayServerIfNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 9, 1, 2),
    _GatewayServerIfNodeIndex_Type()
)
gatewayServerIfNodeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayServerIfNodeIndex.setStatus("current")


class _GatewayServerIfPortIndex_Type(Integer32):
    """Custom type gatewayServerIfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_GatewayServerIfPortIndex_Type.__name__ = "Integer32"
_GatewayServerIfPortIndex_Object = MibTableColumn
gatewayServerIfPortIndex = _GatewayServerIfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 9, 1, 3),
    _GatewayServerIfPortIndex_Type()
)
gatewayServerIfPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayServerIfPortIndex.setStatus("current")
_GatewayServerIfIp_Type = IpAddress
_GatewayServerIfIp_Object = MibTableColumn
gatewayServerIfIp = _GatewayServerIfIp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 9, 1, 4),
    _GatewayServerIfIp_Type()
)
gatewayServerIfIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayServerIfIp.setStatus("current")
_GatewayServerIfIpMask_Type = IpAddress
_GatewayServerIfIpMask_Object = MibTableColumn
gatewayServerIfIpMask = _GatewayServerIfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 9, 1, 5),
    _GatewayServerIfIpMask_Type()
)
gatewayServerIfIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayServerIfIpMask.setStatus("current")
_GatewayServerIfDefaultGateway_Type = IpAddress
_GatewayServerIfDefaultGateway_Object = MibTableColumn
gatewayServerIfDefaultGateway = _GatewayServerIfDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 9, 1, 6),
    _GatewayServerIfDefaultGateway_Type()
)
gatewayServerIfDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayServerIfDefaultGateway.setStatus("current")
_GatewayServerIfLinkRate_Type = LinkRate
_GatewayServerIfLinkRate_Object = MibTableColumn
gatewayServerIfLinkRate = _GatewayServerIfLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 9, 1, 7),
    _GatewayServerIfLinkRate_Type()
)
gatewayServerIfLinkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayServerIfLinkRate.setStatus("current")
_GatewayServerSrvLogicalIndex_Type = Integer32
_GatewayServerSrvLogicalIndex_Object = MibTableColumn
gatewayServerSrvLogicalIndex = _GatewayServerSrvLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 9, 1, 8),
    _GatewayServerSrvLogicalIndex_Type()
)
gatewayServerSrvLogicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayServerSrvLogicalIndex.setStatus("current")
_GatewayServerIfPriLogicalIndex_Type = Integer32
_GatewayServerIfPriLogicalIndex_Object = MibTableColumn
gatewayServerIfPriLogicalIndex = _GatewayServerIfPriLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 9, 1, 9),
    _GatewayServerIfPriLogicalIndex_Type()
)
gatewayServerIfPriLogicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayServerIfPriLogicalIndex.setStatus("current")
_GatewayServerIfSecLogicalIndex_Type = Integer32
_GatewayServerIfSecLogicalIndex_Object = MibTableColumn
gatewayServerIfSecLogicalIndex = _GatewayServerIfSecLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 9, 1, 10),
    _GatewayServerIfSecLogicalIndex_Type()
)
gatewayServerIfSecLogicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayServerIfSecLogicalIndex.setStatus("current")
_GatewayServerIfStatus_Type = RowStatus
_GatewayServerIfStatus_Object = MibTableColumn
gatewayServerIfStatus = _GatewayServerIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 9, 1, 20),
    _GatewayServerIfStatus_Type()
)
gatewayServerIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gatewayServerIfStatus.setStatus("current")
_EthernetDirectTable_Object = MibTable
ethernetDirectTable = _EthernetDirectTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 10)
)
if mibBuilder.loadTexts:
    ethernetDirectTable.setStatus("current")
_EthernetDirectEntry_Object = MibTableRow
ethernetDirectEntry = _EthernetDirectEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 10, 1)
)
ethernetDirectEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "nodeIndex"),
    (0, "FIRETIDE-MESH-MIB", "ethernetRemoteIp"),
)
if mibBuilder.loadTexts:
    ethernetDirectEntry.setStatus("current")
_EthernetRemoteIp_Type = IpAddress
_EthernetRemoteIp_Object = MibTableColumn
ethernetRemoteIp = _EthernetRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 10, 1, 1),
    _EthernetRemoteIp_Type()
)
ethernetRemoteIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethernetRemoteIp.setStatus("current")
_EthernetLocalIp_Type = IpAddress
_EthernetLocalIp_Object = MibTableColumn
ethernetLocalIp = _EthernetLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 10, 1, 2),
    _EthernetLocalIp_Type()
)
ethernetLocalIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetLocalIp.setStatus("current")
_EthernetTunnelName_Type = DisplayString
_EthernetTunnelName_Object = MibTableColumn
ethernetTunnelName = _EthernetTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 10, 1, 3),
    _EthernetTunnelName_Type()
)
ethernetTunnelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetTunnelName.setStatus("current")


class _EthernetPortIndex_Type(Integer32):
    """Custom type ethernetPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EthernetPortIndex_Type.__name__ = "Integer32"
_EthernetPortIndex_Object = MibTableColumn
ethernetPortIndex = _EthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 10, 1, 4),
    _EthernetPortIndex_Type()
)
ethernetPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetPortIndex.setStatus("current")
_EthernetLocalIpMask_Type = IpAddress
_EthernetLocalIpMask_Object = MibTableColumn
ethernetLocalIpMask = _EthernetLocalIpMask_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 10, 1, 5),
    _EthernetLocalIpMask_Type()
)
ethernetLocalIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetLocalIpMask.setStatus("current")
_EthernetDefaultGateway_Type = IpAddress
_EthernetDefaultGateway_Object = MibTableColumn
ethernetDefaultGateway = _EthernetDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 10, 1, 6),
    _EthernetDefaultGateway_Type()
)
ethernetDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetDefaultGateway.setStatus("current")


class _EthernetTunnelAesFlag_Type(Integer32):
    """Custom type ethernetTunnelAesFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("key128bit", 2),
          ("key256bit", 3))
    )


_EthernetTunnelAesFlag_Type.__name__ = "Integer32"
_EthernetTunnelAesFlag_Object = MibTableColumn
ethernetTunnelAesFlag = _EthernetTunnelAesFlag_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 10, 1, 7),
    _EthernetTunnelAesFlag_Type()
)
ethernetTunnelAesFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetTunnelAesFlag.setStatus("current")


class _EthernetTunnelAesKey_Type(OctetString):
    """Custom type ethernetTunnelAesKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
        ValueSizeConstraint(64, 64),
    )


_EthernetTunnelAesKey_Type.__name__ = "OctetString"
_EthernetTunnelAesKey_Object = MibTableColumn
ethernetTunnelAesKey = _EthernetTunnelAesKey_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 10, 1, 8),
    _EthernetTunnelAesKey_Type()
)
ethernetTunnelAesKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetTunnelAesKey.setStatus("current")
_EthernetLinkRate_Type = LinkRate
_EthernetLinkRate_Object = MibTableColumn
ethernetLinkRate = _EthernetLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 10, 1, 9),
    _EthernetLinkRate_Type()
)
ethernetLinkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetLinkRate.setStatus("current")
_EthernetLinkLogicalIndex_Type = Integer32
_EthernetLinkLogicalIndex_Object = MibTableColumn
ethernetLinkLogicalIndex = _EthernetLinkLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 10, 1, 10),
    _EthernetLinkLogicalIndex_Type()
)
ethernetLinkLogicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetLinkLogicalIndex.setStatus("current")
_EthernetDirectEntryStatus_Type = RowStatus
_EthernetDirectEntryStatus_Object = MibTableColumn
ethernetDirectEntryStatus = _EthernetDirectEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 10, 1, 20),
    _EthernetDirectEntryStatus_Type()
)
ethernetDirectEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethernetDirectEntryStatus.setStatus("current")
_MulticastGroupTable_Object = MibTable
multicastGroupTable = _MulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 11)
)
if mibBuilder.loadTexts:
    multicastGroupTable.setStatus("current")
_MulticastGroupEntry_Object = MibTableRow
multicastGroupEntry = _MulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 11, 1)
)
multicastGroupEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "multicastIp"),
    (0, "FIRETIDE-MESH-MIB", "multicastEntryNodeIndex"),
)
if mibBuilder.loadTexts:
    multicastGroupEntry.setStatus("current")
_MulticastIp_Type = IpAddress
_MulticastIp_Object = MibTableColumn
multicastIp = _MulticastIp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 11, 1, 1),
    _MulticastIp_Type()
)
multicastIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    multicastIp.setStatus("current")
_MulticastEntryNodeIndex_Type = Integer32
_MulticastEntryNodeIndex_Object = MibTableColumn
multicastEntryNodeIndex = _MulticastEntryNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 11, 1, 2),
    _MulticastEntryNodeIndex_Type()
)
multicastEntryNodeIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    multicastEntryNodeIndex.setStatus("current")
_MulticastGroupEntryStatus_Type = RowStatus
_MulticastGroupEntryStatus_Object = MibTableColumn
multicastGroupEntryStatus = _MulticastGroupEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 1, 11, 1, 10),
    _MulticastGroupEntryStatus_Type()
)
multicastGroupEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastGroupEntryStatus.setStatus("current")
_FiretideNode_ObjectIdentity = ObjectIdentity
firetideNode = _FiretideNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2)
)
_NodeTable_Object = MibTable
nodeTable = _NodeTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nodeTable.setStatus("current")
_NodeEntry_Object = MibTableRow
nodeEntry = _NodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1)
)
nodeEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "nodeIndex"),
)
if mibBuilder.loadTexts:
    nodeEntry.setStatus("current")
_NodeIndex_Type = Integer32
_NodeIndex_Object = MibTableColumn
nodeIndex = _NodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 1),
    _NodeIndex_Type()
)
nodeIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nodeIndex.setStatus("current")


class _NodeDisplayName_Type(DisplayString):
    """Custom type nodeDisplayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NodeDisplayName_Type.__name__ = "DisplayString"
_NodeDisplayName_Object = MibTableColumn
nodeDisplayName = _NodeDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 2),
    _NodeDisplayName_Type()
)
nodeDisplayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeDisplayName.setStatus("current")
_NodeModelNo_Type = DisplayString
_NodeModelNo_Object = MibTableColumn
nodeModelNo = _NodeModelNo_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 3),
    _NodeModelNo_Type()
)
nodeModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeModelNo.setStatus("current")


class _NodeSubId_Type(Integer32):
    """Custom type nodeSubId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodeDefault", 1),
          ("nodeUsa4g9", 2))
    )


_NodeSubId_Type.__name__ = "Integer32"
_NodeSubId_Object = MibTableColumn
nodeSubId = _NodeSubId_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 4),
    _NodeSubId_Type()
)
nodeSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSubId.setStatus("current")


class _NodeLocationString_Type(DisplayString):
    """Custom type nodeLocationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_NodeLocationString_Type.__name__ = "DisplayString"
_NodeLocationString_Object = MibTableColumn
nodeLocationString = _NodeLocationString_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 5),
    _NodeLocationString_Type()
)
nodeLocationString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeLocationString.setStatus("current")
_NodeLocationX_Type = Integer32
_NodeLocationX_Object = MibTableColumn
nodeLocationX = _NodeLocationX_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 6),
    _NodeLocationX_Type()
)
nodeLocationX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeLocationX.setStatus("current")
_NodeLocationY_Type = Integer32
_NodeLocationY_Object = MibTableColumn
nodeLocationY = _NodeLocationY_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 7),
    _NodeLocationY_Type()
)
nodeLocationY.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeLocationY.setStatus("current")
_NodeLocationZ_Type = Integer32
_NodeLocationZ_Object = MibTableColumn
nodeLocationZ = _NodeLocationZ_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 8),
    _NodeLocationZ_Type()
)
nodeLocationZ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeLocationZ.setStatus("current")


class _NodeSerialNo_Type(DisplayString):
    """Custom type nodeSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_NodeSerialNo_Type.__name__ = "DisplayString"
_NodeSerialNo_Object = MibTableColumn
nodeSerialNo = _NodeSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 9),
    _NodeSerialNo_Type()
)
nodeSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSerialNo.setStatus("current")
_NodeSoftwareVer_Type = DisplayString
_NodeSoftwareVer_Object = MibTableColumn
nodeSoftwareVer = _NodeSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 10),
    _NodeSoftwareVer_Type()
)
nodeSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSoftwareVer.setStatus("current")
_NodeCountryCode_Type = DisplayString
_NodeCountryCode_Object = MibTableColumn
nodeCountryCode = _NodeCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 11),
    _NodeCountryCode_Type()
)
nodeCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeCountryCode.setStatus("current")
_NodeUpTime_Type = TimeTicks
_NodeUpTime_Object = MibTableColumn
nodeUpTime = _NodeUpTime_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 12),
    _NodeUpTime_Type()
)
nodeUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeUpTime.setStatus("current")
_NodeLastResetReason_Type = DisplayString
_NodeLastResetReason_Object = MibTableColumn
nodeLastResetReason = _NodeLastResetReason_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 13),
    _NodeLastResetReason_Type()
)
nodeLastResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeLastResetReason.setStatus("current")


class _NodeOperations_Type(Integer32):
    """Custom type nodeOperations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("rebootNode", 1),
          ("operationInProgress", 2),
          ("operationFailed", 3),
          ("operationComplete", 4),
          ("configureAsGatewaySrv", 5),
          ("configureAsNormalNode", 6),
          ("recoverNeighbors", 7),
          ("refreshNodeConfig", 8),
          ("includeInUpgrade", 9),
          ("excludeFromUpgrade", 10))
    )


_NodeOperations_Type.__name__ = "Integer32"
_NodeOperations_Object = MibTableColumn
nodeOperations = _NodeOperations_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 14),
    _NodeOperations_Type()
)
nodeOperations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeOperations.setStatus("current")
_NodeSetResultStr_Type = DisplayString
_NodeSetResultStr_Object = MibTableColumn
nodeSetResultStr = _NodeSetResultStr_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 15),
    _NodeSetResultStr_Type()
)
nodeSetResultStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSetResultStr.setStatus("current")


class _NodeQosType_Type(Integer32):
    """Custom type nodeQosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qosNoPriority", 1),
          ("qosPortPriority", 2),
          ("qos8021pPriority", 3))
    )


_NodeQosType_Type.__name__ = "Integer32"
_NodeQosType_Object = MibTableColumn
nodeQosType = _NodeQosType_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 16),
    _NodeQosType_Type()
)
nodeQosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeQosType.setStatus("current")
_NodeStatus_Type = RowStatus
_NodeStatus_Object = MibTableColumn
nodeStatus = _NodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 1, 1, 30),
    _NodeStatus_Type()
)
nodeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nodeStatus.setStatus("current")
_NodeQosTable_Object = MibTable
nodeQosTable = _NodeQosTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 2)
)
if mibBuilder.loadTexts:
    nodeQosTable.setStatus("current")
_NodeQosEntry_Object = MibTableRow
nodeQosEntry = _NodeQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 2, 1)
)
nodeQosEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "nodeIndex"),
    (0, "FIRETIDE-MESH-MIB", "nodeQosIndex"),
)
if mibBuilder.loadTexts:
    nodeQosEntry.setStatus("current")
_NodeQosIndex_Type = Integer32
_NodeQosIndex_Object = MibTableColumn
nodeQosIndex = _NodeQosIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 2, 1, 1),
    _NodeQosIndex_Type()
)
nodeQosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nodeQosIndex.setStatus("current")


class _NodeQosPriority_Type(Integer32):
    """Custom type nodeQosPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_NodeQosPriority_Type.__name__ = "Integer32"
_NodeQosPriority_Object = MibTableColumn
nodeQosPriority = _NodeQosPriority_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 2, 1, 2),
    _NodeQosPriority_Type()
)
nodeQosPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeQosPriority.setStatus("current")
_NodeQosStatus_Type = RowStatus
_NodeQosStatus_Object = MibTableColumn
nodeQosStatus = _NodeQosStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 2, 2, 1, 10),
    _NodeQosStatus_Type()
)
nodeQosStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nodeQosStatus.setStatus("current")
_FiretideRadio_ObjectIdentity = ObjectIdentity
firetideRadio = _FiretideRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3)
)
_MeshRadioTable_Object = MibTable
meshRadioTable = _MeshRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 1)
)
if mibBuilder.loadTexts:
    meshRadioTable.setStatus("current")
_MeshRadioEntry_Object = MibTableRow
meshRadioEntry = _MeshRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 1, 1)
)
meshRadioEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
)
if mibBuilder.loadTexts:
    meshRadioEntry.setStatus("current")


class _MeshEssId_Type(OctetString):
    """Custom type meshEssId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MeshEssId_Type.__name__ = "OctetString"
_MeshEssId_Object = MibTableColumn
meshEssId = _MeshEssId_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 1, 1, 1),
    _MeshEssId_Type()
)
meshEssId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshEssId.setStatus("current")
_MeshCountryCode_Type = CountryCode
_MeshCountryCode_Object = MibTableColumn
meshCountryCode = _MeshCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 1, 1, 2),
    _MeshCountryCode_Type()
)
meshCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshCountryCode.setStatus("current")
_MeshPrimaryRadioProtocol_Type = RadioProtocol
_MeshPrimaryRadioProtocol_Object = MibTableColumn
meshPrimaryRadioProtocol = _MeshPrimaryRadioProtocol_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 1, 1, 3),
    _MeshPrimaryRadioProtocol_Type()
)
meshPrimaryRadioProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshPrimaryRadioProtocol.setStatus("current")


class _MeshMaxPrimaryChannelIndex_Type(Integer32):
    """Custom type meshMaxPrimaryChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MeshMaxPrimaryChannelIndex_Type.__name__ = "Integer32"
_MeshMaxPrimaryChannelIndex_Object = MibTableColumn
meshMaxPrimaryChannelIndex = _MeshMaxPrimaryChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 1, 1, 4),
    _MeshMaxPrimaryChannelIndex_Type()
)
meshMaxPrimaryChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meshMaxPrimaryChannelIndex.setStatus("current")
_MeshPrimaryRadioChannelNum_Type = Integer32
_MeshPrimaryRadioChannelNum_Object = MibTableColumn
meshPrimaryRadioChannelNum = _MeshPrimaryRadioChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 1, 1, 5),
    _MeshPrimaryRadioChannelNum_Type()
)
meshPrimaryRadioChannelNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshPrimaryRadioChannelNum.setStatus("current")


class _MeshRadioRange_Type(Integer32):
    """Custom type meshRadioRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("rangeHalfMile", 1),
          ("rangeOneMile", 2),
          ("rangeThreeMile", 3),
          ("rangeFiveMile", 4),
          ("rangeSevenMile", 5),
          ("rangeNineMile", 6))
    )


_MeshRadioRange_Type.__name__ = "Integer32"
_MeshRadioRange_Object = MibTableColumn
meshRadioRange = _MeshRadioRange_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 1, 1, 6),
    _MeshRadioRange_Type()
)
meshRadioRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshRadioRange.setStatus("current")
_MeshRadioRtsCtsEnable_Type = TruthValue
_MeshRadioRtsCtsEnable_Object = MibTableColumn
meshRadioRtsCtsEnable = _MeshRadioRtsCtsEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 1, 1, 7),
    _MeshRadioRtsCtsEnable_Type()
)
meshRadioRtsCtsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshRadioRtsCtsEnable.setStatus("current")


class _MeshRssiThreshold_Type(Integer32):
    """Custom type meshRssiThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-93, -55),
    )


_MeshRssiThreshold_Type.__name__ = "Integer32"
_MeshRssiThreshold_Object = MibTableColumn
meshRssiThreshold = _MeshRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 1, 1, 8),
    _MeshRssiThreshold_Type()
)
meshRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshRssiThreshold.setStatus("current")


class _MeshRssiHysteresisDelta_Type(Integer32):
    """Custom type meshRssiHysteresisDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_MeshRssiHysteresisDelta_Type.__name__ = "Integer32"
_MeshRssiHysteresisDelta_Object = MibTableColumn
meshRssiHysteresisDelta = _MeshRssiHysteresisDelta_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 1, 1, 9),
    _MeshRssiHysteresisDelta_Type()
)
meshRssiHysteresisDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshRssiHysteresisDelta.setStatus("current")
_MeshAccessPointAutoDiscover_Type = NetworkOperation
_MeshAccessPointAutoDiscover_Object = MibTableColumn
meshAccessPointAutoDiscover = _MeshAccessPointAutoDiscover_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 1, 1, 10),
    _MeshAccessPointAutoDiscover_Type()
)
meshAccessPointAutoDiscover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshAccessPointAutoDiscover.setStatus("current")
_MeshEssidEncrypt_Type = TruthValue
_MeshEssidEncrypt_Object = MibTableColumn
meshEssidEncrypt = _MeshEssidEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 1, 1, 11),
    _MeshEssidEncrypt_Type()
)
meshEssidEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshEssidEncrypt.setStatus("current")
_MeshRadioDataRate_Type = RadioDataRate
_MeshRadioDataRate_Object = MibTableColumn
meshRadioDataRate = _MeshRadioDataRate_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 1, 1, 12),
    _MeshRadioDataRate_Type()
)
meshRadioDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshRadioDataRate.setStatus("current")
_MeshRadioEntryStatus_Type = RowStatus
_MeshRadioEntryStatus_Object = MibTableColumn
meshRadioEntryStatus = _MeshRadioEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 1, 1, 20),
    _MeshRadioEntryStatus_Type()
)
meshRadioEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    meshRadioEntryStatus.setStatus("current")
_RadioChannelTable_Object = MibTable
radioChannelTable = _RadioChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 2)
)
if mibBuilder.loadTexts:
    radioChannelTable.setStatus("current")
_RadioChannelEntry_Object = MibTableRow
radioChannelEntry = _RadioChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 2, 1)
)
radioChannelEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "radioChannelProtocol"),
    (0, "FIRETIDE-MESH-MIB", "radioChannelIndex"),
)
if mibBuilder.loadTexts:
    radioChannelEntry.setStatus("current")
_RadioChannelProtocol_Type = RadioProtocol
_RadioChannelProtocol_Object = MibTableColumn
radioChannelProtocol = _RadioChannelProtocol_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 2, 1, 1),
    _RadioChannelProtocol_Type()
)
radioChannelProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radioChannelProtocol.setStatus("current")


class _RadioChannelIndex_Type(Integer32):
    """Custom type radioChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RadioChannelIndex_Type.__name__ = "Integer32"
_RadioChannelIndex_Object = MibTableColumn
radioChannelIndex = _RadioChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 2, 1, 2),
    _RadioChannelIndex_Type()
)
radioChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radioChannelIndex.setStatus("current")
_RadioChannelNum_Type = Integer32
_RadioChannelNum_Object = MibTableColumn
radioChannelNum = _RadioChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 2, 1, 3),
    _RadioChannelNum_Type()
)
radioChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioChannelNum.setStatus("current")
_RadioChannelMinPower_Type = Integer32
_RadioChannelMinPower_Object = MibTableColumn
radioChannelMinPower = _RadioChannelMinPower_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 2, 1, 4),
    _RadioChannelMinPower_Type()
)
radioChannelMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioChannelMinPower.setStatus("current")
_RadioChannelMaxPower_Type = Integer32
_RadioChannelMaxPower_Object = MibTableColumn
radioChannelMaxPower = _RadioChannelMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 2, 1, 5),
    _RadioChannelMaxPower_Type()
)
radioChannelMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioChannelMaxPower.setStatus("current")
_RadioChannelDfsEnabled_Type = TruthValue
_RadioChannelDfsEnabled_Object = MibTableColumn
radioChannelDfsEnabled = _RadioChannelDfsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 2, 1, 6),
    _RadioChannelDfsEnabled_Type()
)
radioChannelDfsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioChannelDfsEnabled.setStatus("current")
_RadioChannelLicensed_Type = TruthValue
_RadioChannelLicensed_Object = MibTableColumn
radioChannelLicensed = _RadioChannelLicensed_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 2, 1, 7),
    _RadioChannelLicensed_Type()
)
radioChannelLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioChannelLicensed.setStatus("current")
_RadioChannelStatus_Type = RowStatus
_RadioChannelStatus_Object = MibTableColumn
radioChannelStatus = _RadioChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 2, 1, 20),
    _RadioChannelStatus_Type()
)
radioChannelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radioChannelStatus.setStatus("current")
_RadioTable_Object = MibTable
radioTable = _RadioTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 3)
)
if mibBuilder.loadTexts:
    radioTable.setStatus("current")
_RadioEntry_Object = MibTableRow
radioEntry = _RadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 3, 1)
)
radioEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "nodeIndex"),
    (0, "FIRETIDE-MESH-MIB", "radioIndex"),
)
if mibBuilder.loadTexts:
    radioEntry.setStatus("current")


class _RadioIndex_Type(Integer32):
    """Custom type radioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RadioIndex_Type.__name__ = "Integer32"
_RadioIndex_Object = MibTableColumn
radioIndex = _RadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 3, 1, 1),
    _RadioIndex_Type()
)
radioIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    radioIndex.setStatus("current")
_RadioMacAddress_Type = OctetString
_RadioMacAddress_Object = MibTableColumn
radioMacAddress = _RadioMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 3, 1, 2),
    _RadioMacAddress_Type()
)
radioMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioMacAddress.setStatus("current")
_RadioSerialNo_Type = OctetString
_RadioSerialNo_Object = MibTableColumn
radioSerialNo = _RadioSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 3, 1, 3),
    _RadioSerialNo_Type()
)
radioSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioSerialNo.setStatus("current")


class _RadioTransmitPower_Type(Integer32):
    """Custom type radioTransmitPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 100),
    )


_RadioTransmitPower_Type.__name__ = "Integer32"
_RadioTransmitPower_Object = MibTableColumn
radioTransmitPower = _RadioTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 3, 1, 4),
    _RadioTransmitPower_Type()
)
radioTransmitPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioTransmitPower.setStatus("current")


class _RadioAntennaType_Type(Integer32):
    """Custom type radioAntennaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("antenna1", 1),
          ("antenna2", 2),
          ("diversity", 3))
    )


_RadioAntennaType_Type.__name__ = "Integer32"
_RadioAntennaType_Object = MibTableColumn
radioAntennaType = _RadioAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 3, 1, 5),
    _RadioAntennaType_Type()
)
radioAntennaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioAntennaType.setStatus("current")
_RadioLogicalIndex_Type = Integer32
_RadioLogicalIndex_Object = MibTableColumn
radioLogicalIndex = _RadioLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 3, 1, 6),
    _RadioLogicalIndex_Type()
)
radioLogicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLogicalIndex.setStatus("current")
_RadioStatus_Type = RowStatus
_RadioStatus_Object = MibTableColumn
radioStatus = _RadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 3, 1, 10),
    _RadioStatus_Type()
)
radioStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radioStatus.setStatus("current")
_AccessPointTable_Object = MibTable
accessPointTable = _AccessPointTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 4)
)
if mibBuilder.loadTexts:
    accessPointTable.setStatus("current")
_AccessPointEntry_Object = MibTableRow
accessPointEntry = _AccessPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 4, 1)
)
accessPointEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "nodeIndex"),
    (0, "FIRETIDE-MESH-MIB", "accessPointIp"),
)
if mibBuilder.loadTexts:
    accessPointEntry.setStatus("current")
_AccessPointIp_Type = IpAddress
_AccessPointIp_Object = MibTableColumn
accessPointIp = _AccessPointIp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 4, 1, 1),
    _AccessPointIp_Type()
)
accessPointIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    accessPointIp.setStatus("current")
_AccessPointName_Type = DisplayString
_AccessPointName_Object = MibTableColumn
accessPointName = _AccessPointName_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 4, 1, 2),
    _AccessPointName_Type()
)
accessPointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessPointName.setStatus("current")
_AccessPointUrl_Type = DisplayString
_AccessPointUrl_Object = MibTableColumn
accessPointUrl = _AccessPointUrl_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 4, 1, 3),
    _AccessPointUrl_Type()
)
accessPointUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessPointUrl.setStatus("current")
_AccessPointManual_Type = TruthValue
_AccessPointManual_Object = MibTableColumn
accessPointManual = _AccessPointManual_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 4, 1, 4),
    _AccessPointManual_Type()
)
accessPointManual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessPointManual.setStatus("current")
_AccessPointStatus_Type = RowStatus
_AccessPointStatus_Object = MibTableColumn
accessPointStatus = _AccessPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 3, 4, 1, 10),
    _AccessPointStatus_Type()
)
accessPointStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessPointStatus.setStatus("current")
_FiretidePort_ObjectIdentity = ObjectIdentity
firetidePort = _FiretidePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 1, 4)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 4, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 4, 1, 1)
)
portEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "nodeIndex"),
    (0, "FIRETIDE-MESH-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")


class _PortIndex_Type(Integer32):
    """Custom type portIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PortIndex_Type.__name__ = "Integer32"
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 4, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")
_PortMacAddress_Type = OctetString
_PortMacAddress_Object = MibTableColumn
portMacAddress = _PortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 4, 1, 1, 2),
    _PortMacAddress_Type()
)
portMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacAddress.setStatus("current")
_PortEnable_Type = TruthValue
_PortEnable_Object = MibTableColumn
portEnable = _PortEnable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 4, 1, 1, 3),
    _PortEnable_Type()
)
portEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEnable.setStatus("current")


class _PortPriority_Type(Integer32):
    """Custom type portPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_PortPriority_Type.__name__ = "Integer32"
_PortPriority_Object = MibTableColumn
portPriority = _PortPriority_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 4, 1, 1, 4),
    _PortPriority_Type()
)
portPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPriority.setStatus("current")
_PortAutoNegotiate_Type = TruthValue
_PortAutoNegotiate_Object = MibTableColumn
portAutoNegotiate = _PortAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 4, 1, 1, 5),
    _PortAutoNegotiate_Type()
)
portAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAutoNegotiate.setStatus("current")


class _PortSpeed_Type(Integer32):
    """Custom type portSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed100mbps", 1),
          ("speed10mbps", 2))
    )


_PortSpeed_Type.__name__ = "Integer32"
_PortSpeed_Object = MibTableColumn
portSpeed = _PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 4, 1, 1, 6),
    _PortSpeed_Type()
)
portSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeed.setStatus("current")


class _PortDuplex_Type(Integer32):
    """Custom type portDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_PortDuplex_Type.__name__ = "Integer32"
_PortDuplex_Object = MibTableColumn
portDuplex = _PortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 4, 1, 1, 7),
    _PortDuplex_Type()
)
portDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDuplex.setStatus("current")


class _PortVlanNo_Type(Integer32):
    """Custom type portVlanNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_PortVlanNo_Type.__name__ = "Integer32"
_PortVlanNo_Object = MibTableColumn
portVlanNo = _PortVlanNo_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 4, 1, 1, 8),
    _PortVlanNo_Type()
)
portVlanNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVlanNo.setStatus("current")


class _PortGatewayNo_Type(Integer32):
    """Custom type portGatewayNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PortGatewayNo_Type.__name__ = "Integer32"
_PortGatewayNo_Object = MibTableColumn
portGatewayNo = _PortGatewayNo_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 4, 1, 1, 9),
    _PortGatewayNo_Type()
)
portGatewayNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portGatewayNo.setStatus("current")
_PortStatus_Type = RowStatus
_PortStatus_Object = MibTableColumn
portStatus = _PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 4, 1, 1, 20),
    _PortStatus_Type()
)
portStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portStatus.setStatus("current")
_FiretideSecurity_ObjectIdentity = ObjectIdentity
firetideSecurity = _FiretideSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5)
)
_MeshSecurityTable_Object = MibTable
meshSecurityTable = _MeshSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1)
)
if mibBuilder.loadTexts:
    meshSecurityTable.setStatus("current")
_MeshSecurityEntry_Object = MibTableRow
meshSecurityEntry = _MeshSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1, 1)
)
meshSecurityEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
)
if mibBuilder.loadTexts:
    meshSecurityEntry.setStatus("current")


class _MeshWepFlag_Type(Integer32):
    """Custom type meshWepFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("key40bit", 2),
          ("key104bit", 3))
    )


_MeshWepFlag_Type.__name__ = "Integer32"
_MeshWepFlag_Object = MibTableColumn
meshWepFlag = _MeshWepFlag_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1, 1, 1),
    _MeshWepFlag_Type()
)
meshWepFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshWepFlag.setStatus("deprecated")


class _MeshWepKey_Type(OctetString):
    """Custom type meshWepKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(26, 26),
    )


_MeshWepKey_Type.__name__ = "OctetString"
_MeshWepKey_Object = MibTableColumn
meshWepKey = _MeshWepKey_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1, 1, 2),
    _MeshWepKey_Type()
)
meshWepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshWepKey.setStatus("deprecated")


class _MeshAesFlag_Type(Integer32):
    """Custom type meshAesFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("key128bit", 2),
          ("key256bit", 3))
    )


_MeshAesFlag_Type.__name__ = "Integer32"
_MeshAesFlag_Object = MibTableColumn
meshAesFlag = _MeshAesFlag_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1, 1, 3),
    _MeshAesFlag_Type()
)
meshAesFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshAesFlag.setStatus("deprecated")


class _MeshAesKey_Type(OctetString):
    """Custom type meshAesKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
        ValueSizeConstraint(64, 64),
    )


_MeshAesKey_Type.__name__ = "OctetString"
_MeshAesKey_Object = MibTableColumn
meshAesKey = _MeshAesKey_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1, 1, 4),
    _MeshAesKey_Type()
)
meshAesKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshAesKey.setStatus("deprecated")


class _MeshRwUser_Type(DisplayString):
    """Custom type meshRwUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MeshRwUser_Type.__name__ = "DisplayString"
_MeshRwUser_Object = MibTableColumn
meshRwUser = _MeshRwUser_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1, 1, 5),
    _MeshRwUser_Type()
)
meshRwUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshRwUser.setStatus("current")


class _MeshRwPasswd_Type(DisplayString):
    """Custom type meshRwPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MeshRwPasswd_Type.__name__ = "DisplayString"
_MeshRwPasswd_Object = MibTableColumn
meshRwPasswd = _MeshRwPasswd_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1, 1, 6),
    _MeshRwPasswd_Type()
)
meshRwPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshRwPasswd.setStatus("current")


class _MeshRoUser_Type(DisplayString):
    """Custom type meshRoUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MeshRoUser_Type.__name__ = "DisplayString"
_MeshRoUser_Object = MibTableColumn
meshRoUser = _MeshRoUser_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1, 1, 7),
    _MeshRoUser_Type()
)
meshRoUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshRoUser.setStatus("current")


class _MeshRoPasswd_Type(DisplayString):
    """Custom type meshRoPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MeshRoPasswd_Type.__name__ = "DisplayString"
_MeshRoPasswd_Object = MibTableColumn
meshRoPasswd = _MeshRoPasswd_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1, 1, 8),
    _MeshRoPasswd_Type()
)
meshRoPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshRoPasswd.setStatus("current")


class _MeshWirelessSecurityFlag_Type(Integer32):
    """Custom type meshWirelessSecurityFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("wep40bit", 2),
          ("wep104bit", 3),
          ("aesPsk256bit", 4))
    )


_MeshWirelessSecurityFlag_Type.__name__ = "Integer32"
_MeshWirelessSecurityFlag_Object = MibTableColumn
meshWirelessSecurityFlag = _MeshWirelessSecurityFlag_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1, 1, 9),
    _MeshWirelessSecurityFlag_Type()
)
meshWirelessSecurityFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshWirelessSecurityFlag.setStatus("current")


class _MeshWirelessSecurityKey_Type(OctetString):
    """Custom type meshWirelessSecurityKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(26, 26),
        ValueSizeConstraint(64, 64),
    )


_MeshWirelessSecurityKey_Type.__name__ = "OctetString"
_MeshWirelessSecurityKey_Object = MibTableColumn
meshWirelessSecurityKey = _MeshWirelessSecurityKey_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1, 1, 10),
    _MeshWirelessSecurityKey_Type()
)
meshWirelessSecurityKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshWirelessSecurityKey.setStatus("current")


class _MeshEndToEndSecurityFlag_Type(Integer32):
    """Custom type meshEndToEndSecurityFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("key128bit", 2),
          ("key256bit", 3))
    )


_MeshEndToEndSecurityFlag_Type.__name__ = "Integer32"
_MeshEndToEndSecurityFlag_Object = MibTableColumn
meshEndToEndSecurityFlag = _MeshEndToEndSecurityFlag_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1, 1, 11),
    _MeshEndToEndSecurityFlag_Type()
)
meshEndToEndSecurityFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshEndToEndSecurityFlag.setStatus("current")


class _MeshEndToEndSecurityKey_Type(OctetString):
    """Custom type meshEndToEndSecurityKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
        ValueSizeConstraint(64, 64),
    )


_MeshEndToEndSecurityKey_Type.__name__ = "OctetString"
_MeshEndToEndSecurityKey_Object = MibTableColumn
meshEndToEndSecurityKey = _MeshEndToEndSecurityKey_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1, 1, 12),
    _MeshEndToEndSecurityKey_Type()
)
meshEndToEndSecurityKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshEndToEndSecurityKey.setStatus("current")


class _MeshRwOldPasswd_Type(DisplayString):
    """Custom type meshRwOldPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MeshRwOldPasswd_Type.__name__ = "DisplayString"
_MeshRwOldPasswd_Object = MibTableColumn
meshRwOldPasswd = _MeshRwOldPasswd_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1, 1, 13),
    _MeshRwOldPasswd_Type()
)
meshRwOldPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshRwOldPasswd.setStatus("current")


class _MeshRoOldPasswd_Type(DisplayString):
    """Custom type meshRoOldPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MeshRoOldPasswd_Type.__name__ = "DisplayString"
_MeshRoOldPasswd_Object = MibTableColumn
meshRoOldPasswd = _MeshRoOldPasswd_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1, 1, 14),
    _MeshRoOldPasswd_Type()
)
meshRoOldPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshRoOldPasswd.setStatus("current")
_MeshSecurityStatus_Type = RowStatus
_MeshSecurityStatus_Object = MibTableColumn
meshSecurityStatus = _MeshSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 1, 1, 20),
    _MeshSecurityStatus_Type()
)
meshSecurityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    meshSecurityStatus.setStatus("current")


class _MeshLoginOperation_Type(Integer32):
    """Custom type meshLoginOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("operationTriggered", 1),
          ("loginOperation", 2),
          ("logoutOperation", 3))
    )


_MeshLoginOperation_Type.__name__ = "Integer32"
_MeshLoginOperation_Object = MibScalar
meshLoginOperation = _MeshLoginOperation_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 2),
    _MeshLoginOperation_Type()
)
meshLoginOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshLoginOperation.setStatus("current")
_MeshLoginIp_Type = IpAddress
_MeshLoginIp_Object = MibScalar
meshLoginIp = _MeshLoginIp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 3),
    _MeshLoginIp_Type()
)
meshLoginIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshLoginIp.setStatus("current")
_MeshLoginUserName_Type = DisplayString
_MeshLoginUserName_Object = MibScalar
meshLoginUserName = _MeshLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 4),
    _MeshLoginUserName_Type()
)
meshLoginUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshLoginUserName.setStatus("current")
_MeshLoginUserPassword_Type = DisplayString
_MeshLoginUserPassword_Object = MibScalar
meshLoginUserPassword = _MeshLoginUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 5),
    _MeshLoginUserPassword_Type()
)
meshLoginUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshLoginUserPassword.setStatus("current")
_MeshLoginPreload_Type = TruthValue
_MeshLoginPreload_Object = MibScalar
meshLoginPreload = _MeshLoginPreload_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 6),
    _MeshLoginPreload_Type()
)
meshLoginPreload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshLoginPreload.setStatus("current")


class _MeshLoginIndex_Type(Integer32):
    """Custom type meshLoginIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MeshLoginIndex_Type.__name__ = "Integer32"
_MeshLoginIndex_Object = MibScalar
meshLoginIndex = _MeshLoginIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 7),
    _MeshLoginIndex_Type()
)
meshLoginIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshLoginIndex.setStatus("current")
_MeshLoginErrorMessage_Type = DisplayString
_MeshLoginErrorMessage_Object = MibScalar
meshLoginErrorMessage = _MeshLoginErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 8),
    _MeshLoginErrorMessage_Type()
)
meshLoginErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meshLoginErrorMessage.setStatus("current")
_MeshRemoteUserTable_Object = MibTable
meshRemoteUserTable = _MeshRemoteUserTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 9)
)
if mibBuilder.loadTexts:
    meshRemoteUserTable.setStatus("current")
_MeshRemoteUserEntry_Object = MibTableRow
meshRemoteUserEntry = _MeshRemoteUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 9, 1)
)
meshRemoteUserEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
)
if mibBuilder.loadTexts:
    meshRemoteUserEntry.setStatus("current")
_MeshRootUserName_Type = DisplayString
_MeshRootUserName_Object = MibTableColumn
meshRootUserName = _MeshRootUserName_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 9, 1, 1),
    _MeshRootUserName_Type()
)
meshRootUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshRootUserName.setStatus("current")
_MeshRootPassword_Type = DisplayString
_MeshRootPassword_Object = MibTableColumn
meshRootPassword = _MeshRootPassword_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 9, 1, 2),
    _MeshRootPassword_Type()
)
meshRootPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshRootPassword.setStatus("current")
_MeshRootOldPassword_Type = DisplayString
_MeshRootOldPassword_Object = MibTableColumn
meshRootOldPassword = _MeshRootOldPassword_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 9, 1, 3),
    _MeshRootOldPassword_Type()
)
meshRootOldPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshRootOldPassword.setStatus("current")
_MeshSupportUserName_Type = DisplayString
_MeshSupportUserName_Object = MibTableColumn
meshSupportUserName = _MeshSupportUserName_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 9, 1, 4),
    _MeshSupportUserName_Type()
)
meshSupportUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshSupportUserName.setStatus("current")
_MeshSupportPassword_Type = DisplayString
_MeshSupportPassword_Object = MibTableColumn
meshSupportPassword = _MeshSupportPassword_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 9, 1, 5),
    _MeshSupportPassword_Type()
)
meshSupportPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshSupportPassword.setStatus("current")
_MeshSupportOldPassword_Type = DisplayString
_MeshSupportOldPassword_Object = MibTableColumn
meshSupportOldPassword = _MeshSupportOldPassword_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 9, 1, 6),
    _MeshSupportOldPassword_Type()
)
meshSupportOldPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshSupportOldPassword.setStatus("current")
_MeshSupportUserEnabled_Type = TruthValue
_MeshSupportUserEnabled_Object = MibTableColumn
meshSupportUserEnabled = _MeshSupportUserEnabled_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 9, 1, 7),
    _MeshSupportUserEnabled_Type()
)
meshSupportUserEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshSupportUserEnabled.setStatus("current")
_MeshCliUserName_Type = DisplayString
_MeshCliUserName_Object = MibTableColumn
meshCliUserName = _MeshCliUserName_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 9, 1, 8),
    _MeshCliUserName_Type()
)
meshCliUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshCliUserName.setStatus("current")
_MeshCliPassword_Type = DisplayString
_MeshCliPassword_Object = MibTableColumn
meshCliPassword = _MeshCliPassword_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 9, 1, 9),
    _MeshCliPassword_Type()
)
meshCliPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshCliPassword.setStatus("current")
_MeshCliOldPassword_Type = DisplayString
_MeshCliOldPassword_Object = MibTableColumn
meshCliOldPassword = _MeshCliOldPassword_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 9, 1, 10),
    _MeshCliOldPassword_Type()
)
meshCliOldPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshCliOldPassword.setStatus("current")
_MeshCliUserEnabled_Type = TruthValue
_MeshCliUserEnabled_Object = MibTableColumn
meshCliUserEnabled = _MeshCliUserEnabled_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 9, 1, 11),
    _MeshCliUserEnabled_Type()
)
meshCliUserEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshCliUserEnabled.setStatus("current")
_MeshTelnetLoginEnabled_Type = TruthValue
_MeshTelnetLoginEnabled_Object = MibTableColumn
meshTelnetLoginEnabled = _MeshTelnetLoginEnabled_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 9, 1, 12),
    _MeshTelnetLoginEnabled_Type()
)
meshTelnetLoginEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshTelnetLoginEnabled.setStatus("current")
_MeshRemoteUserStatus_Type = RowStatus
_MeshRemoteUserStatus_Object = MibTableColumn
meshRemoteUserStatus = _MeshRemoteUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 5, 9, 1, 20),
    _MeshRemoteUserStatus_Type()
)
meshRemoteUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    meshRemoteUserStatus.setStatus("current")
_FiretideTopology_ObjectIdentity = ObjectIdentity
firetideTopology = _FiretideTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6)
)
_NetworkTopologyTable_Object = MibTable
networkTopologyTable = _NetworkTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 1)
)
if mibBuilder.loadTexts:
    networkTopologyTable.setStatus("current")
_NetworkTopologyEntry_Object = MibTableRow
networkTopologyEntry = _NetworkTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 1, 1)
)
networkTopologyEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "neighborMeshIndex"),
    (0, "FIRETIDE-MESH-MIB", "neighborMeshLinkIndex"),
)
if mibBuilder.loadTexts:
    networkTopologyEntry.setStatus("current")


class _NeighborMeshIndex_Type(Integer32):
    """Custom type neighborMeshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NeighborMeshIndex_Type.__name__ = "Integer32"
_NeighborMeshIndex_Object = MibTableColumn
neighborMeshIndex = _NeighborMeshIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 1, 1, 1),
    _NeighborMeshIndex_Type()
)
neighborMeshIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    neighborMeshIndex.setStatus("current")
_NeighborMeshLinkIndex_Type = Integer32
_NeighborMeshLinkIndex_Object = MibTableColumn
neighborMeshLinkIndex = _NeighborMeshLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 1, 1, 2),
    _NeighborMeshLinkIndex_Type()
)
neighborMeshLinkIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    neighborMeshLinkIndex.setStatus("current")
_NeighborMeshLinkType_Type = LinkType
_NeighborMeshLinkType_Object = MibTableColumn
neighborMeshLinkType = _NeighborMeshLinkType_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 1, 1, 3),
    _NeighborMeshLinkType_Type()
)
neighborMeshLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborMeshLinkType.setStatus("current")
_NeighborMeshLinkStatus_Type = RowStatus
_NeighborMeshLinkStatus_Object = MibTableColumn
neighborMeshLinkStatus = _NeighborMeshLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 1, 1, 10),
    _NeighborMeshLinkStatus_Type()
)
neighborMeshLinkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    neighborMeshLinkStatus.setStatus("current")
_MeshTopologyTable_Object = MibTable
meshTopologyTable = _MeshTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 2)
)
if mibBuilder.loadTexts:
    meshTopologyTable.setStatus("current")
_MeshTopologyEntry_Object = MibTableRow
meshTopologyEntry = _MeshTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 2, 1)
)
meshTopologyEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "nodeIndex"),
    (0, "FIRETIDE-MESH-MIB", "neighborNodeIndex"),
    (0, "FIRETIDE-MESH-MIB", "neighborNodeLinkIndex"),
)
if mibBuilder.loadTexts:
    meshTopologyEntry.setStatus("current")
_NeighborNodeIndex_Type = Integer32
_NeighborNodeIndex_Object = MibTableColumn
neighborNodeIndex = _NeighborNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 2, 1, 1),
    _NeighborNodeIndex_Type()
)
neighborNodeIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    neighborNodeIndex.setStatus("current")
_NeighborNodeLinkIndex_Type = Integer32
_NeighborNodeLinkIndex_Object = MibTableColumn
neighborNodeLinkIndex = _NeighborNodeLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 2, 1, 2),
    _NeighborNodeLinkIndex_Type()
)
neighborNodeLinkIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    neighborNodeLinkIndex.setStatus("current")
_NeighborNodeLinkType_Type = LinkType
_NeighborNodeLinkType_Object = MibTableColumn
neighborNodeLinkType = _NeighborNodeLinkType_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 2, 1, 3),
    _NeighborNodeLinkType_Type()
)
neighborNodeLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neighborNodeLinkType.setStatus("current")
_NeighborNodeLinkStatus_Type = RowStatus
_NeighborNodeLinkStatus_Object = MibTableColumn
neighborNodeLinkStatus = _NeighborNodeLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 2, 1, 10),
    _NeighborNodeLinkStatus_Type()
)
neighborNodeLinkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    neighborNodeLinkStatus.setStatus("current")
_StaticRouteTable_Object = MibTable
staticRouteTable = _StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 3)
)
if mibBuilder.loadTexts:
    staticRouteTable.setStatus("current")
_StaticRouteEntry_Object = MibTableRow
staticRouteEntry = _StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 3, 1)
)
staticRouteEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "staticRouteIndex"),
)
if mibBuilder.loadTexts:
    staticRouteEntry.setStatus("current")


class _StaticRouteIndex_Type(Integer32):
    """Custom type staticRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_StaticRouteIndex_Type.__name__ = "Integer32"
_StaticRouteIndex_Object = MibTableColumn
staticRouteIndex = _StaticRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 3, 1, 1),
    _StaticRouteIndex_Type()
)
staticRouteIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    staticRouteIndex.setStatus("current")


class _StaticRouteLength_Type(Integer32):
    """Custom type staticRouteLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StaticRouteLength_Type.__name__ = "Integer32"
_StaticRouteLength_Object = MibTableColumn
staticRouteLength = _StaticRouteLength_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 3, 1, 2),
    _StaticRouteLength_Type()
)
staticRouteLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteLength.setStatus("current")


class _StaticRouteTrafficClass_Type(Integer32):
    """Custom type staticRouteTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("port", 2),
          ("vlan", 3))
    )


_StaticRouteTrafficClass_Type.__name__ = "Integer32"
_StaticRouteTrafficClass_Object = MibTableColumn
staticRouteTrafficClass = _StaticRouteTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 3, 1, 3),
    _StaticRouteTrafficClass_Type()
)
staticRouteTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteTrafficClass.setStatus("current")


class _StaticRouteClientPortIndex_Type(Integer32):
    """Custom type staticRouteClientPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_StaticRouteClientPortIndex_Type.__name__ = "Integer32"
_StaticRouteClientPortIndex_Object = MibTableColumn
staticRouteClientPortIndex = _StaticRouteClientPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 3, 1, 4),
    _StaticRouteClientPortIndex_Type()
)
staticRouteClientPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteClientPortIndex.setStatus("current")


class _StaticRouteClientVlanNo_Type(Integer32):
    """Custom type staticRouteClientVlanNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_StaticRouteClientVlanNo_Type.__name__ = "Integer32"
_StaticRouteClientVlanNo_Object = MibTableColumn
staticRouteClientVlanNo = _StaticRouteClientVlanNo_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 3, 1, 5),
    _StaticRouteClientVlanNo_Type()
)
staticRouteClientVlanNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteClientVlanNo.setStatus("current")
_StaticRouteEnabled_Type = TruthValue
_StaticRouteEnabled_Object = MibTableColumn
staticRouteEnabled = _StaticRouteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 3, 1, 6),
    _StaticRouteEnabled_Type()
)
staticRouteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteEnabled.setStatus("current")
_StaticRouteStatus_Type = RowStatus
_StaticRouteStatus_Object = MibTableColumn
staticRouteStatus = _StaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 3, 1, 10),
    _StaticRouteStatus_Type()
)
staticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteStatus.setStatus("current")
_StaticRouteNodeTable_Object = MibTable
staticRouteNodeTable = _StaticRouteNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 4)
)
if mibBuilder.loadTexts:
    staticRouteNodeTable.setStatus("current")
_StaticRouteNodeEntry_Object = MibTableRow
staticRouteNodeEntry = _StaticRouteNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 4, 1)
)
staticRouteNodeEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "staticRouteIndex"),
    (0, "FIRETIDE-MESH-MIB", "staticRouteNodeEntryIndex"),
)
if mibBuilder.loadTexts:
    staticRouteNodeEntry.setStatus("current")


class _StaticRouteNodeEntryIndex_Type(Integer32):
    """Custom type staticRouteNodeEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_StaticRouteNodeEntryIndex_Type.__name__ = "Integer32"
_StaticRouteNodeEntryIndex_Object = MibTableColumn
staticRouteNodeEntryIndex = _StaticRouteNodeEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 4, 1, 1),
    _StaticRouteNodeEntryIndex_Type()
)
staticRouteNodeEntryIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    staticRouteNodeEntryIndex.setStatus("current")
_StaticRouteNodeIndex_Type = Integer32
_StaticRouteNodeIndex_Object = MibTableColumn
staticRouteNodeIndex = _StaticRouteNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 4, 1, 2),
    _StaticRouteNodeIndex_Type()
)
staticRouteNodeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteNodeIndex.setStatus("current")


class _StaticRouteNodeInputPortIndex_Type(Integer32):
    """Custom type staticRouteNodeInputPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("eth1", 1),
          ("eth2", 2),
          ("eth3", 3),
          ("eth4", 4),
          ("radio", 5))
    )


_StaticRouteNodeInputPortIndex_Type.__name__ = "Integer32"
_StaticRouteNodeInputPortIndex_Object = MibTableColumn
staticRouteNodeInputPortIndex = _StaticRouteNodeInputPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 4, 1, 3),
    _StaticRouteNodeInputPortIndex_Type()
)
staticRouteNodeInputPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteNodeInputPortIndex.setStatus("current")


class _StaticRouteNodeOutputPortIndex_Type(Integer32):
    """Custom type staticRouteNodeOutputPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("eth1", 1),
          ("eth2", 2),
          ("eth3", 3),
          ("eth4", 4),
          ("radio", 5))
    )


_StaticRouteNodeOutputPortIndex_Type.__name__ = "Integer32"
_StaticRouteNodeOutputPortIndex_Object = MibTableColumn
staticRouteNodeOutputPortIndex = _StaticRouteNodeOutputPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 4, 1, 4),
    _StaticRouteNodeOutputPortIndex_Type()
)
staticRouteNodeOutputPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteNodeOutputPortIndex.setStatus("current")


class _StaticRouteNodeInputLogicalIndex_Type(Integer32):
    """Custom type staticRouteNodeInputLogicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_StaticRouteNodeInputLogicalIndex_Type.__name__ = "Integer32"
_StaticRouteNodeInputLogicalIndex_Object = MibTableColumn
staticRouteNodeInputLogicalIndex = _StaticRouteNodeInputLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 4, 1, 5),
    _StaticRouteNodeInputLogicalIndex_Type()
)
staticRouteNodeInputLogicalIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteNodeInputLogicalIndex.setStatus("current")


class _StaticRouteNodeOutputLogicalIndex_Type(Integer32):
    """Custom type staticRouteNodeOutputLogicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_StaticRouteNodeOutputLogicalIndex_Type.__name__ = "Integer32"
_StaticRouteNodeOutputLogicalIndex_Object = MibTableColumn
staticRouteNodeOutputLogicalIndex = _StaticRouteNodeOutputLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 4, 1, 6),
    _StaticRouteNodeOutputLogicalIndex_Type()
)
staticRouteNodeOutputLogicalIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteNodeOutputLogicalIndex.setStatus("current")
_StaticRouteNodeEntryStatus_Type = RowStatus
_StaticRouteNodeEntryStatus_Object = MibTableColumn
staticRouteNodeEntryStatus = _StaticRouteNodeEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 4, 1, 20),
    _StaticRouteNodeEntryStatus_Type()
)
staticRouteNodeEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteNodeEntryStatus.setStatus("current")
_LinkEliminationTable_Object = MibTable
linkEliminationTable = _LinkEliminationTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 5)
)
if mibBuilder.loadTexts:
    linkEliminationTable.setStatus("current")
_LinkEliminationEntry_Object = MibTableRow
linkEliminationEntry = _LinkEliminationEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 5, 1)
)
linkEliminationEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "nodeIndex"),
    (0, "FIRETIDE-MESH-MIB", "linkEliminationNodeIndex"),
)
if mibBuilder.loadTexts:
    linkEliminationEntry.setStatus("current")


class _LinkEliminationNodeIndex_Type(Integer32):
    """Custom type linkEliminationNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_LinkEliminationNodeIndex_Type.__name__ = "Integer32"
_LinkEliminationNodeIndex_Object = MibTableColumn
linkEliminationNodeIndex = _LinkEliminationNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 5, 1, 1),
    _LinkEliminationNodeIndex_Type()
)
linkEliminationNodeIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    linkEliminationNodeIndex.setStatus("current")
_LinkEliminationEntryStatus_Type = RowStatus
_LinkEliminationEntryStatus_Object = MibTableColumn
linkEliminationEntryStatus = _LinkEliminationEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 5, 1, 10),
    _LinkEliminationEntryStatus_Type()
)
linkEliminationEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkEliminationEntryStatus.setStatus("current")
_BroadcastGroupTable_Object = MibTable
broadcastGroupTable = _BroadcastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 6)
)
if mibBuilder.loadTexts:
    broadcastGroupTable.setStatus("current")
_BroadcastGroupEntry_Object = MibTableRow
broadcastGroupEntry = _BroadcastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 6, 1)
)
broadcastGroupEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "broadcastGroupIndex"),
)
if mibBuilder.loadTexts:
    broadcastGroupEntry.setStatus("current")


class _BroadcastGroupIndex_Type(Integer32):
    """Custom type broadcastGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_BroadcastGroupIndex_Type.__name__ = "Integer32"
_BroadcastGroupIndex_Object = MibTableColumn
broadcastGroupIndex = _BroadcastGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 6, 1, 1),
    _BroadcastGroupIndex_Type()
)
broadcastGroupIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    broadcastGroupIndex.setStatus("current")
_BroadcastGroupName_Type = DisplayString
_BroadcastGroupName_Object = MibTableColumn
broadcastGroupName = _BroadcastGroupName_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 6, 1, 2),
    _BroadcastGroupName_Type()
)
broadcastGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastGroupName.setStatus("current")
_BroadcastGroupEntryStatus_Type = RowStatus
_BroadcastGroupEntryStatus_Object = MibTableColumn
broadcastGroupEntryStatus = _BroadcastGroupEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 6, 1, 10),
    _BroadcastGroupEntryStatus_Type()
)
broadcastGroupEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    broadcastGroupEntryStatus.setStatus("current")
_BroadcastMeshTable_Object = MibTable
broadcastMeshTable = _BroadcastMeshTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 7)
)
if mibBuilder.loadTexts:
    broadcastMeshTable.setStatus("current")
_BroadcastMeshEntry_Object = MibTableRow
broadcastMeshEntry = _BroadcastMeshEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 7, 1)
)
broadcastMeshEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "broadcastGroupIndex"),
    (0, "FIRETIDE-MESH-MIB", "broadcastMeshIndex"),
)
if mibBuilder.loadTexts:
    broadcastMeshEntry.setStatus("current")


class _BroadcastMeshIndex_Type(Integer32):
    """Custom type broadcastMeshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BroadcastMeshIndex_Type.__name__ = "Integer32"
_BroadcastMeshIndex_Object = MibTableColumn
broadcastMeshIndex = _BroadcastMeshIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 7, 1, 1),
    _BroadcastMeshIndex_Type()
)
broadcastMeshIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    broadcastMeshIndex.setStatus("current")
_BroadcastMeshEntryStatus_Type = RowStatus
_BroadcastMeshEntryStatus_Object = MibTableColumn
broadcastMeshEntryStatus = _BroadcastMeshEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 6, 7, 1, 10),
    _BroadcastMeshEntryStatus_Type()
)
broadcastMeshEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    broadcastMeshEntryStatus.setStatus("current")
_FiretideStatistics_ObjectIdentity = ObjectIdentity
firetideStatistics = _FiretideStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7)
)
_NodeStatisticsTable_Object = MibTable
nodeStatisticsTable = _NodeStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1)
)
if mibBuilder.loadTexts:
    nodeStatisticsTable.setStatus("current")
_NodeStatisticsEntry_Object = MibTableRow
nodeStatisticsEntry = _NodeStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1, 1)
)
nodeStatisticsEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "nodeIndex"),
)
if mibBuilder.loadTexts:
    nodeStatisticsEntry.setStatus("current")
_NodeFerErrors_Type = Counter64
_NodeFerErrors_Object = MibTableColumn
nodeFerErrors = _NodeFerErrors_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1, 1, 1),
    _NodeFerErrors_Type()
)
nodeFerErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeFerErrors.setStatus("current")
_NodeRssi_Type = Integer32
_NodeRssi_Object = MibTableColumn
nodeRssi = _NodeRssi_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1, 1, 2),
    _NodeRssi_Type()
)
nodeRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRssi.setStatus("current")
_NodeNoiseInterference_Type = Integer32
_NodeNoiseInterference_Object = MibTableColumn
nodeNoiseInterference = _NodeNoiseInterference_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1, 1, 3),
    _NodeNoiseInterference_Type()
)
nodeNoiseInterference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeNoiseInterference.setStatus("current")
_NodeRetransmissions_Type = Counter64
_NodeRetransmissions_Object = MibTableColumn
nodeRetransmissions = _NodeRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1, 1, 4),
    _NodeRetransmissions_Type()
)
nodeRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRetransmissions.setStatus("current")
_NodeOpPackets_Type = Counter64
_NodeOpPackets_Object = MibTableColumn
nodeOpPackets = _NodeOpPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1, 1, 5),
    _NodeOpPackets_Type()
)
nodeOpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeOpPackets.setStatus("current")
_NodeInPackets_Type = Counter64
_NodeInPackets_Object = MibTableColumn
nodeInPackets = _NodeInPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1, 1, 6),
    _NodeInPackets_Type()
)
nodeInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeInPackets.setStatus("current")
_NodeWirelessOpPackets_Type = Counter64
_NodeWirelessOpPackets_Object = MibTableColumn
nodeWirelessOpPackets = _NodeWirelessOpPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1, 1, 7),
    _NodeWirelessOpPackets_Type()
)
nodeWirelessOpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeWirelessOpPackets.setStatus("current")
_NodeWirelessInPackets_Type = Counter64
_NodeWirelessInPackets_Object = MibTableColumn
nodeWirelessInPackets = _NodeWirelessInPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1, 1, 8),
    _NodeWirelessInPackets_Type()
)
nodeWirelessInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeWirelessInPackets.setStatus("current")
_NodeRadioErrors_Type = Counter64
_NodeRadioErrors_Object = MibTableColumn
nodeRadioErrors = _NodeRadioErrors_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1, 1, 9),
    _NodeRadioErrors_Type()
)
nodeRadioErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeRadioErrors.setStatus("current")
_NodeMacIntfErrors_Type = Counter64
_NodeMacIntfErrors_Object = MibTableColumn
nodeMacIntfErrors = _NodeMacIntfErrors_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1, 1, 10),
    _NodeMacIntfErrors_Type()
)
nodeMacIntfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeMacIntfErrors.setStatus("current")
_NodeMajorSoftwareErrors_Type = Counter64
_NodeMajorSoftwareErrors_Object = MibTableColumn
nodeMajorSoftwareErrors = _NodeMajorSoftwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1, 1, 11),
    _NodeMajorSoftwareErrors_Type()
)
nodeMajorSoftwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeMajorSoftwareErrors.setStatus("current")
_NodeMinorSoftwareErrors_Type = Counter64
_NodeMinorSoftwareErrors_Object = MibTableColumn
nodeMinorSoftwareErrors = _NodeMinorSoftwareErrors_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1, 1, 12),
    _NodeMinorSoftwareErrors_Type()
)
nodeMinorSoftwareErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeMinorSoftwareErrors.setStatus("current")
_NodeTemperatureOverRunErrors_Type = Counter64
_NodeTemperatureOverRunErrors_Object = MibTableColumn
nodeTemperatureOverRunErrors = _NodeTemperatureOverRunErrors_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1, 1, 13),
    _NodeTemperatureOverRunErrors_Type()
)
nodeTemperatureOverRunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeTemperatureOverRunErrors.setStatus("current")
_NodeBatteryLowErrors_Type = Counter64
_NodeBatteryLowErrors_Object = MibTableColumn
nodeBatteryLowErrors = _NodeBatteryLowErrors_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1, 1, 14),
    _NodeBatteryLowErrors_Type()
)
nodeBatteryLowErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeBatteryLowErrors.setStatus("current")
_NodeStatisticsRowStatus_Type = RowStatus
_NodeStatisticsRowStatus_Object = MibTableColumn
nodeStatisticsRowStatus = _NodeStatisticsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 1, 1, 30),
    _NodeStatisticsRowStatus_Type()
)
nodeStatisticsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nodeStatisticsRowStatus.setStatus("current")
_PortStatisticsTable_Object = MibTable
portStatisticsTable = _PortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 2)
)
if mibBuilder.loadTexts:
    portStatisticsTable.setStatus("current")
_PortStatisticsEntry_Object = MibTableRow
portStatisticsEntry = _PortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 2, 1)
)
portStatisticsEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "nodeIndex"),
    (0, "FIRETIDE-MESH-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portStatisticsEntry.setStatus("current")
_PortOpPackets_Type = Counter64
_PortOpPackets_Object = MibTableColumn
portOpPackets = _PortOpPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 2, 1, 1),
    _PortOpPackets_Type()
)
portOpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpPackets.setStatus("current")
_PortInPackets_Type = Counter64
_PortInPackets_Object = MibTableColumn
portInPackets = _PortInPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 2, 1, 2),
    _PortInPackets_Type()
)
portInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInPackets.setStatus("current")
_PortOpBytes_Type = Counter64
_PortOpBytes_Object = MibTableColumn
portOpBytes = _PortOpBytes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 2, 1, 3),
    _PortOpBytes_Type()
)
portOpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpBytes.setStatus("current")
_PortInBytes_Type = Counter64
_PortInBytes_Object = MibTableColumn
portInBytes = _PortInBytes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 2, 1, 4),
    _PortInBytes_Type()
)
portInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInBytes.setStatus("current")
_PortCollidedPackets_Type = Counter64
_PortCollidedPackets_Object = MibTableColumn
portCollidedPackets = _PortCollidedPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 2, 1, 5),
    _PortCollidedPackets_Type()
)
portCollidedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCollidedPackets.setStatus("current")
_PortInDropPackets_Type = Counter64
_PortInDropPackets_Object = MibTableColumn
portInDropPackets = _PortInDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 2, 1, 6),
    _PortInDropPackets_Type()
)
portInDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInDropPackets.setStatus("current")
_PortOutDropPackets_Type = Counter64
_PortOutDropPackets_Object = MibTableColumn
portOutDropPackets = _PortOutDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 2, 1, 7),
    _PortOutDropPackets_Type()
)
portOutDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutDropPackets.setStatus("current")
_PortRxErrors_Type = Counter64
_PortRxErrors_Object = MibTableColumn
portRxErrors = _PortRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 2, 1, 8),
    _PortRxErrors_Type()
)
portRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRxErrors.setStatus("current")
_PortStatisticsRowStatus_Type = RowStatus
_PortStatisticsRowStatus_Object = MibTableColumn
portStatisticsRowStatus = _PortStatisticsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 2, 1, 20),
    _PortStatisticsRowStatus_Type()
)
portStatisticsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portStatisticsRowStatus.setStatus("current")
_RadioStatisticsTable_Object = MibTable
radioStatisticsTable = _RadioStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 3)
)
if mibBuilder.loadTexts:
    radioStatisticsTable.setStatus("current")
_RadioStatisticsEntry_Object = MibTableRow
radioStatisticsEntry = _RadioStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 3, 1)
)
radioStatisticsEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "nodeIndex"),
    (0, "FIRETIDE-MESH-MIB", "radioIndex"),
)
if mibBuilder.loadTexts:
    radioStatisticsEntry.setStatus("current")
_RadioOpBytes_Type = Counter64
_RadioOpBytes_Object = MibTableColumn
radioOpBytes = _RadioOpBytes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 3, 1, 1),
    _RadioOpBytes_Type()
)
radioOpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioOpBytes.setStatus("current")
_RadioInBytes_Type = Counter64
_RadioInBytes_Object = MibTableColumn
radioInBytes = _RadioInBytes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 3, 1, 2),
    _RadioInBytes_Type()
)
radioInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioInBytes.setStatus("current")
_RadioDropPackets_Type = Counter64
_RadioDropPackets_Object = MibTableColumn
radioDropPackets = _RadioDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 3, 1, 3),
    _RadioDropPackets_Type()
)
radioDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioDropPackets.setStatus("current")
_RadioRetPackets_Type = Counter64
_RadioRetPackets_Object = MibTableColumn
radioRetPackets = _RadioRetPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 3, 1, 4),
    _RadioRetPackets_Type()
)
radioRetPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRetPackets.setStatus("current")
_RadioOpPackets_Type = Counter64
_RadioOpPackets_Object = MibTableColumn
radioOpPackets = _RadioOpPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 3, 1, 5),
    _RadioOpPackets_Type()
)
radioOpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioOpPackets.setStatus("current")
_RadioInPackets_Type = Counter64
_RadioInPackets_Object = MibTableColumn
radioInPackets = _RadioInPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 3, 1, 6),
    _RadioInPackets_Type()
)
radioInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioInPackets.setStatus("current")
_RadioTxErrors_Type = Counter64
_RadioTxErrors_Object = MibTableColumn
radioTxErrors = _RadioTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 3, 1, 7),
    _RadioTxErrors_Type()
)
radioTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioTxErrors.setStatus("current")
_RadioRxErrors_Type = Counter64
_RadioRxErrors_Object = MibTableColumn
radioRxErrors = _RadioRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 3, 1, 8),
    _RadioRxErrors_Type()
)
radioRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRxErrors.setStatus("current")
_RadioRetFailPackets_Type = Counter64
_RadioRetFailPackets_Object = MibTableColumn
radioRetFailPackets = _RadioRetFailPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 3, 1, 9),
    _RadioRetFailPackets_Type()
)
radioRetFailPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRetFailPackets.setStatus("current")
_RadioRssi_Type = Integer32
_RadioRssi_Object = MibTableColumn
radioRssi = _RadioRssi_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 3, 1, 10),
    _RadioRssi_Type()
)
radioRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioRssi.setStatus("current")
_RadioLinkQuality_Type = Integer32
_RadioLinkQuality_Object = MibTableColumn
radioLinkQuality = _RadioLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 3, 1, 11),
    _RadioLinkQuality_Type()
)
radioLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioLinkQuality.setStatus("current")
_RadioNoise_Type = Integer32
_RadioNoise_Object = MibTableColumn
radioNoise = _RadioNoise_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 3, 1, 12),
    _RadioNoise_Type()
)
radioNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioNoise.setStatus("current")
_RadioUsedAntenna_Type = Integer32
_RadioUsedAntenna_Object = MibTableColumn
radioUsedAntenna = _RadioUsedAntenna_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 3, 1, 13),
    _RadioUsedAntenna_Type()
)
radioUsedAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioUsedAntenna.setStatus("current")
_RadioStatisticsRowStatus_Type = RowStatus
_RadioStatisticsRowStatus_Object = MibTableColumn
radioStatisticsRowStatus = _RadioStatisticsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 3, 1, 30),
    _RadioStatisticsRowStatus_Type()
)
radioStatisticsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radioStatisticsRowStatus.setStatus("current")
_NodeToNodeStatisticsTable_Object = MibTable
nodeToNodeStatisticsTable = _NodeToNodeStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 4)
)
if mibBuilder.loadTexts:
    nodeToNodeStatisticsTable.setStatus("current")
_NodeToNodeStatisticsEntry_Object = MibTableRow
nodeToNodeStatisticsEntry = _NodeToNodeStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 4, 1)
)
nodeToNodeStatisticsEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "nodeIndex"),
    (0, "FIRETIDE-MESH-MIB", "nodeToNodeDestIndex"),
)
if mibBuilder.loadTexts:
    nodeToNodeStatisticsEntry.setStatus("current")
_NodeToNodeDestIndex_Type = Integer32
_NodeToNodeDestIndex_Object = MibTableColumn
nodeToNodeDestIndex = _NodeToNodeDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 4, 1, 1),
    _NodeToNodeDestIndex_Type()
)
nodeToNodeDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nodeToNodeDestIndex.setStatus("current")
_NodeToNodeRssi_Type = Integer32
_NodeToNodeRssi_Object = MibTableColumn
nodeToNodeRssi = _NodeToNodeRssi_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 4, 1, 2),
    _NodeToNodeRssi_Type()
)
nodeToNodeRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeToNodeRssi.setStatus("current")
_NodeToNodeTxRate_Type = Integer32
_NodeToNodeTxRate_Object = MibTableColumn
nodeToNodeTxRate = _NodeToNodeTxRate_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 4, 1, 3),
    _NodeToNodeTxRate_Type()
)
nodeToNodeTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeToNodeTxRate.setStatus("current")
_NodeToNodeInPkts_Type = Counter32
_NodeToNodeInPkts_Object = MibTableColumn
nodeToNodeInPkts = _NodeToNodeInPkts_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 4, 1, 4),
    _NodeToNodeInPkts_Type()
)
nodeToNodeInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeToNodeInPkts.setStatus("current")
_NodeToNodeOutPkts_Type = Counter32
_NodeToNodeOutPkts_Object = MibTableColumn
nodeToNodeOutPkts = _NodeToNodeOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 4, 1, 5),
    _NodeToNodeOutPkts_Type()
)
nodeToNodeOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeToNodeOutPkts.setStatus("current")
_NodeToNodeInBytes_Type = Counter32
_NodeToNodeInBytes_Object = MibTableColumn
nodeToNodeInBytes = _NodeToNodeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 4, 1, 6),
    _NodeToNodeInBytes_Type()
)
nodeToNodeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeToNodeInBytes.setStatus("current")
_NodeToNodeOutBytes_Type = Counter32
_NodeToNodeOutBytes_Object = MibTableColumn
nodeToNodeOutBytes = _NodeToNodeOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 4, 1, 7),
    _NodeToNodeOutBytes_Type()
)
nodeToNodeOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeToNodeOutBytes.setStatus("current")
_NodeToNodeOutPktsDrp_Type = Counter32
_NodeToNodeOutPktsDrp_Object = MibTableColumn
nodeToNodeOutPktsDrp = _NodeToNodeOutPktsDrp_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 4, 1, 8),
    _NodeToNodeOutPktsDrp_Type()
)
nodeToNodeOutPktsDrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeToNodeOutPktsDrp.setStatus("current")
_NodeToNodeTotalRetries_Type = Counter32
_NodeToNodeTotalRetries_Object = MibTableColumn
nodeToNodeTotalRetries = _NodeToNodeTotalRetries_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 4, 1, 9),
    _NodeToNodeTotalRetries_Type()
)
nodeToNodeTotalRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeToNodeTotalRetries.setStatus("current")
_NodeToNodeRowStatus_Type = RowStatus
_NodeToNodeRowStatus_Object = MibTableColumn
nodeToNodeRowStatus = _NodeToNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 4, 1, 20),
    _NodeToNodeRowStatus_Type()
)
nodeToNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nodeToNodeRowStatus.setStatus("current")
_StaticRouteNodeStatisticsTable_Object = MibTable
staticRouteNodeStatisticsTable = _StaticRouteNodeStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 5)
)
if mibBuilder.loadTexts:
    staticRouteNodeStatisticsTable.setStatus("current")
_StaticRouteNodeStatisticsEntry_Object = MibTableRow
staticRouteNodeStatisticsEntry = _StaticRouteNodeStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 5, 1)
)
staticRouteNodeStatisticsEntry.setIndexNames(
    (0, "FIRETIDE-MESH-MIB", "meshIndex"),
    (0, "FIRETIDE-MESH-MIB", "staticRouteIndex"),
    (0, "FIRETIDE-MESH-MIB", "staticRouteNodeEntryIndex"),
)
if mibBuilder.loadTexts:
    staticRouteNodeStatisticsEntry.setStatus("current")
_StaticRouteNodeRcvPackets_Type = Counter32
_StaticRouteNodeRcvPackets_Object = MibTableColumn
staticRouteNodeRcvPackets = _StaticRouteNodeRcvPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 5, 1, 1),
    _StaticRouteNodeRcvPackets_Type()
)
staticRouteNodeRcvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteNodeRcvPackets.setStatus("current")
_StaticRouteNodeFwdPackets_Type = Counter32
_StaticRouteNodeFwdPackets_Object = MibTableColumn
staticRouteNodeFwdPackets = _StaticRouteNodeFwdPackets_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 5, 1, 2),
    _StaticRouteNodeFwdPackets_Type()
)
staticRouteNodeFwdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteNodeFwdPackets.setStatus("current")
_StaticRouteNodeStatisticsEntryStatus_Type = RowStatus
_StaticRouteNodeStatisticsEntryStatus_Object = MibTableColumn
staticRouteNodeStatisticsEntryStatus = _StaticRouteNodeStatisticsEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 22835, 1, 7, 5, 1, 10),
    _StaticRouteNodeStatisticsEntryStatus_Type()
)
staticRouteNodeStatisticsEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteNodeStatisticsEntryStatus.setStatus("current")
_FiretideTrap_ObjectIdentity = ObjectIdentity
firetideTrap = _FiretideTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16)
)
_FiretideMeshMibConformance_ObjectIdentity = ObjectIdentity
firetideMeshMibConformance = _FiretideMeshMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 1, 20)
)
_FiretideMeshMibGroups_ObjectIdentity = ObjectIdentity
firetideMeshMibGroups = _FiretideMeshMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22835, 1, 20, 2)
)

# Managed Objects groups

firetideNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22835, 1, 20, 2, 1)
)
firetideNetworkGroup.setObjects(
      *(("FIRETIDE-MESH-MIB", "numMesh"),
        ("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "meshName"),
        ("FIRETIDE-MESH-MIB", "meshNmsIp"),
        ("FIRETIDE-MESH-MIB", "meshNmsIpMask"),
        ("FIRETIDE-MESH-MIB", "meshNmsDefaultGateway"),
        ("FIRETIDE-MESH-MIB", "meshStatsCollectInterval"),
        ("FIRETIDE-MESH-MIB", "meshNumNodes"),
        ("FIRETIDE-MESH-MIB", "meshNumNodesDown"),
        ("FIRETIDE-MESH-MIB", "meshNumVlans"),
        ("FIRETIDE-MESH-MIB", "meshGatewayGroupConfiguredBitMap"),
        ("FIRETIDE-MESH-MIB", "meshMacListSize"),
        ("FIRETIDE-MESH-MIB", "meshMacFilterType"),
        ("FIRETIDE-MESH-MIB", "meshNeighborTableSize"),
        ("FIRETIDE-MESH-MIB", "rebootMesh"),
        ("FIRETIDE-MESH-MIB", "meshConfigApply"),
        ("FIRETIDE-MESH-MIB", "applyErrorString"),
        ("FIRETIDE-MESH-MIB", "newMeshIndex"),
        ("FIRETIDE-MESH-MIB", "verifyMeshwideConfig"),
        ("FIRETIDE-MESH-MIB", "meshConfigComparison"),
        ("FIRETIDE-MESH-MIB", "verifyRadioConfig"),
        ("FIRETIDE-MESH-MIB", "radioConfigComparison"),
        ("FIRETIDE-MESH-MIB", "upgradeMeshSoftware"),
        ("FIRETIDE-MESH-MIB", "upgradeSoftwarePath"),
        ("FIRETIDE-MESH-MIB", "upgradeSoftwareCompletion"),
        ("FIRETIDE-MESH-MIB", "importMeshwideConfig"),
        ("FIRETIDE-MESH-MIB", "exportMeshwideConfig"),
        ("FIRETIDE-MESH-MIB", "meshConfigUpdateNodeIndex"),
        ("FIRETIDE-MESH-MIB", "meshConfigUpdatePath"),
        ("FIRETIDE-MESH-MIB", "meshConfigSavedPasswd"),
        ("FIRETIDE-MESH-MIB", "meshConfigGwGrpNameToApply"),
        ("FIRETIDE-MESH-MIB", "meshConfigGwPrimary"),
        ("FIRETIDE-MESH-MIB", "meshConfigSavedUserName"),
        ("FIRETIDE-MESH-MIB", "meshwidePriorityEnable"),
        ("FIRETIDE-MESH-MIB", "meshwideCongestionControlEnable"),
        ("FIRETIDE-MESH-MIB", "meshReservedMacEnable"),
        ("FIRETIDE-MESH-MIB", "meshConfigEntryStatus"),
        ("FIRETIDE-MESH-MIB", "vlanTagged"),
        ("FIRETIDE-MESH-MIB", "vlanStatus"),
        ("FIRETIDE-MESH-MIB", "vlanTrunkOnPort3"),
        ("FIRETIDE-MESH-MIB", "vlanTrunkOnPort4"),
        ("FIRETIDE-MESH-MIB", "vlanTrunkMgmtVlanIdOnPort3"),
        ("FIRETIDE-MESH-MIB", "vlanTrunkMgmtVlanIdOnPort4"),
        ("FIRETIDE-MESH-MIB", "vlanTrunkStatus"),
        ("FIRETIDE-MESH-MIB", "macFilterEntryStatus"),
        ("FIRETIDE-MESH-MIB", "bridgeGroupName"),
        ("FIRETIDE-MESH-MIB", "bridgeGroupRemoteMeshIndex"),
        ("FIRETIDE-MESH-MIB", "bridgeGroupNumIfs"),
        ("FIRETIDE-MESH-MIB", "bridgeGroupAesFlag"),
        ("FIRETIDE-MESH-MIB", "bridgeGroupAesKey"),
        ("FIRETIDE-MESH-MIB", "bridgeGroupStatus"),
        ("FIRETIDE-MESH-MIB", "bridgeGroupIfNodeIndex"),
        ("FIRETIDE-MESH-MIB", "bridgeGroupIfIp"),
        ("FIRETIDE-MESH-MIB", "bridgeGroupIfIpMask"),
        ("FIRETIDE-MESH-MIB", "bridgeGroupIfDefaultGateway"),
        ("FIRETIDE-MESH-MIB", "bridgeGroupIfRemoteIp"),
        ("FIRETIDE-MESH-MIB", "bridgeGroupIfPortIndex"),
        ("FIRETIDE-MESH-MIB", "bridgeGroupIfStatus"),
        ("FIRETIDE-MESH-MIB", "gatewayServerName"),
        ("FIRETIDE-MESH-MIB", "gatewayServerPriNode"),
        ("FIRETIDE-MESH-MIB", "gatewayServerNumIfs"),
        ("FIRETIDE-MESH-MIB", "gatewayServerAesFlag"),
        ("FIRETIDE-MESH-MIB", "gatewayServerAesKey"),
        ("FIRETIDE-MESH-MIB", "gatewayServerSrvPriIfIp"),
        ("FIRETIDE-MESH-MIB", "gatewayServerSrvIfIpMask"),
        ("FIRETIDE-MESH-MIB", "gatewayServerSrvIfDefaultGateway"),
        ("FIRETIDE-MESH-MIB", "gatewayServerSrvPortIndex"),
        ("FIRETIDE-MESH-MIB", "gatewayServerSrvRedundant"),
        ("FIRETIDE-MESH-MIB", "gatewayServerSecNode"),
        ("FIRETIDE-MESH-MIB", "gatewayServerSrvSecIfIp"),
        ("FIRETIDE-MESH-MIB", "gatewayServerStatus"),
        ("FIRETIDE-MESH-MIB", "gatewayServerIfNodeIndex"),
        ("FIRETIDE-MESH-MIB", "gatewayServerIfPortIndex"),
        ("FIRETIDE-MESH-MIB", "gatewayServerIfIp"),
        ("FIRETIDE-MESH-MIB", "gatewayServerIfIpMask"),
        ("FIRETIDE-MESH-MIB", "gatewayServerIfDefaultGateway"),
        ("FIRETIDE-MESH-MIB", "gatewayServerIfLinkRate"),
        ("FIRETIDE-MESH-MIB", "gatewayServerSrvLogicalIndex"),
        ("FIRETIDE-MESH-MIB", "gatewayServerIfPriLogicalIndex"),
        ("FIRETIDE-MESH-MIB", "gatewayServerIfSecLogicalIndex"),
        ("FIRETIDE-MESH-MIB", "gatewayServerIfStatus"),
        ("FIRETIDE-MESH-MIB", "ethernetLocalIp"),
        ("FIRETIDE-MESH-MIB", "ethernetTunnelName"),
        ("FIRETIDE-MESH-MIB", "ethernetPortIndex"),
        ("FIRETIDE-MESH-MIB", "ethernetLocalIpMask"),
        ("FIRETIDE-MESH-MIB", "ethernetDefaultGateway"),
        ("FIRETIDE-MESH-MIB", "ethernetTunnelAesFlag"),
        ("FIRETIDE-MESH-MIB", "ethernetTunnelAesKey"),
        ("FIRETIDE-MESH-MIB", "ethernetLinkRate"),
        ("FIRETIDE-MESH-MIB", "ethernetLinkLogicalIndex"),
        ("FIRETIDE-MESH-MIB", "ethernetDirectEntryStatus"),
        ("FIRETIDE-MESH-MIB", "multicastGroupEntryStatus"))
)
if mibBuilder.loadTexts:
    firetideNetworkGroup.setStatus("current")

firetideNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22835, 1, 20, 2, 2)
)
firetideNodeGroup.setObjects(
      *(("FIRETIDE-MESH-MIB", "nodeIndex"),
        ("FIRETIDE-MESH-MIB", "nodeDisplayName"),
        ("FIRETIDE-MESH-MIB", "nodeModelNo"),
        ("FIRETIDE-MESH-MIB", "nodeSubId"),
        ("FIRETIDE-MESH-MIB", "nodeLocationString"),
        ("FIRETIDE-MESH-MIB", "nodeLocationX"),
        ("FIRETIDE-MESH-MIB", "nodeLocationY"),
        ("FIRETIDE-MESH-MIB", "nodeLocationZ"),
        ("FIRETIDE-MESH-MIB", "nodeSerialNo"),
        ("FIRETIDE-MESH-MIB", "nodeSoftwareVer"),
        ("FIRETIDE-MESH-MIB", "nodeCountryCode"),
        ("FIRETIDE-MESH-MIB", "nodeUpTime"),
        ("FIRETIDE-MESH-MIB", "nodeLastResetReason"),
        ("FIRETIDE-MESH-MIB", "nodeOperations"),
        ("FIRETIDE-MESH-MIB", "nodeSetResultStr"),
        ("FIRETIDE-MESH-MIB", "nodeQosType"),
        ("FIRETIDE-MESH-MIB", "nodeStatus"),
        ("FIRETIDE-MESH-MIB", "nodeQosPriority"),
        ("FIRETIDE-MESH-MIB", "nodeQosStatus"))
)
if mibBuilder.loadTexts:
    firetideNodeGroup.setStatus("current")

firetideRadioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22835, 1, 20, 2, 3)
)
firetideRadioGroup.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshEssId"),
        ("FIRETIDE-MESH-MIB", "meshCountryCode"),
        ("FIRETIDE-MESH-MIB", "meshPrimaryRadioProtocol"),
        ("FIRETIDE-MESH-MIB", "meshMaxPrimaryChannelIndex"),
        ("FIRETIDE-MESH-MIB", "meshPrimaryRadioChannelNum"),
        ("FIRETIDE-MESH-MIB", "meshRadioRange"),
        ("FIRETIDE-MESH-MIB", "meshRadioRtsCtsEnable"),
        ("FIRETIDE-MESH-MIB", "meshRssiThreshold"),
        ("FIRETIDE-MESH-MIB", "meshRssiHysteresisDelta"),
        ("FIRETIDE-MESH-MIB", "meshAccessPointAutoDiscover"),
        ("FIRETIDE-MESH-MIB", "meshEssidEncrypt"),
        ("FIRETIDE-MESH-MIB", "meshRadioDataRate"),
        ("FIRETIDE-MESH-MIB", "meshRadioEntryStatus"),
        ("FIRETIDE-MESH-MIB", "radioChannelNum"),
        ("FIRETIDE-MESH-MIB", "radioChannelMinPower"),
        ("FIRETIDE-MESH-MIB", "radioChannelMaxPower"),
        ("FIRETIDE-MESH-MIB", "radioChannelDfsEnabled"),
        ("FIRETIDE-MESH-MIB", "radioChannelLicensed"),
        ("FIRETIDE-MESH-MIB", "radioChannelStatus"),
        ("FIRETIDE-MESH-MIB", "radioIndex"),
        ("FIRETIDE-MESH-MIB", "radioMacAddress"),
        ("FIRETIDE-MESH-MIB", "radioSerialNo"),
        ("FIRETIDE-MESH-MIB", "radioTransmitPower"),
        ("FIRETIDE-MESH-MIB", "radioAntennaType"),
        ("FIRETIDE-MESH-MIB", "radioLogicalIndex"),
        ("FIRETIDE-MESH-MIB", "radioStatus"),
        ("FIRETIDE-MESH-MIB", "accessPointIp"),
        ("FIRETIDE-MESH-MIB", "accessPointName"),
        ("FIRETIDE-MESH-MIB", "accessPointUrl"),
        ("FIRETIDE-MESH-MIB", "accessPointManual"),
        ("FIRETIDE-MESH-MIB", "accessPointStatus"))
)
if mibBuilder.loadTexts:
    firetideRadioGroup.setStatus("current")

firetidePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22835, 1, 20, 2, 4)
)
firetidePortGroup.setObjects(
      *(("FIRETIDE-MESH-MIB", "portIndex"),
        ("FIRETIDE-MESH-MIB", "portMacAddress"),
        ("FIRETIDE-MESH-MIB", "portEnable"),
        ("FIRETIDE-MESH-MIB", "portPriority"),
        ("FIRETIDE-MESH-MIB", "portAutoNegotiate"),
        ("FIRETIDE-MESH-MIB", "portSpeed"),
        ("FIRETIDE-MESH-MIB", "portDuplex"),
        ("FIRETIDE-MESH-MIB", "portVlanNo"),
        ("FIRETIDE-MESH-MIB", "portGatewayNo"),
        ("FIRETIDE-MESH-MIB", "portStatus"))
)
if mibBuilder.loadTexts:
    firetidePortGroup.setStatus("current")

firetideSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22835, 1, 20, 2, 5)
)
firetideSecurityGroup.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshLoginOperation"),
        ("FIRETIDE-MESH-MIB", "meshLoginIp"),
        ("FIRETIDE-MESH-MIB", "meshLoginUserName"),
        ("FIRETIDE-MESH-MIB", "meshLoginUserPassword"),
        ("FIRETIDE-MESH-MIB", "meshLoginPreload"),
        ("FIRETIDE-MESH-MIB", "meshLoginIndex"),
        ("FIRETIDE-MESH-MIB", "meshLoginErrorMessage"),
        ("FIRETIDE-MESH-MIB", "meshWepFlag"),
        ("FIRETIDE-MESH-MIB", "meshWepKey"),
        ("FIRETIDE-MESH-MIB", "meshAesFlag"),
        ("FIRETIDE-MESH-MIB", "meshAesKey"),
        ("FIRETIDE-MESH-MIB", "meshRwUser"),
        ("FIRETIDE-MESH-MIB", "meshRwPasswd"),
        ("FIRETIDE-MESH-MIB", "meshRoUser"),
        ("FIRETIDE-MESH-MIB", "meshRoPasswd"),
        ("FIRETIDE-MESH-MIB", "meshWirelessSecurityFlag"),
        ("FIRETIDE-MESH-MIB", "meshWirelessSecurityKey"),
        ("FIRETIDE-MESH-MIB", "meshEndToEndSecurityFlag"),
        ("FIRETIDE-MESH-MIB", "meshEndToEndSecurityKey"),
        ("FIRETIDE-MESH-MIB", "meshRwOldPasswd"),
        ("FIRETIDE-MESH-MIB", "meshRoOldPasswd"),
        ("FIRETIDE-MESH-MIB", "meshSecurityStatus"),
        ("FIRETIDE-MESH-MIB", "meshRootUserName"),
        ("FIRETIDE-MESH-MIB", "meshRootPassword"),
        ("FIRETIDE-MESH-MIB", "meshRootOldPassword"),
        ("FIRETIDE-MESH-MIB", "meshSupportUserName"),
        ("FIRETIDE-MESH-MIB", "meshSupportPassword"),
        ("FIRETIDE-MESH-MIB", "meshSupportOldPassword"),
        ("FIRETIDE-MESH-MIB", "meshSupportUserEnabled"),
        ("FIRETIDE-MESH-MIB", "meshCliUserName"),
        ("FIRETIDE-MESH-MIB", "meshCliPassword"),
        ("FIRETIDE-MESH-MIB", "meshCliOldPassword"),
        ("FIRETIDE-MESH-MIB", "meshCliUserEnabled"),
        ("FIRETIDE-MESH-MIB", "meshTelnetLoginEnabled"),
        ("FIRETIDE-MESH-MIB", "meshRemoteUserStatus"))
)
if mibBuilder.loadTexts:
    firetideSecurityGroup.setStatus("current")

firetideTopologyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22835, 1, 20, 2, 6)
)
firetideTopologyGroup.setObjects(
      *(("FIRETIDE-MESH-MIB", "neighborMeshIndex"),
        ("FIRETIDE-MESH-MIB", "neighborMeshLinkIndex"),
        ("FIRETIDE-MESH-MIB", "neighborMeshLinkType"),
        ("FIRETIDE-MESH-MIB", "neighborMeshLinkStatus"),
        ("FIRETIDE-MESH-MIB", "neighborNodeIndex"),
        ("FIRETIDE-MESH-MIB", "neighborNodeLinkIndex"),
        ("FIRETIDE-MESH-MIB", "neighborNodeLinkType"),
        ("FIRETIDE-MESH-MIB", "neighborNodeLinkStatus"),
        ("FIRETIDE-MESH-MIB", "staticRouteLength"),
        ("FIRETIDE-MESH-MIB", "staticRouteTrafficClass"),
        ("FIRETIDE-MESH-MIB", "staticRouteClientPortIndex"),
        ("FIRETIDE-MESH-MIB", "staticRouteClientVlanNo"),
        ("FIRETIDE-MESH-MIB", "staticRouteEnabled"),
        ("FIRETIDE-MESH-MIB", "staticRouteStatus"),
        ("FIRETIDE-MESH-MIB", "staticRouteNodeIndex"),
        ("FIRETIDE-MESH-MIB", "staticRouteNodeInputPortIndex"),
        ("FIRETIDE-MESH-MIB", "staticRouteNodeOutputPortIndex"),
        ("FIRETIDE-MESH-MIB", "staticRouteNodeInputLogicalIndex"),
        ("FIRETIDE-MESH-MIB", "staticRouteNodeOutputLogicalIndex"),
        ("FIRETIDE-MESH-MIB", "staticRouteNodeEntryStatus"),
        ("FIRETIDE-MESH-MIB", "linkEliminationEntryStatus"),
        ("FIRETIDE-MESH-MIB", "broadcastGroupName"),
        ("FIRETIDE-MESH-MIB", "broadcastGroupEntryStatus"),
        ("FIRETIDE-MESH-MIB", "broadcastMeshEntryStatus"))
)
if mibBuilder.loadTexts:
    firetideTopologyGroup.setStatus("current")

firetideStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22835, 1, 20, 2, 7)
)
firetideStatisticsGroup.setObjects(
      *(("FIRETIDE-MESH-MIB", "nodeFerErrors"),
        ("FIRETIDE-MESH-MIB", "nodeRssi"),
        ("FIRETIDE-MESH-MIB", "nodeNoiseInterference"),
        ("FIRETIDE-MESH-MIB", "nodeRetransmissions"),
        ("FIRETIDE-MESH-MIB", "nodeOpPackets"),
        ("FIRETIDE-MESH-MIB", "nodeInPackets"),
        ("FIRETIDE-MESH-MIB", "nodeWirelessOpPackets"),
        ("FIRETIDE-MESH-MIB", "nodeWirelessInPackets"),
        ("FIRETIDE-MESH-MIB", "nodeRadioErrors"),
        ("FIRETIDE-MESH-MIB", "nodeMacIntfErrors"),
        ("FIRETIDE-MESH-MIB", "nodeMajorSoftwareErrors"),
        ("FIRETIDE-MESH-MIB", "nodeMinorSoftwareErrors"),
        ("FIRETIDE-MESH-MIB", "nodeTemperatureOverRunErrors"),
        ("FIRETIDE-MESH-MIB", "nodeBatteryLowErrors"),
        ("FIRETIDE-MESH-MIB", "nodeStatisticsRowStatus"),
        ("FIRETIDE-MESH-MIB", "portOpPackets"),
        ("FIRETIDE-MESH-MIB", "portInPackets"),
        ("FIRETIDE-MESH-MIB", "portOpBytes"),
        ("FIRETIDE-MESH-MIB", "portInBytes"),
        ("FIRETIDE-MESH-MIB", "portCollidedPackets"),
        ("FIRETIDE-MESH-MIB", "portInDropPackets"),
        ("FIRETIDE-MESH-MIB", "portOutDropPackets"),
        ("FIRETIDE-MESH-MIB", "portRxErrors"),
        ("FIRETIDE-MESH-MIB", "portStatisticsRowStatus"),
        ("FIRETIDE-MESH-MIB", "radioOpBytes"),
        ("FIRETIDE-MESH-MIB", "radioInBytes"),
        ("FIRETIDE-MESH-MIB", "radioDropPackets"),
        ("FIRETIDE-MESH-MIB", "radioRetPackets"),
        ("FIRETIDE-MESH-MIB", "radioOpPackets"),
        ("FIRETIDE-MESH-MIB", "radioInPackets"),
        ("FIRETIDE-MESH-MIB", "radioTxErrors"),
        ("FIRETIDE-MESH-MIB", "radioRxErrors"),
        ("FIRETIDE-MESH-MIB", "radioRetFailPackets"),
        ("FIRETIDE-MESH-MIB", "radioRssi"),
        ("FIRETIDE-MESH-MIB", "radioLinkQuality"),
        ("FIRETIDE-MESH-MIB", "radioNoise"),
        ("FIRETIDE-MESH-MIB", "radioUsedAntenna"),
        ("FIRETIDE-MESH-MIB", "radioStatisticsRowStatus"),
        ("FIRETIDE-MESH-MIB", "nodeToNodeRssi"),
        ("FIRETIDE-MESH-MIB", "nodeToNodeTxRate"),
        ("FIRETIDE-MESH-MIB", "nodeToNodeInPkts"),
        ("FIRETIDE-MESH-MIB", "nodeToNodeOutPkts"),
        ("FIRETIDE-MESH-MIB", "nodeToNodeInBytes"),
        ("FIRETIDE-MESH-MIB", "nodeToNodeOutBytes"),
        ("FIRETIDE-MESH-MIB", "nodeToNodeOutPktsDrp"),
        ("FIRETIDE-MESH-MIB", "nodeToNodeTotalRetries"),
        ("FIRETIDE-MESH-MIB", "nodeToNodeRowStatus"),
        ("FIRETIDE-MESH-MIB", "staticRouteNodeRcvPackets"),
        ("FIRETIDE-MESH-MIB", "staticRouteNodeFwdPackets"),
        ("FIRETIDE-MESH-MIB", "staticRouteNodeStatisticsEntryStatus"))
)
if mibBuilder.loadTexts:
    firetideStatisticsGroup.setStatus("current")


# Notification objects

meshDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 1)
)
meshDown.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "meshNmsIp"))
)
if mibBuilder.loadTexts:
    meshDown.setStatus(
        "current"
    )

meshUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 2)
)
meshUp.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "meshNmsIp"))
)
if mibBuilder.loadTexts:
    meshUp.setStatus(
        "current"
    )

nodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 3)
)
nodeDown.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "nodeIndex"),
        ("FIRETIDE-MESH-MIB", "nodeDisplayName"),
        ("FIRETIDE-MESH-MIB", "nodeSerialNo"))
)
if mibBuilder.loadTexts:
    nodeDown.setStatus(
        "current"
    )

nodeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 4)
)
nodeUp.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "nodeIndex"),
        ("FIRETIDE-MESH-MIB", "nodeDisplayName"),
        ("FIRETIDE-MESH-MIB", "nodeSerialNo"))
)
if mibBuilder.loadTexts:
    nodeUp.setStatus(
        "current"
    )

edgeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 5)
)
edgeDown.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "nodeIndex"),
        ("FIRETIDE-MESH-MIB", "neighborNodeIndex"))
)
if mibBuilder.loadTexts:
    edgeDown.setStatus(
        "current"
    )

edgeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 6)
)
edgeUp.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "nodeIndex"),
        ("FIRETIDE-MESH-MIB", "neighborNodeIndex"))
)
if mibBuilder.loadTexts:
    edgeUp.setStatus(
        "current"
    )

portDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 7)
)
portDown.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "nodeIndex"),
        ("FIRETIDE-MESH-MIB", "portIndex"),
        ("FIRETIDE-MESH-MIB", "portVlanNo"),
        ("FIRETIDE-MESH-MIB", "portGatewayNo"))
)
if mibBuilder.loadTexts:
    portDown.setStatus(
        "current"
    )

portUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 8)
)
portUp.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "nodeIndex"),
        ("FIRETIDE-MESH-MIB", "portIndex"),
        ("FIRETIDE-MESH-MIB", "portVlanNo"),
        ("FIRETIDE-MESH-MIB", "portGatewayNo"))
)
if mibBuilder.loadTexts:
    portUp.setStatus(
        "current"
    )

meshConfigInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 9)
)
meshConfigInconsistent.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "meshConfigComparison"))
)
if mibBuilder.loadTexts:
    meshConfigInconsistent.setStatus(
        "current"
    )

meshConfigConsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 10)
)
meshConfigConsistent.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "meshConfigComparison"))
)
if mibBuilder.loadTexts:
    meshConfigConsistent.setStatus(
        "current"
    )

radioConfigInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 11)
)
radioConfigInconsistent.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "radioConfigComparison"))
)
if mibBuilder.loadTexts:
    radioConfigInconsistent.setStatus(
        "current"
    )

radioConfigConsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 12)
)
radioConfigConsistent.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "radioConfigComparison"))
)
if mibBuilder.loadTexts:
    radioConfigConsistent.setStatus(
        "current"
    )

thermalOverRun = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 13)
)
thermalOverRun.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "nodeIndex"),
        ("FIRETIDE-MESH-MIB", "nodeDisplayName"),
        ("FIRETIDE-MESH-MIB", "nodeSerialNo"))
)
if mibBuilder.loadTexts:
    thermalOverRun.setStatus(
        "current"
    )

thermalOverRunClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 14)
)
thermalOverRunClear.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "nodeIndex"),
        ("FIRETIDE-MESH-MIB", "nodeDisplayName"),
        ("FIRETIDE-MESH-MIB", "nodeSerialNo"))
)
if mibBuilder.loadTexts:
    thermalOverRunClear.setStatus(
        "current"
    )

batteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 15)
)
batteryLow.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "nodeIndex"),
        ("FIRETIDE-MESH-MIB", "nodeDisplayName"),
        ("FIRETIDE-MESH-MIB", "nodeSerialNo"))
)
if mibBuilder.loadTexts:
    batteryLow.setStatus(
        "current"
    )

batteryLowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 16)
)
batteryLowClear.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "nodeIndex"),
        ("FIRETIDE-MESH-MIB", "nodeDisplayName"),
        ("FIRETIDE-MESH-MIB", "nodeSerialNo"))
)
if mibBuilder.loadTexts:
    batteryLowClear.setStatus(
        "current"
    )

meshConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 17)
)
meshConfigError.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "applyErrorString"))
)
if mibBuilder.loadTexts:
    meshConfigError.setStatus(
        "current"
    )

nodeConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 18)
)
nodeConfigError.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "nodeIndex"),
        ("FIRETIDE-MESH-MIB", "nodeSetResultStr"))
)
if mibBuilder.loadTexts:
    nodeConfigError.setStatus(
        "current"
    )

configChangesWithNodesDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 19)
)
configChangesWithNodesDown.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "meshNumNodesDown"))
)
if mibBuilder.loadTexts:
    configChangesWithNodesDown.setStatus(
        "current"
    )

countryCodeNotSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 20)
)
countryCodeNotSet.setObjects(
    ("FIRETIDE-MESH-MIB", "meshIndex")
)
if mibBuilder.loadTexts:
    countryCodeNotSet.setStatus(
        "current"
    )

concurrentModification = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 21)
)
concurrentModification.setObjects(
    ("FIRETIDE-MESH-MIB", "meshIndex")
)
if mibBuilder.loadTexts:
    concurrentModification.setStatus(
        "current"
    )

meshLoginError = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 22)
)
meshLoginError.setObjects(
    ("FIRETIDE-MESH-MIB", "meshLoginErrorMessage")
)
if mibBuilder.loadTexts:
    meshLoginError.setStatus(
        "current"
    )

bridgeLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 23)
)
bridgeLinkDown.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "neighborMeshIndex"),
        ("FIRETIDE-MESH-MIB", "neighborMeshLinkIndex"))
)
if mibBuilder.loadTexts:
    bridgeLinkDown.setStatus(
        "current"
    )

bridgeLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 24)
)
bridgeLinkUp.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "neighborMeshIndex"),
        ("FIRETIDE-MESH-MIB", "neighborMeshLinkIndex"))
)
if mibBuilder.loadTexts:
    bridgeLinkUp.setStatus(
        "current"
    )

operatingFrequencyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 25)
)
operatingFrequencyChanged.setObjects(
    ("FIRETIDE-MESH-MIB", "meshIndex")
)
if mibBuilder.loadTexts:
    operatingFrequencyChanged.setStatus(
        "current"
    )

radarDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 26)
)
radarDetected.setObjects(
    ("FIRETIDE-MESH-MIB", "meshIndex")
)
if mibBuilder.loadTexts:
    radarDetected.setStatus(
        "current"
    )

radioNolChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 27)
)
radioNolChanged.setObjects(
    ("FIRETIDE-MESH-MIB", "meshIndex")
)
if mibBuilder.loadTexts:
    radioNolChanged.setStatus(
        "current"
    )

licenseAboutToExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 28)
)
licenseAboutToExpire.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "nodeIndex"))
)
if mibBuilder.loadTexts:
    licenseAboutToExpire.setStatus(
        "current"
    )

licenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 29)
)
licenseExpired.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "nodeIndex"))
)
if mibBuilder.loadTexts:
    licenseExpired.setStatus(
        "current"
    )

staticRouteDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 30)
)
staticRouteDown.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "staticRouteIndex"))
)
if mibBuilder.loadTexts:
    staticRouteDown.setStatus(
        "current"
    )

staticRouteUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22835, 1, 16, 31)
)
staticRouteUp.setObjects(
      *(("FIRETIDE-MESH-MIB", "meshIndex"),
        ("FIRETIDE-MESH-MIB", "staticRouteIndex"))
)
if mibBuilder.loadTexts:
    staticRouteUp.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

firetideMeshMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22835, 1, 20, 1)
)
firetideMeshMibCompliance.setObjects(
      *(("FIRETIDE-MESH-MIB", "firetideNetworkGroup"),
        ("FIRETIDE-MESH-MIB", "firetideNodeGroup"),
        ("FIRETIDE-MESH-MIB", "firetideRadioGroup"),
        ("FIRETIDE-MESH-MIB", "firetidePortGroup"),
        ("FIRETIDE-MESH-MIB", "firetideSecurityGroup"),
        ("FIRETIDE-MESH-MIB", "firetideTopologyGroup"),
        ("FIRETIDE-MESH-MIB", "firetideStatisticsGroup"))
)
if mibBuilder.loadTexts:
    firetideMeshMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIRETIDE-MESH-MIB",
    **{"RadioProtocol": RadioProtocol,
       "LinkType": LinkType,
       "VerifyOperation": VerifyOperation,
       "NetworkOperation": NetworkOperation,
       "CountryCode": CountryCode,
       "LinkRate": LinkRate,
       "RadioDataRate": RadioDataRate,
       "firetide": firetide,
       "firetideMesh": firetideMesh,
       "firetideNetwork": firetideNetwork,
       "numMesh": numMesh,
       "meshConfigTable": meshConfigTable,
       "meshConfigEntry": meshConfigEntry,
       "meshIndex": meshIndex,
       "meshName": meshName,
       "meshNmsIp": meshNmsIp,
       "meshNmsIpMask": meshNmsIpMask,
       "meshNmsDefaultGateway": meshNmsDefaultGateway,
       "meshStatsCollectInterval": meshStatsCollectInterval,
       "meshNumNodes": meshNumNodes,
       "meshNumNodesDown": meshNumNodesDown,
       "meshNumVlans": meshNumVlans,
       "meshGatewayGroupConfiguredBitMap": meshGatewayGroupConfiguredBitMap,
       "meshMacListSize": meshMacListSize,
       "meshMacFilterType": meshMacFilterType,
       "meshNeighborTableSize": meshNeighborTableSize,
       "rebootMesh": rebootMesh,
       "meshConfigApply": meshConfigApply,
       "applyErrorString": applyErrorString,
       "newMeshIndex": newMeshIndex,
       "verifyMeshwideConfig": verifyMeshwideConfig,
       "meshConfigComparison": meshConfigComparison,
       "verifyRadioConfig": verifyRadioConfig,
       "radioConfigComparison": radioConfigComparison,
       "upgradeMeshSoftware": upgradeMeshSoftware,
       "upgradeSoftwarePath": upgradeSoftwarePath,
       "upgradeSoftwareCompletion": upgradeSoftwareCompletion,
       "importMeshwideConfig": importMeshwideConfig,
       "exportMeshwideConfig": exportMeshwideConfig,
       "meshConfigUpdateNodeIndex": meshConfigUpdateNodeIndex,
       "meshConfigUpdatePath": meshConfigUpdatePath,
       "meshConfigSavedPasswd": meshConfigSavedPasswd,
       "meshConfigGwGrpNameToApply": meshConfigGwGrpNameToApply,
       "meshConfigGwPrimary": meshConfigGwPrimary,
       "meshConfigSavedUserName": meshConfigSavedUserName,
       "meshwidePriorityEnable": meshwidePriorityEnable,
       "meshwideCongestionControlEnable": meshwideCongestionControlEnable,
       "meshReservedMacEnable": meshReservedMacEnable,
       "meshConfigEntryStatus": meshConfigEntryStatus,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanNo": vlanNo,
       "vlanTagged": vlanTagged,
       "vlanStatus": vlanStatus,
       "vlanTrunkTable": vlanTrunkTable,
       "vlanTrunkEntry": vlanTrunkEntry,
       "vlanTrunkOnPort3": vlanTrunkOnPort3,
       "vlanTrunkOnPort4": vlanTrunkOnPort4,
       "vlanTrunkMgmtVlanIdOnPort3": vlanTrunkMgmtVlanIdOnPort3,
       "vlanTrunkMgmtVlanIdOnPort4": vlanTrunkMgmtVlanIdOnPort4,
       "vlanTrunkStatus": vlanTrunkStatus,
       "macListTable": macListTable,
       "macListEntry": macListEntry,
       "macFilterMacAddress": macFilterMacAddress,
       "macFilterEntryStatus": macFilterEntryStatus,
       "bridgeGroupTable": bridgeGroupTable,
       "bridgeGroupEntry": bridgeGroupEntry,
       "bridgeGroupNo": bridgeGroupNo,
       "bridgeGroupName": bridgeGroupName,
       "bridgeGroupRemoteMeshIndex": bridgeGroupRemoteMeshIndex,
       "bridgeGroupNumIfs": bridgeGroupNumIfs,
       "bridgeGroupAesFlag": bridgeGroupAesFlag,
       "bridgeGroupAesKey": bridgeGroupAesKey,
       "bridgeGroupStatus": bridgeGroupStatus,
       "bridgeGroupIfTable": bridgeGroupIfTable,
       "bridgeGroupIfEntry": bridgeGroupIfEntry,
       "bridgeGroupIfNo": bridgeGroupIfNo,
       "bridgeGroupIfNodeIndex": bridgeGroupIfNodeIndex,
       "bridgeGroupIfIp": bridgeGroupIfIp,
       "bridgeGroupIfIpMask": bridgeGroupIfIpMask,
       "bridgeGroupIfDefaultGateway": bridgeGroupIfDefaultGateway,
       "bridgeGroupIfRemoteIp": bridgeGroupIfRemoteIp,
       "bridgeGroupIfPortIndex": bridgeGroupIfPortIndex,
       "bridgeGroupIfStatus": bridgeGroupIfStatus,
       "gatewayServerTable": gatewayServerTable,
       "gatewayServerEntry": gatewayServerEntry,
       "gatewayServerNo": gatewayServerNo,
       "gatewayServerName": gatewayServerName,
       "gatewayServerPriNode": gatewayServerPriNode,
       "gatewayServerNumIfs": gatewayServerNumIfs,
       "gatewayServerAesFlag": gatewayServerAesFlag,
       "gatewayServerAesKey": gatewayServerAesKey,
       "gatewayServerSrvPriIfIp": gatewayServerSrvPriIfIp,
       "gatewayServerSrvIfIpMask": gatewayServerSrvIfIpMask,
       "gatewayServerSrvIfDefaultGateway": gatewayServerSrvIfDefaultGateway,
       "gatewayServerSrvPortIndex": gatewayServerSrvPortIndex,
       "gatewayServerSrvRedundant": gatewayServerSrvRedundant,
       "gatewayServerSecNode": gatewayServerSecNode,
       "gatewayServerSrvSecIfIp": gatewayServerSrvSecIfIp,
       "gatewayServerStatus": gatewayServerStatus,
       "gatewayServerIfTable": gatewayServerIfTable,
       "gatewayServerIfEntry": gatewayServerIfEntry,
       "gatewayServerIfNo": gatewayServerIfNo,
       "gatewayServerIfNodeIndex": gatewayServerIfNodeIndex,
       "gatewayServerIfPortIndex": gatewayServerIfPortIndex,
       "gatewayServerIfIp": gatewayServerIfIp,
       "gatewayServerIfIpMask": gatewayServerIfIpMask,
       "gatewayServerIfDefaultGateway": gatewayServerIfDefaultGateway,
       "gatewayServerIfLinkRate": gatewayServerIfLinkRate,
       "gatewayServerSrvLogicalIndex": gatewayServerSrvLogicalIndex,
       "gatewayServerIfPriLogicalIndex": gatewayServerIfPriLogicalIndex,
       "gatewayServerIfSecLogicalIndex": gatewayServerIfSecLogicalIndex,
       "gatewayServerIfStatus": gatewayServerIfStatus,
       "ethernetDirectTable": ethernetDirectTable,
       "ethernetDirectEntry": ethernetDirectEntry,
       "ethernetRemoteIp": ethernetRemoteIp,
       "ethernetLocalIp": ethernetLocalIp,
       "ethernetTunnelName": ethernetTunnelName,
       "ethernetPortIndex": ethernetPortIndex,
       "ethernetLocalIpMask": ethernetLocalIpMask,
       "ethernetDefaultGateway": ethernetDefaultGateway,
       "ethernetTunnelAesFlag": ethernetTunnelAesFlag,
       "ethernetTunnelAesKey": ethernetTunnelAesKey,
       "ethernetLinkRate": ethernetLinkRate,
       "ethernetLinkLogicalIndex": ethernetLinkLogicalIndex,
       "ethernetDirectEntryStatus": ethernetDirectEntryStatus,
       "multicastGroupTable": multicastGroupTable,
       "multicastGroupEntry": multicastGroupEntry,
       "multicastIp": multicastIp,
       "multicastEntryNodeIndex": multicastEntryNodeIndex,
       "multicastGroupEntryStatus": multicastGroupEntryStatus,
       "firetideNode": firetideNode,
       "nodeTable": nodeTable,
       "nodeEntry": nodeEntry,
       "nodeIndex": nodeIndex,
       "nodeDisplayName": nodeDisplayName,
       "nodeModelNo": nodeModelNo,
       "nodeSubId": nodeSubId,
       "nodeLocationString": nodeLocationString,
       "nodeLocationX": nodeLocationX,
       "nodeLocationY": nodeLocationY,
       "nodeLocationZ": nodeLocationZ,
       "nodeSerialNo": nodeSerialNo,
       "nodeSoftwareVer": nodeSoftwareVer,
       "nodeCountryCode": nodeCountryCode,
       "nodeUpTime": nodeUpTime,
       "nodeLastResetReason": nodeLastResetReason,
       "nodeOperations": nodeOperations,
       "nodeSetResultStr": nodeSetResultStr,
       "nodeQosType": nodeQosType,
       "nodeStatus": nodeStatus,
       "nodeQosTable": nodeQosTable,
       "nodeQosEntry": nodeQosEntry,
       "nodeQosIndex": nodeQosIndex,
       "nodeQosPriority": nodeQosPriority,
       "nodeQosStatus": nodeQosStatus,
       "firetideRadio": firetideRadio,
       "meshRadioTable": meshRadioTable,
       "meshRadioEntry": meshRadioEntry,
       "meshEssId": meshEssId,
       "meshCountryCode": meshCountryCode,
       "meshPrimaryRadioProtocol": meshPrimaryRadioProtocol,
       "meshMaxPrimaryChannelIndex": meshMaxPrimaryChannelIndex,
       "meshPrimaryRadioChannelNum": meshPrimaryRadioChannelNum,
       "meshRadioRange": meshRadioRange,
       "meshRadioRtsCtsEnable": meshRadioRtsCtsEnable,
       "meshRssiThreshold": meshRssiThreshold,
       "meshRssiHysteresisDelta": meshRssiHysteresisDelta,
       "meshAccessPointAutoDiscover": meshAccessPointAutoDiscover,
       "meshEssidEncrypt": meshEssidEncrypt,
       "meshRadioDataRate": meshRadioDataRate,
       "meshRadioEntryStatus": meshRadioEntryStatus,
       "radioChannelTable": radioChannelTable,
       "radioChannelEntry": radioChannelEntry,
       "radioChannelProtocol": radioChannelProtocol,
       "radioChannelIndex": radioChannelIndex,
       "radioChannelNum": radioChannelNum,
       "radioChannelMinPower": radioChannelMinPower,
       "radioChannelMaxPower": radioChannelMaxPower,
       "radioChannelDfsEnabled": radioChannelDfsEnabled,
       "radioChannelLicensed": radioChannelLicensed,
       "radioChannelStatus": radioChannelStatus,
       "radioTable": radioTable,
       "radioEntry": radioEntry,
       "radioIndex": radioIndex,
       "radioMacAddress": radioMacAddress,
       "radioSerialNo": radioSerialNo,
       "radioTransmitPower": radioTransmitPower,
       "radioAntennaType": radioAntennaType,
       "radioLogicalIndex": radioLogicalIndex,
       "radioStatus": radioStatus,
       "accessPointTable": accessPointTable,
       "accessPointEntry": accessPointEntry,
       "accessPointIp": accessPointIp,
       "accessPointName": accessPointName,
       "accessPointUrl": accessPointUrl,
       "accessPointManual": accessPointManual,
       "accessPointStatus": accessPointStatus,
       "firetidePort": firetidePort,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "portMacAddress": portMacAddress,
       "portEnable": portEnable,
       "portPriority": portPriority,
       "portAutoNegotiate": portAutoNegotiate,
       "portSpeed": portSpeed,
       "portDuplex": portDuplex,
       "portVlanNo": portVlanNo,
       "portGatewayNo": portGatewayNo,
       "portStatus": portStatus,
       "firetideSecurity": firetideSecurity,
       "meshSecurityTable": meshSecurityTable,
       "meshSecurityEntry": meshSecurityEntry,
       "meshWepFlag": meshWepFlag,
       "meshWepKey": meshWepKey,
       "meshAesFlag": meshAesFlag,
       "meshAesKey": meshAesKey,
       "meshRwUser": meshRwUser,
       "meshRwPasswd": meshRwPasswd,
       "meshRoUser": meshRoUser,
       "meshRoPasswd": meshRoPasswd,
       "meshWirelessSecurityFlag": meshWirelessSecurityFlag,
       "meshWirelessSecurityKey": meshWirelessSecurityKey,
       "meshEndToEndSecurityFlag": meshEndToEndSecurityFlag,
       "meshEndToEndSecurityKey": meshEndToEndSecurityKey,
       "meshRwOldPasswd": meshRwOldPasswd,
       "meshRoOldPasswd": meshRoOldPasswd,
       "meshSecurityStatus": meshSecurityStatus,
       "meshLoginOperation": meshLoginOperation,
       "meshLoginIp": meshLoginIp,
       "meshLoginUserName": meshLoginUserName,
       "meshLoginUserPassword": meshLoginUserPassword,
       "meshLoginPreload": meshLoginPreload,
       "meshLoginIndex": meshLoginIndex,
       "meshLoginErrorMessage": meshLoginErrorMessage,
       "meshRemoteUserTable": meshRemoteUserTable,
       "meshRemoteUserEntry": meshRemoteUserEntry,
       "meshRootUserName": meshRootUserName,
       "meshRootPassword": meshRootPassword,
       "meshRootOldPassword": meshRootOldPassword,
       "meshSupportUserName": meshSupportUserName,
       "meshSupportPassword": meshSupportPassword,
       "meshSupportOldPassword": meshSupportOldPassword,
       "meshSupportUserEnabled": meshSupportUserEnabled,
       "meshCliUserName": meshCliUserName,
       "meshCliPassword": meshCliPassword,
       "meshCliOldPassword": meshCliOldPassword,
       "meshCliUserEnabled": meshCliUserEnabled,
       "meshTelnetLoginEnabled": meshTelnetLoginEnabled,
       "meshRemoteUserStatus": meshRemoteUserStatus,
       "firetideTopology": firetideTopology,
       "networkTopologyTable": networkTopologyTable,
       "networkTopologyEntry": networkTopologyEntry,
       "neighborMeshIndex": neighborMeshIndex,
       "neighborMeshLinkIndex": neighborMeshLinkIndex,
       "neighborMeshLinkType": neighborMeshLinkType,
       "neighborMeshLinkStatus": neighborMeshLinkStatus,
       "meshTopologyTable": meshTopologyTable,
       "meshTopologyEntry": meshTopologyEntry,
       "neighborNodeIndex": neighborNodeIndex,
       "neighborNodeLinkIndex": neighborNodeLinkIndex,
       "neighborNodeLinkType": neighborNodeLinkType,
       "neighborNodeLinkStatus": neighborNodeLinkStatus,
       "staticRouteTable": staticRouteTable,
       "staticRouteEntry": staticRouteEntry,
       "staticRouteIndex": staticRouteIndex,
       "staticRouteLength": staticRouteLength,
       "staticRouteTrafficClass": staticRouteTrafficClass,
       "staticRouteClientPortIndex": staticRouteClientPortIndex,
       "staticRouteClientVlanNo": staticRouteClientVlanNo,
       "staticRouteEnabled": staticRouteEnabled,
       "staticRouteStatus": staticRouteStatus,
       "staticRouteNodeTable": staticRouteNodeTable,
       "staticRouteNodeEntry": staticRouteNodeEntry,
       "staticRouteNodeEntryIndex": staticRouteNodeEntryIndex,
       "staticRouteNodeIndex": staticRouteNodeIndex,
       "staticRouteNodeInputPortIndex": staticRouteNodeInputPortIndex,
       "staticRouteNodeOutputPortIndex": staticRouteNodeOutputPortIndex,
       "staticRouteNodeInputLogicalIndex": staticRouteNodeInputLogicalIndex,
       "staticRouteNodeOutputLogicalIndex": staticRouteNodeOutputLogicalIndex,
       "staticRouteNodeEntryStatus": staticRouteNodeEntryStatus,
       "linkEliminationTable": linkEliminationTable,
       "linkEliminationEntry": linkEliminationEntry,
       "linkEliminationNodeIndex": linkEliminationNodeIndex,
       "linkEliminationEntryStatus": linkEliminationEntryStatus,
       "broadcastGroupTable": broadcastGroupTable,
       "broadcastGroupEntry": broadcastGroupEntry,
       "broadcastGroupIndex": broadcastGroupIndex,
       "broadcastGroupName": broadcastGroupName,
       "broadcastGroupEntryStatus": broadcastGroupEntryStatus,
       "broadcastMeshTable": broadcastMeshTable,
       "broadcastMeshEntry": broadcastMeshEntry,
       "broadcastMeshIndex": broadcastMeshIndex,
       "broadcastMeshEntryStatus": broadcastMeshEntryStatus,
       "firetideStatistics": firetideStatistics,
       "nodeStatisticsTable": nodeStatisticsTable,
       "nodeStatisticsEntry": nodeStatisticsEntry,
       "nodeFerErrors": nodeFerErrors,
       "nodeRssi": nodeRssi,
       "nodeNoiseInterference": nodeNoiseInterference,
       "nodeRetransmissions": nodeRetransmissions,
       "nodeOpPackets": nodeOpPackets,
       "nodeInPackets": nodeInPackets,
       "nodeWirelessOpPackets": nodeWirelessOpPackets,
       "nodeWirelessInPackets": nodeWirelessInPackets,
       "nodeRadioErrors": nodeRadioErrors,
       "nodeMacIntfErrors": nodeMacIntfErrors,
       "nodeMajorSoftwareErrors": nodeMajorSoftwareErrors,
       "nodeMinorSoftwareErrors": nodeMinorSoftwareErrors,
       "nodeTemperatureOverRunErrors": nodeTemperatureOverRunErrors,
       "nodeBatteryLowErrors": nodeBatteryLowErrors,
       "nodeStatisticsRowStatus": nodeStatisticsRowStatus,
       "portStatisticsTable": portStatisticsTable,
       "portStatisticsEntry": portStatisticsEntry,
       "portOpPackets": portOpPackets,
       "portInPackets": portInPackets,
       "portOpBytes": portOpBytes,
       "portInBytes": portInBytes,
       "portCollidedPackets": portCollidedPackets,
       "portInDropPackets": portInDropPackets,
       "portOutDropPackets": portOutDropPackets,
       "portRxErrors": portRxErrors,
       "portStatisticsRowStatus": portStatisticsRowStatus,
       "radioStatisticsTable": radioStatisticsTable,
       "radioStatisticsEntry": radioStatisticsEntry,
       "radioOpBytes": radioOpBytes,
       "radioInBytes": radioInBytes,
       "radioDropPackets": radioDropPackets,
       "radioRetPackets": radioRetPackets,
       "radioOpPackets": radioOpPackets,
       "radioInPackets": radioInPackets,
       "radioTxErrors": radioTxErrors,
       "radioRxErrors": radioRxErrors,
       "radioRetFailPackets": radioRetFailPackets,
       "radioRssi": radioRssi,
       "radioLinkQuality": radioLinkQuality,
       "radioNoise": radioNoise,
       "radioUsedAntenna": radioUsedAntenna,
       "radioStatisticsRowStatus": radioStatisticsRowStatus,
       "nodeToNodeStatisticsTable": nodeToNodeStatisticsTable,
       "nodeToNodeStatisticsEntry": nodeToNodeStatisticsEntry,
       "nodeToNodeDestIndex": nodeToNodeDestIndex,
       "nodeToNodeRssi": nodeToNodeRssi,
       "nodeToNodeTxRate": nodeToNodeTxRate,
       "nodeToNodeInPkts": nodeToNodeInPkts,
       "nodeToNodeOutPkts": nodeToNodeOutPkts,
       "nodeToNodeInBytes": nodeToNodeInBytes,
       "nodeToNodeOutBytes": nodeToNodeOutBytes,
       "nodeToNodeOutPktsDrp": nodeToNodeOutPktsDrp,
       "nodeToNodeTotalRetries": nodeToNodeTotalRetries,
       "nodeToNodeRowStatus": nodeToNodeRowStatus,
       "staticRouteNodeStatisticsTable": staticRouteNodeStatisticsTable,
       "staticRouteNodeStatisticsEntry": staticRouteNodeStatisticsEntry,
       "staticRouteNodeRcvPackets": staticRouteNodeRcvPackets,
       "staticRouteNodeFwdPackets": staticRouteNodeFwdPackets,
       "staticRouteNodeStatisticsEntryStatus": staticRouteNodeStatisticsEntryStatus,
       "firetideTrap": firetideTrap,
       "meshDown": meshDown,
       "meshUp": meshUp,
       "nodeDown": nodeDown,
       "nodeUp": nodeUp,
       "edgeDown": edgeDown,
       "edgeUp": edgeUp,
       "portDown": portDown,
       "portUp": portUp,
       "meshConfigInconsistent": meshConfigInconsistent,
       "meshConfigConsistent": meshConfigConsistent,
       "radioConfigInconsistent": radioConfigInconsistent,
       "radioConfigConsistent": radioConfigConsistent,
       "thermalOverRun": thermalOverRun,
       "thermalOverRunClear": thermalOverRunClear,
       "batteryLow": batteryLow,
       "batteryLowClear": batteryLowClear,
       "meshConfigError": meshConfigError,
       "nodeConfigError": nodeConfigError,
       "configChangesWithNodesDown": configChangesWithNodesDown,
       "countryCodeNotSet": countryCodeNotSet,
       "concurrentModification": concurrentModification,
       "meshLoginError": meshLoginError,
       "bridgeLinkDown": bridgeLinkDown,
       "bridgeLinkUp": bridgeLinkUp,
       "operatingFrequencyChanged": operatingFrequencyChanged,
       "radarDetected": radarDetected,
       "radioNolChanged": radioNolChanged,
       "licenseAboutToExpire": licenseAboutToExpire,
       "licenseExpired": licenseExpired,
       "staticRouteDown": staticRouteDown,
       "staticRouteUp": staticRouteUp,
       "firetideMeshMibConformance": firetideMeshMibConformance,
       "firetideMeshMibCompliance": firetideMeshMibCompliance,
       "firetideMeshMibGroups": firetideMeshMibGroups,
       "firetideNetworkGroup": firetideNetworkGroup,
       "firetideNodeGroup": firetideNodeGroup,
       "firetideRadioGroup": firetideRadioGroup,
       "firetidePortGroup": firetidePortGroup,
       "firetideSecurityGroup": firetideSecurityGroup,
       "firetideTopologyGroup": firetideTopologyGroup,
       "firetideStatisticsGroup": firetideStatisticsGroup}
)
